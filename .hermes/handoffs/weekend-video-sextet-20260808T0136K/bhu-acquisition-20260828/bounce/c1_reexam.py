#!/usr/bin/python3
"""Row-specific C1 algebra. Run in bounce/: /usr/bin/python3 c1_reexam.py.

Uses the earlier B1 task's Bianchi I extension for C1_FLUID, not literal KS.
SymPy only; no file writes, numerical evolution, B1 criterion, or C2/C3.
"""
import sys
sys.dont_write_bytecode = True
import sympy as s

T, hs, hn, kappa, C, alpha_F, alpha_D, a, Y = s.symbols(
    "T h_star h_n kappa C alpha_F alpha_D a Y", positive=True)
H, Td, Hd, sigma2, curvature = s.symbols("H Tdot Hdot sigma2 k")
q = s.Rational


def zero(label, expression):
    residual = s.simplify(expression)
    print(f"{label}={residual}")
    assert residual == 0, label


def show(label, expression):
    print(f"{label}={s.simplify(expression)}")


eps, p, n = hs*T**4, hs*T**4/3, hn*T**3
rho_F, p_F = eps-alpha_F*n**2, p-alpha_F*n**2
rho_D, p_D = eps-alpha_D*n**2, p+alpha_D*n**2

# FLUID: GRG (1), (34), (37); earlier B1 Bianchi I extension.
print("C1_FLUID_SCOPE=EARLIER_B1_BIANCHI_I_EXTENSION")
number = s.diff(n, T)*Td+3*H*n
Td_F = s.solve(number, Td)[0]
show("FLUID_TDOT", Td_F)
continuity_F = s.diff(rho_F, T)*Td+3*H*(rho_F+p_F)
zero("FLUID_THERMAL_FACTORIZATION", continuity_F-
     (4*hs*T**3-6*alpha_F*hn**2*T**5)*(Td+H*T))
zero("FLUID_NUMBER_THERMAL_CONTINUITY", continuity_F.subs(Td, Td_F))
a_F = C*s.exp(s.integrate(-1/T, T))
zero("FLUID_A_OF_T", a_F-C/T)
zero("FLUID_COMOVING_NUMBER_DERIVATIVE", s.diff(n*a_F**3, T))
# Compare reduced mean equations directly to flat FLRW source equations.
constraint_BI = 3*H**2-kappa*rho_F-sigma2
acceleration_BI = Hd+H**2+q(2, 3)*sigma2+kappa*(rho_F+3*p_F)/6
zero("FLUID_ISOTROPIC_CONSTRAINT_MATCH",
     constraint_BI.subs(sigma2, 0)-(3*H**2-kappa*rho_F))
zero("FLUID_ISOTROPIC_ACCELERATION_MATCH",
     acceleration_BI.subs(sigma2, 0)-(Hd+H**2+kappa*(rho_F+3*p_F)/6))
Tb = s.solve(rho_F, T)[0]  # Unique positive-temperature zero.
zero("FLUID_TURNING_T_SQUARED", Tb**2-hs/(alpha_F*hn**2))
zero("FLUID_H_ZERO_CONSTRAINT", rho_F.subs(T, Tb))
Hdot_b = s.simplify((-kappa*(rho_F+3*p_F)/6).subs(T, Tb))
zero("FLUID_BOUNCE_ACCELERATION", Hdot_b-kappa*eps.subs(T, Tb)/3)
assert Hdot_b.is_positive
show("FLUID_HDOT_AT_BOUNCE", Hdot_b)
show("FLUID_A_AT_BOUNCE", a_F.subs(T, Tb))
show("FLUID_DADT_AT_BOUNCE", s.diff(a_F, T).subs(T, Tb))
show("FLUID_TURNING_T", Tb.subs(alpha_F, kappa/32))

# K3 analogue uses the correction, not GRG's tilde (which means total).
ratio_F = alpha_F*n**2/eps
R_b = s.simplify(ratio_F.subs(T, Tb).subs(alpha_F, kappa/32))
show("FLUID_RATIO_OF_T", ratio_F.subs(alpha_F, kappa/32))
assert R_b == 1
assert R_b >= q(1, 10)
print("FLUID_RATIO_GE_0_1=YES")
print("FLUID_RATIO_IS_SMALL_BELOW_0_1=NO")

# DIRAC: PRD (10)-(14), then integrate and compare (15)-(17).
continuity_D = s.diff(rho_D, T)*Td+3*H*(rho_D+p_D)
zero("DIRAC_THERMAL_CONTINUITY", continuity_D-
     ((4*hs*T**3-6*alpha_D*hn**2*T**5)*Td+4*hs*H*T**4))
log_slope = s.simplify(s.solve(continuity_D, H)[0]/Td)
zero("DIRAC_EQ14", log_slope-(-1/T+3*alpha_D*hn**2*T/(2*hs)))
a_D = C*s.exp(s.integrate(log_slope, T))
published_a = C/T*s.exp(3*alpha_D*hn**2*T**2/(4*hs))
zero("DIRAC_EQ15", a_D-published_a)
Tc = s.solve(log_slope, T)[0]
zero("DIRAC_EQ16", Tc-s.sqrt(2*hs/(3*alpha_D*hn**2)))
zero("DIRAC_CUSP_DADT", s.diff(a_D, T).subs(T, Tc))
zero("DIRAC_EQ17", a_D.subs(T, Tc)-C*s.sqrt(3*s.E*alpha_D*hn**2/(2*hs)))
assert s.simplify(s.diff(a_D, T, 2).subs(T, Tc)).is_positive
show("DIRAC_TCR", Tc.subs(alpha_D, 9*kappa/16))

# Same-row diagnostics: these extra requirements are not the cusp test.
show("DIRAC_DLOG_COMOVING_NUMBER_DTEMPERATURE", s.diff(s.log(n*a_D**3), T))
show("DIRAC_CONTINUITY_IF_NUMBER_CONSERVED", continuity_D.subs(Td, -H*T))
H2_cusp = s.simplify((kappa*rho_D/3).subs(T, Tc))
show("DIRAC_FLAT_H_SQUARED_AT_CUSP", H2_cusp)
assert H2_cusp.is_positive
Tst = s.solve(rho_D, T)[0]
zero("DIRAC_EQ23", Tst**2-hs/(alpha_D*hn**2))
show("DIRAC_TST_SQUARED_OVER_TCR_SQUARED", Tst**2/Tc**2)
show("DIRAC_CLOSED_H_SQUARED_AT_CUSP", H2_cusp-1/a_D.subs(T, Tc)**2)

# Geometry caveat only: GRG (11) after X=lambda*Y over a time interval.
# Xddot/X=Yddot/Y, Xdot/X=Ydot/Y, hence residual -1/Y^2.
show("LITERAL_KS_EQ11_SHEAR_FREE_RESIDUAL", -1/Y**2)
# Flat T_b and R_b are not universal closed-FLRW values.
show("FLUID_CURVED_TURNING_EQUATION",
     s.expand((kappa*rho_F/3-curvature/a_F**2)*3/(kappa*T**2)))

print("C1_FLUID=PASS")
print("C1_DIRAC=PASS")
print(f"FLUID_RATIO_AT_TURNING_POINT={R_b}")
print("ORIGINAL_C1_FAIL=WITHDRAWN")
