from __future__ import annotations

from pathlib import Path

import requests

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

GSPP_URL = (
    "https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/"
    "main/Anwenderkataloge/Grundschutz%2B%2B/Grundschutz%2B%2B-catalog.json"
)
GS_XML_URL = (
    "https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/"
    "IT-GS-Kompendium/XML_Kompendium_2023.xml?__blob=publicationFile&v=1"
)


def _download(url: str, dest: Path) -> Path:
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, timeout=60, headers={"User-Agent": "isms-gspp-mapping/0.1"})
    resp.raise_for_status()
    dest.write_bytes(resp.content)
    return dest


def fetch_all() -> tuple[Path, Path]:
    gspp = _download(GSPP_URL, DATA_DIR / "gspp.json")
    gs = _download(GS_XML_URL, DATA_DIR / "gs.xml")
    return gspp, gs


if __name__ == "__main__":
    gspp, gs = fetch_all()
    print(f"gspp: {gspp} ({gspp.stat().st_size} bytes)")
    print(f"gs:   {gs} ({gs.stat().st_size} bytes)")
