"""R7: EdS spherical-collapse quantities used by the transfer function, derived (not cited):
(a) overdensity at turnaround = 9 pi^2/16;
(b) rotational-support rate at turnaround omega_0 = sqrt(GM/R_ta^3) = (3 pi/(4 sqrt(2))) H_ta."""
import sympy as sp
theta, G, M, A, B = sp.symbols('theta G M A B', positive=True)
# cycloid solution of the closed patch: R = A(1-cos th), t = B(th - sin th), with A^3 = G M B^2
R = A*(1 - sp.cos(theta)); t = B*(theta - sp.sin(theta))
# patch density and EdS background density rho_bar = 1/(6 pi G t^2)
rho_patch = 3*M/(4*sp.pi*R**3)
rho_bar = 1/(6*sp.pi*G*t**2)
ratio = sp.simplify((rho_patch/rho_bar).subs(A, (G*M*B**2)**sp.Rational(1,3)))
ratio_ta = sp.simplify(ratio.subs(theta, sp.pi))
print("rho_patch/rho_bar at turnaround (theta=pi):", ratio_ta, "=", float(ratio_ta))
print("equals 9 pi^2/16:", sp.simplify(ratio_ta - 9*sp.pi**2/16) == 0)
# omega_0 = sqrt(GM/R_ta^3); H^2 = 8 pi G rho_bar/3 (EdS)
H2 = 8*sp.pi*G*rho_bar/3
GM_over_R3 = sp.simplify((G*M/R**3).subs(A, (G*M*B**2)**sp.Rational(1,3)).subs(theta, sp.pi))
c2 = sp.simplify(GM_over_R3/H2.subs(theta, sp.pi))
# express both at same t (theta=pi): substitute t at theta=pi
c2 = sp.simplify((G*M/R**3 / H2).subs(A, (G*M*B**2)**sp.Rational(1,3)).subs(theta, sp.pi))
print("(GM/R_ta^3)/H_ta^2 =", c2, "=", float(c2), " -> sqrt =", float(sp.sqrt(c2)))
print("equals 9 pi^2/32:", sp.simplify(c2 - 9*sp.pi**2/32) == 0)
