from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from .models import Match, Requirement

COVERAGE_ORDER = ["voll", "teilweise", "keine"]
COVERAGE_LABEL = {
    "voll": "Voll abgedeckt",
    "teilweise": "Teilweise abgedeckt",
    "keine": "Keine Abdeckung",
}


def write_csv(
    path: Path,
    matches: list[Match],
    gspp_index: dict[str, Requirement],
    gs_index: dict[str, Requirement],
    model: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().isoformat(timespec="seconds")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "gspp_id", "gspp_title", "gspp_level",
            "coverage", "confidence",
            "gs_ids", "gs_titles",
            "rationale", "gap_notes",
            "model", "timestamp",
        ])
        for m in matches:
            g = gspp_index.get(m.gspp_id)
            gs_titles = "; ".join(
                f"{gid}: {gs_index[gid].title}" for gid in m.gs_candidates if gid in gs_index
            )
            w.writerow([
                m.gspp_id,
                g.title if g else "",
                g.level if g else "",
                m.coverage,
                f"{m.confidence:.2f}",
                "; ".join(m.gs_candidates),
                gs_titles,
                m.rationale,
                m.gap_notes or "",
                model,
                ts,
            ])


def write_markdown(
    path: Path,
    matches: list[Match],
    gspp_index: dict[str, Requirement],
    gs_index: dict[str, Requirement],
    model: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[Match]] = defaultdict(list)
    for m in matches:
        grouped[m.coverage].append(m)

    total = len(matches)
    lines = [
        f"# GS++ → IT-Grundschutz Mapping (Model: `{model}`)",
        "",
        f"Erzeugt: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"**Gesamt:** {total} GS++-Anforderungen",
        "",
        "| Coverage | Anzahl |",
        "|---|---|",
    ]
    for c in COVERAGE_ORDER:
        lines.append(f"| {COVERAGE_LABEL[c]} | {len(grouped.get(c, []))} |")
    lines.append("")

    for c in COVERAGE_ORDER:
        items = grouped.get(c, [])
        if not items:
            continue
        lines.append(f"## {COVERAGE_LABEL[c]} ({len(items)})")
        lines.append("")
        for m in sorted(items, key=lambda x: x.gspp_id):
            g = gspp_index.get(m.gspp_id)
            title = g.title if g else ""
            lines.append(f"### {m.gspp_id} — {title}")
            lines.append(f"- **Confidence:** {m.confidence:.2f}")
            if m.gs_candidates:
                lines.append("- **Gemappte GS-Anforderungen:**")
                for gid in m.gs_candidates:
                    gs = gs_index.get(gid)
                    if gs:
                        lines.append(f"  - `{gid}` [{gs.level}] {gs.title} — _{gs.baustein}_")
                    else:
                        lines.append(f"  - `{gid}` _(nicht im Korpus gefunden)_")
            if m.rationale:
                lines.append(f"- **Begründung:** {m.rationale}")
            if m.gap_notes:
                lines.append(f"- **Lücken:** {m.gap_notes}")
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_discriminated_csv(
    path: Path,
    matches: list[tuple[Match, dict[str, tuple[str, str]]]],
    gspp_index: dict[str, Requirement],
    gs_index: dict[str, Requirement],
    discriminator_model: str,
    original_model: str,
) -> None:
    """
    Write discriminated matches to CSV, one row per GS candidate.

    Args:
        path: Output CSV file path
        matches: List of (match, per_candidate) where per_candidate maps gs_id -> (decision, reasoning)
        gspp_index: GS++ requirements by ID
        gs_index: GS requirements by ID
        discriminator_model: Name of the discriminator model used
        original_model: Name of the original mapping model
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().isoformat(timespec="seconds")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "gspp_id", "gspp_title", "gspp_level",
            "coverage", "confidence",
            "gs_id", "gs_title", "gs_baustein", "gs_level",
            "rationale", "gap_notes",
            "decision", "discriminator_reasoning",
            "original_model", "discriminator_model", "timestamp",
        ])
        for m, per_candidate in matches:
            g = gspp_index.get(m.gspp_id)
            for gid in m.gs_candidates:
                gs = gs_index.get(gid)
                decision, reasoning = per_candidate.get(gid, ("unknown", ""))
                w.writerow([
                    m.gspp_id,
                    g.title if g else "",
                    g.level if g else "",
                    m.coverage,
                    f"{m.confidence:.2f}",
                    gid,
                    gs.title if gs else "",
                    gs.baustein if gs else "",
                    gs.level if gs else "",
                    m.rationale,
                    m.gap_notes or "",
                    decision,
                    reasoning,
                    original_model,
                    discriminator_model,
                    ts,
                ])
