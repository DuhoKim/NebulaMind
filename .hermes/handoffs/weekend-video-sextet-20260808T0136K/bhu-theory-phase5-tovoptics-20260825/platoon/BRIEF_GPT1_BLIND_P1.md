# Brief: blind independent computation of Phase 5b P1 (seat: gpt1)

INDEPENDENT. Do NOT read p1_optical_depth.py, P1_RECEIPT.md, S0_*, or any earlier optical-depth
file in the parent directory — an earlier attempt was WITHDRAWN as wrong and reading it would
contaminate you. Work only from the physics below.

## Task
Compute the optical depth to Thomson scattering along a null ray through the TOV interior of
the Smoller-Temple inside-a-black-hole shock cosmology.

Geometry (pinned, arXiv astro-ph/0210105, section 3):
  ds^2 = -B(rbar) dtbar^2 + A^-1(rbar) drbar^2 + rbar^2 dOmega^2,  A = 1 - N(rbar) < 0,
  N = 2M/rbar. Because A < 0, rbar is the TIMELIKE variable. The fluid is comoving.
Field equations (pinned, 3.2-3.3):
  pbar' = (pbar + rhobar)/2 * N'/(N-1)
  N'    = -( N/rbar + kappa pbar rbar ),  kappa = 8 pi  (G = c = 1)
Closure: assume pbar = w rhobar with constant w; carry w over a range including 0.2456.
Starting point (the crossing our past light cone reaches, from the gated Phase 4 orbit
../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv, the row minimising
|2 - 2 sqrt(t)(1 + sqrtN)|):
  rho_FRW = 3/(32 pi t^2);  rhobar_s = v * rho_FRW;  pbar_s = u * rho_FRW;
  rbar_s = 2 t sqrtN;  N_s = sqrtN^2.
Electron density: n_e = f_b * Y_e * rhobar / m_p, with f_b (baryon rest-mass fraction of
rhobar) and Y_e carried as assumption ranges.

## Deliverables (your directory)
1. Your derivation of the invariant optical-depth element for a null ray in THIS geometry,
   stated explicitly (do not assume a Euclidean column length — rbar is timelike).
2. Your script.
3. tau integrated from the shock to the horizon (N -> 1), tabulated over w in {0.001, 0.05,
   0.2456, 0.30} and f_b in {1, 0.1, 0.01}, both in geometric units and converted to physical
   units for an anchor t_crit = 4.35e17 s.
4. Whether the integral converges at N -> 1, shown not asserted.
5. README with assumptions and limiting-case checks.

Rules: write only in your directory; no commits. Marker: GPT1_P1_DONE.md.
