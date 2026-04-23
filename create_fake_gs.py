"""
create_fake_gs.py  –  Generate data/fake.xml from data/gspp.json

Takes GS++ requirement content and structures it as a fake IT-Grundschutz XML
dataset that follows the exact format src/parse_gs.py expects.  Running the
mapping pipeline against fake.xml lets you verify that the matcher correctly
finds a 1-to-1 correspondence back to the original GS++ requirements.

Naming convention for generated requirement IDs:
    FAKE.<N>.<M>.A<K>
    N = top-level GS++ group index (1-based)
    M = subgroup index within that group (1-based)
    K = control counter within the subgroup (1-based)

    Example:  FAKE.1.1.A1  (GC group, Grundlagen subgroup, first control)

The original GS++ control ID is appended in brackets to the title so results
can be cross-referenced, e.g.:
    FAKE.1.1.A1 Errichtung und Aufrechterhaltung eines ISMS (S) [GS++:GC.1.1]

Usage:
    python create_fake_gs.py [--gspp data/gspp.json] [--out data/fake.xml]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from xml.etree import ElementTree as ET

GSPP_PATH = Path(__file__).parent / "data" / "gspp.json"
OUT_PATH = Path(__file__).parent / "data" / "fake.xml"

DOCBOOK_NS = "http://docbook.org/ns/docbook"

# Map GS++ sec_level values to (GS flag, level heading).
# In practice gspp.json only uses "normal-SdT" and "erhöht".
_LEVEL_MAP: dict[str, tuple[str, str]] = {
    "normal-SdT": ("S", "Standard"),
    "normal":     ("S", "Standard"),
    "erhöht":     ("H", "Hoch"),
    "erhoehter":  ("H", "Hoch"),
    "high":       ("H", "Hoch"),
    "basis":      ("B", "Basis"),
}


def _sec_level(ctrl: dict) -> tuple[str, str]:
    """Return (GS-flag, level-heading) for a GS++ control."""
    for p in ctrl.get("props", []):
        if p.get("name") == "sec_level":
            val = p.get("value", "").strip()
            if val in _LEVEL_MAP:
                return _LEVEL_MAP[val]
            for key, mapped in _LEVEL_MAP.items():
                if key in val:
                    return mapped
    return ("S", "Standard")


def _prose(ctrl: dict) -> str:
    """Concatenate all prose parts of a GS++ control into one text block."""
    parts = []
    for p in ctrl.get("parts", []):
        text = (p.get("prose") or "").strip()
        if text:
            parts.append(text)
    return "\n\n".join(parts)



# Neue rekursive Funktion: Erzeuge für jeden Control-Knoten einen XML-Eintrag, egal wie tief
def _add_controls_xml(parent_xml, controls, baustein_id, sg_title, id_prefix, req_counter):
    for idx, ctrl in enumerate(controls, start=1):
        flag, heading = _sec_level(ctrl)
        ctrl_title  = (ctrl.get("title") or "").strip()
        prose       = _prose(ctrl)
        gspp_origin = ctrl.get("id", "")

        # ID für tiefe Controls: baustein_id + laufende Nummern
        req_id = f"{id_prefix}.A{req_counter[0]}"
        req_counter[0] += 1
        req_title = ctrl_title or f"Anforderung {req_counter[0]}"
        full_title = f"{req_id} {req_title} ({flag}) [GS++:{gspp_origin}]"

        # Section für die Anforderung
        req_sec = _sub(parent_xml, "section", {"xml:id": f"fake-bookmark-ctrl-{gspp_origin}"})
        _sub(req_sec, "title", text=full_title)
        for para_text in prose.split("\n\n"):
            para_text = para_text.strip()
            if para_text:
                _sub(req_sec, "para", text=para_text)

        # Rekursiv: Child-Controls
        if ctrl.get("controls"):
            _add_controls_xml(req_sec, ctrl["controls"], baustein_id, sg_title, req_id, req_counter)


# ---------- XML helpers ----------

def _sub(parent: ET.Element, tag: str,
         attrib: dict | None = None, text: str | None = None) -> ET.Element:
    el = ET.SubElement(parent, f"{{{DOCBOOK_NS}}}{tag}", attrib or {})
    if text is not None:
        el.text = text
    return el


# ---------- main builder ----------


def build_xml(gspp_path: Path) -> ET.ElementTree:
    data = json.loads(gspp_path.read_text(encoding="utf-8"))["catalog"]
    top_groups: list[dict] = data["groups"]

    ET.register_namespace("", DOCBOOK_NS)

    book = ET.Element(
        f"{{{DOCBOOK_NS}}}book",
        {"version": "5.0", "xml:id": "fake-bookmark-0"},
    )
    info = ET.SubElement(book, f"{{{DOCBOOK_NS}}}info")
    ET.SubElement(info, f"{{{DOCBOOK_NS}}}title").text = (
        "Fake GS Dataset (derived from GS++ content)"
    )

    bm = 0  # bookmark counter

    def next_bm() -> str:
        nonlocal bm
        bm += 1
        return f"fake-bookmark-{bm}"

    def process_group(group, grp_idx, sg_idx, parent_chapter):
        group_id    = group.get("id", f"G{grp_idx}")
        group_title = group.get("title", f"Group {grp_idx}")
        baustein_id = f"FAKE.{grp_idx}.{sg_idx}"

        baustein_sec = _sub(parent_chapter, "section", {"xml:id": next_bm()})
        _sub(baustein_sec, "title", text=f"{baustein_id} {group_title}")

        anf_sec = _sub(baustein_sec, "section", {"xml:id": next_bm()})
        _sub(anf_sec, "title", text="Anforderungen")

        req_counter = [1]
        _add_controls_xml(anf_sec, group.get("controls", []), baustein_id, group_title, baustein_id, req_counter)

        # Rekursiv alle Subgruppen verarbeiten
        for sub_idx, subgroup in enumerate(group.get("groups", []), start=1):
            process_group(subgroup, grp_idx, f"{sg_idx}.{sub_idx}", parent_chapter)

    for grp_idx, group in enumerate(top_groups, start=1):
        group_id    = group.get("id", f"G{grp_idx}")
        group_title = group.get("title", f"Group {grp_idx}")

        chapter = _sub(book, "chapter", {"xml:id": next_bm()})
        _sub(chapter, "title", text=f"FAKE {group_id} {group_title}")

        process_group(group, grp_idx, 1, chapter)

    tree = ET.ElementTree(book)
    ET.indent(tree, space="  ")
    return tree


# ---------- entry point ----------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate data/fake.xml from data/gspp.json"
    )
    parser.add_argument(
        "--gspp", default=str(GSPP_PATH), metavar="PATH",
        help="Path to gspp.json  (default: data/gspp.json)"
    )
    parser.add_argument(
        "--out", default=str(OUT_PATH), metavar="PATH",
        help="Output path for fake.xml  (default: data/fake.xml)"
    )
    args = parser.parse_args()

    gspp_path = Path(args.gspp)
    out_path  = Path(args.out)

    print(f"Reading    {gspp_path}")
    tree = build_xml(gspp_path)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(str(out_path), xml_declaration=True, encoding="UTF-8")
    print(f"Written to {out_path}")

    # Quick sanity-check: run through parse_gs to count parsed requirements
    try:
        import sys
        sys.path.insert(0, str(Path(__file__).parent))
        from src.parse_gs import parse

        reqs = parse(out_path, levels=("Basis", "Standard", "Hoch"))
        by_level: dict[str, int] = {}
        for r in reqs:
            lv = r.level or "?"
            by_level[lv] = by_level.get(lv, 0) + 1
        print(f"Validation: parse_gs found {len(reqs)} requirements  {by_level}")
        if reqs:
            print(f"  Sample : {reqs[0].id}  –  {reqs[0].title[:70]}")
    except Exception as exc:
        print(f"(Validation skipped: {exc})")


if __name__ == "__main__":
    main()
