# Tori A-P3 baseline-test migration note

The first full A-P3 run produced two expected legacy-test conflicts, not implementation regressions:

1. `test_t9_c4_uses_typed_same_cell_claim_units` still required the v2 S2 Result-cell `UNCITED_CELL_CLAIM` that D3 explicitly removes in favor of row-owned Citation plus manual Result review.
2. `test_t14_exact_mechanical_residue...` still pinned the v2 17/73 residue and embedded near-duplicate evidence inside the C7 hard failure, both superseded by the countersigned r3 19/82 pin and manual `C7_NEAR_DUPLICATE`.

The tests are migrated narrowly to the countersigned behavior. No coverage is deleted: S2 typed result/citation behavior, exact residue, C7 mechanical counts, near-duplicate manual routing, determinism, and all unrelated baseline assertions remain.

This is a test expectation migration for changed requirements, not a weakening to make implementation pass.
