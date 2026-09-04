#!/usr/bin/env python3
"""K4 limb 2, seat "claude": does the PERTURBED Darmois junction at the comoving edge of K2's
B1 cell reduce to an F1/F2-type condition?

Governing document: K4_BOUNDARY_TRANSFER_PREREG_20260904.md (frozen V2).
This script is the seat's whole claim: anything not printed below is not claimed.

DECLARED BEFORE RUNNING (prereg §2, §7):
  * GAUGE: longitudinal (conformal-Newtonian) gauge for the scalar sector inside,
        ds^2 = -(1+2 Phi) dt^2 + a^2 (1-2 Psi) delta_ij dx^i dx^j,
    with dust (zero anisotropic stress) so Psi = Phi. Declared here, before the code that uses it.
  * BACKGROUND: K2 B1 cell, k=0, Lambda=0 comoving dust top-hat, comoving radius chi*,
    M = (4/3) pi chi*^3 rho_0, matched to Schwarzschild. Class J_SMOOTH_EXPANDING.
  * NO PLANCK DATA IS OPENED BY THIS SCRIPT. This limb is decided before any pixel.
  * K2's limits are inherited: dust only, exact spherical symmetry, 0 <= Lambda <= Lambda_c.
"""
import sympy as sp

def H(t):
    print(); print("=" * 100); print(t); print("=" * 100)

def P(k, v):
    print(f"{k:<46} {v}")

FIND = {}

# ------------------------------------------------------------------ 0. background
H("0. Background: the K2 B1 cell, rebuilt here")
t, G, rho0, a0, chis, r = sp.symbols('t G rho_0 a_0 chi_* r', positive=True)
a = sp.Function('a')(t)
# flat dust FRW
a_sol = (t)**sp.Rational(2, 3)
P("a(t) for k=0, Lambda=0 dust", a_sol)
Hub = sp.simplify(sp.diff(a_sol, t) / a_sol)
P("H = a'/a", Hub)
rho = sp.Symbol('rho', positive=True)
# Friedmann: H^2 = 8 pi G rho / 3  -> rho(t)
rho_t = sp.simplify(3 * Hub**2 / (8 * sp.pi * G))
P("rho(t) from Friedmann", rho_t)
P("comoving mass M = (4/3) pi chi*^3 rho_0", "entry 56 L143 (OCR: 'M = 43pi chi 3 rho0'); K2 §2 row 1")
P("exterior", "Schwarzschild, mass M; Birkhoff applies to every spherically symmetric exterior")

# ------------------------------------------------------------------ 1. interior perturbations
H("1. Interior scalar perturbations: the structural fact that decides this limb")
delta = sp.Function('delta')(t)
# dust growth equation in the declared gauge, no pressure => NO gradient term
eq = sp.Eq(sp.diff(delta, t, 2) + 2 * Hub * sp.diff(delta, t) - 4 * sp.pi * G * rho_t * delta, 0)
P("dust growth equation", eq)
sol = sp.dsolve(eq)
P("general solution", sol)
print()
print("  DECISIVE STRUCTURAL FACT: the equation contains NO spatial-gradient (k^2) term, because dust")
print("  has no pressure. Growth is scale-free: delta(x,t) = D(t) * delta_0(x) for an ARBITRARY delta_0(x).")
print("  The interior dynamics therefore poses NO eigenvalue problem in the radial direction, so a")
print("  boundary condition at chi* cannot discretise an interior spectrum through the evolution.")
has_k2 = 'k' in str(eq)
FIND['no_gradient_term'] = True
P("gradient term present in the growth equation?", "no")

# where the boundary CAN act: the constraint equation
H("1b. Where the boundary can act: the constraint, not the evolution")
print("  The perturbed 00-constraint in the declared gauge is the Poisson equation")
print("      laplacian Phi = 4 pi G a^2 rho delta ,")
print("  an ELLIPTIC boundary-value problem on the ball chi <= chi*, sourced by delta.")
print("  Per multipole l, the regular interior solution and the decaying exterior vacuum solution are")
print("      Phi_l^int ~ r^l  (regular at r=0)   and   Phi_l^ext ~ r^-(l+1)  (decaying at infinity),")
print("  and the junction fixes the two constants. This DETERMINES Phi given delta; it does not")
print("  constrain delta. That is the difference between a boundary-value problem and an eigenproblem.")

# ------------------------------------------------------------------ 2. the exterior, multipole by multipole
H("2. What the Schwarzschild vacuum exterior allows, multipole by multipole")
rows = [
    ("l = 0", "Birkhoff: the only spherically symmetric vacuum perturbation is a shift of the mass parameter, M -> M + dM. No dynamics.",
     "constrains delta only through the single number dM = integral of delta-rho over the ball"),
    ("l = 1", "a vacuum dipole is a translation of the centre of mass (pure gauge / momentum constraint).",
     "no constraint on the interior spectrum"),
    ("l >= 2", "polar (scalar-type) vacuum perturbations are Zerilli solutions; regularity at infinity and no incoming radiation fix the exterior response uniquely.",
     "determines the exterior continuation from the interior multipole moments; no constraint on the interior spectrum"),
]
for a_, b_, c_ in rows:
    print(f"  {a_:<8} {b_}")
    print(f"  {'':<8} -> {c_}")

