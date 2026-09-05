CONTROL MISMATCH: pool controls reproduced 12,100 / 46 / 12,054, but the 2,000-row ordering control did not reproduce (first difference at rank 1).

- Candidate pool: 12,100 (expected 12,100).
- Guard dropped: 46 (expected 46).
- Guarded pool: 12,054 (expected 12,054).
- Frozen validation ordering: mismatch at rank 1; prescribed `h mod 2^32` order gives GZ1_OBJID `588017977829884152`, while `VALIDATION_SELECTION_V29_20260905.csv` gives `587722981736120347`. Consequently 0 of the required 2,000 ranks were certified, and corpus identity outputs were not emitted.
- Exact disposition fields: completeness receipt top-level field `terminal_dispositions`; each GZ1 object ID is a mapping key and its terminal-disposition string is the corresponding mapping value. Required exact value: `NO-DR10-WITHIN-1ARCSEC`. `checkpoint.jsonl` was used as the named checkpoint context; its rows contain chunk-level query fields rather than per-object terminal dispositions.
- Guard builder runtime: see the exact `runtime_seconds` in `guarded_pool_receipt.json` (approximately 4 seconds in this run).
- Corpus builder time to control stop: approximately 0.3 seconds.
- Did not reproduce: the frozen 2,000-row validation selection under the newly specified low-32-bit SHA-256 ordering. Per instruction, no alternative ordering was tried and no downstream tuning, holdout, or fresh-validation outputs were generated.
