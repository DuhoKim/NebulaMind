# V20 WHOLE-DOCUMENT REVIEW — GPT56

## Verdict

V20 is more honest than V19, and its new line 473 capability inventory is true as a statement about values actually returned by `run_production_verdict()`. It is nevertheless **NOT CLEAR**. One adjacent present-tense sentence still claims four production guards that the pinned runner does not have, and the newly admitted non-executable `VOID` category leaves Clause 10 reverse reachability unresolved without saying that this defect itself blocks BS-6. V20 is therefore potentially sound as an unfinished preregistration draft, but it is not yet a complete executable programme and still contains one false executable-capability claim.

## Subject identity — verified before opening

I first compared the SHA-256 computed by `shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V20_20260827.md` with the brief's required digest `607df3dd5b022a299162dac501b9c5766dda87bac8b3ba1cea11a105efa00261`. The command returned exactly:

`607df3dd5b022a299162dac501b9c5766dda87bac8b3ba1cea11a105efa00261  ../PREREG_SUCCESSOR_DRAFT_V20_20260827.md`

Result: **MATCH**. Only after that comparison did I open V20.

I separately compared the computed source hashes with §0's pins. `successor_ref_v9.py` returned `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` returned `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`. Both equal V20 lines 78–80.

## Numbered findings

### 1. HIGH / BLOCKING — §5 lines 458–473: the runner's return inventory is true, but the immediately preceding guard inventory is still false

**Why it fails.** V20 lines 458–461 say that `run_production_verdict()` “requires and verifies the canonical BS-L artifact and the one-use unblinding receipt,” verifies exact final-mask binding and post-unblinding ledger recomputation, and refuses if the adequacy tree emits an inconclusive result. Those are present-tense executable-capability claims. They are not implemented in the exact pinned source.

**Mechanical comparison and result.** I parsed the exact source file with SHA-256 `6a9abbbd…` and compared V20 lines 458–461 and 473 with the AST of `run_production_verdict()` at source lines 1591–1625.

- The parsed signature returned only `mask`, `cal`, `authorization_path`, `authorization_sha256`, `n_receipts`, `n_parent`, and `stage_c_receipt`.
- The parsed call set returned `require_environment`, `require_authorization`, `require_complete_sample`, `require_sealed`, `adjudicate_path`, `perm_record`, and `_decide_from` (plus ordinary helpers); it returned no lock, unblinding, final-mask, or adequacy verifier call.
- A whole-file source comparison for `verify_lock`, `unblind`, and `BS-L` returned **0 occurrences for each**.
- The function's two direct verdict literals were both `INCONCLUSIVE-BY-POWER`; `_decide_from()` assigned exactly `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, and `INCONCLUSIVE`.

That comparison credits V20 line 473: the runner really can return exactly those three numeric outcomes plus its Stage-C and `N_eq` `INCONCLUSIVE-BY-POWER` branches. It also falsifies lines 458–461's remaining present-tense guard claim. Line 473's “unresolved required implementation” list does not name the BS-L guard, unblinding-receipt authentication, final-mask binding, or adequacy-tree refusal, even though §6.1 clause 3(d), lines 550–551, requires the first of those on the only verdict path.

**Smallest sufficient repair.** Change lines 458–461 from present tense to an explicit unresolved requirement, add all four missing guards to line 473 and §11, and state that the production runner cannot be considered executable until they are implemented and fixture-tested. Do not claim the runner “requires and verifies” any artifact until the pinned function actually accepts and authenticates it.

### 2. HIGH / BLOCKING — §5 line 471, §6.1 Clause 10 line 566, §7/§11: `VOID` is honestly non-executable but still has no reverse-reachable producer, and V20 does not bind that defect to BS-6

**Why it fails.** Clause 10 says every branch of every row must terminate in one stated outcome. V20 now correctly says `VOID` “is not yet executable” and calls `VOID` conversion unresolved. That is honest disclosure, but it does not make the forbidden-act/protocol-deviation/non-finite branches reverse-reachable to the category. The brief permits this posture only if the document plainly states that reverse reachability does not yet resolve and that BS-6 remains blocked because of it. V20 does neither.

**Mechanical comparison and result.** I compared every V20 line containing `VOID` or a void rule against every line/paragraph containing `BS-6`:

- The scan returned void-related lines 373, 471, 473, 518, 556, 592, 594, and 803.
- It returned **0 lines** and **0 paragraphs** containing both `VOID` and `BS-6`.
- Clause 10 was found at line 566; the explicit non-executable admission was found at line 471; unresolved `VOID` conversion was found at line 473.
- A whole-source scan of pinned `successor_ref_v9.py` returned **0 occurrences** of `VOID`.

Forward prose naming exists; executable reverse reachability does not. V20's existing BS-6 blocks at lines 371–372 and 677 arise from BS-2a/C2, not from the missing `VOID` conversion.

