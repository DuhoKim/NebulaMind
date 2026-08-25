HOLD_C2_CRITERION_DRIFT_ROW_MISCLASSIFICATION_AND_SCOPE_EXCESS

# Phase 4 Track C adversarial gate

## 1. Criterion drift after registration

The registered brief itself was not changed: the current `TRACK_C_BRIEF.md` SHA-256 is `1b4fd2e434e5c37a04758489aeaac37bfed7b59acb4eb883035a60541bc2a661`, matching `TRACK_C_GO_RECORD.md` and the bytes at commit `ae0af84b`.

The execution nevertheless bends registered C2 criterion 2. The brief requires that an anomaly's angular size **correspond to** `ℓ ≲ 10` (`TRACK_C_BRIEF.md:29`). The verdict substitutes “`ℓ ≲ 10` reachable” and awards passes because a broader range merely includes low multipoles: B3.1 passes because `ℓ ≲ 40` “includes it,” and B3.3 passes because `ℓmax 26` includes it (`TRACK_C_VERDICT.md:25`). Inclusion in a broader estimator range does not establish that the anomaly's angular size corresponds to `ℓ ≲ 10`. This is a post-registration weakening of the test.

The same row awards B3.2 a scale pass from the qualitative phrase “large angles,” and awards B3.5–B3.7 a grouped generic pass, although the freeze supplies no common per-row angular-size value for those entries. Under the registered test these are unproved or gaps, not passes.

## 2. C2 table does not state each frozen row's statistic class correctly

`TRACK_C_VERDICT.md:22-27` calls itself “Per-row evidence” but collapses B3.5, B3.6, and B3.7 into one column and labels them “same statistic classes.” The freeze states three different forms:

- B3.5: a quadrupole cumulative result plus a full-sky `C(θ)` interval (`TRACK_B_FREEZE.md:81`);
- B3.6: Bayesian odds and a qualitative evidence conclusion (`TRACK_B_FREEZE.md:82`);
- B3.7: estimator/mask-dependent full-sky-versus-masked p-values (`TRACK_B_FREEZE.md:83`).

They are not one statistic class, and the grouped `pass`/`FAIL` cells do not state each row's class or evidence. B3.1 is also called a “full-sky spectrum statistic” (`TRACK_C_VERDICT.md:24`), while the freeze records only a low-`ℓ` power deficit and does not state “full-sky” for that row (`TRACK_B_FREEZE.md:77`). That added classification is not supported by the frozen table.

## 3. Scope excess in the verdict language

The phase summary calls `x_max(t)` “the branch's first quantified hiding condition” without the mandatory direct-post-recombination-photon and pre-horizon restrictions (`TRACK_C_VERDICT.md:54-58`). Amendment 1 limits the result to direct post-recombination photons whose complete paths remain interior and to `t_obs ≤ t_crit`, with other messengers and the post-exit regime unanalyzed (`TRACK_A_VERDICT.md:44-55`). The unqualified summary is broader than the gated Track A result.

## 4. Kill-criteria compliance is overstated

K-C2 requires naming a gap whenever the comparison needs a number absent from the freeze (`TRACK_C_BRIEF.md:54-55`). Instead, the C2 scale row converts absent per-row `ℓ ≲ 10` correspondence for B3.2 and B3.5–B3.7 into passes (`TRACK_C_VERDICT.md:25`). The compliance claim “no number outside the freeze was used” (`TRACK_C_VERDICT.md:47-48`) does not cure the failure to name missing scale evidence.

K-C3 requires all verdict language to remain photon-channel-only and pre-horizon-only (`TRACK_C_BRIEF.md:56-58`). The unqualified “hiding condition” in the phase summary violates that rule, so the blanket K-C3 compliance claim at `TRACK_C_VERDICT.md:48-50` is false.

## 5. Phase summary is not supported line by line

Two claims fail the named-artifact support test:

- “the `z_c = √N` law” (`TRACK_C_VERDICT.md:55`) appears nowhere in `TRACK_A_VERDICT.md` (including Amendment 1), `TRACK_B_FREEZE.md`, `TRACK_C_BRIEF.md`, or `TRACK_C_GO_RECORD.md`. The named gate record therefore does not support this summary item line by line.
- “an 8-corruption-proof frozen bounds apparatus” (`TRACK_C_VERDICT.md:56-57`) overstates the freeze. The freeze records a finite battery of eight corruption cases that fail and a 50-row verifier result (`TRACK_B_FREEZE.md:10-14,44`); it does not establish that the apparatus is corruption-proof.

The remaining summary items do not remove these concrete defects. Track C must rerun the registered scale test without replacing correspondence by inclusion, provide genuinely per-row classes/evidence, mark unavailable scale evidence as gaps, and restore the Track A channel/epoch qualifiers before this gate can pass.
