#!/usr/bin/env python3
"""A2: past light cones of an off-center observer in the sigma=1/3 shock cosmology.

Units: t in units of t_crit (the N=1 crossing, A1's anchor), R(t_crit)=1, so
conformal time eta = 2*sqrt(t), eta_crit = 2. Comoving shock radius r_*(eta) = eta*sqrt(N),
from the A1 solution (recomputed here from the same backward integration, same equations).

A0 (proved in A2_RECEIPT.md from the construction): the interior is EXACT k=0 FRW, so every
observable whose photons stay inside the FRW region is exactly isotropic for any observer
position; anisotropy is boundary-mediated only. This script computes the boundary geometry:
  z_c(mu; x_off, t_obs) — the redshift at which the line of sight in direction mu crosses the
  shock (mu = cos angle between viewing direction and the outward offset direction).
Solve |x_o + chi*n| = r_*(eta_obs - chi) for chi, then 1+z_c = sqrt(t_obs/t_e), t_e=((eta_obs-chi)/2)^2.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import csv, sys

SIGMA = 1.0/3.0

# --- reproduce the A1 orbit (same equations, backward integration) ---
def dudS(S, y):
    u = y[0]
    num = (3*u-1)*(SIGMA-u) + 6*u*(1+u)*S
    den = (SIGMA-u) + (1+u)*S
    return [ (1+u)/(2*(1+3*u)*S) * num/den ]
delta = 1e-8; S0 = 1e-12
sol = solve_ivp(dudS, [1.0-delta, S0], [delta/8.0], method='LSODA', rtol=1e-11, atol=1e-13, dense_output=True)
assert sol.success
def u_of_S(S):
    S = np.clip(S, S0, 1.0-delta)
    return sol.sol(np.atleast_1d(S))[0]

# t(sqrtN): dlnt/dq = 2/(s-q), q=sqrtN, anchored t=1 at q=1  (A1 derivation)
def dlnt_dq(q, y):
    uu = u_of_S(1.0/(q*q))[0]
    s = q*(SIGMA-uu)/(1+uu)
    return [2.0/(s-q)]
QMAX = 1e6
solt = solve_ivp(dlnt_dq, [1.0, QMAX], [0.0], method='LSODA', rtol=1e-12, atol=1e-14, dense_output=True)
assert solt.success

qg   = np.logspace(0, 6, 20001)               # sqrtN grid
tg   = np.exp(solt.sol(qg)[0])                # t/t_crit
etag = 2.0*np.sqrt(tg)                        # conformal time
rsg  = etag*qg                                # comoving shock radius r_* = eta*sqrtN
# r_* is monotone decreasing in q toward... check orientation for interp: eta decreasing in q.
o = np.argsort(etag)
eta_s, rs_s = etag[o], rsg[o]
RSTAR0 = rs_s[0]                              # Big Bang limit r_*(0)
def r_star(eta):
    return np.interp(eta, eta_s, rs_s)        # linear on fine grid

checks=[]
def chk(name, ok, detail=""):
    checks.append((name,bool(ok),detail)); print(("PASS " if ok else "FAIL ")+name+("  "+detail if detail else ""))

# --- model-internal validations against Sec.6 ---
t_vis = (RSTAR0/2.0)**2                       # eta(t_vis) = r_*(0)
chk("(6.3): 1.8 <= t_crit/t_vis <= 4.5", 1.8 <= 1.0/t_vis <= 4.5, f"t_crit/t_vis={1.0/t_vis:.4f}")
sqrtN_vis = np.interp(t_vis, tg, qg)          # tg increasing in... tg decreasing in q; fix below
sqrtN_vis = np.interp(2*np.sqrt(t_vis), eta_s, (qg[o]))
chk("Sec.6: 1 < sqrtN_0 <= 4.5 at first visibility", 1.0 < sqrtN_vis <= 4.5, f"sqrtN_0={sqrtN_vis:.4f}")
chk("r_*(0) finite (free-parameter anchor)", 0.5 < RSTAR0 < 2.0, f"r_*(0)={RSTAR0:.6f} (units eta_crit=2)")

# --- light-cone crossing solver ---
def z_cross(mu, x_off, t_obs):
    """Redshift at shock crossing along direction mu; None if the sight line never crosses."""
    eta_o = 2.0*np.sqrt(t_obs)
    def g(chi):
        p = np.sqrt(max(x_off*x_off + chi*chi + 2.0*chi*x_off*mu, 0.0))
        return p - r_star(eta_o - chi)
    lo, hi = 1e-12, eta_o - 1e-12
    if g(hi) < 0:      # even at the Big Bang end the sight line is still inside the shock
        return None
    if g(lo) > 0:      # observer outside the shock (not our case; guard)
        return None
    chi = brentq(g, lo, hi, xtol=1e-14, rtol=1e-13)
    t_e = ((eta_o - chi)/2.0)**2
    return np.sqrt(t_obs/t_e) - 1.0

# --- survey: t_obs and x_off in natural units ---
t_obs_list = [t_vis, 0.5, 1.0]                                    # first visibility, mid, t_crit
frac_list  = [0.0, 0.05, 0.1, 0.2, 0.3, 0.5]                      # x_off as fraction of r_*(t_obs)
mus        = np.linspace(-1.0, 1.0, 41)

rows=[]
for t_obs in t_obs_list:
    eta_o = 2.0*np.sqrt(t_obs)
    rso = r_star(eta_o)
    for f in frac_list:
        x = f*rso
        zs = np.array([z_cross(mu, x, t_obs) if z_cross(mu, x, t_obs) is not None else np.nan for mu in mus])
        vis = np.isfinite(zs)
        for mu, z in zip(mus, zs):
            rows.append([t_obs, f, x, mu, z])
        if vis.all():
            zbar = zs.mean()
            dip  = (zs[np.isclose(mus,1.0)][0]-zs[np.isclose(mus,-1.0)][0])
            print(f"t_obs={t_obs:.4f} x_off/r_*={f:.2f}: z_c range [{zs.min():.4f},{zs.max():.4f}] "
                  f"mean {zbar:.4f}  (z(+1)-z(-1))/mean = {dip/zbar:+.4e}")
        else:
            print(f"t_obs={t_obs:.4f} x_off/r_*={f:.2f}: shock visible on {vis.sum()}/{len(mus)} directions")

# --- null and monotonicity checks ---
z0 = [z_cross(mu, 0.0, 1.0) for mu in (-1.0, 0.0, 1.0)]
chk("null test: x_off=0 isotropic at t_crit", max(z0)-min(z0) < 1e-10, f"spread={max(z0)-min(z0):.2e}")
za = z_cross(+1.0, 0.2*r_star(2.0), 1.0); zb = z_cross(-1.0, 0.2*r_star(2.0), 1.0)
chk("nearest boundary (mu=+1) crosses at LOWER z than farthest (mu=-1)", za < zb, f"z(+1)={za:.4f} z(-1)={zb:.4f}")

with open("a2_zcross.csv","w",newline="") as fH:
    w=csv.writer(fH); w.writerow(["t_obs_over_tcrit","x_off_frac_of_rstar","x_off_comoving","mu","z_cross"])
    for r in rows: w.writerow([f"{r[0]:.8e}",f"{r[1]:.3f}",f"{r[2]:.8e}",f"{r[3]:.4f}", "" if np.isnan(r[4]) else f"{r[4]:.8e}"])

nfail=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nfail}/{len(checks)} checks passed; rows={len(rows)}; t_vis={t_vis:.6f} t_crit units")
sys.exit(1 if nfail else 0)
