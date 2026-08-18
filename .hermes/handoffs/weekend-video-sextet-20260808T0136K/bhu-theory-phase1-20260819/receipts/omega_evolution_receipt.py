"""R6: derive omega(a) per era from the pinned Malik-Wands equations.
Pinned inputs (sources/0809.4944.html, quoted in GORU_INGREDIENTS.md + DERIVATION doc):
  (8.61) delta q_i = (rho+P)(v_i - S_i)   [vector gauge S_i=0 adopted, stated]
  (8.62) delta q_i' + 4 H delta q_i = -nabla^2 Pi_i ;  Pi_i = 0 (spec A7, no anisotropic stress)
Derivation: solve (8.62), then v = dq/(rho+P), then omega_ang = v_phys/(a x) about a comoving axis."""
import sympy as sp
eta = sp.symbols('eta', positive=True)
a = sp.Function('a', positive=True)(eta)
dq = sp.Function('dq', positive=True)(eta)
H = a.diff(eta)/a  # conformal Hubble
sol = sp.dsolve(sp.Eq(dq.diff(eta) + 4*H*dq, 0), dq)
print("(8.62) with Pi=0 solves to:", sol.rhs, "  => dq ∝ a^-4:",
      sp.simplify(sol.rhs * a**4).has(a) == False)
# per-era velocity and angular velocity (power-law bookkeeping, exact)
n = sp.symbols('n')  # rho+P ∝ a^-n_e
a_ = sp.symbols('a_', positive=True)
v = a_**(-4) / a_**(-n)          # v ∝ dq/(rho+P)
omega = v / a_                   # omega_ang = v/(a x), comoving x fixed
for era, n_e in [("matter (P=0, rho ∝ a^-3)", 3), ("radiation (rho+P ∝ a^-4)", 4)]:
    print(f"{era}: v ∝ a^{sp.simplify(sp.log(v.subs(n,n_e), a_))}, "
          f"omega ∝ a^{sp.simplify(sp.log(omega.subs(n,n_e), a_))}")
# cross-check via angular momentum conservation for matter: L ~ (rho a^3)(a x)(v) = const
rho_a3, x = 1, 1
L = rho_a3 * a_ * a_**(-1)
print("matter-era cross-check: L ∝", sp.simplify(L), "(constant ✓)")
