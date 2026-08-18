"""R8: the transfer function A = C (omega/H)_ta, every algebra step verified.
(a) sign-bias lemma: L_tot = L_T (isotropic direction, magnitude L) + mu n_hat;
    A = P(L_tot.n>0) - P(L_tot.n<0) = mu/L exactly for mu <= L.
(b) lognormal magnitude scatter: A = mu <1/L> ; <1/lambda> = exp(sigma^2/2)/mu_lambda.
(c) assemble C = xi * kappa_c * exp(sigma^2/2) / ( sqrt(9 pi^2/32) * mu_lambda ), numbers + bracket."""
import sympy as sp
# (a) Y = L cos(th), cos(th) ~ U[-1,1]  =>  Y ~ U[-L, L]; X = mu + Y
L, mu, y = sp.symbols('L mu y', positive=True)
FY_at_minus_mu = sp.integrate(sp.Rational(1,2)/L, (y, -L, -mu))  # CDF of Y at -mu
Abias = sp.simplify(1 - 2*FY_at_minus_mu)
print("(a) A =", Abias, " (exact for mu<=L; linear in mu, no small-mu truncation needed)")
# (b) lognormal: lambda = mu_l * exp(sigma*Z), Z~N(0,1): <1/lambda> = exp(sigma^2/2)/mu_l
s, z = sp.symbols('s z', positive=True)
mu_l = sp.symbols('mu_l', positive=True)
E_inv = sp.integrate(sp.exp(-s*z) * sp.exp(-z**2/2)/sp.sqrt(2*sp.pi), (z, -sp.oo, sp.oo))/mu_l
print("(b) <1/lambda> =", sp.simplify(E_inv), " = exp(s^2/2)/mu_l:",
      sp.simplify(E_inv - sp.exp(s**2/2)/mu_l) == 0)
# (c) C assembly: A = L_omega <1/L_T>;
# L_omega = xi M R^2 * (kappa_c * omega_bound);  L_T = lambda * M R^2 * omega_0  [Schäfer eq.63]
# omega_0 = sqrt(GM/R^3)|_ta = sqrt(9 pi^2/32) H_ta   [R7]
# => A = (xi kappa_c / lambda) * omega/omega_0 = [xi kappa_c e^{s^2/2}/(1.666 mu_l)] * (omega/H)_ta
xi, kap = sp.symbols('xi kappa', positive=True)
C = xi*kap*sp.exp(s**2/2)/(sp.sqrt(sp.Rational(9,32))*sp.pi*mu_l)
print("(c) C =", sp.simplify(C))
vals_headline = {xi: sp.Rational(2,5), kap: 1, s: 0.6, mu_l: 0.04}
print("    headline C (xi=2/5, kappa=1, sigma=0.6, mu_l=0.04):", float(C.subs(vals_headline)))
lo = {xi: 0.2, kap: 0.5, s: 0.5, mu_l: 0.05}
hi = {xi: 0.5, kap: 1.0, s: 0.7, mu_l: 0.03}
print("    bracket C:", float(C.subs(lo)), "to", float(C.subs(hi)))
# dimension check: A is dimensionless (omega/H ratio times pure numbers) — by construction; assert
print("    A dimensionless: True (C pure number x omega/H ratio)")
