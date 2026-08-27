# SECTION6 REVIEW R9C — CODEX

Verdict: **NOT CLEAR**. Clause 10 exposes two still-open/contradictory consequence branches in Row P and directly conflicts with Clause 8's expressly deferred principal judgement. The new non-committee-attrition consequence is honest fail-closed handling, but the power-inapplicability consequence needs a cause split so a frozen-protocol deviation cannot be downgraded from void to inconclusive. The numeric thresholds and the dispatched draft identity independently verify, and the R8B→R9→R9B→R9C changes are confined to the represented Row P repairs, Clause 10, metadata, and conforming explanation/finding text.

## Numbered findings

1. **MAJOR — Row P / Clause 10: four record-integrity branches have two stated outcomes, not one.**
   - **Where:** Row P, consequence text and `what voids the run` cell (draft line 53); Clause 10 (line 83).
   - **Why it fails:** zero, duplicate, extra, and malformed records emit respectively `INCONCLUSIVE-BY-MISSING-RECORD`, `INCONCLUSIVE-BY-DUPLICATE`, `INCONCLUSIVE-BY-ORPHAN`, and `INCONCLUSIVE-BY-MALFORMED` in the row body. The same four conditions are then listed in Row P's `what voids the run` cell. The brief expressly distinguishes an inconclusive terminal result from voiding. Each of these branches therefore has two incompatible consequences. Clause 10 requires exactly one.
   - **Smallest sufficient repair:** choose one consequence for each condition and make both cells agree. If the intended terminal result is the named `INCONCLUSIVE-BY-*`, remove those conditions from the void cell. If record-set corruption is intended to void the run, replace the named inconclusive emissions with `VOID` and say so. Do not retain both.

2. **MAJOR — Clause 8 / Clause 10: the retrospective-custody branch is expressly left to later judgement.**
   - **Where:** Clause 8 (line 79) versus Clause 10 (line 83), also §6.2 (line 87).
   - **Why it fails:** Clause 8 says the retrospective-custody question is `open` and that its resolution is a freeze-level decision for the principal. Clause 10 says a consequence depending on a judgement made later is not a termination. The document therefore fails its new rule against itself: it states neither the admissible custody-evidence states nor a fixed terminal consequence for each state.
   - **Smallest sufficient repair:** freeze a custody decision rule now. Enumerate the evidence states and map each to one terminal consequence (for example, proceed only on a specified authenticated attestation/evidence predicate; otherwise refuse/void). A future principal choice is not a terminal rule.

3. **MAJOR — Row P power-inapplicability branch conflates lawful inadequacy with frozen-protocol deviation.**
   - **Where:** Row P line 53; Part 2 item 4 line 106; V15 lines 570–573; pinned `successor_ref_v9.py` lines 77–78 and 1275–1277.
   - **Why it fails:** the pinned code fixes `N_TRIALS = 1_000`, `CP_PASS_X = 962`, and returns a boolean pass/fail whenever `n_trials == N_TRIALS`; it returns `None` when the trial count differs. R9C says that if the exact criterion cannot be applied, "e.g., because the trial structure differs," the run emits `INCONCLUSIVE-BY-POWER`. But a changed trial count/structure caused by departing from the frozen protocol is a binding-rule/code/threshold-contract deviation and is void under V15 lines 570–573, not merely inconclusive. R9C does not identify a distinct, conforming frozen state that makes the criterion inapplicable. Thus this branch either (a) downgrades a void to inconclusive or (b) is unreachable.
   - **Smallest sufficient repair:** split causes. Any deviation from the pinned 1,000-trial protocol or frozen Stage-C implementation must terminate `VOID`. `INCONCLUSIVE-BY-POWER` may remain only for a specifically named inapplicability state produced by the unchanged frozen protocol; name that predicate and its receipt field. If no such lawful state exists, delete the inapplicability branch and apply the pinned `<962` rule.

