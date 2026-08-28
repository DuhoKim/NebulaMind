# The sensitivity-gradient control — design v3, rebuilt on the production estimand

**Status: DESIGN, defined, UNFILLED.** Nothing here has produced a bound.

**v2 was NOT CLEAR from both seats. The blocking finding was that it measured the wrong quantity**
(CODEX-V33-1): recovery was defined on the continuous score `χ`, while production decides on the
**accepted sign** through a confidence threshold with abstention. A quality-dependent amplitude shift
moves objects across that threshold and changes sign accuracy nonlinearly, and subtracting `χ(b)`
does not bridge it. **That defect was in v1 and survived the v2 rewrite unquestioned** — v2 repaired
what the referees named without re-examining what was being measured.

v3 does not invent a statistic. **It reads the production model out of the frozen code.**

---

## 1. Why this is not the antisymmetry receipt — survived two rounds, unchanged

`mirror(·)` is pure index reversal and `χ(x) = (w(x) − w(mirror(x)))/2`, so `χ(mirror(x)) = −χ(x)`
algebraically, for any weights and any raster; `max|χ(mirror(x)) + χ(x)| = 0.0` exactly, 1000/1000
spirals. Therefore `d(g) = χ(g) + χ(Mg) ≡ 0` and stratifying it returns 0.0 in every bin, forever.
CODEX verified this against the extant implementation (`chi_tensor` uses `torch.flip`; the
interpolating mirror that would break the identity is not reachable in the inspected path).
**This corrects `MIRROR_TEST_DESIGN_20260828.md` Q2.**

## 2. The production estimand, read from `successor_ref_v9.py`

`inject_signs()` at v9:1199 defines the model this study actually estimates:

    lat = +1  with probability (1 + A_LONGO · c) / 2,  else −1        # c is cos θ
    s   = −lat with probability (1 − a_b),             else lat        # a_b is per-bin ACCURACY

so, per object in calibration bin `b`,

    E[s] = (2·a_b − 1) · E[lat]

**The production gain is `g_b ≡ 2·a_b − 1`, the sign-accuracy attenuation factor.** It is not a
response of `χ`. This is why v2's statistic could not be converted by any kernel: `K` projects a
valid response slope, but a score-amplitude response is not an accepted-sign response.

**And the design already measures `g` positionally.** `calibration_bins()` at v9:1359 puts the two
interior boundaries at the **count-weighted tertiles of `c`** — *the calibration bins are bins in
`cos θ` along the tested axis.* `accuracy_from_handcheck()` at v9:1446 already returns `a_b` per bin
**with a full covariance matrix**, including the off-diagonal terms induced by the shared `epsilon`.
Its own docstring carries `(2·a_b − 1)`.

**The machinery to bound the sensitivity gradient is therefore already frozen in v9 and already
required by BS-8f/BS-5f.** It needs no new images.

## 3. The statistic

With `ĝ_b = 2·â_b − 1` over the three `cos θ` tertiles, `c̄_b` the mean `cos θ` in bin `b`, and
`Cov(ĝ) = 4·Cov(â)` from BS-8f, fit the **uncentred** model by GLS:

    ĝ_b = θ₀ + θ₁·c̄_b            so  θ₀ = g₀  and  θ₁ = g₀·γ  by construction
    γ̂  = θ₁ / θ₀                 — slope over INTERCEPT, both from the same fit
    σ_γ = √( J·Cov(θ)·Jᵀ ),      J = [ −θ₁/θ₀² , 1/θ₀ ]

**`γ̂` is normalised by the fitted intercept, never by a sample mean.** v3 divided the slope by the
count-weighted mean `ĝ_bar`, which is `g₀(1 + γ·mean(c))`, so the statistic it actually defined was
`γ/(1 + γ·mean(c))` — not `γ`. On the frozen retained geometry (`mean(c) = −0.158387518`) a true
`γ = +0.2` read as `+0.2065` and `γ = +0.5` as `+0.5430`. Both seats found this
(GPT56-GAINV3-1, CODEX-GAINV3-1); it was the same class of error as the v2 blocker, one layer in.

**This also dissolves CODEX's `n_b` ambiguity rather than pinning a fourth convention.** `n_b` was
undefined between the population tertile count, the hand-check allocation (which is deliberately
*not* population-proportional, v9:1378–1443), and the GLS's own implied pivot. **The intercept
normalisation removes `n_b` from the statistic entirely.**

**GLS, not OLS, because `Cov(â)` is not diagonal** — `epsilon` is one shared quantity and its
derivative enters every bin (v9:1446). Treating the bins as independent would understate `σ_γ`.

### The contract is `ref/gain_gradient_estimator.py`, not this paragraph

