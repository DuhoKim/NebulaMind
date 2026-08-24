# A2 receipt — past light cones of the off-center observer (2026-08-24 ~09:35 KST, Tori)

Script `a2_lightcones.py`, output `a2_zcross.csv` (738 rows), 5/5 checks. Reuses the A1-verified
integration (same equations, recomputed in-script; A1 was blind-double-confirmed this morning).

## A0 — proved, from the construction itself

The pinned solution matches a GIVEN, unmodified k=0 FRW metric to the TOV-interior metric
across the shock (S1 §4). The interior is therefore EXACT FRW: for any observer position, every
observable whose photons remain inside the FRW region is exactly isotropic and identical to
standard FRW. **All positional anisotropy is boundary-mediated**: it enters only through the
direction-dependent redshift z_c(n̂) at which each line of sight crosses the shock, and through
whatever lies beyond (TOV side — whose optics the paper does not model; carried as a limitation
to A3/Track C). The one non-geometric freedom is the observer's peculiar velocity (a kinematic
dipole, free in FRW too) — flagged for A3(c).

## Anchor correction absorbed

The paper's t₀ = FIRST VISIBILITY (photon from the Big-Bang shock reaching the center);
the N = 1 crossing is t_crit (A1 receipt addendum). From the A1 solution:
- r_*(0) = 1.05154 (comoving, units where eta_crit = 2) — the §7 free parameter, here fixed by
  the σ=1/3 orbit and the R(t_crit)=1 gauge.
- **t_crit/t_vis = 3.6175** — inside the paper's bound (6.3): [1.8, 4.5]. PASS.
- **√N₀ = 1.579** Hubble lengths at first visibility — inside §6's (1, 4.5]. PASS.
These two are nontrivial quantitative validations of the whole pipeline against the paper's own
theorems, not imposed anywhere in the code.

## Results — z_c(μ; x_off, t_obs) (μ = cos angle from the outward offset direction)

Headline numbers (t_obs = t_crit; x_off as fraction of the comoving shock radius r_*):

| x_off/r_* | z_c(nearest, μ=+1) | z_c(farthest, μ=−1) | full range |
|---|---|---|---|
| 0    | 2.550 | 2.550 | isotropic (null test: spread 0) |
| 0.05 | 2.178 | 3.014 | ±16% about the mean |
| 0.10 | 1.872 | 3.605 | order unity |
| 0.20 | 1.402 | 5.458 | — |
| 0.30 | 1.057 | 9.501 | — |
| 0.50 | shock already crossed in 1 of 41 directions (partial-sky) | | |

At earlier t_obs the effect is stronger (at t_obs = 0.5 t_crit, x_off/r_* = 0.2 spans z_c from
2.38 to over 1000); at t_vis a centered observer sees the shock in NO direction while any
offset observer already sees it over roughly half the sky — first visibility itself is
direction-dependent, nearest boundary first.

## What this means for A4 (stated carefully)

The boundary-crossing redshift is violently anisotropic for even percent-level offsets. So the
observable-scale confrontation will take the form: the observed sky is isotropic (to the known
anomalies) out to z ~ 1100, which requires z_c(μ) > z_obs in EVERY direction — a joint
constraint pushing (x_off/r_*) down and the boundary out. The prediction functions D(x_off,
t_obs) tabulated here are the raw material; converting z_c to real-universe epochs is where the
model's σ = 1/3 (radiation-only) limitation bites, and S1 itself calls these "only rough
qualitative models" — that caveat transfers verbatim into any Track C statement.

Checks: null test at x_off=0 exact; nearest-boundary-crosses-at-lower-z monotonicity; the two
§6 validations above. Pins: script+CSV sha256 in `_tmp_a2_shas.txt` at commit time.
