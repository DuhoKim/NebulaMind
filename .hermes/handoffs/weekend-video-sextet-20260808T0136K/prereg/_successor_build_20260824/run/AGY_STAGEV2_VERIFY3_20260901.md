# AGY Staging V2 Verify Round 3

I performed a targeted verification on the 5 defective regions from Round 2, which were repaired by Codex.

## Verification of the 5 regions

**R1 (Allowed-root probe distinct branch):**
`boundary_test.py` now asserts `allowed_root_refusal != traversal_refusal`. Specifically, it checks that the refusal for a genuine sibling outside all stores throws `REFUSAL_DIRECT` rather than `REFUSAL_TRAVERSAL`. The implementation in `mediator_read` resolves the root and ensures it is in the `allowed` set before checking traversal, producing `REFUSAL_DIRECT`. Both probes hit their expected distinct branches. The fix holds.

**R2 (Containment checks in `mediator_read`):**
I verified the new `mediator_read` implementation now utilizes `resolved_target.relative_to(resolved_root)`. If a path (like a planted symlink) resolves to an outside location, `relative_to` correctly raises a `ValueError`, escalating to `REFUSAL_TRAVERSAL`. I ran a custom script confirming this by planting an unauthorized symlink inside a store root; `bs2k_stage_v2.py` securely blocked read access. The fixture's symlink probe acts as expected. The fix holds.

**R3 (`PINNED_PARENT_RECEIPTS_SHA256` fail-closed removal check):**
I verified via a temp copy modification script that omitting the `PINNED_PARENT_RECEIPTS_SHA256` string assignment from the v9 reference file causes `archive_identity()` to immediately raise `Refusal(REFUSAL_SCHEMA)`. It strictly fails closed as designed. The fix holds.

**R4 (`v9_literal` last assignment precedence):**
I inspected the AST iteration inside `v9_literal` and confirmed it continues looping through all top-level statements, continuously replacing `found` upon matching assignment nodes. I confirmed using a temporary python file with two duplicate assignments that it retrieves the final assignment correctly, respecting Python's runtime precedence. The fix holds.

**R5 (Manifest coverage & honest pre-staging custody scope):**
`OPERATION_SET_COMMIT_20260831.md` is now correctly included in `manifest_materials()` and digested in `STAGED_manifest.json`. I confirmed that mutating the file will trip the `verify_staged()` check, which is mandatorily called at the very beginning of `go_live()`. The pre-staging custody scope is honestly declared, as `STAGED_RowA_receipt.json` explicitly states `"authentication_state": "STAGED-NOT-SIGNED"`. The fix holds.

Both `bs2k_stage_v2.py` and `boundary_test.py` were run without error, validating 17/17 and 16/16 fixtures respectively. No new defects were introduced in these regions.

SEAT: AGY
VERSION: STAGEV2-VERIFY-V3
VERDICT: SOUND
COUNT: 0
F-lines: NONE
