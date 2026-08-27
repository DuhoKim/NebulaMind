#!/usr/bin/env python3
"""p9_hawking.py — can Hawking radiation test the black-hole-universe model?

Self-computing check (lane law: eval what you print). Every number quoted in
P9_HAWKING_RECEIPT.md is produced here. No claim is asserted in prose that is
not printed by this file.

Question posed by Duho, 2026-08-27: is Hawking radiation a route to testing /
proving BHU cosmology?

Structure:
  A. The horizon-mass identity (is the observable universe "inside" a BH?)
  B. The Hawking temperature of that mass, vs the de Sitter horizon temperature
     that ordinary LCDM already predicts  -> scale-distinctiveness (SUPPORTING ONLY)
  C. Wien wavelength vs the size of the observable universe -> structural test
  D. Energy density vs CMB, and evaporation timescale vs age -> amplitude test
  E. The "CMB *is* Hawking radiation" claim: what mass would that require?

REPAIR 2026-08-27, REGATE5 (CGATE_REGATE5_PHASE5B_VERDICT.md,
HOLD_HAWKING_DEGENERACY_OVERCLAIM). The first version of this file made B load-bearing and
called the exact factor of two a DEGENERACY that no horizon-temperature measurement could see
through. That was wrong and the gate was right: a factor of two is not a degeneracy. Two
distinct numbers, 1.326889e-30 K and 2.653778e-30 K, are distinguishable in principle by an
ideal thermometer of unlimited precision. The arithmetic below is unchanged and correct; only
the weight placed on it has been demoted.

B now claims exactly this and no more: the BHU figure sits at the SAME ħH/k_B scale that
standard cosmology already produces for its own horizon, so a horizon temperature "of order
ħH/k_B" is not by itself evidence for BHU. That is a distinctiveness argument, not a
no-discrimination argument.

The route remains closed, on the arguments that actually carry it:
  * NOT DEFINED FOR THIS MODEL (section E note + the receipt): T_H = ħc³/8πGMk_B presumes a
    vacuum Killing horizon with an asymptotic region. The audited exterior is a TOV fluid and
    the horizon is white-hole oriented. There is no sharp BHU number to compare against —
    the "prediction" is a property of the formula imported, not of the solution.
  * STRUCTURAL (C): the Wien wavelength exceeds the observable universe, so no apparatus
    inside our horizon can resolve one mode. This one is untouched by the gate.
  * AMPLITUDE (D): 1e-122 of the CMB, evaporation 1e125 Hubble times.
"""
import math

# --- CODATA 2018 / IAU constants (SI) ---------------------------------------
hbar  = 1.054571817e-34      # J s
c     = 2.99792458e8         # m/s
G     = 6.67430e-11          # m^3 kg^-1 s^-2
kB    = 1.380649e-23         # J/K
sigma = 5.670374419e-8       # W m^-2 K^-4
b_w   = 2.897771955e-3       # m K   (Wien displacement, peak in wavelength)
a_rad = 4.0 * sigma / c      # J m^-3 K^-4
Mpc   = 3.0856775814913673e22  # m
yr    = 3.15576e7            # s (Julian)
T_CMB = 2.72548              # K   (Fixsen 2009)
M_moon = 7.342e22            # kg
M_earth = 5.9722e24          # kg

CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))

def T_hawking(M):
    """Schwarzschild Hawking temperature."""
    return hbar * c**3 / (8.0 * math.pi * G * M * kB)

def r_s(M):
    return 2.0 * G * M / c**2

def t_evap(M):
    """Page/Hawking pure-photon-graviton evaporation time, standard prefactor."""
    return 5120.0 * math.pi * G**2 * M**3 / (hbar * c**4)

def S_horizon(M):
    """Bekenstein-Hawking entropy in units of k_B."""
    A = 4.0 * math.pi * r_s(M)**2
    return c**3 * A / (4.0 * hbar * G)

print("=" * 78)
print("p9_hawking.py -- Hawking radiation as a probe of BHU cosmology")
print("=" * 78)

