from __future__ import annotations

import argparse
import csv
import html
import json
from dataclasses import dataclass
from pathlib import Path

from . import parse_gs, parse_gspp


@dataclass
class MappingEdge:
    gspp_id: str
    coverage: str
    gs_id: str


COVERAGE_COLORS = {
    "voll": "#2e7d32",
    "teilweise": "#ef6c00",
    "keine": "#9e9e9e",
}


def _split_ids(value: str) -> list[str]:
    return [x.strip() for x in value.split(";") if x.strip()]


def _parse_gs_titles(value: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for part in value.split(";"):
        part = part.strip()
        if not part or ":" not in part:
            continue
        rid, title = part.split(":", 1)
        rid = rid.strip()
        title = title.strip()
        if rid and title:
            out[rid] = title
    return out


def _read_rows(csv_path: Path, include_coverages: set[str], max_left: int = 0) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (row.get("coverage") or "").strip() not in include_coverages:
                continue
            rows.append(row)

    if max_left > 0:
        rows = rows[:max_left]
    return rows


def _read_edges(rows: list[dict[str, str]]) -> tuple[list[MappingEdge], list[str], list[str]]:
    edges: list[MappingEdge] = []
    left_nodes: list[str] = []
    left_seen: set[str] = set()
    right_nodes: list[str] = []
    right_seen: set[str] = set()

    for row in rows:
        gspp_id = (row.get("gspp_id") or "").strip()
        coverage = (row.get("coverage") or "").strip()
        if not gspp_id:
            continue

        if gspp_id not in left_seen:
            left_nodes.append(gspp_id)
            left_seen.add(gspp_id)

        for gs_id in _split_ids(row.get("gs_ids") or ""):
            edges.append(MappingEdge(gspp_id=gspp_id, coverage=coverage, gs_id=gs_id))
            if gs_id not in right_seen:
                right_nodes.append(gs_id)
                right_seen.add(gs_id)

    return edges, left_nodes, right_nodes


def _latest_mapping_csv(out_dir: Path) -> Path:
    csvs = sorted(out_dir.glob("mapping_*.csv"), key=lambda p: p.stat().st_mtime)
    if not csvs:
        raise FileNotFoundError(f"No mapping CSV found in {out_dir}")
    return csvs[-1]


def _load_source_texts(gspp_json: Path | None, gs_xml: Path | None) -> tuple[dict[str, str], dict[str, str], dict[str, str], dict[str, str]]:
    gspp_titles: dict[str, str] = {}
    gspp_texts: dict[str, str] = {}
    gs_titles: dict[str, str] = {}
    gs_texts: dict[str, str] = {}

    if gspp_json and gspp_json.exists():
        for req in parse_gspp.parse(gspp_json, scope_prefix=""):
            gspp_titles[req.id] = req.title
            gspp_texts[req.id] = req.text

    if gs_xml and gs_xml.exists():
        for req in parse_gs.parse(gs_xml, levels=("Basis", "Standard", "Hoch")):
            gs_titles[req.id] = req.title
            gs_texts[req.id] = req.text

    return gspp_titles, gspp_texts, gs_titles, gs_texts


def _build_node_payloads(
    rows: list[dict[str, str]],
    left_nodes: list[str],
    right_nodes: list[str],
    gspp_titles: dict[str, str],
    gspp_texts: dict[str, str],
    gs_titles: dict[str, str],
    gs_texts: dict[str, str],
) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    left_payload: dict[str, dict[str, str]] = {}
    right_payload: dict[str, dict[str, str]] = {}

    row_by_left: dict[str, dict[str, str]] = {}
    right_titles_from_csv: dict[str, str] = {}
    mapped_from: dict[str, list[str]] = {rid: [] for rid in right_nodes}

    for row in rows:
        gspp_id = (row.get("gspp_id") or "").strip()
        if gspp_id and gspp_id not in row_by_left:
            row_by_left[gspp_id] = row

        parsed_titles = _parse_gs_titles(row.get("gs_titles") or "")
        for rid, title in parsed_titles.items():
            if rid not in right_titles_from_csv:
                right_titles_from_csv[rid] = title

        for rid in _split_ids(row.get("gs_ids") or ""):
            if rid in mapped_from and gspp_id and gspp_id not in mapped_from[rid]:
                mapped_from[rid].append(gspp_id)

    for node in left_nodes:
        row = row_by_left.get(node, {})
        left_payload[node] = {
            "id": node,
            "title": gspp_titles.get(node) or (row.get("gspp_title") or "").strip(),
            "level": (row.get("gspp_level") or "").strip(),
            "coverage": (row.get("coverage") or "").strip(),
            "confidence": (row.get("confidence") or "").strip(),
            "rationale": (row.get("rationale") or "").strip(),
            "gap_notes": (row.get("gap_notes") or "").strip(),
            "source_text": gspp_texts.get(node, ""),
        }

    for node in right_nodes:
        right_payload[node] = {
            "id": node,
            "title": gs_titles.get(node) or right_titles_from_csv.get(node, ""),
            "mapped_from": ", ".join(mapped_from.get(node, [])),
            "source_text": gs_texts.get(node, ""),
        }

    return left_payload, right_payload


def _json_for_script(data: dict[str, dict[str, str]]) -> str:
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def _build_html(
    title: str,
    edges: list[MappingEdge],
    left_nodes: list[str],
    right_nodes: list[str],
    left_payload: dict[str, dict[str, str]],
    right_payload: dict[str, dict[str, str]],
) -> str:
    left_x = 220
    right_x = 980
    top_margin = 80
    lane_gap = 28
    node_radius = 7

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
        edge_lines.append(f'<path d="{d}" stroke="{color}" stroke-width="1.6" fill="none" opacity="0.6" />')

    left_nodes_svg: list[str] = []
    for node in left_nodes:
        y = left_y[node]
        node_id = html.escape(node)
        left_nodes_svg.append(
            f'<g class="node clickable" data-side="left" data-id="{node_id}" role="button" tabindex="0">'
            f'<circle cx="{left_x}" cy="{y}" r="{node_radius}" fill="#0d47a1" />'
            f'<text x="{left_x - 14}" y="{y + 4}" text-anchor="end" class="label-left">{node_id}</text>'
            "</g>"
        )

    right_nodes_svg: list[str] = []
    for node in right_nodes:
        y = right_y[node]
        node_id = html.escape(node)
        right_nodes_svg.append(
            f'<g class="node clickable" data-side="right" data-id="{node_id}" role="button" tabindex="0">'
            f'<circle cx="{right_x}" cy="{y}" r="{node_radius}" fill="#004d40" />'
            f'<text x="{right_x + 14}" y="{y + 4}" text-anchor="start" class="label-right">{node_id}</text>'
            "</g>"
        )

    left_json = _json_for_script(left_payload)
    right_json = _json_for_script(right_payload)

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
    h1 {{ margin: 0 0 8px; font-size: 1.15rem; letter-spacing: 0.01em; }}
    p.meta {{ margin: 0 0 12px; color: var(--muted); font-size: 0.92rem; }}
    .legend {{ display: flex; gap: 14px; flex-wrap: wrap; margin: 10px 0 14px; color: var(--muted); font-size: 0.88rem; }}
    .dot {{ width: 10px; height: 10px; border-radius: 99px; display: inline-block; margin-right: 6px; }}
    .viewport {{ overflow: auto; border: 1px solid #e5e7eb; border-radius: 10px; background: #fcfcfc; }}
    svg {{ width: 100%; min-width: 1100px; height: auto; display: block; }}
    .clickable {{ cursor: pointer; }}
    .clickable:hover text {{ text-decoration: underline; }}
    .node.active circle {{ stroke: #111827; stroke-width: 2; }}
    .label-left, .label-right {{ fill: var(--ink); font-size: 12px; font-weight: 500; }}
    .column-title {{ fill: var(--muted); font-size: 12px; font-weight: 700; letter-spacing: 0.08em; }}
    .details {{ margin-top: 14px; border: 1px solid #e5e7eb; border-radius: 10px; background: #fff; padding: 12px; }}
    .details h2 {{ margin: 0 0 8px; font-size: 1rem; }}
    .details .meta-row {{ margin: 6px 0; color: var(--muted); font-size: 0.9rem; }}
    .details pre {{
      margin: 8px 0 0;
      white-space: pre-wrap;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 10px;
      font-size: 0.84rem;
      line-height: 1.4;
      max-height: 360px;
      overflow: auto;
    }}
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>{html.escape(title)}</h1>
    <p class=\"meta\">GS++ links: {len(left_nodes)} | GS rechts: {len(right_nodes)} | Kanten: {len(edges)}</p>
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
    <div class=\"details\" id=\"node-details\">
      <h2>Node Details</h2>
      <div class=\"meta-row\">Click a node on the left or right to display its full content.</div>
    </div>
  </div>
  <script id=\"left-data\" type=\"application/json\">{left_json}</script>
  <script id=\"right-data\" type=\"application/json\">{right_json}</script>
  <script>
    const leftData = JSON.parse(document.getElementById('left-data').textContent || '{{}}');
    const rightData = JSON.parse(document.getElementById('right-data').textContent || '{{}}');
    const details = document.getElementById('node-details');

    function escapeHtml(value) {{
      return String(value || '')
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/\"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }}

    function detailBlock(label, value) {{
      if (!value) return '';
      return `<div class=\"meta-row\"><strong>${{escapeHtml(label)}}:</strong> ${{escapeHtml(value)}}</div>`;
    }}

    function detailText(label, value) {{
      if (!value) return '';
      return `<div class=\"meta-row\"><strong>${{escapeHtml(label)}}:</strong></div><pre>${{escapeHtml(value)}}</pre>`;
    }}

    function activateNode(side, id) {{
      document.querySelectorAll('.node.active').forEach((el) => el.classList.remove('active'));
      const selector = `.node[data-side=\"${{side}}\"][data-id=\"${{CSS.escape(id)}}\"]`;
      document.querySelectorAll(selector).forEach((el) => el.classList.add('active'));
    }}

    function renderNode(side, id) {{
      activateNode(side, id);
      const payload = side === 'left' ? leftData[id] : rightData[id];
      if (!payload) {{
        details.innerHTML = `<h2>Node Details</h2><div class=\"meta-row\">No details available for ${{escapeHtml(id)}}.</div>`;
        return;
      }}

      if (side === 'left') {{
        details.innerHTML = [
          `<h2>GS++ Node: ${{escapeHtml(payload.id || id)}}</h2>`,
          detailBlock('Title', payload.title),
          detailBlock('Level', payload.level),
          detailBlock('Coverage', payload.coverage),
          detailBlock('Confidence', payload.confidence),
          detailText('Rationale', payload.rationale),
          detailText('Gap Notes', payload.gap_notes),
          detailText('Source Text (JSON)', payload.source_text),
        ].join('');
      }} else {{
        details.innerHTML = [
          `<h2>GS Node: ${{escapeHtml(payload.id || id)}}</h2>`,
          detailBlock('Title', payload.title),
          detailBlock('Mapped from', payload.mapped_from),
          detailText('Source Text (XML)', payload.source_text),
        ].join('');
      }}
    }}

    document.querySelectorAll('.node.clickable').forEach((node) => {{
      node.addEventListener('click', () => renderNode(node.dataset.side, node.dataset.id));
      node.addEventListener('keydown', (ev) => {{
        if (ev.key === 'Enter' || ev.key === ' ') {{
          ev.preventDefault();
          renderNode(node.dataset.side, node.dataset.id);
        }}
      }});
    }});
  </script>
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
    parser.add_argument("--gspp-json", type=Path, default=Path("data/gspp.json"), help="Optional path to GS++ catalog JSON")
    parser.add_argument("--gs-xml", type=Path, default=Path("data/gs.xml"), help="Optional path to IT-Grundschutz XML")
    args = parser.parse_args(argv)

    csv_path = args.input_csv or _latest_mapping_csv(Path("out"))
    include_coverages = {x.strip() for x in args.include_coverage.split(",") if x.strip()}
    if not include_coverages:
        raise ValueError("--include-coverage must contain at least one value")

    rows = _read_rows(csv_path=csv_path, include_coverages=include_coverages, max_left=args.max_left)
    edges, left_nodes, right_nodes = _read_edges(rows)

    gspp_titles, gspp_texts, gs_titles, gs_texts = _load_source_texts(args.gspp_json, args.gs_xml)
    left_payload, right_payload = _build_node_payloads(
        rows=rows,
        left_nodes=left_nodes,
        right_nodes=right_nodes,
        gspp_titles=gspp_titles,
        gspp_texts=gspp_texts,
        gs_titles=gs_titles,
        gs_texts=gs_texts,
    )

    out_path = args.out or csv_path.with_name(f"{csv_path.stem}_graph.html")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    html_doc = _build_html(args.title, edges, left_nodes, right_nodes, left_payload, right_payload)
    out_path.write_text(html_doc, encoding="utf-8")

    print(f"[i] input: {csv_path}")
    print(f"[i] output: {out_path}")
    print(f"[i] left_nodes={len(left_nodes)} right_nodes={len(right_nodes)} edges={len(edges)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
