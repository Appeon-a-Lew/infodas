from __future__ import annotations

import hashlib
import json
import os
import pathlib
import time
from abc import ABC, abstractmethod
from collections import defaultdict

from .models import Match, Requirement
from .rate_limit import estimate_tokens, get_limiter

CACHE_DIR = pathlib.Path(os.environ.get("JUDGE_CACHE_DIR", ".cache/judge"))
CACHE_ENABLED = os.environ.get("JUDGE_CACHE", "1") != "0"

import threading as _threading
_MEM_CACHE: dict[str, dict] = {}
_MEM_LOCK = _threading.Lock()
_MEM_NEG: set[str] = set()  # known-missing keys, avoid stat() repeat
_PRELOADED = False


def _cache_key(*parts: str) -> str:
    h = hashlib.sha256()
    for p in parts:
        h.update(p.encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()


def preload_cache() -> int:
    """Load every cache file into RAM once. Avoids per-lookup disk I/O."""
    global _PRELOADED
    if not CACHE_ENABLED or _PRELOADED:
        return len(_MEM_CACHE)
    if not CACHE_DIR.exists():
        _PRELOADED = True
        return 0
    count = 0
    for f in CACHE_DIR.iterdir():
        if f.suffix != ".json":
            continue
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(data, dict):
            _MEM_CACHE[f.stem] = data
            count += 1
    _PRELOADED = True
    return count


def _cache_get(key: str) -> dict | None:
    if not CACHE_ENABLED:
        return None
    hit = _MEM_CACHE.get(key)
    if hit is not None:
        return hit
    if key in _MEM_NEG:
        return None
    p = CACHE_DIR / f"{key}.json"
    if not p.exists():
        _MEM_NEG.add(key)
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None
    if isinstance(data, dict):
        _MEM_CACHE[key] = data
        return data
    return None


def _cache_put(key: str, payload: dict) -> None:
    if not CACHE_ENABLED or not isinstance(payload, dict):
        return
    with _MEM_LOCK:
        _MEM_CACHE[key] = payload
        _MEM_NEG.discard(key)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    p = CACHE_DIR / f"{key}.json"
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    tmp.replace(p)

SYSTEM_PROMPT = (
    "Du bist ein Experte für Textanalyse. "
    "Deine Aufgabe: Prüfe, ob eine Menge von Kandidat-Texten gemeinsam den Zieltext vollständig abdecken. "
    "Sei präzise: Nur echte inhaltliche Übereinstimmungen zählen als Match. "
    "Wenn kein Kandidat wirklich passt, ist das Ergebnis 'keine'. "
    "Erstelle ein minimales, nicht-redundantes Set von Kandidaten, das alle wesentlichen Aspekte des Zieltexts abdeckt."
)

COVERAGE_CRITERIA = """
Bewerte coverage basierend auf:
1. [ASPEKT-ÜBERDECKUNG] Werden alle Schutzaspekte der GS++-Anforderung adressiert?
2. [DETAILTIEFE] Entspricht die Detaillierung dem GS++-Standard?
3. [DOMAIN-MATCH] Stimmen die technischen Domains überein? (z.B. Netzwerk ≠ Anwendung)
4. [REGLUNGSART] Ist die Art der Regelung vergleichbar? (organisatorisch/technisch)

Coverage-Definitionen:
- "voll": ALLE wesentlichen Aspekte der GS++-Anforderung werden durch die GS-Anforderung(en) abgedeckt. Die GS++-Anforderung könnte allein mit den gemappten GS-Anforderungen umgesetzt werden.
- "teilweise": Einige wesentliche Aspekte werden abgedeckt, aber andere fehlen oder sind unvollständig.
- "keine": Keine inhaltliche Überschneidung oder die Domains sind grundlegend verschieden.
"""

FEW_SHOT_EXAMPLES = """
Beispiel 1 - Korrektes Mapping (Vollständige Abdeckung):
GS++: "GC.6.1.3 Erstellung einer Sicherheitsleitlinie" - Die Institution MUSS eine Leitlinie zur Informationssicherheit erstellen, die Sicherheitsziele und grundlegende Regeln festlegt.
GS-Kandidat: "ISMS.1.A3 Erstellung einer Leitlinie zur Informationssicherheit" [Basis]
→ Ergebnis: coverage="voll", confidence=0.95, gs_ids=["ISMS.1.A3"]
→ Begründung: Beide Anforderungen beschreiben die Pflicht zur Erstellung einer Sicherheitsleitlinie mit identischem Inhalt.

Beispiel 2 - Falsches Mapping (Keine Abdeckung):
GS++: "GC.5.1.2 Festlegung des Schutzbedarfs" - Systematische Einstufung des Schutzbedarfs als 'normal' oder 'hoch'.
GS-Kandidat: "APP.3.3.A1 Sichere Authentisierung" [Standard] - Anforderungen an die Authentisierung in Webanwendungen.
→ Ergebnis: coverage="keine", confidence=0.05, gs_ids=[]
→ Begründung: Schutzbedarfseinstufung (Risikomanagement) und Authentisierung (technische Maßnahme) sind grundlegend verschiedene Domains.

Beispiel 3 - Teilweise Abdeckung:
GS++: "GC.2.1 Festlegung des externen Kontextes" - Analyse gesellschaftlicher, technologischer, ökonomischer Faktoren.
GS-Kandidat: "ORP.5.A1 Identifikation der Rahmenbedingungen" [Basis] - Identifikation gesetzlicher und vertraglicher Rahmenbedingungen.
→ Ergebnis: coverage="teilweise", confidence=0.60, gs_ids=["ORP.5.A1"]
→ Begründung: Rechtliche Rahmenbedingungen werden abgedeckt, aber gesellschaftliche/technologische Faktoren fehlen.
→ Gap Notes: Nicht abgedeckt: gesellschaftliche, ökonomische und technologische Trends außerhalb rechtlicher Vorgaben.
"""

USER_TEMPLATE = """\
# Grundschutz++-Anforderung

**ID:** {gspp_id}
**Titel:** {gspp_title}
**Text:**
{gspp_text}

# Kandidaten aus IT-Grundschutz-Kompendium 2023

{candidates}

# Bewertungskriterien

{coverage_criteria}

# Beispiele

{few_shot_examples}

# Aufgabe

Wähle aus den Kandidaten diejenigen GS-Anforderungen, die die GS++-Anforderung inhaltlich abdecken.

**WICHTIGE REGELN:**
1. Verwende NUR GS-IDs aus der obigen Kandidatenliste. IDs wie "1", "13", "14" ohne Baustein-Präfix sind UNGÜLTIG.
2. Ein gültiger GS-ID hat immer das Format: BAUSTEIN.Anummer (z.B. ISMS.1.A2, ORP.5.A1, APP.3.3.A1)
3. coverage="voll": ALLE wesentlichen Aspekte der GS++-Anforderung werden durch die GS-Anforderung(en) abgedeckt.
4. coverage="teilweise": Einige Aspekte fehlen - beschreibe diese in gap_notes.
5. coverage="keine": Keine inhaltliche Überschneidung - gs_ids muss leer sein.
6. confidence: 0.0-1.0 basierend auf der Sicherheit deiner Entscheidung (nicht immer 0.9!)
7. rationale: Begründung MUSS alle gewählten GS-IDs namentlich erwähnen und die inhaltliche Verbindung erklären.

Antworte ausschließlich als JSON mit dem vorgegebenen Schema.
"""

OUTPUT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "gs_ids": {"type": "array", "items": {"type": "string"}},
        "coverage": {"type": "string", "enum": ["voll", "teilweise", "keine"]},
        "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
        "rationale": {"type": "string"},
        "gap_notes": {"type": "string"},
    },
    "required": ["gs_ids", "coverage", "confidence", "rationale", "gap_notes"],
}


