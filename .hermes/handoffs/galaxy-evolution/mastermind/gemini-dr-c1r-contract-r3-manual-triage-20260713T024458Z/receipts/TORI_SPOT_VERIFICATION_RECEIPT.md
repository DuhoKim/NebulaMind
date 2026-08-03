# Tori P3 spot-verification receipt

Status: PASS
Amendment applied: `HWAO_PLAN_AMENDMENT_1.md`

## Sampling

Fifteen entries were sampled, satisfying `min(2, lane size)` for every non-empty lane and total ≥15:

- `VERIFY_UNCERTAINTY_OR_SCOPE` (4): M001, M005, M010, M018
- `VERIFY_SOURCE_FIDELITY` (8): M019, M028, M044, M050, M053, M062, M064, M065
- `VERIFY_SCIENTIFIC_COMPARABILITY` (3): M066, M069, M073

For each sample Tori independently checked:

1. manual ID and 1-based finding ordinal;
2. clause, code, status, and source_refs against `validator_result_v2.json`;
3. evidence snippet against the source finding;
4. table cell, bullet, or GAP text against the repaired structured capture at the exact source_ref;
5. assigned lane against Hwao's pinned definition;
6. classification reason as routing only, not scientific adjudication.

## Sample results

| ID | Source unit | Lane | Result |
|---|---|---|---|
| M001 | table_row_4:3 | VERIFY_UNCERTAINTY_OR_SCOPE | PASS |
| M005 | table_row_6:2 | VERIFY_UNCERTAINTY_OR_SCOPE | PASS |
| M010 | table_row_9:2 | VERIFY_UNCERTAINTY_OR_SCOPE | PASS |
| M018 | gap_line_4 | VERIFY_UNCERTAINTY_OR_SCOPE | PASS |
| M019 | table_row_4:1 | VERIFY_SOURCE_FIDELITY | PASS |
| M028 | table_row_6:2 | VERIFY_SOURCE_FIDELITY | PASS |
| M044 | table_row_10:3 | VERIFY_SOURCE_FIDELITY | PASS |
| M050 | bullet_23 | VERIFY_SOURCE_FIDELITY | PASS |
| M053 | table_row_28:1 | VERIFY_SOURCE_FIDELITY | PASS |
| M062 | gap_line_1 | VERIFY_SOURCE_FIDELITY | PASS |
| M064 | aggregate: 62 resolved inline citation occurrences | VERIFY_SOURCE_FIDELITY | PASS |
| M065 | aggregate: 62 resolved inline citation occurrences | VERIFY_SOURCE_FIDELITY | PASS |
| M066 | table_row_14:3 | VERIFY_SCIENTIFIC_COMPARABILITY | PASS |
| M069 | table_row_17:3 | VERIFY_SCIENTIFIC_COMPARABILITY | PASS |
| M073 | table_row_21:3 | VERIFY_SCIENTIFIC_COMPARABILITY | PASS |

No sampled disagreement was found.

## Zero-lane audit

Tori scanned all 73 lane assignments, not only the sample:

- all 18 C3 manual findings conservatively route to `VERIFY_UNCERTAINTY_OR_SCOPE`;
- all 47 C4 manual findings conservatively route to `VERIFY_SOURCE_FIDELITY`;
- all 8 C6 manual findings conservatively route to `VERIFY_SCIENTIFIC_COMPARABILITY`;
- `CONTRACT_R3_CHANGE` is correctly zero because the D1–D5 items absorbed by r3 are deterministic findings outside the 73-entry queue;
- `IGNORE_FOR_THIS_CONTRACT_TEST` is correctly zero because every manual entry retains a genuine review obligation; none is merely a formatting-only duplicate.

The two `ZERO_LANE` statements in `TRIAGE_LEDGER.md` are countersigned. No entry was forced into a lane to satisfy sampling.

## Boundary

This verifies custody and routing only. No cited source was retrieved, and no scientific, source-fidelity, uncertainty, or comparability conclusion was made. All such work remains separately gated.

TORI_R3_TRIAGE_SPOT_VERIFICATION_GREEN_20260713T024458Z
