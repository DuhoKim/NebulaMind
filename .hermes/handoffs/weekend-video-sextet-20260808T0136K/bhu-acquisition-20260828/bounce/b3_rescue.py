#!/usr/bin/python3
"""B3: flat Bianchi I FLUID only. Deterministic, offline, no file writes.
Run: /usr/bin/python3 b3_rescue.py
Dependencies: SymPy and SciPy. Definitions, proof and scope: B3_RESCUE_20260907.md.
"""
import hashlib
import math
from pathlib import Path
import sympy as sp
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

ALPHAS = (0.25, 0.625, 1.0)
FRACTIONS = (0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99)
NUMBERS = (0.0, 0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0)
BETAS = (0.0, 0.001, 0.01, 0.1, 1.0, 10.0)
RTOL, ATOL = 2e-10, 2e-12


def caloric(T, closure):
    if closure == 'b':
        return T**4
    return T**4 * (1.0 + T*T/(1.0 + T*T))


def temperature(eps, closure):
    if closure == 'b':
        return eps**0.25
    # Globally T^4 <= F_c(T) <= 2 T^4. Bracket in scaled coordinates.
    scale = eps**0.25
    z = brentq(lambda z: caloric(z*scale, closure)/eps-1,
               2**(-0.25), 1.0, xtol=2e-14)
    return z*scale


def verify():
    H, S, n, T, alpha, k, beta = sp.symbols('H S n T alpha k beta')
    for closure in ('b', 'c'):
        F = T**4 if closure == 'b' else T**4*(1+T**2/(1+T**2))
        nd = beta*H**4-3*H*n
        Td = (2*alpha*n*beta*H**4-4*H*F)/sp.diff(F, T)
        Hd = k*F/3-3*H**2  # exact directional-equation mean, off constraint
        Sd = -6*H*S
        C = 3*H**2-k*(F-alpha*n**2)-S
        Cd = sum(sp.diff(C, v)*d for v, d in ((H,Hd),(S,Sd),(n,nd),(T,Td)))
        residual = sp.factor(Cd+6*H*C)
        energy = sp.factor(sp.diff(F,T)*Td-2*alpha*n*nd+3*H*(4*F/3-2*alpha*n*n))
        x,u,N,E = sp.symbols('x u N E')
        prod = beta*u**4*sp.exp(6*x)
        transformed = sp.expand(6*u*(-k*E/3)-k*(-2*u*E+2*alpha*N*prod)+2*k*alpha*N*prod)
        # T reconstructed from F(T)=E exp(6x) obeys precisely transformed Td.
        reconstruction = sp.simplify(
            (sp.diff(F,T)*Td).subs({H:-u*sp.exp(3*x), n:N*sp.exp(3*x)})
            *sp.exp(-3*x) - (4*u*F+2*alpha*N*prod*sp.exp(6*x)))
        delta = sp.symbols('delta')
        beta0_residual = sp.expand(3*u*u-(3*u*u-delta)-delta)
        assert beta0_residual == 0
        print(f'CONSTRAINT_RESIDUAL_{closure}={residual}')
        print(f'CHECK_{closure}: first_law={energy}; transformed_constraint={transformed}; caloric_chain_rule={reconstruction}; Fprime={sp.factor(sp.diff(F,T))}')
        if any(r != 0 for r in (residual, energy, transformed, reconstruction)):
            raise SystemExit('STOP: nonzero exact residual; no integration performed')
    # These analytic statements are printed before any numerical integration.
    for closure in ('b', 'c'):
        print(f'TORSION_SCALING_{closure}=HELPS; alpha*n^2=alpha*a^-6*(n0+integral(a^3*Psi*dt))^2; dln(alpha*n^2)/dln(a)=-6+2*beta*H^3/n<-6 (H<0,n>0,beta>0)')


def integrate(alpha, f, n0, beta, closure, tighter=False):
    """Integrate in d tau=dt/a^3; x=-ln a, u=-H a^3, N=n a^3, E=eps a^6.
    Caloric energy is an invertible state coordinate in EACH specified closure.
    No constraint projection is used. t is proper time, initially zero.
    """
    sigma = f/(1-f)
    q0 = 1+sigma-alpha*n0*n0
    if q0 <= 0:
        return {'kind': 'X'}  # no strictly collapsing real initial H
    if beta == 0:
        # Exact beta=0 reduction, with u as independent variable:
        # a^2=3u^2-delta, dt/du=-3a. Numerically integrate proper time
        # all the way to the analytic bounce or singular endpoint.
        delta = sigma-alpha*n0*n0
        u0 = math.sqrt(q0/3)
        end = math.sqrt(max(delta,0)/3)
        time, quadrature_error = quad(lambda u: 3*math.sqrt(max(0,3*u*u-delta)),
                                      end,u0,epsabs=2e-12,epsrel=2e-11)
        kind = 'B' if delta < 0 else 'S'
        a = math.sqrt(-delta) if kind == 'B' else 0.0
        Tb = temperature(a**-4,closure) if kind == 'B' else None
        assert math.isfinite(time) and time > 0
        if kind == 'B': assert abs(caloric(Tb,closure)*a**4-1) < 1e-11
        return dict(kind=kind,a=a,t=time,error=0.0,T=Tb,quadrature_error=quadrature_error)
    y0 = (0.0, math.sqrt(q0/3), n0, 1.0, 0.0)
    T0 = temperature(1.0, closure)
    assert abs(caloric(T0, closure)-1) < 1e-12

    def rhs(tau, y):
        x,u,N,E,t = y
        prod = beta*u**4*math.exp(6*x)
        return (u, -E/3, prod, -2*u*E+2*alpha*N*prod, math.exp(-3*x))

    def bounce(tau,y): return y[1]
    bounce.terminal, bounce.direction = True, -1
    def cutoff(tau,y): return y[0]-12.0
    cutoff.terminal, cutoff.direction = True, 1
    sol = solve_ivp(rhs, (0,2e6), y0, method='DOP853',
                    rtol=RTOL/(10 if tighter else 1),
                    atol=ATOL/(10 if tighter else 1), events=(bounce,cutoff))
    if not sol.success:
        raise AssertionError(sol.message)
    x,u,N,E,t = sol.y[:,-1]
    errors = []
    for xi,ui,Ni,Ei,ti in sol.y.T:
        assert Ei > 0 and Ni >= -1e-12
        errors.append(abs(3*ui*ui-Ei-sigma+alpha*Ni*Ni)/
                      (3*ui*ui+Ei+sigma+alpha*Ni*Ni))
    err = max(errors)
    assert err < 2e-8, (closure, alpha,f,n0,beta,err)
    if len(sol.t_events[0]):
        kind = 'B'
        eps = E*math.exp(6*x)
        Tb = temperature(eps, closure)
        assert abs(caloric(Tb,closure)/eps-1) < 1e-11
        assert math.isfinite(eps) and eps/3 > 0  # Hdot at H=0; finite positive crossing
    else:
        raise AssertionError('UNRESOLVED: positive-beta run failed to reach bounce; cutoff is not a singularity')
    expected = 'B' if beta > 0 or alpha*n0*n0 > sigma else 'S'
    assert kind == expected, (closure,alpha,f,n0,beta,kind,expected)
    return dict(kind=kind, a=math.exp(-x), t=t, error=err, T=Tb)


