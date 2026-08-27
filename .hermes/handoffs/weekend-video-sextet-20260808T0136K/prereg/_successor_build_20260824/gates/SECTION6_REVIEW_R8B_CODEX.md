# CODEX referee report — proposed replacement §6, eighth pass R8B

## Verdict

**NOT CLEAR.** The two replacement numeric thresholds are genuine frozen values, not composed numbers: calibration fails at any `a_LB_b < 0.85`, and the 1,000-trial power rule fails below 962 successes. R8B also makes the exact-parent terminal-state partition materially more decidable. But Row P still leaves two post-unblinding branches to future policy: it explicitly permits the frozen 962/1,000 rule to become “inapplicable” without assigning a terminal consequence, and it binds a `calibration applicability` field without defining the applicability predicate for non-committee attrition. Those are verdict-path freedoms after outcomes are available, not merely missing BS-2a implementation bytes. §6 is therefore not yet sound as prose; the remaining blockers are not confined to the acknowledged BS-2a mechanism.

## Numbered findings

### 1. BLOCKING — the “inapplicable” Stage-C branch has no terminal consequence and invites a forbidden post-unblinding threshold

**Row / clause.** Row P, line 53; Part 2 items 2–4, lines 102–104; V15 void rule, lines 570–573; frozen code lines 77–78 and 1277.

**Why it fails.** The ordinary branch is now exact and correct: `N_TRIALS = 1_000`, `CP_PASS_X = 962`, and `stage_power()` returns `succ >= CP_PASS_X` only when `n_trials == N_TRIALS`. Thus “fewer than 962 passing trials out of 1,000” is the inherited failure predicate.

The next sentence defeats decidability: if attrition makes that criterion inapplicable, R8B records only “a stated gap requiring a defined post-attrition threshold.” It does not say who may define it, when it must have been frozen, or what Row P emits now. Because this branch is reached after unblinding, defining a new threshold then would directly conflict with V15 lines 570–573, which void any post-first-real-χ change to a decision threshold. A named gap is candid, but candor is not a terminal state. A gate still cannot decide whether to emit `INCONCLUSIVE-BY-POWER`, void the run, or wait for a newly composed threshold.

The hypothesized trial-structure change is also not forced by ordinary attrition: frozen `stage_power(mask, a, STAGE_C, ..., n_trials=N_TRIALS)` accepts a changed mask while retaining 1,000 trials. If some final mask cannot satisfy the function’s frozen input contract, that is a failure to execute the frozen test, not authority to substitute a different threshold.

**Smallest sufficient repair.** Freeze one consequence in the prose now: re-run the pinned Stage-C procedure on the final mask with exactly 1,000 trials and the frozen 962-success rule; if the pinned procedure is inapplicable, cannot return a Boolean, or cannot execute under its frozen contract, emit `INCONCLUSIVE-BY-POWER` and refuse the verdict. Delete the invitation to define a post-attrition threshold. Any genuinely different trial structure requires a new preregistration before unblinding, not a Row-P repair after unblinding.

### 2. BLOCKING — `calibration applicability` remains an undefined post-unblinding policy for non-committee attrition

**Row / clause.** Row P, line 53; Part 2 items 2–4, lines 102–104; Part 4 R3, line 122.

**Why it fails.** R8B correctly freezes two consequences: removal of any allocated committee member unconditionally emits `INCONCLUSIVE-BY-CALIBRATION`, and any inherited per-bin lower bound below 0.85 emits the same result. But the adequacy receipt also binds “calibration applicability,” while no rule computes that field for the ordinary case in which absent, non-finite, or low-confidence non-committee objects are removed.

Re-reading the unchanged pre-unblinding calibration artifact does not re-evaluate applicability to a selected final population. The old `a_LB_b` values do not change merely because non-committee objects were removed. The prose does not state whether survival-conditioned selection is accepted as preserving calibration, which frozen evidence proves that, or which fixed failure follows when applicability cannot be established. Consequently an executor must still supply a substantive Boolean after unblinding. This is the same class of freedom R7 asked the draft to remove.

The inherited 0.85 predicate itself is valid post-unblinding as a fail-closed re-check of the already frozen calibration artifact, despite V15 calling its original use a pre-unblinding halt. What is missing is not a new numeric floor; it is the applicability rule for the changed final mask.

**Smallest sufficient repair.** Before unblinding, define a mechanically evaluable calibration-applicability predicate for every permitted terminal-state partition and bind its inputs to the adequacy receipt. If that predicate cannot be defined without new design work, make inability to establish applicability emit `INCONCLUSIVE-BY-CALIBRATION`. Retain the unconditional committee-member-removal refusal and the inherited `a_LB_b < 0.85` floor. Do not permit Row P to invent a post-result calibration-validity rule.

### 3. LOW — the R8→R8B claim “only the thresholds changed” is false literally, though no unrelated operational rule changed

**Row / clause.** Mechanical diff; R8B lines 1, 3, 53, and 114.

**Why it fails.** The diff has four hunks: the title changed R8→R8B; the governing-brief name changed; Row P’s invented thresholds were replaced; and a new Part 3 choice C2 was inserted. Therefore “only the thresholds changed” is not byte-accurate. The extra edits are administrative or explanatory and all relate to the threshold correction; I found no unrelated lifecycle, custody, actor, terminal-state, or BS-2a disposition change.

