from __future__ import annotations

import argparse
import csv
import html
from dataclasses import dataclass
from pathlib import Path


@dataclass
class MappingEdge:
    gspp_id: str
    gspp_title: str
    coverage: str
    gs_id: str


COVERAGE_COLORS = {
    "voll": "#2e7d32",
    "teilweise": "#ef6c00",
    "keine": "#9e9e9e",
}


def _split_ids(value: str) -> list[str]:
    return [x.strip() for x in value.split(";") if x.strip()]


def _read_edges(csv_path: Path, include_coverages: set[str], max_left: int = 0) -> tuple[list[MappingEdge], list[str], list[str]]:
    rows: list[dict[str, str]] = []
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (row.get("coverage") or "").strip() not in include_coverages:
                continue
            rows.append(row)

    if max_left > 0:
        rows = rows[:max_left]

    edges: list[MappingEdge] = []
    left_nodes: list[str] = []
    left_seen: set[str] = set()
    right_nodes: list[str] = []
    right_seen: set[str] = set()

    for row in rows:
        gspp_id = (row.get("gspp_id") or "").strip()
        gspp_title = (row.get("gspp_title") or "").strip()
        coverage = (row.get("coverage") or "").strip()
        if not gspp_id:
            continue

        if gspp_id not in left_seen:
            left_nodes.append(gspp_id)
            left_seen.add(gspp_id)

        for gs_id in _split_ids(row.get("gs_ids") or ""):
            edges.append(MappingEdge(gspp_id=gspp_id, gspp_title=gspp_title, coverage=coverage, gs_id=gs_id))
            if gs_id not in right_seen:
                right_nodes.append(gs_id)
                right_seen.add(gs_id)

    return edges, left_nodes, right_nodes


def _latest_mapping_csv(out_dir: Path) -> Path:
    csvs = sorted(out_dir.glob("mapping_*.csv"), key=lambda p: p.stat().st_mtime)
    if not csvs:
        raise FileNotFoundError(f"No mapping CSV found in {out_dir}")
    return csvs[-1]


