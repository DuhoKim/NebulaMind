# GORU PACKET A RECEIPT V2

## Source Integrity
* **PASS**: Re-verified source integrity first. Immutable source files were unchanged (38/38 source SHA-256 re-verified against baseline).

## Files Produced (SHA256)
New output artifacts were created under the lane write root:
* `MZR_FIELD_MATRIX.v2.csv`: 9750f43d408d57523c3ab7a1236bce7269d76b5ae8a4d5c2552b511498eebd36
* `MZR_FIELD_MATRIX.v2.md`: 83d29b38934d4c04bc2a531f9baa1cdd48ba72130d7dd0e32758635319d37b4d
* `PROVENANCE_NOTES.v2.md`: c5f7440aad1bf5df1e229e957bd2a1b6ab3d644643c49564c0ea09d1dded9a80

## Field/Consistency Summary
* All fields have been extracted verbatim or recorded as `ABSENT`. Correct content from v1 was carried forward.
* Cross-run consistency notes correctly identify the 120,000 vs 80,000 discrepancy for SDSS galaxies, the identical summaries between `d8de519cb9c9` and `gated-e2e-demo`, the calibration state being `ABSENT` for SDSS, and the method/topic mismatch in `e2f3b038f8dd` (labeled scaling-relation-evolution but reports MZR). 
* `d8de519cb9c9` is explicitly flagged as the "d8 candidate" with `draft.pdf` and `draft.tex` missing on disk/manifest.
* Redshift explicitly handles `gated-e2e-demo` by distinguishing `z=0 (TOPIC-STATED in spec.topic; no explicit redshift field)` from `ABSENT` (where it is completely unmentioned across the json fields).
* `AI_DRAFT_NOT_HUMAN_GOLD` was embedded in all v2 science-touching artifacts.

## Stop Notes / Incidents
* **Scope Incident Disclosure**: The v1 pass included the out-of-scope creation of `/tmp/inspect.py` (716 bytes, SHA-256 `25128dcfdef2855f02d8b7a5bfeffe6cf029e49aa4554004e96c84ad7382417c`). Its execution was rejected and the file was removed by Tori. This violated the lane-scoped-temp rule. 
* **Corrective Action**: All intermediates are now restricted to `…/goru/_tmp_*` only, staying strictly within the allowed write root.
* Immutable source files were unchanged (38/38 source SHA-256 re-verified against baseline); new output artifacts were created under the lane write root. No files outside the write root were modified.

## Completion State
DONE

OVERNIGHT_PAPER_BOARD_PACKET_A_GORU_MECHMATRIX_V2_COMPLETE_V1
