from __future__ import annotations

import json
import math
import random

from collections import defaultdict

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



def _tiered_sample_size(category_size: int) -> int:
    if category_size < 10:
        return min(3, category_size)
    if category_size > 50:
        return max(1, math.ceil(category_size * 0.10))
    return max(1, math.ceil(category_size * 0.20))

def _pool_size(n: int) -> int:
    """Return the sample size for a control family of size n."""
    if n < 10:
        return min(3, n)
    elif n < 50:
        return max(1, math.ceil(n * 0.20))
    else:
        return max(1, math.ceil(n * 0.10))


def _control_family(cid: str) -> str:
    """
    Derive the control family from a control ID.
    E.g. 'GC.AC-1.2' → 'GC.AC', 'GC.SC-28' → 'GC.SC'
    Falls back to the full ID if no '-' separator is found.
    """
    parts = cid.split("-", 1)
    return parts[0]



def parse(
    json_path: Path | str,
    scope_prefix: str = "",
    sample_ratio_per_category: float = 0.20,
    random_seed: int | None = None,
) -> list[Requirement]:
    catalog = json.loads(Path(json_path).read_text(encoding="utf-8"))["catalog"]
    collected: list[tuple[dict, list[str]]] = []
    _walk(catalog, [], collected)

    # Build full list of in-scope requirements first
    all_reqs: list[Requirement] = []
    for ctrl, parents in collected:
        cid = ctrl.get("id", "")
        if not cid.startswith(scope_prefix):
            continue
        prose = _prose(ctrl)
        if not prose:
            continue
        context = " / ".join(p for p in parents if p)
        all_reqs.append(
            Requirement(
                id=cid,
                title=ctrl.get("title", ""),
                text=f"{context}\n{prose}" if context else prose,
                source="gspp",
                baustein=None,
                level=_sec_level(ctrl),
            )
        )

    if 0 < sample_ratio_per_category < 1:
        rng = random.Random(random_seed)
        by_category: dict[str, list[Requirement]] = {}
        for req in out:
            category = req.id.split(".", 1)[0]
            by_category.setdefault(category, []).append(req)

        sampled: list[Requirement] = []
        for category in sorted(by_category):
            bucket = by_category[category]
            k = _tiered_sample_size(len(bucket))
            sampled.extend(rng.sample(bucket, k=k))
        out = sampled

    return out


if __name__ == "__main__":
    reqs = parse(Path(__file__).resolve().parent.parent / "data" / "gspp.json")
    print(f"parsed {len(reqs)} GS++ controls")
    for r in reqs[:3]:
        print(" -", r.id, "|", r.title)
        print("   text:", r.text[:120].replace("\n", " "), "...")