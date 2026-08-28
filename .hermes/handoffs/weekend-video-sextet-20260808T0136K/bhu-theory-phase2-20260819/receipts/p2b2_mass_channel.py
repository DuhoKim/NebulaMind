"""p2b2-R1: the M channel — re-derive the audited M->(a0,T0,R0) map from its two defining
relations (our own algebra), then the scaling of the bounce-patch size with parent mass.
Defining relations (source: TRACK_A2_AUDIT B-8/B-9, gate-certified; Paper B = sources/1410.3881):
 (i) closed-FLRW turnaround: (kappa/3) eps0 = 1/a0^2   (adot=0, k=1)
 (ii) patch mass: M c^2 = (4 pi/3) r0^3 eps0, with r0 = a0 sin(R0)."""
import sympy as sp
G, c, M, r0, kappa = sp.symbols('G c M r0 kappa', positive=True)
eps0, a0, R0 = sp.symbols('epsilon0 a0 R0', positive=True)
kap = 8*sp.pi*G/c**4
e1 = sp.Eq(kap/3*eps0, 1/a0**2)
e2 = sp.Eq(M*c**2, sp.Rational(4,3)*sp.pi*r0**3*eps0)
sol_eps = sp.solve(e2, eps0)[0]
a0_sol = sp.solve(e1.subs(eps0, sol_eps), a0)[0]
rg = 2*G*M/c**2
print("a0 =", sp.simplify(a0_sol), " = (r0^3/r_g)^(1/2):",
      sp.simplify(a0_sol - sp.sqrt(r0**3/rg)) == 0)
sinR0 = sp.simplify(r0/a0_sol)
print("sin R0 =", sinR0, " = (r_g/r0)^(1/2):", sp.simplify(sinR0 - sp.sqrt(rg/r0)) == 0)
# T0 from eps0 = h_star T0^4  (thermal form; T0 in energy units)
hs = sp.symbols('h_star', positive=True)
T0 = sp.solve(sp.Eq(sol_eps, hs*sp.Symbol('T0', positive=True)**4), sp.Symbol('T0', positive=True))[0]
print("T0 =", T0)
# scaling of a0*T0 with M at fixed compactness chi = r0/rg
chi = sp.symbols('chi', positive=True)
a0T0 = sp.simplify((a0_sol*T0).subs(r0, chi*rg))
print("a0*T0 (r0 = chi r_g):", sp.simplify(a0T0))
expM = sp.simplify(sp.diff(sp.log(a0T0), sp.log(M))) if False else None
print("  -> proportional to chi^(3/4) M^(1/2):",
      sp.simplify(a0T0/(chi**sp.Rational(3,4)*M**sp.Rational(1,2))).has(M) == False)
print("Conclusion: M alone fixes patch geometry (a0, R0, T0) given r0; bounce T is")
print("M-INDEPENDENT (universal); M enters interior initial data only through SIZE (a0 T0 ~ M^1/2).")