4. **HIGH, DESIGN CONSEQUENCE — Row P is attrition-intolerant: one post-unblinding removal ends the study inconclusive by calibration.**
   - **Where:** Row P line 53; Part 2 item 4 line 106; V15 lines 302–310.
   - **Why it fails as a design:** every removal is either of an allocated committee member or a non-committee object. The first unconditionally emits `INCONCLUSIVE-BY-CALIBRATION`; the second also fails closed to `INCONCLUSIVE-BY-CALIBRATION` because no frozen applicability predicate exists. Therefore any single `EXCLUDED-BY-ABSENCE`, `EXCLUDED-BY-NONFINITE`, or `EXCLUDED-BY-CONFIDENCE` event makes the verdict path inconclusive. The frozen parent has 65,060 objects (V15 lines 302–305), so the design has no tolerance for even one such event. This also makes the later post-attrition Stage-C power branches unreachable after any removal under the stated calibration precedence.
   - **Smallest sufficient repair:** either explicitly accept and prominently state the one-removal-means-inconclusive design, or—before any image byte—freeze a mechanically evaluable non-committee calibration-applicability predicate and its receipt semantics in the replacement BS-2a design. The latter is the smallest repair that preserves a potentially conclusive study; it belongs to the still-refused BS-2a mechanism.

## The two new terminal consequences

- **Non-committee attrition → `INCONCLUSIVE-BY-CALIBRATION`: correct as fail-closed prose, not a void.** Missing calibration applicability is inadequacy, not itself a custody or frozen-rule breach, and the consequence is now fixed before real χ is read. Its severe design cost is Finding 4.
- **Inapplicable 962/1,000 criterion → `INCONCLUSIVE-BY-POWER`: conditionally correct only for a conforming, pre-frozen inapplicability state.** R9C does not name such a state and its example can include frozen-protocol deviation, which must void. Finding 3 is required before this consequence is sound.

## Numeric and identity verification

- Dispatched R9C sha256 in `runner_s6rev9c_round.log`: `ad2b23f058a4304025a1b267d8790ec563a4a61c5384a8017185ab6b7300c576`.
- Independently recomputed R9C sha256: `ad2b23f058a4304025a1b267d8790ec563a4a61c5384a8017185ab6b7300c576`. Identity holds.
- Pinned V15 sha256 recomputed: `efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28`.
- Pinned `successor_ref_v9.py` sha256 recomputed: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- Calibration: V15 lines 566–567 require every `a_LB_b ≥ 0.85` and assign `INCONCLUSIVE-BY-CALIBRATION` for any `a_LB_b < 0.85`; code line 81 fixes `A_FLOOR = 0.85`. R9C matches.
- Power: code lines 77–78 fix `N_TRIALS = 1_000` and `CP_PASS_X = 962`; lines 1275–1277 implement pass as `succ >= CP_PASS_X` for exactly `N_TRIALS`, hence failure is `<962/1,000`. R9C matches.
- A comparison-operator and numeric-literal sweep of R9C found no additional composed numeric decision threshold. The other material number in §6 is the inherited archive count `208,405`, not a decision threshold.

## Diff-confinement verification

Independent unified diffs show:

- R8B→R9: Row P's non-committee calibration fail-closed consequence and power-inapplicability consequence; matching Part 2 item 4, Part 3 C2, finding-map entries, and R9 metadata.
- R9→R9B: Clause 10 addition, matching finding-map addition, and metadata.
- R9B→R9C: Clause 10's explanatory sentence, matching finding-map rewrite, and metadata.

No unrelated normative table row, clause body, or threshold moved in this chain.

## Failed attacks

- The dispatched hash matched the bytes reviewed.
- `a_LB_b < 0.85` is not composed; it matches both V15 and pinned code.
- `<962 passing trials out of 1,000` is not composed; it matches the pinned constants and boolean comparison.
- Committee attrition has a fixed terminal consequence.
- Non-committee attrition now has a fixed terminal consequence rather than a missing applicability judgement.
- The no-removal accepted-finite path reaches the post-unblinding adequacy receipt and then BS-7f/BS-V.
- The diff-confinement claim held.

## Testimony

- The brief states that attrition is near-certain at 65,060 objects. No empirical attrition-rate artifact was authorised or read in this pass, and `/Users/duhokim/NebulaMindData/` was not accessed. I therefore do not independently assert a probability. What is independently established is the stronger structural sensitivity: **any one removal** forces `INCONCLUSIVE-BY-CALIBRATION` under R9C.

## Standing scope

Findings 1, 2, 2b, and 3 from the standing state remain unresolved pending the replacement BS-2a design; Rows C2 and E cannot run, BS-6 and the first image byte remain blocked. §6 is **not yet sound as prose** because Findings 1–3 above are internal branch-termination defects, not merely missing BS-2a mechanism detail. Finding 4 is genuinely BS-2a design work.

**NOT CLEAR**