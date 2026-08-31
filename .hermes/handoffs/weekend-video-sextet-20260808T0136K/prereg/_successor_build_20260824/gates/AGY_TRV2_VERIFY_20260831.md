# Terminal Review Verifier V2 Verification

1. **Verify the repairs**:
   - **F1 (trailing garbage)**: Verified.
     - Garbage after a `TERMINATED` checkpoint is correctly caught as `TRAILING-RECORDS`.
     - An export inside its commit is successfully accepted.
     - An export placed after the ending but outside its commit is correctly caught as `TRAILING-RECORDS`.
     - An export placed *before* the disclosure record outside the commit is correctly caught as `EXPORT-OUTSIDE-COMMIT` (ensuring the earlier branch stays reachable).
     - Two drain-starts for one receipt are correctly caught as `DUPLICATE-DRAIN-START`.
   - **F2 (refusal-not-crash)**: Verified.
     - Empty receipt store properly handles the exception, writes `REFUSED: RECEIPT-NOT-IN-STORE` to the transcript, and exits 2.
     - Tampered chain file (running-digest mismatch) correctly raises `ev.Refusal` inside `recompute_terminal_head`, gets caught by the refusal handler, and refuses gracefully.
     - No-ending chain is safely caught and writes `REFUSED: NO-ENDING`.
     - The printed counts exactly match the expected values: `terminal_review_verifier.py` (24/24 green) and `terminal_ceremony.py` selftest (4/4 green).

2. **HUNT NEW DEFECTS**:
   Probing the requested edge cases reveals exactly 3 new defects in the v2-changed regions:
   - **Commit_set containing out-of-range positions**: Accepted. `derive_ending` relies on `range(pos + 1, len(chain))` and does not verify whether the positions claimed in the `commit_set` actually exist. An enumerator can pass an incomplete, partial commit.
   - **An ending at position 0**: Accepted. `ev.verify_prefix` acts as a no-op when `len(chain) - 1 == 0`. An ending at position 0 lacks an `epoch-opening` record, breaking custody to the predecessor, yet `derive_ending` and `build_review_body` execute successfully and authorize the unmoored chain.
   - **Refusal handler's transcript rewrite**: A transcript digest invalidation issue. If a refusal occurs late (e.g., inside `build_review_body` after `t_digest` is calculated and printed), `_refuse` rewrites the existing transcript file with a new `REFUSED:` line. This modifies the file on disk, breaking the previously logged transcript SHA256 digest.

SEAT: AGY
VERSION: TRV-V2
VERDICT: DEFECTIVE
COUNT: 3
F-lines: 57, 95, 106