**Smallest sufficient repair.** Add a direct Clause-10 status sentence: `VOID` reverse reachability is unresolved; therefore Clause 10 is not yet executable and BS-6 remains blocked until a pinned producer/conversion handles every enumerated void antecedent. Add the producer/conversion and its branch-complete fixtures to §11. Keep “not yet executable” until those bytes pass a gate.

### 3. LOW — §10 lines 797–805: the V19→V20 aggregate-validation trace overstates what the changed prose names

**Why it fails.** The trace says V20 “named `validate_calibration_aggregates` as the producer.” The V19→V20 diff did add the symbol, but line 469 calls it a validator “emitting the authenticated aggregate outcome”; it does not unambiguously say that this function produces the run-level `INCONCLUSIVE-BY-CALIBRATION` outcome. §11 line 822 repeats the aggregate-outcome wording. In the current source the symbol does not exist at all, which V20 properly treats as required work.

**Mechanical comparison and result.** The exact V19→V20 diff returned 9 deleted and 21 added lines. The symbol count changed from **0 in V19 to 3 in V20**. A whole-source scan returned **0 occurrences** of `validate_calibration_aggregates`. The added §5 and §11 text says validation/authenticated aggregate outcome; the added trace alone uses the stronger word “producer.”

**Smallest sufficient repair.** Either change the trace to “named the required aggregate validator and its authenticated aggregate outcome,” or change §5/§11 to state exactly which component converts validator failure into the single run-level registry outcome. The latter is preferable because it also closes producer reachability.

## Central capability ruling

**V20 line 473 is true, narrowly read as a return-value inventory.** The comparison was V20 line 473 against the AST and source bodies of `run_production_verdict()` lines 1591–1625 and `_decide_from()` lines 1561–1588. It returned two direct `INCONCLUSIVE-BY-POWER` literals in the runner and three numeric verdict assignments in the helper, and no other returned verdict literal. `adjudicate_path()` lines 1492–1496 can raise `InconclusiveByCalibration`; it does not return a run outcome, which is consistent with V20 marking the Row-J calibration guard unresolved.

That narrow success does not cure Finding 1: the same §5 paragraph still claims lock/unblinding/final-mask/adequacy guards absent from the code.

## Clause 10 and threshold audit, both directions

I compared the threshold-bearing branches in §§0–11 with their exact source constants/conditions and their stated lifecycle phase/failure effect:

- `N_eq`: V20 lines 184, 462–473 versus source `NEQ_MIN = 100_000` and lines 1613–1616. Returned comparison: `< 100,000` produces the runner's `INCONCLUSIVE-BY-POWER`; equality passes. Value, production phase, and failure effect agree.
- Numeric decision regions: V20 line 468 versus source lines 1579–1584 and constants lines 73, 79–80, 83. Returned comparison: `p < 0.001`/positive sign/3σ band/floor for reproduction; `p > 0.05` and strict amplitude-band inequality for rejection; complement is numeric inconclusive. The prose and code agree.
- Calibration ordering: V20 lines 388, 448, 530, 588–589 versus source lines 1492–1496. Returned comparison: `< 0.85` raises before the spread test; on the complement, `<= 0.03` is scalar and `> 0.03` is profile. Value and order agree, but the lifecycle outcome conversion is not implemented and is disclosed at line 473.
- Stage P/C count threshold: V20 lines 417–418 and Row J line 530 versus source `N_TRIALS = 1_000`, `CP_PASS_X = 962`, and lines 1275–1277. Returned comparison: any `refuted` or `nonconservative` condition returns failure; otherwise 1,000-trial execution passes iff successes are `>= 962`. Value and failure direction agree. V20 separately discloses that its preferred exact-per-trial Stage P is not in the definitional code.
- Post-unblinding accounting/attrition: V20 lines 475–477 and Row P line 536 give an ordered, single-valued prose partition and fixed failure effects, but the source scan returned zero occurrences for all accounting outcome names and all per-attempt state names. V20 line 473 correctly marks these unresolved.
- `VOID`: forward antecedents are named at lines 471, 556, and 592–595, but reverse executable reachability returned none, producing Finding 2.

Result: I found no additional threshold-value inversion or phase ambiguity beyond the two blocked conversions above. The document is honest about several non-executable branches, but Clause 10 is not executable as a whole.

## §10 repair-trace audit — four entries

I compared each adjacent pair with `git diff --no-index --unified=1`; exit code 1 means the compared files differ and the returned hunks were inspected. A separate `difflib.SequenceMatcher` count returned these changed-line totals: V16→V17 28 deleted/61 added; V17→V18 17/37; V18→V19 13/21; V19→V20 9/21.