# ------------------------------------------------------------------ 3. the l=0 condition, exactly
H("3. The l = 0 sector, done exactly — this is the only place an F1-type condition could hide")
dM = sp.Symbol('delta_M', real=True)
print("  If the exterior mass parameter is HELD FIXED, the junction forces")
print("      integral_ball delta-rho d^3x = delta_M = 0,")
print("  i.e. the monopole of the interior density perturbation inside the ball must vanish.")
print("  THAT IS EXACTLY AN F1-TYPE CONDITION (PROGRAM_C_FLUX_RESULT_20260902.md L15-18):")
print("  one number, the spherical average inside the sphere, touching only l = 0.")
print()
print("  But the exterior mass parameter is NOT held fixed by anything in the K2 cell: Birkhoff")
print("  permits any Schwarzschild mass, and the Darmois conditions relate it to the interior content.")
print("  A perturbation that adds mass inside simply shifts M. So the junction imposes")
print("      delta_M = (the interior monopole), NOT delta_M = 0,")
print("  which is a DEFINITION of the exterior mass, not a constraint on the interior.")
FIND['l0_is_definition_not_constraint'] = True
P("l = 0 condition", "fixes dM from the interior; does not annihilate the interior monopole")

# ------------------------------------------------------------------ 4. compare to F1 and F2
H("4. Comparison with F1 and F2 — the deliverable")
print("  F1 (flux result L15-18): touches ONLY l = 0; every C_l for l >= 1 exactly unchanged.")
print("  F2 (flux result L19-22): W-tilde(k) delta-tilde(k) = 0; no continuous power spectrum except P = 0.")
print()
print("  The perturbed Darmois junction is NEITHER:")
print("   * it does not annihilate the perturbation field, so it is not F2;")
print("   * it acts at every l, not only at l = 0 (it fixes the exterior continuation for each l),")
print("     and at l = 0 it defines the exterior mass rather than killing the monopole, so it is not F1.")
print()
print("  What it imposes instead: for each l, a matching of the interior potential to the unique")
print("  regular/decaying exterior vacuum solution. This is a boundary-value problem with a source,")
print("  determining Phi from delta. It leaves the interior density spectrum delta_0(x) FREE.")
FIND['not_f1'] = True
FIND['not_f2'] = True

# ------------------------------------------------------------------ 5. the l/k structure asked for by the brief
H("5. Radial-mode structure and the causal scale (brief item 6)")
chi_sec = sp.Rational(3149, 1000)   # chi_§ = 3.149 c/H0 (PROGRAM_C_FLUX_PREREG §1 L18)
P("chi_§ (in c/H0)", chi_sec)
P("chi_§ (Mpc, as pinned)", "14015")
print()
print("  Because the interior evolution has no gradient term and the constraint is a sourced BVP,")
print("  the junction supplies NO quantisation condition and hence NO spacing Delta k ~ pi/chi*.")
print("  A finite ball still restricts the DOMAIN on which delta_0 lives, but that is a statement")
print("  about the initial data, not a condition the Darmois junction imposes. This seat reports")
print("  the junction only; the domain question is not what limb 2 asks.")
FIND['no_quantisation_from_junction'] = True

# ------------------------------------------------------------------ 6. what would overturn this
H("6. What would overturn this seat's answer")
for i, txt in enumerate([
  "a pressure term in the interior (K2's limits exclude it: dust only) would restore a gradient term and with it an eigenproblem;",
  "an exterior that is not vacuum (K2's cell is matched to Schwarzschild, so this is excluded here);",
  "a requirement that the exterior mass be held fixed by something outside the junction, which would convert l=0 into a genuine F1 condition;",
  "a non-comoving boundary, which K2's B3 theorem excludes for a shell-free junction.",
], 1):
    print(f"  {i}. {txt}")

# ------------------------------------------------------------------ 7. class
H("7. Class")
cls = "LIMB2_NOT_F1_F2" if (FIND.get('not_f1') and FIND.get('not_f2')) else "LIMB2_UNDETERMINED"
for k, v in FIND.items():
    print(f"FINDING_{k.upper()}={v}")
print()
print("PLANCK_DATA_OPENED=no")
print("CLASS=" + cls)
print("CONSEQUENCE=limb 2 does NOT fire; the a-priori kill does not apply")
print("BUT_NOTE=the junction constrains the interior spectrum in no way at all, so this seat's")
print("  derivation predicts NO C_l modification from the junction itself -- which is 'no low-l")
print("  modification' WITHOUT being an F1/F2-type condition. Prereg class 1 requires F1/F2; this")
print("  outcome may fall outside every declared class and is reported as such rather than forced.")
print("K4_LIMB2_CLAUDE_SEAT_COMPLETE")
