"""p2b1-R1: Treatment I (spin-fluid, PLB-class) — OUR OWN derivation, fresh algebra.
Base equations source-pinned: effective-fluid Friedmann system (sources/1007.0587/main.tex
lines 121-131); s^2 = C_avg (hbar c)^2 n^2 form ASSUMED-WITH-CITATION (line 136-140, cited
there to Nurgaliev-Ponomariev; underived in the chain per audit H2).
Steps: (1) conservation law from the Friedmann pair; (2) n(a); (3) eps_S ~ a^-6;
(4) species-coherence algebra (the bracket); (5) bounce a_m incl. curvature-neglect
justification; (6) addot > 0; (7) numeric bracket table incl. quarantined P13 recompute."""
import sympy as sp

# ---- (1) conservation law derived from the Friedmann pair (not assumed) ----
t = sp.symbols('t'); k, c = sp.symbols('kappa c', positive=True)
a = sp.Function('a', positive=True)(t)
eps = sp.Function('epsilon')(t); p = sp.Function('p')(t); s2 = sp.Function('s2')(t)
ee = eps - k*s2/4; pe = p - k*s2/4
F1 = sp.Eq(a.diff(t)**2 + 1, k/3*ee*a**2)          # dots wrt ct (paper convention)
F2 = sp.Eq(a.diff(t)**2 + 2*a*a.diff(t,2) + 1, -k*pe*a**2)
# The conservation law is the integrability condition: differentiate F1, eliminate a'' via F2
# and a'^2 via F1; the remainder must be proportional to the law expression.
G = sp.diff(F1.lhs - F1.rhs, t)
app = sp.solve(F2, a.diff(t,2))[0]
G = sp.expand(G.subs(a.diff(t,2), app))
G = sp.expand(G.subs(a.diff(t)**3, a.diff(t)*(k/3*ee*a**2 - 1)))
G = sp.expand(G.subs(a.diff(t)**2, k/3*ee*a**2 - 1))
law = sp.expand(sp.diff(ee*a**3, t) + pe*sp.diff(a**3, t))
ratio = sp.simplify(G/law)
print("(1) dF1/dt with F2,F1 substituted = (pure factor) x [conservation law]:",
      "factor =", ratio, "-> law forced to 0 (a'!=0):", ratio.has(eps) == False and ratio.has(s2) == False)

# ---- (2)+(3) n(a) and eps_S(a): with p = w eps, dn/n = deps/(eps+p) ----
w, A3, C, n0, a_ = sp.symbols('w A3 C n0 a', positive=True)
epsw = A3*a_**(-3*(1+w))
n_of_a = (epsw)**(1/(1+w))                     # n ~ eps^{1/(1+w)}
print("(2) n ~ a^-3 for any w:", sp.simplify(n_of_a - A3**(1/(1+w))*a_**(-3)) == 0)
epsS = -k*C*n_of_a**2/4
print("(3) eps_S ~ a^-6 for any w:", sp.simplify(epsS*a_**6).has(a_) == False)

# ---- (4) species coherence: E[(sum_i s_i)^2] = sum_i E[s_i^2] for independent zero-mean ----
N = 6
ss = sp.symbols('s1:7')   # s1..s6 zero-mean independent
tot2 = sp.expand((sum(ss))**2)
# expectation: E[si sj] = 0 (i!=j), E[si^2] = v
v = sp.symbols('v', positive=True)
E = tot2
for i in range(N):
    for j in range(N):
        if i != j: E = E.subs(ss[i]*ss[j], 0)
    E = E.subs(ss[i]**2, v)
print("(4) E[s_tot^2] =", E, "= N*v (incoherent);  coherent (identical fields): (N)^2 v =", N**2, "v",
      " -> coherent/incoherent =", N)

# ---- (5) bounce with curvature retained, then neglect justified ----
OR, OSm, Om1 = sp.symbols('Omega_R Omega_Sm Omega_minus1', positive=True)  # OSm = |Omega_S|
ah = sp.symbols('ahat', positive=True)
# H^2/H0^2 = OR ah^-4 - OSm ah^-6 - (Om-1) ah^-2 = 0 at bounce (exact, closed universe)
poly = OR*ah**2 - OSm - Om1*ah**4   # multiplied by ah^6/H0^2
sols = sp.solve(sp.Eq(poly, 0), ah**2)
exact = [sp.simplify(s_) for s_ in sols]
approx = OSm/OR
# expand exact root to first order in Om1:
ah2_exact = [s_ for s_ in exact if sp.limit(s_, Om1, 0) == approx][0]
corr = sp.simplify(sp.series(ah2_exact, Om1, 0, 2).removeO() - approx)
print("(5) exact bounce root -> a_m^2 = OSm/OR + [", sp.simplify(corr), "] ;")
rel = sp.simplify(corr/approx)
print("    relative curvature correction =", rel, " (numeric below)")

# ---- (6) addot at the bounce (fresh) ----
epsv, s2v = sp.symbols('eps s2', positive=True)
acc = -(epsv - k*s2v/4 + 3*(epsv/3 - k*s2v/4))     # ~ -(e_eff + 3 p_eff), w=1/3
print("(6) at eps = kappa s2/4:", sp.simplify(acc.subs(epsv, k*s2v/4)), "> 0  (bounce, not stall)")

# ---- (7) numeric bracket ----
import math
hbar, cc, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
kap = 8*math.pi*G/cc**4
H0 = 1/4.4e17; Om, ORn = 1.002, 8.8e-5
n1, Ns = 5.6e7, 6
eps_c = 3*H0**2*cc**2/(8*math.pi*G)
a0 = cc/(H0*math.sqrt(Om-1))
eps_P = cc**7/(hbar*G**2)
print(f"\n(7) eps_c = {eps_c:.4e} J/m^3, a0 = {a0:.3e} m, eps_Planck = {eps_P:.3e} J/m^3")
print(f"{'quantity':28s}{'coherent':>14s}{'incoherent':>14s}")
rows = {}
for tag, s2f in [("coherent", ((hbar*cc*(n1*Ns))**2)/8), ("incoherent", Ns*((hbar*cc*n1)**2)/8)]:
    OS = -(kap/4)*s2f/eps_c
    amh = math.sqrt(-OS/ORn)
    am = amh*a0
    dev = -4*OS*(Om-1)/ORn**2
    f2 = math.sqrt(2)/2 + 0.5*math.log(math.sqrt(2)+1)
    tt = -OS/(ORn**1.5*H0)*f2
    va = math.pi*ORn/(2*math.sqrt(-OS*(Om-1)))
    epsR = ORn*eps_c*amh**-4
    rows[tag] = (OS, amh, am, dev, tt, va, epsR)
labels = ["Omega_S", "a_m^", "a_m [m]", "Omega(min)-1", "t(sqrt2 a_m) [s]", "v_a/c", "eps_R(a_m) [J/m^3]"]
for i, lab in enumerate(labels):
    print(f"{lab:28s}{rows['coherent'][i]:14.3e}{rows['incoherent'][i]:14.3e}")
print(f"{'eps_R/eps_Planck':28s}{rows['coherent'][6]/eps_P:14.1f}{rows['incoherent'][6]/eps_P:14.1f}")
print(f"quarantined P13 check: our coherent eps_R = {rows['coherent'][6]:.3e}  (audit R2: 7.650e116; printed 1.1e116 NOT used)")
# curvature-neglect numeric: rel = Om1*OSm/OR^2 at leading order
relnum = (Om-1)*(-rows['coherent'][0])/ORn**2
print(f"curvature correction to a_m^2: relative ~ {relnum:.1e}  -> utterly negligible")
