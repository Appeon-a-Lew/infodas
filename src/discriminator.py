from __future__ import annotations

import json
import os
import time
from abc import ABC, abstractmethod

from .judge import _cache_get, _cache_key, _cache_put
from .models import Match, Requirement
from .rate_limit import estimate_tokens, get_limiter


def _is_retryable(exc: Exception) -> bool:
    try:
        import openai
    except Exception:
        openai = None
    if openai is not None:
        if isinstance(exc, (openai.APITimeoutError, openai.APIConnectionError, openai.RateLimitError)):
            return True
        if isinstance(exc, openai.APIStatusError):
            return exc.status_code in (408, 409, 429, 500, 502, 503, 504, 524)
    try:
        import anthropic
    except Exception:
        anthropic = None
    if anthropic is not None:
        if isinstance(exc, (anthropic.APITimeoutError, anthropic.APIConnectionError, anthropic.RateLimitError)):
            return True
        if isinstance(exc, anthropic.APIStatusError):
            return getattr(exc, "status_code", 0) in (408, 409, 429, 500, 502, 503, 504, 524)
    name = type(exc).__name__.lower()
    return "timeout" in name or "connection" in name or "rate" in name


def _retry_after_seconds(exc: Exception) -> float | None:
    resp = getattr(exc, "response", None)
    headers = getattr(resp, "headers", None) if resp is not None else None
    if not headers:
        return None
    val = headers.get("retry-after") or headers.get("Retry-After")
    if not val:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def _backoff(attempt: int, exc: Exception | None = None) -> float:
    if exc is not None:
        ra = _retry_after_seconds(exc)
        if ra is not None:
            return min(60.0, max(1.0, ra))
    return min(30.0, 2 ** (attempt - 1))

DISCRIMINATOR_SYSTEM = (
    "Du bist ein Experte für Textanalyse. "
    "Deine Aufgabe: Prüfe, ob eine Menge von Kandidat-Texten gemeinsam den Zieltext vollständig abdecken. "
    "Erstelle ein MINIMALES Set an Kandidaten, das alle wesentlichen Aspekte des Zieltexts abdeckt. Entferne alle redundanten oder überflüssigen Kandidaten.\n\n"
    "ARBEITSSCHRITTE:\n"
    "1. Extrahiere die KERNASPEKTE des Zieltexts (max. 3-5 Punkte).\n"
    "2. Für jeden Kandidaten prüfe:\n"
    "   - Deckt er einen Aspekt ab, den kein anderer Kandidat abdeckt?\n"
    "   - Ist er der BESTE/Beste Kandidat für diesen Aspekt?\n"
    "3. Entscheidung:\n"
    "   - keep: NOTWENDIG - ohne diesen Kandidaten geht ein Kernaspekt verloren\n"
    "   - remove: REDUNDANT - alle seine Aspekte werden durch bessere/andere Kandidaten abgedeckt\n\n"
    "AGGRESSIVE DEDUPLIKATIONS-REGELN:\n"
    "- Wenn 2+ Kandidaten denselben Aspekt abdecken: behalte nur den SPEZIFISCHSTEN, entferne den Rest.\n"
    "- Allgemeine Kandidaten sind oft redundant zu spezifischen.\n"
    "- Wenn ein Kandidat nur einen Teilaspekt abdeckt, der schon durch umfassendere Kandidaten abgedeckt ist: REMOVE.\n"
    "- Das Ziel ist ein MINIMALES Set - je weniger Kandidaten, desto besser.\n"
    "- Bei Unsicherheit: Bevorzuge 'remove' - nur 'keep', wenn wirklich notwendig.\n\n"
    "VALIDIERUNG:\n"
    "- Nach dem Entfernen müssen ALLE Kernaspekte noch durch 'keep'-Kandidaten abgedeckt sein.\n"
    "- Wenn ein Kernaspekt verloren geht, muss der entsprechende Kandidat 'keep' sein."
)

