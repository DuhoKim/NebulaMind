# KUN_HC1H_GATE_20260814

Timestamp: 2026-08-14 KST

Brief: `prereg/_tmp_KUN_HC1H_GATE_BRIEF.md`

Inputs inspected:

- `prereg/LANA_ONE_HUMAN_ATTENUATION_20260814.md` —
  `14336d8c3e3f0286df8a3cabf5f9ea8ab9baeb4c59c5f1c16221a93d86c08308`
- `prereg/KUN_ONE_HUMAN_ADVERSARY_20260814.md` —
  `c7140bb4d8114852e81f753a43ffb34f21b53e83675c75263fedb1af7b14f583`
- `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260814_CANDIDATE.md`
- `prereg/GORU_BS8_POWER_RECEIPT_20260814.md`
- `prereg/LANA_BS9_CONSTANTS_TABLE_20260814.md`

Boundary: documentation/gate only. I did not inspect sky data, rows, positions, images, chirality
labels, or sky statistics. I did not freeze, publish, accept, commit, or push anything. Duho owns
acceptance.

## Verdict

**PASS WITH REQUIRED REPAIRS.**

Lana's HC-1H design satisfies the core adversarial requirements from my sealed position:

- one human is blinded;
- the human samples the accepted population, not only machine disagreements;
- machine committee state is stratifier/allocator/diagnostic only, never inside `a`;
- machine-machine agreement cannot raise `a`;
- synthetic injections and mirrored re-presentations address the self-agreement trap better than a
  retest-only protocol;
- failure remains INCONCLUSIVE-BY-POWER before any run.

But I would not freeze the amendment exactly as written. Two arithmetic/statistical repairs are
blocking:

1. **Her `a_gate = 0.873` is not the BS-8/HC-6 break-even at `N = 130,076`; I recompute
   `a_gate ≈ 0.7905`.** She appears to have introduced an extra square/root in the threshold
   derivation. A stricter floor is allowed only if explicitly labeled as a new conservative human
   quality floor, not as the HC-6 analytical break-even.
2. **`σ_a ≈ 0.012` is optimistic and not valid as a binding expected width unless the assumed
   real-agreement and synthetic-error rates are frozen.** Under plausible values near the proposed
   floors, I recompute `σ_a` closer to `0.017–0.023` before stratification/design effects. The
   protocol must compute `σ_a` from observed stratum counts and observed `ε_syn`, with conservative
   intervals; it must not freeze `0.012` as the expected answer.

These are fixable. I do not reject the one-human path.

## 1. Self-Agreement Trap

Lana closes the main self-agreement trap **for absolute inversion and simple orientation
misunderstanding** by adding 200 blind synthetic ground-truth injections. That is materially better
than mirrored retest alone. A checker who consistently swaps signs should fail the synthetic
ground-truth set even if they are perfectly self-consistent.

Limit: synthetics only cover the failure modes the generator reaches. They do not directly catch a
single human's stable, confident misreadings on real hard cases where the synthetic generator is not
realistic. Lana states that limit honestly in §5. That residual does not block the design, but it
must travel into the preregistration/paper claim boundary.

## 2. Pre-Screen Bias

Her stratified design is statistically valid in principle. A stratified estimator is unbiased for
the population quantity if:

- strata are fixed before unblinding;
- population stratum counts are known;
- sampling is random within each stratum;
- the estimator uses population weights or equivalent inverse-probability weights;
- machine committee state affects only strata/allocation, not the label reference or `a`.

That answers my disagreements-only objection. The dangerous route was "human sees only hard cases
and we take the naive agreement rate." Lana does not do that.

Repair required: the amendment should explicitly say the final estimator uses the realized sample
counts and population weights, and that any missing stratum population count or violated random
sampling key forces INCONCLUSIVE. It says this in prose, but the freeze text should make it a hard
condition.

## 3. Naming: Can This Be Called `a`?

Synthetic ground truth is enough to justify a **noise-corrected one-human attenuation estimate**,
but not enough to pretend that one human has become a three-human truth panel.

I will allow the symbol `a` if the preregistration defines it as:

> `a`: the one-human, synthetic-error-corrected attenuation estimate under HC-1H.

It must not be described as visual truth, consensus truth, or equivalent to the original
two-checker-plus-adjudicator reference. If the paper uses plain `a`, it must carry the HC-1H
definition and the synthetic-realism caveat wherever attenuation is interpreted.

## 4. Recomputed HC-6 Floor

Using the same analytical logic I used in my sealed position and Goru used in BS-8:

- `D = (2a - 1) * 0.0408 / 3`
- `sigma_D = 1 / sqrt(3N)`
- for `p < 0.001` with power `>= 0.95`, require approximately
  `D >= (3.2905 + 1.6449) * sigma_D`

At `N = 130,076`:

- `sigma_D = 0.0016008136762691544`
- required effective amplitude on the `A` scale is `0.023701873126159057`
- therefore `a_gate = (0.023701873126159057 / 0.0408 + 1) / 2 = 0.7904641314480276`

At `N = 100,000`, the same formula gives:

- `a_gate = 0.8312768568857085`

Lana's `a_gate = 0.873` is therefore not the lane's power break-even. If retained, it must be
renamed as an added conservative reference-quality floor, and Duho should be told it is stricter
than the science-power requirement.

I do **not** recommend adding that stricter floor unless there is a separate reason. The prereg
already has safeguards: synthetic error, mirrored retest, per-stratum floor, and INCONCLUSIVE on
incompatible `ε_rr`/`ε_syn`.

## 5. Recomputed `σ_a`

For the correction

`a = (r - ε) / (1 - 2ε)`,

the delta derivatives are:

