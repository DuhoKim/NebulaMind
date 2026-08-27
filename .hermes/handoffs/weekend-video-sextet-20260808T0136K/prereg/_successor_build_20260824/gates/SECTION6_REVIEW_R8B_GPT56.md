# §6 EIGHTH-PASS REPAIR B (R8B) REFEREE REPORT — GPT56

## Verdict

NOT CLEAR. The two replacement numeric predicates are genuine inherited thresholds, not composed values: V15 defines calibration failure at any `a_LB_b < 0.85`, and the pinned reference defines a 1,000-trial Stage-C pass at `x >= 962` (therefore failure below 962). Row I's halt reveals an aggregate completeness failure, not a handedness value or direction; unconditional refusal when an allocated committee object is removed is a conservative, determinate choice; and refusing an entire 65,060-object run for any unusable row would be operationally brittle. But R8b still leaves an expressly reachable Row-P branch without a consequence: if the 962/1,000 rule is “inapplicable,” the draft merely requests a future threshold. That is post-unblinding policy freedom and leaves the verdict path unevaluable. This is a prose defect, not merely the acknowledged future BS-2a implementation work. Blocking finding: 1.

## Numbered findings

### 1. BLOCKER — the stated post-attrition power “gap” has no terminal consequence

**Row / clause.** Row P (R8b line 53); Part 2 items 3–4 (lines 103–104); Part 3 C2 (line 114); Part 5 defect 4 (line 132).

**Why it fails.** Row P deterministically emits `INCONCLUSIVE-BY-POWER` when a same-contract Stage-C rerun returns fewer than 962 successes out of 1,000. It then introduces a second branch: if attrition makes that criterion inapplicable, the text says only that a “defined post-attrition threshold” is required. It neither forbids entry to that branch, emits a terminal state, nor identifies a pre-unblinding slot that must freeze the missing rule. Consequently, after real outcomes are visible, the verdict path can arrive at a condition for which this draft supplies no answer. Declaring that a policy gap exists is candid, but candor does not make the gate decidable.

The frozen record gives a smaller and safer answer than inventing another threshold. V15 §4 lines 421–425 says Stage C uses the **same frozen generator, addresses and pass rule** on the accepted-position mask. `successor_ref_v9.py` lines 1218–1277 fixes the 1,000-trial behavior and returns PASS only when `succ >= CP_PASS_X`; a nonstandard trial count returns `None`, not a new threshold. A post-attrition adequacy rerun can therefore require the same 1,000-trial contract on the final sealed mask. If that exact rerun cannot be formed, the correct deterministic consequence is refusal, not a later-created numeric rule.

**Smallest sufficient repair.** Replace the gap sentence with one of these fully frozen consequences, preferably the first: (a) the post-attrition Stage-C rerun MUST use the same frozen generator, addresses, 1,000 trials, and `x >= 962` pass rule on the canonical final mask, and inability to execute that exact contract emits `INCONCLUSIVE-BY-POWER`; or (b) unconditional refusal under a separately named terminal state. Do not authorize a future post-unblinding threshold.

### 2. MINOR — post-unblinding calibration re-use is numerically correct but its applicability must remain a frozen predicate

**Row / clause.** Row P line 53; Part 2 items 3–4; residual risk R3 line 122.

**Why it matters.** The number and inequality are correct. V15 lines 566–567 states `a_LB_b < 0.85` means `INCONCLUSIVE-BY-CALIBRATION`, and `successor_ref_v9.py` line 81 fixes `A_FLOOR = 0.85`; the executable comparator is at lines 1492–1496. Although V15 describes the consequence as a pre-unblinding halt, the predicate is the inherited calibration-admissibility floor and is the right numerical predicate to carry into a later adequacy check.

What the floor does **not** establish by itself is that the frozen calibration remains applicable to a confidence-/finiteness-attrited final population. R8b makes removal of an allocated committee object an unconditional calibration refusal, which is a sound conservative rule, and the receipt binds a `calibration applicability` result. But that result must be mechanically derived from a rule frozen before outcomes, not supplied after unblinding. To the extent this rule depends on the still-refused BS-2a confidence design, it is legitimate BS-2a work; the §6 prose should make that dependency explicit rather than permit an uninstantiated applicability judgment.

**Smallest sufficient repair.** State that the post-unblinding adequacy verifier accepts calibration applicability only under the pre-unblinding predicate frozen in the eventual BS-2a design/protocol digest; missing or non-evaluable applicability emits `INCONCLUSIVE-BY-CALIBRATION`. Retain the unconditional refusal for removal of any allocated committee object and retain the inherited `a_LB_b < 0.85` floor.

### 3. LOW — the mechanical R8→R8b diff is not literally “only the thresholds changed”

**Row / clause.** File heading/status; Row P; Part 3 C2.

**Why it matters.** `git diff --no-index` shows four edit regions in substance/form: (1) the title changes R8 to R8B; (2) the status points to the R8B brief; (3) Row P replaces the three invented thresholds and adds the inapplicability-gap sentence; and (4) Part 3 adds a new C2 explanation. No unrelated lifecycle, actor, clause, or route rule changed. Thus the normative change is confined to threshold handling, but the literal statement “only the thresholds changed” is false because metadata and explanatory prose also changed.

**Smallest sufficient repair.** No normative repair is needed beyond finding 1. Describe the diff accurately as “only threshold handling changed normatively, plus R8B metadata and the corresponding C2 explanation.”