1. **V16→V17 — ACCURATE in V20.** Exact count comparison returned the class-P sentence unchanged at “One of fourteen” in both files, while Class E changed from 7 to 8. The diff also returned the §6.3 title bodies, Row-P citation replacement, Stage-C gate/pre-attrition text, candidate-evidence narrowing, and 0.03 spread addition described by V20 lines 773–780.
2. **V17→V18 — ACCURATE.** The diff returned removal of “Reason (d),” sole BS-2a threshold ownership, floor-before-spread ordering, run/per-attempt registry separation including Row-I abort, chronology repair, and the two repair-trace blocks described at lines 782–789.
3. **V18→V19 — ACCURATE.** The diff returned the lifecycle-registry/process naming, the then-narrowed runner claim, non-finite split, §6.3/Row-P citation trace expansion, partial-repair addition, and label correction described at lines 791–795.
4. **V19→V20 — ACCURATE for A–D and Trace repair; PARTIAL for E.** The diff returned the exact runner return inventory, both runner power guards, `VOID` non-executability, the corrected 7→8 Class-E wording, and three new `validate_calibration_aggregates` mentions. The claimed producer role is stronger than the changed §5/§11 wording, as Finding 3 records.

## Failed attacks / adjacent checks that held

- **Pinned identity attack failed:** V20 and both §0 code pins matched their claimed SHA-256 values.
- **Central return-inventory attack failed:** the exact AST comparison returned only the three numeric helper verdicts plus the runner's two `INCONCLUSIVE-BY-POWER` branches.
- **Power-producer completeness attack failed at the prose level:** V20 line 469 now includes Row J plus both production-runner power guards.
- **Row-I overlap attack failed:** line 469 excludes Row-I missing allocated outputs from aggregate non-finite/degenerate calibration handling and keeps its separate outcome.
- **Per-attempt/run-cardinality attack failed:** lines 466–475 still separate exactly one lifecycle run outcome from zero-or-more attempt states.
- **Trace count attack failed after correction:** exact V16/V17 comparison returned class P unchanged at 14 and Class E changed 7→8, matching V20's repaired trace.
- **No invented orchestration-symbol attack:** whole-source searches found no lock/unblinding/aggregate-validation symbols; V20 does not invent a new orchestration symbol as executable. The defect is the surviving natural-language present-tense claim in Finding 1.

## Testimony / not mechanically verified

The following V20 assertions were not promoted to mechanical findings because this pass did not compare them with their primary evidence: the Longo source quotation and bibliographic claims; chronology and referee timestamps; previous-seat verdict summaries; real-geometry counts and the 995/1000 Stage-P measurement; closure reproduction counts; fixture transcript claims; authority/authorization history; and claims about immutable V15–V19 custody beyond the hashes computed here. They remain **Testimony** in this report.

I did not read `/Users/duhokim/NebulaMindData/`, did not fetch anything, did not run real data, did not open secrets, and did not read the sibling CODEX report.

## Evidence ledger

Content read:

- `gates/BRIEF_V20_WHOLE_REVIEW.md` (all 74 lines).
- `PREREG_SUCCESSOR_DRAFT_V20_20260827.md` (all 822 lines), only after its digest matched.
- `ref/successor_ref_v9.py` lines 1492–1625 plus searched constant/guard/Stage-P regions.
- V16, V17, V18, and V19 only through exact hashes, adjacent diffs, and targeted occurrence comparisons needed for §10.
- The three loaded local audit skills supplied method discipline only; they are not evidence about V20.

Commands/comparisons and returned results:

- `pwd` after absolute `cd`: returned the assigned `.../_successor_build_20260824/gates` directory.
- `shasum -a 256` on V20, both reference files, and V16–V19: returned the hashes recorded above; V19 also matched V20's banner pin `b7deb106…`.
- AST comparison of the pinned runner/helper: returned the seven arguments, call set, two direct power verdict literals, and three helper numeric literals recorded above.
- Whole-source regex comparisons: returned zero occurrences for `verify_lock`, `unblind`, `BS-L`, `validate_calibration_aggregates`, accounting outcomes, per-attempt outcomes, and `VOID`.
- Four exact adjacent diffs: returned the hunks and change counts recorded in the trace section.
- Targeted V16–V20 occurrence comparison: returned Class P 14 unchanged; Class E 7→8 at V17; Row-P citation V15→§6.3 at V17; Reason-(d) removed/Row-P-state-(7) added at V18; aggregate-validator mentions 0→3 and `VOID` non-executable 0→1 at V20.
- V20 `VOID`/BS-6 paragraph comparison: returned eight void-related lines, zero same-line and zero same-paragraph `VOID`/BS-6 co-occurrences.
- Pre-write `git status --short`: returned a heavily pre-existing dirty/untracked repository, including sibling `V20_WHOLE_REVIEW_CODEX.md`; this report path was absent before my write.

## Scope and programme status

This verdict judges the whole V20 document as instructed. Findings 1, 2, 2b, and 3 remain declared unresolved; BS-2a remains refused; Rows C2 and E cannot run; BS-6 and the first image byte remain blocked. V20's disclosure of unfinished implementation is generally honest. The blocking defects here are narrower: one surviving false present-tense runner claim and one Clause-10/BS-6 consequence not stated for the admitted non-executable `VOID` category.

**NOT CLEAR**