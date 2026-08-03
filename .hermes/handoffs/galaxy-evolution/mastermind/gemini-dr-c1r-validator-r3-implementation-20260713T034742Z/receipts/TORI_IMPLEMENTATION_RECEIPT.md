# Tori Gate A implementation receipt

Status: A-P3 GREEN; ready for independent A-P4 verification.

## RED custody

Kun independently certified the frozen RED phase in `KUN_RED_RECEIPT.md`:

- baseline Python: 8 passed;
- baseline Node capture: passed;
- r3 RED suite before implementation: 5 failed, 1 passed;
- failures were D5, D4, D1, D3, and exact integration; D2 already passed;
- immutable input hashes were GREEN.

## Packet-local implementation

Only Gate A working artifacts were changed:

- `capture/structured_capture_v3.js`: records the nearest gap paragraph's stable `data-path-to-node` as `parent_path` and fails capture closed if missing;
- `validator/validator_v3.py`: enforces one GAP per parent paragraph, canonicalizes arXiv URL forms, routes near duplicates to manual review, recognizes observation-target calibration cells missing the typed prefix, and makes each Section-2 Citation cell authoritative for its Result cell;
- `validator/contract_spec_v3.json`: records the implemented r3 policy fields;
- v3 runners: corrected version labels only.

No prior packet or fixture input was mutated.

## Narrow test migration

Two legacy v2 expectations conflicted directly with the countersigned r3 contract. `TORI_A_P3_BASELINE_TEST_MIGRATION.md` documents the narrow migration. Coverage was preserved: typed S2 routing, exact residue, C7 counts, near-duplicate routing, and determinism remain asserted.

One extra D3 extraction assertion incorrectly selected retained `table_row_10/11` manual findings because it used the prefix `table_row_1*`. It was narrowed to the exact frozen row set 14–21; the stronger exact 82-item multiset assertion had already passed before this correction.

## GREEN execution

Command:

`python3 -m pytest -q tests/test_validator_v3_baseline.py tests/test_integration_v3_baseline.py tests/test_validator_v3_r3_red.py tests/test_integration_v3_r3_red.py`

Result: **14 passed**.

Command:

`node --test tests/test_capture_v3_baseline.mjs`

Result: **1 suite passed**.

Syntax checks:

- Python `py_compile`: passed;
- `node --check` for capture and runner: passed.

## Fresh offline output

- schema: `NM_GEMINI_RENDERED_DOM_V3`;
- capture blocks: 46;
- validator overall: FAIL, as expected for the unchanged C1r artifact;
- exact statuses: 19 FAIL, 82 MANUAL_REVIEW_REQUIRED, 4 PASS;
- exact deterministic failure families match the countersigned r3 pin;
- `C4:UNCITED_CELL_CLAIM` is absent;
- one manual `C7_NEAR_DUPLICATE` is present.

Hashes:

- `structured_capture_v3.js`: `dd2a96707bc47456bbfc9383b384a164e1d86c7e8933b707a4ad22fa4d3fa924`
- `run_capture_v3.mjs`: `0c7dda7224ca767c12eb2f24da6238ab0da3f0bc922f4da3d3e1376f5ef9cb8a`
- `validator_v3.py`: `6aaf3348a47abbcce86919823b27896d0acebe6837a6dddb033d93e59dc82aae`
- `run_validator_v3.py`: `c0d10a6604f80d52e45e285f06da566a753112e5441f5a05842170305f339287`
- `contract_spec_v3.json`: `f5bd072f80ec35dc0fdc2414a43fadae698aeca3726ea7701c43e32855367b0d`
- `structured_capture_v3.json`: `95f0fe7a3fe710a4599188c18a2c39717887e970f62b64e36d10804b6afffe76`
- `validator_result_v3.json`: `5fa0adb8a91ce3af7f19cfc88582cde8e0065e58f996c5c8370bc1f6d944bed0`

## Boundaries

Offline packet only. No network, browser, live Deep Research, DB, dashboard, deploy, cron, git write, or publication action occurred in Gate A.

TORI_GATE_A_IMPLEMENTATION_GREEN_20260713T034742Z
