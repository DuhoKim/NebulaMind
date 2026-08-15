# KUN_HC1H_RECONFIRM_20260814

Timestamp: 2026-08-14 KST

Brief: `prereg/_tmp_KUN_HC1H_RECONFIRM_BRIEF.md`

Inputs inspected:

- `prereg/LANA_ONE_HUMAN_ATTENUATION_20260814.md` —
  `45e6edea87afe923afbb436388d0bbeaf2a7be85c983631d35c2efa677b4cd30`
- `prereg/KUN_HC1H_GATE_20260814.md` —
  `efccbd8c24856b8224c9aabf273289ccf419394ed58731c9e69957de76226c95`
- `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260814_CANDIDATE.md`
- `prereg/GORU_BS8_POWER_RECEIPT_20260814.md`

Boundary: documentation/gate only. I did not inspect sky data, rows, positions, images, chirality
labels, or sky statistics. I did not freeze, publish, accept, commit, or push anything. Duho owns
acceptance.

## Verdict

**HOLD FOR TWO STATISTICAL REPAIRS.**

Lana delivered the five repairs in spirit:

- `a_gate = 0.7905` is corrected and properly separated from the retained `0.85` quality floor.
- `sigma_a` is no longer frozen as `0.012`.
- `epsilon_syn` is global, with per-stratum rates diagnostic only.
- `a` is named as the HC-1H one-human, synthetic-error-corrected attenuation estimate, not a
  multi-human truth reference.
- HC-7 hard integrity triggers are present.

But two new load-bearing issues appear in the repaired text:

1. **The global-`epsilon` variance formula undercounts covariance unless repaired.** Because the
   same global `epsilon_hat` corrects every stratum, its uncertainty is shared across strata. The
   variance contribution from `epsilon_hat` must be computed after summing the weighted
   derivatives, not as only `sum w_s^2 * derivative_s^2 * Var(epsilon_hat)`.
2. **The optional pilot carry-forward rule is biased as written if pilot labels count after a pass
   criterion that includes `epsilon_hat < 0.10`.** Conditional on passing a low synthetic-error
   pilot screen, carrying those same pilot synthetics into the final `epsilon_hat` biases the final
   error estimate downward unless the sequential selection is modeled. That would inflate `a`.

These are narrow and fixable. I still do not reject HC-1H as a design.

## 1. Recomputed `a_gate`

Using the lane's normal approximation:

- `sigma_D = 1 / sqrt(3N)`
- `E[D_hat] = (2a - 1) * 0.0408 / 3`
- require `E[D_hat] >= (z_alpha + z_power) * sigma_D`

At `N = 130,076`:

- `sigma_D = 0.0016008136762691544`
- with `z_alpha = 3.2905267314919255` and `z_power = 1.6448536269514722`,
  `D_required = 0.007900624375386352`
- on the amplitude scale, `A_required = 0.023701873126159057`
- `a_gate = (A_required / 0.0408 + 1) / 2 = 0.7904641314480276`

With the stricter one-sided F-3 convention `z_alpha = 3.090232306167813`, I get:

- `a_gate = 0.7786761147076118`

Therefore Lana's choice to freeze `0.7905` is acceptable and conservative, provided it remains
identified as the conservative gate convention. The repaired text does that.

## 2. Recomputed `sigma_a` Rule

The repaired design correctly withdraws `sigma_a ~= 0.012` as a promise and uses a formula-only
rule. That repairs the first-order problem.

However, the formula as printed is still not safe for a global error correction:

> `sigma_a^2 = sum_s w_s^2 * [ Var(a_hat_s)/(1-2epsilon_hat)^2 + ((2a_hat_s-1)/(1-2epsilon_hat)^2)^2 * Var(epsilon_hat) ]`

That is the diagonal-only expression. It is correct if every stratum has an independent
`epsilon_hat_s`. Lana explicitly repaired away from per-stratum `epsilon_hat_s` and now uses one
global `epsilon_hat`, so the covariance induced by the shared error estimate is real.

For

`a = sum_s w_s * (r_s - epsilon) / (1 - 2epsilon)`,

the correct global-epsilon delta form is:

> `Var(a) = sum_s w_s^2 * Var(r_s)/(1-2epsilon)^2 + [sum_s w_s * (2r_s - 1)/(1-2epsilon)^2]^2 * Var(epsilon) + covariance terms conservatively >= 0`

Equivalently: compute the derivative of the final weighted estimator with respect to the one
global `epsilon_hat`, then square it.

Why this matters numerically: if there are nine roughly balanced strata with similar derivatives,
the diagonal-only epsilon term is too small by about a factor of three in standard deviation. For
example:

- at `a = 0.90`, `epsilon = 0.02`, the correct global-epsilon contribution is about `0.00825`;
  a diagonal-only equal-nine-strata calculation gives about `0.00275`.
- at `a = 0.90`, `epsilon = 0.05`, the correct contribution is about `0.01370`;
  diagonal-only gives about `0.00457`.

