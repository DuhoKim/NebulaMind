# §6 NINTH-PASS C (R9C) REFEREE REPORT — GPT56

## Verdict

NOT CLEAR. The two R9 repairs choose honest fail-closed terminal consequences rather than pretending that an unfrozen post-unblinding predicate exists, and both numeric thresholds remain exact copies of the pinned record. But applying new Clause 10 to the whole table exposes unresolved termination conflicts. Row P assigns the missing/duplicate/orphan/malformed branches an `INCONCLUSIVE-BY-*` outcome while its own “what voids the run” column says the same branches void the run. Its attrition path also has no precedence across calibration and power outcomes; indeed every possible attrition now unconditionally fails calibration, making the promised Stage-C re-evaluation either unreachable or a competing second outcome. Clause 8 separately declares retrospective custody open for a later principal judgment. Those are prose-level branch defects, not BS-2a implementation details. Blocking findings: 1–3.

## Numbered findings

### 1. BLOCKER — Row P gives four join-anomaly branches two different terminal consequences

**Row / clause.** Row P, line 53; Clause 10, line 83.

**Why it fails.** Row P’s ordered state partition says: zero records emits `INCONCLUSIVE-BY-MISSING-RECORD`; duplicates emit `INCONCLUSIVE-BY-DUPLICATE`; extras emit `INCONCLUSIVE-BY-ORPHAN`; malformed records emit `INCONCLUSIVE-BY-MALFORMED`. The final column of the same row then lists “missing/duplicate/extra/malformed records” under “what voids the run.” The brief expressly asks whether inconclusive or void is the honest state; they are therefore not interchangeable labels. Each of these four branches reaches two stated dispositions, so Clause 10’s requirement that every branch terminate in one stated outcome fails against the table itself.

**Smallest sufficient repair.** Choose one status class for these four branches. The smaller and more coherent repair is to keep the named `INCONCLUSIVE-BY-*` refusals and delete missing/duplicate/extra/malformed from Row P’s void column, reserving void for prohibited execution outside the symbol, silent inner-join loss, and discretionary retry. If the intended legal state is void instead, delete the four inconclusive emissions and say `VOID` explicitly.

### 2. BLOCKER — the post-attrition calibration and power predicates have no cross-predicate precedence

**Row / clause.** Row P, line 53; Clause 10, line 83; Part 2 items 3–4, lines 105–106; residual risk R3, line 124.

**Why it fails.** Committee attrition unconditionally emits `INCONCLUSIVE-BY-CALIBRATION`. Non-committee attrition also unconditionally emits `INCONCLUSIVE-BY-CALIBRATION`, because the applicability predicate is absent. Those two cases exhaust attrition. Yet the same row says every removal forces re-evaluation of the locked adequacy predicates and separately emits `INCONCLUSIVE-BY-POWER` when the Stage-C rerun is below 962/1,000 or cannot apply that exact criterion. Part 2 likewise requires both calibration and Stage-C re-evaluation. For an attrited mask that also fails power, the prose does not say whether calibration terminates first, power terminates first, both are emitted, or power is never run. The explicit precedence list covers per-attempt states only; it does not order these adequacy predicates.

The present fail-closed calibration rule also makes every post-attrition Stage-C branch unreachable if “emits” means immediate termination. That contradicts Part 2’s promise to re-evaluate Stage C and R3’s “strict recomputation protocol.” R3 compounds the conflict by saying post-unblinding failure “would void the run,” whereas Row P assigns `INCONCLUSIVE-BY-CALIBRATION` or `INCONCLUSIVE-BY-POWER`.

**Smallest sufficient repair.** Freeze an ordered adequacy decision tree. If calibration is first, state that any attrition immediately emits `INCONCLUSIVE-BY-CALIBRATION`, no Stage-C rerun is performed, and replace R3’s “void” language with that outcome. If both checks must run, define one deterministic combined or precedence outcome for simultaneous failures and make Part 2 and R3 use the same disposition. Do not leave the executor to choose which failure names the result.

### 3. BLOCKER — Clause 8 is expressly open and depends on a later principal judgment

