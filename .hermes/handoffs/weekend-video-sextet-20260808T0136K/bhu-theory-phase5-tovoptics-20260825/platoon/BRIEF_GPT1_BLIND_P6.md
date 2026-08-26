# Brief: blind independent computation of Phase 5b P6 (seat: gpt1)

INDEPENDENT. Do NOT read p6_path_transfer.py, P6_RECEIPT.md, p5_joint_exclusion.py,
P5_JOINT_RECEIPT.md, or anything under platoon/gpt1_blind_p5/. Parts of the earlier line are
WITHDRAWN and reading them would contaminate you. Work only from what is below.

## The situation

An observer sits at comoving offset x_off from the centre of an FRW interior. Sight lines cross
a shock into a TOV exterior that lies INSIDE a black-hole horizon, where the areal radius rbar
is the TIMELIKE coordinate. Compute the sky anisotropy the crossing produces, and the bound
that the published limit on a non-kinematic CMB dipole places on x_off.

GIVEN — pinned, use as stated:
- metric: ds^2 = -B(rbar) dtbar^2 + A^-1(rbar) drbar^2 + rbar^2 dOmega^2, A = 1 - N < 0,
  N = 2M/rbar. rbar is timelike; the fluid is comoving.
- field equations: pbar' = (pbar+rhobar)/2 * N'/(N-1); N' = -(N/rbar + kappa pbar rbar);
  B'/B = -(1/(N-1)) (N/rbar + kappa rhobar).   kappa = 8 pi, G = c = 1.
- gated orbit data (crossing conditions and shock state):
  ../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv
  (t_over_tcrit, sqrtN_hubble_lengths, u_pbar_over_rho, v_rhobar_over_rho).
  At a crossing at conformal time eta: rho_FRW = 3/(32 pi t^2) with t = (eta/2)^2;
  rhobar = v*rho_FRW; pbar = u*rho_FRW; rbar_shock = 2 t sqrtN; N_shock = sqrtN^2.
- conformal time eta = 2 sqrt(t); comoving shock radius r_*(eta) = eta sqrtN(eta);
  crossing condition |x_off + chi n| = r_*(eta_obs - chi); observer at eta_obs = 2.
- the two fluids' relative speed at a crossing is beta = 1/sqrtN there.
- closure: assume pbar = w rhobar with w constant away from a narrow junction transition;
  sweep w over 0.01 to 0.999 (the junction value is u/v).
- observational limit: intrinsic non-kinematic CMB dipole < 3.7 mK on T0 = 2.7255 K.

## TO BE DECIDED BY YOU — do not ask, choose and justify in your README

1. **What does a sight line that crosses the shock actually terminate on?** Does radiation from
   beyond the exterior reach the observer, and if so at what strength? Derive it; do not assume.
2. Whether emission from different DEPTHS in the exterior arrives with different weight, and if
   so what sets that weight. (The metric function B is given above for a reason; whether you
   need it is your call.)
3. The observable normalisation, given all directions may share a large common factor.
4. Which radius normalises x_off, and why.
5. Whether the anisotropy strengthens, weakens, saturates, or behaves non-monotonically as the
   exterior becomes opaque — report what you find, including any non-monotonicity, rather than
   fitting a trend.

## Deliverables
Your script; a README stating each decision above with its derivation; the dipole coefficient
and the bound on x_off as functions of w across the swept range; and your limiting-case checks.
State plainly whether the crossing region is brighter, dimmer, or comparable to the surrounding
sky, and why.

Rules: write only inside your directory; no commits. Marker: GPT1_P6_DONE.md (exact filename).
