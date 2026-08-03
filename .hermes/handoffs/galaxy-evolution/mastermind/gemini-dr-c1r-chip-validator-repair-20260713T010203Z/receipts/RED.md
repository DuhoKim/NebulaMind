# RED receipt — T0–T15 contract established

Timestamp: 2026-07-13T01:38:25Z
Packet: `gemini-dr-c1r-chip-validator-repair-20260713T010203Z`

## Fixture supersession

Goru's second-pass fact files were rejected and preserved as invalid custody evidence. Hwao approved packet-local parse5 supersession in `HWAO_GORU_FIXTURE_ADJUDICATION.md`. The corrected deterministic generator reproduced every published pin: 108 chips; S1/S2/S3/S4/S5/ledger = 40/8/3/9/2/46; 46 ledger pairs; 37 unique indices; 0 real conflicts; S2 Citation chips `[27,28,10,11,15,20,30,30]`; four GAP units; 12 orphan indices; 9 duplicate rows; 46 blank short names. The deliberately corrupted v2 fixture produces a real index-10→two-URL conflict.

## Baseline state

`capture/structured_capture_v2.js`, `validator/validator_v2.py`, and `validator/contract_spec_v2.json` began as byte-identical copies of the sealed v1 files. `receipts/BASELINE_V2_COPY.json` records the hashes.

## RED execution

Command family:
- backend venv pytest for Python tests
- Node 22.23.1 for the real-HTML capture test

Observed results:

- T0 custody: `3 passed`; exit 0.
- T1–T6 capture: exit 1 at the first intended assertion, schema actual `NM_GEMINI_RENDERED_DOM_V1` vs expected `NM_GEMINI_RENDERED_DOM_V2`.
- T7–T13 validator: `7 failed`; exit 1. Failures match missing behaviors: BAD_STRUCTURE coupling with `set()`, bare-word fraction false positive, untyped C4, row-level C6 anchoring, no exact sentinel defect, no typed C7 integrity finding, and no manual-review boundary.
- T14–T15 integration/determinism: `1 failed`; exit 1 at the intended v1-vs-v2 schema assertion.

No syntax/import/fixture-custody failure occurred. The suite is RED because the copied v1 implementation lacks the newly specified behavior, not because the tests are broken.

RED_EXIT_CODES custody=0 capture=1 validator=1 integration=1

TORI_C1R_REPAIR_RED_20260713T010203Z
