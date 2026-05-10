import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_artifact_status_and_budget():
    artifact = json.loads((ROOT / "artifacts/fo4_constraint_isolation.json").read_text())
    assert artifact["status"] == "FO4_CONSTRAINT_ISOLATION_ONLY"
    assert artifact["variable_budget"] == 4
    assert artifact["logic_surface"] == "FO4"
    assert artifact["theorem_closure"] is False

def test_status_doc_contains_boundaries():
    text = (ROOT / "docs/status/FO4_CONSTRAINT_ISOLATION_STATUS.md").read_text()
    required = [
        "No unrestricted graph-rigidity theorem is proved.",
        "No unrestricted Cayley-graph rigidity theorem is proved.",
        "No Chronos-RR closure is claimed.",
        "No H4.1/FGL closure is claimed.",
        "No UniversalFiberEntropyGap theorem is claimed.",
        "No P vs NP result is claimed.",
        "No Clay-problem closure is claimed."
    ]
    for token in required:
        assert token in text

def test_no_forbidden_overclaim_tokens():
    combined = "\n".join(
        path.read_text()
        for path in [
            ROOT / "README.md",
            ROOT / "docs/status/FO4_CONSTRAINT_ISOLATION_STATUS.md",
            ROOT / "artifacts/fo4_constraint_isolation.json"
        ]
    )
    forbidden = [
        "Chronos-RR is solved",
        "H4.1/FGL is solved",
        "UniversalFiberEntropyGap is proved",
        "P vs NP is solved",
        "Clay problem is solved",
        "unrestricted graph rigidity is proved"
    ]
    for token in forbidden:
        assert token not in combined
