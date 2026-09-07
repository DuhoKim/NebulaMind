#!/usr/bin/python3
"""ECSK auxiliary-connection elimination and Weyssenhoff metric variation.

Run from this directory: /usr/bin/python3 ecsk_derive.py
Requires SymPy. No files are opened or written; bytecode caching is disabled.
Signature (-+++), full torsion T = 2 Gamma_[mu nu], positive kappa.
All tensor arrays below have LOWER indices; contractions include eta signs.
"""

import sys
sys.dont_write_bytecode = True

from itertools import product
import sympy as sp


def main():
    d = range(4)
    triples = list(product(d, repeat=3))
    independent = [(a, b, c) for a, b, c in triples if a < b]
    eta = (-1, 1, 1, 1)
    kappa = sp.Symbol('kappa', positive=True)

    def antisymmetric_array(prefix):
        vals = {i: sp.Symbol(prefix + ''.join(map(str, i)), real=True)
                for i in independent}
        return {i: (vals[i] if i[0] < i[1] else
                    -vals[i[1], i[0], i[2]] if i[0] > i[1] else sp.S.Zero)
                for i in triples}, list(vals.values())

    A, variables = antisymmetric_array('A')
    tau, _ = antisymmetric_array('tau')

    def dot(X, Y):
        return sum(eta[a] * eta[b] * eta[c] * X[a, b, c] * Y[a, b, c]
                   for a, b, c in triples)

    def trace_spin(X):
        return [sum(eta[b] * X[a, b, b] for b in d) for a in d]

    def q_gravity(X):
        V = [sum(eta[a] * X[a, b, a] for a in d) for b in d]
        return -sum(eta[b] * V[b]**2 for b in d) - sum(
            eta[a] * eta[b] * eta[c] * X[a, b, c] * X[b, c, a]
            for a, b, c in triples)

    def solve_formula(X):
        t = trace_spin(X)
        return {(a, b, c): kappa / 2 * (
            X[b, c, a] + X[c, a, b] - X[a, b, c]
            - (eta[a] * t[b] if a == c else 0)
            + (eta[b] * t[a] if b == c else 0))
            for a, b, c in triples}

    Q = sp.expand(q_gravity(A))
    Laux = Q / (2 * kappa) + dot(tau, A) / 2
    solution = solve_formula(tau)
    substitution = {A[i]: solution[i] for i in independent}
    equations = [sp.diff(Laux, v) for v in variables]
    assert all(sp.expand(e.xreplace(substitution)) == 0 for e in equations)
    # A nonsingular 24 x 24 Hessian proves unique algebraic elimination.
    hessian_rank = sp.hessian(Q, variables).rank()
    assert hessian_rank == 24

    t = trace_spin(tau)
    I = dot(tau, tau)
    J = sum(eta[a] * eta[b] * eta[c] * tau[a, b, c] * tau[b, c, a]
            for a, b, c in triples)
    F = 2 * J - I + 2 * sum(eta[a] * t[a]**2 for a in d)
    Lcontact = sp.expand(Laux.xreplace(substitution))
    assert sp.expand(Lcontact - kappa * F / 8) == 0
    assert sp.expand(Lcontact - dot(tau, solution) / 4) == 0

    # Check the FULL torsion equation, including nonzero spin trace.
    T = {(c, a, b): eta[c] * (solution[c, b, a] - solution[c, a, b])
         for c, a, b in triples}
    Ttrace = [sum(T[b, a, b] for b in d) for a in d]
    assert all(sp.expand(Ttrace[a] - kappa * t[a] / 2) == 0 for a in d)
    assert all(sp.expand(
        T[c, a, b] + (Ttrace[b] if c == a else 0)
        - (Ttrace[a] if c == b else 0) + kappa * eta[c] * tau[a, b, c]
    ) == 0 for c, a, b in triples)

    # Weyssenhoff current in a local rest frame: u^a=(1,0,0,0).
    x, y, z = sp.symbols('s12 s23 s31', real=True)
    s = sp.Matrix([[0, 0, 0, 0], [0, 0, x, -z],
                   [0, -x, 0, y], [0, z, -y, 0]])
    u_lower = (-1, 0, 0, 0)
    fluid_tau = {(a, b, c): s[a, b] * u_lower[c] for a, b, c in triples}
    fluid_A = solve_formula(fluid_tau)
    s2 = x**2 + y**2 + z**2
    fluid_Q = sp.expand(q_gravity(fluid_A))
    fluid_coupling = sp.expand(dot(fluid_tau, fluid_A) / 2)
    fluid_L = sp.expand(fluid_Q / (2 * kappa) + fluid_coupling)
    assert sp.expand(fluid_Q + kappa**2 * s2 / 2) == 0
    assert sp.expand(fluid_coupling - kappa * s2 / 2) == 0
    assert sp.expand(fluid_L - kappa * s2 / 4) == 0

    # Derive density dependence at fixed particle current and spin/particle.
    n, C, hbar = sp.symbols('n C hbar', positive=True)
    Ls = fluid_L.subs({x: n * x, y: n * y, z: n * z})
    Ls = sp.expand(Ls).subs(x**2, C - y**2 - z**2).expand()
    assert Ls == kappa * C * n**2 / 4
    # delta n = n/2 (g_mn + u_m u_n) delta g^mn.
    # Therefore T_mn = Ls*g_mn - n*dLs/dn*(g_mn+u_m*u_n).
    metric = sp.diag(*eta)
    u = sp.Matrix(u_lower)
    projector = metric + u * u.T
    Ts = sp.simplify(Ls * metric - n * sp.diff(Ls, n) * projector)
    eps_s = sp.simplify(Ts[0, 0])
    p_s = sp.simplify(sum(Ts[i, i] for i in range(1, 4)) / 3)
    w = sp.simplify(p_s / eps_s)
    assert p_s == n * sp.diff(eps_s, n) - eps_s
    assert w == 1

    # Independent lapse/scale-factor variation, fixed comoving number N.
    lapse, a, number = sp.symbols('N_lapse a N_particles', positive=True)
    mini_L = lapse * a**3 * Ls.subs(n, number / a**3)
    mini_eps = -sp.diff(mini_L, lapse) / a**3
    mini_p = sp.diff(mini_L, a) / (3 * lapse * a**2)
    assert sp.simplify(mini_eps - eps_s.subs(n, number/a**3)) == 0
    assert sp.simplify(mini_p - p_s.subs(n, number/a**3)) == 0

    H = sp.Symbol('H', real=True)
    eps_dot = sp.diff(eps_s, n) * (-3 * H * n)
    continuity = sp.simplify(eps_dot + 3 * H * (eps_s + p_s))
    wrong_continuity = sp.simplify(eps_dot + 3 * H * (eps_s - eps_s))
    assert continuity == 0
    assert sp.simplify(wrong_continuity + 6 * H * eps_s) == 0

    print('Conventions: (-+++); kappa > 0; T = 2 Gamma_[mu nu]')
    print('Algebraic contortion Hessian rank:', hessian_rank, '/ 24')
    print('All 24 connection variations and all torsion components: PASS')
    print('General eliminated L_contact = kappa*(2*J - I + 2*t^2)/8: PASS')
    print('Weyssenhoff Q =', fluid_Q)
    print('Weyssenhoff L_contact =', fluid_L)
    print('Use <s^2> = C*n^2, with C constant and positive.')
    print('eps_s =', eps_s)
    print('p_s   =', p_s)
    print('w =', w)
    print('Rest-frame T_s =', Ts)
    print('For the conventional closure C = hbar^2/8:')
    print('eps_s =', eps_s.subs(C, hbar**2 / 8))
    print('p_s   =', p_s.subs(C, hbar**2 / 8))
    print('Lapse and scale-factor variations: PASS')
    print('Continuity residual =', continuity)
    print('Opposite-pressure trial residual =', wrong_continuity)
    print('Pressure and energy-density corrections have the SAME sign.')


if __name__ == '__main__':
    main()
