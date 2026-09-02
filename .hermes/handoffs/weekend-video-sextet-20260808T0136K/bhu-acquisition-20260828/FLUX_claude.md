F1=FLUX_ALPHA F2=FLUX_GAMMA

# Program (C) flux route — claude-seat independent derivation (BLIND)

Inputs used: `PROGRAM_C_FLUX_PREREG_20260902.md`; `../bhu-reading-20260823/sources/2003.11544_clean.txt`
lines 130–160 (Eqs. 6–7, Newtonian flux) and 186–300 (Eqs. 10–19, Eq. 11 `R⁰₀ = 4πG(ρ+3p) − Λ`,
Eq. 16 `Φ = −∫_M √(−g) d⁴x R⁰₀`, the condition Φ(χ>χ_§)=0, Eq. 17). Nothing else opened.
Stance: adversarial toward the prereg's control expectation; every place the expectation could
fail is flagged in §6.

## 1. Linearised flux functional δΦ[δ]

**Conventions.** Signature (+,−,−,−) (the paper cites Landau–Lifshitz and writes u⁰u₀ = 1),
c = 1, field equations `G^μ_ν = 8πG T^μ_ν + Λ δ^μ_ν`. Trace: `−R = 8πG T + 4Λ`, so
`R^μ_ν = 8πG (T^μ_ν − ½ δ^μ_ν T) − Λ δ^μ_ν`. For a perfect fluid
`T^μ_ν = (ρ+p) u^μ u_ν − p δ^μ_ν`, `T = ρ − 3p`, and in the fluid rest frame
`T⁰₀ = ρ`, giving `R⁰₀ = 8πG(ρ − ½(ρ−3p)) − Λ = 4πG(ρ+3p) − Λ`. This reproduces the paper's
Eq. 11, fixing the convention in which every symbol below is read.

**Gauge.** Comoving-synchronous gauge: `ds² = a²(η)[dη² − (δ_ij + h_ij) dx^i dx^j]`, fluid
`u^i = 0` exactly, the observer on the worldline x = 0. This is the gauge in which the paper's
own statement "events comoving with the fluid, u^i = 0" holds at all orders, and in which the
window `χ ≤ χ_§` is a fixed coordinate region. Gauge robustness is argued at the end of this section.

**Fluid term.** `R⁰₀ = 8πG (T⁰₀ − ½T) − Λ`. The Λ term is `Λ δ⁰₀`, a fixed number: no
perturbation. Perturb the fluid: with `u^μ u_μ = 1`, `u⁰u₀ = 1 − u^i u_i = 1 + O(v²)`, so
`T⁰₀ = (ρ+p)(1 + O(v²)) − p = ρ + O(v²)` and `δT⁰₀ = δρ` at linear order in every gauge
(velocity enters T⁰₀ only quadratically). `δT = δρ − 3δp`. Hence
`δ(T⁰₀ − ½T) = δρ − ½δρ + (3/2)δp = ½(δρ + 3δp)` and

    δR⁰₀ = 4πG (δρ + 3δp)          (linear order, exact)

**Volume element.** `√(−g) = a⁴ √det(δ_ij + h_ij) = a⁴ (1 + ½h) + O(h²)`, `h ≡ h_ii`, so
`δ(√−g) = ½ a⁴ h`, `√(−ḡ) = a⁴`.

**Boundary.** Φ is defined on the region M_§; in synchronous-comoving coordinates M_§ is a fixed
coordinate region `{(η, x): |x| ≤ χ_§, η ∈ I(|x|)}` (any time extent I, possibly χ-dependent, e.g.
a light cone). The prereg fixes only spherical symmetry about the observer's worldline, so write
its indicator as `W(η, χ)`, χ = |x|. If instead the boundary were defined physically and moved
under perturbation by `δχ_b(η, n̂)`, the extra term is `−∫ dη a⁴ R̄⁰₀(η) χ_§² ∫dΩ δχ_b(η, n̂)`:
linear, and (§2) again only its ℓ = 0 part survives, so nothing below changes.

