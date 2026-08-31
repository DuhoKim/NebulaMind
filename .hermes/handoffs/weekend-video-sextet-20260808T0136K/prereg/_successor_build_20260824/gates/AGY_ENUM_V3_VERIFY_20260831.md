# AGY Enumeration Verifier V3 Verification

## Task 1: Verify ENV-V2 Repairs

### F1: `joined_read` Exclusion
The exclusion now correctly runs after the termination check.
* **Probe (a) - `drain-start` with `joined_read`**: REFUSED with `PASS-ABORTED-BY-TERMINATION`. The termination unit outranks verification and aborts the pass, fixing the V2 defect.
* **Probe (b) - `signed-cut` with `joined_read`**: REFUSED with `FOREIGN-RECORD-IN-HOLD`. It falls through to the catch-all foreign record check, correctly treating joined foreign kinds as foreign.
* **Probe (c) - legitimately joined `termrec`**: ACCEPTED. Legitimate events bypass the hold correctly.
* **Probe (d) - `arrival` carrying `joined_read` pointing at a bound read**: ACCEPTED. The code admits it, excluding it from the hold checks (evading `MALFORMED-HOLD-ARRIVAL`).
    * **Judgment**: This is a **documented admission**, not a defect. The draft language specifically names `"verification-reads and their joined arrival/touch events"` as the pass's own records. The only mechanism the chain provides to identify a pass-emitted arrival is this `joined_read` claim. The code faithfully implements the draft's documented design for pass-own records.

### F2: `COMMIT-EVENT-AFTER-CHECKPOINT`
* **Probe (a) - refusal after the checkpoint in `commit_set`**: REFUSED with `COMMIT-EVENT-AFTER-CHECKPOINT`.
* **Probe (b) - a TOUCH after the checkpoint in `commit_set`**: ACCEPTED.
    * **Judgment**: This is **right** per the draft clause. The draft's structural obligation ("the refusal events ride the commit IMMEDIATELY PRECEDING the checkpoint record") explicitly places contiguity and positioning constraints *only* on refusal events. A TOUCH event is unconstrained by these rules and may legally follow the checkpoint in the commit set.
* **Probe (c) - out-of-range commit position**: ACCEPTED. An out-of-range position (e.g. `p >= len(chain)`) is ignored by the check since `p < len(chain)` is false. This is architecturally sound and necessary because the `successor-export` is emitted *after* the checkpoint but must be included in the checkpoint's `commit_set`.

## Task 2: Hunt New Defects in V3-Changed Regions
**Confirmed Fixture Count**: 123/123 green

I found **two new defects** in the V3-changed regions:

**F3: Refusal Events Can Evade the Hold via `joined_read` (F1 Region)**
The V3 change restricts joined records to `rec["k"] in ("arrival", "termrec")`. However, it fails to check the `outcome` field of the `termrec`. The draft strictly specifies "joined arrival/touch events", but the code allows a `termrec` with `outcome="REFUSAL"` to ride the join and bypass the hold checks. A foreign refusal event can maliciously add a `joined_read` to evade the boundary check.

**F4: Verifier Crash in `COMMIT-EVENT-AFTER-CHECKPOINT` Loop (F2 Region)**
The new V3 loop iterates with `for p in commit` and directly evaluates `p > pos` and `chain[p]["outcome"]`. 
- If a producer places a string in the `commit_set` (e.g. `"foo"`), `p > pos` crashes the verifier with a Python `TypeError`.
- If a `termrec` is structurally malformed and missing the `"outcome"` field, `chain[p]["outcome"]` crashes the verifier with a `KeyError`.
A verifier must raise a `Refusal` at the first failed check; an unhandled crash allows malformed input to halt the verification process entirely.

SEAT: AGY
VERSION: ENV-V3
VERDICT: DEFECTIVE
COUNT: 123
F-lines: 3, 4
