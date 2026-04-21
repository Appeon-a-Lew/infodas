from __future__ import annotations

import json
from pathlib import Path

from .models import Requirement


def _walk(node, parent_titles: list[str], out: list[tuple[dict, list[str]]]):
    for c in node.get("controls", []):
        out.append((c, parent_titles))
        _walk(c, parent_titles + [c.get("title", "")], out)
    for g in node.get("groups", []):
        _walk(g, parent_titles + [f"{g.get('id','')} {g.get('title','')}".strip()], out)


def _prose(ctrl: dict) -> str:
    parts = []
    for p in ctrl.get("parts", []):
        label = p.get("name", "part")
        prose = (p.get("prose") or "").strip()
        if prose:
            parts.append(f"[{label}] {prose}")
    return "\n".join(parts)


def _sec_level(ctrl: dict) -> str | None:
    for p in ctrl.get("props", []):
        if p.get("name") == "sec_level":
            return p.get("value")
    return None


def parse(
    json_path: Path | str,
    scope_prefix: str = "GC.",
) -> list[Requirement]:
    catalog = json.loads(Path(json_path).read_text(encoding="utf-8"))["catalog"]
    collected: list[tuple[dict, list[str]]] = []
    _walk(catalog, [], collected)

    out: list[Requirement] = []
    for ctrl, parents in collected:
        cid = ctrl.get("id", "")
        if not cid.startswith(scope_prefix):
            continue
        prose = _prose(ctrl)
        if not prose:
            continue
        context = " / ".join(p for p in parents if p)
        out.append(
            Requirement(
                id=cid,
                title=ctrl.get("title", ""),
                text=f"{context}\n{prose}" if context else prose,
                source="gspp",
                baustein=None,
                level=_sec_level(ctrl),
            )
        )
    return out


if __name__ == "__main__":
    reqs = parse(Path(__file__).resolve().parent.parent / "data" / "gspp.json")
    print(f"parsed {len(reqs)} GS++ controls in scope GC.")
    for r in reqs[:3]:
        print(" -", r.id, "|", r.title)
        print("   text:", r.text[:120].replace("\n", " "), "...")