**Result.** `Φ = Φ̄ + δΦ`, with `Φ̄ = −∫ dη d³x W a⁴ R̄⁰₀(η) = 0` being exactly the paper's Eq. 17
(`R̄⁰₀ = 4πG(ρ̄+3p̄) − Λ`, Λ chosen to kill the 4-volume average), and

    δΦ[δ] = −∫ dη ∫ d³x  W(η,|x|) a⁴(η) [ 4πG (δρ + 3δp) + ½ h · R̄⁰₀(η) ](η, x)
          = ∫ dη ∫ d³x  W(η,|x|) Σ_A c_A(η) f_A(η, x),     f_A ∈ {δρ, δp, h},
            c_δρ = −4πG a⁴, c_δp = −12πG a⁴, c_h = −½ a⁴ R̄⁰₀.

The essential structure: δΦ is a **linear** functional whose kernel depends on x **only through
|x|** (W spherically symmetric, coefficients c_A functions of η only because the background is
homogeneous). Note R̄⁰₀(η) changes sign during the expansion (4πGρ̄ > Λ early, < Λ late), so the
h-term is not negligible in general; it is nevertheless of the same form.

**Gauge robustness.** Under `x^μ → x^μ + ξ^μ`, δρ, δp, h shift by terms linear in ξ^μ and in
background quantities (`δρ → δρ − ρ̄' ξ⁰` etc.), and the integrand `√−g R⁰₀ d⁴x` is not a scalar
density (R⁰₀ is a mixed component), so δΦ changes by a linear functional of ξ^μ. The class results
in §2–§3 use only (i) linearity and (ii) covariance of the kernel under rotations about the
observer / translations (F2). Any gauge choice that preserves the observer-centred spherical
symmetry of the set-up (ξ⁰ = ξ⁰(η, χ), ξ^i ∝ x^i) preserves (ii); therefore the classification is
gauge-independent, while the *numerical value* of δΦ for a given realisation is gauge-dependent,
as it must be for a non-covariant quantity. (Conformal-Newtonian gauge gives the same result with
`√−g = a⁴(1 + Ψ − 3Φ_N)` in place of `a⁴(1 + ½h)`.)

## 2. Reading F1 — one scalar constraint δΦ[δ] = 0 for our M_§

**Harmonic decomposition about the observer.** For each field,
`f_A(η, x) = Σ_{ℓ≥0} Σ_{|m|≤ℓ} f_{A,ℓm}(η, χ) Y_ℓm(n̂)`, x = χ n̂. Insert into δΦ:

    δΦ = Σ_A ∫ dη c_A(η) ∫ χ² dχ W(η,χ) Σ_{ℓm} f_{A,ℓm}(η,χ) ∫ dΩ Y_ℓm(n̂).

Since `∫dΩ Y_ℓm = √(4π) δ_{ℓ0} δ_{m0}` (Y_00 = 1/√4π is the only harmonic with nonzero angular
mean),

    δΦ = √(4π) Σ_A ∫ dη c_A(η) ∫ χ² dχ W(η,χ) f_{A,00}(η,χ).

**Exactly which (ℓ, m) enter: (0, 0) only**, for every field, at every radius and time. Every
`f_{A,ℓm}` with ℓ ≥ 1 is multiplied by zero — not suppressed, absent.

