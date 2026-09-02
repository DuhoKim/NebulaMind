# AGY REFEREE REPORT: V5

## A. Closure of F11 and F14

### F11: PARTIAL
The set condition for acquisition completion is correctly specified. V5 states: "the set of `brick` values having at least one receipt with `verdict == "OK"` in `tier_c_fetch_receipts.jsonl` equals the 17,947-element manifest set". It handles multiple process runs and properly fail-closes on any non-OK verdict lacking a later OK receipt. It correctly identifies the acquisition journal schema and distinguishes it from the chained seal journal. I verified the live journal's first line matches the 7-key schema exactly.
However, V5 asserts the condition `computed_sha256 == published_sha256` in prose for the set condition, but does not provide a mechanism for the seal seat to structurally receipt this check at freeze.

### F14: PARTIAL
V5 correctly introduces a read-only Git witness for the script and mandates freeze-time verification of the blob ID, the SHA-256 of the live file, the SHA-256 of the pinned copy, and a zero exit status from `git diff --quiet -- <path>`. This properly defends against untracked edits and rewritten history because all three SHA-256 hashes must exactly match the pinned copy's SHA-256, ensuring content identity regardless of the index state.
However, V5 makes a materially false claim about the Git history it cites.

* `git ls-files -s -- ../_successor_build_20260824/acquire/fetch_bricks.py` returns `100644 df704bed1c5fd872cf9dee9f4be2e88f64bb94a0 0	../_successor_build_20260824/acquire/fetch_bricks.py`.
* `git cat-file -p df704bed1c5fd872cf9dee9f4be2e88f64bb94a0 | shasum -a 256` returns `35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99  -`.
* `git log --format='%h %ad' --date=iso -- ../_successor_build_20260824/acquire/fetch_bricks.py` confirms commits `888c0a2ff` and `ad21829fa` exist at the times stated.
* BUT `git rev-parse 888c0a2ff:../_successor_build_20260824/acquire/fetch_bricks.py` returns `3f994f8d2112660e21d73a4f3651c71feef16bbb`, NOT `df704bed`.

## B. Verbatim Preservation

The `diff` of V4 against V5 confirms that changes are strictly confined to §§7.9–7.11, §16.3, §16.12, §18, and §19. 
I manually verified that the §19 rule register has exactly 170 rules, and that entries 081, 082, and 083 correctly reflect the new text of 7.9, 7.10, and 7.11. I also successfully re-hashed the six §2 pins and ran the fixture test.
However, there is an F14/F11-unrelated edit to the fixture output time in §16.12.

## C. New Findings

| ID | Severity | Clause | Defect and Repair |
|---|---|---|---|
| F15 | MINOR | §16.12 | **UNAUTHORIZED EDIT:** The fixture output time was changed from 0.081s to 0.079s. Though technically true on execution, this edit violates verbatim preservation outside F11/F14. **REPAIR:** Revert the time to 0.081s. |
| F16 | FATAL | §7.11 | **FALSE HISTORY CLAIM:** V5 falsely claims that the `df704bed...` blob was committed by `888c0a2ff`. The blob at `888c0a2ff` was actually `3f994f8d...`, proving the script was modified mid-run before `ad21829fa`. **REPAIR:** Acknowledge the mid-run change. If the script was repaired mid-run and custody is proven from that point, state the exact commit that introduced the final blob and bind the restart. |
| F17 | FATAL | §7.11 | **MISSING RECEIPT FOR SET CONDITION:** The `computed_sha256 == published_sha256` equality is required for completion but is never formally receipted by the seal seat. **REPAIR:** Require the seal seat to execute a programmatic check of the 17,947 OK lines and append its success to the chained seal journal at freeze. |

SEAT: AGY
VERSION: MINIPREREG-REFEREE-V5
VERDICT: NOT-SIGNABLE
COUNT: 3
F11: PARTIAL
F14: PARTIAL
