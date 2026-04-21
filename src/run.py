from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from . import parse_gs, parse_gspp, report
from .judge import combine_matches, make_judge
from .models import Match
from .shortlist import Shortlister

ROOT = Path(__file__).resolve().parent.parent


def _parse_models(raw_models: list[str] | str) -> list[str]:
    if isinstance(raw_models, str):
        raw_values = [raw_models]
    else:
        raw_values = raw_models

    models: list[str] = []
    for raw_value in raw_values:
        models.extend(model.strip() for model in raw_value.split(",") if model.strip())
    if not models:
        raise ValueError("--model must contain at least one model name")
    return models


def _safe_model_label(models: list[str]) -> str:
    return "+".join(models).replace("/", "_").replace(":", "_").replace(",", "_")


def _parse_manual_match(row: dict[str, str]) -> Match:
    gs_ids = [gs_id.strip() for gs_id in (row.get("gs_ids") or "").split(";") if gs_id.strip()]
    rationale = (row.get("rationale") or "").strip()
    gap_notes = (row.get("gap_notes") or "").strip() or None
    if rationale == "N/A":
        rationale = ""
    if gap_notes == "N/A":
        gap_notes = None
    return Match(
        gspp_id=(row.get("gspp_id") or "").strip(),
        gs_candidates=gs_ids,
        confidence=float(row.get("confidence") or 0.0),
        coverage=((row.get("coverage") or "keine").strip() or "keine"),
        rationale=rationale,
        gap_notes=gap_notes,
    )


def _load_manual_matches(csv_path: Path, allowed_ids: set[str]) -> dict[str, Match]:
    matches: dict[str, Match] = {}
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            gspp_id = (row.get("gspp_id") or "").strip()
            if not gspp_id or gspp_id not in allowed_ids:
                continue
            matches[gspp_id] = _parse_manual_match(row)
    return matches


def main(argv: list[str] | None = None) -> int:
    load_dotenv(ROOT / ".env")
    p = argparse.ArgumentParser(description="Map Grundschutz++ to IT-Grundschutz")
    p.add_argument("--model", nargs="+", default=["claude-sonnet-4-5"],
                   help="one or more models, either space-separated or comma-separated, e.g. --model claude-sonnet-4-5 gpt-5.4-mini")
    p.add_argument("--scope", default="",
                   help="GS++ ID-prefix to include (default: all categories)")
    p.add_argument("--sample-ratio", type=float, default=0.20,
                   help="ratio of GS++ controls sampled per category (default: 0.20 = 20%%, <=0 or >=1 means all)")
    p.add_argument("--seed", type=int, default=42,
                   help="random seed for per-category sampling")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--gs-levels", default="Basis,Standard",
                   help="comma-separated levels from GS to consider")
    p.add_argument("--limit", type=int, default=0, help="limit number of GS++ controls (0=all)")
    p.add_argument("--manual-csv", default=str(ROOT / "out" / "gspp_compliance_v2.csv"),
                   help="optional CSV with additional manual mappings to add after the model run")
    p.add_argument("--out-dir", default=str(ROOT / "out"))
    args = p.parse_args(argv)

    models = _parse_models(args.model)
    model_sources = list(models)
    levels = tuple(s.strip() for s in args.gs_levels.split(",") if s.strip())
    scope_display = args.scope or "<all>"
    print(
        f"[i] scope={scope_display!r} sample_ratio={args.sample_ratio:.2f} "
        f"seed={args.seed} models={'+'.join(model_sources)} top_k={args.top_k} levels={levels}",
        file=sys.stderr,
    )

    gspp_reqs = parse_gspp.parse(
        ROOT / "data" / "gspp.json",
        scope_prefix=args.scope,
        sample_ratio_per_category=args.sample_ratio,
        random_seed=args.seed,
    )
    gs_reqs = parse_gs.parse(ROOT / "data" / "gs.xml", levels=levels)
    if args.limit:
        gspp_reqs = gspp_reqs[: args.limit]
    print(f"[i] {len(gspp_reqs)} GS++ controls | {len(gs_reqs)} GS requirements", file=sys.stderr)

    gspp_idx = {r.id: r for r in gspp_reqs}
    gs_idx = {r.id: r for r in gs_reqs}

    manual_csv_path = Path(args.manual_csv) if args.manual_csv else None
    manual_source: str | None = None
    manual_matches: dict[str, Match] = {}
    if manual_csv_path and manual_csv_path.exists():
        manual_source = f"manual:{manual_csv_path.stem}"
        manual_matches = _load_manual_matches(manual_csv_path, set(gspp_idx))
        if manual_matches:
            model_sources.append(manual_source)
            print(f"[i] loaded manual mappings from {manual_csv_path} for {len(manual_matches)} GS++ controls", file=sys.stderr)

    sl = Shortlister(gs_reqs)
    judges = [make_judge(model) for model in models]

    matches = []
    for i, q in enumerate(gspp_reqs, 1):
        cands = [r for r, _ in sl.top_k(q, k=args.top_k)]
        print(f"[{i}/{len(gspp_reqs)}] {q.id} ...", file=sys.stderr)
        parts = [judge.classify(q, cands) for judge in judges]
        part_names = [judge.model for judge in judges]
        if manual_source and q.id in manual_matches:
            parts.append(manual_matches[q.id])
            part_names.append(manual_source)
        m = combine_matches(parts, part_names) if len(parts) > 1 else parts[0]
        matches.append(m)
        print(f"    → coverage={m.coverage} conf={m.confidence:.2f} gs={m.gs_candidates}", file=sys.stderr)
    model_label = "+".join(model_sources)

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_model = _safe_model_label(model_sources)
    out_dir = Path(args.out_dir)
    csv_path = out_dir / f"mapping_{safe_model}_{ts}.csv"
    md_path = out_dir / f"mapping_{safe_model}_{ts}.md"
    report.write_csv(csv_path, matches, gspp_idx, gs_idx, model_label)
    report.write_markdown(md_path, matches, gspp_idx, gs_idx, model_label)
    print(f"[i] wrote {csv_path}\n[i] wrote {md_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