**Symmetry argument, written out.** Let R ∈ SO(3) act on fields by `(R f)(η, x) = f(η, R⁻¹x)`.
Because W depends on x only via |x| and c_A only on η, `δΦ[R f] = δΦ[f]`: δΦ is an
SO(3)-invariant linear functional. The harmonic coefficients transform in the (2ℓ+1)-dimensional
irreducible representation, `f_{ℓm} → Σ_{m'} D^ℓ_{m'm}(R) f_{ℓm'}`. Restrict δΦ to the subspace
`V_ℓ` spanned by `{g(η,χ) Y_ℓm}_m` at fixed radial profile g: this is a linear map from the ℓ-irrep
to the trivial representation, commuting with SO(3); by Schur's lemma it is zero unless ℓ = 0.
Constructively: `δΦ[f_ℓm] = ∫dR δΦ[R f_ℓm] = δΦ[∫dR R f_ℓm] = Σ_{m'} (∫dR D^ℓ_{m'm}(R)) δΦ[f_ℓm'] = 0`
for ℓ ≥ 1, since Haar-averaged Wigner matrices vanish for ℓ ≥ 1. This reproduces the explicit
`∫dΩ Y_ℓm` computation without ever needing the shape of W beyond spherical symmetry.

**Consequence for the CMB.** The observed `a_ℓm` (ℓ ≥ 1) are linear functionals of the same
perturbation fields, with kernels (Sachs–Wolfe, Doppler, ISW, in a homogeneous isotropic
background) that are rotation-covariant about the observer: the sky multipole (ℓ, m) is built from
the (ℓ, m) components of the fields along the line of sight. Hence
- The constraint `δΦ = 0` is a single linear condition on the ℓ = 0 sector
  `{f_{A,00}(η, χ)}`. It leaves the ℓ ≥ 1 sector of every field unconstrained.
- For a statistically isotropic Gaussian field, the (0,0) and (ℓ≥1, m) sectors are uncorrelated:
  `⟨f_{00}(χ) a_ℓm⟩` must be invariant under R but transforms as `D^ℓ` ⇒ zero for ℓ ≥ 1 (same
  Schur argument, applied to the correlation vector). Conditioning a Gaussian on a linear
  functional of variables independent of `{a_ℓm}_{ℓ≥1}` leaves the distribution of
  `{a_ℓm}_{ℓ≥1}` unchanged. Therefore

      C_ℓ (ℓ ≥ 1) unchanged for every ℓ;  S₁/₂ = ∫_{−1}^{1/2} C(θ)² dcosθ, built from ℓ ≥ 2, unchanged.

- The constrained monopole is, moreover, degenerate with the mean temperature T₀ in the CMB and
  is not an anisotropy observable at all.
- The paper's stated hope of "an infrared cutoff in the spectrum of inhomogeneities" does not
  follow from F1: no scale χ_§-dependent factor multiplies any ℓ ≥ 1 mode.
- Alternative F1 phrasing — "Λ is whatever makes Φ(M_§) = 0 including the perturbation": then
  `δΛ = 8πG · ½ δ⟨ρ+3p⟩_§` (plus the h-term), a renormalisation of the background Λ by the
  monopole; zero constraint on any anisotropy. Same class.

**Class: FLUX_ALPHA.**

## 3. Reading F2 — Φ(M_§(x)) = 0 for every comoving observer x

Translate the window to each observer: `G(x) ≡ Σ_A ∫ dη c_A(η) ∫ d³y W(η, |y − x|) f_A(η, y) = 0`
for all x ∈ ℝ³ (comoving). The 3-integral is a convolution `(W(η,·) ⋆ f_A(η,·))(x)`.

**Fourier transform** (convention `f̃(k) = ∫ d³x e^{−ik·x} f(x)`; convolution theorem):

    G̃(k) = Σ_A ∫ dη c_A(η) W̃(η, k) f̃_A(η, k) = 0   for all k,   with k ≡ |k|,

where `W̃(η, k) = 4π ∫₀^{χ_§} W(η, χ) (sin kχ / kχ) χ² dχ` depends on |k| only. At linear order every
field is a transfer function times the primordial amplitude, `f̃_A(η, k) = T_A(η, k) ζ̃(k)`
(adiabatic single mode; for several modes read ζ̃ as a vector and K as a row vector), so

    G̃(k) = K(k) ζ̃(k),   K(k) ≡ Σ_A ∫ dη c_A(η) W̃(η, k) T_A(η, k).

