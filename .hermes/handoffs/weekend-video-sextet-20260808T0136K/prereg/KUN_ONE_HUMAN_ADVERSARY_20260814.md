# KUN_ONE_HUMAN_ADVERSARY_20260814

Timestamp: 2026-08-14 KST

Brief: `prereg/_tmp_KUN_ONE_HUMAN_ADVERSARY_BRIEF.md`

Boundary: documentation/design gate only. I did not inspect sky data, rows, positions, images,
chirality labels, or sky statistics. I did not freeze, publish, accept, commit, or push anything.

## Sealed Independent Position Before Reading Lana

Status of this section: **written before reading `LANA_ONE_HUMAN_ATTENUATION_20260814.md`.**

### Verdict Before Comparison

**One human can support a limited machine-vs-human attenuation audit, but cannot by itself supply a
truth-grounded attenuation measurement equivalent to the original two-checker-plus-adjudicator
HC-1..HC-5.**

The valid one-human construction is narrower:

1. keep the human blind to machine sign, mirror status, axis, and outcome;
2. sample from the accepted population, not only machine disagreements;
3. estimate machine agreement with that one human under a frozen stratified design;
4. publish it as `a_human_reference`, not as ground-truth `a`, unless an external calibration term
   for human error is also frozen;
5. force **INCONCLUSIVE-BY-DESIGN** if the lower confidence bound on the usable attenuation is too
   weak for HC-6.

If the preregistration continues to call the one-human estimate simply `a`, it overclaims. It must
either define `a` as human-reference attenuation, with limitations carried into the claim boundary,
or add an external ground-truth calibration source.

### 1. Where One Human Stops Being Enough, Quantitatively

HC-6 power is controlled by the lower usable attenuation, not the point estimate. Using the lane's
normal-approximation logic:

- signal on the dipole scale: `D = (2a - 1) * 0.0408 / 3`;
- null standard deviation: `sigma_D = 1 / sqrt(3N)`;
- approximate one-sided `p < 0.001` critical value: `3.2905 * sigma_D`;
- for power `>= 0.95`, require mean signal at least `(3.2905 + 1.6449) * sigma_D`.

This implies:

- at `N_accepted = 100,000`, `a_min ≈ 0.8313`;
- at the current bound `N_accepted = 130,076`, `a_min ≈ 0.7905`.

Therefore, if one-human sampling is treated as a binomial reference estimate with point `ahat`,
the lower confidence bound must exceed those values.

Approximate one-sided 95% sample-size requirement near the original floor:

- at `N_accepted = 100,000`, if `ahat = 0.85`, the margin is only `0.0187`, requiring about
  **956** independently sampled human-reference labels for the lower bound to clear `a_min`.
  A 500-object audit is not enough if the observed rate lands near 0.85.
- at `N_accepted = 130,076`, if `ahat = 0.85`, the margin to `a_min` is about `0.0595`, requiring
  about **98** labels for the same purely statistical lower-bound calculation.

That second number is not a reason to use only 98 labels. It only says HC-6 power is not the
binding constraint once `N_accepted` is 130,076. The binding constraints become human-reference
bias, stratum coverage, and pre-screen sampling bias.

My quantitative rule:

> One human stops being enough whenever the lower confidence bound of the frozen human-reference
> attenuation, after stratification and any human-error penalty, is below `a_min(N_accepted)`:
> `0.8313` at `100,000`, `0.7905` at `130,076`, or the formula above at the final accepted count.

### 2. HC-5's 0.85 Floor

**The old `a >= 0.85` floor is not automatically transferable.**

It was tolerable when the reference label was a two-checker-plus-adjudicator construction. With one
human, the floor mixes two quantities:

- machine agreement with the checker;
- the checker's own systematic correctness.

If no external human-error calibration exists, `0.85` is too weak as a truth-accuracy floor. It may
remain a minimum **human-reference agreement** floor, but then the claim must say so and the power
calculation must either:

- use a conservative lower bound on true `a` after subtracting a frozen human-error allowance; or
- declare the result as relative to the one-human reference only, not to visual truth.

I would set the replacement HC-5 as:

- `a_human_reference_LB >= max(0.85, a_min(N_accepted))`;
- no primary stratum below a frozen floor, but the stratum floor should be a warning/INCONCLUSIVE
  trigger unless its sample size is adequate;
- if no external calibration of the single human's sign error exists, the study may not describe
  this as ground-truth attenuation.

### 3. Self-Agreement Trap

Test-retest self-agreement is useful for fatigue and interface instability. It does **not** detect
consistent wrongness.

A checker who always swaps clockwise and counter-clockwise would score perfect self-agreement and
destroy `a` if used as truth. Randomized mirror repeats catch one important subset: if the same
object and its mirror are both shown, the human's label should flip. But even that catches
anti-equivariance, not absolute orientation. A consistently inverted convention can still pass
mirror-pair self-consistency.

What detects it:

