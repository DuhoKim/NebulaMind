"""p2b2-R3: shear vs the torsion term — the frozen-ratio result (sympy).
Setup (standard Bianchi-I-type anisotropic Friedmann bookkeeping; shear enters the
effective Friedmann equation as +Sigma^2 a^-6; the spin-fluid torsion term enters as
-(kappa/4) s^2 with s^2 = C n^2 and n ~ a^-3 [B1-derived], i.e. also ~ a^-6):
  H^2 = (kappa/3)[ eps_R0 a^-4 ] + [ Sigma^2 - (kappa/3)(kappa C n0^2/4) ] a^-6
Claims derived:
 (1) the shear/torsion ratio is a-INDEPENDENT (both a^-6): the bounce cannot change it;
 (2) a bounce exists iff the net a^-6 coefficient is negative, i.e. iff shear is ALREADY
     subdominant: Sigma^2 < (kappa^2 C/12) n0^2;
 (3) consequence: the bounce mechanism itself performs NO isotropization — any shear
     erasure must come from particle production (the heuristic step B-13), which is
     underived in the published chain."""
import sympy as sp
a, k, C, n0, S2, eR = sp.symbols('a kappa C n0 Sigma2 epsR0', positive=True)
shear_term  = S2*a**-6
torsion_term = -(k/3)*(k*C*n0**2/4)*a**-6
ratio = sp.simplify(shear_term/torsion_term)
print("(1) shear/torsion ratio =", ratio, " -> a-independent:", ratio.has(a) == False)
H2 = (k/3)*eR*a**-4 + (S2 - (k**2*C*n0**2/12))*a**-6
# bounce: H^2 = 0 at finite a with H^2 > 0 just above -> needs negative a^-6 coefficient
coeff = S2 - k**2*C*n0**2/12
am2 = sp.solve(sp.Eq(H2*a**6, 0), a**2)
print("(2) bounce root a_m^2 =", sp.simplify(am2[0]), " -> positive iff Sigma2 < kappa^2 C n0^2/12:",
      sp.simplify(am2[0] - (-coeff*3/(k*eR))) == 0)
print("(3) at the bounce, shear fraction of the torsion term equals its initial fraction")
print("    (frozen ratio): the bounce does not isotropize; production (B-13, heuristic) must.")
