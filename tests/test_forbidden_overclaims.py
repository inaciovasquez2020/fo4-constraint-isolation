from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCANNED = [
    ROOT / "README.md",
    ROOT / "docs/status/FO4_CONSTRAINT_ISOLATION_STATUS.md",
    ROOT / "artifacts/fo4_constraint_isolation.json",
]

FORBIDDEN = [
    "Chronos-RR is solved",
    "Chronos-RR is proved",
    "H4.1/FGL is solved",
    "H4.1/FGL is proved",
    "UniversalFiberEntropyGap is solved",
    "UniversalFiberEntropyGap is proved",
    "P vs NP is solved",
    "P≠NP is proved",
    "P = NP is proved",
    "Clay problem is solved",
    "Clay-problem closure is proved",
    "unrestricted graph rigidity is proved",
    "unrestricted Cayley-graph rigidity is proved",
]

def test_forbidden_overclaim_tokens_absent():
    combined = "\n".join(path.read_text() for path in SCANNED)
    for token in FORBIDDEN:
        assert token not in combined
