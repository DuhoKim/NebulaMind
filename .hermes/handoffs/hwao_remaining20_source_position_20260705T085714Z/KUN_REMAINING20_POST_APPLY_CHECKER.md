PASS.

Corrected proposal aligns with the applied rows and amended counts. I verified the 20 proposal IDs match the pre-apply pending IDs, and the applied nested queue fields match the proposal decisions/targets/roles with no meaningful mismatches. Final applied counts are correct under the amendment: `relink=17`, `route_kinetic_radio=5`, `leave_archival=14`, `pending=0`, all 36 reviewed.

The count correction correctly resolves the earlier expected-count failure without changing row decisions. Snapshot arithmetic closes: pre-pass `relink=8`, `route_kinetic_radio=3`, `leave_archival=5`, plus this pass `9/2/9`, equals final `17/5/14`.

Non-target preservation and format consistency are sufficient for reproducible receipts: amended validation has no failed checks, no bad format rows, empty non-target diffs for csv/json/jsonl/markdown, file hashes match current queue artifacts, no DML/locked-file hits, hard locks held, Gemini web quota unused.

No row needs revert, hold, or Gemini web second opinion. Preserve the stated caveats in receipts, especially same-source stacking, thin capped spans, abstract/source-record verification caps, and deferred malformed arXiv URL cleanup for 28110/28131.

KUN_REMAINING20_POST_APPLY_CHECKER_20260705T103310Z
