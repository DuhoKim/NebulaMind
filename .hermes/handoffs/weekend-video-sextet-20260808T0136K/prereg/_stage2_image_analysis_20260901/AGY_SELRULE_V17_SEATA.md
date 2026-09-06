ACCESS_SHA=ef222a1e298f2787e9cc6f1937dc646a453b0d263ddd427cc8324353c2ca4108

Seat A — independent referee report on OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V17_20260906.md (Second draft of a prospective sampling amendment).

AUTHORSHIP: All new code by the author (Hwao).

### REQUIRED CHECKS
- (a) `test_beacon_record_expedited.py` (14 tests) and `test_beacon_v2.py` (19 tests) passed cleanly under `-W error`.
- (b) `test_build_corpus_identity_v17.py` (7 tests), `test_build_corpus_identity_v16.py` (3 tests), and `test_build_corpus_identity.py` (4 tests) passed cleanly under `-W error::ResourceWarning`.
- (c) `beacon_record.py` vs `beacon_record_expedited.py` diff confirms the removed lines exactly match the fixture's frozen list; `build_corpus_identity_v17.py` diff checks out with 8 changed lines including the expedited import and approval witness call.
- (d) `signature_preimage.py` produced exactly `ef222a1e298f2787e9cc6f1937dc646a453b0d263ddd427cc8324353c2ca4108`.
- (e) Every E3 file hash was verified against the files on disk and all 28 pins match exactly.
- (f) The Codex counterexamples were reproduced. V15's `beacon_record.py` incorrectly returns `ACCEPT-NIST` in both cases (a raising live fetch after retained authentication, and before `T_pulse`). V17's `beacon_record_expedited.py` correctly returns `RETRY` for both, effectively refusing them.

### THE FIVE HARD CONSTRAINTS
- **C1: MET.** §3b(1a) line 32 and `beacon_record_expedited.py` lines 25, 40, 69 exclude the 2026-09-06T00:15:00Z pulse by name.
- **C2: MET.** The `T_pulse` formula is identical (ceiling to minute, `DELAY_S = 600`), using the new approval time.
- **C3: MET.** V15 and the RETRY evidence are preserved unaltered and remain operative pending this approval.
- **C4: MET.** §3c plainly discloses that the expedited rule will almost certainly force drand fallback due to the lack of live NIST authentication, relying on 2 of 4 unverified-BLS relays.
- **C5: MET.** Approval is seen before seed via `approval_witness.py`.
  - *What each check proves:* W1 (commit integrity) ensures the record's bytes match the commit; W2 (remote ancestry) proves it was pushed to the protected branch; W3 (committer time) proves order relative to the protected tip; W4 (single record per version) proves first approval is final; W5 (freshness nonce verified live) proves the record was created at or after the nonce round.
  - *Attack vectors closed:* A backdated commit cannot bypass the nonce round which must be `< seed_round`; a chosen old nonce round still requires the record to be pushed to GitHub; a second approval is explicitly refused by W4; a delayed build does not alter the fact that the identity is built *once* and T_pulse was fixed by the already-pushed unique approval.
  - *What remains attested:* The wall-clock push time remains attested by GitHub (the script only checks ancestry), and who approved remains attested by the Codex record.

### FINDINGS
1. **ACCEPTANCE SET under V17:** [REPAIRED] There is no accepted record outside (a) an authenticable NIST pulse with live equality, or (b) $\ge$ 2 of 4 pinned relays agreeing retained and live, combined with a valid approval witness. The clock is checked first. A raising live fetch is evaluated as `RETRY` and never as a seed or a NIST failure.
2. **REPAIR AUDIT of every V16 finding:**
   - **[FATAL 1a] ACCEPT-NIST on a raising live re-fetch:** REPAIRED. `beacon_record_expedited.py` line 92 correctly catches the exception and returns `RETRY` (never a seed).
   - **[FATAL 1b] ACCEPT-NIST before the clock check:** REPAIRED. `beacon_record_expedited.py` line 74 moves the `now < t_pulse` check to the top.
   - **[C5 NOT MET / MAJOR 2] Chronology and selection freedom:** REPAIRED. `approval_witness.py` lines 44-53 enforce the single-approval-is-final rule, drand freshness nonce, and committer time bounds.
   - **[MAJOR 3a] "Ten minutes" overstated; no source-decision procedure:** REPAIRED. §3c (line 40) explicitly states that the identity is built *once* at the first collection at or after `T_pulse` and that a later NIST recovery does not reopen it.
   - **[MAJOR 3b] Contradictory §3b sentences:** REPAIRED. Draft line 32 accurately describes the new clock-first behavior and live-fetch equality constraints.
   - **[MINOR] Stale 24h documentation and test claims:** REPAIRED. V16 counterexamples are accurately documented; stale docstrings were updated (`beacon_record_expedited.py` line 14).
3. **DIFF CONFINEMENT V15→V17:** [PASSED] Changes are confined to the listed repairs. Sample sizes, floors, 0.70 bar, exclusions, holdout, boundaries, custody, and branch protection are byte-identical. The §3b description accurately matches executed behavior.
4. **SOURCE-DECISION PROCEDURE (§3c):** Fixed. "NIST recovers later" is closed by sealing the single identity build, and "re-approve for another round" is closed by W4 prohibiting more than one approval record per version.
5. **INHERITED V15 DEFECT:** The disclosure is exact and correctly states that no identity will be built under V15 as signed.
6. **ASPIRATIONAL/UNEXECUTED:** Approval, pre-pulse evidence, new pulse collection, and corpus freeze remain future acts. The guarded pool re-derivation from the absent GZ1 table remains unverifiable here.
7. **WHAT IS STILL MISSING:** Nothing is missing for a pre-commitment approval. The draft successfully incorporates necessary witness and bounds validations.

VERDICT: SIGNABLE-AS-PRECOMMITMENT
