from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from . import parse_gs, parse_gspp, report
from .judge import make_judge
from .shortlist import Shortlister

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    load_dotenv(ROOT / ".env")
    p = argparse.ArgumentParser(description="Map Grundschutz++ to IT-Grundschutz")
    p.add_argument("--model", default="claude-sonnet-4-5",
                   help="e.g. claude-sonnet-4-5, claude-opus-4-1-20250805, gpt-4o-2024-11-20")
    p.add_argument("--scope", default="GC.",
                   help="GS++ ID-prefix to include (default: 'GC.')")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--gs-levels", default="Basis,Standard",
                   help="comma-separated levels from GS to consider")
    p.add_argument("--limit", type=int, default=0, help="limit number of GS++ controls (0=all)")
    p.add_argument("--out-dir", default=str(ROOT / "out"))
    args = p.parse_args(argv)

    levels = tuple(s.strip() for s in args.gs_levels.split(",") if s.strip())
    print(f"[i] scope={args.scope!r} model={args.model} top_k={args.top_k} levels={levels}", file=sys.stderr)

    gspp_reqs = parse_gspp.parse(ROOT / "data" / "gspp.json", scope_prefix=args.scope)
    gs_reqs = parse_gs.parse(ROOT / "data" / "gs.xml", levels=levels)
    if args.limit:
        gspp_reqs = gspp_reqs[: args.limit]
    print(f"[i] {len(gspp_reqs)} GS++ controls | {len(gs_reqs)} GS requirements", file=sys.stderr)

    sl = Shortlister(gs_reqs)
    judge = make_judge(args.model)

    matches = []
    for i, q in enumerate(gspp_reqs, 1):
        cands = [r for r, _ in sl.top_k(q, k=args.top_k)]
        print(f"[{i}/{len(gspp_reqs)}] {q.id} ...", file=sys.stderr)
        m = judge.classify(q, cands)
        matches.append(m)
        print(f"    → coverage={m.coverage} conf={m.confidence:.2f} gs={m.gs_candidates}", file=sys.stderr)

    gspp_idx = {r.id: r for r in gspp_reqs}
    gs_idx = {r.id: r for r in gs_reqs}

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_model = args.model.replace("/", "_").replace(":", "_")
    out_dir = Path(args.out_dir)
    csv_path = out_dir / f"mapping_{safe_model}_{ts}.csv"
    md_path = out_dir / f"mapping_{safe_model}_{ts}.md"
    report.write_csv(csv_path, matches, gspp_idx, gs_idx, args.model)
    report.write_markdown(md_path, matches, gspp_idx, gs_idx, args.model)
    print(f"[i] wrote {csv_path}\n[i] wrote {md_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
