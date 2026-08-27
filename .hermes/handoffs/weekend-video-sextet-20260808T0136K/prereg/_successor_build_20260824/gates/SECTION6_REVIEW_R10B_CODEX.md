# SECTION6 REVIEW R10B — CODEX

Verdict: **NOT CLEAR**. The power-inapplicability cause split is substantively correct against the pinned code: a non-1,000 trial count returns `None`, but that state is a frozen-protocol deviation and therefore `VOID`, not a lawful inconclusive state. However, the dispatched identity does not bind the bytes reviewed; applying Clause 10 to the whole table exposes that the remaining `<962` branch is unreachable in post-unblinding Row P; and two unchanged explanatory/finding-map passages still promise a post-attrition Stage-C recomputation despite the ordered tree saying no rerun.

## Numbered findings

1. **BLOCKER — Subject identity / dispatch receipt: the reviewed R10B bytes do not match the send-time sha256.**
   - **Where:** `runner_s6rev10b_round.log` lines 1–3 versus `SECTION6_DRAFT_AGY_R10B.md`.
   - **Why it fails:** the log pins `4e36683e33cb8c69d13583b6d4bd271c3b0b78a06c7463f5d57b32d5112f263f`, says `changed lines R10 -> R10B: 0`, and thereby pins the bytes that are currently `SECTION6_DRAFT_AGY_R10.md`. Independent hashing of the actual R10B subject gives `ef35a8b1aad1b023ded0cb42b3632dfa1d14036d65b6bca788c8c772def88383`. A mechanical R10→R10B diff is non-empty (6 added and 5 removed content lines): it adds the power-deviation `VOID` repair in Row P and Part 2, rewrites C2 and finding 8, changes metadata, and adds finding 16. The referee brief expressly requires the file read to match the send-time hash; it does not.
   - **Smallest sufficient repair:** issue a corrected immutable dispatch log/receipt pinning `ef35a8b1…` (or restore the subject to the actually dispatched bytes and re-dispatch). Then rerun the referee against that exact pin. Do not overwrite the present log while retaining its original send-time claim.

2. **BLOCKER — Row P / Clause 10: the retained locked-Stage-C `<962` branch is unreachable on the only authorized post-unblinding path.**
   - **Where:** Row P line 53; Clauses 3(c), 3(d), and 10; Row J line 47; V15 lines 421–425; pinned code lines 1275–1277.
   - **Why it fails:** Row P is authorized only after unblinding and requires a verified BS-L. Clause 3(c) says `verify_lock()` checks BS-5f's PASS, Clause 3(d) requires that verified lock on the only verdict path, and Row J forbids continuing after Stage-C FAIL. V15 independently freezes Stage C before unblinding and says FAIL emits `INCONCLUSIVE-BY-POWER`, halts the run, and prevents any real-sky statistic. Consequently, a Row-P invocation can only inherit a locked Stage-C PASS; it cannot lawfully encounter a locked result below 962. Once R10 removed the post-attrition Stage-C rerun, the Row-P third branch became unreachable. The brief specifically says an unreachable branch is forbidden by Clause 10.
   - **Smallest sufficient repair:** delete the Stage-C power branch from Row P's post-unblinding adequacy tree and from Part 2 item 4. Keep the exact `<962/1,000 → INCONCLUSIVE-BY-POWER` decision where it is executable: pre-unblinding Row J / BS-5f. The post-unblinding adequacy receipt may bind the already-verified locked PASS and protocol digest, but must not pretend to branch on a FAIL that BS-L excludes.

3. **MAJOR — Part 3 C1 and Part 5 finding 5 contradict the frozen no-rerun decision.**
   - **Where:** Part 3 C1 line 115; Part 5 item 5 line 134; versus Row P line 53, Part 2 items 2 and 4 (lines 104 and 106), R3 line 124, and Part 5 item 13 line 142.
   - **Why it fails:** C1 still says post-unblinding exclusions rely on a consequence that is “recomputing power and potentially failing the verdict.” Finding-map item 5 still says the adequacy receipt binds a “re-evaluated Stage-C result.” Those are the old behavior. The normative ordered tree says any one removal immediately emits `INCONCLUSIVE-BY-CALIBRATION` and **no Stage-C rerun is performed**. The brief explicitly requires this proposition to agree everywhere, including residual/explanatory text; it does not.
   - **Smallest sufficient repair:** in C1, replace the recomputation claim with immediate `INCONCLUSIVE-BY-CALIBRATION` and no rerun. In Part 5 item 5, replace “re-evaluated Stage-C result” with the original locked BS-5f PASS/result and protocol digest, or simply remove the re-evaluation phrase.

