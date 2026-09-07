#!/usr/bin/python3
"""B7: curved Kantowski--Sachs FLUID, B2 closures (b) and (c).

Run: /usr/bin/python3 b7_curved.py
Requires the already installed numpy, scipy, sympy. No network or file writes.
Numerical quantities are dimensionless; see B7_CURVED_20260907.md for units.
Closure (b) integrates T. Closure (c) integrates the exact energy coordinate
e=F(T), valid for every specified regular F on the energy range traversed.
No n(T) relation, creation pressure, or constraint projection is imposed.
"""
import sys
sys.dont_write_bytecode = True
import hashlib
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import solve_ivp
import sympy as sp

HERE = Path(__file__).resolve().parent
SOURCE_SHA = "fb94da36db11823ed1081fd39226a7134dec64883a7811c4011a1ea7234efc88"
ALPHAS = (0.25, 0.5, 1.0)
BETAS = (0.01, 0.1, 1.0)


def exact_checks():
    u, v, K, e, n, a, b, k = sp.symbols("u v K epsilon n alpha beta kappa")
    T, hs, F, Fp = sp.symbols("T h_star F Fprime", nonzero=True)
    H = (u + 2*v)/3
    D = u-v
    S = D**2/3
    rho, P = e-a*n*n, e/3-a*n*n
    C = v*v+2*u*v+K-k*rho
    psi = b*H**4
    fu = -u*u-u*v+(v*v+K-k*P)/2
    fv = -(3*v*v+K+k*P)/2
    fn = psi-3*H*n
    fe = 2*a*n*psi-4*H*e
    state = (u, v, K, e, n)
    flow = (fu, fv, -2*v*K, fe, fn)

    def dot(q):
        return sum(sp.diff(q, x)*f for x, f in zip(state, flow))

    def zero(label, q):
        r = sp.factor(q)
        print(label + "=" + str(r))
        assert r == 0, (label, r)

    # Verify the actual spatial-equation extension, including off C=0.
    for closure in ("b", "c"):
        if closure == "b":
            et = hs*T**4
            td = (2*a*n*psi-4*H*et)/(4*hs*T**3)
            ed = 4*hs*T**3*td
        else:
            et = F
            td = (2*a*n*psi-4*H*F)/Fp
            ed = Fp*td
        zero("closure_"+closure+"_energy_residual",
             ed-2*a*n*fn+3*H*(4*et/3-2*a*n*n))
        # Apply the chain rule with this closure's own temperature/energy rate.
        cd = sum(sp.diff(C,x)*fx for x,fx in zip(state,flow) if x != e)
        cd = cd.subs(e,et) + sp.diff(C,e)*ed
        zero("closure_"+closure+"_constraint_propagation_residual",
             cd+3*H*C.subs(e,et))
    zero("signed_shear_residual", dot(D)+3*H*D-K)
    zero("comoving_shear_residual", dot(S)+6*H*S-2*K*D/3)
    ray = -H*H-2*S/3-k*e/3+2*k*a*n*n/3
    zero("raychaudhuri_off_constraint_residual", dot(H)-ray+C/6)
    zero("turn_margin_off_constraint_residual",
         dot(H)-(-2*H*H+(k*a*n*n-S-K)/3)-C/6)
    R = k*a*n*n/S
    zero("fractional_race_residual", dot(R)/R-2*(psi/n-K/D))
    J = 2*k*a*n*n-2*S-k*e
    zero("eq32_margin_evolution_residual",
         dot(J)+6*H*J+2*H*k*e-2*k*a*n*psi+4*K*D/3)
    geometric_trace = 2*(fu+u*u+2*(fv+v*v)+2*u*v+v*v+K)
    zero("ricci_trace_off_constraint_residual", geometric_trace-2*k*a*n*n-C)
    delta = sp.symbols("Delta")
    hdd = sp.expand(dot(dot(H)))
    boundary = hdd.subs({u:2*delta/3, v:-delta/3, e:2*K/k})
    boundary = boundary.subs(n**2,(K+delta**2/3)/(k*a))
    zero("degenerate_H_second_derivative_residual", boundary+4*K*delta/9)
    hthird = sp.expand(dot(hdd)).subs({u:0,v:0,e:2*K/k})
    zero("degenerate_H_third_derivative_residual",
         hthird.subs(n**2,K/(k*a))+4*K*K/9)


