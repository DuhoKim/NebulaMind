# Enumeration Verifier Re-verification

## Part 1: Verification of Repairs

**F1 (Reset Fixture):**
Verified by hand-simulation. The `ch_rst` fixture contains 4 closes total. Since `pass_retry_max` is 3, if the `closes_since_pass = 0` reset logic on `passrec` was deleted, `closes_since_pass` would reach 4 at the end of the chain, failing the `closes_since_pass >= constants.pass_retry_max` check outside the loop. The fixture correctly accepts this only because the `passrec` at pos 5 resets the count to 0, leaving 2 closes post-reset. The `ch_rst2` probe successfully adds a 5th close (3rd post-reset), which brings the post-reset count to 3, correctly reaching `PASS-RETRY-EXHAUSTED`.

**F2 (Positive Control for Second Occurrence):**
Verified. The new positive control properly feeds `EXPLAINED` then `NAMED-AS-DEFECT` on the same class key, and it correctly accepts. An aggressive refuse-all-seconds mutation (e.g. checking `len(key_order[key]) > 1` regardless of disposition) would now fail this fixture because the `len` check correctly scopes only to `EXPLAINED` entries, bypassing it for `NAMED-AS-DEFECT`.

**F3 (Immediately Preceding Contiguity):**
Verified via probe. I crafted an edge-case chain where the refusal block was contiguous but ended at `pos-2`, separated from the checkpoint by a `bindmap-entry` inside the `commit_set`. The verifier correctly refused it with `COMMIT-EVENTS-NOT-ADJACENT: checkpoint 6: in-commit refusal events at [3, 4] do not form the contiguous block immediately preceding the checkpoint record`.

**F4 (Defense-in-Depth Branch Reachability):**
Verified via probe. I intercepted the `_r()` calls during the execution of the `BOUNDARY-EPOCH-CHANGED` clock-malformed fixture. The execution successfully bypassed the pre-loop boundary validation and accurately hit the specific in-loop branch: `pos 1: cross-epoch arrival inside a hold`.

**F5 (Verification-Read Laundering):**
Probed. I tested whether a `drain-start` record could bypass the hold by simply including `"joined_read": 1` (where 1 is a valid read position). The probe was ACCEPTED (bug!). This means laundering is still possible, which I have documented in the new defects section.

**F6 (First-Refusal Semantics):**
Verified. The docstring correctly asserts first-refusal gate semantics. The `UNQUANTIZED-READING` and `ROW-ALIAS` composite-defect fixtures assert the documented order perfectly.

## Part 2: Hunt for New Defects

1. **Defect in Read-Binding Check (Laundering Evasion):**
   The fix for F5 (laundering) introduced a new flaw. In `boundary_pass` (line 351), the check `if rec.get("joined_read") in read_positions: continue` unconditionally skips subsequent loop validations for *any* record kind that specifies a valid `joined_read`. A malformed producer can attach `"joined_read": <open_read_position>` to a termination-unit record (like `drain-start`) or an arrival, laundering it past the `PASS-ABORTED-BY-TERMINATION` and `FOREIGN-RECORD-IN-HOLD` checks.

2. **Defect in Contiguity Check (Refusals After Checkpoint Ignored):**
   The check for in-commit refusals (line 461) explicitly filters `p < pos`:
   `ref_positions = sorted(p for p in commit if p < pos and chain[p]["k"] == "termrec" and chain[p]["outcome"] == "REFUSAL")`
   If a producer places a refusal event *after* the checkpoint but includes it in the `commit_set`, it is completely ignored. Because `ref_positions` omits it, it bypasses the `COMMIT-EVENTS-NOT-ADJACENT` check. Furthermore, it is missing from `in_commit_refusals`, so the `EVENT-UNLISTED` check also fails to detect it. This allows a malformed commit to hide post-checkpoint refusals.

*(Tests confirmed that `enumeration_verifier.py` outputs exactly `120/120 green` when run).*

SEAT: AGY
VERSION: ENV-V2
VERDICT: DEFECTIVE
COUNT: 2
F-lines: 351, 461
