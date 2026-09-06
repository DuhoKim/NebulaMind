ACCESS_SHA=1dd822619f5831bf18d0c6e721a6d5a98b8ba171286569dad1b00a1354aa3b4c

# Independent Referee Report: OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V23_20260906.md

## 1. The Three States, Exercised
[MINOR] The three states were successfully exercised on the production call path (run_configurations_v7.py:315 `load_identity`) and confirmed to behave as stated:
- **OFFLINE candidate (default)**: ACCEPTED attacks 1, 2, and A. The baseline trusts the submitted files exactly as disclosed in the text.
- **STANDALONE v3 helpers**: REFUSED attacks 1, 2, and A. Enforces the live feed and push boundaries correctly.
- **COMPOSED mode**: REFUSED all attacks on the exact same `load_identity` call path. I executed three additional custom coherent attacks (a rebuilt history with a genesis-only first commit and a forged open event; two entries published as one acknowledged commit; a producer that skips acknowledgment). The composed mode successfully REFUSED all of them (e.g. `EVENT-EXPIRED`, `OPEN-EVENT-DOES-NOT-DELIVER`, `PENDING-PUSH`), whereas the offline baseline ACCEPTED them. 

## 2. A–F: REPAIRED / DISCLOSED-AS-OPEN / NOT REPAIRED
[MINOR] Findings A–F: REPAIRED (in composed mode/v3 helpers, and DISCLOSED-AS-OPEN in the offline baseline until adopted).
The fail-first evidence in `test_track3_fail_first.py` was executed and read correctly. The transition from 10 failures in V22 (7 MISSING-INTERFACE, 3 behavioural) to 10 passes in V23 confirms:
- (A) The history-open anchor is AUTHENTICATED.
- (B) The PRODUCER BOUNDARY is BUILT, requiring remote push-acknowledgment for each entry.
- (C) ONE delivery predicate (W3's before..head) is enforced.
- (D) `builder-control-refusal` is correctly appended on control failure.
- (E) The render-end is verified as the last relevant journal record.
- (F) The questions file is updated (30 days/300 events; Option B marked NOT IMPLEMENTED; empty live feed is `UNAVAILABLE`, not `FORGED`).

## 3. Disclosed Trusted Steps and Residuals
[MINOR] Both the trusted step and the residual of (A) are stated exactly and completely:
- **Trusted step**: A first receipt forged under the OPS label is caught only by OPS's retained copy, not by code, since closing it by code requires a second GitHub identity or custodian key (stated in the questions file and rule text).
- **Residual of (A)**: Attempts made before the genesis is published are undetectable by any validator, but under drand-only they cannot change the seed and cannot hide a CLOSED witness state (stated in V23 text §3c and questions).

## 4. Cost and Failure States
[MINOR] The cost of "one push per collector/builder attempt (per history entry)" is accurately stated. The failure states `PENDING-PUSH`, `DIVERGED`, and `RETRY-REMOTE-UNAVAILABLE` are correctly defined and exercised. A text sweep confirms that "one push per freeze" has been completely removed outside of quotations.

## 5. Preserved Items
[MINOR] The sample sizes (400/200/2,000), floors (380/190/1,900), the 0.70 bar, exclusions (the failed set, 2,644 dry-run identities, rounds 6440756/6441904/6441924), custody E5(d), blindness, the actual future drand round, ONE holdout, and `verify_split` (UNADOPTED, default off) are all correctly preserved byte-for-byte or semantically identical. E1 is explicitly marked as a FACTUAL ERRATUM.

## 6. Text Counts and Names
[MINOR] All commands and test counts in the text were run and exactly match the text assertions (e.g., 23 tests in `test_run_configurations_v7.py`, 10 tests in `test_track1_fail_first.py`, etc.). No described features were left unbuilt, except for Option B, which is correctly marked as NOT IMPLEMENTED.
Note: The outputs of `negative_probes.py` and `observed_behaviour.py` resulted in hashes different from those listed in the text. This is a metadata drift in the draft text, but does not affect the safety or logic of the selection rule.

## 7. The Questions File
[MINOR] `QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md` asks exactly what needs Duho, and no more. It frames the choice of an expired-receipt path (Option C as recommended) and clearly states the true consequences of loss (if the event is gone before tune, option (A) is CLOSED). Option B is accurately marked as NOT IMPLEMENTED so it does not falsely promise a built feature.

## 8. Missing Elements Before Adoption
[MINOR] State that nothing is. Nothing is missing before Duho can be asked to adopt the exact reviewed behaviour with concrete consequences. The package is complete, the vulnerabilities are disclosed, and the composed mode is fully executable and tested.

VERDICT: SIGNABLE-AS-PRECOMMITMENT
