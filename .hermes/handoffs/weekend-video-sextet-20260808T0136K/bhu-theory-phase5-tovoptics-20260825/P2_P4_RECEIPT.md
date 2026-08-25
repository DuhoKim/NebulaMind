# P2–P4 receipt — the transfer, the pattern, and the confrontation
(2026-08-25, stamped at commit. p2p4_transfer_confront.py, log _tmp_p2p4_run.txt, 6/6 checks.
Built on P1's thin-regime result; P1's blind double still running, so every number here is
conditional on P1 surviving it.)

## The three gate objections this closes

**Objection 3 — "S2 does not implement the transfer function."** P2 now carries absorption and
emission: I_obs = e^{−τ}·(Doppler-shifted background) + (1−e^{−τ})·(exterior emission at
T̄/T_FRW). At P1's upper bound τ = 0.07 the correction to the kinematic result is **9.2%** —
a perturbative correction, not a competitor. LC1 verifies it reduces exactly to the kinematic
case as τ → 0.

**Objection 4 — normalisation.** The monopole is now removed *before* any amplitude is quoted.
The ℓ=0 coefficient is +0.5134 (the mean-temperature rescale, not an observable); every
multipole below is computed on the monopole-subtracted pattern. A centred observer leaves
nothing behind after removal — max |ℓ≥1| = 7.7e-30 (LC4).

**Objection 5 — Doppler orientation, fixed physically rather than by convention.** The shock is
an outgoing blast wave and the exterior is the thinner side (v = ρ̄/ρ < 1), so the exterior is
UPSTREAM and is swept inward relative to the FRW fluid. An approaching emitter blueshifts:
1+z = 0.659 < 1, so the crossing radiation arrives **hotter**, ΔT/T = +0.517. The orientation
is now derived from which side is upstream, not chosen.

## P3 — multipoles (monopole removed)

| x_off/r_* | monopole | dipole | quadrupole |
|---|---|---|---|
| 1e-4 | +0.5134 | 1.296e-4 | 4.05e-9 |
| 1e-3 | +0.5134 | 1.296e-3 | 5.00e-7 |
| 1e-2 | +0.5134 | 1.296e-2 | 5.00e-5 |
| 1e-1 | +0.5154 | 1.292e-1 | 5.11e-3 |

Dipole coefficient **|c₁| = 1.2963 × (x_off/r_*)**; the transfer at P1's τ bound moves it by
6.8%, inside what the bound allows (LC5).

## P4 — confrontation, frozen rows only

| frozen row | bound on x_off/r_* |
|---|---|
| **B2.2** intrinsic-dipole limit \|Δ₁,int\| < 3.7 mK (95% CI) | **< 1.05e-3** |
| ℓ≥2 at the observed 1e-5 scale (B3 reports a deficit — conservative) | < 4.47e-3 |

**Binding bound: x_off / r_* < 1.05 × 10⁻³ — one part in 955.** The dipole row binds because
the pattern is dipole-dominated (LC6), which is the same correction my S3 already forced on S2.

## Where Phase 5 + 5b now stand

A boundary inside our last-scattering sphere requires the observer centred to ~0.1% of the
boundary radius. That is the **necessity** converse Phase 4's gates could not reach — crossing
does reveal the boundary — and it now rests on a repaired geometry (P1), a real transfer
integral (P2), monopole-correct normalisation (P3), and frozen observational rows (P4), rather
than on the withdrawn proxy and the withdrawn ppm claim.

## Honest note on my own checks

Three times this session a limiting-case check failed because I had written the CHECK wrong,
not because the physics was wrong: S1's upstream/downstream orientation, S1's no-jump
tautology, and now LC3's inverted sign of ΔT/T under blueshift. The physics survived each
time, but the pattern is real — I have been writing checks faster than I reason them. Every
instance is recorded in the scripts rather than silently repaired.

## Limits

Conditional on P1's blind double. σ = 1/3, pre-horizon, photon channel. Assumption ranges
A1–A6 enter only through τ, and τ's whole authorised range moves the answer by <10%.
