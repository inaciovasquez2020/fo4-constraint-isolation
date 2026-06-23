import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def test_fo4_finite_witness_search_target_artifact():
    artifact = json.loads((ROOT / "artifacts/fo4_finite_witness_search_target_2026_06_23.json").read_text())
    assert artifact["status"] == "FINITE_WITNESS_SEARCH_TARGET_ONLY"
    assert artifact["logic_surface"] == "FO4"
    assert artifact["variable_budget"] == 4
    assert artifact["theorem_closure"] is False
    assert artifact["target_object"]["name"] == "FO4FiniteCycleOverlapWitnessSearch"

def test_fo4_finite_witness_search_target_boundary_doc():
    text = (ROOT / "docs/status/FO4_FINITE_WITNESS_SEARCH_TARGET_2026_06_23.md").read_text()
    assert "does not solve `FO4CycleOverlapRankRigidityDichotomy`" in text
    assert "does not prove the rigidity branch" in text
    assert "does not prove the counterexample-family branch" in text
    assert "does not prove unrestricted graph-rigidity" in text

def test_fo4_finite_witness_search_target_verifier():
    result = subprocess.run(
        [sys.executable, "tools/verify_fo4_finite_witness_search_target.py"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    assert "FO4_FINITE_WITNESS_SEARCH_TARGET_OK" in result.stdout
