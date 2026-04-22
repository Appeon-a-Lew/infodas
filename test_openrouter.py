"""Quick diagnostic for OpenRouterJudge."""
import os
import sys
import traceback

print(f"OPENROUTER_API_KEY set: {bool(os.environ.get('OPENROUTER_API_KEY'))}")
print(f"key len: {len(os.environ.get('OPENROUTER_API_KEY', ''))}")

from src.models import Requirement
from src.judge import OpenRouterJudge, make_judge

gspp = Requirement(
    id="GC.TEST.1",
    title="Test",
    text="Die Institution MUSS eine Sicherheitsleitlinie erstellen.",
    source="gspp",
)
cands = [
    Requirement(
        id="ISMS.1.A3",
        title="Erstellung einer Leitlinie",
        text="Leitlinie zur Informationssicherheit erstellen.",
        source="gs",
        baustein="ISMS.1",
        level="Basis",
    ),
]

model = sys.argv[1] if len(sys.argv) > 1 else "google/gemma-4-26b-a4b-it"
print(f"model: {model}")

try:
    j = make_judge(model)
    print(f"judge: {type(j).__name__}")
    print("calling classify...")
    m = j.classify(gspp, cands)
    print(f"OK: coverage={m.coverage} conf={m.confidence} ids={m.gs_candidates}")
    print(f"rationale: {m.rationale[:200]}")
except Exception as e:
    print(f"FAIL: {type(e).__name__}: {e}")
    traceback.print_exc()