DISCRIMINATOR_USER_TEMPLATE = """\
# Set-Minimierung

## GS++-Anforderung (zu beschreiben)

**ID:** {gspp_id} — {gspp_title}
**Text:**
{gspp_text}

## Aktuelles GS-Kandidaten-Set

Dieses Set wurde vorgeschlagen und gilt als vollständig (alle relevanten Aspekte sind abgedeckt).
Es ist jedoch möglicherweise zu groß und enthält redundante Anforderungen:

{gs_details}

**Coverage-Level des Gesamt-Sets:** {coverage}
**Confidence-Score:** {confidence:.2f}

**Begründung des Gesamt-Mappings:**
{rationale}

{gap_section}

## Analyse-Vorlage (für interne Analyse)

Kernaspekte der GS++-Anforderung:
1. [Aspekt 1]
2. [Aspekt 2]
...

Zuordnung der GS-Anforderungen zu Kernaspekten:
- GS_ID_1: deckt Aspekt 1, 2 ab
- GS_ID_2: deckt Aspekt 1 ab (auch durch GS_ID_1 abgedeckt) → redundant?
...

## Aufgabe: Minimales Überdeckungs-Set finden

Für JEDE GS-Anforderung im Set:
1. Identifiziere ihre einzigartigen Beiträge (Aspekte, die sie abdeckt)
2. Prüfe: Werden diese Aspekte auch durch andere GS-Anforderungen im Set abgedeckt?
3. Entscheide:
   - **keep**: Diese GS-Anforderung ist NOTWENDIG — ohne sie geht mindestens ein Kernaspekt verloren.
   - **remove**: Diese GS-Anforderung ist REDUNDANT — alle ihre Aspekte werden durch andere abgedeckt.

VALIDIERUNG vor der Entscheidung:
- Wenn du alle 'remove'-Kandidaten entfernst: Sind noch alle Kernaspekte abgedeckt?
- Wenn NEIN: Diese Kandidaten müssen 'keep' sein!

WICHTIG:
- Bevorzuge SPEZIFISCHE gegenüber ALLGEMEINEN Anforderungen.
- Behalte Anforderungen bei, die der einzige Vertreter ihres Bausteins sind.
- Im Zweifelsfall: IMMER 'keep' wählen!

# Entscheidung

Antworte ausschließlich als JSON mit dem vorgegebenen Schema.
Jede GS-Anforderung muss mit 'keep' oder 'remove' und einer konkreten Begründung versehen werden.
"""

DISCRIMINATOR_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "candidate_decisions": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "gs_id": {"type": "string"},
                    "decision": {"type": "string", "enum": ["keep", "remove"]},
                    "reasoning": {"type": "string"},
                },
                "required": ["gs_id", "decision", "reasoning"],
            },
        }
    },
    "required": ["candidate_decisions"],
}


def _format_gs_details(gs_dict: dict[str, Requirement]) -> str:
    """Format GS requirements for display, including full text as entry point."""
    lines = []
    for gs_id in gs_dict.keys():
        req = gs_dict[gs_id]
        lines.append(f"### {gs_id} — {req.title}")
        lines.append(f"_Baustein: {req.baustein}, Level: {req.level}_")
        lines.append(req.text.strip())
        lines.append("")
    return "\n".join(lines) if lines else "Keine"