def _format_candidates(candidates: list[Requirement]) -> str:
    lines = []
    for i, r in enumerate(candidates, 1):
        lines.append(f"## [{i}] {r.id} — {r.title}  _(Baustein: {r.baustein}; Level: {r.level})_")
        lines.append(r.text.strip())
        lines.append("")
    return "\n".join(lines)


class Judge(ABC):
    model: str

    @abstractmethod
    def classify(self, gspp: Requirement, candidates: list[Requirement]) -> Match: ...

    def _build_user(self, gspp: Requirement, candidates: list[Requirement]) -> str:
        return USER_TEMPLATE.format(
            gspp_id=gspp.id,
            gspp_title=gspp.title,
            gspp_text=gspp.text,
            candidates=_format_candidates(candidates),
            coverage_criteria=COVERAGE_CRITERIA,
            few_shot_examples=FEW_SHOT_EXAMPLES,
        )

    def _cache_id(self, gspp: Requirement, candidates: list[Requirement], extra: str = "") -> str:
        user = self._build_user(gspp, candidates)
        tag = f"{type(self).__name__}::{self.model}"
        return _cache_key(tag, SYSTEM_PROMPT, user, extra)

    @staticmethod
    def _to_match(gspp_id: str, payload: dict, valid_gs_ids: set[str] | None = None) -> Match:
        """Convert payload to Match with optional validation."""
        if not isinstance(payload, dict):
            payload = {}
        raw_ids = list(payload.get("gs_ids") or [])
        
        # Filter out invalid/hallucinated IDs
        if valid_gs_ids:
            valid_candidates = [gid for gid in raw_ids if gid in valid_gs_ids]
            invalid_ids = [gid for gid in raw_ids if gid not in valid_gs_ids]
        else:
            # Basic format validation: must match pattern like ISMS.1.A2 or SYS.3.2.1.A28
            import re
            valid_pattern = re.compile(r'^[A-Z]+(?:\.\d+)+\.A\d+$')
            valid_candidates = [gid for gid in raw_ids if valid_pattern.match(gid)]
            invalid_ids = [gid for gid in raw_ids if not valid_pattern.match(gid)]
        
        coverage = payload.get("coverage") or "keine"
        rationale = payload.get("rationale") or ""
        
        # Auto-correct coverage if no valid candidates
        if not valid_candidates and coverage != "keine":
            coverage = "keine"
            if rationale:
                rationale += " [AUTO-KORREKTUR: Keine gültigen GS-IDs gefunden]"
        
        # Add validation notes to rationale
        if invalid_ids:
            validation_note = f" [Hinweis: Ignorierte ungültige IDs: {', '.join(invalid_ids)}]"
            rationale = (rationale + validation_note).strip()
        
        # Validate confidence range
        confidence = float(payload.get("confidence") or 0.0)
        confidence = max(0.0, min(1.0, confidence))
        
        # Check if rationale mentions all candidate IDs
        if valid_candidates and rationale:
            missing_mentions = [gid for gid in valid_candidates if gid not in rationale]
            if missing_mentions:
                rationale += f" [Hinweis: GS-IDs {missing_mentions} nicht in Begründung explizit genannt]"
        
        return Match(
            gspp_id=gspp_id,
            gs_candidates=valid_candidates,
            confidence=confidence,
            coverage=coverage,
            rationale=rationale,
            gap_notes=payload.get("gap_notes") or None,
        )


