# Program (C) pre-registration — the flux route: impose Φ(χ>χ_§)=0 on the PERTURBED solution

**Ordered by Duho in direct chat, 2026-09-02 ~16:25 KST: "go ahead with the flux condition route."**
Written BEFORE any derivation is filed. In-lane; the paper is HELD; whatever this returns is
lane-owned and moves no tier by itself (ruling `INTERP_RULING_23_27_20260902.md`, option (d) note).

## 0. Why this exists
Program (A) found the paper's ONE derived condition is the flux condition (source lines 235–264,
Eqs. 16–17), that it constrains Λ, and that it "has never been imposed on the perturbed solution by
anyone" (freedom map §2, flag ii). This program imposes it and reports what it constrains.

## 1. Objects, every symbol bound (register §1at)
- Source: `../bhu-reading-20260823/sources/2003.11544_clean.txt` (arXiv 2003.11544, entry 23).
- **R⁰₀** — the mixed time-time component of the Ricci tensor. For a perfect fluid in its rest
  frame the paper's Eq. 11 (line 191): `R⁰₀ = 4πG(ρ + 3p) − Λ` (units c = 1).
- **Φ(M)** — the paper's relativistic flux, Eq. 16 (line 235): `Φ = −∫_M √(−g) d⁴x R⁰₀`, M a
  4-region bounded by a 3-surface ∂M. Eq. 15 (line 225) is the weak-field version.
- **χ_§** — the comoving causal scale; the paper's Eq. 23 gives `χ_§ = 3.149 c/H₀ = 14,015 Mpc`
  (freedom map §1, verified). Its exact value is irrelevant here; only that it is finite.
- **M_§** — "the volume inside the lightcone to the surface ∂M_§, where χ = χ_§" (line 264ff).
  Its precise 4-shape is not fixed by the paper; **this program requires only that M_§ is
  spherically symmetric about the observer's worldline** (comoving radius χ ≤ χ_§ on each slice,
  any time extent). Results must be stated for any such window.
- **The condition** (line 260): "we will require Φ(χ>χ_§)=0 in Eq.16 … This implies" Eq. 17:
  `Λ/8πG = ½⟨ρ+3p⟩_§`, the 4-volume average over M_§.
- **Perturbed solution**: FLRW background `ḡ` + linear perturbations (any standard gauge; the
  result must be gauge-robust or the gauge dependence stated). At linear order the fluid side is
  `δR⁰₀ = 4πG(δρ + 3δp)` exactly (from `R^μ_ν = 8πG(T^μ_ν − ½δ^μ_ν T) − Λδ^μ_ν` with
  `δT⁰₀ = δρ`, velocity entering T⁰₀ only at second order). The volume element also varies:
  `δ(√−g)`. So the linearised flux is the linear functional
  `δΦ[δ] = −∫_M [ √(−ḡ) 4πG(δρ+3δp) + δ(√−g) R̄⁰₀ ] d⁴x`, with `R̄⁰₀ = 4πG(ρ̄+3p̄) − Λ`.

## 2. Two readings of "impose it on the perturbed solution" — both are computed
- **F1 (observer-centred, as the paper uses it for Λ):** Φ(M_§) = 0 for OUR M_§ only, background
  part already satisfied by Eq. 17. Then the perturbations must satisfy ONE scalar constraint
  `δΦ[δ] = 0`.
- **F2 (universal):** Φ(M_§(x)) = 0 for the causal region of EVERY comoving observer x (the paper
  says an observer at our boundary "will find a similar solution", line 250). Then
  `(W ⋆ δ)(x) = 0` for all x, W the 4-window of M_§.

## 3. Outcome classes — declared now, before derivation
- **FLUX_ALPHA:** the condition constrains only the ℓ = 0 (monopole) part of the observer's sky
  and leaves every C_ℓ, ℓ ≥ 1, and hence S₁/₂, exactly unchanged.
- **FLUX_BETA:** the condition produces a definite suppression/cutoff of the anisotropy spectrum at
  scales tied to χ_§ — a computed C_ℓ modification (then: compute it and its S₁/₂).
- **FLUX_GAMMA:** the condition admits no continuous power spectrum at all (perturbations confined
  to a measure-zero set of wavenumbers, or forced to vanish) — incompatible with the observed
  smooth acoustic spectrum.
- **FLUX_DELTA:** something else (state it exactly).
A reading may land in a different class from the other; report each.

## 4. What would count as a licensed cutoff (the bar, stated in advance)
Only FLUX_BETA with a computed C_ℓ would give the paper's cutoff a theory-fixed amplitude, and even
then it would be the lane's construction of M_§'s shape (unfixed by the paper) that set the number.
ALPHA or GAMMA closes flag (ii) negatively: the flux condition is not the missing prescription.

## 5. Method and controls
- Blind double at minimum (codex + claude-seat; kimi and agy if available), each deriving from THIS
  file and the source only; coordinator derives independently and writes a numeric check
  (`flux_monopole_check.py`): for a spherical top-hat window compute the cross-correlation
  ⟨δ_§ a_ℓm⟩ from a smooth P(k) for ℓ = 0, 1, 2 (expected: nonzero at ℓ = 0 only, by isotropy —
  this is the control that must reproduce the symmetry argument numerically, not assert it), and
  for F2 show ∫P(k)|W̃(k)|²d³k > 0 for any P > 0 on a set of positive measure.
- Refutation of the coordinator's expectation: a seat exhibiting, for a spherically symmetric M_§,
  a nonzero ⟨δ_§ a_ℓm⟩ at some ℓ ≥ 1, or a continuous P(k) ≠ 0 satisfying F2, with the arithmetic.
- Reporting grammar: classes, derivations, and receipts; no tier language.