class Discriminator(ABC):
    """Base class for discrimination models."""

    model: str

    @abstractmethod
    def decide(
        self,
        match: Match,
        gspp_req: Requirement,
        gs_reqs: dict[str, Requirement],
    ) -> dict[str, tuple[str, str]]:
        """
        Decide whether to keep or remove each GS candidate individually.
        Returns: dict mapping gs_id -> (decision: "keep" | "remove", reasoning: str)
        """
        ...

    def _cache_id(self, match: Match, user_prompt: str, extra: str = "") -> str:
        tag = f"{type(self).__name__}::{self.model}"
        ids = ",".join(sorted(match.gs_candidates))
        return _cache_key(tag, DISCRIMINATOR_SYSTEM, user_prompt, match.gspp_id, ids, extra)

    def _payload_to_results(self, payload: dict) -> dict[str, tuple[str, str]]:
        results: dict[str, tuple[str, str]] = {}
        if not isinstance(payload, dict):
            return results
        for item in payload.get("candidate_decisions") or []:
            if not isinstance(item, dict):
                continue
            gs_id = item.get("gs_id", "")
            if gs_id:
                results[gs_id] = (item.get("decision", "remove"), item.get("reasoning", ""))
        return results

    def _build_user_prompt(
        self,
        match: Match,
        gspp_req: Requirement,
        gs_details: str,
    ) -> str:
        gap_section = ""
        if match.gap_notes:
            gap_section = f"\n**Nicht abgedeckte Aspekte (Gap Notes):**\n{match.gap_notes}"

        return DISCRIMINATOR_USER_TEMPLATE.format(
            gspp_id=gspp_req.id,
            gspp_title=gspp_req.title,
            gspp_text=gspp_req.text.strip(),
            coverage=match.coverage,
            confidence=match.confidence,
            gs_details=gs_details,
            rationale=match.rationale or "Keine Begründung verfügbar.",
            gap_section=gap_section,
        )

    def _validate_decisions(
        self,
        decisions: dict[str, tuple[str, str]],
        match: Match,
        max_keep: int = 5,
    ) -> dict[str, tuple[str, str]]:
        """
        Validate and correct discrimination decisions.
        
        Rules:
        1. If all candidates would be removed, keep at least the highest-confidence one
        2. Ensure decisions are only for valid candidate IDs
        3. Default to 'keep' for any missing decisions
        4. If too many 'keep' decisions, force removal of excess (most redundant)
        """
        validated = {}
        
        # Start with all valid candidates
        valid_candidates = set(match.gs_candidates)
        
        # Process existing decisions
        for gs_id in valid_candidates:
            if gs_id in decisions:
                decision, reasoning = decisions[gs_id]
                # Normalize decision
                decision = decision.lower().strip()
                if decision not in ("keep", "remove"):
                    decision = "keep"
                    reasoning += " [AUTO-KORREKTUR: Ungültige Entscheidung, auf 'keep' gesetzt]"
                validated[gs_id] = (decision, reasoning)
            else:
                # Missing decision - default to keep
                validated[gs_id] = ("keep", "Keine Entscheidung erhalten - als notwendig betrachtet")
        
        # Rule: Don't remove all candidates unless original coverage was "keine"
        kept = [gid for gid, (dec, _) in validated.items() if dec == "keep"]
        if not kept and match.coverage != "keine" and valid_candidates:
            # Keep the first candidate (or could use confidence to pick best)
            first_candidate = match.gs_candidates[0]
            validated[first_candidate] = (
                "keep",
                "[AUTO-KORREKTUR: Mindestens ein Kandidat muss erhalten bleiben]"
            )
            kept = [first_candidate]
        
        # Rule: If too many kept, force-remove the ones with weakest reasoning
        if len(kept) > max_keep:
            # Sort by reasoning quality (length is a simple heuristic)
            kept_with_reasoning = [(gid, validated[gid][1]) for gid in kept]
            # Keep the ones with more detailed reasoning (likely more important)
            kept_with_reasoning.sort(key=lambda x: len(x[1]), reverse=True)
            
            to_keep = kept_with_reasoning[:max_keep]
            to_remove = kept_with_reasoning[max_keep:]
            
            for gid, _ in to_remove:
                validated[gid] = (
                    "remove",
                    validated[gid][1] + " [AUTO: Entfernt wegen Überschuss - max {max_keep} Kandidaten]"
                )
        
        return validated


