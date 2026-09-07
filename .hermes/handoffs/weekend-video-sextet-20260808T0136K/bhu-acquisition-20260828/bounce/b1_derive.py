#!/usr/bin/python3
"""Bounded B1 derivation and C1 gate. No network or file writes.
Physics inputs: B1_PREREG_BIANCHI_I_BOUNCE_20260907.md and SOURCES_20260907.md.
Exit 1 means the requested published-recovery control failed.
"""
import sys
import sympy as s


def emit(label, expression):
    print(label + ' = ' + s.sstr(expression))


def main():
    print('B1: formal S1 system and C1 failure diagnostic only')
    assumptions = [
        'Use c=1, signature (+---), proper comoving time and zero cosmological constant.',
        'Replace S1 Eq. (6) KS geometry by diagonal Bianchi I: ds^2=dt^2-sum_i a_i(t)^2 dx_i^2; a_i>0, twice differentiable.',
        'Use an effective Levi-Civita Einstein equation G^mu_nu=kappa diag(rho_eff,-p_eff,-p_eff,-p_eff), extending S1 Eq. (1) to this geometry.',
        'Average the spin source into an isotropic perfect fluid: no residual anisotropic stress, heat flux or polarization-current terms; comoving flow is geodesic and irrotational.',
        'Treat alpha as a constant parameter in an unspecified interval [alpha_minus,alpha_plus]; no free-gas normalization is imposed.',
        'Use local effective energy conservation; no production means conserved comoving fermion number, n_dot+3H*n=0 (S1 Eq. (34), beta=0).',
        'For C1 comparison only use p=epsilon/3, epsilon=h_star*T^4, n=h_n*T^3 with fixed positive h_star,h_n and T>0, as in the quoted thermal formulas.',
        'Compare the same symbolic correction alpha*n^2 between sources without equating their printed numerical alpha prescriptions; use alpha>0 only to test the real S3 cusp.',
        'Bianchi I has zero spatial curvature; compare S3 also at k=0 to isolate the pressure mismatch from its published k=1 geometry.',
    ]
    print('EXPLICIT ADDED/MODEL ASSUMPTIONS (including choices transferred from sources):')
    for i, item in enumerate(assumptions, 1):
        print(str(i) + '. ' + item)

    t, x, y, z = s.symbols('t x y z', real=True)
    coords = (t, x, y, z)
    a_i = [s.Function('a' + str(i))(t) for i in range(1, 4)]
    g = s.diag(1, *[-ai**2 for ai in a_i])
    inv = g.inv()
    gamma = [[[s.simplify(sum(inv[r, l] * (
        s.diff(g[l, j], coords[i]) + s.diff(g[l, i], coords[j])
        - s.diff(g[i, j], coords[l])) for l in range(4))/2)
        for j in range(4)] for i in range(4)] for r in range(4)]
    ric = s.zeros(4)
    for i in range(4):
        for j in range(4):
            ric[i, j] = s.simplify(sum(
                s.diff(gamma[r][i][j], coords[r])
                - s.diff(gamma[r][i][r], coords[j])
                + sum(gamma[r][r][l]*gamma[l][i][j]
                      - gamma[r][j][l]*gamma[l][i][r] for l in range(4))
                for r in range(4)))
    mixed_ric = inv * ric
    ein = s.simplify(mixed_ric - s.eye(4)*s.trace(mixed_ric)/2)
    hi = s.symbols('H1 H2 H3', real=True)
    dhi = s.symbols('H1_dot H2_dot H3_dot', real=True)
    repl = {}
    for ai, h, dh in zip(a_i, hi, dhi):
        repl[s.diff(ai, t, 2)] = ai*(dh+h**2)
        repl[s.diff(ai, t)] = ai*h
    def geom(expr):
        return s.simplify(expr.subs(repl, simultaneous=True))
    print('Metric-derived components; H_i=a_i_dot/a_i:')
    emit('a', s.prod(a_i)**s.Rational(1, 3))
    for i in range(4):
        emit('R^' + str(i) + '_' + str(i), geom(mixed_ric[i, i]))
        emit('G^' + str(i) + '_' + str(i), geom(ein[i, i]))
    assert all(ein[i, j] == 0 for i in range(4) for j in range(4) if i != j)
    Hmean = sum(hi)/3
    shear = sum((h-Hmean)**2 for h in hi)/2
    emit('H', Hmean)
    emit('sigma^2', s.factor(shear))
    emit('constraint geometric identity residual', s.simplify(geom(ein[0, 0])-(3*Hmean**2-shear)))
    emit('sum H_i^2 identity residual', s.simplify(sum(h*h for h in hi)-3*Hmean**2-2*shear))
    kappa, eps, p, alpha, n, H, q = s.symbols('kappa epsilon p alpha n H sigma_squared', real=True)
    rho = eps-alpha*n**2
    peff = p-alpha*n**2
    emit('rho_eff [S1 (1)]', rho)
    emit('p_eff [S1 (1)]', peff)
    emit('Friedmann: 3H^2', kappa*rho+q)
    ray = -H**2-s.Rational(2, 3)*q-kappa*(rho+3*peff)/6
    emit('Raychaudhuri: H_dot', s.expand(ray))
    print('Step: R00=-sum(H_i_dot+H_i^2)=kappa*(rho_eff+3*p_eff)/2; divide by 3 and use the sum-of-squares identity.')
    print('Directional: a_i_dot=H_i*a_i; H_i_dot+3H*H_i=kappa*(rho_eff-p_eff)/2.')
    emit('directional common RHS', s.simplify(kappa*(rho-peff)/2))
    print('Subtract directional equations: d(H_i-H_j)/dt+3H*(H_i-H_j)=0. No scaling criterion evaluated before C1.')
    print('Effective continuity: d(rho_eff)/dt+3H*(rho_eff+p_eff)=0.')

    print('CONTROL C1: sigma^2=0, beta=0; compare S1 to S3 (10)-(17).')
    T, hs, hn, C = s.symbols('T h_star h_n C', positive=True)
    A = s.symbols('alpha_cusp', positive=True)
    # A is the positive portion of the symbolic alpha interval, not a chosen value.
    thermal_rho = hs*T**4-A*hn**2*T**6
    thermal_p1 = hs*T**4/3-A*hn**2*T**6
    thermal_p3 = hs*T**4/3+A*hn**2*T**6
    Td = s.symbols('T_dot', real=True)
    continuity1 = s.factor(s.diff(thermal_rho, T)*Td+3*H*(thermal_rho+thermal_p1))
    continuity3 = s.factor(s.diff(thermal_rho, T)*Td+3*H*(thermal_rho+thermal_p3))
    emit('S1 thermal continuity LHS', continuity1)
    emit('S3 thermal continuity LHS', continuity3)
    emit('S1 minus S3 continuity residual', s.factor(continuity1-continuity3))
    emit('S1 minus S3 effective pressure residual', s.expand(thermal_p1-thermal_p3))
    # Eq. (14) gives d(log(a))/dT; integrate rather than assume Eq. (15).
    dlog3 = -1/T + 3*A*hn**2*T/(2*hs)
    a3 = s.simplify(C*s.exp(s.integrate(dlog3, T)))
    a15 = C/T*s.exp(3*A*hn**2*T**2/(4*hs))
    tc = s.sqrt(2*hs/(3*A*hn**2))
    ac = C*s.sqrt(3*s.E*A*hn**2/(2*hs))
    r15 = s.simplify(a3-a15)
    r16 = s.simplify(s.diff(a3, T).subs(T, tc))
    r17 = s.simplify(a3.subs(T, tc)-ac)
    emit('integrated S3 (14) -> a(T), C=a_r*T_r', a3)
    emit('S3 (15) comparison residual', r15)
    emit('S3 (16) T_cr', tc)
    emit('S3 da/dT(T_cr) residual', r16)
    emit('S3 (17) a_cr', ac)
    emit('S3 (17) comparison residual', r17)
    internal_ok = all(r == 0 for r in (r15, r16, r17))
    print('S3_REFERENCE_ALGEBRA=' + ('PASS' if internal_ok else 'FAIL'))
    # Conserved n*a^3 with n=h_n*T^3 fixes a*T=C, including at the
    # isolated point where the S1 thermal-continuity coefficient vanishes.
    a1 = C/T
    da1tc = s.simplify(s.diff(a1, T).subs(T, tc))
    emit('S1 no-production temperature law', s.Eq(Td, -H*T))
    emit('S1 a(T)', a1)
    emit('S1 da/dT(T_cr) compared with S3 zero', da1tc)
    emit('S1 a(T_cr)/S3 a_cr compared with 1', s.simplify(a1.subs(T, tc)/ac))
    emit('S3 d(log(n*a^3))/dT compared with conserved-number zero', s.simplify(3/T+3*s.diff(a3, T)/a3))
    # A smooth stationary solution of the flat density constraint is a
    # diagnostic for C1, not the later anisotropic criterion.
    tstationary_sq = s.solve(thermal_rho/T**4, T**2)[0]
    emit('flat H=0: T^2 [S3 (23), not (16)]', tstationary_sq)
    emit('T_stationary^2/T_cr^2 compared with 1', s.simplify(tstationary_sq/tc**2))
    emit('alpha*n^2/epsilon at S3 (16)', s.simplify((A*hn**2*T**2/hs).subs(T, tc)))
    emit('flat H^2 at S3 T_cr', s.factor((kappa*thermal_rho/3).subs(T, tc)))
    recovered = internal_ok and s.simplify(thermal_p1-thermal_p3) == 0 and da1tc == 0
    print('C1=' + ('PASS' if recovered else 'FAIL'))
    if not recovered:
        print('STOP: S1 pressure correction and conserved-number temperature law do not recover S3 cusp. Matching S3 alone is not C1 recovery.')
        print('C2=NOT_RUN')
        print('C3=NOT_RUN')
        print('CRITERION=NOT_EVALUATED_C1_FAILED')
        return 1
    raise RuntimeError('Unexpected recovery: downstream work has not been authorized through this gate.')


if __name__ == '__main__':
    sys.exit(main())
