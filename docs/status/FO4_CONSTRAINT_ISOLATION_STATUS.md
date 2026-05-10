# FO4 Constraint Isolation Status

Status: FO4_CONSTRAINT_ISOLATION_ONLY

## Object

This module isolates the FO^4 constraint surface used by local-rigidity and Cayley-graph arguments.

## Admissible claims

- FO^4 variable-budget boundary is explicitly registered.
- FO^4 assumptions are separated from general FO^k assumptions.
- Cayley/local-rigidity downstream arguments may cite this as a constraint-isolation layer.

## Non-claims

- No unrestricted graph-rigidity theorem is proved.
- No unrestricted Cayley-graph rigidity theorem is proved.
- No Chronos-RR closure is claimed.
- No H4.1/FGL closure is claimed.
- No UniversalFiberEntropyGap theorem is claimed.
- No P vs NP result is claimed.
- No Clay-problem closure is claimed.

## Required invariant

Every registered FO4 constraint must satisfy:

variable_budget = 4
status = "FO4_CONSTRAINT_ISOLATION_ONLY"
theorem_closure = false