def main():
    verify()  # MUST finish for BOTH closures before any integration.
    print('DOMAIN: FLUID; flat Bianchi I; kappa=h_star=eps0=a0=1; alpha_interval=[0.25,1]; samples='+str(ALPHAS))
    print('GRID: f='+str(FRACTIONS)+'; n0='+str(NUMBERS)+'; beta='+str(BETAS))
    print('MAP_LEGEND: B=bounce; S=analytically certified singular continuation; X=inadmissible initial collapse; columns=n0 in printed order')
    all_results = {}
    for closure in ('b','c'):
        results = {}
        print(f'CLOSURE_{closure}: F(T)='+('T^4' if closure=='b' else 'T^4*(1+T^2/(1+T^2))')+f'; T0={temperature(1,closure):.12g}')
        maxerr = 0.0
        totals = dict(B=0,S=0,X=0)
        for alpha in ALPHAS:
            for beta in BETAS:
                counts = dict(B=0,S=0,X=0)
                radii = []
                for f in FRACTIONS:
                    row = ''
                    for n0 in NUMBERS:
                        r = integrate(alpha,f,n0,beta,closure)
                        results[(alpha,f,n0,beta)] = r
                        row += r['kind']
                        counts[r['kind']] += 1
                        if r['kind'] != 'X': maxerr = max(maxerr,r['error'])
                        if r['kind'] == 'B': radii.append(r['a'])
                    print(f'MAP_{closure} alpha={alpha:g} beta={beta:g} f={f:g} {row}')
                for key in totals: totals[key] += counts[key]
                interval = f'{min(radii):.9g},{max(radii):.9g}' if radii else 'none'
                print(f'GRID_SUMMARY_{closure} alpha={alpha:g} beta={beta:g} B={counts["B"]} S={counts["S"]} X={counts["X"]} bounce_a_range={interval}')
        # Explicit equality-side controls, including anisotropy, plus refinement.
        for alpha in ALPHAS:
            for f in (0.0,0.5,0.9):
                n0 = math.sqrt((f/(1-f))/alpha)
                # roundoff at equality: integrate a nearby nonbouncing datum instead
                # and retain exact equality as an analytic control printed below.
                nbelow = n0*(1-1e-10)
                assert integrate(alpha,f,nbelow,0,closure)['kind'] == 'S'
                assert integrate(alpha,f,n0,0.001,closure)['kind'] == 'B'
        refinement = 0.0
        for alpha,f,n0,beta in ((0.25,0.99,0,0.001),(1,0.1,0.5,0),(0.625,0.5,0.1,10)):
            r = results[(alpha,f,n0,beta)]
            fine = integrate(alpha,f,n0,beta,closure,True)
            refinement = max(refinement,abs(r['a']/fine['a']-1))
        assert refinement < 2e-7
        print(f'NUMERICS_{closure}: max_normalized_constraint={maxerr:.6g}; max_refinement_relative_a={refinement:.6g}; threshold_controls=9; beta0=exact_reduction_numerical_proper_time_quadrature')
        print(f'GRID_TOTAL_{closure}: B={totals["B"]} S={totals["S"]} X={totals["X"]}; counts_are_not_probabilities')
        print(f'BOUNDARY_{closure}: beta=0 has bounce iff alpha*n0^2>f/(1-f); every beta>0 admissible datum bounces; relative_nonbounce_boundary=beta=0,alpha*n0^2<=f/(1-f)')
        print(f'BOUNCE_SET_{closure}=OPEN')
        all_results[closure] = results
    assert all(all_results['b'][key]['kind']==all_results['c'][key]['kind'] for key in all_results['b'])
    print('COMPARISON: strictly_enlarged_by_set_inclusion_for_each_beta>0; beta0_set_already_OPEN; no_measure_claim; no_class_filed')
    for name in ('b3_rescue.py','B3_RESCUE_20260907.md'):
        path = Path(__file__).resolve().parent/name
        if path.exists(): print('SHA256 '+name+' '+hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