def physical(y, closure):
    lx, ly, u, v, n, z = y[:6]
    e = z**4 if closure == "b" else z
    H, D = (u+2*v)/3, u-v
    K, V = np.exp(-2*ly), np.exp(lx+2*ly)
    return lx, ly, u, v, n, e, H, D, K, V


def rhs(closure, a, b):
    def f(t, y):
        lx, ly, u, v, n, e, H, D, K, V = physical(y, closure)
        P = e/3-a*n*n
        psi = b*H**4
        ed = 2*a*n*psi-4*H*e
        zd = ed/(4*y[5]**3) if closure == "b" else ed
        return np.array([u, v, -u*u-u*v+(v*v+K-P)/2,
                         -(3*v*v+K+P)/2, psi-3*H*n, zd,
                         V*H**4, np.exp(lx)])
    return f


def initial(closure, a, spec):
    H, D, K, w = spec
    if not (a > 0 and K > 0 and w > 0 and H < 0):
        raise ValueError("INADMISSIBLE_INITIAL_DATA: require A,K,w>0 and H<0")
    e = 3*H*H-D*D/3+K+w
    if e <= 0:
        raise ValueError("INADMISSIBLE_INITIAL_DATA: ordinary energy <= 0")
    z = e**0.25 if closure == "b" else e
    return np.array([0., -0.5*math.log(K), H+2*D/3, H-D/3,
                     math.sqrt(w/a), z, 0., 0.])


def diagnostics(t, yy, closure, a, b, y0):
    lx, ly, u, v, n, e, H, D, K, V = physical(yy, closure)
    w, S = a*n*n, D*D/3
    C = v*v+2*u*v+K-e+w
    scale = 1+v*v+2*np.abs(u*v)+K+e+w
    f = rhs(closure, a, b)
    ff = np.stack([f(tt, y) for tt, y in zip(t, yy.T)], axis=1)
    # Orthonormal KS curvature invariant; a large finite value is NOT an event.
    kretsch = 4*((ff[2]+u*u)**2+2*(ff[3]+v*v)**2
                +2*(u*v)**2+(v*v+K)**2)
    q0 = physical(y0, closure)
    N0, D0V0 = q0[4]*q0[9], q0[7]*q0[9]
    rN = n*V-N0-b*yy[6]
    rD = D*V-D0V0-yy[7]
    return dict(absC=float(np.max(np.abs(C))),
                relC=float(np.max(np.abs(C)/scale)),
                Nres=float(np.max(np.abs(rN)/(1+np.abs(n*V)))),
                Dres=float(np.max(np.abs(rD)/(1+np.abs(D*V)))),
                maxKretsch=float(np.max(kretsch)),
                minX=float(np.min(np.exp(lx))), minY=float(np.min(np.exp(ly))),
                minE=float(np.min(e)), minN=float(np.min(n)))


