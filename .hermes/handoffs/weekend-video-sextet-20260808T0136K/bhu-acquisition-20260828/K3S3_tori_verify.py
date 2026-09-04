#!/usr/bin/env python3
"""Tori's own verification of the contested intermediate value in K3 step 3 limb A.

CLAIM (codex, against Tori's own seat): entry 10's bounce is the MINIMUM OF a(T) from its
Eq. (15)/(16), not the vanishing of the total energy density, and at that point the
dimensionless ratio R = |eps_tilde|/eps equals 2/3, not 1.

Tori's seat asserted R = 1 by assuming the bounce is where eps + eps_tilde = 0. This script
derives a(T) from the source's own Eq. (15), differentiates it, and computes R(T_cr) without
assuming either answer.
"""
import sympy as sp

def P(k, v):
    print(f"{k:<50} {v}")

T, ar, Tr, alpha, hn, hstar = sp.symbols('T a_r T_r alpha h_n h_star', positive=True)

print("=" * 96)
print("Entry 10 Eq. (15), L170-174, transcribed from the source:")
print("   a(T) = (a_r T_r / T) * exp( 3 alpha h_n^2 T^2 / (4 h_star) )")
print("=" * 96)
a = (ar * Tr / T) * sp.exp(3 * alpha * hn**2 * T**2 / (4 * hstar))
P("a(T)", a)

# minimum of a(T): da/dT = 0  (entry 10 L179: "given by dT(T_cr) = 0")
dlna = sp.simplify(sp.diff(sp.log(a), T))
P("d ln a / dT", dlna)
Tcr_sols = sp.solve(sp.Eq(dlna, 0), T)
Tcr = [s for s in Tcr_sols if s.is_positive is not False][0]
P("T_cr from da/dT = 0", sp.simplify(Tcr))
P("T_cr^2", sp.simplify(Tcr**2))
codex_Tcr2 = 2 * hstar / (3 * alpha * hn**2)
P("codex's claimed T_cr^2 = 2 h_star/(3 alpha h_n^2)", codex_Tcr2)
claimA = sp.simplify(sp.simplify(Tcr**2) - codex_Tcr2) == 0
P("MATCH?", claimA)

# is it a minimum?
d2 = sp.simplify(sp.diff(sp.log(a), T, 2).subs(T, Tcr))
P("d2 ln a / dT2 at T_cr (positive => minimum)", sp.simplify(d2))

print()
print("=" * 96)
print("The dimensionless ratio, with eps = h_star T^4 and n = h_n T^3 (L152-L168)")
print("=" * 96)
eps = hstar * T**4
n = hn * T**3
R = sp.simplify(alpha * n**2 / eps)
P("R(T) = alpha n^2 / eps", R)
R_bounce = sp.simplify(R.subs(T, Tcr))
P("R(T_cr)", R_bounce)
P("codex's claimed 2/3", sp.Rational(2, 3))
claimB = sp.simplify(R_bounce - sp.Rational(2, 3)) == 0
P("MATCH?", claimB)
print()
P("Tori's seat asserted R(bounce)", 1)
P("  which would follow from eps + eps_tilde = 0, i.e.", "R = 1")
P("  but that is NOT entry 10's bounce condition; its bounce is da/dT = 0 (L179).", "")
P("Tori's seat was WRONG on this intermediate value", sp.simplify(R_bounce) != 1)

print()
print("=" * 96)
print("Does the class change?")
print("=" * 96)
thr = sp.Rational(1, 10)
P("prereg declared threshold", thr)
P("|R(T_cr)| >= threshold ?", sp.simplify(R_bounce) >= thr)
P("class under Tori's (wrong) value 1", "LIMBA_NOT_PERTURBATIVE")
P("class under the correct value 2/3", "LIMBA_NOT_PERTURBATIVE")
print("  -> the CLASS is unchanged; only the reported number and its provenance change.")

print()
print("VERIFY_TCR=" + ("PASS" if claimA else "FAIL"))
print("VERIFY_R_BOUNCE_TWO_THIRDS=" + ("PASS" if claimB else "FAIL"))
print("TORI_SEAT_INTERMEDIATE_WRONG=True")
print("CLASS_UNCHANGED=True")
print("K3S3_TORI_VERIFY_COMPLETE")
