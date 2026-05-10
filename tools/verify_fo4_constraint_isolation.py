#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

artifact = json.loads((ROOT / "artifacts/fo4_constraint_isolation.json").read_text())
status_doc = (ROOT / "docs/status/FO4_CONSTRAINT_ISOLATION_STATUS.md").read_text()
readme = (ROOT / "README.md").read_text()

assert artifact["artifact"] == "fo4_constraint_isolation"
assert artifact["status"] == "FO4_CONSTRAINT_ISOLATION_ONLY"
assert artifact["variable_budget"] == 4
assert artifact["logic_surface"] == "FO4"
assert artifact["theorem_closure"] is False

required_tokens = [
    "FO4_CONSTRAINT_ISOLATION_ONLY",
    "variable_budget = 4",
    "theorem_closure = false",
    "No unrestricted graph-rigidity theorem is proved.",
    "No unrestricted Cayley-graph rigidity theorem is proved.",
    "No Chronos-RR closure is claimed.",
    "No H4.1/FGL closure is claimed.",
    "No UniversalFiberEntropyGap theorem is claimed.",
    "No P vs NP result is claimed.",
    "No Clay-problem closure is claimed."
]

for token in required_tokens:
    assert token in status_doc, token

readme_tokens = [
    "FO4_CONSTRAINT_ISOLATION_ONLY",
    "FO^4",
    "does not prove unrestricted graph rigidity",
    "does not prove Chronos-RR"
]

for token in readme_tokens:
    assert token in readme, token

for forbidden in [
    "Chronos-RR is solved",
    "H4.1/FGL is solved",
    "UniversalFiberEntropyGap is proved",
    "P vs NP is solved",
    "Clay problem is solved",
    "unrestricted graph rigidity is proved"
]:
    assert forbidden not in readme
    assert forbidden not in status_doc
    assert forbidden not in json.dumps(artifact)

print("FO4 constraint isolation verified: FO4_CONSTRAINT_ISOLATION_ONLY")
