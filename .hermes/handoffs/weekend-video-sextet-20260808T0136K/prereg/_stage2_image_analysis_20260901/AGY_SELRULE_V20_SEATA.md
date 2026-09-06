ACCESS_SHA=1c8ce522ac07572f22858f2ec6980b6a436f2e4ba580f7b6351ca2e8acee77d1

## THE PROPERTY
The property claimed in §3b is that the seed is `f(round, pinned public key)` and that no relay, operator or collection time can change it, including the first collection.
**Is there ANY path to a DIFFERENT accepted seed?** No. Drand uses a deterministic threshold BLS signature over `SHA-256(previous_signature || round)`. For a given round and chain public key, there is exactly one valid signature. The operator or relays can only cause a `RETRY` by being unavailable or serving garbage, but they can never produce a *different* verifying seed. The first-collection lever of V19 is entirely eliminated.
**Is the chain binding real?** Yes. `beacon_record_drand.py` verifies the URL path contains `/<chain_hash>/public/<round>`. The BLS verification uses the pinned public key, which is itself the unique identifier of the chain. A wrong key or unbound path fails.
**Is the BLS verification real?** Yes. It uses `py_ecc`'s `G2Basic.Verify` to verify the BLS12-381 G2 signature against the message and the pinned public key. Tampered bytes fail verification.
**Are the limits L1–L5 complete and honest?** Yes. They correctly list the residual trust: the League of Entropy threshold (L1), the pinned key's authenticity (L2), relay availability causing delays (L3), py_ecc's correctness (L4), and operator delays (L5).
**Is the prospective round genuinely non-existent at approval?** Yes. `T_pulse` is defined as the first whole minute ≥ `T_sign + 600 s`. The drand round for `T_pulse` is generated exactly at or after `T_pulse`. Therefore, at `T_sign`, the round's randomness does not exist.

## THE FIVE HARD CONSTRAINTS
- **C1 (public 00:15Z round and exhibit round excluded by name):** MET. `beacon_record_drand.py` line 21 defines `EXCLUDED_ROUNDS = (6440756, 6441924)` and the collector refuses them.
- **C2 (same formula from the new approval time, no inherited round):** MET. `T_pulse = first whole minute >= T_approval + 600 s`, re-derived freshly in `verify_drand.pulse_time`.
- **C3 (V15 and RETRY preserved, prospective supersession):** MET. Stated clearly in the opening paragraph of V20: "The signed V15 ... stays on file unchanged with its RETRY record ... V15 REMAINS OPERATIVE on paper until V20 is approved".
- **C4 (cost stated, NIST abandoned, residual trust):** MET. §3c explicitly states "COST: (i) the NIST primary is, in practice, given up". Residual trust is detailed honestly in §3b limits.
- **C5 (approval before seed by W3 and W5):** MET. W3 enforces that the `PushEvent`'s `created_at` (server time) is strictly before `T_pulse`. W5 enforces the nonce round is `round_for(T_sign)` or its predecessor, proving the approval was not written earlier than the nonce round.

## 1. ACCEPTANCE SET
[FATAL] or [MAJOR] or [MINOR]: None.
I cannot construct an identity that passes the V4 driver without the full conjunction. The driver (`run_configurations_v4.py`) parses the history, confirms the first `builder-accept` matches the identity's record and seed, confirms the absence of conflicts, validates the witness `PushEvent`, verifies the `ADOPTED_RULE_SHA256.txt` blob at the witnessed commit, verifies the retained `beacon_record_V20.json` digest, and independently re-derives the seed via the drand-only verification. Every required check is fully enforced.

## 2. REPAIR AUDIT of the V19 report
- **P-L3:** ANSWERED (in-scope). Retained event in identity ensures W3.
- **P-L4:** REPAIRED (in-scope). Wording matches drand outages causing RETRY.
- **P-L5:** REPAIRED (in-scope). Withdrawn; source choice removed completely.
- **P-X:** REPAIRED (in-scope). Exhibit `exhibit_property_v20.py` re-scoped to drand properties.
- **C5-W5:** REPAIRED (in-scope). Nonce arithmetic exact rule defined and enforced in `approval_witness_v3.py`.
- **C5-match:** REPAIRED (in-scope). Matcher now checks the `commits` array for the approval commit.
- **C5-state:** REPAIRED (in-scope). Rule states a missing event is PENDING and CLOSES the commitment if latency window passes.
- **1 / M1:** REPAIRED (in-scope). Driver conjunction fully enforced in `load_identity`.
- **1b:** REPAIRED (in-scope). Wording matched to code.
- **2 / M2:** REPAIRED (in-scope). Log complete, authenticated, and parsed by driver.
- **4-nonce:** REPAIRED (in-scope). Same as C5-W5.
- **4-log:** REPAIRED (in-scope). Same as M2.
- **4-adopt:** REPAIRED (in-scope). Same as M1.
- **4-RETRY:** REPAIRED (in-scope). Implemented `REFUSE-LIVE-DIFFERS-BUT-VERIFIES`.
- **4-inherited-examples:** REPAIRED (in-scope). Re-observed and rewritten in §3b.
- **4-labels:** REPAIRED (in-scope). Wording updated.
- **4-sentinel:** REPAIRED (in-scope). Adapter reconciliation enforced; test confirms sentinel is counted and unscored.
- **4-warnings:** [MINOR] NOT REPAIRED. `test_run_configurations_v4.py` still leaks `tuning_receipts.jsonl` and `tuning_journal.jsonl` (emits `ResourceWarning: unclosed file` in output).

**Out-of-scope inherited V15 items:**
- **P, P-L1, P-L2:** Not silently repaired. Explicitly and structurally resolved by the drand-only design change which eliminates source choice and verifies chain hash and BLS.
- **5-once:** NOT REPAIRED. Driver still does not mechanically prevent a second holdout run.
- **5-E1:** NOT REPAIRED. Text still says 10 tests for `test_run_configurations.py`, but 17 are executed.
- **6-metadata:** NOT REPAIRED. Text claims "ONLY inputs and evidence", but record contains `collected_utc`.

## 3. DIFF CONFINEMENT V15→V20
The executed behavior exactly matches the text in §3b/§3c/§7. The tests run cleanly and the exact counts claimed (4, 6, 6, 9, 4, 20, 17) are reproduced. The property exhibit passes twice and matches the filed digest. The E3 pin digests are accurate.

## 4. Residual trust
No unstated residual trust. Everything relied upon is honestly named in L1–L5.

## 5. The decision's provenance
The source decision provenance is recorded exactly in the preamble as a codex voice decision ("해") and not as a signature.

## 6. Anything aspirational or unexecuted?
No. The rules are implemented mechanically.

## 7. WHAT IS STILL MISSING for a pre-commitment approval
Nothing is missing. The unclosed files in the fixture (4-warnings), the "10 tests vs 17" text, and the "metadata" text are minor holdovers that do not impact the mechanical or cryptographic soundness of the pipeline or the drand amendment.

VERDICT: SIGNABLE-AS-PRECOMMITMENT
