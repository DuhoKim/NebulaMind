# KUN_HC1H_FINAL_20260814

Timestamp: 2026-08-15 KST

Brief: `prereg/_tmp_KUN_HC1H_FINAL_BRIEF.md`

Inputs inspected:

- `prereg/LANA_ONE_HUMAN_ATTENUATION_20260814.md` —
  `04eac35f402774e464b8ab6cd8eff0a19a6a5a3ef5f7a61554ad598747c4c4e2`
- `prereg/KUN_HC1H_RECONFIRM_20260814.md` —
  `cc0e329a24391ac43e03d4aae3c9347abef716e118be6ffff5509000d9d6db86`

Boundary: documentation/gate only. I did not inspect sky data, rows, positions, images, chirality
labels, or sky statistics. I did not freeze, publish, accept, commit, or push anything. Duho owns
acceptance and is asleep.

## Verdict

**PASS THE TWO STATISTICAL REPAIRS; HOLD FREEZE FOR ONE REMAINING PROTOCOL-INTEGRITY REPAIR.**

The two statistical issues I held on are repaired:

1. the shared-`epsilon_hat` variance formula is now the correct summed-derivative delta expression;
2. the pilot no longer reuses pass-filtered synthetic labels in the final `epsilon_hat`.

I also inspected Lana's added value-blind carry-forward rule. I do **not** find a point-estimate
bias in carrying forward the pilot's 90 real labels and 20 retests, provided the pilot pass rule
remains exactly as written: no pass criterion may reference real-label agreement values or retest
non-flip values.

However, my previous HC-7 blocker is still not fully closed: **synthetic/repeat identity exposure**
is still not named as a hard INCONCLUSIVE trigger. The text says the human cannot distinguish
synthetic from real or first-showing from repeat, but HC-7 does not say what happens if that
assumption fails through visual recognizability, UI leakage, or obvious duplication rather than a
key compromise.

That is a narrow text repair. I see no remaining statistical blocker.

## 1. Variance Recompute

For

`a = sum_s w_s * (r_s - epsilon) / (1 - 2epsilon)`,

where one global `epsilon_hat` is shared by all strata, the derivative with respect to epsilon is:

`d a / d epsilon = sum_s w_s * (2r_s - 1) / (1 - 2epsilon)^2`.

Therefore:

`Var(a) = sum_s w_s^2 * Var(r_s)/(1 - 2epsilon)^2 + [sum_s w_s * (2r_s - 1)/(1 - 2epsilon)^2]^2 * Var(epsilon) + covariance terms conservatively >= 0`.

Lana's revised text now matches this structure:

> `sigma_a^2 = sum_s w_s^2*Var(a_hat_s)/(1-2epsilon_hat)^2 + [sum_s w_s*(2a_hat_s-1)/(1-2epsilon_hat)^2]^2*Var(epsilon_hat) (+ covariance >= 0)`

That is the correct shared-`epsilon` delta form. It is not merely different from the old diagonal
formula; it fixes the actual covariance problem.

Numerical check, balanced nine-stratum example:

- at `a = 0.90`, `epsilon = 0.02`, shared-epsilon contribution to `sigma_a` is about `0.00825`;
  diagonal-only would be about `0.00275`;
- at `a = 0.90`, `epsilon = 0.05`, shared-epsilon contribution is about `0.01370`;
  diagonal-only would be about `0.00457`;
- variance ratio is `9x`, standard-deviation ratio is `3x`.

The revised text states that relationship and withdraws the diagonal form. **Repair A passes.**

## 2. `a_gate` Recompute

Using the same conservative convention as before:

- `N = 130,076`
- `sigma_D = 1/sqrt(3N) = 0.0016008136762691544`
- `z_alpha + z_power = 3.2905267314919255 + 1.6448536269514722`
- `D_required = 0.007900624375386352`
- `A_required = 3 * D_required = 0.023701873126159057`
- `a_gate = (A_required / 0.0408 + 1) / 2 = 0.7904641314480276`

Lana's `0.7905` is the right frozen conservative gate. The stricter one-sided F-3 variant gives
about `0.7787`; choosing `0.7905` is acceptable because it is explicitly labeled as the more
conservative convention.

## 3. Pilot Carry-Forward

Lana's revised pilot rule:

- pilot synthetics are excluded from final `epsilon_hat`;
- final `epsilon_hat` comes from 200 fresh synthetics;
- pilot real labels and pilot retests may carry forward only if the pilot passes and the sealed-key
  chain is unbroken;
- no datum selected on may be reused in estimating the quantity it was selected on.

This fixes the dangerous bias I identified. The pilot pass criterion conditions on crude
synthetic `epsilon_hat < 0.10`, so reusing those synthetics would bias the final `epsilon_hat`
downward and inflate `a`. Lana excludes them.

The 90 real labels are different. The pilot pass criteria, as written, do not condition on
machine-human agreement values for those real labels. If those 90 are the predeclared first random
tranche, with the same strata, weights, blinding, and inclusion probabilities as the full HC-1H
design, carrying them forward is value-blind for the final `a` estimate.

The 20 retests are also value-blind under the written rule because pilot pass does not condition on
the non-flip rate. They can carry forward as part of the self-consistency/drift record if their
early-session timing is retained in the analysis. If a later revision adds any retest-value pass
criterion, those 20 must be excluded just like the synthetics.

So: **the carry-forward claim is clean under the frozen rule, but only under that rule.** It does
not relocate the synthetic selection bias into real labels unless pilot pass begins to use real
agreement, retest outcomes, or post-hoc session-quality judgments tied to label values.

## 4. Remaining HC-7 Issue

My previous re-gate required:

> add the synthetic/repeat identity exposure HC-7 trigger, or explicitly show why the existing key
> trigger covers it.

The current text has not done that. It says the human cannot distinguish synthetic from real or
first-showing from repeat, and HC-7 covers key compromise and visible machine/instrument signs. But
identity exposure can occur without a key problem: synthetic images may be visually obvious, repeat
pairs may be recognized, filenames/UI state may leak category, or session ordering may reveal them.

Required one-sentence repair:

> Synthetic/repeat identity exposure: if the checker can identify which items are synthetic,
> repeated, or mirrored repeats before key opening, the affected batch is void and the protocol
> returns hard INCONCLUSIVE unless a predeclared discard/replacement rule applies.

This is not a new stylistic objection. It is the same protocol-integrity blocker I named in
`KUN_HC1H_RECONFIRM_20260814.md`.

## Plain Answer For Duho

The two statistical repairs landed. The variance formula is now correct, `a_gate = 0.7905` checks
out, and the pilot's 90 real labels plus 20 retests can carry forward without bias under the
written value-blind rule.

I would still not freeze HC-1H until one narrow HC-7 sentence is added for synthetic/repeat identity
exposure. After that sentence, I see no remaining blocker from my HC-1H gates.

No real images, sky run, publication, freeze, acceptance, commit, or push follows from this gate.
