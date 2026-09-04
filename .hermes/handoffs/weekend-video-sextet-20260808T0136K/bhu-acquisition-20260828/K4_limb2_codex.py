#!/usr/bin/env python3
"""K4 limb-2 blind seat: codex.

GAUGE DECLARATION (before computation): use boundary-adapted Gaussian-normal
gauge at the comoving timelike surface Sigma.  Sigma is n=0, n is proper
distance along its normal, and h_nn=h_na=0 on Sigma.  Scalar interior modes
are matched to even-parity (polar) Schwarzschild modes; exterior statements
are equivalently expressible in Regge-Wheeler gauge through the Zerilli
master variable.  The displayed junction amplitudes are intrinsic to Sigma.

No CMB map, estimator, or planck_data asset is read by this script.
"""

from math import pi

CHI_CAUSAL_MPC = 14015.0
CAUSAL_H0_FACTOR = 3.149


def main() -> None:
    spacing = pi / CHI_CAUSAL_MPC
    print("SEAT=codex")
    print("GAUGE=boundary-adapted Gaussian-normal at Sigma (n=0; h_nn=h_na=0); exterior polar modes represented by the Zerilli variable")
    print("NO_PIXEL_INPUT=TRUE")
    print("BACKGROUND=k=0, Lambda=0, dust, comoving chi*=constant, R=a chi*, M=(4/3) pi chi*^3 rho0, Schwarzschild exterior, J_SMOOTH_EXPANDING")
    print("JUNCTION_DECOMPOSITION=h_tt=A_lm Y_lm; h_tA=B_lm Y_A; h_AB=R^2[K_lm Omega_AB Y_lm+G_lm Y_AB]")
    print("DARMOIS_FIRST_FORM=[A_lm]=[B_lm]=[K_lm]=[G_lm]=0 (retain only harmonics existing at that ell)")
    print("DARMOIS_SECOND_FORM=[d_n A_lm]=[d_n B_lm]=[d_n K_lm]=[d_n G_lm]=0 in Gaussian-normal gauge (same harmonic qualifications)")
    print("MULTIPOLE_STRUCTURE=rotational symmetry makes every (ell,m) match independently; it does not project onto ell=0")
    print("ELL0=matches the spherical density/mass perturbation to a constant exterior delta-M; background mass conservation supplies M but does not erase generic nonspherical modes")
    print("ELL1=even-parity vacuum dipole is center-of-mass/gauge data; regular matching fixes relative displacement/gauge, not all ell>=2 amplitudes")
    print("ELL_GE_2=Schwarzschild vacuum has a polar Zerilli master field with two real functional Cauchy data per (ell,m); Darmois relates its boundary value/normal derivative to the interior mode")
    print("BIRKHOFF=Birkhoff fixes only the exactly spherical exterior (ell=0) to Schwarzschild with constant mass; it says nothing that removes ell>=2 vacuum gravitational perturbations")
    print("FREE_MODE=for every ell>=2 and -ell<=m<=ell, arbitrary real finite-energy exterior Zerilli incoming/Cauchy data (two functions, subject to reality and regularity) remain unspecified")
    print("SPECTRUM=without an exterior state/no-incoming-radiation condition, Darmois supplies transmission data, not a homogeneous reflecting eigencondition; k remains continuous and no Delta-k is derived")
    print(f"CONDITIONAL_CAVITY_SPACING=pi/chi*; if chi*=chi_section={CHI_CAUSAL_MPC:.0f} Mpc then pi/chi*={spacing:.12e} Mpc^-1, but this spacing is NOT implied by Darmois")
    print(f"CAUSAL_SCALE=chi_section={CAUSAL_H0_FACTOR:.3f} c/H0={CHI_CAUSAL_MPC:.0f} Mpc")
    print("F1_COMPARISON=NO: the conditions act mode-by-mode, including ell>=2, rather than only on ell=0")
    print("F2_COMPARISON=NO: they equate boundary data across Sigma and do not impose W_tilde(k) delta_tilde(k)=0 or P=0")
    print("FREEDOM=exterior polar radiation state for every ell>=2; parameter space is arbitrary real finite-energy Zerilli Cauchy-data pairs, not a fixed numeric interval")
    print("LIMITS=dust only; exact spherical symmetry of the background; inherited 0<=Lambda<=Lambda_c (the selected B1 cell has Lambda=0)")
    print("CLASS=LIMB2_UNDETERMINED")


if __name__ == "__main__":
    main()