class AnthropicJudge(Judge):
    def __init__(self, model: str = "claude-sonnet-4-5") -> None:
        import anthropic

        self.model = model
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    def classify(self, gspp: Requirement, candidates: list[Requirement]) -> Match:
        tool = {
            "name": "report_mapping",
            "description": "Meldet das Mapping-Ergebnis.",
            "input_schema": OUTPUT_SCHEMA,
        }
        valid_gs_ids = {c.id for c in candidates}
        ckey = self._cache_id(gspp, candidates)
        cached = _cache_get(ckey)
        if cached is not None:
            return self._to_match(gspp.id, cached, valid_gs_ids)
        user_msg = self._build_user(gspp, candidates)
        limiter = get_limiter("ANTHROPIC")
        est_tokens = estimate_tokens(SYSTEM_PROMPT, user_msg)
        for attempt in range(3):
            limiter.acquire(est_tokens)
            resp = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                tools=[tool],
                tool_choice={"type": "tool", "name": "report_mapping"},
                messages=[{"role": "user", "content": user_msg}],
            )
            u = getattr(resp, "usage", None)
            if u is not None:
                actual = (getattr(u, "input_tokens", 0) or 0) + (getattr(u, "output_tokens", 0) or 0)
                if actual:
                    limiter.reconcile(actual)
            for block in resp.content:
                if getattr(block, "type", None) == "tool_use" and block.name == "report_mapping":
                    payload = block.input if isinstance(block.input, dict) else {}
                    _cache_put(ckey, payload)
                    return self._to_match(gspp.id, payload, valid_gs_ids)
            time.sleep(1 + attempt)
        raise RuntimeError(f"AnthropicJudge: no tool_use block for {gspp.id}")


