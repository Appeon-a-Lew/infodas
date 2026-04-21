from __future__ import annotations

import json
import os
import time
from abc import ABC, abstractmethod

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


def make_judge(model: str) -> Judge:
    m = model.lower()
    if m.startswith("claude") or m.startswith("anthropic"):
        return AnthropicJudge(model=model)
    if m.startswith("gpt") or m.startswith("o1") or m.startswith("o3") or m.startswith("o4") or m.startswith("openai"):
        return OpenAIJudge(model=model)
    raise ValueError(f"Unknown model family for: {model}")
