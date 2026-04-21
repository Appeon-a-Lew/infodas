from dataclasses import dataclass, field
from typing import Literal


@dataclass
class Requirement:
    id: str
    title: str
    text: str
    source: Literal["gspp", "gs"]
    baustein: str | None = None
    level: str | None = None


@dataclass
class Match:
    gspp_id: str
    gs_candidates: list[str] = field(default_factory=list)
    confidence: float = 0.0
    coverage: Literal["voll", "teilweise", "keine"] = "keine"
    rationale: str = ""
    gap_notes: str | None = None
