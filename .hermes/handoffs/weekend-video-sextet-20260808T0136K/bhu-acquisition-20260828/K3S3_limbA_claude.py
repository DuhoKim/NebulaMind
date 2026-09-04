#!/usr/bin/env python3
"""K3 step 3, limb A, seat "claude": is the four-fermion interaction a small perturbation
at the densities entry 10's bounce invokes?

Governing document: K3S3_SELFCONSISTENCY_PREREG_20260904.md (frozen V2), §1 limb A.
This script is the seat's whole claim: anything not printed below is not claimed.

DECLARED BEFORE RUNNING:
  * The prereg's threshold is |R| >= 0.1 at the bounce => file K3S3_NOT_PERTURBATIVE. The
    threshold is the prereg's, not this seat's, and is not moved here.
  * Regime: entry 10's own, ultrarelativistic matter in kinetic equilibrium (L152).
  * PREDICTION, stated before the algebra: the bounce is defined by the spin term balancing
    the ordinary energy density, so R at the bounce is expected to be fixed at 1 BY
    CONSTRUCTION rather than computed. If so this script says so plainly and does not dress
    a definition as a measurement. The informative part is then R away from the bounce.
  * Limb A does not reach C1, C2, C3, C5, C6, C7; they are NOT RUN, not passes.
"""
import sympy as sp

def H(t):
    print(); print("=" * 96); print(t); print("=" * 96)

def P(k, v):
    print(f"{k:<44} {v}")

# ---------------------------------------------------------------- 1. definitions, with source lines
H("1. Definitions taken from entry 10, each with its source line")
kappa, T, zeta3 = sp.symbols('kappa T zeta_3', positive=True)
gstar, gn, gf, gb = sp.symbols('g_star g_n g_f g_b', positive=True)

alpha = sp.Rational(9, 16) * kappa
P("alpha  [Eq. (10), L116-118]", alpha)
eps = sp.pi**2 / 30 * gstar * T**4
P("epsilon(T)  [L152]", eps)
n = zeta3 / sp.pi**2 * gn * T**3
P("n(T)  [L155]", n)
P("g_star = g_b + (7/8) g_f  [L156]", sp.Eq(gstar, gb + sp.Rational(7,8)*gf))
P("g_n = (3/4) g_f  [L158]", sp.Eq(gn, sp.Rational(3,4)*gf))
print("  (L158 also states the reason: 'only fermions contribute to torsion')")
eps_tilde = -alpha * n**2
P("epsilon-tilde = -alpha n^2  [Eq. (10), L116-118]", sp.simplify(eps_tilde))

# ---------------------------------------------------------------- 2. the dimensionless ratio
H("2. The dimensionless ratio R(T) = |epsilon-tilde| / epsilon")
R = sp.simplify(sp.Abs(eps_tilde) / eps)
R = sp.simplify(alpha * n**2 / eps)
P("R(T) symbolic", R)
R_exp = sp.simplify(sp.expand(R))
P("R(T) expanded", R_exp)
Tpow = sp.simplify(sp.degree(sp.Poly(sp.simplify(R_exp * 1), T)) if R_exp.is_polynomial(T) else None)
print()
print("  TEMPERATURE SCALING: R is proportional to T^2 -- the spin term grows as T^2 relative")
print("  to the ordinary energy density, so it is negligible at low T and comparable at high T.")
scaling_ok = sp.simplify(sp.diff(sp.log(R_exp), sp.log(T)) if False else sp.simplify(R_exp.subs(T, 2*T)/R_exp)) 
P("R(2T)/R(T)  (should be 4 if R ~ T^2)", sp.simplify(scaling_ok))

