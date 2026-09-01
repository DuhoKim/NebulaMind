#!/usr/bin/env python3
"""Axis-substitution leverage + power for the frozen Longo-amplitude machinery.

Question this answers, for the (B) amendment proposal ONLY:
if the frozen statistic is evaluated on a DIFFERENT pre-registered axis (a CMB
axis) instead of Longo's, how much detection power survives?

Uses ONLY public numbers quoted from the frozen text V134 (§2.6, §3, §4).
Touches NO sealed artifact, no object row, no chi sign, no label. Geometry
constants are quoted, not recomputed from data.

Frozen inputs (V134):
  N            = 49,211      accepted objects (BS-2f locked mask, §4)
  Var(cos t)   = 0.7517      post-exclusion, about LONGO'S axis (§4)
  N_eq         = 110,983     = 3*N*Var(cos t), floor 100,000 PASS (§4)
  A_LONGO      = 0.0408      our-convention Longo amplitude (§1)
  a_LB floor   = 0.85        calibration floor; below -> INCONCLUSIVE (§3)
  estimand     : E[s_obs|c] = (2a-1)*A_L*c ;  A_hat = beta_hat/(2a_hat-1) (§3)
  Var(beta)    = Var_pop(s)/((N-1)*Var_pop(c))  (§3)
"""

import math

N = 49_211
VAR_COS_LONGO = 0.7517
N_EQ_FROZEN = 110_983
A_LONGO = 0.0408
A_FLOOR = 0.85
POWER_FLOOR = 100_000        # frozen N_eq gate (§4); FAIL -> INCONCLUSIVE-BY-POWER
BATTERY_POS_AHAT = 0.04243   # measured on the positive-control fixture (§4)
BATTERY_POS_P = 2.2e-21


def n_eq(var_cos, n=N):
    """Effective N in the dipole convention: full sky (Var=1/3) gives N_eq = N."""
    return 3.0 * n * var_cos


def sigma_A(n_eq_value, a=A_FLOOR):
    """Std error on the DEBIASED amplitude A.

    CORRECTED 2026-09-01 after adversarial refutation (AMENDMENT_B_REFUTED).

    THE ERROR: this used sigma_beta = 1/sqrt(N_eq), treating N_eq as an inverse
    variance. It is not -- N_eq = 3*N*Var(cos) is a GATE THRESHOLD. The frozen
    text (V134 §3) defines the variance itself:
        Var(beta_hat) = Var_pop(s)/((N-1)*Var_pop(c))
    so with Var_pop(s) ~ 1 for s = +/-1,
        sigma_beta = 1/sqrt(N*Var(c)) = sqrt(3)/sqrt(N_eq).
    The old form was optimistic by exactly sqrt(3) = 1.732 at every axis.

    Consequence: the "model validation" this script originally reported was a
    coincidence produced BY the error. Under the correct variance no admissible
    a reproduces the receipt's ~9.5 sigma (5.71 at a=0.85, 8.16 even at a=1.0),
    so the Gaussian model does not in fact reproduce BATTERY-POS and must not be
    cited as if it did.
    """
    dilution = 2.0 * a - 1.0
    n_var_c = n_eq_value / 3.0          # N*Var(c), the real inverse variance
    return 1.0 / (dilution * math.sqrt(n_var_c))


def var_cos_at_angle(psi_deg, var_cos_ref=VAR_COS_LONGO):
    """Leverage of a NEW axis at angle psi from the selection axis.

    cos t' = cos(psi) cos t + sin(psi) sin t cos(phi).
    The selection is azimuthally symmetric about Longo's axis and symmetric in
    +/- cos t (polar |cos t| selection), so E[cos t] = 0 and the cross term
    vanishes under the phi average:
        Var(cos t') = cos^2(psi) Var(cos t) + sin^2(psi) E[sin^2 t]/2
    with E[sin^2 t] = 1 - E[cos^2 t] = 1 - Var(cos t).
    """
    psi = math.radians(psi_deg)
    e_sin2 = 1.0 - var_cos_ref
    return math.cos(psi) ** 2 * var_cos_ref + math.sin(psi) ** 2 * e_sin2 / 2.0


def check_model_against_frozen_receipt():
    """The model must reproduce the frozen positive control, or it is wrong."""
    sig = sigma_A(N_EQ_FROZEN, a=A_FLOOR)
    snr = BATTERY_POS_AHAT / sig
    p_two_sided = math.erfc(snr / math.sqrt(2.0))
    return sig, snr, p_two_sided