**Implication for δ̃(k):** `ζ̃(k) = 0` at every k where `K(k) ≠ 0`; equivalently `δ̃(k)` (any
gauge-choice of δ, being `T_δ ζ̃`) vanishes off the zero set `Z = {k : K(k) = 0}`.

**Zero set of W̃ and of K.** For each η, W(η, ·) is compactly supported (|y| ≤ χ_§), and M_§ is a
bounded 4-region. By the **Paley–Wiener theorem** (Paley–Wiener–Schwartz for distributions), the
Fourier transform of a compactly supported function is an **entire** function of k ∈ ℂ³ of
exponential type; for radial W it is an entire, even function of the single complex variable k.
An entire function that is not identically zero has **isolated zeros** (identity theorem), with no
accumulation point in the finite plane — a countable discrete set on k > 0, i.e. countably many
spheres in k-space, Lebesgue measure zero. `W̃(0) = 4-volume-weighted 3-volume > 0`, so W̃ ≢ 0.
The transfer functions T_A(η, k) solve linear ODEs in η whose coefficients are polynomials in k,
so they are entire in k as well; hence K(k) is real-analytic on k > 0 and, unless K ≡ 0
(see §6), its zero set Z is likewise discrete and of measure zero.

**Compatible power spectra.** Define P by `⟨ζ̃(k) ζ̃*(k')⟩ = (2π)³ δ³(k−k') P(k)`. Then

    ⟨|G(x)|²⟩ = ∫ d³k/(2π)³ |K(k)|² P(k) = 0   ⇒   |K(k)|² P(k) = 0 for a.e. k   ⇒   P(k) = 0 for a.e. k

(P ≥ 0 and |K|² > 0 off a null set). A **continuous** P that vanishes on a dense set (the
complement of the closed null set Z) vanishes identically. Hence the only continuous P compatible
with F2 is **P ≡ 0**: no perturbations. The most F2 allows is a singular spectrum supported on the
shells |k| ∈ Z — a sum of delta functions in k, and even that only where K (not merely W̃) vanishes.
Equivalently, in the prereg's control form: `∫ P(k) |W̃(k)|² d³k > 0` for any P > 0 on a set of
positive measure, since |W̃|² > 0 off a null set. The observed smooth acoustic spectrum is
incompatible. Two adversarial corollaries against the paper's "infrared cutoff" expectation:
(i) an IR cutoff `P = 0 for k < k_§, P = P_ΛCDM above` does **not** satisfy F2 — every k > k_§ off
Z must vanish too; (ii) |W̃(k)| is *largest* at k → 0 (it equals the window volume), so the
condition bears hardest on the largest scales, but what it does there is "zero", not "suppress".

**Class: FLUX_GAMMA.**

## 4. Classification per prereg §3

- **F1 = FLUX_ALPHA.** δΦ[δ] contains only (ℓ, m) = (0, 0) of every field; every C_ℓ, ℓ ≥ 1, and
  S₁/₂ are exactly unchanged; the constrained monopole is not even a CMB observable.
  Not BETA: no C_ℓ modification exists to exhibit — the ℓ ≥ 1 kernel is identically zero, not
  small.
- **F2 = FLUX_GAMMA.** Perturbations confined to the measure-zero set Z (shells |k| ∈ Z), and for
  continuous P forced to vanish. No cutoff at χ_§ emerges; the condition kills all scales.

Neither reading yields a licensed cutoff under prereg §4: flag (ii) closes negatively — the flux
condition, imposed on the perturbed solution, is not the missing prescription for a theory-fixed
cutoff amplitude.

## 5. Mandatory sanity check — spherical top-hat window of radius R

