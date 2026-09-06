ACCESS_SHA=75eceb104b75ac614a0b3b0f1e4ee758913b0fbfdd6ae54848de49bce521e90a

## 1. THE THREE STATES, EXERCISED
[MINOR] The three states described in the text (§3c, rows 10a-10c) are correctly exercised:
- **State 1: CURRENT OFFLINE CANDIDATE (`Protocol.provenance_mode='offline'`)**. ACCEPTS coherent attacks (forged-but-consistent GitHub event, rebuilt history before first freeze). Discloses them as open boundaries.
- **State 2: STANDALONE staged helpers (`provenance_designs_v2`)**. REFUSES the attacks in isolation (`FORGED`, `NOT-AN-EXTENSION`, `PENDING-PUSH`).
- **State 3: COMPOSED RECOMMENDED MODE (`Protocol.provenance_mode='composed'`)**. Helpers called INSIDE `load_identity` on the production call path. REFUSES the attacks on the same call path (`EVENT-EXPIRED-NO-RECEIPT-PATH`, `HISTORY-CONTINUATION`), and accepts the genuine identity.
- **ADDED ATTACK (State 1 vs State 2/3)**: A history entry appended locally and coherently sealed, but NOT pushed to the remote branch.
  - State 1 (Offline): ACCEPTED
  - State 2 (Standalone): REFUSED PENDING-PUSH
  - State 3 (Composed): REFUSED HISTORY-CONTINUATION (PENDING-PUSH)

## 2. CODEX V21 FINDINGS (C1–C12)
[MAJOR] All findings accurately classified and addressed. The fail-first evidence was read correctly: Track 2 run 1 was a MISSING-INTERFACE run (AttributeErrors because the v2 interfaces did not exist), while the old code's wrong behaviour was proven separately by run 1b (returning True/True for counterexamples).
- C1: DISCLOSED-AS-OPEN (Forged event, boundaries disclosed in offline mode)
- C2: REPAIRED (W4 reproduced in driver v6)
- C3: DISCLOSED-AS-OPEN (History reset, boundaries disclosed)
- C4: REPAIRED (Missing args logged)
- C5: REPAIRED (Round 6441904 excluded by name)
- C6: REPAIRED (Decoded-bytes equality for signature)
- C7: REPAIRED (Draft text error fixed)
- C8: REPAIRED (Draft text filename fixed)
- C9: REPAIRED (Sentinel reconciliation requires reason)
- C10: REPAIRED (Minor text on seed wording)
- C11: DISCLOSED-AS-OPEN (verify_split unadopted, driver trust disclosed)
- C12: REPAIRED (Checklist no longer overstates repairs)

## 3. THE REMAINING TRUSTED STEP AND THE EXPECTED-RECEIPT IDENTITY
[MINOR] The delegated workflow's expired path relies on a receipt taken by the OPS session under an unadopted lane-proposed label (`{actor: ops-witness, session: OPS}`). A receipt forged by the lane as the first receipt under this label is NOT caught by the code, only by OPS's retained copy outside the lane. To close this gap by code, an INDEPENDENT EXPECTED-RECEIPT IDENTITY is needed: either a second GitHub identity's PushEvent actor (where `actor.login` = pinned witness login != lane's login) or a custodian key signature over the receipt. The lane's recommendation (Q1 Option C: no expired path at all) is sound, as it enforces completion within GitHub's feed window and avoids introducing any receipt or witness identity to trust.

## 4. COST AND FAILURE STATES
[MINOR] Cost is correctly stated as ONE PUSH PER COLLECTOR/BUILDER ATTEMPT (per history entry). Failure states are accurately defined: uncommitted extension and committed-but-unacknowledged = PENDING-PUSH; rejected push = DIVERGED; remote unreachable = RETRY. No sentence was found in the text that incorrectly says 'one push per freeze'.

## 5. PRESERVED ITEMS
[MINOR] The preserved items from V15 are intact and verified: sample sizes 400/200/2,000; floors 380/190/1,900; the 0.70 bar; the exclusions (failed set, 2,644 dry-run identities, historical rounds 6440756/6441904/6441924 by name); custody (E5(d)); blindness (no pixel/label before freezes); an ACTUAL FUTURE drand round (T_pulse > T_sign); the ONE holdout (Protocol.holdout_once prepared but unadopted). The inherited wrong E1 test count is annotated truthfully as a FACTUAL ERRATUM of the signed source without altering the signed substance. The inherited split-reconstruction limitation is disclosed (Protocol.verify_split staged unadopted and exhibited).

## 6. COUNTS AND NAMES
[MINOR] Every count and name in the text is TRUE. The execution of the suites confirms the number of tests (e.g., 23 and 17 in fourier_chirality, 10 in track1, 8 in track2). There is no aspirational or described-not-built text.

## 7. THE QUESTIONS FILE
[MINOR] The questions put to Duho exactly target the trust decisions that require his authority (whether an expired-receipt path should exist, and whether to provide a second identity/key), delegating all routine checks to the OPS session or the code. No more is asked of him.

## 8. WHAT IS STILL MISSING
[MINOR] Nothing is missing before Duho can be asked to adopt exact reviewed behaviour with concrete consequences. The staged candidate properly isolates unadopted track 2 modules and plainly discloses open boundaries.

VERDICT: SIGNABLE-AS-PRECOMMITMENT
