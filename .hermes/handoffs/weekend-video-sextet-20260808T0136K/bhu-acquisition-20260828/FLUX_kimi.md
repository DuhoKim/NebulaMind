F1=FLUX_ALPHA F2=FLUX_GAMMA

Derivation

1. The linearised flux functional δΦ[δ]

Setup and gauge. Take the background ḡ to be FLRW with perfect-fluid source (ρ̄, p̄) and a cosmological constant Λ, satisfying the background flux condition (source Eq. 17, line 262):
Λ/8πG = ½⟨ρ̄+3p̄⟩_§ over M_§. Add linear perturbations in any standard gauge (the argument below uses only scalars constructed from the mixed components T^μ_ν and R^μ_ν, which are gauge-invariant at linear order for the monopole sector that survives; where a gauge choice is needed for concreteness I use the comoving/synchronous slicing of the paper, line 189: u^i = 0, u⁰u₀ = 1).

The fluid term. From the field equation in the paper's conventions (Eq. 9, line 178):
R^μ_ν = 8πG(T^μ_ν − ½δ^μ_ν T) − Λδ^μ_ν.
For a perfect fluid T^μ_ν = (ρ+p)u^μu_ν − p δ^μ_ν, trace T = ρ − 3p, so
R⁰₀ = 8πG( T⁰₀ − ½T ) − Λ = 8πG( ρ − ½(ρ−3p) ) − Λ = 4πG(ρ+3p) − Λ,
which is the paper's Eq. 11 (line 191). Now perturb: ρ = ρ̄ + δρ, p = p̄ + δp. The perturbed 4-velocity u^μ enters T⁰₀ = (ρ+p)u⁰u₀ − p only quadratically in the peculiar velocity (u⁰u₀ = 1 + O(v²)), so at linear order δT⁰₀ = δρ exactly, and δT = δρ − 3δp. Therefore
δR⁰₀ = 8πG( δρ − ½(δρ − 3δp) ) = 4πG(δρ + 3δp),
with no metric perturbation appearing on the right-hand side at this order — the metric enters only through the volume element.

The volume element. The flux is Φ(M) = −∫_M √(−g) d⁴x R⁰₀ (Eq. 16, line 235). Both factors vary: R⁰₀ = R̄⁰₀ + δR⁰₀ and √(−g) = √(−ḡ)(1 + ½h), where h ≡ ḡ^{μν}h_{μν} is the trace of the metric perturbation. Expanding to first order and dropping the background term (already set to zero by Eq. 17):

δΦ[δ] = −∫_{M_§} √(−ḡ) [ 4πG(δρ + 3δp) + ½h R̄⁰₀ ] d⁴x,
with R̄⁰₀ = 4πG(ρ̄+3p̄) − Λ.