`W(χ) = Θ(R − χ)`:

    W̃(k) = 4π ∫₀^R (sin kχ / kχ) χ² dχ = (4π/k³) [ sin kR − kR cos kR ] = (4πR³/3) · 3 j₁(kR)/(kR).

Verified numerically against direct quadrature (R = 1; k = 1: 3.784597 both; k = 3: 1.447971
both; k = 6: −0.351418 both). Zeros: `tan x = x`, x = kR, x ≠ 0 (at x → 0, W̃ → 4πR³/3 ≠ 0):

    x₁ = 4.493409,   x₂ = 7.725252   (x₃ = 10.904122)
    ⇒ k₁ = 4.4934/R,  k₂ = 7.7253/R.

For R = χ_§ = 14,015 Mpc: `k₁ = 3.206 × 10⁻⁴ Mpc⁻¹`, `k₂ = 5.512 × 10⁻⁴ Mpc⁻¹`. The zeros are simple
and isolated, spacing → π/R asymptotically, exactly as the Paley–Wiener / identity-theorem argument
requires; the zero set in k-space is the countable family of spheres |k| = x_n/R, measure zero.
`W̃(k₁) = −1.2 × 10⁻¹⁵` (R = 1) in the quadrature, i.e. zero to machine precision.

## 6. Where the prereg's expectation could have failed (adversarial audit) — and did not

1. *Non-spherical M_§.* If the lane's 4-window were not spherically symmetric about the observer,
   ℓ ≥ 1 modes would enter δΦ with amplitude set by the window's own multipoles — but then the
   "cutoff" would be the lane's window shape, not the paper's physics (prereg §4 already says so).
   Under the stated hypothesis there is no leak.
2. *Non-Gaussianity.* With Gaussian, statistically isotropic initial conditions the F1 monopole
   constraint cannot alter ℓ ≥ 1 statistics. For non-Gaussian fields, conditioning on the monopole
   could in principle reach ℓ ≥ 1 through mode coupling — but that is beyond linear order and
   beyond the paper, and is not a "cutoff tied to χ_§".
3. *Velocity / dipole.* Velocities enter T⁰₀ only at O(v²); the ℓ = 1 sector is untouched in F1.
4. *K ≡ 0 identically (F2).* Would require the window to be tuned so that
   `Σ_A ∫dη c_A W̃ T_A` cancels for every k — a non-generic fine tuning of M_§'s shape against the
   ΛCDM transfer functions. If the lane ever constructed such a window, F2 would become vacuous
   (no constraint at all, i.e. ALPHA-like, not BETA) — still no cutoff.
5. *Statistical reading of F2* (`⟨Φ⟩ = 0` for every observer). This is Eq. 17 itself, satisfied by
   the background; it constrains no perturbation.
6. *Gauge.* δΦ's value is gauge-dependent (R⁰₀ is not a scalar), but the class depends only on
   linearity and rotation/translation covariance, both gauge-independent (§1).
7. *Boundary perturbation.* A physically defined, perturbed ∂M_§ adds a linear term with the same
   spherical kernel; ℓ = 0 only (§1).

## Plain language

The paper's one real equation says: add up all the gravity "pull" inside our causal bubble and
demand it comes out to zero; that fixes the value of Λ. I asked what happens if you also demand
this of the small ripples in the density. If you demand it only for our own bubble (the way the
paper uses it), the sum only sees the average of the ripples over the bubble — the part that looks
the same in every direction — so it cannot touch anything that varies across the sky: the CMB
anisotropy spectrum, and the S₁/₂ statistic built from it, are left exactly as they were. If
instead you demand it for every observer everywhere, the convolution with a finite ball has a
Fourier transform that is zero only on a sparse set of isolated wavenumbers (the top-hat's first
two at kR = 4.49 and 7.73), so the ripples would have to vanish at essentially every scale — not
just the largest ones — which no smooth spectrum, and certainly not the observed one, can
satisfy. Either way the flux condition does not supply the missing large-scale cutoff.
