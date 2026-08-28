"""R-P2A1-3: PRD 85,107502 (arXiv:1111.4595 TeX pinned 9ac75297...) symbolic checks (sympy).
(a) a(T) from Eq.(diff);  (b) T_cr from da/dT=0;  (c) a_cr closed form;
(d) t/t0 parametric integral;  (e) bounce speed v closed form with alpha=9 kappa/16;
(f) Omega(T_cr) formula."""
import sympy as sp
T, a, hs, hn, al, k = sp.symbols('T a h_star h_n alpha kappa', positive=True)
c1 = 3*al*hn**2/(2*hs)
# (a) integrate dT/T - c1*T dT + da/a = 0  ->  a = ar Tr/T * exp(c1 T^2/2)
ar, Tr = sp.symbols('a_r T_r', positive=True)
a_of_T = ar*Tr/T*sp.exp(c1*T**2/2)
resid = sp.simplify(sp.diff(sp.log(a_of_T), T) + 1/T - c1*T)
print("(a) a(T) solves the conservation ODE:", sp.simplify(resid - 2/T + 2*c1*T*0) == sp.simplify(2*(c1*T - 1/T) + resid)*0 + sp.simplify(resid) == 0 if False else sp.simplify(sp.diff(sp.log(a_of_T), T) - (c1*T - 1/T)) == 0)
# paper Eq.(int) has exp(3 alpha hn^2 T^2 /(4 hs)) = exp(c1 T^2 /2)  ✓ same
# (b) T_cr
Tcr = sp.solve(sp.diff(a_of_T, T), T)
Tcr = [t_ for t_ in Tcr if t_.is_positive][0]
print("(b) T_cr =", sp.simplify(Tcr), " = sqrt(2 hs/(3 alpha hn^2)):",
      sp.simplify(Tcr - sp.sqrt(2*hs/(3*al*hn**2))) == 0)
# (c) a_cr
acr = sp.simplify(a_of_T.subs(T, Tcr))
target = ar*Tr*sp.sqrt(3*sp.E*al*hn**2/(2*hs))
print("(c) a_cr =", acr, " matches paper:", sp.simplify(acr - target) == 0)
# (d) t/t0: integrand (2/3 cosh^2 eta - 1); antiderivative sinh(2eta)/6 - 2eta/3
eta = sp.symbols('eta')
F = sp.sinh(2*eta)/6 - 2*eta/3
print("(d) dF/deta = 2/3 cosh^2 - 1:", sp.simplify(sp.diff(F, eta) - (sp.Rational(2,3)*sp.cosh(eta)**2 - 1)) == 0)
# (e) v = |adot(Tcr)| with adot^2 = (kappa/3)(hs T^4 - alpha hn^2 T^6) a^2, alpha = 9k/16
v2 = (k/3*(hs*Tcr**4 - al*hn**2*Tcr**6)*acr**2)
v2_target = sp.Rational(32,243)*sp.E*(hs/hn)**2*ar**2*Tr**2
print("(e) v^2 with alpha=9kappa/16 equals (32e/243)(hs/hn)^2 (ar Tr)^2:",
      sp.simplify(v2.subs(al, 9*k/16) - v2_target) == 0)
# (f) Omega(Tcr) - 1 = 1/v^2 -> 243 hn^2/(32 e hs^2 (ar Tr)^2)
print("(f) 1/v^2 matches paper Eq.(density):",
      sp.simplify(1/v2.subs(al, 9*k/16) - sp.Rational(243,32)/sp.E*hn**2/(hs**2*ar**2*Tr**2)) == 0)
