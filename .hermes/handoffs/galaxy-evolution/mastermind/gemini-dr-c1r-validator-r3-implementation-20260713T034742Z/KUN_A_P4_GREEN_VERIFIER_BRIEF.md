# Kun A-P4 independent GREEN verifier brief

A-P3 is complete. Read:

- coordination `HWAO_PARALLEL_PLAN.md`;
- Gate A `design/LANA_R3_RED_PIN.md` and `design/HWAO_R3_RED_PIN_COUNTERSIGN.md`;
- `receipts/KUN_RED_RECEIPT.md`;
- `receipts/TORI_A_P2_TEST_SPEC_REVIEW.md`, `_2.md`, `TORI_A_P3_BASELINE_TEST_MIGRATION.md`, and `TORI_IMPLEMENTATION_RECEIPT.md`;
- current Gate A working code/tests/fixtures/readjudication.

Do not edit code, tests, fixtures, spec, runners, or readjudication.

Independently:

1. Re-run all four Python test files and the Node capture baseline; require 14 Python tests and the Node suite GREEN.
2. Run Python and Node syntax checks.
3. Regenerate capture and validator output into receipt-scoped temporary files; compare byte-for-byte with `readjudication/structured_capture_v3.json` and `validator_result_v3.json`.
4. Independently assert exact 19 FAIL / 82 MANUAL / 4 PASS, exact deterministic family counts, absence of `C4:UNCITED_CELL_CLAIM`, exact eight D3 row refs, one C7 near-duplicate manual, exact D1 refs, and shared non-empty D5 `parent_path`.
5. Recheck all immutable v2 input hashes from P0 and all current implementation/output hashes.
6. Audit boundaries: no writes outside this Gate A packet, no network/live action, no generated caches/temp left behind.
7. Review the two test migrations and decide whether they preserve rather than weaken frozen r3 coverage.

Write only `receipts/KUN_GREEN_RECEIPT.md`, ending with `KUN_GATE_A_GREEN_RECEIPT_DONE_20260713T034742Z`. State GREEN or STOP. Clean receipt-scoped temporary files before finishing.