def main():
    print("=" * 72)
    print("AXIS-SUBSTITUTION LEVERAGE AND POWER  (frozen machinery, public numbers)")
    print("=" * 72)

    print("\n[1] MODEL CHECK against the frozen positive control (BATTERY-POS)")
    print("    *** THIS CHECK FAILS UNDER THE CORRECTED VARIANCE. Reported as a")
    print("    *** failure, not repaired away: the earlier PASS was produced by")
    print("    *** the sqrt(3) error it was supposed to catch.")
    sig, snr, p = check_model_against_frozen_receipt()
    print(f"    sigma_A at N_eq={N_EQ_FROZEN:,}, a={A_FLOOR}  : {sig:.5f}")
    print(f"    frozen BATTERY-POS A_hat                    : {BATTERY_POS_AHAT}")
    print(f"    implied significance                        : {snr:.2f} sigma")
    print(f"    implied two-sided p                         : {p:.2e}")
    print(f"    frozen receipt p                            : {BATTERY_POS_P:.2e} (~9.5 sigma)")
    snr_best = BATTERY_POS_AHAT / sigma_A(N_EQ_FROZEN, a=1.0)
    print(f"    best case a=1.0 (perfect classifier)        : {snr_best:.2f} sigma")
    print("    -> NO admissible a reproduces the receipt's ~9.5 sigma.")
    print("       The Gaussian model does NOT reproduce BATTERY-POS and cannot")
    print("       be cited as validation of the table below.")

    print("\n[2] DETECTION FLOOR ON LONGO'S OWN AXIS (what the frozen footprint buys)")
    for a in (0.85, 0.90, 0.95, 1.00):
        s = sigma_A(N_EQ_FROZEN, a=a)
        print(f"    a={a:.2f}  sigma_A={s:.5f}   3-sigma floor A>={3*s:.4f} "
              f"({3*s*100:.2f}%)   5-sigma A>={5*s:.4f}")

    print("\n[3] LEVERAGE LOSS WHEN THE AXIS MOVES OFF LONGO'S")
    print("    psi = angle between the new (CMB) axis and the selection axis")
    print("    GATE = the frozen power floor N_eq >= 100,000 (§4). The original")
    print("    version of this script never applied it. It is decisive.")
    print(f"    {'psi':>5} {'Var(cos)':>9} {'N_eq':>10} {'loss':>7} "
          f"{'sigma_A':>9} {'3sig floor':>11} {'GATE':>6}")
    for psi in (0, 15, 20, 30, 45, 50, 60, 75, 90):
        v = var_cos_at_angle(psi)
        ne = n_eq(v)
        s = sigma_A(ne, a=A_FLOOR)
        loss = N_EQ_FROZEN / ne
        gate = "PASS" if ne >= POWER_FLOOR else "FAIL"
        print(f"    {psi:>4}d {v:>9.4f} {ne:>10,.0f} {loss:>6.2f}x "
              f"{s:>9.5f} {3*s*100:>9.2f}% {gate:>6}")

    # where does the frozen gate stop admitting an axis?
    psi_max = None
    for tenth in range(0, 901):
        if n_eq(var_cos_at_angle(tenth / 10.0)) < POWER_FLOOR:
            psi_max = (tenth - 1) / 10.0
            break
    print(f"\n    -> the frozen N_eq floor admits ONLY psi <= {psi_max:.1f} degrees.")
    print("    Candidate CMB axes reported by the adversarial review sit at")
    print("    psi ~ 48-61 deg (hemispherical asymmetry 53.6, low-l alignment 49.9,")
    print("    kinematic dipole 61.1) -- NOT independently verified here, but all")
    print(f"    far beyond {psi_max:.1f} deg, so every one of them FAILS the frozen gate")
    print("    and the run would return INCONCLUSIVE-BY-POWER before any statistic.")

    print("\n[4] WHAT THIS MEANS FOR THE CONTESTED AMPLITUDE RANGE")
    print(f"    Longo's claimed amplitude   : {A_LONGO*100:.2f}%")
    print("    Shamir-class claims         : ~1-2%")
    worst = sigma_A(n_eq(var_cos_at_angle(90)), a=A_FLOOR)
    best = sigma_A(N_EQ_FROZEN, a=A_FLOOR)
    print(f"    3-sigma floor, aligned axis : {3*best*100:.2f}%  -> Longo range OK,"
          f" Shamir range {'OK' if 3*best*100 <= 2 else 'MARGINAL'}")
    print(f"    3-sigma floor, worst axis   : {3*worst*100:.2f}%  -> Longo range "
          f"{'OK' if 3*worst*100 <= 4.08 else 'LOST'},"
          f" Shamir range {'OK' if 3*worst*100 <= 2 else 'LOST'}")
    print("\n    NOTE: [3] assumes the footprint is azimuthally symmetric about")
    print("    Longo's axis and symmetric in +/-cos t. That is the DESIGN intent")
    print("    (polar |cos t| selection) but is NOT verified here against the real")
    print("    mask. The real Var(cos t') for a named CMB axis must be measured by")
    print("    the lane that owns the geometry. This is an upper bound on power,")
    print("    i.e. the honest case is no better than the table above.")
    print("=" * 72)


if __name__ == "__main__":
    main()
