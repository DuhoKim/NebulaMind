# Brief: blind independent search for a dipole cancellation (seat: gpt1)

INDEPENDENT. Do NOT read p7_signed_sweep.py, P7_RECEIPT.md, p6_path_transfer.py, P6_*.md,
REGATE3_PHASE5B_VERDICT.md, or anything under platoon/gpt1_blind_p6/ (including your own
earlier work — this is a fresh question and prior framing would bias it).

## The question — and it is a yes/no with a location, not a confirmation task

An observer sits at comoving offset x_off from the centre of an FRW interior inside a black-hole
horizon. Sight lines cross a shock into a TOV exterior. The crossing imprints a temperature
anisotropy with (at least) two contributions: the Doppler factor at the junction, and the fact
that different directions cross at different epochs and therefore meet different exteriors.

**Does the resulting dipole vanish anywhere as the exterior's equation of state is varied?**

If it does, report WHERE (the value of w) and HOW WIDE the region is in which the dipole is too
small to constrain the offset at all. If it does not, say so and show why. Do not assume either
answer; I am not telling you which I found.

## GIVEN — pinned, use as stated
- metric: ds^2 = -B dtbar^2 + A^-1 drbar^2 + rbar^2 dOmega^2, A = 1 - N < 0, N = 2M/rbar;
  rbar is TIMELIKE; the fluid is comoving.
- field equations: pbar' = (pbar+rhobar)/2 N'/(N-1);  N' = -(N/rbar + kappa pbar rbar);
  B'/B = -(1/(N-1))(N/rbar + kappa rhobar).   kappa = 8 pi, G = c = 1.
- closure: pbar = w rhobar, w constant away from a narrow junction transition; the junction
  value is u/v from the data below. Sweep w over 0.005 to 0.999.
- gated orbit data: ../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv
  (t_over_tcrit, sqrtN_hubble_lengths, u_pbar_over_rho, v_rhobar_over_rho).
  At a crossing at conformal time eta: t=(eta/2)^2; rho_FRW=3/(32 pi t^2); rhobar=v*rho_FRW;
  pbar=u*rho_FRW; rbar_shock=2 t sqrtN; N_shock=sqrtN^2.
- eta = 2 sqrt(t); r_*(eta) = eta sqrtN(eta); crossing |x_off + chi n| = r_*(eta_obs - chi);
  observer at eta_obs = 2; relative fluid speed at a crossing beta = 1/sqrtN there.
- radiative transfer is BOLOMETRIC: intensities add, and a beam's bolometric weight goes as the
  fourth power of its frequency ratio.
- the exterior's source temperature follows the adiabatic law for the imposed equation of state.
- observational limit: intrinsic non-kinematic CMB dipole < 3.7 mK on T0 = 2.7255 K.

## YOU DECIDE, and justify in the README
- the observable normalisation; which radius normalises x_off; how you resolve any sign
  structure (sampling is explicitly insufficient — if you sample, say why that suffices);
  what threshold makes a dipole "too small to constrain anything", and why.

## Deliverables
Your script; README with each decision justified; a table of the SIGNED dipole coefficient
against w; the location and width of any cancellation; and your stability checks (quadrature
order, offset magnitude, integrator tolerance) demonstrating any null is not numerical.

Rules: write only in your directory; no commits. Marker: GPT1_P7_DONE.md (exact filename).