def _build_html(title: str, edges: list[MappingEdge], left_nodes: list[str], right_nodes: list[str]) -> str:
    left_x = 220
    right_x = 980
    top_margin = 80
    lane_gap = 28
    node_radius = 7

    # Ensure enough vertical space even for sparse but high-indexed right-side references.
    height = max(320, top_margin * 2 + lane_gap * max(len(left_nodes), len(right_nodes), 1))
    width = 1280

    left_y = {node: top_margin + i * lane_gap for i, node in enumerate(left_nodes)}
    right_y = {node: top_margin + i * lane_gap for i, node in enumerate(right_nodes)}

    edge_lines: list[str] = []
    for e in edges:
        if e.gspp_id not in left_y or e.gs_id not in right_y:
            continue
        y1 = left_y[e.gspp_id]
        y2 = right_y[e.gs_id]
        color = COVERAGE_COLORS.get(e.coverage, "#757575")
        c1x = left_x + 250
        c2x = right_x - 250
        d = f"M {left_x} {y1} C {c1x} {y1}, {c2x} {y2}, {right_x} {y2}"
        edge_lines.append(
            f'<path d="{d}" stroke="{color}" stroke-width="1.6" fill="none" opacity="0.6" />'
        )

    left_nodes_svg: list[str] = []
    for node in left_nodes:
        y = left_y[node]
        left_nodes_svg.append(
            f'<circle cx="{left_x}" cy="{y}" r="{node_radius}" fill="#0d47a1" />'
            f'<text x="{left_x - 14}" y="{y + 4}" text-anchor="end" class="label-left">{html.escape(node)}</text>'
        )

    right_nodes_svg: list[str] = []
    for node in right_nodes:
        y = right_y[node]
        right_nodes_svg.append(
            f'<circle cx="{right_x}" cy="{y}" r="{node_radius}" fill="#004d40" />'
            f'<text x="{right_x + 14}" y="{y + 4}" text-anchor="start" class="label-right">{html.escape(node)}</text>'
        )

    left_count = len(left_nodes)
    right_count = len(right_nodes)
    edge_count = len(edges)

    return f"""<!doctype html>
<html lang=\"de\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --bg: #f8f7f4;
      --panel: #ffffff;
      --ink: #1f2937;
      --muted: #6b7280;
      --accent: #0d47a1;
      --accent-2: #004d40;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background:
        radial-gradient(circle at 0% 0%, #f5efe3 0%, transparent 40%),
        radial-gradient(circle at 100% 100%, #e7f3f0 0%, transparent 40%),
        var(--bg);
      color: var(--ink);
      font-family: "IBM Plex Sans", "Avenir Next", "Segoe UI", sans-serif;
      padding: 20px;
    }}
    .card {{
      max-width: 100%;
      margin: 0 auto;
      background: var(--panel);
      border: 1px solid #e5e7eb;
      border-radius: 14px;
      padding: 16px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 1.15rem;
      letter-spacing: 0.01em;
    }}
    p.meta {{
      margin: 0 0 12px;
      color: var(--muted);
      font-size: 0.92rem;
    }}
    .legend {{
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      margin: 10px 0 14px;
      color: var(--muted);
      font-size: 0.88rem;
    }}
    .dot {{ width: 10px; height: 10px; border-radius: 99px; display: inline-block; margin-right: 6px; }}
    .viewport {{
      overflow: auto;
      border: 1px solid #e5e7eb;
      border-radius: 10px;
      background: #fcfcfc;
    }}
    svg {{ width: 100%; min-width: 1100px; height: auto; display: block; }}
    .label-left, .label-right {{ fill: var(--ink); font-size: 12px; font-weight: 500; }}
    .column-title {{ fill: var(--muted); font-size: 12px; font-weight: 700; letter-spacing: 0.08em; }}
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>{html.escape(title)}</h1>
    <p class=\"meta\">GS++ links: {left_count} | GS rechts: {right_count} | Kanten: {edge_count}</p>
    <div class=\"legend\">
      <span><span class=\"dot\" style=\"background:{COVERAGE_COLORS['voll']}\"></span>voll</span>
      <span><span class=\"dot\" style=\"background:{COVERAGE_COLORS['teilweise']}\"></span>teilweise</span>
      <span><span class=\"dot\" style=\"background:{COVERAGE_COLORS['keine']}\"></span>keine</span>
    </div>
    <div class=\"viewport\">
      <svg viewBox=\"0 0 {width} {height}\" role=\"img\" aria-label=\"GS++ zu GS Mapping\">
        <text x=\"70\" y=\"36\" class=\"column-title\">GS++ (neu)</text>
        <text x=\"910\" y=\"36\" class=\"column-title\">GS (klassisch)</text>
        {''.join(edge_lines)}
        {''.join(left_nodes_svg)}
        {''.join(right_nodes_svg)}
      </svg>
    </div>
  </div>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Create a left-to-right GS++->GS graph visualization from a mapping CSV. "
            "GS++ nodes are placed on the left, GS nodes on the right."
        )
    )
    parser.add_argument("--input-csv", type=Path, default=None, help="Path to mapping_*.csv; defaults to latest file in ./out")
    parser.add_argument("--out", type=Path, default=None, help="Output HTML path (default: <csv_stem>_graph.html)")
    parser.add_argument(
        "--include-coverage",
        default="voll,teilweise",
        help="Comma-separated coverage values to draw (default: voll,teilweise)",
    )
    parser.add_argument("--max-left", type=int, default=0, help="Limit number of GS++ nodes from CSV order (0=all)")
    parser.add_argument("--title", default="GS++ -> IT-Grundschutz Mapping Graph")
    args = parser.parse_args(argv)

    csv_path = args.input_csv or _latest_mapping_csv(Path("out"))
    include_coverages = {x.strip() for x in args.include_coverage.split(",") if x.strip()}
    if not include_coverages:
        raise ValueError("--include-coverage must contain at least one value")

    edges, left_nodes, right_nodes = _read_edges(
        csv_path=csv_path,
        include_coverages=include_coverages,
        max_left=args.max_left,
    )

    out_path = args.out or csv_path.with_name(f"{csv_path.stem}_graph.html")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    html_doc = _build_html(args.title, edges, left_nodes, right_nodes)
    out_path.write_text(html_doc, encoding="utf-8")

    print(f"[i] input: {csv_path}")
    print(f"[i] output: {out_path}")
    print(f"[i] left_nodes={len(left_nodes)} right_nodes={len(right_nodes)} edges={len(edges)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
