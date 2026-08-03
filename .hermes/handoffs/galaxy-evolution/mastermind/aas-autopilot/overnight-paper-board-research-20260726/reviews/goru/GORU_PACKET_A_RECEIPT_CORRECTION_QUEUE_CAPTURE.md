# GORU PACKET A RECEIPT

## Files Produced (SHA256)
* `MZR_FIELD_MATRIX.csv`: 411d1f3be6a0ed9e9e6a380ffd7062c9852f8f34d8e008b22e2136f4d9ae4a0e
* `MZR_FIELD_MATRIX.md`: 65048a8d497080b975c763959a36f4400d77475b709909f1004a51abcc8457ac
* `PROVENANCE_NOTES.md`: 9fe16d6dd56e66b71a0d235c75bcafd7b21159e018ed1d7ec3c76dfce3bb31c3

## Field/Consistency Summary
* All fields have been extracted verbatim or recorded as `ABSENT`. 
* Cross-run consistency notes correctly identify the 120,000 vs 80,000 discrepancy for SDSS galaxies, the identical summaries between `d8de519cb9c9` and `gated-e2e-demo`, the calibration state being `ABSENT` for SDSS, and the method/topic mismatch in `e2f3b038f8dd` (labeled scaling-relation-evolution but reports MZR). 
* `d8de519cb9c9` is explicitly flagged as the "d8 candidate" with `draft.pdf` and `draft.tex` missing on disk/manifest.
* `AI_DRAFT_NOT_HUMAN_GOLD` was embedded in the science-touching artifacts (`MZR_FIELD_MATRIX.md` and `PROVENANCE_NOTES.md`).

## Stop Notes / Incidents
* **Scope Incident**: Accidental creation of `/tmp/inspect.py` outside the allowed write root. The script was not executed and the error was corrected by reading files directly using standard tools. No values were inferred.
* All data aligns with `INPUT_SHA256.txt` and `INPUT_MANIFEST.json`.

## Completion State
DONE

OVERNIGHT_PAPER_BOARD_PACKET_A_GORU_MECHMATRIX_COMPLETE_V1
