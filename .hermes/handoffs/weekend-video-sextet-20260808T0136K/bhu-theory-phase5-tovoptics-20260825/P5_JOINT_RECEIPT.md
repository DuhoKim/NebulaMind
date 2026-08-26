# P5 receipt — the joint exclusion. One transfer, every opacity, no branch split.
(2026-08-26. p5_joint_exclusion.py, log _tmp_p5_run.txt, 4/4 checks. This is the phase's real
deliverable, built after P1c reopened the opacity question.)

## Why a joint argument was necessary

P1 claimed the exterior was optically thin and retired the emitting branch. P1c withdrew that:
τ runs from 0.04 to above 2.6 *inside* the authorised range, so thin and opaque are both live
and neither can be resolved from the pinned physics. The phase therefore cannot rest on
choosing a branch. It has to show the two exclude **together**.

## The correction this exposed in my own P2

P2 applied the Doppler factor only to the transmitted background, treating the exterior's
emission as unshifted. **That is wrong**: the emitting matter IS the TOV fluid, moving at
β_rel relative to us, so its emission carries the same D. The transfer is

  1 + ΔT/T (μ) = **D(μ) · [ e^(−τ) + (1 − e^(−τ))·(T̄/T_FRW) ]**

with D outside the bracket. The bracket varies only weakly with direction (through the
crossing epoch); D carries the strong angular dependence. **D multiplies the entire beam** —
transmitted and re-emitted alike.

## The structural result

**An opaque exterior does not hide the offset. It re-emits it.**

| τ | regime | dipole coefficient | bound on x_off/r_*(cross) |
|---|---|---|---|
| 0 | vacuum | 0.6153 | 2.21e-3 |
| 0.13 | junction w | 0.5774 | 2.35e-3 |
| 0.93 | marginal | 0.4107 | 3.31e-3 |
| 2.6 | opaque | 0.2794 | 4.86e-3 |
| 20 | saturated | 0.2461 | 5.52e-3 |
| 1000 | — | 0.2461 | — |

**The dipole SATURATES at a finite floor** (0.2461, reached by τ ≈ 20 and unchanged at
τ = 1000) instead of vanishing. Opacity dilutes the anisotropy by a bounded factor of 2.50 —
it never removes it, at any opacity, because the same Doppler factor multiplies the re-emitted
light that multiplied the transmitted light.

*(Honest note: my first version of this check asserted the coefficient was nearly independent
of opacity, and the run refuted it at 2.5×. The corrected claim — saturation at a nonzero
floor — is what is true and is what the argument actually needs.)*

## The joint conclusion

**Over the FULL opacity range, thin through saturated, a boundary inside our last-scattering
sphere requires the observer centred to between one part in 453 and one part in 181** of the
crossing radius (normalised per the gate's B1 ruling).

**The exclusion does not depend on resolving the opacity** — which is what makes it survive
P1c's withdrawal. The unknown that Phase 5b was commissioned to pin down turns out not to need
pinning down: it moves the bound by a factor of 2.5 and cannot escape it.

## Standing limits

σ = 1/3, pre-horizon, photon channel. B2 ruling applied (no standalone propagation factor).
Source ceilinged at the energy budget (T̄/T_FRW = v^(1/4)). Frozen row B2.2 supplies the
observational limit. NOT yet blind-doubled — this transfer is new, including the Doppler
correction above, and the double is owed before any of it is claimed as confirmed.