for label, H0_kms in (("Planck-2018", 67.36), ("SH0ES", 73.04)):
    H0 = H0_kms * 1.0e3 / Mpc            # s^-1
    R_H = c / H0                          # Hubble radius, m
    rho_c = 3.0 * H0**2 / (8.0 * math.pi * G)

    print(f"\n--- {label}: H0 = {H0_kms} km/s/Mpc = {H0:.6e} 1/s ---")
    print(f"  Hubble radius R_H            = {R_H:.6e} m = {R_H/(1e3*Mpc):.4f} Gpc")
    print(f"  critical density rho_c       = {rho_c:.6e} kg/m^3")

    # ---- A. horizon-mass identity ------------------------------------------
    # Mass inside R_H at critical density.
    M_H = (4.0/3.0) * math.pi * R_H**3 * rho_c
    # Closed form: M = c^3 / (2 G H0)
    M_closed = c**3 / (2.0 * G * H0)
    print(f"\n  A. mass inside R_H at rho_c  = {M_H:.6e} kg")
    print(f"     closed form c^3/(2 G H0)  = {M_closed:.6e} kg")
    check("A1 mass integral == c^3/(2GH0)",
          abs(M_H - M_closed) / M_closed < 1e-12,
          f"rel.diff {abs(M_H-M_closed)/M_closed:.3e}")

    rs_MH = r_s(M_H)
    print(f"     Schwarzschild radius of that mass = {rs_MH:.6e} m")
    print(f"     r_s / R_H = {rs_MH/R_H:.12f}")
    check("A2 r_s(M_H) == R_H exactly (this is Omega=1, not a discovery)",
          abs(rs_MH/R_H - 1.0) < 1e-12,
          f"ratio-1 = {rs_MH/R_H - 1.0:.3e}")

    # ---- B. degeneracy with the de Sitter horizon temperature ---------------
    T_H = T_hawking(M_H)
    T_dS_H0 = hbar * H0 / (2.0 * math.pi * kB)          # Gibbons-Hawking at H0
    Omega_L = 0.6847                                     # Planck 2018
    H_L = H0 * math.sqrt(Omega_L)                        # asymptotic de Sitter rate
    T_dS_future = hbar * H_L / (2.0 * math.pi * kB)

    print(f"\n  B. [SUPPORTING ONLY — demoted at REGATE5; see the module docstring]")
    print(f"     T_Hawking(M_H)             = {T_H:.6e} K")
    print(f"     T_deSitter(H0)  = hH0/2pi  = {T_dS_H0:.6e} K")
    print(f"     ratio T_dS(H0)/T_H         = {T_dS_H0/T_H:.12f}")
    check("B1 both temperatures sit at the same hH/kB scale, differing by exactly 2",
          abs(T_dS_H0 / T_H - 2.0) < 1e-12,
          f"ratio = {T_dS_H0/T_H:.12f} — an O(1) factor, NOT a degeneracy: "
          f"an ideal thermometer could tell {T_H:.4e} K from {T_dS_H0:.4e} K")

    print(f"     asymptotic de Sitter T (H_L=H0*sqrt(Om_L)) = {T_dS_future:.6e} K")
    print(f"     ratio T_dS(future)/T_H     = {T_dS_future/T_H:.6f}")
    check("B2 so a horizon temperature 'of order hH/kB' is not by itself evidence for BHU",
          0.1 < T_dS_future / T_H < 10.0,
          f"ratio {T_dS_future/T_H:.4f} -> not a DISTINCTIVE prediction "
          f"(this is a distinctiveness claim, not a no-discrimination claim)")
    print(f"     NOTE: the BHU value is not even well-defined — T_H = hc^3/8piGMkB presumes a")
    print(f"     vacuum Killing horizon; the audited exterior is a TOV fluid and the horizon is")
    print(f"     white-hole oriented. B cannot carry the closure. C and E do.")

    # ---- C. structural test: is the quantum bigger than the box? -----------
    lam_peak = b_w / T_H
    print(f"\n  C. Wien peak wavelength       = {lam_peak:.6e} m")
    print(f"     observable-universe radius R_H = {R_H:.6e} m")
    print(f"     lambda_peak / R_H          = {lam_peak/R_H:.4f}")
    check("C1 Hawking wavelength EXCEEDS the observable universe",
          lam_peak > R_H,
          f"lambda_peak = {lam_peak/R_H:.2f} x R_H -- not one mode fits inside")

    # ---- D. amplitude and timescale ----------------------------------------
    u_H = a_rad * T_H**4
    u_CMB = a_rad * T_CMB**4
    print(f"\n  D. u_Hawking                  = {u_H:.6e} J/m^3")
    print(f"     u_CMB                      = {u_CMB:.6e} J/m^3")
    print(f"     u_Hawking / u_CMB          = {u_H/u_CMB:.6e}")
    check("D1 Hawking energy density is >100 orders below the CMB",
          u_H / u_CMB < 1e-100,
          f"ratio {u_H/u_CMB:.3e}")

    te = t_evap(M_H)
    age = (2.0/3.0) / H0   # order-of-magnitude matter-era age; only used as a scale
    print(f"     evaporation time           = {te/yr:.6e} yr")
    print(f"     ~Hubble time               = {(1.0/H0)/yr:.6e} yr")
    print(f"     t_evap / t_Hubble          = {te*H0:.6e}")
    check("D2 evaporation is irrelevant on any cosmological timescale",
          te * H0 > 1e100,
          f"t_evap = {te*H0:.3e} Hubble times")

    print(f"     horizon entropy S/k_B      = {S_horizon(M_H):.6e}")

# ---- E. the "CMB is Hawking radiation" claim -------------------------------
print("\n" + "=" * 78)
print("E. If the CMB WERE the Hawking radiation of the universe's horizon,")
print("   what mass and horizon size would that require?")
print("=" * 78)
M_needed = hbar * c**3 / (8.0 * math.pi * G * kB * T_CMB)
print(f"  required mass       = {M_needed:.6e} kg")
print(f"                      = {M_needed/M_moon:.4f} lunar masses")
print(f"                      = {M_needed/M_earth:.6f} Earth masses")
print(f"  required r_s        = {r_s(M_needed):.6e} m = {r_s(M_needed)*1e6:.2f} micrometres")
check("E1 a 2.72548 K Hawking source is sub-planetary with a micron-scale horizon",
      M_needed < M_earth and r_s(M_needed) < 1e-3,
      f"{M_needed/M_moon:.3f} M_moon, r_s = {r_s(M_needed)*1e6:.1f} um")
H0p = 67.36 * 1e3 / Mpc
check("E2 that mass is >30 orders below the observable-universe mass",
      (c**3/(2*G*H0p)) / M_needed > 1e30,
      f"M_H/M_needed = {(c**3/(2*G*H0p))/M_needed:.3e}")

# ---- summary ---------------------------------------------------------------
print("\n" + "=" * 78)
npass = sum(1 for _, ok, _ in CHECKS if ok)
print(f"SELF-CHECKS: {npass}/{len(CHECKS)} passed")
print("=" * 78)
raise SystemExit(0 if npass == len(CHECKS) else 1)
