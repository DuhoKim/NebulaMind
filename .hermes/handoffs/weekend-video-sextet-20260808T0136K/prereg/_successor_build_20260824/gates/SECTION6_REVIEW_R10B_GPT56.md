# SECTION 6 REVIEW R10B — GPT56

Verdict: NOT CLEAR. The power-inapplicability repair itself is substantively correct, but the dispatched artifact identity is not the identity recorded in the send-time log, the no-rerun rule still contradicts two whole-document statements, and Clause 10 exposes an overlapping Row-P outcome between attrition and protocol deviation. Those are freeze-blocking prose/custody defects. The remaining unresolved substance is still genuinely the BS-2a mechanism, but §6 is not yet sound enough to isolate the remainder to BS-2a.

## Numbered findings

1. **BLOCKER — artifact identity / dispatch custody.**
   - **Row/clause:** Brief lines 3–4; dispatch log.
   - **Why it fails:** The live sha256 of `SECTION6_DRAFT_AGY_R10B.md` is `ef35a8b1aad1b023ded0cb42b3632dfa1d14036d65b6bca788c8c772def88383`. `runner_s6rev10b_round.log` records `4e36683e33cb8c69d13583b6d4bd271c3b0b78a06c7463f5d57b32d5112f263f`, so the file read does not match the send-time pin the brief requires me to verify. Independent hashing shows that the logged digest is exactly the digest of `SECTION6_DRAFT_AGY_R10.md`, not R10B. The same log says `changed lines R10 -> R10B: 0`, while a direct diff shows the intended R10B repair in Row P, Part 2 item 4, Part 3 C2, Part 5 items 8 and 16, and metadata. This is not merely a cosmetic stale label: the dispatch receipt binds the predecessor bytes.
   - **Smallest sufficient repair:** Finalize R10B first, then regenerate the dispatch log from those exact bytes, recording the true R10B sha256 and a truthful nonzero R10→R10B diff summary; re-dispatch that pinned artifact for review.

2. **BLOCKER — Clause 10 finds two outcomes for the combined attrition-plus-protocol-deviation branch.**
   - **Row/clause:** Row P, Clause 10; Part 2 item 4 repeats the same ordering.
   - **Why it fails:** Row P calls the adequacy tree ordered and says **First**, any post-unblinding removal “immediately” emits `INCONCLUSIVE-BY-CALIBRATION`. The same row later says **any** deviation from the pinned 1,000-trial protocol or frozen Stage-C implementation terminates `VOID`. Attrition and a protocol/implementation deviation are not stated to be mutually exclusive. If both are present, “first/immediately INCONCLUSIVE” and “any deviation VOID” both fire. Clause 10 requires one stated outcome per branch; the repair therefore recreates the double-consequence defect at the intersection of two branches. The absolute wording does not establish which absolute rule has precedence.
   - **Smallest sufficient repair:** Make protocol/implementation conformance an explicit step zero, before the adequacy tree, and state that a deviation terminates `VOID` before and overrides every adequacy outcome. Then apply calibration applicability, calibration accuracy, and locked Stage-C power only to protocol-conforming runs. Mirror that ordering in Part 2 item 4 and the explanatory mapping.

3. **MAJOR — “no Stage-C rerun” remains inconsistent across the whole draft.**
   - **Row/clause:** Row P; Part 2 items 2 and 4; Part 3 C1 (line 115); Part 5 finding 5 (line 134); R3.
   - **Why it fails:** Row P, Part 2, R3, and Part 5 finding 13 correctly say that any removal immediately ends in `INCONCLUSIVE-BY-CALIBRATION` and no Stage-C rerun/re-evaluation occurs. But Part 3 C1 still says the design relies on the post-unblinding confidence-cut consequence “**recomputing power and potentially failing the verdict**.” Part 5 finding 5 still says the adequacy receipt binds a “**re-evaluated Stage-C result**.” Those are assertions of the old behavior, not neutral historical descriptions. The brief expressly requires the no-rerun rule to be consistent everywhere.
   - **Smallest sufficient repair:** In C1, replace the recomputation sentence with the actual consequence: any post-unblinding removal emits `INCONCLUSIVE-BY-CALIBRATION` without rerunning Stage C. In Part 5 finding 5, replace “re-evaluated Stage-C result” with the locked BS-5f Stage-C inputs/result (or exact wording that clearly means carried/bound, not recomputed).