class AnthropicDiscriminator(Discriminator):
    """Discriminator using Anthropic's Claude model."""

    def __init__(self, model: str = "claude-sonnet-4-5") -> None:
        import anthropic

        self.model = model
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    def decide(
        self,
        match: Match,
        gspp_req: Requirement,
        gs_reqs: dict[str, Requirement],
    ) -> dict[str, tuple[str, str]]:
        gs_details = _format_gs_details({gid: gs_reqs[gid] for gid in match.gs_candidates if gid in gs_reqs})
        user_prompt = self._build_user_prompt(match, gspp_req, gs_details)

        tool = {
            "name": "discriminate_mapping",
            "description": "Minimiert das GS-Kandidaten-Set: keep = notwendig für vollständige Abdeckung, remove = redundant.",
            "input_schema": DISCRIMINATOR_SCHEMA,
        }

        ckey = self._cache_id(match, user_prompt)
        cached = _cache_get(ckey)
        if cached is not None:
            import sys as _sys
            print(f"    [cache] disc hit {self.model} {match.gspp_id}", file=_sys.stderr, flush=True)
            return self._validate_decisions(self._payload_to_results(cached), match)

        limiter = get_limiter("ANTHROPIC")
        est_tokens = estimate_tokens(DISCRIMINATOR_SYSTEM, user_prompt)
        max_attempts = 8
        for attempt in range(1, max_attempts + 1):
            try:
                limiter.acquire(est_tokens)
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=1024,
                    system=DISCRIMINATOR_SYSTEM,
                    tools=[tool],
                    tool_choice={"type": "tool", "name": "discriminate_mapping"},
                    messages=[{"role": "user", "content": user_prompt}],
                )
                actual = 0
                u = getattr(resp, "usage", None)
                if u is not None:
                    actual = (getattr(u, "input_tokens", 0) or 0) + (getattr(u, "output_tokens", 0) or 0)
                if actual:
                    limiter.reconcile(actual)
            except Exception as e:
                if not _is_retryable(e) or attempt == max_attempts:
                    raise
                time.sleep(_backoff(attempt, e))
                continue

            for block in resp.content:
                if getattr(block, "type", None) == "tool_use" and block.name == "discriminate_mapping":
                    payload = block.input if isinstance(block.input, dict) else {}
                    _cache_put(ckey, payload)
                    return self._validate_decisions(self._payload_to_results(payload), match)
            time.sleep(_backoff(attempt))

        raise RuntimeError(f"AnthropicDiscriminator: no tool_use block for {match.gspp_id}")


class OpenAIDiscriminator(Discriminator):
    """Discriminator using OpenAI's GPT model."""

    def __init__(self, model: str = "gpt-4o-2024-11-20") -> None:
        from openai import OpenAI

        self.model = model
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def _is_reasoning_model(self) -> bool:
        """Check if model supports reasoning/thinking."""
        model_lower = self.model.lower()
        return (
            "thinking" in model_lower
            or model_lower.startswith("gpt-5")
            or model_lower.startswith("o1")
            or model_lower.startswith("o3")
            or model_lower.startswith("o4")
        )
    
    def _supports_reasoning_effort(self) -> bool:
        """Check if model supports reasoning_effort parameter."""
        model_lower = self.model.lower()
        return "thinking" in model_lower or model_lower.startswith("gpt-5")

    def _candidate_models(self) -> list[str]:
        """Return preferred fallback chain for unavailable model IDs."""
        requested = self.model
        candidates = [requested]

        if requested == "gpt-5.4-thinking":
            candidates.extend(["gpt-5.4-mini", "gpt-5-mini", "gpt-5"])
        elif requested.endswith("-thinking"):
            base = requested[: -len("-thinking")]
            candidates.extend([f"{base}-mini", base])
            if base.startswith("gpt-5"):
                candidates.extend(["gpt-5-mini", "gpt-5"])

        # Keep order, remove duplicates.
        deduped: list[str] = []
        seen: set[str] = set()
        for model in candidates:
            if model not in seen:
                deduped.append(model)
                seen.add(model)
        return deduped

    def decide(
        self,
        match: Match,
        gspp_req: Requirement,
        gs_reqs: dict[str, Requirement],
    ) -> dict[str, tuple[str, str]]:
        gs_details = _format_gs_details({gid: gs_reqs[gid] for gid in match.gs_candidates if gid in gs_reqs})
        user_prompt = self._build_user_prompt(match, gspp_req, gs_details)

        schema = {
            "name": "discrimination_result",
            "strict": True,
            "schema": DISCRIMINATOR_SCHEMA,
        }

        model_candidates = self._candidate_models()
        use_reasoning_effort = self._supports_reasoning_effort()

        ckey = self._cache_id(match, user_prompt, extra=f"reff={use_reasoning_effort}")
        cached = _cache_get(ckey)
        if cached is not None:
            import sys as _sys
            print(f"    [cache] disc hit {self.model} {match.gspp_id}", file=_sys.stderr, flush=True)
            return self._validate_decisions(self._payload_to_results(cached), match)

        limiter = get_limiter("OPENAI")
        est_tokens = estimate_tokens(DISCRIMINATOR_SYSTEM, user_prompt)
        max_attempts = 8
        for attempt in range(1, max_attempts + 1):
            try:
                resp = None
                last_error: Exception | None = None
                for model_name in model_candidates:
                    request_kwargs = {
                        "model": model_name,
                        "max_completion_tokens": 1024,
                        "messages": [
                            {"role": "system", "content": DISCRIMINATOR_SYSTEM},
                            {"role": "user", "content": user_prompt},
                        ],
                        "response_format": {"type": "json_schema", "json_schema": schema},
                    }
                    if use_reasoning_effort:
                        request_kwargs["reasoning_effort"] = "high"

                    try:
                        limiter.acquire(est_tokens)
                        resp = self.client.chat.completions.create(**request_kwargs)
                        actual = getattr(getattr(resp, "usage", None), "total_tokens", 0) or 0
                        if actual:
                            limiter.reconcile(actual)
                        break
                    except Exception as e:
                        err = str(e).lower()
                        if use_reasoning_effort and "reasoning_effort" in err and "unsupported" in err:
                            use_reasoning_effort = False
                            request_kwargs.pop("reasoning_effort", None)
                            try:
                                resp = self.client.chat.completions.create(**request_kwargs)
                                break
                            except Exception as inner_e:
                                e = inner_e
                                err = str(e).lower()

                        if "model_not_found" in err or "does not exist" in err:
                            last_error = e
                            continue

                        raise

                if resp is None:
                    if last_error is not None:
                        raise last_error
                    raise RuntimeError("OpenAIDiscriminator: no response from model candidates")

                content = resp.choices[0].message.content or "{}"
                try:
                    payload = json.loads(content)
                except json.JSONDecodeError as je:
                    if attempt == max_attempts:
                        raise
                    time.sleep(_backoff(attempt))
                    continue
                if not isinstance(payload, dict):
                    if attempt == max_attempts:
                        raise TypeError(f"expected JSON object, got {type(payload).__name__}")
                    time.sleep(_backoff(attempt))
                    continue
                _cache_put(ckey, payload)
                return self._validate_decisions(self._payload_to_results(payload), match)
            except Exception as e:
                if not _is_retryable(e) or attempt == max_attempts:
                    raise
                time.sleep(_backoff(attempt, e))

        raise RuntimeError("unreachable")


