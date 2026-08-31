# AGY Enumeration Verifier Adversarial Review (2026-08-31)

This report details the findings of the first adversarial pass on `enumeration_verifier.py`.

### 1. Vacuity
- **Vacuous Fixture (`ch_rst`)**: The fixture tests that a "pass record resets the derived count", but the `_prec` record is placed at `pos=1`, before any `verification-close` records have incremented the count. `closes_since_pass` is already 0. If the verifier's reset logic were completely removed, the fixture would still pass because the count only ever reaches 2 (less than `PASS_RETRY_MAX` of 3).
- **Missing Positive Control (`SECOND-EXPLAINED`)**: The docstring claims to test "does a NAMED-AS-DEFECT second occurrence pass as the draft demands?". The code correctly allows it, but there is no `ok()` fixture testing this accepted case. If the code were altered to aggressively refuse *all* second occurrences regardless of disposition, `expect("SECOND-EXPLAINED")` would still pass because it only tests a chain with two `EXPLAINED` entries.

### 2. Missed Obligations vs Draft Item (SS11)
I spot-checked the following five obligations:
1. *Consulted at five gates (BS-L, LOCK-OPENING, BS-7F, BS-V, DISCLOSURE).* (Enforced and fixtured via `UNKNOWN-GATE`).
2. *The entry↔emission relation is a BIJECTION checked in both directions.* (Enforced and fixtured via `ORPHAN-ENTRY`, `UNENUMERATED-EMISSION`, `DUPLICATE-ENTRY`).
3. *The first record's predecessor is BS-2f's receipt digest.* (Enforced and fixtured via `FIRST-PREDECESSOR`).
4. *The per-key EXPLAINED count (≤ 1 within the run).* (Enforced and fixtured via `SECOND-EXPLAINED`, though missing the positive control).
5. **MISSED OBLIGATION:** *"each listed member's refusal event must sit in the checkpoint commit's own write set, immediately preceding the checkpoint record"*. The code in `join_pass` checks if the refusal event is `< pos` and its key is in `commit_set`. It **does not** enforce the "immediately preceding" contiguity constraint (i.e., that the events form a contiguous block ending at `pos - 1`), nor is there any fixture testing an event that is in the commit set but not immediately preceding. 

### 3. Unreachable or Dead Branches
- **Dead Branch (`BOUNDARY-EPOCH-CHANGED` inside hold)**: In `boundary_pass`, the loop over the hold interval contains `if rec["epoch"] != b["epoch"]: _r("BOUNDARY-EPOCH-CHANGED", ...)` for arrivals. This branch is completely unreachable. Any cross-epoch record added during a hold will already trigger the `cur[-1]["epoch"] != b["epoch"]` check at the start of the function (before the loop begins), aborting the pass early.

### 4. Order-of-Check Gaming
- **Accept (Bypassing Hold Restrictions)**: In `boundary_pass`, an attacker can inject arbitrary unjoined `verification-read` records inside a hold. The check `if rec["k"] == "verification-read": read_positions.add(pos); continue` unconditionally accepts them without verifying they are actually joined to any pass-owned events. This allows foreign records to silently bypass the hold restrictions.
- **Hiding (Milder Refusal)**: In `clock_pass`, a record with an unquantized reading that is also a regression (e.g., `cur_reading=15`, `reading=12` with `g=5`) will raise `UNQUANTIZED-READING` first, successfully hiding the `READING-REGRESSION` defect. Similarly in `join_pass`, a `ROW-ALIAS` defect hides a `DIGEST-NOT-RECOMPUTED` defect.

SEAT: AGY
VERSION: ENV-V1
VERDICT: DEFECTIVE
COUNT: 6
F-lines: 212, 320, 330, 363, 424, 862, 1080