def integrate(closure, a, b, spec, tight=True, cap=1e7, tmax=2.):
    if b < 0 or not np.isfinite(b):
        raise ValueError("INADMISSIBLE_PARAMETER: beta must be finite and >=0")
    y0 = initial(closure, a, spec)
    f = rhs(closure, a, b)

    def turn(t, y):
        return (y[2]+2*y[3])/3
    turn.direction, turn.terminal = 1, True

    def cutoff(t, y):
        e = y[5]**4 if closure == "b" else y[5]
        return cap-max(abs(y[2]), abs(y[3]), abs(y[4]), abs(e))
    cutoff.direction, cutoff.terminal = -1, True

    rtol, atol, step = (2e-12, 2e-14, .002) if tight else (2e-9, 2e-11, .01)
    sol = solve_ivp(f, (0., tmax), y0, method="DOP853", dense_output=True,
                    rtol=rtol, atol=atol, max_step=step, events=(turn, cutoff))
    if not sol.success:
        status = "INTEGRATION_FAILURE"
    elif len(sol.t_events[0]):
        status = "REGULAR_TURN"
    elif len(sol.t_events[1]):
        status = "FINITE_CUTOFF_UNRESOLVED"
    else:
        status = "NO_EVENT_ON_FINITE_WINDOW"
    times = np.unique(np.concatenate((sol.t, np.linspace(0., sol.t[-1], 1001))))
    yy = sol.sol(times)
    out = diagnostics(times, yy, closure, a, b, y0)
    end = physical(sol.y[:, -1], closure)
    lx, ly, u, v, n, e, H, D, K, V = end
    margin = a*n*n-D*D/3-K
    out.update(status=status, t=float(sol.t[-1]), H=float(H),
               R=float(3*a*n*n/(D*D)), K=float(K), e=float(e),
               X=float(np.exp(lx)), Y=float(np.exp(ly)), n=float(n),
               Delta=float(D), margin=float(margin),
               Hdot=float((f(sol.t[-1], sol.y[:, -1])[2]
                           +2*f(sol.t[-1], sol.y[:, -1])[3])/3),
               production=float(b*sol.y[6, -1]),
               N_initial=float(physical(y0, closure)[4]*physical(y0, closure)[9]))
    q = physical(yy, closure)
    race = 2*(b*q[6]**4/q[4]-q[8]/q[7])
    out.update(race_initial=float(race[0]), race_min=float(np.min(race)),
               race_max=float(np.max(race)), race_event=float(race[-1]))
    # Locate the two race crossings on Delta>0 data with continuous dense output.
    from scipy.optimize import brentq
    race_roots = []
    if np.min(q[7]) > 0:
        def rate(t):
            z = physical(sol.sol(t), closure)
            return 2*(b*z[6]**4/z[4]-z[8]/z[7])
        for j in range(len(times)-1):
            if race[j]*race[j+1] < 0:
                race_roots.append(float(brentq(rate, times[j], times[j+1], xtol=1e-14)))
    out["race_roots"] = race_roots
    if status == "REGULAR_TURN":
        assert margin > 0 and out["Hdot"] > 0
        dt = .01/max(1., math.sqrt(e), abs(u), abs(v))
        post = solve_ivp(f, (sol.t[-1], sol.t[-1]+dt), sol.y[:, -1],
                         method="DOP853", dense_output=True,
                         rtol=rtol, atol=atol, max_step=dt/8)
        assert post.success, "post-event integration failed"
        pt = np.unique(np.concatenate((post.t, np.linspace(post.t[0],post.t[-1],101))))
        pd = diagnostics(pt, post.sol(pt), closure, a, b, y0)
        for key in ("absC", "relC", "Nres", "Dres", "maxKretsch"):
            out[key] = max(out[key], pd[key])
        for key in ("minX", "minY", "minE", "minN"):
            out[key] = min(out[key], pd[key])
        out["post_H"] = float((post.y[2,-1]+2*post.y[3,-1])/3)
        assert out["post_H"] > 0
    assert out["minE"] > 0 and out["minN"] > 0
    assert out["minX"] > 0 and out["minY"] > 0
    return out


