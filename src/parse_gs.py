from __future__ import annotations

import re
from pathlib import Path

from lxml import etree

from .models import Requirement

NS = {"d": "http://docbook.org/ns/docbook"}

LEVEL_MAP = {"B": "Basis", "S": "Standard", "H": "Hoch"}
TITLE_RE = re.compile(r"^([A-Z]+(?:\.\d+)+\.A\d+)\s+(.*?)\s*\(([BSH])\)")


def _text_of(section) -> str:
    paras = section.findall("d:para", NS)
    parts = []
    for p in paras:
        txt = "".join(p.itertext()).strip()
        if txt:
            parts.append(txt)
    return "\n".join(parts)


def parse(xml_path: Path | str, levels: tuple[str, ...] = ("Basis", "Standard")) -> list[Requirement]:
    tree = etree.parse(str(xml_path))
    out: list[Requirement] = []

    for chapter in tree.getroot().findall("d:chapter", NS):
        ct = (chapter.find("d:title", NS).text or "").strip()
        # Baustein-chapters start with uppercase layer code followed by space
        if not re.match(r"^[A-Z]+\s", ct):
            continue
        layer = ct.split()[0]
        if layer in {"Elementare", "Vorwort", "Neues", "IT-Grundschutz", "Schichtenmodell", "Rollen", "Glossar"}:
            continue

        for baustein_sec in chapter.findall("d:section", NS):
            bt = (baustein_sec.find("d:title", NS).text or "").strip()
            m = re.match(r"^([A-Z]+(?:\.\d+)+)\s+(.*)$", bt)
            if not m:
                continue
            baustein_id, baustein_name = m.group(1), m.group(2)

            anf_sec = next(
                (s for s in baustein_sec.findall("d:section", NS)
                 if (s.find("d:title", NS).text or "").startswith("Anforderungen")),
                None,
            )
            if anf_sec is None:
                continue

            for level_group in anf_sec.findall("d:section", NS):
                lgt = (level_group.find("d:title", NS).text or "")
                if lgt.startswith("Basis"):
                    level = "Basis"
                elif lgt.startswith("Standard"):
                    level = "Standard"
                elif "erhöhtem" in lgt or "erhoehtem" in lgt:
                    level = "Hoch"
                else:
                    continue
                if level not in levels:
                    continue

                for req in level_group.findall("d:section", NS):
                    raw_title = (req.find("d:title", NS).text or "").strip()
                    tm = TITLE_RE.match(raw_title)
                    if not tm:
                        continue
                    req_id, req_title, _flag = tm.group(1), tm.group(2), tm.group(3)
                    if "ENTFALLEN" in req_title.upper():
                        continue
                    body = _text_of(req)
                    if not body:
                        continue
                    out.append(
                        Requirement(
                            id=req_id,
                            title=req_title,
                            text=body,
                            source="gs",
                            baustein=f"{baustein_id} {baustein_name}",
                            level=level,
                        )
                    )
    return out


if __name__ == "__main__":
    reqs = parse(Path(__file__).resolve().parent.parent / "data" / "gs.xml")
    print(f"parsed {len(reqs)} GS requirements")
    by_level: dict[str, int] = {}
    for r in reqs:
        by_level[r.level or "?"] = by_level.get(r.level or "?", 0) + 1
    print("by level:", by_level)
    print("sample:", reqs[0].id, "-", reqs[0].title[:60])
