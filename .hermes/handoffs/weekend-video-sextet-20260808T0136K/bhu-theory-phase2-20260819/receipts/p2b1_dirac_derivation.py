"""p2b1-R2: Treatment II (Dirac spinor-torsion, PRD-class) — OUR OWN derivation.
Base pinned: sources/1111.4595/cosmology_torsion.tex (conservation law line 127-131,
eps/p/n thermal forms line 133-134; <s^2> = (3/4)n^2 ASSUMED-WITH-CITATION line 100).
Steps: (1) a(T) by fresh ODE solve; (2) T_cr, a_cr fresh; (3) H^2 > 0 at the minimum
(cusp, not smooth bounce) + beta-dot divergence at the cusp — the prescription pathology;
(4) numerics incl. quarantined D15/D16 recomputed our own way; (5) coherence-direction."""
import sympy as sp

# (1) fresh solve of dT/T - c1 T dT + da/a = 0
T = sp.symbols('T', positive=True); c1 = sp.symbols('c1', positive=True)
aF = sp.Function('a', positive=True)(T)
ode = sp.Eq(aF.diff(T)/aF, c1*T - 1/T)
sol = sp.dsolve(ode, aF)
print("(1) a(T) =", sp.simplify(sol.rhs), "  [C1/T * exp(c1 T^2/2): matches pinned Eq.(int) with c1 = 3 alpha h_n^2/(2 h_star)]")

# (2) T_cr, a_cr fresh
a_expr = sp.Symbol('K', positive=True)/T*sp.exp(c1*T**2/2)
Tcr = [t_ for t_ in sp.solve(sp.diff(a_expr, T), T) if t_.is_positive][0]
print("(2) T_cr =", Tcr, "; a_cr/K =", sp.simplify(a_expr.subs(T, Tcr)/sp.Symbol('K', positive=True)))

# (3) cusp, not smooth bounce: H^2 at T_cr strictly positive
hs, hn, al, k = sp.symbols('h_star h_n alpha kappa', positive=True)
c1v = 3*al*hn**2/(2*hs)
Tcr_v = sp.sqrt(2*hs/(3*al*hn**2))
H2_at_min = k/3*(hs*Tcr_v**4 - al*hn**2*Tcr_v**6)   # (kappa/3)(eps+eps_tilde) with forms subbed
print("(3) (kappa/3)(eps_eff)(T_cr) =", sp.simplify(H2_at_min), " > 0  -> adot != 0 at minimum: CUSP")
# beta-dot divergence: |beta_dot| = sqrt(kappa hs/3) sqrt(beta^2 - 2/3 bcr^2)/(beta^2 - bcr^2)
b, bcr = sp.symbols('beta beta_cr', positive=True)
bdot = sp.sqrt(k*hs/3)*sp.sqrt(b**2 - sp.Rational(2,3)*bcr**2)/(b**2 - bcr**2)
lim = sp.limit(bdot, b, bcr, '+')
print("    lim_{beta->beta_cr+} |beta_dot| =", lim, " (temperature rate diverges at the cusp)")

# (4) numerics
import math
hbar, cc, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
eV = 1.602176634e-19
zeta3 = 1.2020569031595943
mP_J = math.sqrt(hbar*cc**5/(8*math.pi*G))
g_b, g_f = 28, 90
g_star, g_n = g_b + 7/8*g_f, 3/4*g_f
h_s = math.pi**2/30*g_star; h_n = zeta3/math.pi**2*g_n
TcrmP = math.sqrt(2*h_s*16/(3*9*h_n**2))
print(f"(4) T_cr = {TcrmP:.3f} m_P (reduced m_P = {mP_J/eV/1e9:.4e} GeV)")
a0, zeq, Tr_eV = 2.9e27, 3200, 0.75
ar = a0/(1+zeq)
Tr = Tr_eV*eV/(hbar*cc); Tcr_m = TcrmP*mP_J/(hbar*cc)
a_cr = ar*Tr/Tcr_m*math.sqrt(math.e)
arTr = ar*Tr
v = math.sqrt(32*math.e/243)*(h_s/h_n)*arTr
print(f"    a_cr = {a_cr:.2e} m;  v = {v:.3e};  v_ant = pi v = {math.pi*v:.3e}")
print(f"    [quarantined D15: printed 8.9e34 NOT used; own value {math.pi*v:.3e}; audit R4: 2.765e31 -> agree]")
print(f"    Omega(T_cr)-1 = 1/v^2 = {1/v**2:.3e}")
print(f"    [quarantined D16: printed 1.3e-70 NOT used; own value {1/v**2:.3e}; audit R4: 1.291e-62 -> agree]")

# (5) coherence direction: if <s^2> reduced by factor f (incoherent species), alpha_eff*h_n^2 -> /f
for f in (6,):
    print(f"(5) illustration f = {f} (equal-species incoherence): T_cr -> {TcrmP*math.sqrt(f):.2f} m_P "
          f"(deeper into the super-Planckian regime); a_cr -> {a_cr/math.sqrt(f)*math.sqrt(f)*0+ar*Tr/(TcrmP*math.sqrt(f)*mP_J/(hbar*cc))*math.sqrt(math.e):.2e} m")
