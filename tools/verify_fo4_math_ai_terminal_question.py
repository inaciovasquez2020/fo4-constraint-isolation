#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

base = json.loads((ROOT / "artifacts/fo4_constraint_isolation.json").read_text())
artifact = json.loads((ROOT / "artifacts/fo4_math_ai_terminal_question_2026_05_12.json").read_text())
doc = (ROOT / "docs/status/FO4_MATH_AI_TERMINAL_QUESTION_2026_05_12.md").read_text()
readme = (ROOT / "README.md").read_text()

assert base["status"] == "FO4_CONSTRAINT_ISOLATION_ONLY"
assert base["variable_budget"] == 4
assert base["theorem_closure"] is False

assert artifact["artifact"] == "fo4_math_ai_terminal_question"
assert artifact["status"] == "OPEN_PROBLEM_REQUIRED"
assert artifact["logic_surface"] == "FO4"
assert artifact["variable_budget"] == 4
assert artifact["theorem_closure"] is False
assert artifact["terminal_question"]["name"] == "FO4CycleOverlapRankRigidityDichotomy"
assert artifact["missing_lemma"] == "FO4CycleOverlapRankRigidity_or_CounterexampleFamily"

required = [
    "Status: OPEN_PROBLEM_REQUIRED",
    "FO4CycleOverlapRankRigidityDichotomy",
    "FO4CycleOverlapRankRigidity_or_CounterexampleFamily",
    "Rigidity branch",
    "Counterexample branch",
    "No unrestricted graph-rigidity theorem is proved.",
    "No unrestricted Cayley-graph rigidity theorem is proved.",
    "No Chronos-RR closure is claimed.",
    "No H4.1/FGL closure is claimed.",
    "No UniversalFiberEntropyGap theorem is claimed.",
    "No P vs NP result is claimed.",
    "No Clay-problem closure is claimed."
]
for token in required:
    assert token in doc, token

readme_required = [
    "FO4 Math-AI Terminal Question",
    "OPEN_PROBLEM_REQUIRED",
    "FO4CycleOverlapRankRigidityDichotomy",
    "FO4CycleOverlapRankRigidity_or_CounterexampleFamily"
]
for token in readme_required:
    assert token in readme, token

combined = "\n".join([
    json.dumps(base, sort_keys=True),
    json.dumps(artifact, sort_keys=True),
    doc,
    readme,
])

forbidden = [
    "Chronos-RR is solved",
    "H4.1/FGL is solved",
    "UniversalFiberEntropyGap is proved",
    "P vs NP is solved",
    "Clay problem is solved",
    "unrestricted graph rigidity is proved",
    "FO4CycleOverlapRankRigidityDichotomy is proved",
    "theorem_closure\": true"
]
for token in forbidden:
    assert token not in combined, token

print("FO4 Math-AI terminal question verified: OPEN_PROBLEM_REQUIRED")
