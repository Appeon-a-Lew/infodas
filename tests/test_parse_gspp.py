import json
import math
import sys
import pathlib
import pytest

# Tell Python that 'src' is a package named 'src' so relative imports work
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Import as part of the 'src' package (preserves relative imports)
from src.parse_gspp import _pool_size, _control_family, parse


# --- _pool_size ---

def test_pool_size_less_than_10():
    assert _pool_size(1) == 1
    assert _pool_size(5) == 3
    assert _pool_size(9) == 3

def test_pool_size_between_10_and_49():
    assert _pool_size(10) == 2   # ceil(10 * 0.20) = 2
    assert _pool_size(25) == 5
    assert _pool_size(49) == 10  # ceil(49 * 0.20) = 10

def test_pool_size_50_and_above():
    assert _pool_size(50) == 5   # ceil(50 * 0.10) = 5
    assert _pool_size(100) == 10
    assert _pool_size(99) == 10  # ceil(99 * 0.10) = 10


# --- _control_family ---

def test_control_family_basic():
    assert _control_family("GC.AC-1") == "GC.AC"
    assert _control_family("GC.SC-28") == "GC.SC"

def test_control_family_nested():
    assert _control_family("GC.IA-5.1") == "GC.IA"

def test_control_family_no_dash():
    assert _control_family("GC.AC") == "GC.AC"


# --- parse() integration ---

FAKE_CATALOG = {
    "catalog": {
        "groups": [
            {
                "id": "GC.AC", "title": "Access Control",
                "controls": [
                    {"id": f"GC.AC-{i}", "title": f"AC Control {i}",
                     "parts": [{"name": "statement", "prose": f"Prose {i}"}],
                     "props": []}
                    for i in range(1, 6)   # 5 controls → pool = 3
                ]
            },
            {
                "id": "GC.SC", "title": "System Comms",
                "controls": [
                    {"id": f"GC.SC-{i}", "title": f"SC Control {i}",
                     "parts": [{"name": "statement", "prose": f"Prose {i}"}],
                     "props": []}
                    for i in range(1, 15)  # 14 controls → pool = ceil(14*0.2) = 3
                ]
            }
        ]
    }
}

@pytest.fixture
def fake_json(tmp_path):
    p = tmp_path / "gspp.json"
    p.write_text(json.dumps(FAKE_CATALOG))
    return p

def test_parse_no_pool_returns_all(fake_json):
    reqs = parse(fake_json, random_pool=False)
    assert len(reqs) == 19  # 5 + 14

def test_parse_pool_reduces_count(fake_json):
    reqs = parse(fake_json, random_pool=True)
    assert len(reqs) < 19

def test_parse_pool_correct_sizes(fake_json):
    reqs = parse(fake_json, random_pool=True, seed=42)
    ac = [r for r in reqs if r.id.startswith("GC.AC")]
    sc = [r for r in reqs if r.id.startswith("GC.SC")]
    assert len(ac) == 3   # < 10 → take 3
    assert len(sc) == 3   # ceil(14 * 0.20) = 3

def test_parse_pool_reproducible(fake_json):
    r1 = [r.id for r in parse(fake_json, seed=42)]
    r2 = [r.id for r in parse(fake_json, seed=42)]
    assert r1 == r2

def test_parse_pool_different_seeds(fake_json):
    r1 = {r.id for r in parse(fake_json, seed=1)}
    r2 = {r.id for r in parse(fake_json, seed=99)}
    assert r1 != r2