class OpenAIJudge(Judge):
    def __init__(self, model: str = "gpt-4o-2024-11-20") -> None:
        from openai import OpenAI

        self.model = model
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def classify(self, gspp: Requirement, candidates: list[Requirement]) -> Match:
        schema = {
            "name": "mapping_result",
            "strict": True,
            "schema": OUTPUT_SCHEMA,
        }
        valid_gs_ids = {c.id for c in candidates}
        ckey = self._cache_id(gspp, candidates)
        cached = _cache_get(ckey)
        if cached is not None:
            return self._to_match(gspp.id, cached, valid_gs_ids)
        user_msg = self._build_user(gspp, candidates)
        limiter = get_limiter("OPENAI")
        est_tokens = estimate_tokens(SYSTEM_PROMPT, user_msg)
        for attempt in range(3):
            try:
                limiter.acquire(est_tokens)
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_msg},
                    ],
                    response_format={"type": "json_schema", "json_schema": schema},
                )
                actual = getattr(getattr(resp, "usage", None), "total_tokens", 0) or 0
                if actual:
                    limiter.reconcile(actual)
                content = resp.choices[0].message.content or "{}"
                payload = json.loads(content)
                if isinstance(payload, dict):
                    _cache_put(ckey, payload)
                return self._to_match(gspp.id, payload, valid_gs_ids)
            except Exception as e:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)
        raise RuntimeError("unreachable")


