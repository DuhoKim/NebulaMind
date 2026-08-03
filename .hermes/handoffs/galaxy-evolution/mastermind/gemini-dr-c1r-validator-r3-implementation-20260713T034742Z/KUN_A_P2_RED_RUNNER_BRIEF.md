# Kun A-P2 independent RED runner brief

A-P2 test authoring and two Tori spec corrections are complete. Independently read:

- `design/LANA_R3_RED_PIN.md`;
- `design/HWAO_R3_RED_PIN_COUNTERSIGN.md`;
- `receipts/KUN_INPUT_CUSTODY_RECEIPT.md`;
- `receipts/TORI_A_P2_TEST_SPEC_REVIEW.md` and `_2.md`;
- current Gate A tests/fixtures and packet-local v3 working code.

Do not modify tests, fixtures, validator, capture, spec, or runners.

Run independently:

1. Baseline Python tests and Node capture baseline; verify GREEN.
2. New r3 RED Python tests; verify they fail for missing D5/D4/D1/D3/integration behavior while D2 positive/negative family already passes because v2 retained that behavior.
3. Verify T-CUST reference hashes are GREEN, not the cause of RED.
4. Audit test shapes: exact 19 deterministic and exact 82 manual identity multiset; exact D1 refs; actual D5 `parent_path`; D4 arXiv normalization and 14↔29 manual; D3 empty guard and exact row reviews; deterministic double-run.
5. Hash the RED test files and note no implementation files changed by the Goru authoring phase.

Write only `receipts/KUN_RED_RECEIPT.md` with exact commands, pass/fail counts, failing test names/reasons, custody results, and either GREEN-to-open-A-P3 or STOP. End with `KUN_GATE_A_RED_RECEIPT_DONE_20260713T034742Z`.

No network/live/browser/DB/dashboard/deploy/cron/git action. Receipt-scoped temporary output only; clean it before finishing.