def main():
    assert hashlib.sha256((HERE/"b4_springer_access.html").read_bytes()).hexdigest() == SOURCE_SHA
    print("PUBLISHER_SHA256="+SOURCE_SHA)
    print("VERSIONS python="+sys.version.split()[0]+" numpy="+np.__version__
          +" scipy="+scipy.__version__+" sympy="+sp.__version__)
    exact_checks()
    print("NUMERIC_ALPHA_INTERVAL=[0.25,1]; sampled=0.25,0.5,1")
    print("NUMERIC_BETA_PARAMETERS=0.01,0.1,1; beta=0 is diagnostic control only")
    print("MAIN_INITIAL H=-1 Delta=3 K=1 w=A*n^2=0.1 e=1.1 X=Y=1")
    print("case closure A B status t Hdot R_at_turn max_abs_C max_rel_C")
    all_out, main_out, maxima = {}, {}, {}
    weak = (-1., 3., 1., .1)
    cases = [("weak", weak), ("source_velocity_sign", (-1., -3., 1., .25)),
             ("preloaded", (-.25, .3, 1., 2.))]
    for closure in ("b", "c"):
        rows = []
        for name, spec in cases:
            pairs = [(a,b) for a in ALPHAS for b in BETAS] if name == "weak" else [(.5,.1)]
            for a,b in pairs:
                z = integrate(closure, a, b, spec)
                assert z["status"] == "REGULAR_TURN"
                rows.append(z)
                all_out[(closure,name,a,b)] = z
                if name == "weak" and a == .5 and b == .1:
                    main_out[closure] = z
                print(f'{name} {closure} {a:g} {b:g} {z["status"]} '
                      f'{z["t"]:.12g} {z["Hdot"]:.9g} {z["R"]:.9g} '
                      f'{z["absC"]:.3e} {z["relC"]:.3e}')
        # Independent changes of every non-gauge datum and both parameters.
        # Evidence of robustness; openness itself is proved in the report.
        for j in range(6):
            for sign in (-1, 1):
                vals = [*weak, .5, .1]
                vals[j] *= 1+sign*.01
                z = integrate(closure, vals[4], vals[5], tuple(vals[:4]))
                assert z["status"] == "REGULAR_TURN"
                rows.append(z)
        coarse = integrate(closure, .5, .1, weak, tight=False)
        fine = main_out[closure]
        dt = abs(coarse["t"]-fine["t"])
        de = abs(coarse["e"]-fine["e"])/fine["e"]
        assert dt < 1e-7 and de < 1e-7
        print(f'CONVERGENCE closure={closure} abs_delta_t={dt:.3e} rel_delta_e={de:.3e}')
        print(f'PERTURBATIONS closure={closure} turns=12/12')
        print("REPRESENTATIVE closure="+closure+" "+repr(fine))
        maxima[closure] = {key:max(r[key] for r in rows)
                           for key in ("absC","relC","Nres","Dres")}
        assert maxima[closure]["relC"] < 1e-9
        assert maxima[closure]["Nres"] < 1e-9 and maxima[closure]["Dres"] < 1e-9
        # Thresholds are diagnostic stops, never numerical singularity findings.
        for cap in (1e3,1e4,1e5):
            z = integrate(closure,.5,0.,weak,cap=cap)
            assert z["status"] == "FINITE_CUTOFF_UNRESOLVED"
            print(f'ZERO_PRODUCTION_CONTROL closure={closure} cap={cap:.0e} '
                  f'status={z["status"]} t={z["t"]:.12g} '
                  f'Kretschmann={z["maxKretsch"]:.6g} rel_C={z["relC"]:.3e}')
        try:
            initial(closure,.5,(-.1,4.,1.,.1))
        except ValueError as err:
            print("REJECTED_TEST closure="+closure+" "+str(err))
        else:
            raise AssertionError("inadmissible energy accepted")
        try:
            integrate(closure,.5,-.1,weak)
        except ValueError as err:
            print("REJECTED_TEST closure="+closure+" "+str(err))
        else:
            raise AssertionError("negative production accepted")
    for key in ("t", "e", "n", "Delta", "K"):
        diff = abs(main_out["b"][key]-main_out["c"][key])/(1+abs(main_out["c"][key]))
        assert diff < 1e-9, ("closure coordinate agreement",key,diff)
    print("CLOSURE_COORDINATE_AGREEMENT=PASS")
    for closure in ("b", "c"):
        z = maxima[closure]
        print(f'CONSTRAINT_RESIDUAL closure={closure} symbolic=0 '
              f'max_abs={z["absC"]:.12e} max_normalized={z["relC"]:.12e} '
              f'number_integral={z["Nres"]:.3e} shear_integral={z["Dres"]:.3e}')
    print("OUTCOME=TURNS_OVER")
    for name in ("B7_CURVED_20260907.md", "b7_curved.py"):
        p = HERE/name
        if p.exists():
            print("SHA256 "+name+" "+hashlib.sha256(p.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