So δΦ is a linear functional of the perturbation field δ ≡ (δρ, δp, h_{μν}): an integral over the fixed background 4-window M_§ of a linear combination of perturbation fields, weighted by background quantities only. Defining the window function W(x) = √(−ḡ(x))·1_{M_§}(x) (a spherically symmetric, compactly supported scalar density about the observer's worldline), this is

δΦ[δ] = −∫ d⁴x W(x) S[δ](x),  S[δ] ≡ 4πG(δρ+3δp) + ½h R̄⁰₀.

2. Reading F1: δΦ[δ] = 0 — what it constrains

F1 imposes one scalar equation: the single number δΦ must vanish. Decompose the perturbation field on the observer's sky in spherical harmonics, S[δ](χ, n̂, t) = Σ_{ℓm} S_{ℓm}(χ, t) Y_{ℓm}(n̂). Because M_§ is spherically symmetric about the observer (comoving radius χ ≤ χ_§ on each slice), the window W depends on n̂ not at all: W = W(χ, t). The angular integral then projects exactly one multipole:

δΦ = −∫ dt dχ W(χ,t) χ² ∫ dΩ S[δ] = −∫ dt dχ W(χ,t) χ² √(4π) S₀₀(χ,t),

since ∫ dΩ Y_{ℓm}(n̂) = √(4π) δ_{ℓ0}δ_{m0}. Only (ℓ, m) = (0, 0) enters δΦ. Every ℓ ≥ 1 coefficient of the perturbation field drops out of the constraint identically — not by tuning, but by orthogonality of the spherical harmonics against a constant window.

Consequence for the CMB. The CMB anisotropy a_{ℓm} is a linear functional of the perturbation field along the past light cone, and the two-point statistic C_ℓ = ⟨|a_{ℓm}|²⟩ for ℓ ≥ 1 involves only the ℓ ≥ 1 multipoles of δ. The symmetry argument, written out: the functional δΦ[δ] is invariant under the rotation group SO(3) acting about the observer (W is a scalar under rotations; the integration measure and domain are invariant). Under a rotation R, a_{ℓm} → Σ_{m′} D^{ℓ}_{m′m}(R) a_{ℓm′} — the a_{ℓm} transform as an irreducible (2ℓ+1)-dimensional representation. A rotationally invariant linear constraint can therefore only couple to the trivial representation, ℓ = 0; any coupling to ℓ ≥ 1 would define a preferred direction or multipole pattern, contradicting invariance. Hence δΦ = 0 constrains the observer's monopole only, and

C_ℓ(ℓ ≥ 1) is exactly unchanged, and so is S₁/₂ = (C₂ + C₃)/... any combination of ℓ ≥ 1 spectra.

This is the definition of FLUX_ALPHA in prereg §3. (It is also the control the prereg's numeric check must reproduce: ⟨δ_§ a_{ℓm}⟩ = 0 for ℓ ≥ 1 by isotropy, nonzero only at ℓ = 0.)

3. Reading F2: (W ⋆ δ)(x) = 0 for all x

F2 demands the flux vanish for the causal window of every comoving observer x. Stationarity of the background makes the window the same shape for every observer, so the condition is a convolution: (W ⋆ S[δ])(x) = 0 ∀x (I write δ for the source field S[δ] from here). Fourier transform: the convolution theorem gives

Ŵ(k) · δ̃(k) = 0 for all k.

So at every wavenumber, either δ̃(k) = 0 or Ŵ(k) = 0: the perturbation's Fourier support must lie inside the zero set of Ŵ.

The zero set of Ŵ. W is compactly supported (M_§ is bounded) and not identically zero, so by the Paley–Wiener theorem Ŵ(k) extends to an entire function of exponential type in each k-component; in particular it is real-analytic on ℝ³, and spherically symmetric, so Ŵ(k) = Ŵ(k) with k = |k| an analytic function of k. A nonconstant real-analytic function has isolated zeros (an analytic function vanishing on any set with an accumulation point, or on any open set, vanishes identically — which would contradict W ≢ 0). Hence the zero set of Ŵ is a countable union of isolated spherical shells k = k_n in k-space — a measure-zero set.

Compatible power spectra. A continuous power spectrum P(k) has ⟨|δ̃(k)|²⟩ ∝ P(k), and if P(k) > 0 on any set of positive measure (any open k-interval), then δ̃ has support off the zero shells, and Ŵ·δ̃ ≢ 0 — F2 fails. The variance through the window, ∫ d³k P(k)|Ŵ(k)|², is strictly positive for any such P (the prereg's control integral). The only spectra satisfying F2 are those supported entirely on the measure-zero shell set {k_n}: discrete sums of delta-shells, or P ≡ 0. No continuous power spectrum — in particular nothing resembling the observed smooth acoustic spectrum — is compatible. This is exactly FLUX_GAMMA: perturbations confined to a measure-zero set of wavenumbers, or forced to vanish.

4. Classification

F1 = FLUX_ALPHA. The constraint touches only the observer's ℓ = 0 sky monopole; every C_ℓ with ℓ ≥ 1, and hence S₁/₂, is exactly unchanged. Not BETA, so no C_ℓ modification is owed (and none exists to exhibit).

F2 = FLUX_GAMMA. The universal condition admits no continuous power spectrum at all; it is incompatible with the observed smooth acoustic spectrum.

Per prereg §4, either ALPHA or GAMMA closes flag (ii) negatively: imposed on the perturbed solution, the flux condition is not the missing prescription for a theory-fixed cutoff.

5. Sanity check: spherical top-hat window

For W(r) = 1 for r ≤ R, 0 otherwise:

Ŵ(k) = ∫_{r≤R} d³r e^{−ik·r} = 4π ∫₀^R r² (sin kr)/(kr) dr = 4π [ sin(kR) − kR cos(kR) ] / k³ = (4πR³/3) · 3 j₁(kR)/(kR),

with Ŵ(0) = 4πR³/3 (verified numerically: limit = 4.188790 at R = 1). Zeros satisfy sin x = x cos x, i.e. tan x = x, x = kR. Bisection (200 iterations per root, residual |tan x − x| < 3×10⁻¹⁴, Ŵ at the roots < 6×10⁻¹⁶) gives the first two positive zeros:

x₁ = 4.493409  →  k₁ = 4.493409/R
x₂ = 7.725252  →  k₂ = 7.725252/R

Isolated, simple zeros on discrete shells, as the analyticity argument requires.

Plain-language paragraph

The paper's one derived condition — that the gravitational flux through the causal boundary vanish — was only ever imposed on the smooth background universe, where it fixes Λ. This derivation asks what happens if you also impose it on the lumpy, perturbed universe, and the answer comes out two ways depending on how broadly you read it. Read narrowly, as the paper uses it (our causal region only), the condition says only one thing: the average density-plus-pressure lumpiness inside our causal sphere must balance to zero. Because the sphere is perfectly round, it is blind to every pattern on the sky — all the hot and cold spots, all the acoustic wiggles in the CMB spectrum, are completely untouched, so it predicts no cutoff and no suppression of any kind. Read broadly — the condition holds for every observer everywhere — it becomes far too strong: the mathematics of Fourier transforms then forces the universe's lumpiness to live on a measure-zero set of isolated wavelengths, which means no smooth, continuous spectrum of fluctuations can exist at all, flatly contradicting the smooth acoustic spectrum we actually observe. Either way, the flux condition cannot be the missing ingredient that gives the paper's cutoff a fixed, computable strength: in its usable form it says nothing about anisotropies, and in its strong form it says too much to be true.
