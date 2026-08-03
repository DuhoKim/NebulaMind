# Kun Write-Scope Audit

Packet: `gemini-dr-c1r-chip-validator-repair-20260713T010203Z`

Scope audited against `KUN_GREEN_BRIEF.md`: allowed writes were `tests/run_all.sh` and new files under `receipts/`. No capture, validator, fixture, design, readjudication, sealed packet, product code, git, dashboard, DB, deploy, browser, network, or live Gemini action was taken.

## Commands and Exit Codes

- `bash -n tests/run_all.sh` -> exit 0
- `tests/run_all.sh` -> exit 0 after final harness repair
- `find tests validator -path '*/__pycache__/*' -type f -print` -> exit 0, no files printed after cleanup and final harness rerun
- `find ../gemini-dr-revised-canary-20260712T045317Z ../dr-c1r-root-cause-20260712T163156Z -type f -print0 | xargs -0 shasum -a 256 | sort > receipts/_kun_green_current_sealed_hashes.txt` -> exit 0
- `awk ... receipts/KUN_IMMUTABLE_INPUT_RECEIPT.md | sort > receipts/_kun_green_pref_sealed_hashes.txt` -> exit 0
- `diff -u receipts/_kun_green_pref_sealed_hashes.txt receipts/_kun_green_current_sealed_hashes.txt` -> exit 0
- `wc -l receipts/_kun_green_pref_sealed_hashes.txt receipts/_kun_green_current_sealed_hashes.txt` -> exit 0; 78 and 78

## Hashes

- `tests/run_all.sh`: `c39eb96ac7cbb7b5c7d95b9690b801ff3f21d869b4634b738391b126c0f1fdfe`
- preflight sealed hash list: `08a2e77a09b94b80b66a4c83c1038ba94514e849964acb0a9309b04234bdf3d3`
- current sealed hash list: `08a2e77a09b94b80b66a4c83c1038ba94514e849964acb0a9309b04234bdf3d3`

RUN_RECEIPT named custody files rechecked:
- `prompt_submitted.md`: `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef`
- `body.md`: `8a130c5a6fc1b1f5d534888d3fb20806230b8b4c7737cb00f9bfb18ad0d6bc00`
- `rendered_body.html`: `78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc`
- `structured_capture.json`: `2d10e34a46c609b713d980ded746c8bf4f1214ea7213603535cd3c7e271ec468`
- `validator_result.json`: `34f525a58b1c71d237b1723fc42bfab5acfaf631e9b25175a703462e108c91f4`
- `manual_review_gate.json`: `b9522943dfd6c3c8788ec881abdb376f2de5661420ada76b1ce188e62dc95d5b`
- `quota_postflight.json`: `7ffdc56b30f53d38199a735cb9e1d22bf893625f0641e32293fd1090c4d64ceb`
- `RUN_RECEIPT_PRE_CLEANUP.json`: `54d119d8b64ab120cb29e8baa06ad9c9dd1cb43e09cc2810c817da72fbeaaa2a`
- `cleanup_receipt.json`: `2b4e0e8f1c2e702db5670f320cf3bb56435e0ecb3d4060a9fffd1b1a0a454f01`

## Task Writes

Modified allowed existing file:
- `tests/run_all.sh`

New receipt-scoped files/directories used for verification evidence:
- `receipts/_kun_green_gen_run1/`
- `receipts/_kun_green_gen_run2/`
- `receipts/_kun_green_det_run1/`
- `receipts/_kun_green_det_run2/`
- `receipts/_kun_green_pref_sealed_hashes.txt`
- `receipts/_kun_green_current_sealed_hashes.txt`
- this receipt and the two companion Kun GREEN receipts

Temporary Python bytecode files produced by early harness runs were removed, and the harness was hardened with `PYTHONDONTWRITEBYTECODE=1`, `-B`, and `--assert=plain`. Final audit found no `tests/` or `validator/` bytecode files.

KUN_C1R_WRITE_SCOPE_GREEN_20260713T010203Z
