from __future__ import annotations

import json
import os
import time
from abc import ABC, abstractmethod
from collections import defaultdict

from .models import Match, Requirement

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

    @staticmethod
    def _to_match(gspp_id: str, payload: dict, valid_gs_ids: set[str] | None = None) -> Match:
        """Convert payload to Match with optional validation."""
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
        for attempt in range(3):
            resp = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                tools=[tool],
                tool_choice={"type": "tool", "name": "report_mapping"},
                messages=[{"role": "user", "content": self._build_user(gspp, candidates)}],
            )
            for block in resp.content:
                if getattr(block, "type", None) == "tool_use" and block.name == "report_mapping":
                    return self._to_match(gspp.id, block.input, valid_gs_ids)
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
        for attempt in range(3):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": self._build_user(gspp, candidates)},
                    ],
                    response_format={"type": "json_schema", "json_schema": schema},
                )
                content = resp.choices[0].message.content or "{}"
                return self._to_match(gspp.id, json.loads(content), valid_gs_ids)
            except Exception as e:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)
        raise RuntimeError("unreachable")


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
    if m.startswith("claude") or m.startswith("anthropic"):
        return AnthropicJudge(model=model)
    if m.startswith("gpt") or m.startswith("o1") or m.startswith("o3") or m.startswith("o4") or m.startswith("openai"):
        return OpenAIJudge(model=model)
    raise ValueError(f"Unknown model family for: {model}")


def make_combined_judge(models: list[str]) -> Judge:
    judges = [make_judge(model) for model in models]
    if len(judges) == 1:
        return judges[0]
    return CombinedJudge(judges)
