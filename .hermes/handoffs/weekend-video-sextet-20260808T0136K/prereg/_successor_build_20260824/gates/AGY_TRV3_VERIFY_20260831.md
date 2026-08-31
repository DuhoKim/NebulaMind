# TRV-V3 Verification

## Task 1: Verify TRV-V2 Repairs
- **F1 (ENDING-COMMIT-MALFORMED):** Verified. Valid commits are accepted, and fictional/out-of-range positions are gracefully refused.
- **F2 (CHAIN-UNMOORED):** Verified. Normal chains rooted with an epoch-opening are processed correctly, while an unmoored chain (e.g. starting with a checkpoint) is gracefully refused with `CHAIN-UNMOORED`.
- **F3 (LATE REFUSAL SIDECAR):** Verified. An early refusal correctly writes the refusal directly to the transcript since it has not been signed/hashed yet. A late refusal (e.g., `RECEIPT-NOT-IN-STORE` raised after the transcript hash is generated) leaves the original transcript unchanged and correctly records the refusal in a `.REFUSED` sidecar.

## Task 2: Hunt New Defects in V3-Changed Lines
1. **F1:** The V3 repair for `ENDING-COMMIT-MALFORMED` introduced a defect where a non-iterable `commit_set` causes an unhandled crash instead of a graceful refusal.
   - At `terminal_review_verifier.py:123`, the line `for p in raw_commit:` blindly iterates over `raw_commit`.
   - If a malicious enumerator presents a chain where the ending checkpoint has a non-iterable `commit_set` value (such as a boolean `true`, an integer like `123`, or `null`), the verifier crashes with `TypeError` (e.g., `'bool' object is not iterable` or `'NoneType' object is not iterable`).
   - A verifier must refuse malformed input gracefully and never crash over it.

SEAT: AGY
VERSION: TRV-V3
VERDICT: DEFECTIVE
COUNT: 1
F-lines: 123
