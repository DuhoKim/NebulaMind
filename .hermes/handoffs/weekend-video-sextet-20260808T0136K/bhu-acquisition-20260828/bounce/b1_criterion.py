#!/usr/bin/python3
"""B1 symbolic checks, two matter rows; run /usr/bin/python3 b1_criterion.py.

Requires SymPy (checked with 1.14.0). No file writes. C3 row tokens are
conjunctions of NO_PRODUCTION and PRODUCTION_THERMAL checks. A failed case
has no physical interpretation; its constraint roots are formal algebra only.
See B1_CRITERION_20260907.md for source comparisons and all assumptions.
"""
import sys
sys.dont_write_bytecode = True
import sympy as s


def zero(expr):
    if isinstance(expr, s.MatrixBase):
        return all(s.simplify(x) == 0 for x in expr)
    return s.simplify(expr) == 0


def main():
    k, hbar, a, eps, n, eps0, n0 = s.symbols(
        'kappa hbar a eps n eps_0 n_0', positive=True)
    AF, AD = s.symbols('alpha_F alpha_D', positive=True)
    S, Sigma2 = s.symbols('sigma2 Sigma2', nonnegative=True)
    H, Psi, J = s.symbols('H Psi J', real=True)
    beta = s.symbols('beta', nonnegative=True)
    g = s.diag(-1, 1, 1, 1)
    u = s.Matrix([-1, 0, 0, 0])
    uu = u*u.T
    ordinary = (eps + eps/3)*uu + eps/3*g
    qF, tauD2 = s.symbols('q_F_squared tau_D_squared', real=True)
    # RMP (3.23)-(3.24), evaluated in its printed (5.18)/(5.15).
    # q_F_squared denotes RMP's s^2; tau_D_squared = tau^{abc}tau_{abc}.
    rmpF = (eps + eps/3 - 2*k*qF)*uu + (eps/3-k*qF)*g
    rmpD = ordinary - k*tauD2*g/2
    # Check the Dirac dual-current contraction, independent of the density map.
    axial = s.symbols('axial_1:4', real=True)
    eta = (-1, 1, 1, 1)
    tau = {(i,j,l): sum(s.LeviCivita(i,j,l,m)*axial[m-1]/2
                       for m in range(1,4))
           for i in range(4) for j in range(4) for l in range(4)}
    tau_square = s.expand(sum(eta[i]*eta[j]*eta[l]*v**2
                              for (i,j,l),v in tau.items()))
    assert zero(tau_square + s.Rational(3,2)*sum(v**2 for v in axial))
    print('ALPHA_FLUID = kappa*hbar**2/32 (symbol alpha_F retained)')
    print('ALPHA_DIRAC = 9*kappa/16 (hbar=1; symbol alpha_D retained)')
    print('C = 3*H**2 - kappa*rho - sigma2')
    print('R_C = C_dot + 2*H*C = -kappa*(rho_dot+3*H*(rho+P))')
    print('R_C is C_dot on C=0; no division by H is used.')
    for row, alpha, sign, rmp in [('FLUID', AF, -1, rmpF),
                                   ('DIRAC', AD, 1, rmpD)]:
        rho = eps-alpha*n**2
        P = eps/3 + sign*alpha*n**2
        stress = (rho+P)*uu+P*g
        source = rmp.subs(qF, alpha*n**2/k) if row == 'FLUID' else \
            rmp.subs(tauD2, -2*alpha*n**2/k)
        c2res = s.simplify(stress-source)
        assert zero(c2res)
        # Independently check the published coefficient normalization.
        if row == 'FLUID':
            assert zero(rmp.subs(qF, hbar**2*n**2/32)
                        - stress.subs(alpha, k*hbar**2/32))
        else:
            assert zero(rmp.subs(tauD2, -s.Rational(9,8)*n**2)
                        - stress.subs(alpha, 9*k/16))
        print(f'C2_{row}=PASS')
        print(f'C2_COMPARED_TENSOR_{row} = {source}')
        print(f'C2_TENSOR_RESIDUAL_{row} = {c2res}')
        C = 3*H**2-k*rho-S
        Hdot = -H**2-2*S/3-k*(rho+3*P)/6
        adot, Sdot = a*H, -6*H*S
        # Geometric component check with all three Bianchi I directions.
        d1, d2 = s.symbols('d1 d2', real=True)
        d = [d1,d2,-d1-d2]
        geomS = sum(v**2 for v in d)/2
        Hi = [H+v for v in d]
        Hidot = [Hdot.subs(S,geomS)-3*H*v for v in d]
        G00 = Hi[0]*Hi[1]+Hi[1]*Hi[2]+Hi[2]*Hi[0]
        assert zero(G00-(3*H**2-geomS))
        for j,l in [(1,2),(0,2),(0,1)]:
            Gii = -(Hidot[j]+Hidot[l]+Hi[j]**2+Hi[l]**2+Hi[j]*Hi[l])
            assert zero(Gii-k*P+C.subs(S,geomS)/3)
        ndot = -3*H*n+Psi
        edot = -4*H*eps+J
        Cdot = (s.diff(C,H)*Hdot+s.diff(C,eps)*edot
                +s.diff(C,n)*ndot+s.diff(C,S)*Sdot)
        residual = s.factor(Cdot+2*H*C)
        energy = s.factor(edot-2*alpha*n*ndot+3*H*(rho+P))
        assert zero(residual+k*energy)
        no = s.factor(residual.subs({Psi:0,J:0}))
        add_only = s.factor(residual.subs(J,0))
        # GRG (34),(37) with fixed thermal coefficients implies this J.
        thermal = s.factor(residual.subs(J,4*eps*Psi/(3*n)))
        production = s.factor(thermal.subs(Psi,beta*H**4))
        no_ok, prod_ok = zero(no), zero(production)
        assert no_ok == (row == 'FLUID')
        assert not prod_ok
        print(f'ENERGY_RESIDUAL_GENERAL_{row} = {energy}')
        print(f'CONSTRAINT_RESIDUAL_GENERAL_{row} = {residual}')
        print(f'CONSTRAINT_RESIDUAL_NO_PRODUCTION_{row} = {no}')
        print(f'CONSTRAINT_RESIDUAL_PRODUCTION_NUMBER_ONLY_{row} = {add_only}')
        print(f'CONSTRAINT_RESIDUAL_PRODUCTION_THERMAL_{row} = {thermal}')
        print(f'CONSTRAINT_RESIDUAL_PRODUCTION_BETA_H4_{row} = {production}')
        print(f'C3_{row}_NO_PRODUCTION={"PASS" if no_ok else "FAIL"}')
        print(f'C3_{row}_PRODUCTION_NUMBER_ONLY=FAIL')
        print(f'C3_{row}_PRODUCTION_THERMAL={"PASS" if prod_ok else "FAIL"}')
        print(f'C3_{row}={"PASS" if no_ok and prod_ok else "FAIL"}')
        # Merely the necessary energy-balance equation, NOT an adopted repair.
        Jrequired = s.solve(energy,J)[0]
        print(f'REQUIRED_J_FOR_CONSERVATION_{row} = {Jrequired}')
        # The requested no-production algebra, even when C3 has failed.
        rhs = k*eps0/a**4+(Sigma2-k*alpha*n0**2)/a**6
        x = s.symbols('a_squared', positive=True)
        polynomial = s.expand(rhs*a**6).subs(a**2,x)
        root = s.solve(polynomial,x)[0]
        expected = (k*alpha*n0**2-Sigma2)/(k*eps0)
        assert zero(root-expected)
        assert zero(polynomial.subs(x,root))
        correction_ratio = s.factor((alpha*n0**2/(eps0*a**2)).subs(a**2,root))
        total_ratio = s.factor(Sigma2/(k*eps0*root))
        assert zero(correction_ratio-1-total_ratio)
        z = s.symbols('z', nonnegative=True)
        # Root domain is 0 <= z=Sigma2/(kappa*alpha*n_0**2) < 1.
        assert zero(correction_ratio.subs(Sigma2,z*k*alpha*n0**2)-1/(1-z))
        assert zero(1/(1-z)-s.Rational(1,10)-(9+z)/(10*(1-z)))
        assert zero((total_ratio-s.Rational(1,10)).subs(
            Sigma2,k*alpha*n0**2/11))
        torsion = -k*alpha*n0**2/a**6
        shear = Sigma2/a**6
        degenerate = zero(s.diff(a**6*torsion,a)) and zero(s.diff(a**6*shear,a))
        assert degenerate
        print(f'CRITERION_{row} = kappa*{alpha}*n_0**2 > Sigma2')
        print(f'A_MIN_{row} = sqrt({root})')
        print(f'RATIO_{row} = {correction_ratio}')
        print(f'TOTAL_DENSITY_RATIO_{row} = {total_ratio}')
        print(f'SCALING_DEGENERATE_{row}=YES')
        print(f'[{row}] SCALING_DEGENERATE=YES')
        print(f'RATIO_{row}_EXCEEDS_K3_0_1=YES')
        print(f'NO_PRODUCTION_ROOT_{row}={"SMOOTH_BOUNCE" if no_ok else "FORMAL_ONLY"}')
        if no_ok:
            at_root = s.factor(Hdot.subs({H:0,S:Sigma2/a**6,
                              eps:eps0/a**4,n:n0/a**3}).subs(a**2,root))
            assert zero(at_root-k*eps0/(3*root**2))
            print(f'H_DOT_AT_BOUNCE_{row} = kappa*eps_0/(3*a_min**4) > 0')
        else:
            print('DIRAC: stop physical interpretation; root and ratio are conditional algebra.')
    # Production pivot: symbolic derivatives, no trajectories or rescue test.
    Ndot = s.expand(3*a**2*(a*H)*n+a**3*(-3*H*n+Psi))
    Ctors_dot = s.simplify(k*AF*(2*n*(-3*H*n+Psi)*a**6
                                +6*n**2*a**5*(a*H)))
    assert zero(Ndot-a**3*Psi)
    assert zero(Ctors_dot-2*k*AF*n*a**6*Psi)
    print(f'PRODUCTION_N_COMOVING_DOT = {Ndot}')
    print(f'PRODUCTION_TORSION_COEFFICIENT_DOT_FLUID = {Ctors_dot}')
    print(f'PRODUCTION_TORSION_COEFFICIENT_DOT_DIRAC = {Ctors_dot.subs(AF,AD)}')
    print('SYMBOLIC_CHECKS=PASS')


if __name__ == '__main__':
    main()
