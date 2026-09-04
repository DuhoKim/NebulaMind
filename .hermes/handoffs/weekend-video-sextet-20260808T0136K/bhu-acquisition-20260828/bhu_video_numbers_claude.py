#!/usr/bin/env python3
"""BHU video numbers, seat "claude". Every number Blanc may use must be printed here.

Scope: a receipted numbers note for a public explainer. No study, no tier movement.

INPUTS AND THEIR STATUS (see the note for line receipts):
  G, c        : exact/CODATA, cited
  H0          : Planck 2018 TT,TE,EE+lowE+lensing, 67.4 +/- 0.5 km/s/Mpc
  Omega_Lambda: Planck 2018, 0.6889
  M_sun, Mpc, ly : IAU / CODATA definitions, cited
Anything NOT reproducible from an equation plus these inputs is marked UNRECEIPTED in the output.
"""
import math

def P(k, v, unit=""):
    print(f"{k:<52} {v}{(' ' + unit) if unit else ''}")

def H(t):
    print(); print("=" * 96); print(t); print("=" * 96)

# ---------------------------------------------------------------- inputs
H("1. Inputs")
G      = 6.67430e-11          # CODATA 2018, m^3 kg^-1 s^-2
c      = 2.99792458e8         # exact by definition, m/s
Mpc    = 3.0856775814913673e22  # m, IAU
ly     = 9.4607304725808e15     # m, IAU
M_sun  = 1.98892e30           # kg
H0_kms = 67.4                 # Planck 2018
H0_err = 0.5
Om_L   = 0.6889               # Planck 2018
H0     = H0_kms * 1000.0 / Mpc
P("G  (CODATA 2018)", G, "m^3 kg^-1 s^-2")
P("c  (exact)", c, "m/s")
P("H0 (Planck 2018)", f"{H0_kms} +/- {H0_err}", "km/s/Mpc")
P("H0 in SI", f"{H0:.6e}", "s^-1")
P("Omega_Lambda (Planck 2018)", Om_L)
P("M_sun", f"{M_sun:.5e}", "kg")

# ---------------------------------------------------------------- the headline chain
H("2. Mass-energy inside the Hubble radius")
rho_c = 3 * H0**2 / (8 * math.pi * G)
R_H   = c / H0
M     = (4.0/3.0) * math.pi * rho_c * R_H**3
P("rho_c = 3 H0^2 / (8 pi G)", f"{rho_c:.4e}", "kg/m^3")
P("R_H = c/H0", f"{R_H:.5e}", "m")
P("R_H", f"{R_H/ly:.4e}", "light years")
P("R_H", f"{R_H/ly/1e9:.3f}", "billion light years")
P("M = (4/3) pi rho_c R_H^3", f"{M:.5e}", "kg")
P("M", f"{M/M_sun:.4e}", "solar masses")

# closed form, to show it is not a numerical accident
M_closed = c**3 / (2 * G * H0)
P("closed form  M = c^3 / (2 G H0)", f"{M_closed:.5e}", "kg")
P("agreement with the integral form", f"{abs(M-M_closed)/M:.3e}", "relative")

H("3. Schwarzschild radius of that mass")
R_s = 2 * G * M / c**2
P("R_s = 2GM/c^2", f"{R_s:.5e}", "m")
P("R_s", f"{R_s/ly:.4e}", "light years")
P("R_s", f"{R_s/ly/1e9:.3f}", "billion light years")

H("4. The ratio")
P("R_s / R_H", f"{R_s/R_H:.12f}")
P("R_s - R_H", f"{R_s-R_H:.3e}", "m  (floating-point residue only)")

# ---------------------------------------------------------------- the honest part
H("5. WHY it is exactly 1 -- algebra, not coincidence")
print("  Substitute rho_c = 3H0^2/(8 pi G) and R_H = c/H0 into M = (4/3) pi rho_c R_H^3:")
print()
print("      M = (4/3) pi * [3 H0^2 / (8 pi G)] * [c/H0]^3")
print("        = (4/3) * (3/(8G)) * c^3 / H0")
print("        = c^3 / (2 G H0)")
print()
print("  Then the Schwarzschild radius of THAT mass is")
print()
print("      R_s = 2GM/c^2 = (2G/c^2) * c^3/(2 G H0) = c/H0 = R_H .")
print()
print("  The G's, the c's and the 2 all cancel. R_s = R_H is an IDENTITY for any spatially flat")
print("  universe at critical density -- it is the Friedmann equation rearranged, not an")
print("  independent numerical coincidence. It would hold for ANY value of H0.")
print()
print("  Demonstration: recompute the ratio at H0 values spanning far more than the tension.")
for h in [50.0, 67.4, 73.0, 100.0, 500.0]:
    hh = h * 1000.0 / Mpc
    rc = 3 * hh**2 / (8 * math.pi * G)
    rh = c / hh
    mm = (4.0/3.0) * math.pi * rc * rh**3
    rs = 2 * G * mm / c**2
    print(f"    H0 = {h:6.1f} km/s/Mpc  ->  M = {mm/M_sun:.4e} Msun,  R_s/R_H = {rs/rh:.12f}")
