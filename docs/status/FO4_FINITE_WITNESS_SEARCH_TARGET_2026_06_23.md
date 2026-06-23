# FO4 Finite Witness Search Target

Status: `FINITE_WITNESS_SEARCH_TARGET_ONLY`

This record adds a bounded finite-witness search target below the existing FO4 Math-AI terminal question.

Target object: `FO4FiniteCycleOverlapWitnessSearch`

Purpose: make the terminal dichotomy experimentally inspectable on finite bounded graph families without claiming either branch.

## Bounded parameters

- finite maximum degree `Delta`
- finite radius `R`
- finite graph-size cap `N`
- declared FO4 radius-`R` rooted local type proxy
- declared `R`-local cycle-overlap rank proxy

## Admissible output

- finite witness candidate
- finite obstruction candidate
- empty bounded search result

## Blocked until

- formal definition of FO4 radius-`R` rooted local type inside this repo
- formal definition of `R`-local cycle-overlap rank inside this repo
- verified finite graph enumerator or externally supplied finite witness corpus
- proof that the finite proxy agrees with the intended FO4/rank definitions on the searched class

## Boundary

This target does not solve `FO4CycleOverlapRankRigidityDichotomy`.

It does not prove the rigidity branch.

It does not prove the counterexample-family branch.

It does not prove unrestricted graph-rigidity.

It does not prove unrestricted Cayley-graph rigidity.

It does not prove Chronos-RR, H4.1/FGL, UniversalFiberEntropyGap, P vs NP, or any Clay-problem result.
