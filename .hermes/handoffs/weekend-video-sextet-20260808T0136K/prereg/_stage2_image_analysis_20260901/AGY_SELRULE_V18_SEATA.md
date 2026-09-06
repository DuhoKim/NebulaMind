ACCESS_SHA=121b1e0e4a8af6d82e12d02cbb433c80f6ea10d781d781d1330ba2c1ac90d866

# Independent Referee Report: V18 Prospective Sampling Amendment
**Seat B (Codex / agy)**

**AUTHORSHIP**: All new code in V18 was authored by Hwao. Earlier builder field-validation code was authored by the codex seat (2026-09-06 00:13–00:18), but it no longer participates, as every V16–V18 module is now the author's.

## 0. RUN (warning-strict)
All specified unit tests and script verifications were executed successfully in a warning-strict environment:
- (a) `test_beacon_record_expedited` (15 tests) and `test_beacon_v2` (19 tests) passed.
- (b) `test_approval_witness_v2` (8 tests), `test_build_corpus_identity_v18` (5 tests), and `test_build_corpus_identity` (4 tests) passed.
- (c) `test_run_configurations_v2` (19 tests) and `test_run_configurations` (17 tests) passed.
- (d) `beacon_record.py` and `beacon_record_expedited.py` diff confirms the fixture's FROZEN removed-line list exactly equals the diff's 18 removed lines.
- (e) `signature_preimage.py` correctly printed `121b1e0e4a8af6d82e12d02cbb433c80f6ea10d781d781d1330ba2c1ac90d866`.
- (f) Hashes for every file pinned in V18 E3 were computed and all 23 pins match identically.
- (g) **V17 counterexamples reproduced**:
  - The late writer with a backdated commit is REFUSED (`APPROVAL-PUSHED-AFTER-T-PULSE`) by the server-side push time. A REAL GitHub PushEvent cannot be forged or backdated by the operator because the `created_at` timestamp is set by GitHub's servers when the payload is received, providing a secure and queryable wall-clock upper bound.
  - HTTPError(404)/(500) on NIST at build time now returns `RETRY` under V18 (it previously erroneously advanced to `ACCEPT-DRAND` under V15's module).
  - A second build after simulated NIST recovery is blocked by `COLLECTION-LOCKED` due to the append-only log.
  - The driver without the adoption file fails closed as expected.

## 1. THE FIVE HARD CONSTRAINTS
- **C1: public 00:15Z pulse excluded by name**
  - **MET.** Clause §3b. Code line: `beacon_record_expedited.py:31` (`EXCLUDED_T_PULSE`) and lines 45, 74.
- **C2: same formula from the new approval time, no inherited pulse**
  - **MET.** Clause §3b. Code line: `beacon_record_expedited.py:34-36` (`pulse_time` function adds `DELAY_S = 600`).
- **C3: V15 and RETRY evidence preserved, prospective supersession**
  - **MET.** V15 remains signed and unmodified on file. The amendment limits itself narrowly and notes that V15 remains operative until V18 is signed.
- **C4: the cost stated**
  - **MET.** Clause §3b LIMITS states the cost clearly: NIST's 2048-bit key against a 512-byte signature means the NIST pulse is refused under this rule, making drand the expected source.
- **C5: a reader can SEE approval before seed**
  - **MET.** Clause §3b (W3, W5). Code line: `approval_witness_v2.py:73, 84`.
  - **Attack C5:** The operator cannot forge or backdate the `created_at` timestamp of a GitHub PushEvent because it is assigned by GitHub's server upon receipt. While they could delay pushing, this would only result in a *later* push event, which would fail the `created_at < T_pulse` check, safely closing the commitment. A second approval or late record is blocked by the strict "first approval is final" single-record check. The checks PROVE that the approval existed on the remote before `T_pulse`. Who spoke remains ATTESTED by the chat record. The 90-day query window is a limit stated in the text (GitHub Events API retention limit), making it clear how long the verifiable window lasts.

## 2. EVALUATION LABELS

1. **[MAJOR] ACCEPTANCE SET under V18**:
   - The acceptance conditions are exact. The clock is strictly checked *before* any public evidence is weighed (`beacon_record_expedited.py:79`).
   - ANY exception on a live fetch (including HTTPErrors) is caught and yields `RETRY` (`beacon_record_expedited.py:93-95`). It is never treated as a seed and never treated as a NIST failure that opens the drand fallback.
   - The fallback requires positive public evidence (a served, live-equal, but unauthenticable pulse).
   - The removed VOID re-check is genuinely unreachable because live equality is required *first*. If live equals retained, and retained is unauthenticable, live is inherently unauthenticable. If live is authenticable, it differs from retained, and `NIST-LIVE-DIFFERS` fires.

2. **[MAJOR] REPAIR AUDIT of every V17 finding**:
   - *FATAL 1 / C5 (witness had no wall-clock upper bound)*: **REPAIRED**. GitHub server-side PushEvent time now enforces upper bound (`approval_witness_v2.py:73, 84`).
   - *MAJOR (HTTPError counted as public NIST failure)*: **REPAIRED**. Live fetch exceptions now explicitly yield `RETRY` (`beacon_record_expedited.py:93-95`).
   - *MAJOR (no first-ACCEPT lock)*: **REPAIRED**. Append-only log with first-verdict locking implemented (`build_corpus_identity_v18.py:89`).
   - *MAJOR carried (no adoption binding)*: **REPAIRED**. `ADOPTED_RULE_SHA256.txt` is required and enforced (`build_corpus_identity_v18.py:17`, `run_configurations_v2.py:42`).
   - *MAJOR prerequisite (render-refused objects)*: **REPAIRED**. Canonical NaN sentinel tensor is present, unscored, and correctly counted in the denominator (`run_configurations_v2.py:43-44, 186`).

3. **[MINOR] DIFF CONFINEMENT V15→V18 and §3b/§3c/§7 versus executed behaviour**:
   - Every sentence is supported by the diffs. There are no aspirational changes or out-of-scope refactoring. The diffs rigidly align with the text.

4. **[MAJOR] Source-decision lock and adoption binding**:
   - Fixed in execution, not only in text. `ADOPTED_RULE_SHA256.txt` closes the loop mechanically. The render-refused sentinel is a fixed `np.nan` byte sequence mapped definitively, ensuring it stays in the denominator without ad hoc substitution.

5. **[MINOR] The inherited V15 defect**:
   - The disclosure is exact and the consequence is correct: the V15 rule accepted nothing (RETRY), and no identity will be built under it.

6. **Anything aspirational or unexecuted?**
   - None. Everything promised in the text executes and is defended by fixtures.

7. **WHAT IS STILL MISSING**:
   - Nothing is missing. The rule is fully verifiable, strict, and tightly bound.

VERDICT: SIGNABLE-AS-PRECOMMITMENT
