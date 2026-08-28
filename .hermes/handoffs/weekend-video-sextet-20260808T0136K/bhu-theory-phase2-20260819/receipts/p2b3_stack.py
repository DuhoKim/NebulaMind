"""p2b3-R2: the stack — maximal rotating-parent handedness amplitude under the B2 ceiling.
Two independent stack forms, all assumptions named; treatment fork carried.
STACK A (spec-chain form): omega_0 <= (eps*f_b)_max * Omega_H / D with (eps f_b) <= eps_max
 (B2 ceiling; the roof applies to the eps*f_b product per B2 A5 row / inherit-gate note),
 Omega_H(10 Msun, a*=0.7) = 4.144e3 s^-1 (Phase 1 inversion receipt, gate-passed),
 D >= Z_mat^2 = (1+z_eq)^2, z_eq = 3400 [standard value, flagged; Z_rad, Z_inf >= 1 dropped
 — maximally generous]. Then A = C (omega/H)(z_ta) with the Phase 1 gated transfer
 (C = 7.19 [1.36,12.78]; (1+z)^2/E(z) = 3.50 at z_ta = 3).
STACK B (angular-momentum form, no D): L conserved after bounce (spec A2/A7 named);
 J_b <= xi M c R_b (B2 ceiling); today omega_0 = J_b/I_today, I_today = xi M_univ a_0^2
 with M_univ = eps_c * 2 pi^2 a_0^3 / c^2 (closed 3-sphere at critical density; using the
 PLB-chain a_0 = 2.95e27 m; Hubble-volume-only I would only RAISE omega_0 -> conservative).
Floors: design 3-sigma 9.5e-3; all-sky 1-sigma 7.07e-7 (Phase 0/1 pins).
Gate-corrected slivers restated: Treatment I 5.1e-13; Treatment II matched-input (nit N2)."""
import math
G, c, hbar, kB = 6.67430e-11, 2.99792458e8, 1.054571817e-34, 1.380649e-23
Msun = 1.989e30
H0 = 1/4.4e17
OmegaH = 4.144e3
eps_max = {"I": 1.51e-27, "II": 1.36e-26}
Rb = {"I": 3.91e-23, "II": 3.52e-22}
T_b = {"I": kB*1.152e32, "II": 0.785*math.sqrt(hbar*c**5/(8*math.pi*G))}
zeq = 3400
C_headline, C_hi = 7.19, 12.78
zmap = 3.50   # (1+z)^2/E(z) at z_ta = 3 (Phase 1 W, gated)
floor_design, floor_allsky = 9.5e-3, 7.07e-7
print("STACK A (spec-chain, D >= Z_mat^2 only — maximally generous):")
for t in ("I", "II"):
    w0 = eps_max[t]*OmegaH/(1+zeq)**2
    wh = w0/H0
    A = C_headline*zmap*wh
    A_hi = C_hi*zmap*wh
    print(f"  Treatment {t}: omega_0 <= {w0:.2e} s^-1; (w/H)_0 <= {wh:.2e}; "
          f"A <= {A:.1e} (C-bracket top {A_hi:.1e})")
    print(f"    vs all-sky 1-sigma floor: A/floor = {A/floor_allsky:.1e}; vs design 3-sigma: {A/floor_design:.1e}")
print("STACK B (angular momentum, no D):")
eps_c = 3*H0**2*c**2/(8*math.pi*G)
a0 = 2.95e27
xi = 0.4
M_univ = eps_c*2*math.pi**2*a0**3/c**2
I_today = xi*M_univ*a0**2
for t in ("I", "II"):
    for Mfac in (10,):
        M = Mfac*Msun
        Jb = xi*M*c*Rb[t]
        w0 = Jb/I_today
        wh = w0/H0
        A = C_headline*zmap*wh
        print(f"  Treatment {t}, {Mfac} Msun: J_b <= {Jb:.2e} J s; omega_0 <= {w0:.2e} s^-1; "
              f"(w/H)_0 <= {wh:.2e}; A <= {A:.1e}")
print(f"  (M_univ = {M_univ:.2e} kg; I_today = {I_today:.2e} kg m^2; larger closed volume or")
print(f"   supermassive parents only lower A further: eps_max ~ M^(-2/3), J_b ~ M^(4/3), I fixed)")
# supermassive check for stack B: J_b ∝ M * R_b ∝ M^{4/3}
M = 1e9*Msun; Jb9 = xi*M*c*(Rb["I"]*(1e8)**(1/3))
print(f"  supermassive 1e9 Msun (I): J_b <= {Jb9:.2e}; omega_0 <= {Jb9/I_today:.2e} s^-1 (still absurdly small)")
# gate-corrected slivers
Om_max = {t: c/Rb[t] for t in ("I","II")}
for t in ("I","II"):
    print(f"polarization sliver, matched inputs ({t}): hbar*(c/R_b)/k_B T_b = {hbar*Om_max[t]/T_b[t]:.1e}")
