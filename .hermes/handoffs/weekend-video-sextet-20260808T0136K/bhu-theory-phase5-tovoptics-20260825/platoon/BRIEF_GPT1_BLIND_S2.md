# Brief: blind independent computation of Phase 5 S2 (seat: gpt1)

INDEPENDENT implementation. Do NOT read s2_transfer.py, S2_RECEIPT.md, S1_RECEIPT.md, or
s1_crossing_shift.py. Work only from the physics stated here.

## Task
For an observer displaced x_off (comoving) from the centre of the FRW interior in the
Smoller-Temple inside-a-black-hole shock cosmology (sigma = 1/3), compute the KINEMATIC
temperature pattern across the region of sky where the line of sight crosses the shock.

Physics given:
- The gated Phase 4 orbit is data: ../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv
  (columns S, sqrtN_hubble_lengths, u_pbar_over_rho, v_rhobar_over_rho, t_over_tcrit).
- Conformal time eta = 2 sqrt(t) (units t_crit). Comoving shock radius r_*(eta) = eta*sqrtN(eta).
- A sight line in direction n from the observer crosses the shock where
  |x_off + chi*n| = r_*(eta_obs - chi); mu is the cosine between n and the outward offset axis.
- At the crossing the two fluids (FRW interior, TOV exterior) have relative speed
  beta = 1/sqrt(N) evaluated at the crossing event. [Given to you; do not re-derive.]
- The relative motion is radial (along the shock normal at the crossing point).
- Kinematic temperature shift: the Doppler factor between the two fluid frames, projected on
  the ray's direction relative to the shock normal at the crossing point.

## Deliverables (in your directory)
1. Your script.
2. For observer epoch t_obs = t_crit and offsets x_off/r_* = 0.001, 0.01, 0.05, 0.1: the
   angular radius of the crossing region, and the kinematic Delta T / T across it (its range
   and its value at the region's centre and edge).
3. The maximum |Delta T / T| over those cases, and how it compares in order of magnitude with
   the observed CMB anisotropy amplitude of about 1e-5.
4. README: assumptions, your projection geometry, limiting-case checks you ran.

Rules: write only inside your directory; no commits. Marker: GPT1_S2_DONE.md when finished.
