import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_terminal_question_artifact_status():
    artifact = json.loads((ROOT / "artifacts/fo4_math_ai_terminal_question_2026_05_12.json").read_text())
    assert artifact["status"] == "OPEN_PROBLEM_REQUIRED"
    assert artifact["logic_surface"] == "FO4"
    assert artifact["variable_budget"] == 4
    assert artifact["theorem_closure"] is False
    assert artifact["missing_lemma"] == "FO4CycleOverlapRankRigidity_or_CounterexampleFamily"

def test_terminal_question_contains_both_branches():
    text = (ROOT / "docs/status/FO4_MATH_AI_TERMINAL_QUESTION_2026_05_12.md").read_text()
    assert "Rigidity branch" in text
    assert "Counterexample branch" in text
    assert "FO4CycleOverlapRankRigidityDichotomy" in text

def test_terminal_question_preserves_boundary():
    combined = "\n".join([
        (ROOT / "README.md").read_text(),
        (ROOT / "docs/status/FO4_MATH_AI_TERMINAL_QUESTION_2026_05_12.md").read_text(),
        (ROOT / "artifacts/fo4_math_ai_terminal_question_2026_05_12.json").read_text(),
    ])
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
        assert token in combined
    forbidden = [
        "Chronos-RR is solved",
        "H4.1/FGL is solved",
        "UniversalFiberEntropyGap is proved",
        "P vs NP is solved",
        "Clay problem is solved",
        "unrestricted graph rigidity is proved",
        "FO4CycleOverlapRankRigidityDichotomy is proved"
    ]
    for token in forbidden:
        assert token not in combined