**Smallest sufficient repair.** Describe the scope exactly: “Only Row P’s operational threshold rule changed; the remaining diffs are the R8B label/brief reference and the explanatory C2 entry.”

## Direct judgments requested by the brief

1. **Numeric thresholds.** Verified. V15 lines 566–567 say any `a_LB_b < 0.85` produces `INCONCLUSIVE-BY-CALIBRATION`; `successor_ref_v9.py` line 81 sets `A_FLOOR = 0.85`, and lines 1492–1496 enforce it. V15 lines 390–391 state the 1,000-trial, `x >= 962` rule; code lines 77–78 set `N_TRIALS = 1_000` and `CP_PASS_X = 962`; line 1277 compares `succ >= CP_PASS_X`. R8B’s “fewer than 962” wording is exact. I found no other composed decision threshold in R8B. The other material counts I checked also trace: 208,405 appears in V15 lines 35–36 and 546; 65,060 appears in V15 lines 225 and 612.
2. **Post-unblinding use of `a_LB_b < 0.85`.** Correct as a conservative re-check of a frozen artifact, not as a newly computed post-unblinding threshold. It does not by itself establish calibration applicability after outcome-conditioned attrition; Finding 2 remains.
3. **Declared power gap.** Insufficient. It leaves the verdict branch unevaluable and suggests a threshold could be defined only after unblinding. Finding 1 gives the fail-closed repair.
4. **Row I halt before BS-8f.** The halt directly discloses only an aggregate completeness/finiteness fact: at least one allocated object had no usable finite output. It does not disclose a handedness sign or direction. Whether that missingness is statistically associated with handedness or morphology is unverified Testimony, so the draft must not claim independence. The fail-closed halt is the safer prose choice.
5. **Allocated committee-member removal.** Unconditional `INCONCLUSIVE-BY-CALIBRATION` with frozen recalculation forbidden is the right conservative rule. A post-unblinding replacement allocation or recalculation would introduce selection freedom after outcomes are known.
6. **Refusal on every unusable row.** I found no frozen evidence in the files reviewed that proves unusable outputs are “near-certain” among 65,060 objects; that rationale is Testimony. The policy conclusion is nevertheless reasonable: unconditional refusal on any unusable row is needlessly brittle if and only if the final-mask power and calibration applicability contracts are complete and fail closed. R8B has not yet met that condition because of Findings 1–2.
7. **Whether to stop rewriting §6.** Not yet. The BS-2a implementation/schema findings can remain unresolved, but Row P itself still needs the two prose-level terminal consequences above.

## Failed attacks / what held

1. Subject identity held: SHA-256 of R8B is `5a407225ec21792cfe4c342d2dec681943eb00a7a376f90053f297e56a03f2a2`, exactly the brief’s pin.
2. The calibration floor held independently in both frozen sources: V15 lines 566–567 and code lines 81 and 1492–1496.
3. The power threshold held independently in both frozen sources: V15 lines 390–391 and code lines 77–78 and 1277.
4. The prior invented `epsilon >= 0.1`, sample-size `< 400`, and power `< 0.8` rules are absent from R8B.
5. The terminal-state prose now names fixed keys, a pinned attempt set, an ordered closed partition, explicit refusal/exclusion consequences, a duplicate refusal, an orphan refusal, and no retry. I did not find a remaining permission for silent inner-join loss.
6. The BS-5f temporal overclaim is removed: Row J now limits BS-5f to the pre-attrition mask, and Row P requires a separate adequacy receipt after a final-mask change.
7. The committee-removal branch is determinate and conservative.
8. Beyond the four diff hunks identified in Finding 3, the rest of R8 and R8B is byte-identical.

## Testimony and limits

I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, inspect any image/cutout/χ value, inspect sealed payloads, or execute future Row-P/BS-2a code. I did not verify actual missingness rates, the claim that an unusable output is near-certain among 65,060 attempts, statistical independence of missingness/non-finiteness/confidence from handedness or morphology, historical archive access, runtime mediation, or future calibration representativeness. Those assertions remain Testimony or design obligations, not observed facts.

## Evidence ledger

- Read `BRIEF_SECTION6_REVIEW_R8B.md`, `SECTION6_DRAFT_AGY_R8.md`, `SECTION6_DRAFT_AGY_R8B.md`, and prior `SECTION6_REVIEW_R7_CODEX.md` as text.
- Read frozen `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` around the power rule, calibration admissibility, void rule, and cited population counts.
- Read frozen `../ref/successor_ref_v9.py` constants and the `stage_power()` / `adjudicate_path()` decision code.
- Recomputed SHA-256: V15 `efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28`; `successor_ref_v9.py` `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; R8 `f3d4509bb4d45b4b84ebee361f30166332a348f15f207dab0e114c9c2a7b96ad`; R8B `5a407225ec21792cfe4c342d2dec681943eb00a7a376f90053f297e56a03f2a2`.
- Ran `git diff --no-index -- SECTION6_DRAFT_AGY_R8.md SECTION6_DRAFT_AGY_R8B.md` and a `difflib.SequenceMatcher` hunk inventory. Changed regions are R8/R8B lines 1, 3, 53, plus the inserted R8B line 114.
- Wrote only this referee report. No production artifact, frozen source, data file, or preregistration draft was modified.

**NOT CLEAR**