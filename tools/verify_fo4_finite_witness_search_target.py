#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

base = json.loads((ROOT / "artifacts/fo4_math_ai_terminal_question_2026_05_12.json").read_text())
artifact = json.loads((ROOT / "artifacts/fo4_finite_witness_search_target_2026_06_23.json").read_text())
doc = (ROOT / "docs/status/FO4_FINITE_WITNESS_SEARCH_TARGET_2026_06_23.md").read_text()

assert base["status"] == "OPEN_PROBLEM_REQUIRED"
assert base["terminal_question"]["name"] == "FO4CycleOverlapRankRigidityDichotomy"
assert base["theorem_closure"] is False

assert artifact["artifact"] == "fo4_finite_witness_search_target"
assert artifact["status"] == "FINITE_WITNESS_SEARCH_TARGET_ONLY"
assert artifact["logic_surface"] == "FO4"
assert artifact["variable_budget"] == 4
assert artifact["theorem_closure"] is False
assert artifact["depends_on"] == "fo4_math_ai_terminal_question"
assert artifact["target_object"]["name"] == "FO4FiniteCycleOverlapWitnessSearch"

required_doc = [
    "Status: `FINITE_WITNESS_SEARCH_TARGET_ONLY`",
    "FO4FiniteCycleOverlapWitnessSearch",
    "finite maximum degree `Delta`",
    "finite radius `R`",
    "finite graph-size cap `N`",
    "does not solve `FO4CycleOverlapRankRigidityDichotomy`",
    "does not prove the rigidity branch",
    "does not prove the counterexample-family branch",
    "does not prove unrestricted graph-rigidity",
    "does not prove unrestricted Cayley-graph rigidity",
]
for token in required_doc:
    assert token in doc, token

required_artifact = [
    "formal definition of FO4 radius-R rooted local type inside this repo",
    "formal definition of R-local cycle-overlap rank inside this repo",
    "verified finite graph enumerator or externally supplied finite witness corpus",
    "proof that the finite proxy agrees with the intended FO4/rank definitions on the searched class",
]
for token in required_artifact:
    assert token in artifact["blocked_until"], token

combined = "\n".join([
    json.dumps(artifact, sort_keys=True),
    doc,
])

forbidden = [
    "FO4CycleOverlapRankRigidityDichotomy is proved",
    "rigidity branch is proved",
    "counterexample-family branch is proved",
    "unrestricted graph rigidity is proved",
    "unrestricted Cayley-graph rigidity is proved",
    "Chronos-RR is solved",
    "H4.1/FGL is solved",
    "UniversalFiberEntropyGap is proved",
    "P vs NP is solved",
    "Clay problem is solved",
    "theorem_closure\": true",
]
for token in forbidden:
    assert token not in combined, token

print("FO4_FINITE_WITNESS_SEARCH_TARGET_OK")
