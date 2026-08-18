"""R10: invert the CMB rotation bound into parent-hole constraints (MODEL_SPEC frozen chain):
omega_0 = eps * Omega_H(M_p, a*) * f_b / D,  D = Z_inf^{n_inf} * Z_rad^{1} * Z_mat^{2}
(exponents n_rad=1, n_mat=2 derived in R6; n_inf in [1,2] parameterized per spec A6).
Bound: omega_0 < omega_max = 7.6e-10 * H0  =>  D > D_min = eps * Omega_H * f_b / omega_max.
Kerr: Omega_H = a* c^3 / (2 G M_p (1 + sqrt(1-a*^2)))  [standard; source-pin flagged in doc]."""
import math
G, c = 6.67430e-11, 2.99792458e8
Msun = 1.989e30
H0 = 67.4e3/3.0856775814913673e22
omega_max = 7.6e-10*H0
print(f"omega_max,0 (S2) = {omega_max:.3e} s^-1  (S1: {4.7e-11*H0:.3e})")
def OmH(M, astar):
    return astar*c**3/(2*G*M*(1+math.sqrt(1-astar**2)))
print("\nD_min = Omega_H/omega_max (eps=1, f_b=1):")
print("M_p [Msun]   a*     Omega_H [s^-1]   D_min          ln(D_min)")
for M, a in [(3,0.7),(10,0.7),(10,0.998),(1e6,0.7),(1e9,0.7),(1e9,0.1)]:
    d = OmH(M*Msun,a)/omega_max
    print(f"{M:10.0e}  {a:5.3f}  {OmH(M*Msun,a):.3e}     {d:.3e}   {math.log(d):.1f}")
# split D_min into known-ish late factors and the required early dilution:
# Z_mat = 1+z_eq (matter era exponent 2), z_eq ~ 3400 [standard value, flagged not pinned];
# remaining requirement on Z_inf^{n_inf} * Z_rad:
zeq = 3400
late = (1+zeq)**2
print(f"\nZ_mat^2 = (1+z_eq)^2 = {late:.2e}  [z_eq=3400 flagged standard, not pinned]")
for M, a in [(10,0.7),(1e9,0.7)]:
    d = OmH(M*Msun,a)/omega_max
    early = d/late
    print(f"M={M:.0e} Msun a*={a}: Z_inf^n_inf * Z_rad > {early:.2e}  "
          f"(if n_inf=2 and Z_rad=1: N_inf > {0.5*math.log(early):.1f} e-folds)")
# converse: constraint on eps*a*-combination at fixed total dilution D
print("\nconverse: eps * astar_eff < omega_max * D / (c^3/(2 G M_p))  at given D:")
for M in (10, 1e9):
    K = omega_max/(c**3/(2*G*M*Msun))
    for D in (1e20, 1e30, 1e40):
        print(f"  M_p={M:.0e} Msun, D={D:.0e}: eps*a*_eff < {K*D:.2e}"
              + ("  (no constraint: >1)" if K*D > 1 else "  BINDING"))
