from __future__ import annotations

import json
import os
import time
from abc import ABC, abstractmethod

from .models import Match, Requirement

DISCRIMINATOR_SYSTEM = (
    "Du bist Experte für BSI IT-Grundschutz und Grundschutz++. "
    "Deine Aufgabe: Minimiere ein vorgeschlagenes GS-Anforderungs-Set, sodass es die GS++-Anforderung "
    "vollständig beschreibt — aber ohne redundante oder irrelevante Anforderungen. "
    "Gehe davon aus, dass das vorliegende Set vollständig ist (nichts fehlt), aber möglicherweise zu groß ist. "
    "Leitlinien:"
    "- Analysiere zuerst die GS++-Anforderung: Welche Kernaspekte muss das Set abdecken?"
    "- Prüfe dann jede GS-Anforderung: Welchen einzigartigen Beitrag leistet sie zur Abdeckung?"
    "- Behalte eine GS-Anforderung (keep), wenn sie einen Aspekt abdeckt, der ohne sie verloren ginge."
    "- Entferne eine GS-Anforderung (remove), wenn ihr Beitrag bereits durch andere GS-Anforderungen im Set abgedeckt ist."
    "- Das minimale Set muss die GS++-Anforderung noch vollständig beschreiben."
    "- Im Zweifelsfall: behalte lieber eine Anforderung zu viel als eine zu wenig."
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

## Aufgabe: Minimales Überdeckungs-Set finden

1. Identifiziere die **Kernaspekte** der GS++-Anforderung.
2. Prüfe für jede GS-Anforderung: Deckt sie einen Aspekt ab, den **keine andere** GS-Anforderung im Set abdeckt?
3. Entscheide:
   - **keep**: Diese GS-Anforderung ist notwendig — ohne sie geht ein Aspekt der GS++-Anforderung verloren.
   - **remove**: Diese GS-Anforderung ist redundant — ihr Beitrag wird bereits durch andere GS-Anforderungen im Set abgedeckt.

Wichtig: Das verbleibende Set muss die GS++-Anforderung noch vollständig beschreiben.
Im Zweifelsfall: behalte lieber eine Anforderung zu viel.

# Entscheidung

Antworte ausschließlich als JSON mit dem vorgegebenen Schema.
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

        for attempt in range(3):
            resp = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=DISCRIMINATOR_SYSTEM,
                tools=[tool],
                tool_choice={"type": "tool", "name": "discriminate_mapping"},
                messages=[{"role": "user", "content": user_prompt}],
            )
            for block in resp.content:
                if getattr(block, "type", None) == "tool_use" and block.name == "discriminate_mapping":
                    payload = block.input
                    results: dict[str, tuple[str, str]] = {}
                    for item in payload.get("candidate_decisions", []):
                        gs_id = item.get("gs_id", "")
                        if gs_id:
                            results[gs_id] = (item.get("decision", "remove"), item.get("reasoning", ""))
                    return results
            time.sleep(1 + attempt)

        raise RuntimeError(f"AnthropicDiscriminator: no tool_use block for {match.gspp_id}")


class OpenAIDiscriminator(Discriminator):
    """Discriminator using OpenAI's GPT model."""

    def __init__(self, model: str = "gpt-4o-2024-11-20") -> None:
        from openai import OpenAI

        self.model = model
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def _supports_reasoning_effort(self) -> bool:
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

        for attempt in range(3):
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
                        # Use explicit thinking budget when a reasoning-capable model is selected.
                        request_kwargs["reasoning_effort"] = "high"

                    try:
                        resp = self.client.chat.completions.create(**request_kwargs)
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

                        # Try next fallback model if current one is unavailable.
                        if "model_not_found" in err or "does not exist" in err:
                            last_error = e
                            continue

                        raise

                if resp is None:
                    if last_error is not None:
                        raise last_error
                    raise RuntimeError("OpenAIDiscriminator: no response from model candidates")

                content = resp.choices[0].message.content or "{}"
                payload = json.loads(content)
                results: dict[str, tuple[str, str]] = {}
                for item in payload.get("candidate_decisions", []):
                    gs_id = item.get("gs_id", "")
                    if gs_id:
                        results[gs_id] = (item.get("decision", "remove"), item.get("reasoning", ""))
                return results
            except Exception as e:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)

        raise RuntimeError("unreachable")


def make_discriminator(model: str) -> Discriminator:
    """Factory function to create a discriminator instance."""
    if model.startswith("claude"):
        return AnthropicDiscriminator(model)
    elif model.startswith("gpt"):
        return OpenAIDiscriminator(model)
    else:
        raise ValueError(f"Unknown discriminator model: {model}")
