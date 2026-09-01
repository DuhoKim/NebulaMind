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
BATTERY_POS_AHAT = 0.04243   # measured on the positive-control fixture (§4)
BATTERY_POS_P = 2.2e-21


def n_eq(var_cos, n=N):
    """Effective N in the dipole convention: full sky (Var=1/3) gives N_eq = N."""
    return 3.0 * n * var_cos


def sigma_A(n_eq_value, a=A_FLOOR):
    """Std error on the DEBIASED amplitude A.

    sigma_beta = 1/sqrt(N_eq) in this convention; dividing by the dilution
    (2a-1) to reach A inflates it. Detection (beta != 0) does NOT need a;
    only the amplitude scale does.
    """
    dilution = 2.0 * a - 1.0
    return 1.0 / (dilution * math.sqrt(n_eq_value))


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
    sig, snr, p = check_model_against_frozen_receipt()
    print(f"    sigma_A at N_eq={N_EQ_FROZEN:,}, a={A_FLOOR}  : {sig:.5f}")
    print(f"    frozen BATTERY-POS A_hat                    : {BATTERY_POS_AHAT}")
    print(f"    implied significance                        : {snr:.1f} sigma")
    print(f"    implied two-sided p                         : {p:.2e}")
    print(f"    frozen receipt p                            : {BATTERY_POS_P:.2e}")
    ok = 5.0 < snr < 20.0
    print(f"    -> model reproduces the receipt order-of-magnitude: {ok}")
    print("       (receipt p is from a permutation null, not this Gaussian;")
    print("        agreement to ~1 order of magnitude is the intended check)")

    print("\n[2] DETECTION FLOOR ON LONGO'S OWN AXIS (what the frozen footprint buys)")
    for a in (0.85, 0.90, 0.95, 1.00):
        s = sigma_A(N_EQ_FROZEN, a=a)
        print(f"    a={a:.2f}  sigma_A={s:.5f}   3-sigma floor A>={3*s:.4f} "
              f"({3*s*100:.2f}%)   5-sigma A>={5*s:.4f}")

    print("\n[3] LEVERAGE LOSS WHEN THE AXIS MOVES OFF LONGO'S")
    print("    psi = angle between the new (CMB) axis and the selection axis")
    print(f"    {'psi':>5} {'Var(cos)':>9} {'N_eq':>10} {'loss':>7} "
          f"{'sigma_A':>9} {'3sig floor':>11}")
    for psi in (0, 15, 30, 45, 60, 75, 90):
        v = var_cos_at_angle(psi)
        ne = n_eq(v)
        s = sigma_A(ne, a=A_FLOOR)
        loss = N_EQ_FROZEN / ne
        print(f"    {psi:>4}d {v:>9.4f} {ne:>10,.0f} {loss:>6.2f}x "
              f"{s:>9.5f} {3*s*100:>9.2f}%")

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
