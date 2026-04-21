from __future__ import annotations

import json
import os
import time
from abc import ABC, abstractmethod
from collections import defaultdict

from .models import Match, Requirement

SYSTEM_PROMPT = (
    "Du bist Experte für BSI IT-Grundschutz und Grundschutz++. "
    "Deine Aufgabe: bewerte, ob eine Grundschutz++-Anforderung durch eine oder mehrere "
    "klassische IT-Grundschutz-Anforderungen (Basis/Standard) inhaltlich abgedeckt wird. "
    "Sei präzise: nur echte inhaltliche Übereinstimmungen zählen als Match. "
    "Wenn keine Kandidatin wirklich passt, ist das Ergebnis 'keine'."
)

USER_TEMPLATE = """\
# Grundschutz++-Anforderung

**ID:** {gspp_id}
**Titel:** {gspp_title}
**Text:**
{gspp_text}

# Kandidaten aus IT-Grundschutz-Kompendium 2023

{candidates}

# Aufgabe

Wähle aus den Kandidaten diejenigen GS-Anforderungen, die die GS++-Anforderung inhaltlich abdecken.
- coverage="voll": alle Aspekte der GS++-Anforderung sind abgedeckt.
- coverage="teilweise": Teile der Anforderung sind abgedeckt, andere fehlen. Beschreibe in gap_notes was fehlt.
- coverage="keine": kein Kandidat passt inhaltlich. gs_ids = [].

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
        )

    @staticmethod
    def _to_match(gspp_id: str, payload: dict) -> Match:
        return Match(
            gspp_id=gspp_id,
            gs_candidates=list(payload.get("gs_ids") or []),
            confidence=float(payload.get("confidence") or 0.0),
            coverage=payload.get("coverage") or "keine",
            rationale=payload.get("rationale") or "",
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
                    return self._to_match(gspp.id, block.input)
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
                return self._to_match(gspp.id, json.loads(content))
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
    gap_notes: list[str] = []
    coverage_score = 0

    for match, model_name in zip(matches, model_names, strict=True):
        if match.gspp_id != gspp_id:
            raise ValueError("cannot combine matches from different GS++ requirements")
        coverage_score += {"keine": 0, "teilweise": 1, "voll": 2}.get(match.coverage, 0)
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

    rationale = "\n".join([rationale_header, *rationales]).strip()
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