Both seats found the GLS and delta-method "named, not written down", with no singular-covariance
rule. **They are now code.** `estimate_gamma(a_hat, cov_a, c_bar)` returns a result or a refusal set,
never a partial answer, and pins every choice: the design matrix including the intercept, a Cholesky
solve rather than an explicit inverse, eigenvalue-based rank and conditioning checks *before* any
inverse, the delta-method Jacobian written out, and the exact receipt fields.

| code | refusal |
|---|---|
| `G01` | an input is not finite |
| `G02` | the covariance is not symmetric |
| `G03` | the covariance is rank-deficient — **no generalised inverse is substituted**, because choosing one would itself be an unpinned freedom |
| `G04` | the covariance is worse-conditioned than the frozen ceiling `1e12` |
| `G05` | the design matrix is rank-deficient; the bin centres do not span a slope |
| `G06` | the intercept is within `3σ` of zero, so `slope/intercept` is undefined |
| `G07` | a bin accuracy is outside v9's `(0.5, 1.0]` domain |
| `G08` | **declared unreachable** and exempted from coverage *by name* — after G01/G03/G05/G06 the result cannot be non-finite. Not counted as covered. |

`--self-test` recovers `γ` exactly on noiseless fixtures at `γ ∈ {0, ±0.2, ±0.5}`, fires every
reachable refusal with an exact code set, computes coverage from the controls that ran, and **carries
a regression control asserting the old sample-mean normalisation gives a different, predicted
number** — so the defect cannot return silently.

**And `verify_mu_gamma.py` now builds `γ̂` through this recipe end-to-end**, binning simulated data
with v9's own `calibration_bins()` and calling the same estimator. GPT56 observed that the earlier
verifier "does not construct `γ̂` by §3's three-bin recipe" — a guard that could not fail for this
defect. It can now.

### The bias, derived and then verified by simulation

With `E[lat|c] = μ + A·c` and `g(c) = ḡ(1 + γc)`, expanding `Cov(s,c)/Var(c)` exactly gives

    recovered = A + γ·(μ + A·κ),      κ ≡ Cov(c², c) / Var(c)

so the spurious contribution is

    A_spurious = |γ̂| · |μ + A·κ|

**`κ` is a skewness term of the realised `cos θ` distribution, not a free parameter.** Computed on
the 49,211 retained objects with the frozen axis: **`κ = +0.005104`**, so `A·κ = +0.000208` — an
effective monopole that exists *even when `μ = 0`*. It is small, but it is exact and it is now
stated rather than dropped.

**What the simulation does and does not establish, stated precisely.**
`gates/verify_mu_gamma.py` simulates v9's own production model on the real `cos θ` distribution and
recovers the predicted amplitude across ten `(μ, γ, ḡ)` combinations including negative `μ` and
negative `γ`. **It confirms the `γ·μ` structure — sign, magnitude and the absence of bias at
`γ = 0` — but it does NOT discriminate the `A·κ` term**, which at `0.000208` sits far below the
simulation's standard error of `≈0.001`. The naive form passes every case too.

**So `A·κ` is derived algebraically and is stated as derived, not as verified.** Resolving it by
simulation would need roughly a hundredfold increase in replicates, which has not been run. Anyone
relying on the `A·κ` term should check the expansion in this section rather than the script.

*(An earlier draft of this section claimed the script had falsified the naive form. It had not — the
first run failed because it exceeded v9's accuracy domain, and `κ` was found by doing the expansion
while investigating that failure. The claim is withdrawn.)*

**A domain constraint came out of the same check and belongs in the contract.** v9 requires accuracy
in `(0.5, 1.0]` (`inject_signs`, v9:1207). Since `a = (1 + ḡ(1+γc))/2` and `c ∈ [−1, 1]`, this bounds
the physically representable gradient at `|γ| ≤ 1/ḡ − 1`. The verification script **refuses**
out-of-domain parameters rather than clamping them; clamping silently is what made its first run
report a false mismatch.

**Everything in this statistic is already produced by the frozen pipeline.** No injection campaign,
no cutout, no fetch.

## 4. The decision rule — exact, not sampled

v2 evaluated the verdict at `δ ∈ {−Γ, +Γ}` and called equal endpoints invariance. **Both seats were
right that this is not an invariance test**; a decision function can differ in the interior.

The repair does not need sampling. The verdict is a function of `Â` compared against a finite set of
**preregistered decision thresholds** `T` (detection floor, amplitude band edges, rejection upper
limit, sign boundary). A piecewise-constant function is invariant on an interval **iff no breakpoint
lies inside it**. So:

    Γ = |μ_ceiling| · (|γ̂| + 1.96·σ_γ)
    if any t ∈ T satisfies  Â − Γ  ≤  t  ≤  Â + Γ :
        emit INCONCLUSIVE-BY-SENSITIVITY-GRADIENT

