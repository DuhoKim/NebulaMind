CLASS_REFUTED

# AGATE — Program (A) step 2, PHYSICS/THEORY lens

**Bottom line.** Step 1's machinery is correct and I am not attacking it. I am attacking the class and
the decision rule bolted to it. Three independent findings, any one of which is fatal as written:

1. **The class contains models that are not causal-cutoff models at all**, and the minimiser lands on
   one of them. `S_min` is therefore a function of the unpinned knob `k_norm`, not of the physics.
   The refutation branch **cannot fire** and the accommodation branch fires **trivially**: the
   pre-registered fork has only one reachable outcome. A rule whose outcome is fixed before the run
   is not pre-registration.
2. **The decision rule confuses the statistic-at-the-mean-spectrum with the realised statistic.**
   Applied to ΛCDM itself the rule returns "ΛCDM refuted." I ran it; the counterexample is below.
3. **Constraint (i) — Reading A, `P(k)=0` for `k<k_§` — is the opposite of a causality condition.**
   A spectrum vanishing on an IR interval is hyperuniform / long-range-ordered: it requires exact
   cancellation of density fluctuations across unboundedly separated regions. Causal decoupling
   gives *more* IR power than this, not zero.

Everything below is reproducible; the arithmetic was run, not asserted. Numbers marked **[toy]** come
from a Sachs–Wolfe-only kernel calibrated to reproduce the charter's own ΛCDM value
(`S[C̄]=32,486 μK⁴` vs the charter's 34,926 — 7% agreement), and land at the bottom of the prior blind
seats' 6,230–22,327 μK⁴ spread, so it is trustworthy to a factor ~2. The **structural** arguments do
not depend on the toy at all.

---

## THE LEMMA (this alone refutes the class; no numerics required)

The class is: `P=0` for `k<k_§`; `P≥0` free on `[k_§, k_norm]`; `P=P_ΛCDM` for `k>k_norm`.

`P≥0` **permits `P=0`**. So the class contains

> `P(k) = 0` for `k < k_norm`,  `P(k) = P_ΛCDM(k)` for `k ≥ k_norm`

— i.e. **a causal cutoff placed at `k_norm` instead of at `k_§`**. Hence for every admissible choice

> **`S_min ≤ S_1/2[ cut at k_norm ]`**, and `S_1/2[cut at k_c] → 0` monotonically as `k_c` grows.

`k_norm` is not fixed by the theory. It is set by "where high-ℓ is measured" — a data-convenience
choice. **Therefore `S_min` is a property of `k_norm`, not of the causal model.** Measured **[toy]**:

| `k_norm/k_§` | `S_min`, `P≥0` free | `S_min`, with `P ≤ P_ΛCDM` |
|---|---|---|
| 1.5 | 198 | 198 |
| 2 | 51 | 55 |
| 3 | 21 | 30 |
| 5 | 5.6 | 6.1 |
| 10 | **4.0** | **4.1** |
| 30 | 0.03 | 0.05 |

Target is 1150 μK⁴. `k_norm ≈ 10 k_§` (≈ ℓ≳30, the honest "high-ℓ is measured" choice) gives
`S_min ≈ 4 μK⁴` — **~300× below the target.** The accommodation branch fires by three orders of
magnitude, and `S_min > 1150` is unreachable for any `k_norm ≳ 2k_§`.

Note the second column: I tried the obvious repair (bound the class above by `P ≤ P_ΛCDM`) and it
**does not work** — 4.09 vs 4.00. The minimiser wins by *removing* band power, not adding it. An
upper envelope cannot stop that. What is needed is a **lower** envelope, and a lower envelope is
precisely what the theory has already been proven not to supply. **The freedom that kills the program
is downward freedom, and it is structurally identical to the freedom the program exists to measure.**
The optimisation is therefore circular in the one way that matters: it measures its own premise.

By contrast the one number the physics actually fixes — the pure Reading-A cut, `P=P_ΛCDM` above
`k_§`, nothing reshaped — is **`k_norm`-independent**: `6,713 μK⁴` **[toy]**, consistent with the
prior seats. *That* is the model's prediction. The optimisation destroys it.

---

## 1. THE CLASS — which error does it make?

**TOO WIDE. Decisively, and in a way that makes the no-go the trivial one.** It is simultaneously too
narrow in two places, but the width is what determines publishability.

**Why too wide** — beyond the Lemma:

- **(W1) The free band is a cone of measures, not of spectra.** `dim(p) → ∞` on a continuum band;
  `C` has ~ℓ_max components. The map `p ↦ C` is compact with an enormous kernel intersected with the
  cone, so the argmin is a **high-dimensional face, not a point**. The charter's "unique global
  optimum" is **false**: the *value* `S_min` is unique, the *spectrum* achieving it is not. I confirmed
  the minimiser is supported on **12 of 300 k-bins** — a near-delta comb, not a primordial spectrum.
  This breaks step 6 too: there is no "the completion" whose held-out EE/ISW predictions you can test.
- **(W2) No mechanism/regularity condition.** Nothing in the class requires `P` to be producible by any
  physical process. Extreme points of `{p≥0}` are Dirac deltas in `k`. A delta comb is falsified on
  sight by the matter power spectrum, by the ringing it imprints on `C(θ)` at `θ<60°` (which is
  *observed* and *fits ΛCDM*), and by low-ℓ EE.
- **(W3) `k_norm` is not pre-registered.** It alone sets the answer (table above). Live
  researcher-degrees-of-freedom leak inside a program whose selling point is pre-registration.
- **(W4) `S_max = +∞`.** `p` is unbounded above, so the feasible set is an unbounded polyhedral cone
  and its extreme rays give `S → ∞`. **The advertised deliverable `[S_min, S_max]` does not exist.**
- **(W5) The observer-position freedom is uncounted.** The source says a different observer "sees a
  different patch." That is an *additional* free parameter which the class neither constrains nor
  even represents — it widens the model further and makes both branches weaker.

**Where it is too narrow** (this is not a rescue — it is a second, independent error):

- **(N1) Statistical homogeneity and isotropy are assumed, and the model denies them.** A finite causal
  patch with the observer at a generic (non-central) position does **not** give a diagonal covariance:
  `⟨a_ℓm a*_ℓ'm'⟩ ≠ C_ℓ δ_ℓℓ' δ_mm'`. Boundary/patch constructions generically produce ℓ↔ℓ±1, ℓ±2
  coupling. The whole `P(k) → C_ℓ → S_1/2` chain presupposes the stationarity a causal boundary breaks.
  **This is not repairable by adding a row to the constraint table** — it changes the object being
  optimised. Optimising over `P` alone tests an *isotropised surrogate* of Gaztañaga's model, and that
  substitution must be declared, not silently made.
- **(N2) The transfer function is held at ΛCDM.** But Λ is *derived* in this model (Eq. 17), and `χ_§`
  follows from Λ. Fork: either the background is exactly ΛCDM — in which case Eq. 17 is a consistency
  relation / postdiction of a measured Λ, not a prediction — or it is not, in which case CAMB's ΛCDM
  transfer functions, distance to LSS, and ISW growth are all inapplicable. The class assumes the first
  while the program's motivation assumes the second.

**Is (iii) non-circular?** Not fully, on three counts of decreasing severity:
- **The Lemma.** (iii) is what creates the free band, and the free band is what makes the answer
  knob-controlled. This is the severe one.
- **`P_ΛCDM` is not low-ℓ-free.** Planck's `A_s` is fit with the low-ℓ EE likelihood, which is what
  breaks the `A_s e^{-2τ}` degeneracy. Genuinely holding out low-ℓ means refitting to ℓ>ℓ_min only,
  after which `τ` degrades and `A_s` with it. `S_1/2 ∝ A_s²`, so a 4% amplitude error is 8% in `S`.
  Not decisive; must be in the error budget rather than assumed zero.
- The target 1150 must not also be allowed to select `ℓ_max`, the mask, the reading, or `k_norm`.
  At present `k_norm` and the reading are both unpinned, so it can.

**What is NOT missing, said plainly so the list isn't padded:** a Hadamard/adiabatic UV condition is
**not** needed. (iii) already fixes `P` above `k_norm`; the class is free only on a compact interval,
so there is no UV freedom to regulate. And `P≥0` (Bochner) is complete for a Gaussian field — no
further positivity condition exists. The real gaps are W1–W5 and N1–N2.

---

## 2. THE OBSERVABLE — four problems, two of them decision-relevant

**(a) The rule compares an ensemble-level quantity to a single-realisation measurement. Fatal.**
`S_1/2` is quadratic in `C`, so for a full-sky estimator

> `⟨Ŝ⟩ = S[C̄] + Σ_ℓ 2 M_ℓℓ C_ℓ²/(2ℓ+1)`

and the second term is **not small**: **84% of the first** **[toy]** — `S[C̄]=32,486`, CV term
`27,353`, `⟨Ŝ⟩ = 59,839 μK⁴`. So "ΛCDM gives ~34,900" is `S` at the mean spectrum; it is neither the
mean nor the median of the statistic the data delivers. Worse, the distribution is a PSD quadratic
form in Gaussians — strongly right-skewed. Monte Carlo, 2×10⁵ realisations **[toy]**:

| quantile | 0.01% | 0.1% | 1% | 5% | 50% | mean |
|---|---|---|---|---|---|---|
| `Ŝ` (μK⁴) | 621 | 1,236 | 2,680 | 5,554 | 33,976 | 59,612 |

`P(Ŝ ≤ 1150) = 0.08%`, `P(Ŝ ≤ 8000) = 9.6%` — reassuringly close to the published cut-sky ~0.03–0.1%
and full-sky ~5%. **So ΛCDM DOES produce the observed value, at the ~10⁻³ level.** Now apply the
pre-registered rule to ΛCDM: its class is a single point, `S_min = 34,900 > 1150`, therefore
"**the model cannot produce the observed deficit at all**" and ΛCDM is "refuted." It is not. The
inference `mean > observed ⟹ cannot produce` is simply invalid, and it is the load-bearing inference
of the refutation branch.

**(b) Full-sky theory vs cut-sky data. Decision-relevant.** `S_1/2 ≈ 1150 μK⁴` is the *masked* value;
the full-sky ILC/SMICA value is several times larger (~8,000 μK⁴, p ≈ 5%). `C^T M C` is a full-sky
quantity. Comparing them mixes estimators by a factor of several *and* silently selects the more
anomalous of the two — the a-posteriori choice the referee is already primed for. The same estimator
(mask, pixel-space `Ĉ(θ)`) must be applied to theory via simulated maps.

**(c) Can the minimiser cheat SW against ISW? Yes — and it is worse than the question implies.**
`C_ℓ = ∫ dlnk Δ_ℓ(k)² Δ²_R(k)` with the SW/ISW/Doppler sum squared *inside* at fixed `k`, so the
kernel is `≥0` and `C_ℓ` is a positive linear functional of `P` — the minimiser cannot make any `C_ℓ`
negative. It does not need to. It exploits (i) the *existing* SW–ISW cancellation structure, piling
power where `Δ_ℓ(k)²` is smallest for the ℓ's `M` weights most, and (ii) the sign structure of `M`'s
off-diagonals. Empirically it barely bothers: it wins overwhelmingly by *deleting* band power (the
Lemma). Separately, there is a physics inconsistency: if the causal cut is real it should also cut the
**late-time** ISW source, which the class does not do — it cuts primordial `P` while keeping ΛCDM's
ISW growth.

**(d) Lensing breaks the linearity claim.** `C^lensed` is a convolution of `C^unlensed` with `C_L^φφ`,
and `C^φφ` is itself linear in `P` — so `C^lensed` is **quadratic** in `P` and `S_1/2` is **quartic**,
hence **not convex**. The magnitude at ℓ<20 is ≪1%, so this is a bookkeeping fix, not a physics
problem — but the charter's headline ("linear ⟹ convex ⟹ unique global optimum ⟹ certifiable, not
argued") is **false as stated** if lensed spectra enter. Use unlensed `C_ℓ`, or a fixed lensing kernel,
and bound the residual.

**(e) Is `S_1/2` the right adjudicator?** It cuts both ways and the program cannot escape it. The
a-posteriori criticism (Efstathiou; Efstathiou, Ma & Hanson; Bennett et al.) is standard: the 1/2, the
use of `C(θ)` over `C_ℓ`, the estimator and the mask were all chosen post hoc, and the significance
shrinks under reasonable variation. **If the program refutes on `S_1/2`, the defender says "you chose
the statistic that maximises the anomaly." If it accommodates, the sceptic says "you fitted a statistic
that was never significant."** Also note `S_1/2 = ∫_{-1}^{1/2} C(θ)² dcosθ` is a lossy scalar summary,
whereas the source's actual claim is about the *shape* of `C(θ)` beyond 60°. A likelihood on low-ℓ
`C_ℓ` (or on `C(θ)` itself) is the faithful observable; `S_1/2` should be one member of a
pre-registered family, with the caveat printed.

*(Aside, on step 1's machinery: `M` is a Gram matrix of Legendre polynomials on `[-1,1/2]`, so
strictly PD in exact arithmetic — but numerically `cond(M) ≈ 2.4×10³` at ℓ_max=10 and `≈3×10¹⁵` with
**24 numerically-null directions** at ℓ_max=100. `S_min`'s value is safe; a raw NNLS on a
rank-deficient `AᵀMA` returns a solver-dependent spectrum. Regularise, or report the face.)*

---

## 3. THE PHYSICS OF A CAUSAL CUT — Reading A is anti-causal, and the cut is mis-posed

**A hard IR cut is not a causality condition; it is a long-range-order condition.** `P(k)→0` as `k→0`
is the definition of a **hyperuniform / superhomogeneous** field (lattices, one-component plasmas). It
suppresses the variance of arbitrarily large volume averages to zero, which requires density
fluctuations in causally disconnected regions to cancel **exactly**. That is a global conspiracy — the
*maximum* possible long-range correlation, not its absence. Reading A imposes more super-horizon
structure than ΛCDM does, in the name of forbidding it.

**The causal condition, done correctly, is Reading B — and it forbids Reading A.** "If there is no
cause there should not be any effect" is a statement about *correlations*: `ξ(r)=0` for `r>χ_§`. By
Paley–Wiener, compact support in `r` forces `P` entire in `k`, so `P` cannot vanish on any interval —
exactly what the lane's own script measured (P largest at smallest `k`, 729–1217× the reference). The
standard cosmological result is sharper: compactly-correlated fields have `P(k→0) = ∫ξ d³r = const`
(causal white noise), or `∝k⁴` if the causal mechanism conserves energy-momentum (Traschen integral
constraints; the classic causal-seed/defect result). **Causality gives steep-but-analytic suppression,
never a hard zero.** Consequences:

- **Reading A is strictly the model-favourable reading.** It suppresses low-ℓ harder than Reading B
  does. If even A cannot reach the target, a refutation is *a fortiori* robust; if A can and B cannot,
  the ambiguity is decision-relevant and must be resolved before any claim. Running only A and claiming
  a positive result is the worst of the three options.
- **The two readings are not a robustness check.** The lane's brief asks whether they land on the same
  side. Under the current class they both land far below 1150 (the Lemma is reading-independent — it
  only uses `P≥0` on a free band), so the ambiguity is masked by a larger defect. Once the class is
  repaired, they will **not** agree, because B is strictly weaker.

**And the deeper objection you asked me to press: yes, the optimisation is mis-posed.** Fourier modes
are global; a causal horizon is local. There is no local statement whose translation is "delete these
global modes." The physically coherent implementations are (a) conditioning the field on a finite
region — which is a statement about the *observable being a patch average and its conditional
statistics*, not a constraint on any global `P`; or (b) a genuine matching/patch construction, which
the source gestures at (Sanghai & Clifton) and never supplies. Under (a) the field on the patch is
**not statistically homogeneous** (the patch centre and the observer's offset from it are physical),
so `C_ℓ` is not a functional of a global `P` at all, and — per the source's own "she sees a different
patch" — **`C_ℓ` is a random variable over patches**, so `S_1/2` is a *distribution*, not a number.
Minimising a number over `P` answers a question the model does not pose.

**One more thing step 3 must not assume.** With Planck inputs, `√(3/Λ) = 5.38 Gpc` and
`D_M(LSS) = 13.885 Gpc`. A causal scale at the de Sitter radius subtends `2 arcsin(χ_§/2D_M) = 22.3°`
(chord) or `22.2°` (arc) — **not 60°**. Reaching 60° needs `χ_§ ≈ 13.9 Gpc`, ≈2.6× the de Sitter
radius. I cannot check Gaztañaga's `χ_§` without opening the source, so I flag rather than conclude:
**step 3 must publish the explicit `Eq.17 → Λ → χ_§ → k_§ → θ` chain and show that 60° falls out, not
assume it.** If 60° requires a factor ~2.6 that Eq. 17 does not supply, then the *location* — the one
thing the corpus credits as a-priori — is also unfixed, and Program (A) is over before step 4.

---

## 4. WOULD EITHER BRANCH BE PUBLISHABLE? — no; one is unreachable, one is vacuous

**Refutation branch: unreachable, and invalid if it fired.** Unreachable by the Lemma
(`S_min ≈ 4 μK⁴` at any honest `k_norm`). Invalid because "mean > observed ⟹ cannot produce" would
refute ΛCDM (§2a). Two independent kills.

**Accommodation branch: exactly the trivial outcome the task warns about.** "A free function on a
compact band, optimised against a scalar, reaches the target" is not a finding — it is the definition
of a free function, and it is *already* what the corpus concluded ("the amplitude is free"). The
convex program would spend real effort re-deriving its own premise, and would report `[S_min, S_max]`
where `S_min` is set by `k_norm` (§W3) and `S_max` is infinite (§W4). A referee closes this in one
sentence: *"Your class contains a cutoff at `k_norm`, so your minimum measures `k_norm`."*

**What WOULD be publishable, and it is close to hand.** Not an optimisation — an **evaluation**:

> The causal cutoff, evaluated at its own licensed point, predicts `S_1/2 ≈ 6.7×10³ μK⁴` **[toy;
> real pipeline required]**, against a masked observation of `1.15×10³`. Under the model's own
> cosmic-variance distribution the observed sky remains a p ≈ X outlier — the causal cutoff moves the
> low-ℓ anomaly from p≈0.1% to p≈X% and no further, **for every spectrum in a class bounded below by
> the model's own content.** The residual freedom is exactly the downward freedom the theory declines
> to fix, and that freedom is unbounded, so no calibration exists.

That is a real no-go *with* a number, it survives the a-posteriori objection (it is a p-value shift,
not a threshold crossing), and it is honest about which half of the freedom is fatal.

---

## MINIMUM REPAIR SET

Ordered; **R1 and R2 are not optional — without them no number should be believed.**

- **R1 — Close the free band.** The class must be bounded **below** as well as above, or `k_norm` must
  be set to `k_§` so no free band exists. The defensible non-circular version: `P = P_ΛCDM` for
  `k ≥ k_§`, `P = 0` (A) or `P` = the Paley–Wiener-consistent analytic form (B) below — a **single
  point**, evaluated, not optimised. Residual freedom is then reported as an explicit low-dimensional
  sensitivity scan (cut sharpness, band tilt), **not** as an infimum over a function space.
- **R2 — Replace min-of-the-mean with a p-value.** Decision rule becomes: *does any admissible spectrum
  raise `P(Ŝ ≤ S_obs)` materially above ΛCDM's ~10⁻³?* This is the only form in which either branch is
  logically valid, and the refutation it yields is stronger than the current one.
- **R3 — Match estimators.** Cut-sky theory vs cut-sky data (simulated masked maps), or move to the
  full-sky number and its ~5% p-value. State which, and do not switch afterwards.
- **R4 — Unlensed `C_ℓ`** (or fixed lensing kernel), so the linearity ⟹ convexity claim is true; bound
  the residual.
- **R5 — Run Reading B as the licensed condition and Reading A as the model-favourable bound.** Claim
  a refutation only if **both** fail. Never claim a positive result from A alone.
- **R6 — Step 3 must derive `χ_§ → 60°` explicitly** and show it lands, given that the de Sitter scale
  gives ~22°.
- **R7 — Declare the isotropisation.** State in the paper that optimising over an isotropic `P(k)` tests
  a statistically-homogeneous surrogate of a model whose defining feature is a finite patch, and that
  the model's own off-diagonal `⟨a_ℓm a*_ℓ'm'⟩` signature is untested here.
- **R8 — Pre-register `k_norm`, `ℓ_max`, mask and estimator before running**, and pull the held-out
  observables (low-ℓ EE, ISW×LSS, `C(θ)` at `θ<60°`) *into* the program rather than leaving them to a
  conditional step 6 that has no unique completion to test.

**Verification receipts (all recomputed here, no file written outside this one):** `M` reproduces
`S[C̄]=32,486 μK⁴` vs charter 34,926 (7%); CV term `+27,353 μK⁴`; MC `P(Ŝ≤1150)=8×10⁻⁴`,
`P(Ŝ≤8000)=9.6×10⁻²`; `cond(M)`: 2.4e3 (ℓ_max=10) → 3e15 with 24 null directions (ℓ_max=100);
SW-toy pure cut `6,713 μK⁴`; `S_min` vs `k_norm` table above; minimiser support 12/300 bins.