**Row / clause.** Clause 8, line 79; Clause 10, line 83; §6.2, line 87; residual risk R2, line 123.

**Why it fails.** Clause 8 says the retrospective-custody question is “open” and that “its resolution is a freeze-level decision for the principal.” Clause 10 says a consequence depending on a judgment made later is not a termination. The draft never states what archive seal/custody facts make the run eligible, what outcome follows if retrospective custody cannot be established, or whether the principal’s decision is non-operative disclosure policy rather than a validity branch. Naming the decision-maker does not terminate the branch.

This is not the same as asking software to prove historical access. The prose can remain candid that history is unknowable while still freezing the consequence of that uncertainty.

**Smallest sufficient repair.** Before freeze, state one deterministic consequence: either inability to establish retrospective custody refuses/voids the run, or retrospective uncertainty has no effect on execution/verdict and must appear only as a fixed disclosure limitation. Remove the later discretionary principal choice.

### 4. HIGH DESIGN COST — any post-unblinding attrition now forces calibration inconclusive

**Row / clause.** Row P, line 53; Part 2 item 4, line 106; residual risk R3, line 124.

**Why it matters.** The committee/non-committee split is exhaustive. Removing any committee member emits `INCONCLUSIVE-BY-CALIBRATION`; removing any non-committee object emits the same outcome because no frozen applicability predicate exists. Therefore one absent, non-finite, or low-confidence object among the fixed attempts is sufficient to end the study inconclusive. The design is not logically guaranteed to fail—there is a zero-attrition branch—but it is now a single-attrition-intolerant design, and the advertised post-attrition power rerun cannot rescue it.

The pinned V15 reports 65,060 raw objects. No inspected frozen file supplies a per-object attrition rate, so “near-certain” cannot be verified. The scale sensitivity is nevertheless severe: under an illustrative independent per-object attrition model, only `1.06539115922e-5` per object makes at least one attrition 50% likely; `4.60446250283e-5` makes it 95% likely; and `1e-4` makes it 99.850604053% likely. These are sensitivity calculations, not measured rates.

**Smallest sufficient repair.** Price this as an explicit design acceptance before freeze, or build and gate a mechanically frozen non-committee calibration-applicability predicate in the eventual BS-2a design. Do not describe the current route as robust to post-unblinding attrition.

## Requested judgments

1. **Are the new terminal consequences the right ones?** Yes in kind. `INCONCLUSIVE-BY-POWER` is the honest result when the exact frozen Stage-C contract cannot execute; inability to execute an adequacy check is not itself evidence that the preregistered run was void. `INCONCLUSIVE-BY-CALIBRATION` is likewise the conservative fail-closed result when calibration applicability cannot be established from the frozen record. The defect is not those labels; it is their collision with Row P’s void column, the missing precedence between calibration and power, and R3’s inconsistent “void” wording.
2. **Does fail-closed missing applicability make the study always inconclusive?** Not as a logical identity: zero post-unblinding attrition remains a possible path. But any attrition whatsoever is now sufficient, so the design may be overwhelmingly likely to terminate inconclusive at 65,060 opportunities even at very small attrition rates. No actual rate was available in the authorized files, so near-certainty remains Testimony.
3. **Is §6 now sound apart from BS-2a?** No. Findings 1–3 are independent prose-level termination defects. Once they are repaired, the remaining findings 1, 2, 2b, and 3 can genuinely remain confined to the refused BS-2a mechanism.

## Whole-table Clause 10 walk / failed attacks

