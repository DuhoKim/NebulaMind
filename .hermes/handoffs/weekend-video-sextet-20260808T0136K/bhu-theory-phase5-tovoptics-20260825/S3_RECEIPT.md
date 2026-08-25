# S3 receipt — the confrontation, on frozen rows only
(2026-08-25, stamped from mtime at commit. s3_confrontation.py, log _tmp_s3_run.txt, 4/4 checks.)

## Multipole content of the crossing pattern (monopole excluded throughout)

| x_off/r_* | c₁ (dipole) | c₂ (quadrupole) | c₃ |
|---|---|---|---|
| 1e-4 | 1.296e-4 | 4.05e-9 | -1.02e-8 |
| 1e-3 | 1.296e-3 | 5.00e-7 | 2.27e-9 |
| 1e-2 | 1.296e-2 | 5.00e-5 | 1.18e-6 |
| 1e-1 | 1.292e-1 | 5.11e-3 | 1.18e-3 |

**The pattern is dipole-dominated**: c₁ ≈ 1.296 × (x_off/r_*), with c₂/c₁ ≈ 4×10⁻⁴. That fact
is what corrects S2 (see its amendment): the span cannot be compared against the ℓ≥2 anisotropy
scale, because most of the span IS the dipole.

## Confrontation — every observational number from the gated freeze, none new

| frozen row | value | bound on x_off/r_* |
|---|---|---|
| **B2.2** intrinsic-dipole limit, \|Δ₁,int\| < 3.7 mK (95% CI) | 1.358e-3 fractional | **< 1.05e-3** |
| B2.1 total solar dipole 3362.08 µK (context only) | 1.234e-3 | < 9.52e-4 |
| ℓ≥2 at the observed 1e-5 scale (B3 reports a deficit — conservative) | 1e-5 | < 4.47e-3 |

**Binding bound: x_off / r_* < 1.05 × 10⁻³**, from B2.2 — the correct row, because this effect
produces a genuinely NON-KINEMATIC dipole and is therefore not degenerate with our motion. B2.1
is quoted for context only; using it would double-count the kinematic interpretation the
frozen record still disputes (B2.5–B2.11), and Track C forbade taking a side in that dispute.

## What this establishes

A boundary inside our last-scattering sphere requires the observer within **~0.1% of the
boundary radius** of the exact centre — one part in ~950. Combined with S2b (the opaque branch
gives an order-0.6 contrast, 6×10⁴ times the anisotropy scale), **both branches of the τ ≈ 0.3
knife edge exclude a crossing sky at plausible offsets.** That is the necessity converse Phase
4 could not reach: crossing does reveal the boundary, unless a 1-in-950 centring is granted.

## Limits

σ = 1/3, pre-horizon, photon channel; kinematic branch assumes a shared radiation bath;
opaque branch assumes radiation-carried exterior energy; the Doppler sign convention affects
the mean shift's sign but not the span or the bounds; K4 (absolute brightness) remains
uncomputed and is not needed for any bound above.
