ACCESS_SHA=f294cb55ac4c87daf156d2b9875d9bbd40434d93908f64c536cb1dbc751bff15

# V33 Complete-Package Review: Seat A Report

**1. The Three States, Exercised**
The three states were correctly exercised on the production call path:
- **OFFLINE candidate:** `PRODUCTION.rederive_seed` defaults to offline and accepts counter-cases 1, 2, and A. This is explicitly disclosed as a limit in the §3c column (L-OFF).
- **STANDALONE v13 helpers:** `validate_continuation_v13` sweeps the local state first and correctly contributes partial/malformed findings for the retrieval.
- **COMPOSED mode:** Using `provenance_mode='composed'` running `load_identity_composed` correctly refuses all the counter-cases (e.g., `EVENT-FORGED`, `HISTORY-CONTINUATION`).

**2. V32-1..5 and Seat A's Observations**
All points are **REPAIRED**:
- **V32-1 & Seat A Obs 1 (NSD incomplete / Table falsehoods):** The identity read no longer gates the open-file read or repository discovery. S3's approval gate no longer hides the open same-id check. The conjunction's nonce check runs independently. The table is now exact and verified against the code.
- **V32-2 (Absence deciding FORGED):** On a partial snapshot, only predicates that survive completion are decided; absence from a partial prefix does not decide `FORGED`.
- **V32-3 (Erased history findings):** `history_findings_v13` acts as a durable collector, contributing each finding at its boundary.
- **V32-4 (Aggregate gate v1):** Gate v3 correctly judged RUN2 and enforces genuine exit codes.
- **V32-5 (Accounting & Naming):** Dynamic refusal names (like tuning receipts) are a declared family in the allowlist. Wording and method counts are corrected.
- **Seat A Obs 2 (Degraded context):** Every degraded approval-byte source is checked against the witness digest, and the source is recorded.
- **Blanc's 4 items:** NSD is stated once and named; it is enforced at input granularity in `load_identity_composed`; controls are derived from the INDEPENDENCE table without exemption; and per-subcase evidence is provided by the v3 differential controls and fail-first regressions.

**3. The Two Categories (Disclosed Limits vs Contradictions)**
Every entry in §3c's "DISCLOSED LIMITS" column (L-OFF, L-COV, L-RCPT, L-INH, L-AVAIL) is a genuine limit of the environment, trust boundaries, or offline protocol. There are **no unrepaired contradictions** where the code does something contrary to the text's promises.

**4. The Table Versus the Code**
The test `test_track13_table_vs_code.py` is complete. It extracts every `add`, `_Blocked`, and `stage` site using regex and strictly enforces that every check, code, and prerequisite matches the table exactly. No contribution site or code escapes this verification.

**5. The Differential Controls**
The v3 differential controls correctly assert the independent baselines. The differential form correctly generates every independent subcase pair (no exemptions for identity-file pairs) and verifies that a failed prerequisite precisely blocks the dependents while independent checks still execute. No stage can secretly decide or silently abort.

**6. The Evidence Chain**
The evidence chain holds. The receipt per-run classifications are read correctly against the retained logs. The open historical gap in early regressions is recorded transparently. Aggregate RUN2 was judged strictly by `scripts/aggregate_gate_v3.py` on verified portable copies, resulting in a strict pass.

**7. Cost and Failure States**
The cost estimates (~7.8 GB development, ~26 GB validation) are accurate. The failure states (PENDING-PUSH, DIVERGED, RETRY-REMOTE-UNAVAILABLE) have been thoroughly exercised and reflect the true cost of attempting rebuilt/failed chains.

**8. Preserved Items**
Sample sizes (400/200/2,000), floors (380/190/1,900), the 0.70 bar, excluded dry-run identities, custody E5(d), holdout_once, and the unadopted `verify_split` remain accurately preserved byte-for-byte.

**9. Text Counts and Names**
All counts and names in the text are TRUE. The 32 suites containing 369 tests run successfully when the complete sandbox environment (including external `scratch` dependencies) is supplied, matching the verified portable aggregate log. Nothing is described without being built.

**10. What is Still Missing**
Nothing is missing before Duho can be asked to adopt exact reviewed behavior with concrete consequences.

VERDICT: SIGNABLE-AS-PRECOMMITMENT
