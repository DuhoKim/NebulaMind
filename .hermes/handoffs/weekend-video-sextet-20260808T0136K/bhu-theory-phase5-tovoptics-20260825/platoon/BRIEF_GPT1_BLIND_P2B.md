# Brief: blind independent computation of Phase 5b P2b (seat: gpt1)

INDEPENDENT. Do NOT read p2b_transfer_sweep.py, p2p4_transfer_confront.py, P1B_P2B_RECEIPT.md,
P2_P4_RECEIPT.md, or any S2/S3 file — parts of that earlier line are WITHDRAWN and reading them
would contaminate you.

## The question (not the closure — choose and justify these yourself)
An observer sits at comoving offset x_off from the centre of the FRW interior; sight lines cross
the shock into the TOV exterior. Compute the resulting sky anisotropy and the bound that the
published limit on a non-kinematic CMB dipole places on x_off.

GIVEN (use these):
- gated orbit data: ../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv
  (t_over_tcrit, sqrtN_hubble_lengths, v_rhobar_over_rho).
- conformal time eta = 2 sqrt(t); comoving shock radius r_*(eta) = eta sqrtN(eta);
  crossing condition |x_off + chi n| = r_*(eta_obs - chi).
- the relative speed of the two fluids at the crossing is beta = 1/sqrtN there.
- optical depth of the exterior lies somewhere in 0 to 0.15 (an independently derived range).
- observational limit: intrinsic (non-kinematic) CMB dipole < 3.7 mK on T0 = 2.7255 K.

TO BE CHOSEN AND JUSTIFIED BY YOU (do not ask me; state your choice and why):
- how the observable anisotropy should be normalised given that all directions share a large
  common shift;
- what source function the exterior contributes when it is partially opaque, and what bounds it;
- which multipole the published dipole limit constrains, and whether that is the binding one.

## Deliverables
1. Your script and a README stating every choice above with its justification.
2. The dipole coefficient per unit x_off/r_*, and the resulting bound on x_off/r_*, reported
   across whatever ranges your choices imply.
3. Limiting-case checks you ran.

Rules: write only in your directory; no commits. Marker: GPT1_P2B_DONE.md.
