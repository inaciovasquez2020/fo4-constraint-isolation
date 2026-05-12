# FO4 Constraint Isolation

Standalone boundary module for isolating the exact FO^4 constraint surface used in Cayley/local-rigidity arguments.

## Status

FO4_CONSTRAINT_ISOLATION_ONLY

## Purpose

This repository records the formal boundary:

- FO^4 is treated as a fixed finite-variable constraint surface.
- The package isolates admissible FO^4 assumptions.
- The package does not prove unrestricted graph rigidity.
- The package does not prove Chronos-RR, H4.1/FGL, UniversalFiberEntropyGap, P vs NP, or any Clay-problem result.

## Core invariant

Finite-variable soundness requires that every exported constraint remain inside the FO^4 variable budget.

## Boundary

This repository is a proof-hygiene and status-isolation layer only.

<!-- FO4_SOURCE_OF_TRUTH_BEGIN -->
## Source of Truth

This repository is the canonical public FO4 constraint-isolation package.

Canonical status: `FO4_CONSTRAINT_ISOLATION_ONLY`

Canonical artifact: `artifacts/fo4_constraint_isolation.json`

Canonical verifier: `python3 tools/verify_fo4_constraint_isolation.py`

Canonical boundary:

This repository isolates the FO^4 variable-budget constraint surface. It does not prove unrestricted graph rigidity, unrestricted Cayley-graph rigidity, Chronos-RR, H4.1/FGL, UniversalFiberEntropyGap, P vs NP, or any Clay-problem result.
<!-- FO4_SOURCE_OF_TRUTH_END -->

## FO4 Math-AI Terminal Question

Status: `OPEN_PROBLEM_REQUIRED`

Terminal object: `FO4CycleOverlapRankRigidityDichotomy`

Weakest missing object: `FO4CycleOverlapRankRigidity_or_CounterexampleFamily`

Canonical artifact: `artifacts/fo4_math_ai_terminal_question_2026_05_12.json`

Canonical verifier: `python3 tools/verify_fo4_math_ai_terminal_question.py`

Boundary: this records the full terminal question needed to move beyond FO4 constraint isolation. It does not prove unrestricted graph rigidity, unrestricted Cayley-graph rigidity, Chronos-RR, H4.1/FGL, UniversalFiberEntropyGap, P vs NP, or any Clay-problem result.