## Requested judgments

1. **Row I leakage.** The halt discloses the aggregate completeness fact that at least one allocated object has no usable finite output. It does not disclose a χ value, sign, handedness direction, object identity, or count. Missingness could still be outcome-adjacent or correlated with morphology; independence is not proved. Within route (b), fail-closed treatment is safer than silently calibrating a changed sample.
2. **Allocated committee-object removal.** Unconditional `INCONCLUSIVE-BY-CALIBRATION` with frozen recalculation forbidden is a conservative and determinate choice. It avoids a post-allocation subset/recalculation degree of freedom. I found no prose reason to weaken it.
3. **Unconditional refusal on any unusable row.** The design rationale is directionally sound but “near-certain” is Testimony without a frozen per-object unusable-output rate. For 65,060 independent opportunities, an unusable probability of about `4.60446e-5` per object already makes at least one unusable output 95% likely; at `1e-4`, the probability is about 99.8506%. Conversely, at `1e-6`, it is only about 6.30%. The document need not prove near-certainty to reject the route: an all-or-nothing rule is plainly brittle at this scale, while R8b's exact accounting plus frozen adequacy refusal can be safer if findings 1–2 are closed.
4. **Is §6 sound as prose apart from BS-2a?** Not yet. Finding 1 is an independent Row-P prose blocker. Finding 2 may properly be discharged by the eventual BS-2a design only if §6 makes the dependency and fail-closed consequence explicit. Once those bounded repairs are made, the remaining channel-closure mechanism can genuinely stay in BS-2a rather than trigger another broad §6 rewrite.

## Checks that held / failed attacks

1. **Subject identity held.** Recomputed R8b sha256 is `5a407225ec21792cfe4c342d2dec681943eb00a7a376f90053f297e56a03f2a2`, exactly matching the brief.
2. **Frozen-file identities recorded.** V15 sha256 is `efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28`; `successor_ref_v9.py` sha256 is `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, matching the V15 BS-2m receipt's displayed prefix.
3. **Calibration-threshold attack failed.** V15 lines 566–567 contains the exact `a_LB_b < 0.85` refusal predicate. Code line 81 contains `A_FLOOR = 0.85`; lines 1492–1496 apply the same strict-less-than comparator. Equality at 0.85 is admissible, as R8b implies.
4. **Power-threshold attack failed.** Code lines 77–78 contain `N_TRIALS = 1_000` and `CP_PASS_X = 962`; lines 1218–1277 apply `succ >= CP_PASS_X` only for the frozen trial count. V15 lines 390–391 independently states `x >= 962`, with 961 failing. R8b's “fewer than 962 out of 1,000” is exact.
5. **Whole-document numeric-threshold sweep held.** The only numeric decision thresholds in R8b's replacement/conforming prose are 0.85 and 962/1,000. The other substantive numeric literal, 208,405 archived measurements, is an inherited count repeated in V15 line 546, not a decision threshold. I found no residual ε=0.1, sample-size=400, power=0.8, or other composed numeric gate.
6. **Terminal-state closure attack mostly failed.** R8b now names the eight-state precedence, refuses missing/duplicate/orphan/malformed joins, drops absence/non-finite/low-confidence deterministically, forbids retry, and binds the parent set, complete partition, final mask, adequacy inputs/result, protocol digest, and verifier result in a separately named post-unblinding receipt. The remaining defect is the explicit inapplicability branch in finding 1, not the old silent-inner-join seam.
7. **Temporal BS-5f attack failed.** Row J now says BS-5f certifies only the locked pre-attrition mask, and Part 2 requires the verdict guard to verify both the old BS-5f and the separately named post-unblinding adequacy receipt against the final mask.
8. **Standing-state candor held.** BS-2a remains REFUSED/UNFILLED; Rows C2/E and BS-6 remain blocked. Part 5 correctly separates the resolved refusal of impossible future-execution facts from the unresolved BS-2a mechanism.

## Testimony

I did not read `/Users/duhokim/NebulaMindData/`, fetch data, inspect any image, cutout, χ value, sealed-store payload, key, credential, committee record, or runtime attestation, or execute the scientific pipeline. I did not verify a future BS-2a or Row-P implementation. The statement that unusable outputs are near-certain was not verifiable from the frozen files inspected; I evaluated its dependence on an assumed per-object rate and label it Testimony rather than fact.

## Evidence ledger

- Read `BRIEF_SECTION6_REVIEW_R8B.md`, `SECTION6_DRAFT_AGY_R8B.md`, `SECTION6_DRAFT_AGY_R8.md`, `SECTION6_REVIEW_R7_GPT56.md`, and `SECTION6_REVIEW_R7_CODEX.md`.
- Read frozen `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` around §4 lines 385–425, §5 lines 429–437, calibration lines 544–573, and the BS-2m/slot area.
- Read frozen `../ref/successor_ref_v9.py` constants lines 68–95, `stage_power()` lines 1218–1277, and calibration/adjudication lines 1446–1496.
- Recomputed sha256 values for R8b, R8, V15, and `successor_ref_v9.py`; mechanically diffed R8→R8b; enumerated numeric literals and searched the entire R8b draft for threshold/floor/inequality language.
- Independently calculated the any-failure probabilities for 65,060 opportunities. No data or fitted failure rate was used.
- No write occurred except this referee report.

**NOT CLEAR**