- `∂a/∂r = 1 / (1 - 2ε)`
- `∂a/∂ε = (2r - 1) / (1 - 2ε)^2`

Using 500 real labels and 200 synthetic labels before any stratification design effect:

| true `a` | `ε` | implied `r` | recomputed `σ_a` |
|---:|---:|---:|---:|
| 0.85 | 0.00 | 0.850 | 0.0160 |
| 0.85 | 0.02 | 0.836 | 0.0187 |
| 0.85 | 0.05 | 0.815 | 0.0227 |
| 0.90 | 0.00 | 0.900 | 0.0134 |
| 0.90 | 0.02 | 0.884 | 0.0170 |
| 0.90 | 0.05 | 0.860 | 0.0220 |
| 0.95 | 0.00 | 0.950 | 0.0097 |
| 0.95 | 0.02 | 0.932 | 0.0150 |
| 0.95 | 0.05 | 0.905 | 0.0212 |

So `σ_a ≈ 0.012` is reachable only in a favorable regime, not as a general expected width. It is not
a safe frozen planning number for a one-human protocol.

Additional issue: Lana says `ε_s` is per stratum from 200 synthetics allocated across 9 strata. If
that is literal, the average synthetic stratum has about 22 labels. Even with zero errors, a
one-sided 95% upper bound on `ε_s` is about `0.127`, not close to the overall `ε <= 0.05` floor.
Per-stratum synthetic correction at that sample size is too noisy unless a shrinkage/pooling rule
is frozen.

Required repair:

- either make `ε_syn` an overall correction with per-stratum synthetic results as diagnostics and
  hard-failure alarms;
- or freeze a specific hierarchical/shrinkage estimator for `ε_s`;
- or increase synthetic labels substantially if literal per-stratum `ε_s` is load-bearing.

Do not leave "per-stratum `ε_s` from 200 synthetics" as if it were precise.

## 6. HC-5 Floor

The old `0.85` floor should not carry over as a simple point estimate. Lana is right to replace it
with a lower-bound condition. The repaired floor should be:

> `a_LB = a - 1.645 * sigma_a >= max(0.85, a_gate(N))`, where `a_gate(N)` is recomputed by the BS-8
> analytical method.

Because `a_gate(130,076) ≈ 0.7905`, the `0.85` quality floor dominates at the current bound. That
matches my sealed position and avoids the false precision of her `0.873` number.

Per-stratum `a_s >= 0.70` can remain as a local hard-failure rule, but its uncertainty should be
reported and the sample-size floor per stratum must be honored. With a 30-real floor, a stratum
point estimate can be noisy; that is acceptable only because the rule is conservative and can force
INCONCLUSIVE rather than rescue a run.

## 7. Is 850 The Right Budget?

**850 is defensible, but not for the reason Lana gives. It is not justified by HC-6 sample-size
math alone.**

My sealed analysis showed that, at `N = 130,076` and point `a ≈ 0.85`, roughly 100 independent
labels can be enough for the purely statistical lower-bound-to-power calculation. That was never
the whole problem. The hard parts are one-human bias, stratified coverage, synthetic absolute-error
calibration, and fatigue/drift checks.

Budget ruling:

- **Not overspending** if the goal is a serious one-human replacement for the original 500-object,
  multi-human attenuation design.
- **Overspending** if the only goal is to decide the HC-6 power inequality under an assumed
  human-reference agreement rate.
- **Misallocated/under-specified** if the 200 synthetic labels are intended to estimate nine
  independent per-stratum `ε_s` values.

I would approve 850 as a weekend budget only with the repairs above:

- 500 real labels for population-weighted `a`;
- 150 mirrored repeats for self-consistency/drift;
- 200 synthetics for overall absolute-error calibration and stratum diagnostics, not precise
  per-stratum corrections unless a shrinkage rule is frozen.

If Duho wants a smaller pilot, a valid reduced design is possible, but it should be labeled a pilot
that can only return PASS-TO-FULL-HC1H or INCONCLUSIVE, not the final attenuation gate.

## Required Repairs Before Freeze

1. Replace `a_gate = 0.873 at N = 130,076` with `a_gate ≈ 0.7905` under the BS-8 analytical method,
   or explicitly relabel `0.873` as an added conservative human-quality floor with independent
   justification.
2. Replace `σ_a ≈ 0.012` as a general expected width with a formula-only rule: compute `σ_a` from
   realized stratum counts, observed raw agreement, observed synthetic error, and design weights.
   The document may include examples, but not a binding optimistic width.
3. Clarify the `ε_syn` estimator: overall correction plus stratum diagnostics, or a frozen
   hierarchical/shrinkage method. Do not imply that 200 synthetics support nine precise independent
   stratum error corrections.
4. Define `a` as the HC-1H one-human, synthetic-error-corrected attenuation estimate and carry the
   synthetic-realism caveat. Do not imply equivalence to the original multi-human truth reference.
5. Make missing stratum population counts, broken random-within-stratum sampling, unsealed keys, or
   visible machine signs hard INCONCLUSIVE triggers.

## Plain Answer

Lana's one-human direction is scientifically usable after repair. It is not
INCONCLUSIVE-BY-DESIGN. Your correlated-failure-mode objection is handled correctly: machines are
not allowed inside `a`.

I would not freeze the current HC-1H text because the power threshold and uncertainty arithmetic are
wrong or over-optimistic. The 850-label budget is defensible as a serious one-human replacement, not
as a minimal power calculation. It is not obviously wasting Duho's weekend, but the text must stop
pretending `σ_a ≈ 0.012` and `a_gate = 0.873` are the governing math.

No real images, sky run, publication, freeze, acceptance, commit, or push follows from this gate.