This is exact, closed-form, and executable. No retry, no rebinning, no recalibration. Terminated
branch under §6.3 clause 10. **`T` must be enumerated in the receipt**, and the check is vacuous
unless `T` is complete — so the receipt records `T` and its digest, and a control asserts the rule
fires when a threshold is placed inside the interval.

## 5. `μ`, and why `max()` is doing the work

    μ_ceiling = max(0.10, |μ_obs|)

`μ_obs` is the mean **accepted sign** over exactly the accepted population the estimator uses — same
rows, same acceptance, same phase — produced automatically and receipted **before any result is
displayed to any operator**.

**`0.10` is an assumed pre-unblinding working ceiling, not a derived or generous one.** Both cited
comparisons reproduce (`0.070624` from Land's superclean counts; `0.094962 ± 0.024` from this lane's
GZ1 paired-flip record) but `0.10` exceeds the latter by only 5.3%, its ~95% upper value is `0.142`,
and both are human-label GZ1 statistics that do not bound this instrument's output monopole. **The
`max(...)` is what makes the rule safe; the constant is not.**

## 6. What injections would add, and what they would not

The statistic above is first-order and has **three** positional points. A synthetic-injection
campaign on **non-sample** cutouts remains useful as an *independent* estimate at finer positional
resolution and beyond first order — but it is **secondary**, and it must be defined at the same
estimand boundary or it repeats v2's error:

- each injection cell is a frozen population passed through the **complete production instrument and
  acceptance path**, not through `χ`;
- both handedness signs are injected into the **same** background at the same amplitude;
- the recovered quantity is the **balanced accuracy** `ĝ = p⁺ + p⁻ − 1`, where `p^±` is the fraction
  of *accepted* outputs whose sign matches the injected sign. Balanced accuracy is what cancels an
  additive sign bias from the background — **and unlike v2's `χ(b⊕i) − χ(b)`, it is a cancellation
  in the same quantity the estimator consumes.** v2's claim that subtraction cancels background
  chirality was too strong for a nonlinear instrument (both seats); this is the narrower true one;
- abstention rate is reported per cell. Quality-dependent abstention changes the effective weighting
  along `cos θ`, so it changes **leverage**, not bias — and if it varies, `Var(cos θ)` and hence
  `N_eq` must be recomputed on the realised accepted set;
- gain is evaluated **at the tested amplitude** `A_LONGO`, because accuracy near a confidence
  threshold is amplitude-dependent.

**This section is DESIGN and its sampling contract is deliberately not frozen here.** v2 claimed a
contract was "frozen in full" and both seats found deferred answer-determining choices. Rather than
repeat that, this document states plainly: **the injection campaign is not freezeable yet**, and the
primary statistic in §3 does not depend on it.

## 7. Blindness

For §3: the inputs are hand-check labels and catalogue geometry already required by BS-8p/BS-8f. No
new image, no fetch, and `γ̂` is a property of accuracy versus position, not of any per-object `χ`
sign. It is computed pre-unblinding from the calibration that the design already performs.

For §6: **no study-parent image and no study `χ` enters**; the injected handedness is known; the
kernel is catalogue-only. **The v2 claim that "the real sky is simply absent" is withdrawn and not
reinstated** — real DR10 backgrounds are real sky.

## 8. What remains open

- `γ̂` is unmeasured. **DESIGN, defined, UNFILLED.** Nothing may be filled against this.
- Three positional points support a slope and no curvature. Non-linear positional structure in `a`
  is unbounded by §3.
- Routes (a) upstream chirality and (c) non-equivariant selection remain unbounded.
- **This does not close conditional independence.** It bounds one first-order route.
- The §6 injection campaign is not freezeable and is not required by §3.
- `SLOT_SCHEMA` is frozen; where this receipt lives is a **gate matter, not an edit**.

## 9. What changed from v2, by finding

| finding | v3 |
|---|---|
| CODEX-V33-1 estimand | statistic is now `2a−1`, read from `inject_signs()`; measured per `cos θ` tertile by machinery already in v9 |
| both, endpoint ≠ invariance | exact threshold-in-interval test; no sampling |
| both, contract not frozen | primary statistic needs no sampling contract; the injection campaign is declared **not freezeable** rather than claimed frozen |
| both, subtraction overclaim | withdrawn; replaced by balanced accuracy, which cancels in the estimator's own quantity |
| GPT56-V32-3 vector kernel | retained and still correct, but **no longer load-bearing for §3** — the gradient is now measured directly in `cos θ` rather than propagated from quality |
