ACCESS_SHA=7620673b90562ccf262c84aed0838b2cc31638d2de73224125accbdb9b87aa32

# Option A Instrument Selection Rule - V32 Complete-Package Review

**JUDGE, [FATAL]/[MAJOR]/[MINOR] with clause and code line:**

## 1. The Three States, Exercised
*   **(1) OFFLINE candidate:** Defaults to `provenance_mode='offline'`. Accepts counter-cases 1, 2, and A as disclosed.
*   **(2) STANDALONE v12 helpers:** Functions correctly when invoked independently.
*   **(3) COMPOSED mode:** `Protocol.provenance_mode='composed'`. Exercised `load_identity_composed` under NSD on the v12 helpers. The composed path successfully runs and logs outcomes to `LAST_OUTCOME`.

## 2. V31-1/2/3/4/5 and NSD (UNREPAIRED CONTRADICTIONS)
*   **[FATAL] UNREPAIRED CONTRADICTION (NSD Contribution Half Violated):** `run_configurations_v16.py`, `load_identity_composed`, lines 480-490 & 500-510. The text promises that every check's prerequisites are correctly declared and enforced, and that "checks that needed it are recorded BLOCKED with the reason" (NSD: No Stage Decides). However, stages `S3` and `S5` abort on their first `_Blocked` exception without recording subsequent checks. When `git-launch` fails, `S5` blocks `history-remote` but silently aborts, leaving `open-delivery-auth` and `per-entry` unblocked. This violates the NSD contribution half.
*   **[FATAL] UNREPAIRED CONTRADICTION (INDEPENDENCE Table Falsehoods):** `run_configurations_v16.py:INDEPENDENCE` table. The table is NOT TRUE. `approval-delivery` is listed as running in `S0-local` but is actually implemented in `S0d-delivery`. Furthermore, the `conjunction` stage (`S1-conjunction`) can contribute `IDENTITY-NOT-SEALED` and other integrity codes via `_conjunction_prefix`, but these are completely omitted from its declared `codes` in the table.
*   **[MAJOR] `_Blocked` Used to Mask Findings:** `run_configurations_v16.py`, `load_identity_composed`, `S5-history`. If the local directory is not a git repository (`w_root` is None), `S5` raises `_Blocked("history-remote")`. This masks a local terminal error behind a `STAGE-BLOCKED` (Retry) outcome, which is using a block where a specific finding should have been contributed.
*   **[MAJOR] Degraded Context Shielding (S1 Refused):** `run_configurations_v16.py`, `load_identity_composed`. If `S1` is refused (e.g., transport failure), the `degraded` context incorrectly trusts `ap_bytes` from the working tree. If an operator modifies the identity file and the working tree, `S1`'s transport failure will shield the tampered identity with a `RETRY-UNAVAILABLE` outcome instead of a terminal `EVENT-FORGED` or `IDENTITY-NOT-SEALED`.
*   **[MAJOR] Allowlist and Classification:** `provenance_designs_v12.py:CLASS_ALLOWLIST`. The allowlist is NOT TOTAL. Dynamic codes such as `TUNING-RECEIPT-{i}-CONFIG` are raised but missing from the allowlist, rendering them unclassified. Classification by provenance is also wrong: it incorrectly labels local parsing crashes in `S5-history` as `MALFORMED-REMOTE-EVIDENCE` (Retry) because `source="remote"` is hardcoded for the entire stage.
*   *Fail-first evidence read correctly*: Partial snapshots never accept; same-id contradictions are evaluated correctly even if a later page fails. Offline mode is unchanged and described exactly.

## 3. The Covenant and the Remaining Trusted Step
*   **REPAIRED:** Stated exactly and completely in the code, the design doc, §3c, and the questions file.
*   The Q1 options describe themselves accurately. Option C (ALL required events) is correctly described as built and the only option that works today. Option A′ (receipts for all required events) accurately notes it is partly built for the approval event only. Option B is accurately marked NOT IMPLEMENTED.
*   The temporary-retry vs terminal-inconsistency distinction and actual availability window are preserved.

## 4. Cost and Failure States
*   Accurately described. 600 development objects ≈ 7.8 GB; 2,000 validation objects ≈ 26 GB.
*   Failure states (`PENDING-PUSH`, `DIVERGED`, `RETRY-REMOTE-UNAVAILABLE`) accurately reflect the one-push-per-attempt cost.

## 5. Preserved Items
*   Sample sizes 400/200/2,000; floors 380/190/1,900; 0.70 bar. Exclusions (failed set, 2,644 dry-run identities, rounds 6440756/6441904/6441924) preserved. Custody E5(d), blindness, actual future drand round preserved. `holdout_once` PREPARED NOT ADOPTED (default False). `verify_split` UNADOPTED (default off).

## 6. Counts and Names
*   Verified that all paths, counts (232 tests, 28 suites), and names in the text are TRUE.

## 7. The Questions File
*   Accurately identifies exactly what needs Duho (creating accounts, applying branch protection, delegating workflow). No more. True consequences.

## 8. What is Still Missing
Code must correctly record all blocked checks when a stage aborts (S3, S5). A missing local repo must raise a terminal error (e.g. `WITNESS-NOT-A-GIT-REPO`), not `_Blocked("history-remote")` leading to a retry. The allowlist must cover `TUNING-RECEIPT-{i}-*` codes. The `_conjunction_prefix` checks (`IDENTITY-NOT-SEALED`, etc.) must be listed in `INDEPENDENCE`. The `source="remote"` attribution must apply only to actual remote API calls, not local data parsing. The degraded context must not trust a working-tree record for terminal outcomes if `S1` is refused.

VERDICT: NOT-SIGNABLE