## Power-inapplicability repair — independent result

The substantive choice to delete the lawful-inapplicability branch is correct.

- `successor_ref_v9.py` line 1277 returns a boolean only when `n_trials == N_TRIALS`; otherwise it returns `None`.
- Lines 77–78 pin `N_TRIALS = 1_000` and `CP_PASS_X = 962`.
- Production `build_plan()` passes `n_trials=N_TRIALS` into `_plan()` (lines 1303–1305), so the unchanged production protocol has no lawful differing-trial-count state.
- V15 lines 570–573 make a post-first-real-χ change to a binding rule, algorithm, reference-code byte, or decision threshold `VOID`.

Therefore a differing trial structure is a protocol departure, not a lawful power-inapplicability state. R10B correctly deletes `INCONCLUSIVE-BY-POWER` for that case and retains `INCONCLUSIVE-BY-POWER` only for the pinned boolean failure `< 962/1,000`. Finding 2 concerns precedence when that correct VOID branch overlaps attrition; it does not reverse this substantive result.

## Clause 10 whole-table test

I reapplied Clause 10 to Rows A–S and Clauses 1–10 rather than checking Row P alone.

- The four join anomalies now terminate once as `INCONCLUSIVE-BY-MISSING-RECORD`, `-DUPLICATE`, `-ORPHAN`, and `-MALFORMED`; they have been removed from Row P’s void column.
- Missing/non-finite/low-confidence states terminate as exclusions and then immediately lead to calibration inconclusiveness because they remove an object; no discretionary retry remains.
- Clause 8 now terminates: unresolved retrospective custody at freeze refuses the run.
- Stage-C FAIL cannot proceed to lock: Row J forbids continuation and Clause 3(c) refuses unblinding/verdict when lock verification cannot establish BS-5f PASS.
- Clause 10 itself introduces no delayed judgement; it states a termination invariant.
- The remaining failed Clause-10 case is the overlapping Row-P attrition/protocol-deviation branch in finding 2.

## Number sweep

The operative numeric claims checked cleanly:

- `1,000` trials and threshold `962` match `successor_ref_v9.py` lines 77–78 and V15 lines 390–391.
- `a_LB_b < 0.85` matches code line 81, `adjudicate_path()` lines 1492–1496, and V15 lines 566–567.
- `208,405` archived measurements matches V15 lines 35–36 and 546–547.
- V15 lines 570–573 support the cited void rule.

No new numeric fabrication or threshold drift was found.

## Diff-confinement test

The semantic R9C→R10 changes are confined to the stated join-anomaly cleanup, ordered no-rerun adequacy tree, terminating Clause 8, conforming explanatory/mapping edits, and metadata. R10→R10B is confined to the power-inapplicability/VOID repair plus its conforming explanation and metadata. The live diff is therefore substantively confined, although the dispatch log falsely reports zero changed lines and pins R10 rather than R10B (finding 1).

## Failed attacks

- I tried to find a lawful unchanged-protocol path producing `stage_power(...)=None`; production hard-pins `N_TRIALS`, so the attack failed.
- I tried to find the four join anomalies duplicated in Row P’s void column; they are absent.
- I tried to find old “void on attrition” language in R3; it has been removed.
- I tried to find Clause 8 still depending on a later principal judgement; it now refuses at freeze.
- I reswept the inherited numbers and found no mismatch.
- I compared both revision steps and found no unrelated semantic expansion.

## Testimony

- The operational claims about future hermetic enforcement, authenticated schemas, mediation, fixtures, and exact-parent closure are not verified here; the draft itself correctly leaves the relevant BS-2a findings unresolved/refused.
- The predecessor archive’s retrospective pre-freeze custody cannot be established from this prose or software. Clause 8 now treats that fact as a pre-freeze decision/refusal condition.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch data, execute the science pipeline, or modify the draft under review.

**NOT CLEAR**