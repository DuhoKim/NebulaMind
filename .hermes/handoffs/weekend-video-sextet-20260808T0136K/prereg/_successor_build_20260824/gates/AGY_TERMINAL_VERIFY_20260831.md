# AGY Verification: Terminal Ceremony & Review Verifier

## Probes & Findings

### 1. ENDING DERIVATION & TRAILING GARBAGE (DEFECT)
- **Both-endings, multiple checkpoints, empty chain**: Handled correctly. `derive_ending` strictly refuses ambiguous endings and `recompute_terminal_head` refuses an empty chain.
- **RUNNING checkpoint alone**: Correctly falls through to `NO-ENDING` because the filter strictly demands `status == "TERMINATED"`.
- **Claimed vs Chain-Derived**: Secure. The verifier never trusts the presented `kind`; it infers it strictly via `derive_ending` and constructs the body manually.
- **Trailing Garbage Authorization (Finding 1)**: `recompute_terminal_head` unconditionally returns `chain[-1]["running"]`. However, neither `derive_ending` nor `build_review_body` asserts that the terminal event (the checkpoint or the disclosure's export) is actually at the end of the chain. An enumerator can append unauthorized garbage records post-termination, and the principal will blindly sign a `recomputed_head` that encompasses and legally authorizes this trailing garbage.

### 2. THE COMPLETED PATH
- **Export Mismatches**: Correctly caught. Any divergence in `flagged_keys` or other fields fails the strict `ev._canon` byte-match against the recomputed export.
- **Commit Set Edge Cases**: Secure. If `commit_set` is missing, it evaluates as empty `()`, and `epos not in set()` safely raises `EXPORT-OUTSIDE-COMMIT`.
- **Regeneration Head**: Secure. `regenerate_export` receives the correct `pos` (the disclosure record's position) to use as the `terminal_head`.

### 3. THE TERMINATED PATH
- **Receipt vs Store / Missing Digests**: Handled properly.
- **Multiple Drain-Starts**: `drains[0]` deterministically binds the earliest `drain-start` matching the receipt digest. This is strictly deterministic, though it means an injected earlier fake `drain-start` would win over the real one.

### 4. THE SIGNING BYTES
- **Determinism & Schema Exactness**: Robust. The `ev._canon` function prevents any JSON key-reordering collisions, and `validate_review_body` enforces exactness (rejecting missing/extra/alien-kind fields).
- **Collision Resistance**: Because the two review schemas have mutually exclusive field names (e.g., `terminal_checkpoint_digest` vs `disclosure_record_digest`), their canonical serializations can never collide by construction.

### 5. THE CEREMONY SCRIPT (DEFECT)
- **Refusal Before Emission**: Holds; no signing bytes are printed on any failure path.
- **Self-Reference Discipline**: Holds; signing bytes are printed only after the transcript file is finalized and hashed.
- **Unhandled ReviewRefusal (Finding 2)**: The docstring guarantees "a refusal at any check exits 2". While the `head != head_indep` check properly handles this by logging `REFUSED` to the transcript and returning `2`, validation failures inside `trv.build_review_body` (like `EXPORT-MISMATCH` or `RECEIPT-NOT-IN-STORE`) raise `trv.ReviewRefusal`. The `run_ceremony` script lacks a `try/except` block to catch this, crashing with a Python unhandled exception (exit code 1) and abandoning the on-disk transcript without a refusal line.

### 6. VACUITY
All fixtures pass for the correct cryptographic or logical reasons. The reported "21/21 fixtures" printed by the script perfectly matches the 21 unique assertions executed (3 `ok` calls, 16 `expect` calls, and 2 manual `TOTAL` increments for determinism).

SEAT: AGY
VERSION: TRV-V1
VERDICT: DEFECTIVE
COUNT: 2
F-lines: 66, 90, 112, 138