print()
print("  The MASS changes with H0. The RATIO does not, ever.")

H("5b. What that means for the claim 'the numbers match, so we are inside a black hole'")
print("  The match is not evidence for the claim. Saying 'R_s equals R_H' is the same statement")
print("  as 'the universe is spatially flat at the critical density' -- which is what we measure")
print("  independently. Any flat critical-density universe reproduces it exactly, whether or not")
print("  it is inside anything. The coincidence has no work left to do once flatness is assumed.")

# ---------------------------------------------------------------- H0 tension
H("6. Does the H0 tension change the conclusion?")
for h, label in [(67.4, "Planck 2018 (CMB)"), (73.0, "local distance-ladder value")]:
    hh = h * 1000.0 / Mpc
    mm = c**3 / (2 * G * hh)
    print(f"  H0 = {h:5.1f} ({label:28s})  M = {mm:.4e} kg = {mm/M_sun:.3e} Msun,"
          f"  R_H = {c/hh/ly/1e9:.2f} Gly")
m67 = c**3/(2*G*(67.4*1000/Mpc)); m73 = c**3/(2*G*(73.0*1000/Mpc))
P("spread in M across the tension", f"{abs(m67-m73)/m67*100:.1f}", "%")
print("  => the tension moves the mass by about 8 per cent. It changes the last digit of the")
print("     quoted mass; it does not touch the ratio, which stays exactly 1.")

# ---------------------------------------------------------------- what the papers print
H("7. What the corpus's own papers print")
r_S_gaz = c / (H0 * math.sqrt(Om_L))
M_gaz   = c**2 * r_S_gaz / (2 * G)
print("  ENTRY 56 (Gaztanaga, MNRAS) abstract L29 and Eq. (21) L259: 'a mass M ~ 6 x 10^22 Msun'.")
print("  His r_S is NOT the Hubble radius: he sets Lambda = 3/r_S^2 (L28, L252), so")
print("      r_S = sqrt(3/Lambda) = c / (H0 sqrt(Omega_Lambda)).")
P("  r_S (Gaztanaga's definition)", f"{r_S_gaz:.5e}", "m")
P("  r_S / R_H", f"{r_S_gaz/R_H:.4f}")
P("  M_T = c^2 r_S / (2G)", f"{M_gaz/M_sun:.3e}", "solar masses")
P("  his printed value", "~6e22 solar masses")
P("  agreement", f"{M_gaz/M_sun/6e22:.3f}", "of his rounded figure")
print()
print("  SO: our 4.6e22 Msun and his 6e22 Msun are NOT in conflict -- they are different")
print("  quantities. Ours is the mass whose Schwarzschild radius equals the HUBBLE radius;")
print("  his is the mass whose gravitational radius equals the LAMBDA (de Sitter) radius,")
print("  larger by 1/sqrt(Omega_Lambda) = 1.20. Both follow from the same inputs.")
print()
print("  ENTRY 1 (Pathria 1972) L399-L405 prints a DIFFERENT identity again: R_s = R_max, the")
print("  Schwarzschild radius equal to the maximum expansion radius of a CLOSED (k=+1) universe,")
print("  'can hardly be a coincidence'. That is not the flat-universe identity computed here, and")
print("  Pathria states no mass value at that point. Our numbers neither confirm nor contradict it.")

# ---------------------------------------------------------------- receipts
H("8. Receipt status of every number above")
rows = [
 ("rho_c, R_H, M, R_s, R_s/R_H", "RECEIPTED", "equations printed above + the pinned inputs"),
 ("M in solar masses", "RECEIPTED", "M / M_sun, M_sun cited"),
 ("R_H, R_s in light years", "RECEIPTED", "IAU light year"),
 ("the 8% H0 spread", "RECEIPTED", "computed above from 67.4 vs 73.0"),
 ("Gaztanaga r_S, M_T", "RECEIPTED", "his Lambda = 3/r_S^2 (L28, L252) + Planck Omega_Lambda"),
 ("Gaztanaga's ~6e22 Msun", "QUOTED FROM SOURCE", "abstract L29, Eq. (21) L259"),
 ("Pathria R_s = R_max", "QUOTED FROM SOURCE", "L399-L405; no mass value printed there"),
 ("age of the universe", "NOT COMPUTED", "not needed; do not quote from this note"),
 ("number of atoms / stars", "NOT COMPUTED", "do not quote from this note"),
]
print(f"{'quantity':<34}{'status':<22}basis")
print("-" * 96)
for a,b,cc in rows:
    print(f"{a:<34}{b:<22}{cc}")
print()
print("BHU_VIDEO_NUMBERS_CLAUDE_SEAT_COMPLETE")
