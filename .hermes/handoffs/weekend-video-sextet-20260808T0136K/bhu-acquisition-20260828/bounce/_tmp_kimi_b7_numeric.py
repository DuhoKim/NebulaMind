#!/usr/bin/python3
"""KIMI independent numerics for B7 challenge.
My own RHS (from my own symbolic rewrite of publisher (10),(14),(34)),
two solver paths (LSODA and a hand-written RK4), my own perturbation sets,
a direct openness test around B7's analytic construction point, the
zero-production control, and a small-beta probe.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp

KAPPA = 1.0

def make_rhs(a, b):
    def f(t, y):
        lx, ly, u, v, n, e = y
        H = (u + 2*v)/3.0
        K = math.exp(-2*ly)
        psi = b*H**4
        P = e/3.0 - a*n*n
        return np.array([
            u,
            v,
            -u*u - u*v + (v*v + K - P)/2.0,     # my derived dot u
            -(3*v*v + K + P)/2.0,               # my derived dot v
            psi - 3*H*n,
            2*a*n*psi - 4*H*e,
        ])
    return f

def initial(H, D, K, w, a):
    e = 3*H*H - D*D/3.0 + K + w
    if e <= 0: raise ValueError("inadmissible")
    return np.array([0.0, -0.5*math.log(K), H + 2*D/3.0, H - D/3.0,
                     math.sqrt(w/a), e])

def turn_event(t, y):
    return (y[2] + 2*y[3])/3.0
turn_event.direction, turn_event.terminal = 1, True

def run(a, b, spec, method="LSODA", rtol=1e-11, atol=1e-13, tmax=3.0):
    y0 = initial(*spec, a)
    sol = solve_ivp(make_rhs(a, b), (0., tmax), y0, method=method,
                    rtol=rtol, atol=atol, max_step=0.005,
                    events=turn_event, dense_output=True)
    turned = len(sol.t_events[0]) > 0
    out = {"turned": turned, "t": float(sol.t[-1])}
    if turned:
        yb = sol.y[:, -1]
        u, v, n, e = yb[2], yb[3], yb[4], yb[5]
        D = u - v; Kb = math.exp(-2*yb[1])
        out.update(Hdot=(a*n*n - D*D/3.0 - Kb)/3.0, e=e, n=n, Delta=D, K=Kb,
                   margin=a*n*n - D*D/3.0 - Kb)
        # constraint residual along trajectory
        ts = np.linspace(0, sol.t[-1], 2001)
        yy = sol.sol(ts)
        Hh = (yy[2] + 2*yy[3])/3
        Dd = yy[2] - yy[3]
        Kk = np.exp(-2*yy[1])
        Cc = yy[3]**2 + 2*yy[2]*yy[3] + Kk - yy[5] + a*yy[4]**2
        scale = 1 + yy[3]**2 + 2*np.abs(yy[2]*yy[3]) + Kk + yy[5] + a*yy[4]**2
        out.update(absC=float(np.max(np.abs(Cc))), relC=float(np.max(np.abs(Cc/scale))))
    return out

def rk4_run(a, b, spec, h=2e-5, tmax=3.0):
    """Hand-written fixed-step RK4, fully independent of scipy."""
    f = make_rhs(a, b)
    y = initial(*spec, a).astype(float)
    t = 0.0
    prevH = (y[2] + 2*y[3])/3.0
    while t < tmax:
        k1 = f(t, y); k2 = f(t+h/2, y+h*k1/2)
        k3 = f(t+h/2, y+h*k2/2); k4 = f(t+h, y+h*k3)
        y = y + h*(k1 + 2*k2 + 2*k3 + k4)/6.0
        t += h
        Hn = (y[2] + 2*y[3])/3.0
        if prevH < 0 <= Hn:   # upward crossing
            # bisect within the step
            lo, hi = t-h, t
            ylo = y - h*(k1 + 2*k2 + 2*k3 + k4)/6.0
            for _ in range(60):
                mid = 0.5*(lo+hi)
                ym = ylo.copy()
                # re-integrate one partial step via RK4 substeps
                yy = ylo.copy(); tt = t-h
                hh = (mid-(t-h))/4
                for _s in range(4):
                    m1=f(tt,yy); m2=f(tt+hh/2,yy+hh*m1/2); m3=f(tt+hh/2,yy+hh*m2/2); m4=f(tt+hh,yy+hh*m3)
                    yy = yy + hh*(m1+2*m2+2*m3+m4)/6.0; tt += hh
                if (yy[2]+2*yy[3])/3.0 < 0: lo = mid
                else: hi = mid
            return True, 0.5*(lo+hi)
        prevH = Hn
    return False, None

# ---------- 1. representative datum, two independent solvers ----------
spec = (-1.0, 3.0, 1.0, 0.1)
r_lsoda = run(0.5, 0.1, spec)
t_rk4, tb_rk4 = rk4_run(0.5, 0.1, spec)
print("REP LSODA:", r_lsoda)
print("REP RK4   : turned=%s tb=%.12f" % (t_rk4, tb_rk4))
print("B7 claims : tb=0.313980691809 Hdot=1316.48101 e=4150.24452223")

# ---------- 2. my own perturbations: random +/-5% and +/-10% on constraint manifold ----------
rng = np.random.default_rng(20260907)
for pct in (0.05, 0.10):
    turns = 0; total = 0
    for i in range(40):
        fac = 1 + pct*rng.uniform(-1, 1, size=6)
        H0, D0, K0, w0 = spec[0]*fac[0], spec[1]*fac[1], spec[2]*fac[2], spec[3]*fac[3]
        aa, bb = 0.5*fac[4], 0.1*fac[5]
        if H0 >= 0 or K0 <= 0 or w0 <= 0 or aa <= 0: continue
        try:
            r = run(aa, bb, (H0, D0, K0, w0), rtol=1e-10, atol=1e-12)
            total += 1; turns += int(r["turned"])
        except ValueError:
            pass
    print(f"RANDOM_PERTURBATION +/-{int(pct*100)}%: turns {turns}/{total}")

# ---------- 3. direct openness test around B7's section-4 construction ----------
# construction: H_b=0, K_b=k e_b/4, S_b=k e_b/12, k a n_b^2 = 5 k e_b/6
eb = 2.0; aa, bb = 0.5, 0.1
Kb = eb/4.0; Db = math.sqrt(3*eb/12.0)  # S = D^2/3 = e/12 -> D = sqrt(e/4)
Db = math.sqrt(eb/4.0)
nb = math.sqrt(5*eb/(6*aa))
ub, vd = 2*Db/3.0, -Db/3.0
yb = np.array([0.0, -0.5*math.log(Kb), ub, vd, nb, eb])
Cchk = vd**2 + 2*ub*vd + Kb - eb + aa*nb*nb
print("CONSTRUCTION constraint residual at point:", Cchk, " margin:", aa*nb*nb - Db*Db/3 - Kb)
# integrate backward 0.02 to get contracting data, then perturb each component 1% and
# re-derive nothing (constraint-preserving perturbations: perturb and re-solve e from C=0)
solb = solve_ivp(make_rhs(aa, bb), (0., -0.02), yb, method="DOP853",
                 rtol=1e-12, atol=1e-14, dense_output=True)
yc = solb.y[:, -1]
print("back-integrated H:", (yc[2]+2*yc[3])/3)
def reclose(y):
    # recompute e from the constraint given (u,v,K,n,a)
    return y[3]**2 + 2*y[2]*y[3] + math.exp(-2*y[1]) + aa*y[4]**2
turns = 0; total = 0
rng2 = np.random.default_rng(7)
for i in range(30):
    y0 = yc.copy()
    for j in (2, 3, 4):   # perturb u, v, n by up to 2%
        y0[j] *= 1 + 0.02*rng2.uniform(-1, 1)
    y0[5] = reclose(y0)
    if y0[5] <= 0: continue
    sol = solve_ivp(make_rhs(aa, bb), (0., 0.1), y0, method="LSODA",
                    rtol=1e-11, atol=1e-13, events=turn_event)
    total += 1; turns += int(len(sol.t_events[0]) > 0)
print(f"OPENNESS_DIRECT around construction: turns {turns}/{total}")

# ---------- 4. zero-production control with my integrator ----------
f0 = make_rhs(0.5, 0.0)
y0 = initial(*spec, 0.5)
sol = solve_ivp(f0, (0., 1.0), y0, method="LSODA", rtol=1e-10, atol=1e-12,
                max_step=1e-4)
yy = sol.y
Htr = (yy[2]+2*yy[3])/3
print("B=0: integration ended at t=%.6f success=%s" % (sol.t[-1], sol.success))
print("B=0: H(first,last)=(%.3f, %.3g)  Y(last)=%.3g  K(last)=%.3g  monotonic_decreasing_H=%s"
      % (Htr[0], Htr[-1], math.exp(yy[1,-1]), math.exp(-2*yy[1,-1]),
         bool(np.all(np.diff(Htr) < 0))))
# analytic bound: cannot turn before t0+1/|H0| = 1.0 ; check H below Riccati bound
bound = -1.0/(1.0 - sol.t)   # solution of H'=-H^2 from H0=-1
print("B=0: H <= Riccati upper bound everywhere:", bool(np.all(Htr <= bound + 1e-6)))

# ---------- 5. small-beta probe of the main family ----------
for bv in (1e-2, 1e-3, 1e-4, 1e-5):
    r = run(0.5, bv, spec, tmax=2.0)
    print(f"SMALL_BETA B={bv:g}: turned={r['turned']}" + (f" tb={r['t']:.6f}" if r['turned'] else ""))
print("DONE")
