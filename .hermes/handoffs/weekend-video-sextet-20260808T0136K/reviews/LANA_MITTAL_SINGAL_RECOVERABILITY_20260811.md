# LANA — is the Mittal–Singal factor-of-three recoverable from stated methods?

Per `HWAO_LOOSENED_BAR_MITTAL_SINGAL_ORDER_20260811T1110K.md` (`1d33052a25a8fc6b`). Filed **2026-08-11 11:26
KST**. **Assessment only — no design, no run, no statistic. Public data only.** Bar loosened on *novelty
only*: adjudicating a published disagreement is now admissible. Custody, pre-registration, believe-and-build,
and my claim boundary are unchanged. This order settles one thing: **is the difference recoverable from the
papers' stated methods, or does it hide in unstated choices?** I read both papers' methods (not abstracts).

## Answer up front — RECOVERABLE, and both authors name the same cause. NOT the fifth closure.
The entire factor of three is **one stated, first-order fork: the Quaia selection-function correction.**
Mittal applies it; Singal explicitly refuses it — and Singal names Mittal's selection step as the reason they
differ. It does **not** hide in unstated choices. This is adjudicable.

---

## Part A — every stated analysis choice, Mittal vs Singal

| Choice | Mittal et al. 2024 (MNRAS 527, 8497) | Singal 2024 (MNRAS 532, L1) | Same driver? |
|---|---|---|---|
| **Selection function** | **Applied.** Multiplicative in the rate: Poisson `λᵢ·sᵢ`; point-by-point scales `Nᵢ` by `1/sᵢ`; normalised `f̂ᵢ = sᵢfᵢ/Σsᵢfᵢ`. | **NOT applied.** Verbatim: *"We did not incorporate the selection function… their procedure seems to obliterate any dipole asymmetries across the sky."* | **★ THE DRIVER** |
| **Mask / Galactic plane** | `|b|<10,20,30,40°` tested; headline consistency at `|b|<40°` (+ a `30∗` composite, 4 sr cap on centre). | `|b|>30,35,40°`; explicitly *"following Mittal… we also employ |b|<40° mask,"* still gets 3.3×10⁻². | Second-order |
| **Estimator** | Bayesian nested sampling (Dynesty), Poisson / point-by-point likelihood, HEALPix `Nside=64`. | Dipole **vector sum** + hemisphere `2(N₁−N₂)/(N₁+N₂)` on 10°×10° cells. | Second-order* |
| **Kinematic null** | Ellis–Baldwin via actual counts + per-source Doppler boost `S→Sδ^(1+α)`; expected `D̄≈0.0080` (low). | Ellis–Baldwin `D=[2+x(1+α)]β`, `x=1.3, α≈2.4 (from Mittal)` → factor `6.4`; `v=370 km/s`. | **Same (≈6.4)** |
| **Magnitude cuts** | `G<20.0` (low, 755,850); `G<20.5` (high). | `G<20.5`, `G<20.0`, and `20<G<20.5` — all give `D≈3.3×10⁻²`. | Second-order |
| **Redshift** | none | none | Identical |
| **Measured amplitude** | selection-corrected ⇒ **consistent with `D̄≈0.008`** (CMB-kinematic), `|b|<40`. | **`D=3.3±0.5×10⁻²`, `p=4.2±0.6`** (≈4× CMB), direction RA 181°/Dec +20°. | — |

\* Note the *estimator×mask* interaction as a **candidate second-order contributor**: a linear/vector
estimator on a **cut sky** is biased unless mask geometry is corrected, and can inflate amplitude. Worth
checking in an adjudication, but it is not the factor-of-three — Singal himself attributes that to selection.

## Part B — what could produce a factor of three
**One thing does: the selection function.** The kinematic null is essentially identical (both ≈6.4, both
expect `D̄≈0.008`), so the gap is entirely in the **measured** amplitude: `3.3×10⁻²` **without** the
selection function (Singal) versus **`≈0.008`-consistent with it** (Mittal). Singal states the mechanism in
his own words: *"the dipoles will get suppressed in this procedure and that might be the reason why results of
Mittal et al. (2024) differ from ours."* Everything else is second-order and **controlled by cross-checks in
the papers themselves**: Singal reproduces `3.3×10⁻²` even under Mittal's own `|b|<40°` mask and across three
magnitude cuts, so mask and magnitude are ruled out as the driver *by his own tables*.

## Part C — recoverable, or hidden in unstated choices?
**Recoverable, decisively.** The decisive choice is **stated in both papers** — Mittal writes the selection
function into the likelihood; Singal states he omits it and why. This is the cleanest possible recoverability
result: the two groups do not secretly disagree about the data, they openly disagree about **one correction.**
So this is **not** a dead end, and it is not the fifth closure — the honest closure is not the answer here.

## Part D — what a careful adjudication would establish, and what it would NOT
**Would establish (mechanical, reproducible):** the exact decomposition — how much of the raw Quaia dipole the
published selection function absorbs — confirming that the full 4× → CMB-consistent shift is the selection
correction and nothing else. That alone is an admissible, novelty-loosened result: *"the Mittal–Singal
factor-of-three is entirely the Quaia selection-function correction; with it the amplitude is CMB-consistent,
without it it is ≈4×."*

**Would NOT establish — and here is the real question the adjudication turns on:** *whether the Quaia
selection function is entitled to absorb that amplitude.* Singal's charge is structural — a selection function
built under an isotropy assumption **cannot help but** suppress a real dipole. Whether that charge is valid
depends entirely on **how the selection function is constructed** — specifically, whether its systematics
templates (dust, stellar density, Gaia scanning depth) carry **dipole-scale/large-angular power that could
soak up a genuine cosmological dipole**, or whether it is built only from small-scale systematics with no
freedom at the dipole mode. **That is not in Mittal or Singal — it is in the Quaia catalogue paper
(Storey-Fisher et al. 2024) and the public selection-function product.** It is **readable, not hidden** — but
it requires reading the Quaia selection-function construction, which I have **not** yet done. So the pivotal
item for any design is: *does the Quaia selection-function regression have dipole-mode freedom?* If **no**
(external templates only), the selection-corrected/CMB-consistent result is the defensible one; if **yes**,
the amplitude is not cleanly separable from selection on Quaia and the disagreement is genuinely irreducible
on this catalogue. Both are real, publishable adjudication outcomes.

**Claim boundary (binds, unchanged):** an adjudication may say *"the factor-of-three is attributable to the
selection-function correction,"* and, per the Storey-Fisher finding, either *"the correction cannot absorb a
dipole-scale mode, so the CMB-consistent amplitude is defensible"* or *"the correction has dipole-mode
freedom, so the amplitude is not separable from selection."* It may **not** say the universe is anisotropic or
isotropic, that the cosmological principle is upheld or refuted, or that Mittal or Singal is "correct" as
cosmology. The direction is undisputed; only the amplitude's selection-dependence is at issue. **Neither
paper's conclusion becomes ours to assert.**

## Disposition
The difference is **recoverable from stated methods** — one fork, the selection-function correction, named by
both authors. This is adjudicable and admissible under the loosened bar. The **one pivotal readable item**
before any design is the **Quaia selection-function construction (Storey-Fisher 2024): does it have
dipole-mode freedom?** — that determines whether an adjudication settles the amplitude or only decomposes it.
Assessment only; no design, no run; nothing accepted without Duho. Relay submitted.