# ---------------------------------------------------------------- 3. R at the bounce
H("3. R AT THE BOUNCE -- is it computed, or fixed by construction?")
print("  Entry 10's bounce (L179-L193) is the minimum of the scale factor: a >= a_cr, with a_cr")
print("  reached where da/dT = 0. The mechanism the paper states is that the spin term")
print("  epsilon-tilde = -alpha n^2 is a NEGATIVE energy density (L114-115, 'acts thus like a")
print("  perfect fluid with a negative energy density') which cancels the ordinary epsilon.")
print()
print("  So the bounce condition is  epsilon + epsilon-tilde = 0, i.e. epsilon = alpha n^2.")
R_bounce = sp.simplify((alpha * n**2) / (alpha * n**2))
P("R at the bounce = alpha n^2 / epsilon with epsilon = alpha n^2", R_bounce)
print()
print("  THIS IS FIXED BY CONSTRUCTION, NOT COMPUTED. The bounce is DEFINED as the point where")
print("  these two quantities balance, so their ratio there is 1 identically. Reporting '1' as a")
print("  measured expansion parameter would be dressing a definition as a result; it is stated")
print("  here as what it is.")
FIRES = bool(sp.simplify(R_bounce - sp.Rational(1,10)) >= 0)
P("prereg threshold", "|R| >= 0.1 fires limb A")
P("R at bounce", R_bounce)
P("limb A fires?", FIRES)

# ---------------------------------------------------------------- 4. R away from the bounce
H("4. R AWAY from the bounce -- the part that is actually informative")
print("  Solve R(T) = 1 for the bounce temperature implied by entry 10's own relations:")
T_b = sp.symbols('T_b', positive=True)
sol = sp.solve(sp.Eq(R_exp.subs(T, T_b), 1), T_b)
sol = [x for x in sol if x.is_real is not False]
P("T_bounce from R = 1", sp.simplify(sol[0]) if sol else "no closed form")
print()
print("  Then, since R ~ T^2, at a temperature T = x * T_bounce the ratio is simply x^2:")
x = sp.symbols('x', positive=True)
P("R(x * T_bounce)", sp.simplify((x*T_b)**2 / T_b**2))
for xv, label in [(sp.Rational(1,10), "T = 0.1 T_bounce"), (sp.Rational(1,100), "T = 0.01 T_bounce"),
                  (sp.Rational(1,1000), "T = 0.001 T_bounce")]:
    P(f"  R at {label}", sp.simplify(xv**2))
print()
print("  So the four-fermion interaction is perturbative (R < 0.1) for T < ~0.32 T_bounce, and")
print("  utterly negligible at ordinary densities -- but NOT at the bounce, which is the only")
print("  place the chain's claim lives.")
P("R < 0.1 requires", "T/T_bounce < sqrt(0.1) = " + str(sp.sqrt(sp.Rational(1,10)).evalf(4)))

# ---------------------------------------------------------------- 5. controls
H("5. Controls")
print("C4_EXPANSION_PARAMETER_COMPUTED=PASS")
print("  (R(T) derived symbolically above from entry 10's own relations and printed, not asserted)")
print()
print("NOT RUN, and NOT passes -- these belong to limb B, which this limb does not reach:")
for c in ["C1_FREE_LIMIT_MATCHES_K3S2", "C2_INTERACTION_DELETED", "C3_FOUR_TERMS_SEPARATE",
          "C5_MAP_DERIVED", "C6_BOTH_OBJECTS_REPORTED", "C7_NO_PRINTED_COEFF_INPUT"]:
    print(f"  {c}=NOT_RUN")

# ---------------------------------------------------------------- 6. class
H("6. Class")
print("R_AT_BOUNCE=" + str(R_bounce))
print("R_AT_BOUNCE_IS_BY_CONSTRUCTION=True")
print("R_TEMPERATURE_SCALING=T^2")
print("THRESHOLD=0.1 (declared in the prereg, not moved here)")
print("LIMB_A_FIRES=" + str(FIRES))
print("CLASS=LIMBA_NOT_PERTURBATIVE")
print("CONSEQUENCE=limb B (Hartree-Fock) is NOT written; K3 step 3 files K3S3_NOT_PERTURBATIVE")
print("WHAT_SURVIVES=K3 step 2's free-field coefficient is safe wherever the theory is")
print("  perturbative, i.e. for T below about 0.32 of the bounce temperature; it is NOT")
print("  established at the bounce itself, which is where the chain's claim lives.")
print("K3S3_LIMBA_CLAUDE_SEAT_COMPLETE")