Required repair: replace the printed `sigma_a` formula with the global-epsilon derivative formula
above, or state an explicitly conservative implementation that cannot be smaller than it.

## 3. `epsilon_syn` Repair

The conceptual repair is right: 200 synthetics can support one global absolute-error correction
plus stratum diagnostics. They cannot support nine independent precise `epsilon_s` corrections.

After the covariance fix above, this requirement is satisfied.

One wording detail: line 78 still says "per difficulty stratum" in the bullet describing the 200
synthetics. Because the estimator now uses global `epsilon_hat`, this should be softened to
"with per-stratum diagnostics" to avoid reviving the old interpretation. That is editorial if the
formula is repaired, but it is worth fixing while touching the text.

## 4. Naming And Claim Boundary

The naming repair lands. The text now says:

> `a` is the HC-1H one-human, synthetic-error-corrected attenuation estimate

and explicitly denies equivalence to a multi-human truth-reference measurement. The synthetic
realism caveat is carried in §5. This satisfies my sealed-position requirement.

## 5. HC-7 Integrity Triggers

The four HC-7 triggers are the right core set:

1. missing or unreconstructable stratum population counts;
2. broken random-within-stratum sampling;
3. unsealed, prematurely opened, or compromised blinding key;
4. machine or instrument signs visible to the checker.

I would add one fifth trigger:

5. **synthetic/repeat identity exposure:** if the checker can identify which items are synthetic,
   repeated, or mirrored repeats before the key opens, the relevant batch is void and the protocol
   returns hard INCONCLUSIVE unless a predeclared discard/replacement rule applies.

This is not cosmetic. HC-1H relies on blind synthetics and blind mirrored re-presentations to
replace missing humans. If their identity becomes visible, the reference-error and self-consistency
measurements no longer mean what the protocol says they mean.

## 6. Pilot Carry-Forward Bias

The pilot is useful, but its carry-forward rule is not clean as written.

Current rule:

- 150-label pilot: 90 real, 40 synthetics, 20 mirrored re-presentations;
- outcomes only PASS-TO-FULL-HC1H or INCONCLUSIVE;
- pilot passes if protocol executes cleanly, ergonomics acceptable, crude `epsilon_hat < 0.10`, and
  no HC-7 trigger;
- if pilot passes, its labels may be retained and counted toward the full design totals.

The bias is in the synthetics. If the pilot passes partly because the 40 synthetic labels have
`epsilon_hat < 0.10`, then carrying those same 40 synthetics into the final global
`epsilon_hat` conditions the final estimator on a low-error preliminary realization. That biases
`epsilon_hat` downward. A downward-biased `epsilon_hat` biases `a` upward after correction.

Real pilot labels are less dangerous because the pass rule does not depend on the real
machine-human agreement `a`. If real labels are the first random tranche from each stratum and the
stratum weights/inclusion probabilities remain fixed, carrying them forward does not by itself bias
the point estimate. But mixing a feasibility screen with final inference should be avoided unless
the sequential rule is explicitly modeled.

Required repair. Choose one:

- **cleanest:** pilot labels never enter final HC-1H. The pilot only returns PASS-TO-FULL-HC1H or
  INCONCLUSIVE.
- **acceptable:** pilot real labels may carry forward if they are a predeclared random first tranche
  in each stratum, but pilot synthetic and mirrored-repeat labels used in pass/fail criteria do not
  enter final `epsilon_hat` or `epsilon_rr`.
- **harder:** carry all pilot labels forward only with a frozen sequential-inference correction for
  the pilot pass condition.

I recommend the second option if Duho wants to save useful real-label effort without biasing the
error calibration.

## Freeze Blocker Status

Still blocking HC-1H freeze:

1. repair the global-`epsilon` variance formula to include shared-epsilon covariance;
2. repair the pilot carry-forward rule so pass-conditioned synthetic/retest labels do not bias final
   `epsilon_hat`/`epsilon_rr`;
3. add the synthetic/repeat identity exposure HC-7 trigger, or explicitly show why the existing key
   trigger covers it.

After those repairs, I see no remaining conceptual blocker from my HC-1H gate. The 850-label budget
is still defensible as a full one-human attenuation design. It is not justified by pure HC-6 power
math, but it is justified by stratum coverage, one-human error calibration, mirrored-repeat drift
checks, and replacing the old multi-human reference as honestly as the constraint permits.

## Plain Answer For Duho

HC-1H is close, but I would not freeze this exact revision. The corrected `a_gate = 0.7905` is right.
The problem is now the global error-calibration math and the pilot. A pilot that counts its own
pass-filtered synthetic labels into the final error estimate can bias the final attenuation upward.
Fix that, and fix the shared-epsilon covariance in `sigma_a`, before asking Duho to spend the
weekend labelling.

No real images, sky run, publication, freeze, acceptance, commit, or push follows from this gate.
