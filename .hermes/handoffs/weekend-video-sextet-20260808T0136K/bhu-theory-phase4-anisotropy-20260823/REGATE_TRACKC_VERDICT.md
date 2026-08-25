HOLD_B3_STATISTIC_CLASSES_NOT_FREEZE_VERBATIM

# Phase 4 Track C — Amendment 1 regate

## Verdict

Amendment 1 discharges four of the five gate objections and most of the fifth. It correctly reruns C2 under the registered correspondence criterion, marks all seven B3 scale cells as gaps, splits B3.5/B3.6/B3.7, withdraws the unsupported B3.1 full-sky label, restores the Track A Amendment 1 channel/path/epoch scope, names the K-C2 gaps, binds the `z_c = √N(η_e)` law to `A3_RECEIPT.md`, and replaces “corruption-proof” with a finite eight-case statement. One concrete residue remains: the amendment says its per-row statistic classes use “the freeze's own words,” but several header labels introduce words absent from `TRACK_B_FREEZE.md`; B3.5 is materially recast as a “cumulative posterior,” although the freeze states only “ΛCDM at cumulative 0.824” and never identifies that quantity as a posterior. The exact-freeze-word requirement is therefore not yet met.

## Objection-by-objection regate

### 1. Registered C2 criterion drift — DISCHARGED

`TRACK_C_BRIEF.md:26-33` requires angular-size correspondence to `ℓ ≲ 10`, not mere inclusion in a broader estimator range. Amendment 1 restores that exact criterion at `TRACK_C_VERDICT.md:68-72` and records all seven B3 scale entries as `GAP — no angular-size value frozen` at line 78. No row is still awarded a scale pass from `ℓ ≲ 40`, “large angles,” `ℓmax 26`, or `θ > 60°`.

### 2. Per-row statistic classes — PARTIAL; BLOCKING RESIDUE

The structural defects are repaired: B3.5, B3.6, and B3.7 now have separate columns, and the B3.1 “full-sky spectrum statistic” label is explicitly withdrawn at `TRACK_C_VERDICT.md:82-83`.

But the amendment's stronger claim at `TRACK_C_VERDICT.md:72-75`—that each class is stated “in the freeze's own words”—is false. A direct term search finds none of `TT`, `real-space`, `temperature-map`, `posterior`, or `two-point correlation statistic` in `TRACK_B_FREEZE.md`, while all appear in the amended header. The sharpest defect is B3.5:

- freeze (`TRACK_B_FREEZE.md:81`): `COUNTER: quadrupole not anomalous` / `ΛCDM at cumulative 0.824; full-sky C(θ) within 95%`;
- amendment (`TRACK_C_VERDICT.md:75`): `quadrupole cumulative posterior + full-sky C(θ) interval`.

“Posterior” is neither frozen nor a neutral byte-level restatement of “cumulative 0.824”; it assigns a statistic type the freeze does not assign. The added `TT` for B3.1 and `real-space temperature-map` for B3.2 are also outside the freeze's words, even if scientifically plausible. Under this regate's exact frozen-record rule, plausibility cannot substitute for frozen wording.

Required repair: replace each B3 header's statistic-class label with the literal corresponding `bound / claim` wording from `TRACK_B_FREEZE.md:77-83` (optionally copying its value cell separately). In particular, B3.5 must not say `posterior` unless that classification is first frozen through an authorized Track B addendum.

### 3. Track A scope excess — DISCHARGED

The corrected phase summary limits `x_max(t_obs)` to a hiding condition for `DIRECT POST-RECOMBINATION PHOTONS ON WHOLLY-INTERIOR PATHS, PRE-HORIZON EPOCHS ONLY` (`TRACK_C_VERDICT.md:102-104`). This matches Track A Amendment 1's direct-photon, complete-interior-path, and `t_obs ≤ t_crit` limitations (`TRACK_A_VERDICT.md:44-55`).

### 4. Kill-criteria compliance — DISCHARGED

K-C2 is now satisfied for the challenged scale comparison: the missing correspondence evidence is named as a gap for every B3 row (`TRACK_C_VERDICT.md:78,91-95`), with no new value harvested. K-C3's challenged summary language now carries the photon-channel, wholly-interior-path, and pre-horizon qualifiers. No residue from the prior K-C2/K-C3 objections remains.

### 5. Phase-summary support — DISCHARGED

`A3_RECEIPT.md:4-9` explicitly derives and claims `z_c(center) = √N(η_e)` and says it was verified against the A2 solver to `1e-6`; `A3_RECEIPT.md:59-61` again names the `z_c = √N` law. The amended summary now cites that receipt rather than implying the law appears in the verdict set.

The former “8-corruption-proof” overclaim is replaced by `EIGHT EMBEDDED CORRUPTION CASES ALL FAIL (a finite battery, not a proof of corruption-proofness)` (`TRACK_C_VERDICT.md:104-106`), matching `TRACK_B_FREEZE.md:10-14`.

## Failed attacks

The correspondence/inclusion attack, seven-row gap accounting, B3.5/B3.6/B3.7 grouping attack, B3.1 full-sky-label attack, direct-photon/wholly-interior/pre-horizon scope attack, K-C2 gap attack, `z_c` provenance attack, and corruption-proofness attack all hold under Amendment 1. Only the exact frozen-statistic-class wording attack remains.

## Gate boundary

This regate addresses only Amendment 1 against the five objections in `GATE_TRACKC_VERDICT.md`. It does not reopen unrelated sibling findings or authorize the post-PASS bibliography/update sequence. A narrow header-only amendment copying `TRACK_B_FREEZE.md:77-83` literally is sufficient for another regate.