class OpenRouterJudge(Judge):
    """Judge via OpenRouter (OpenAI-compatible API). Model names like 'google/gemma-4-26b-a4b-it'."""

    MAX_ATTEMPTS = int(os.environ.get("OPENROUTER_MAX_ATTEMPTS", "6"))
    REQUEST_TIMEOUT = float(os.environ.get("OPENROUTER_TIMEOUT", "180"))

    def __init__(self, model: str, enable_reasoning: bool | None = None) -> None:
        if enable_reasoning is None:
            enable_reasoning = os.environ.get("OPENROUTER_REASONING", "0") == "1"
        from openai import OpenAI

        self.model = model
        self.enable_reasoning = enable_reasoning
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ["OPENROUTER_API_KEY"],
        )
        # Memoized: set to False once we detect the model does not support json_schema.
        self._use_json_schema = True

    @staticmethod
    def _is_retryable(exc: Exception) -> bool:
        """Retry on timeouts, rate limits, and transient 5xx. Don't retry auth/validation errors."""
        import openai
        if isinstance(exc, (openai.APITimeoutError, openai.APIConnectionError, openai.RateLimitError)):
            return True
        if isinstance(exc, openai.APIStatusError):
            return exc.status_code in (408, 409, 429, 500, 502, 503, 504, 524)
        # httpx-level timeouts (shouldn't leak past OpenAI SDK, but be defensive)
        name = type(exc).__name__.lower()
        return "timeout" in name or "connection" in name

    @staticmethod
    def _is_schema_unsupported(exc: Exception) -> bool:
        """Detect 'model doesn't support json_schema' style 400s so we can fall back permanently."""
        import openai
        if isinstance(exc, openai.BadRequestError):
            msg = str(exc).lower()
            return "json_schema" in msg or "response_format" in msg or "structured" in msg
        return False

    def _make_call(self, gspp: Requirement, candidates: list[Requirement], extra_body: dict):
        schema = {"name": "mapping_result", "strict": True, "schema": OUTPUT_SCHEMA}
        if self._use_json_schema:
            return self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": self._build_user(gspp, candidates)},
                ],
                response_format={"type": "json_schema", "json_schema": schema},
                extra_body=extra_body or None,
                timeout=self.REQUEST_TIMEOUT,
            )
        return self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT + " Antworte ausschließlich als gültiges JSON."},
                {"role": "user", "content": self._build_user(gspp, candidates)},
            ],
            response_format={"type": "json_object"},
            extra_body=extra_body or None,
            timeout=self.REQUEST_TIMEOUT,
        )

    def classify(self, gspp: Requirement, candidates: list[Requirement]) -> Match:
        import sys as _sys
        valid_gs_ids = {c.id for c in candidates}
        extra_body: dict = {}
        if self.enable_reasoning:
            extra_body["reasoning"] = {"enabled": True}

        ckey = self._cache_id(gspp, candidates, extra=f"reasoning={self.enable_reasoning}")
        cached = _cache_get(ckey)
        if cached is not None:
            print(f"  [openrouter] cache hit {self.model} {gspp.id}", file=_sys.stderr, flush=True)
            return self._to_match(gspp.id, cached, valid_gs_ids)

        last_exc: Exception | None = None
        for attempt in range(1, self.MAX_ATTEMPTS + 1):
            t0 = time.time()
            mode = "json_schema" if self._use_json_schema else "json_object"
            print(
                f"  [openrouter] {self.model} mode={mode} reasoning={self.enable_reasoning} "
                f"cand={len(candidates)} attempt={attempt}/{self.MAX_ATTEMPTS} ...",
                file=_sys.stderr, flush=True,
            )
            try:
                limiter = get_limiter("OPENROUTER")
                est = estimate_tokens(SYSTEM_PROMPT, self._build_user(gspp, candidates))
                limiter.acquire(est)
                resp = self._make_call(gspp, candidates, extra_body)
                actual = getattr(getattr(resp, "usage", None), "total_tokens", 0) or 0
                if actual:
                    limiter.reconcile(actual)
                content = resp.choices[0].message.content or "{}"
                dt = time.time() - t0
                print(f"  [openrouter] done in {dt:.1f}s", file=_sys.stderr, flush=True)
                try:
                    payload = json.loads(content)
                except json.JSONDecodeError as je:
                    last_exc = je
                    print(f"  [openrouter] invalid JSON: {je}; retrying", file=_sys.stderr, flush=True)
                    backoff = min(30, 2 ** (attempt - 1))
                    time.sleep(backoff)
                    continue
                if not isinstance(payload, dict):
                    last_exc = TypeError(f"expected JSON object, got {type(payload).__name__}")
                    print(
                        f"  [openrouter] payload not object ({type(payload).__name__}); retrying",
                        file=_sys.stderr, flush=True,
                    )
                    backoff = min(30, 2 ** (attempt - 1))
                    time.sleep(backoff)
                    continue
                _cache_put(ckey, payload)
                return self._to_match(gspp.id, payload, valid_gs_ids)

            except Exception as e:
                dt = time.time() - t0
                last_exc = e

                # One-time permanent fallback when model can't do json_schema.
                if self._use_json_schema and self._is_schema_unsupported(e):
                    self._use_json_schema = False
                    print(
                        f"  [openrouter] json_schema unsupported ({e}); switching to json_object permanently",
                        file=_sys.stderr, flush=True,
                    )
                    continue  # don't consume a retry slot

                if not self._is_retryable(e) or attempt == self.MAX_ATTEMPTS:
                    print(
                        f"  [openrouter] giving up after {attempt} attempt(s) ({dt:.1f}s): "
                        f"{type(e).__name__}: {e}",
                        file=_sys.stderr, flush=True,
                    )
                    raise

                # Exponential backoff with jitter, capped at 30s. Honor Retry-After on 429.
                backoff = min(30.0, 2 ** (attempt - 1))
                retry_after = getattr(getattr(e, "response", None), "headers", {}) or {}
                if isinstance(retry_after, dict):
                    ra = retry_after.get("retry-after") or retry_after.get("Retry-After")
                    if ra:
                        try:
                            backoff = max(backoff, float(ra))
                        except ValueError:
                            pass
                import random
                backoff = backoff * (0.75 + 0.5 * random.random())
                print(
                    f"  [openrouter] retryable error after {dt:.1f}s ({type(e).__name__}: {e}); "
                    f"sleeping {backoff:.1f}s",
                    file=_sys.stderr, flush=True,
                )
                time.sleep(backoff)

        raise RuntimeError(f"OpenRouterJudge: exhausted retries: {last_exc}")


