#!/usr/bin/python3
"""KIMI independent symbolic re-derivation for B7 challenge.
Derives the KS first-order system from publisher (10), (14), (34) directly,
then checks every B7 identity WITHOUT importing any of B7's expressions.
"""
import sympy as sp

u, v, K, e, n, a, b, k = sp.symbols("u v K epsilon n alpha beta kappa", positive=True)
T, hs, F, Fp = sp.symbols("T h_star F Fprime", positive=True)

# --- Printed (10): three equations. Unknowns ud=dot u, vd=dot v.
# (10a) v^2 + K + 2 u v = k (e - a n^2)          [constraint]
# (10b) v^2 + K + 2(vd + v^2) = -k (e/3 - a n^2)
# (10c) (ud + u^2) + (vd + v^2) + u v = -k (e/3 - a n^2)
ud, vd = sp.symbols("ud vd")
rho = e - a*n**2
P = e/sp.Integer(3) - a*n**2
eq10b = sp.Eq(v**2 + K + 2*(vd + v**2), -k*P)
eq10c = sp.Eq((ud + u**2) + (vd + v**2) + u*v, -k*P)
sol = sp.solve([eq10b, eq10c], [ud, vd], dict=True)[0]
fu = sp.expand(sol[ud]); fv = sp.expand(sol[vd])
print("derived dot u =", fu)
print("derived dot v =", fv)

# --- Printed (34): nd = beta H^4 - 3 H n ;  (14): energy law.
H = (u + 2*v)/3
D = u - v
S = D**2/3
psi = b*H**4
fn = psi - 3*H*n
# (14): d(rho V)/dt + P dV/dt = 0 with Vdot/V = 3H  =>
# ed - 2 a n nd + 3H(rho + P) = 0 ; rho+P = e + e/3 - 2 a n^2
ed_sym = 2*a*n*fn - 3*H*(4*e/sp.Integer(3) - 2*a*n**2)
fe = sp.expand(ed_sym)
print("derived dot epsilon =", fe)

state = (u, v, K, e, n)
flow = (fu, fv, -2*v*K, fe, fn)
def dot(q):
    return sum(sp.diff(q, x)*f for x, f in zip(state, flow))

ok = 0
def chk(label, q):
    global ok
    r = sp.factor(q)
    print(f"{label} -> {r}")
    assert r == 0, label
    ok += 1

C = v**2 + 2*u*v + K - k*rho
# Constraint propagation for BOTH closures via chain rule on the actual state.
for name, et, edot in (("b", hs*T**4, fe.subs(e, hs*T**4)), ("c", F, fe.subs(e, F))):
    cd = sum(sp.diff(C, x)*f for x, f in zip(state, flow) if x != e)
    cd = cd.subs(e, et) + sp.diff(C, e)*edot
    chk("constraint_prop_closure_" + name, cd + 3*H*C.subs(e, et))
    # energy residual E = ed - 2 a n nd + 3H(4e/3 - 2 a n^2) must vanish identically
    chk("energy_residual_closure_" + name,
        (edot - 2*a*n*fn + 3*H*(4*et/sp.Integer(3) - 2*a*n**2)))

# Raychaudhuri off-constraint: dot H = -H^2 - 2S/3 - k e/3 + 2 k a n^2/3 - C/6 ? (B7 form: R - C/6)
ray = -H**2 - 2*S/sp.Integer(3) - k*e/sp.Integer(3) + 2*k*a*n**2/sp.Integer(3)
chk("raychaudhuri_offC", dot(H) - ray + C/sp.Integer(6))
# Turn-margin form: dot H = -2H^2 + (k a n^2 - S - K)/3 + C/6
chk("turn_margin_offC", dot(H) - (-2*H**2 + (k*a*n**2 - S - K)/sp.Integer(3)) - C/sp.Integer(6))

# On C=0, H=0: dot H = (k a n^2 - S - K)/3  -> turning condition (B7.7)
print("turn condition on C=0,H=0: dotH = (kappa*alpha*n^2 - S - K)/3 [from turn_margin_offC]")

# Degenerate equality analysis: H=0 => u=2d/3, v=-d/3 ; C=0 & k a n^2 = S+K => e=2K/k
d = sp.symbols("Delta", positive=True)
sub0 = {u: 2*d/sp.Integer(3), v: -d/sp.Integer(3), e: 2*K/k}
n2sub = (K + d**2/sp.Integer(3))/(k*a)   # k a n^2 = S + K
Hdd = sp.expand(dot(dot(H)))
bnd = Hdd.subs(sub0)
bnd = bnd.subs(n**2, n2sub)
chk("degenerate_Hdd = -4 K Delta/9", bnd + 4*K*d/sp.Integer(9))
Hddd = sp.expand(dot(dot(dot(H)))).subs({u: sp.Integer(0), v: sp.Integer(0), e: 2*K/k})
chk("degenerate_Hddd(Delta=0) = -4 K^2/9", Hddd.subs(n**2, K/(k*a)) + 4*K**2/sp.Integer(9))

# Fractional race (B7.11)
R = k*a*n**2/S
chk("fractional_race", dot(R)/R - 2*(psi/n - K/D))

# J evolution (B7.13): J = 2 k a n^2 - 2S - k e
J = 2*k*a*n**2 - 2*S - k*e
chk("J_evolution", dot(J) + 6*H*J + 2*H*k*e - 2*k*a*n*psi + 4*K*D/sp.Integer(3))

# J = 3(dot H + H^2) on C=0  (off C: J = 3(dotH+H^2) - C/2 ?)
expr = sp.expand(dot(H) + H**2 - J/sp.Integer(3))
print("dotH + H^2 - J/3 =", sp.factor(expr), " (should be proportional to C)")

# Comoving identities
chk("signed_shear: dot D + 3 H D = K", dot(D) + 3*H*D - K)
chk("comoving_shear: dot S + 6 H S = 2 K D/3", dot(S) + 6*H*S - 2*K*D/sp.Integer(3))

# Closure (b) temperature equation: e = h T^4 => Tdot = fe/(4 h T^3)
Td_b = sp.expand(fe.subs(e, hs*T**4)/(4*hs*T**3))
print("closure b Tdot =", Td_b)
Td_c = sp.expand(fe.subs(e, F)/Fp)
print("closure c Tdot =", Td_c)

# Zero-production control step-2 inequality ingredients:
# dot H = -H^2 - (2/3)(S - w) - k e/3 with w = k a n^2 : verified by raychaudhuri_offC above.
print("ALL_CHECKS_PASSED", ok)