## Power-inapplicability verification

The R10B cause split itself is correct. `successor_ref_v9.py` fixes `N_TRIALS = 1_000` and `CP_PASS_X = 962` at lines 77–78. At lines 1275–1277, audit refutation/nonconservatism returns `False`; otherwise `stage_power()` returns the boolean `succ >= CP_PASS_X` only when `n_trials == N_TRIALS`, and returns `None` when the count differs. No lawful unchanged-protocol inapplicability state was found. A changed trial count is a protocol/code-contract deviation, and V15 lines 570–573 makes such a post-first-real-χ change `VOID`. Deleting `INCONCLUSIVE-BY-POWER` for inapplicability was therefore the right repair. Finding 2 concerns the separate fact that the ordinary locked-FAIL branch is located in an unreachable post-unblinding row after the rerun was deleted.

## Whole-table Clause 10 test / failed attacks

- **Rows A–H held.** Authorized branches emit their named artifacts; forbidden touches have a fixed refusal/void consequence. Row B's pre-C2 request is explicitly refused and logged.
- **Rows I–O held.** Row I fails before BS-8f on an unusable allocated output; Row J terminates Stage-C FAIL pre-unblinding; Clauses 3(c)–(d) prevent such a failure from reaching BS-L or Row P. Rows K–O have fixed custody, verification, refusal, emission, or void consequences.
- **Row P did not hold.** The eight attempt states now have one consequence each, and missing/duplicate/orphan/malformed no longer collide with the void cell. The calibration-first attrition branch terminates and no discretionary retry remains. But the locked `<962` branch is unreachable after BS-L verification (Finding 2).
- **Rows Q–S held.** Archive-transition failure refuses lock verification; unauthorized content access voids; the default row forbids every unlisted touch; publication requires BS-V.
- **Clauses 1–9 held under the termination attack.** Clause 8 now refuses the run if retrospective custody remains unresolved at freeze; the decision remains pre-freeze rather than post-data. Clause 10 is a validation invariant rather than a data-dependent execution branch, but it fails when applied to Row P as above.
- The ordered calibration tree itself held: any attrition immediately terminates `INCONCLUSIVE-BY-CALIBRATION`, so there is no collision between calibration and a later power result in the normative row.
- The four join-anomaly repairs held: each now reaches only its named `INCONCLUSIVE-BY-*` refusal, while Row P's void cell is confined to out-of-symbol execution, silent inner-join loss, discretionary retry, and protocol/implementation deviation.

## Numeric and diff verification

- Actual R10B sha256: `ef35a8b1aad1b023ded0cb42b3632dfa1d14036d65b6bca788c8c772def88383` (does not match dispatch).
- V15 sha256: `efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28`.
- `successor_ref_v9.py` sha256: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- Calibration threshold held: V15 lines 566–567 and code lines 81 and 1492–1496 implement `a_LB_b < 0.85 → INCONCLUSIVE-BY-CALIBRATION`.
- Power numbers held: V15 lines 390–391 and code lines 77–78 and 1275–1277 fix 1,000 trials and PASS at `succ >= 962`, so ordinary threshold failure is `<962`.
- Archive count held: V15 lines 35 and 546 state 208,405 sealed predecessor measurements.
- No additional composed numeric decision threshold was found in the whole-draft sweep.
- R9C→R10 is confined to the three R10 repairs, the attrition wording correction, conforming explanation/finding-map text, and metadata. R10→R10B is confined to the power-inapplicability repair and metadata/finding-map text. The diff itself is confined; the dispatch log's “0” claim is not true of the present files.

## Testimony and limits

- Findings 1, 2, 2b, and 3 remain unresolved pending BS-2a. Rows C2 and E cannot run; BS-6 and the first image byte remain blocked.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch data, inspect χ-bearing bytes, or execute the scientific pipeline.
- I did not verify any future BS-2a artifact or future runtime implementation. The present review is of the prose, pinned reference code, V15, dispatch receipt, and exact inter-draft diffs.
- Because Findings 2–3 are prose-level defects independent of BS-2a, §6 is not yet sound apart from the BS-2a mechanism. If those passages are repaired and a correctly pinned subject is re-dispatched, the remaining open substance appears genuinely confined to BS-2a.

**NOT CLEAR**