1. **Rows A–H held.** Their authorized path emits the named artifact, while out-of-surface behavior falls under the table’s void column and Clause 5. Row B’s pre-C2 Row-D request has the fixed refusal-and-log result.
2. **Rows I–O held.** Row I’s missing/non-finite allocated-output predicate explicitly fails the run before BS-8f; its complement emits BS-8f. Row J’s FAIL cannot continue to BS-L; Clause 3(c) refuses unblinding/verdict when BS-5f is not PASS. Rows K–O have fixed emission or void/refusal consequences.
3. **Row P did not hold.** The attempt-state precedence closes silent join loss, the two newly added fail-closed branches do terminate individually, and no discretionary retry remains. Findings 1–2 are the residual collisions exposed only when the whole row is treated as one decision tree.
4. **Rows Q–S otherwise held.** Clause 7 makes nonconforming archive transitions refuse `verify_lock()` and therefore unblinding/verdict; unauthorized archive-content reads void under Clauses 5 and 7. Row R’s default is forbidden; Row S requires BS-V before publication.
5. **Clauses 1–7 and 9 held under the termination attack.** Their failure branches resolve to unfillable gates, verifier refusal, or void. Clause 8 did not hold (Finding 3).
6. **The two numeric-threshold attacks failed.** V15 lines 566–567 states any `a_LB_b < 0.85` is `INCONCLUSIVE-BY-CALIBRATION`; code line 81 fixes `A_FLOOR = 0.85`, and lines 1492–1496 use the same strict-less-than comparator. V15 lines 390–391 states 1,000 trials and pass at `x >= 962` (961 fails); code lines 77–78 fix `N_TRIALS = 1_000` and `CP_PASS_X = 962`, and line 1277 applies `succ >= CP_PASS_X` only at the frozen trial count. R9C’s “fewer than 962” wording is exact.
7. **The whole-draft numeric sweep held.** I found no residual composed numeric decision threshold. The other material count, 208,405 archived measurements, is inherited from V15 rather than a decision gate. The 65,060 population used in the design-cost analysis is pinned at V15 line 225.
8. **Subject identity held.** Recomputed R9C sha256 is `ad2b23f058a4304025a1b267d8790ec563a4a61c5384a8017185ab6b7300c576`, exactly matching `runner_s6rev9c_round.log`.
9. **Frozen identities held.** Recomputed sha256 values are V15 `efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28` and `successor_ref_v9.py` `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
10. **Diff confinement held, with one chronology clarification.** R8B→R9 changes Row P’s two terminal consequences, matching Part 2/Part 3/Part 5 explanations and metadata. R9→R9B adds Clause 10 plus its Part 5 entry and metadata. R9B→R9C rewrites Clause 10’s rationale plus the matching Part 5 entry and metadata. No unrelated lifecycle/table rule moved. Thus the Row P changes occur in R8B→R9, not in the literal R9→R9B or R9B→R9C sub-diffs.
11. **Standing state held.** BS-2a remains REFUSED/UNFILLED; Rows C2 and E cannot run; BS-6 and the first image byte remain blocked. This pass did not purport to resolve findings 1, 2, 2b, or 3.

## Testimony and limits

I did not read `/Users/duhokim/NebulaMindData/`, fetch data, inspect images, cutouts, χ values, sealed-store payloads, credentials, keys, committee records, or runtime attestations, or execute the scientific pipeline. I did not verify a future BS-2a or Row-P implementation. I found no authorized evidence of the actual absent/non-finite/low-confidence rate, independence between objects, or retrospective archive access. The attrition probabilities above are explicitly illustrative sensitivity calculations, not observations.

## Evidence ledger

- Read `BRIEF_SECTION6_REVIEW_R9C.md`, `SECTION6_DRAFT_AGY_R9C.md`, `runner_s6rev9c_round.log`, `SECTION6_DRAFT_AGY_R9.md`, `SECTION6_DRAFT_AGY_R9B.md`, `SECTION6_DRAFT_AGY_R8B.md`, and both R8B referee reports.
- Read pinned `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` around the Stage-C contract (lines 385–425), calibration and void rules (lines 550–573), and the 65,060-object count (lines 223–232).
- Read pinned `../ref/successor_ref_v9.py` constants (lines 68–88), `stage_power()` decision code (lines 1218–1277), and `adjudicate_path()` (lines 1487–1496).
- Recomputed all hashes quoted above; mechanically diffed R8B→R9, R9→R9B, and R9B→R9C; enumerated numeric literals and threshold language across R9C; independently computed the stated attrition sensitivities.
- No write occurred except this referee report.

**NOT CLEAR**