- synthetic orientation anchors with known signs shown before and after the session;
- duplicated mirror pairs with required flip behavior;
- forced "uncertain/abstain" option so low-confidence cases do not become false certainty;
- comparison to a deterministic geometry estimator only as an alarm, not as a truth reference;
- external literature/human calibration if available.

Self-consistency alone cannot certify `a`.

### 4. Pre-Screen Bias

If machines label everything and the human sees only disagreements, the sample is not
representative. The naive agreement rate is invalid because it estimates error conditional on
machine disagreement or low confidence, not over accepted galaxies.

This route is salvageable only with a frozen sampling design:

- draw a probability sample from the full accepted population strata;
- optionally oversample disagreements, low-confidence cases, and covariate tails;
- record each sampled unit's known inclusion probability;
- estimate `a` by Horvitz-Thompson / inverse-probability weighting or an equivalent frozen
  stratified estimator;
- compute a conservative lower bound with design effects included;
- if any inclusion probability or stratum count is not known before unblinding, INCONCLUSIVE.

A disagreements-only audit is unsalvageable for `a`. It can be a diagnostic, not the attenuation
measurement.

### 5. Machine Reference And Correlated Failure Modes

A machine reference can contribute only as a **negative control, triage aid, or bound**, not as an
independent truth source for `a`, unless its error model is externally calibrated and frozen before
use.

The correlated-failure-modes argument is basically right. Two ML vision systems trained on similar
synthetic families, seeing the same rendered/cutout artifacts, or sharing preprocessing can agree
for the same wrong reason. That inflates apparent `a` and can silently disable HC-5. Equivariance
does not fix this: two equivariant systems can both flip correctly under mirroring and both fail on
the same ambiguous morphology class or preprocessing artifact.

The only safe machine contribution to `a` without external calibration is a one-sided bound:

- machine-machine disagreement is evidence that at least one system is unstable on those cases;
- machine-machine agreement is **not** evidence that both are correct;
- therefore a second machine can identify regions requiring human review or force
  INCONCLUSIVE/abstention, but it cannot raise `a` above the one-human lower bound.

If a protocol averages human and machine references or treats machine-machine agreement as
additional "votes" for truth, I would block it.

### 6. Honest Floor

One human is enough for a valid **limited** attenuation protocol if all of the following are true:

1. the sample is probability-based over the accepted population, with any oversampling reweighted;
2. the human is blind and has an abstain option;
3. synthetic absolute-sign anchors and mirrored repeat pairs are passed;
4. the output is named `a_human_reference` unless an external calibration supplies a human-error
   correction;
5. the lower confidence bound after all penalties exceeds `a_min(N_accepted)`;
6. machine references cannot increase `a`, only flag failures or shrink the accepted set.

If any of those are absent, the honest verdict is **INCONCLUSIVE-BY-DESIGN**, not a weakened HC-5.

## Comparison To Lana

**BLOCKED: Lana's parallel design is not present at the path named in the brief, and I found no
same-named file anywhere under this handoff tree.**

Commands run after sealing the independent section:

- `sed -n '1,280p' prereg/LANA_ONE_HUMAN_ATTENUATION_20260814.md`
  - failed: no such file
- `find . -name 'LANA_ONE_HUMAN_ATTENUATION_20260814.md' -print`
  - returned no matches
- `rg --files | rg -i 'lana.*(one|human|attenuation)|one.*human|attenuation.*20260814'`
  - returned only this Kun report

I therefore cannot compare to Lana's design yet. This is not a substantive gate on Lana; it is a
custody/path blocker. The independent position above remains sealed before any Lana read at SHA-256
`c9a11eb17b589e22458d99c1a36c0778241835a5d6e32704c8fa037cfa188673`.

## Direct Answer On The Correlated-Failure-Modes Argument

Your correlated-failure-modes argument is **not wrong**. It is the central reason a machine
reference cannot be allowed to increase `a` without an external error calibration.

The adversarial point is precise:

- two ML systems can share synthetic priors, preprocessing artifacts, deblending failures,
  inclination failure modes, arm-contrast failures, or mirror-equivariant but wrong morphology
  decisions;
- if they agree for the same wrong reason, machine-machine agreement inflates apparent attenuation;
- that inflation can silently disable HC-5 by making a weak instrument look safe;
- mirror anti-equivariance does not solve this, because two wrong systems can still flip correctly
  under mirroring.

The limited valid use of a machine reference is asymmetric:

- disagreement can lower confidence, trigger human review, shrink the accepted set, or force
  INCONCLUSIVE;
- agreement cannot raise `a` above the one-human or externally calibrated lower bound.

If Lana's missing design lets machine agreement contribute positive evidence to `a`, I would block
that. If it uses machines only for triage, negative controls, and conservative down-bounding, that
part is compatible with my position.

## Current Gate Status

**INDEPENDENT POSITION FILED; LANA COMPARISON BLOCKED BY MISSING ARTIFACT.**

Nothing here authorizes real images, a sky run, publication, freeze, acceptance, commit, or push.
