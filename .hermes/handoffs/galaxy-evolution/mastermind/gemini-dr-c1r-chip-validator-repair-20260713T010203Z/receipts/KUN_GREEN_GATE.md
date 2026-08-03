# Kun GREEN Gate Rev2

Packet: `gemini-dr-c1r-chip-validator-repair-20260713T010203Z`
Role: independent final custody/reproducibility gate.

Conclusion: GREEN gate passed locally. C1r remains FAIL_CLOSED; this gate verifies the offline repair pipeline and deterministic residue, not scientific/source-fidelity acceptance.

Revision: rev2 after `receipts/TORI_KUN_GREEN_REV1_SCOPE_BLOCKED.md`.

Rev1 scope correction acknowledged: rev1 GREEN findings were not accepted as final because packet-root `_tmp_run_all/` remained after the harness. Rev1 receipts are preserved byte-identically:
- `receipts/KUN_FIXTURE_COUNTERSIGN_REV1_SCOPE_INVALID.md`: `0554025a3d1f0d1604a86fd907547b8fa8fcd9f79ca102a82e83e5bd7e69da03`
- `receipts/KUN_WRITE_SCOPE_AUDIT_REV1_SCOPE_INVALID.md`: `edbca3ca5c482e5282dc0c39fa601eadea4ed43aded2bc99d0eb06d27fbe9fca`
- `receipts/KUN_GREEN_GATE_REV1_SCOPE_INVALID.md`: `35f40eb57daaad2d6e016b522deb84f0d74036633751b2aff936058ac3a795fe`

Rev2 harness correction: temp use moved to `receipts/_tmp_run_all`, an EXIT trap removes it, packet-root `_tmp_run_all/` was removed, and the full harness reran GREEN with no temp or bytecode output left outside `receipts/`.

## Required Reads Verified

Read and reconciled:
- `HWAO_IMPLEMENTATION_DIRECTION.md`
- `HWAO_GORU_FIXTURE_ADJUDICATION.md`
- `HWAO_T14_DEVIATION_ADJUDICATION.md`
- `design/LANA_T14_COUNTERSIGN.md`
- `fixtures/TORI_FIXTURE_SUPERSEDE_RECEIPT.md`
- `receipts/RED.md`
- `readjudication/READJUDICATION_SUMMARY.json`
- `readjudication/RESIDUE_REPORT.md`

## Commands and Exit Codes

Harness:
- `bash -n tests/run_all.sh` -> exit 0
- `rm -rf _tmp_run_all` -> exit 0
- `tests/run_all.sh` -> exit 0
- `test ! -e _tmp_run_all` -> exit 0
- `test ! -e receipts/_tmp_run_all` -> exit 0
- `find . -maxdepth 3 -path './receipts' -prune -o \( -name '_tmp_run_all' -o -name '_tmp*' -o -path '*/__pycache__/*' \) -print` -> exit 0, no files printed

Harness command coverage:
- `/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -B -m py_compile validator/validator_v2.py validator/run_validator_v2.py`
- `node -e require(process.argv[1]); capture/structured_capture_v2.js`
- `node --check capture/run_capture_v2.mjs`
- `node tests/test_capture_v2.mjs`
- `/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -B -m pytest -q tests`

Harness output counts:
- Node capture test: `T1-T6 capture RED/GREEN contract passed`
- Pytest: `11 passed in 0.23s`

Independent determinism:
- `node capture/run_capture_v2.mjs fixtures/rendered_body.html fixtures/body.md receipts/_kun_green_det_run1/structured_capture_v2.json` -> exit 0
- `node capture/run_capture_v2.mjs fixtures/rendered_body.html fixtures/body.md receipts/_kun_green_det_run2/structured_capture_v2.json` -> exit 0
- `/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python validator/run_validator_v2.py --body fixtures/body.md --structured receipts/_kun_green_det_run1/structured_capture_v2.json --spec validator/contract_spec_v2.json --output receipts/_kun_green_det_run1/validator_result_v2.json` -> exit 0
- `/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python validator/run_validator_v2.py --body fixtures/body.md --structured receipts/_kun_green_det_run2/structured_capture_v2.json --spec validator/contract_spec_v2.json --output receipts/_kun_green_det_run2/validator_result_v2.json` -> exit 0
- `cmp -s receipts/_kun_green_det_run1/structured_capture_v2.json receipts/_kun_green_det_run2/structured_capture_v2.json` -> exit 0
- `cmp -s receipts/_kun_green_det_run1/validator_result_v2.json receipts/_kun_green_det_run2/validator_result_v2.json` -> exit 0

Residue/governance:
- `node -e <validator result status counter>` -> exit 0
- `rg -n "mechanical only|does not certify science|source fidelity|retroactively accept|FAIL_CLOSED|..." readjudication/RESIDUE_REPORT.md` -> exit 0
- `node -e <artifact regression checker>` -> exit 0

## Deterministic Output Hashes

Independent run 1:
- capture: `e26819dbc90a040ecc228639fbee3e2a68f8942fa9d26b9458aee71bbc65e3e9`
- validator: `ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52`

Independent run 2:
- capture: `e26819dbc90a040ecc228639fbee3e2a68f8942fa9d26b9458aee71bbc65e3e9`
- validator: `ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52`

Published readjudication:
- `readjudication/structured_capture_v2.json`: `e26819dbc90a040ecc228639fbee3e2a68f8942fa9d26b9458aee71bbc65e3e9`
- `readjudication/validator_result_v2.json`: `ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52`

## 17-Finding Residue

Validator output:
- overall: `FAIL`
- total findings: 94
- PASS: 4
- FAIL: 17
- MANUAL_REVIEW_REQUIRED: 73

FAIL breakdown:
- `C2:SENTINEL_FORMAT_DEFECT`: 1
- `C4:UNCITED_CELL_CLAIM`: 8
- `C6:UNLABELED_COMPARISON`: 6
- `C6:MISSING_QUALIFIER`: 1
- `C7:C7_INTEGRITY_FAILURE`: 1

This matches the Hwao-adjudicated and Lana-countersigned amended T14 residue: 17 FAIL findings = C2 sentinel 1 + C4 uncited result 8 + C6 unlabeled comparison 6 + C6 missing qualifier 1 + C7 integrity 1.

Artifact regressions absent in independent validator output:
- `EMPTY_TABLE_CELL`: absent
- `BAD_STRUCTURE`: absent
- fail codes limited to `C7_INTEGRITY_FAILURE`, `MISSING_QUALIFIER`, `SENTINEL_FORMAT_DEFECT`, `UNCITED_CELL_CLAIM`, and `UNLABELED_COMPARISON`

## Residue Report Governance

`readjudication/RESIDUE_REPORT.md` states:
- result remains `FAIL_CLOSED`
- re-adjudication is mechanical only
- it does not certify science or source fidelity
- it does not retroactively accept C1r or authorize reuse as evidence
- no live Gemini run, browser action, network call, DB/wiki/product write, publication, deploy, restart, git action, or public-cockpit change occurred

## Sealed Inputs

All 78 sealed files from `../gemini-dr-revised-canary-20260712T045317Z` and `../dr-c1r-root-cause-20260712T163156Z` were rehashed and diffed against `receipts/KUN_IMMUTABLE_INPUT_RECEIPT.md`; diff exit 0. RUN_RECEIPT-named byte files still match their custody hashes.

KUN_C1R_REPAIR_GREEN_GATE_20260713T010203Z