class ReasoningDiscriminator(OpenAIDiscriminator):
    """Discriminator that uses reasoning/thinking models with extended thinking time."""
    
    def decide(
        self,
        match: Match,
        gspp_req: Requirement,
        gs_reqs: dict[str, Requirement],
    ) -> dict[str, tuple[str, str]]:
        """Use reasoning model with high effort for better discrimination."""
        # Force use of reasoning capabilities
        original_model = self.model
        
        # If not already a reasoning model, try to use one
        if not self._is_reasoning_model():
            # Try reasoning variants
            reasoning_models = [
                "o3-mini",
                "o1-mini", 
                "gpt-5.4-thinking",
                "gpt-5-thinking",
            ]
            for rm in reasoning_models:
                try:
                    self.model = rm
                    result = super().decide(match, gspp_req, gs_reqs)
                    self.model = original_model
                    return result
                except Exception:
                    continue
            # Fall back to original
            self.model = original_model
        
        return super().decide(match, gspp_req, gs_reqs)


def make_discriminator(model: str, strict: bool = False) -> Discriminator:
    """Factory function to create a discriminator instance.
    
    Args:
        model: Model name (claude-*, gpt-*, o1-*, o3-*)
        strict: If True, use aggressive filtering (max 3 candidates)
    """
    # Use reasoning discriminator for thinking/reasoning models
    if model.startswith(("o1", "o3")) or "thinking" in model.lower():
        return ReasoningDiscriminator(model)
    elif model.startswith("claude"):
        return AnthropicDiscriminator(model)
    elif model.startswith("gpt"):
        return OpenAIDiscriminator(model)
    else:
        raise ValueError(f"Unknown discriminator model: {model}")