class CombinedJudge(Judge):
    def __init__(self, judges: list[Judge]) -> None:
        if not judges:
            raise ValueError("CombinedJudge requires at least one model")
        self.judges = judges
        self.model = "+".join(judge.model for judge in judges)

    def classify(self, gspp: Requirement, candidates: list[Requirement]) -> Match:
        parts = [judge.classify(gspp, candidates) for judge in self.judges]
        return combine_matches(parts, [judge.model for judge in self.judges])


def combine_matches(matches: list[Match], model_names: list[str]) -> Match:
    if not matches:
        raise ValueError("combine_matches requires at least one match")
    if len(matches) != len(model_names):
        raise ValueError("combine_matches requires equally many matches and model names")

    gspp_id = matches[0].gspp_id
    source_count = len(matches)
    candidate_scores: dict[str, float] = defaultdict(float)
    rationales: list[str] = []
    source_summaries: list[str] = []
    gap_notes: list[str] = []
    coverage_score = 0

    for match, model_name in zip(matches, model_names, strict=True):
        if match.gspp_id != gspp_id:
            raise ValueError("cannot combine matches from different GS++ requirements")
        coverage_score += {"keine": 0, "teilweise": 1, "voll": 2}.get(match.coverage, 0)
        selected_ids = ";".join(match.gs_candidates)
        source_summaries.append(
            f"[{model_name}] coverage={match.coverage} confidence={match.confidence:.4f} gs_ids={selected_ids}"
        )
        for gs_id in match.gs_candidates:
            candidate_scores[gs_id] += match.confidence
        if match.rationale:
            rationales.append(f"[{model_name}] {match.rationale}")
        if match.gap_notes:
            gap_notes.append(f"[{model_name}] {match.gap_notes}")

    gs_candidates = [
        gs_id for gs_id, _ in sorted(candidate_scores.items(), key=lambda item: (-item[1], item[0]))
    ]
    if gs_candidates:
        coverage = "voll" if coverage_score == 2 * len(matches) else "teilweise"
        confidence = max(candidate_scores.values()) / source_count
        score_summary = ", ".join(
            f"{gs_id}={candidate_scores[gs_id] / source_count:.2f}" for gs_id in gs_candidates
        )
        rationale_header = f"Gemittelte Kandidatenscores: {score_summary}"
    else:
        coverage = "keine"
        confidence = sum(match.confidence for match in matches) / source_count
        rationale_header = "Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt."

    rationale = "\n".join([
        rationale_header,
        "Model-Entscheidungen:",
        *source_summaries,
        "Model-Begründungen:",
        *rationales,
    ]).strip()
    combined_gap_notes = "\n".join(gap_notes).strip() or None
    return Match(
        gspp_id=gspp_id,
        gs_candidates=gs_candidates,
        confidence=confidence,
        coverage=coverage,
        rationale=rationale,
        gap_notes=combined_gap_notes,
    )


def make_judge(model: str) -> Judge:
    m = model.lower()
    if m.startswith("openrouter:"):
        return OpenRouterJudge(model=model.split(":", 1)[1])
    if m.startswith("claude") or m.startswith("anthropic"):
        return AnthropicJudge(model=model)
    if m.startswith("gpt") or m.startswith("o1") or m.startswith("o3") or m.startswith("o4") or m.startswith("openai"):
        return OpenAIJudge(model=model)
    if "/" in model:
        return OpenRouterJudge(model=model)
    raise ValueError(f"Unknown model family for: {model}")


def make_combined_judge(models: list[str]) -> Judge:
    judges = [make_judge(model) for model in models]
    if len(judges) == 1:
        return judges[0]
    return CombinedJudge(judges)
