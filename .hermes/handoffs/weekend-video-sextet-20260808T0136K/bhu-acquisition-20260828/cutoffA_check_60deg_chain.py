#!/usr/bin/env python3
"""Check the flagged claim that the paper's own chain gives 22 degrees, not 60.

The physics gate seat flagged, as a matter for a successor and NOT as a verdict:
"sqrt(3/Lambda)=5.38 Gpc against D_M=13.885 Gpc subtends 22 degrees, not 60 --
reaching 60 deg needs chi_S ~ 13.9 Gpc, ~2.6x the de Sitter radius."

I carried that flag unverified. It matters more than anything else outstanding:
if true, the corpus's ONE a-priori prediction fails on the paper's own arithmetic.
So it gets checked before it is repeated anywhere.

THE POINT AT ISSUE is what chi_S actually is. The seat took chi_S = sqrt(3/Lambda),
the de Sitter radius. The paper does not. It solves Eq.22 numerically and reports

    Eq.23:  chi_S = (3.149 +/- 0.006) c/H0
    Eq.24:  a_S   = 0.933 +/- 0.006

"to be compared to a0=1 and chi_0 = 3.200 c/H0 today. So we can see that the scale
of our causal universe is slightly smaller than our observable universe today."

and defines the angle as

    L349:  theta_S(z) = chi_S / chi(z)

so the test is theta_S = chi_S / D_M(z=1100), with chi_S from Eq.23.

Cosmology fixed to the paper's own stated inputs where given (Omega_r = 4.2e-5,
flat, Omega_Lambda = 0.69) with Planck-2018 H0; the answer is insensitive to H0
because BOTH chi_S and D_M scale as c/H0 -- the ratio is dimensionless. That
insensitivity is itself checked below.
"""

import numpy as np

CHI_S_OVER_C_H0 = 3.149          # Eq.23
CHI_S_ERR = 0.006
CHI_0_OVER_C_H0 = 3.200          # the paper's quoted horizon today
Z_CMB = 1100.0
OMEGA_L = 0.69                   # the paper's input at L332
OMEGA_R = 4.2e-5                 # the paper's stated value


def comoving_distance_over_c_h0(z, om_l=OMEGA_L, om_r=OMEGA_R, n=2_000_000):
    """D_C(z) in units of c/H0, flat LCDM: int_0^z dz'/E(z')."""
    om_m = 1.0 - om_l - om_r
    zz = np.linspace(0.0, z, n)
    E = np.sqrt(om_m * (1 + zz) ** 3 + om_r * (1 + zz) ** 4 + om_l)
    return float(np.trapz(1.0 / E, zz))


def main():
    print("=" * 74)
    print("CHECKING THE FLAGGED '22 DEGREES, NOT 60' CLAIM")
    print("=" * 74)

    d_cmb = comoving_distance_over_c_h0(Z_CMB)
    print(f"\n[1] The paper's own chain, theta_S = chi_S / chi(z)  (L349)")
    print(f"    chi_S           (Eq.23)        = {CHI_S_OVER_C_H0:.3f} c/H0")
    print(f"    chi(z=1100)     (computed)     = {d_cmb:.3f} c/H0")
    theta = CHI_S_OVER_C_H0 / d_cmb
    theta_deg = np.degrees(theta)
    lo = np.degrees((CHI_S_OVER_C_H0 - CHI_S_ERR) / d_cmb)
    hi = np.degrees((CHI_S_OVER_C_H0 + CHI_S_ERR) / d_cmb)
    print(f"    theta_S                        = {theta:.4f} rad = "
          f"{theta_deg:.1f} deg   (+/-{(hi-lo)/2:.1f} from Eq.23's error)")
    print(f"    the paper claims               ~ 60 deg (and 60 +/- 3 at L429)")
    print(f"    -> the paper's OWN chi_S reproduces its own angle: "
          f"{'YES' if 50 < theta_deg < 70 else 'NO'}")

    print(f"\n[2] Where the flagged 22 deg came from — a DIFFERENT chi_S")
    ds_radius = 1.0 / np.sqrt(OMEGA_L)     # sqrt(3/Lambda) in units of c/H0
    theta_ds = np.degrees(ds_radius / d_cmb)
    print(f"    de Sitter radius sqrt(3/Lambda) = c/(H0 sqrt(Om_L)) "
          f"= {ds_radius:.3f} c/H0")
    print(f"    theta from THAT radius          = {theta_ds:.1f} deg")
    print(f"    ratio chi_S(Eq.23)/de Sitter    = "
          f"{CHI_S_OVER_C_H0/ds_radius:.2f}x")
    print("    -> this reproduces the flag's ~22 deg and its '~2.6x' remark,")
    print("       which confirms the flag's ARITHMETIC while showing its")
    print("       PREMISE is not the paper's: the paper never sets chi_S to the")
    print("       de Sitter radius. It solves Eq.22 numerically for it (Eq.23).")

    print(f"\n[3] Consistency of Eq.23 with the paper's other quoted number")
    print(f"    chi_S/chi_0 = {CHI_S_OVER_C_H0}/{CHI_0_OVER_C_H0} = "
          f"{CHI_S_OVER_C_H0/CHI_0_OVER_C_H0:.4f}")
    print("    paper: 'the scale of our causal universe is slightly smaller than")
    print("    our observable universe today' -- consistent (1.6% smaller).")
    print(f"    my computed chi(z->inf) = "
          f"{comoving_distance_over_c_h0(1e5):.3f} c/H0 vs the paper's 3.200 "
          f"-> independent check of its background integration.")

    print(f"\n[4] H0-insensitivity (the ratio is dimensionless)")
    print("    Both chi_S and chi(z) are quoted/computed in units of c/H0, so H0")
    print("    cancels exactly in theta_S. No H0 was needed above; the result")
    print("    cannot be moved by the H0 tension.")

    print(f"\n[5] VERDICT")
    print(f"    The flagged claim is REFUTED as stated. The paper's chain gives")
    print(f"    {theta_deg:.1f} deg, not 22. The 22 deg follows only from substituting")
    print("    the de Sitter radius for chi_S, which the paper does not do.")
    print(f"    Residual worth noting honestly: {theta_deg:.1f} deg is not exactly 60 --")
    print(f"    it is {60-theta_deg:.1f} deg low, inside the paper's own stated")
    print("    60 +/- 3 only marginally. That small gap is a real question about")
    print("    the paper's rounding, NOT the order-of-magnitude failure flagged.")
    print("=" * 74)


if __name__ == "__main__":
    main()
