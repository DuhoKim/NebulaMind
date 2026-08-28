"""R-P2A1-1: PLB 694,181 (arXiv:1007.0587 TeX pinned 95ba2de3...) symbolic checks.
(a) scaling: with s^2 = C n^2 and dn/n = d(eps)/(eps+p), p = w*eps  =>  conservation law
    (law) admits eps ~ a^-3(1+w) and eps_S = -(kappa/4)s^2 ~ a^-6  [paper Eqs. scaling, ome2]
(b) bounce: at a_m (H=0), effective acceleration > 0 for w=1/3
(c) Omega(a-hat) formula [paper Eq. omega] from (ide)+(Hub)
(d) f(x) = int sqrt(x^2-1)... check d/dx [x/2 sqrt(x^2-1) + 1/2 ln|x+sqrt(x^2-1)|] = sqrt(x^2-1)
    and that (Hub) integrates to -Omega_R^{3/2} H0 t/Omega_S = f(a/a_m) for k-neglected era.
(e) SI dimension check of s^2 = (hbar c n)^2/8 and eps_S = -kappa s^2/4."""
import sympy as sp

# (a) conservation law check
a, w, C, k = sp.symbols('a w C kappa', positive=True)
A3, A6 = sp.symbols('A3 A6', positive=True)
eps = A3 * a**(-3*(1+w))
n   = eps**(1/(1+w))          # n ~ eps^{1/(1+w)} (from dn/n = deps/(eps+p))
s2  = C * n**2
epsS = -k*s2/4
p   = w*eps
lhs = sp.diff((eps + epsS)*a**3, a) + (p - k*s2/4)*sp.diff(a**3, a)
print("(a) conservation law satisfied:", sp.simplify(lhs) == 0)
print("    eps_S scaling exponent:", sp.simplify(sp.log(epsS/(-k*C/4), a).rewrite(sp.log)))
# exponent: epsS ~ a^{-6} independent of w:
expo = sp.simplify(sp.diff(sp.log(-epsS), sp.log(a))) if False else None
print("    eps_S ~ a^-6 for any w:", sp.simplify(-k*C/4*(A3*a**(-3*(1+w)))**(2/(1+w)) - (-k*C*A3**(2/(1+w))/4)*a**(-6)) == 0)

# (b) bounce acceleration: Fri2 - Fri1 => 2 a addot = -kappa(p - k s2/4) a^2 - (1/3)kappa(eps - k s2/4)a^2 + ...
# do it directly: addot/a = -(kappa/6)(eps_eff + 3 p_eff), eps_eff = eps - ks2/4, p_eff = p - ks2/4
epsv, s2v, kv = sp.symbols('eps s2 kappa', positive=True)
eps_eff = epsv - kv*s2v/4
p_eff   = epsv/3 - kv*s2v/4     # w = 1/3
acc = -(eps_eff + 3*p_eff)      # sign of addot
acc_at_bounce = acc.subs(epsv, kv*s2v/4)   # bounce: eps_eff = 0
print("(b) at bounce (eps = kappa s2/4): -(eps_eff+3p_eff) =", sp.simplify(acc_at_bounce),
      "> 0:", sp.simplify(acc_at_bounce) == kv*s2v/2)

# (c) Omega(a-hat): |H| = H0 sqrt(OR ah^-4 + OS ah^-6); Omega-1 = c^2/(a^2 H^2) [from a|H|sqrt(Omega-1)=c]
ah, OR, OS, Om1, H0, a0, c = sp.symbols('ahat Omega_R Omega_S Omega_minus1 H0 a0 c', positive=True)
# with a0 H0 sqrt(Omega-1) = c: Omega(ah)-1 = c^2/(ah^2 a0^2 H^2) = (Omega-1) H0^2/(ah^2 H^2)
H2 = H0**2*(OR*ah**-4 - sp.Symbol('OSm', positive=True)*ah**-6)  # OS = -OSm (negative)
OSm = sp.Symbol('OSm', positive=True)
omega_minus_1 = Om1*H0**2/(ah**2*H2)
paper = Om1*ah**4/(OR*ah**2 - OSm)
print("(c) Omega(ahat)-1 matches paper Eq.(omega):", sp.simplify(omega_minus_1 - paper) == 0)

# (d) f(x) antiderivative
x = sp.symbols('x', positive=True)
f = x/2*sp.sqrt(x**2-1) + sp.Rational(1,2)*sp.log(x + sp.sqrt(x**2-1))
print("(d) f'(x) = x^2/sqrt(x^2-1) (the t-integrand):", sp.simplify(sp.diff(f, x) - x**2/sp.sqrt(x**2-1)) == 0)
# and dt relation: dt = da-hat/(a-hat |H|) ... = am^2/(H0 sqrt(OR)) * sqrt(x^2-1)^{-1} x^2 dx ... verify:
# |H| = H0 sqrt(OR) ah^-2 sqrt(1 - am^2/ah^2) with am^2 = OSm/OR  =>  t = int dah/(ah H)
am = sp.sqrt(OSm/OR)
Hmag = H0*sp.sqrt(OR)*ah**-2*sp.sqrt(1 - OSm/(OR*ah**2))
integrand = 1/(ah*Hmag)
sub = integrand.subs(ah, am*x)*am   # dah = am dx
expected = OSm/(OR**sp.Rational(3,2)*H0) * x**2/sp.sqrt(x**2-1)
print("(d) t-integrand matches -OS/(OR^{3/2}H0) * x^2/sqrt(x^2-1):",
      sp.simplify(sub - expected) == 0, " (and d f/dx * x^2/(x^2-1)... f' relation: int x^2/sqrt(x^2-1) = f)")
print("    int x^2/sqrt(x^2-1) dx = f(x):", sp.simplify(sp.diff(f, x)*0 + sp.integrate(x**2/sp.sqrt(x**2-1), x) - f) in (0, sp.S(0)) or sp.simplify(sp.diff(f,x) - x**2/sp.sqrt(x**2-1)) == 0)

# careful: f'(x) computed above was sqrt(x^2-1); but the t-integral needs x^2/sqrt(x^2-1).
print("    d/dx f =", sp.simplify(sp.diff(f, x)), " vs x^2/sqrt(x^2-1) =", sp.simplify(x**2/sp.sqrt(x**2-1)))

# (e) SI dimensions
kg, m_, s_ = sp.symbols('kg m s', positive=True)
J = kg*m_**2/s_**2
hbar, cc, n_, G = J*s_, m_/s_, m_**-3, m_**3/(kg*s_**2)
kappa_dim = G/cc**4 * 8*sp.pi
s2_dim = (hbar*cc*n_)**2/8
epsS_dim = kappa_dim*s2_dim
ratio = sp.simplify(epsS_dim/(J/m_**3))
print("(e) [kappa s^2]/(J/m^3) =", ratio, "-> dimensionless (pure number):", ratio.free_symbols == set())
