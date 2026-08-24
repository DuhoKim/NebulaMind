#!/usr/bin/env python3
"""A3: from crossing geometry to the three observables (sigma=1/3 model, units of A2).

Analytic backbone (derived by hand, checked here against the A2 solver):
  1+z = eta_obs/eta_e (conformal ratio, exact FRW interior)
  center crossing: eta_obs = eta_e (1 + sqrtN(eta_e))  =>  z_c(center) = sqrtN(eta_e)
  mu=+1 (nearest) crossing with offset x: x = eta_e (1 + sqrtN(eta_e)) - eta_obs
    =>  x_max(z; t_obs) = eta_obs [ (1+sqrtN(eta_e))/(1+z) - 1 ],  eta_e = eta_obs/(1+z)

Observable (a) CMB: sky uniform to z_ls ~ 1100 requires z_c(mu) > z_ls in ALL directions
  (unless the unmodeled TOV side mimics FRW — non-generic, recorded as the conspiracy out).
  => t_obs window above t_vis where z_c(center) >= z_ls, and x_off bound within it.
Observable (b) expansion anisotropy: NULL by A0 — exact FRW interior => NO H0 dipole for
  sources with z < min_mu z_c. Computed here: nothing; stated in receipt.
Observable (c) dipole: no structured non-kinematic dipole for interior signals (A0);
  boundary-crossed sky unconstrained without TOV optics. Stated in receipt.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import csv, sys

SIGMA=1.0/3.0
def dudS(S,y):
    u=y[0]
    return [ (1+u)/(2*(1+3*u)*S) * (((3*u-1)*(SIGMA-u)+6*u*(1+u)*S)/((SIGMA-u)+(1+u)*S)) ]
delta=1e-8; S0=1e-14
sol=solve_ivp(dudS,[1.0-delta,S0],[delta/8.0],method='LSODA',rtol=1e-11,atol=1e-13,dense_output=True)
assert sol.success
def u_of_S(S): return sol.sol(np.atleast_1d(np.clip(S,S0,1.0-delta)))[0]
def dlnt_dq(q,y):
    uu=u_of_S(1.0/(q*q))[0]; s=q*(SIGMA-uu)/(1+uu)
    return [2.0/(s-q)]
QMAX=3e6
solt=solve_ivp(dlnt_dq,[1.0,QMAX],[0.0],method='LSODA',rtol=1e-12,atol=1e-14,dense_output=True)
assert solt.success
qg=np.logspace(0,np.log10(QMAX),30001)
tg=np.exp(solt.sol(qg)[0]); etag=2.0*np.sqrt(tg)
o=np.argsort(etag); eta_s=etag[o]; q_s=qg[o]; rs_s=eta_s*q_s
RSTAR0=rs_s[0]; ETA_VIS=RSTAR0; T_VIS=(RSTAR0/2)**2
def sqrtN_of_eta(eta): return np.interp(eta,eta_s,q_s)
def r_star(eta):       return np.interp(eta,eta_s,rs_s)

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

# cross-validate analytic z_c(center)=sqrtN(eta_e) against the A2-style root solve at t_crit
def z_cross_num(mu,x,t_obs):
    eo=2*np.sqrt(t_obs)
    def g(ee):
        chi=eo-ee
        p=np.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0))
        return p-ee*sqrtN_of_eta(ee)
    ee=brentq(g,1e-9,eo-1e-12,xtol=1e-15)
    return eo/ee-1.0
z_num=z_cross_num(0.0,0.0,1.0)
ee=2.0/(1.0+z_num)
chk("analytic z_c(center)=sqrtN(eta_e) matches solver", abs(z_num-sqrtN_of_eta(ee))<1e-6,
    f"z_num={z_num:.6f} sqrtN={sqrtN_of_eta(ee):.6f}")

# (a) the t_obs window where z_c(center) >= z_ls
ZLS=1100.0
def zc_center(t_obs):
    eo=2*np.sqrt(t_obs)
    f=lambda ee: eo-ee*(1.0+sqrtN_of_eta(ee))
    ee=brentq(f,1e-9,eo-1e-15,xtol=1e-16)
    return eo/ee-1.0
T_CRIT=1.0
chk("z_c(center) at t_crit ~ 2.55 (A2 value)", abs(zc_center(1.0)-2.5499)<0.01, f"{zc_center(1.0):.4f}")
# find t_1100: zc_center(t)=ZLS
tf=brentq(lambda t: zc_center(t)-ZLS, T_VIS*(1+1e-12), 0.9999, xtol=1e-14)
W=(tf-T_VIS)/(T_CRIT-T_VIS)
print(f"t_vis={T_VIS:.8f}  t_1100={tf:.8f}  t_crit=1  => window fraction W={W:.3e}")
chk("window where boundary hides beyond z_ls is a strict subinterval", 0<W<1, f"W={W:.3e}")

# x_off bound: x_max(z_ls; t_obs) = eta_obs[(1+sqrtN(eta_e))/(1+z)-1], eta_e=eta_obs/(1+z)
def x_max(t_obs, z=ZLS):
    eo=2*np.sqrt(t_obs); ee=eo/(1.0+z)
    return eo*((1.0+sqrtN_of_eta(ee))/(1.0+z)-1.0)
rows=[]
for f_ in [0.0,0.1,0.25,0.5,0.75,0.9,0.99]:
    t=T_VIS+f_*(tf-T_VIS)
    if t<=T_VIS: t=T_VIS*(1+1e-10)
    xm=x_max(t); rs=r_star(2*np.sqrt(t))
    rows.append([t,zc_center(t),xm,rs,max(xm,0.0)/rs])
    print(f"t_obs={t:.8f} (window frac {f_:.2f}): z_c(center)={zc_center(t):.1f}  "
          f"x_max/r_* = {max(xm,0.0)/rs:.3e}")
chk("x_max -> 0 at window edge t_1100", abs(x_max(tf))<1e-9*r_star(2*np.sqrt(tf)), f"x_max(tf)={x_max(tf):.2e}")
# max allowed offset anywhere in the window (at t_vis edge)
xm_best=x_max(T_VIS*(1+1e-12)); rs_vis=r_star(2*np.sqrt(T_VIS))
print(f"max offset in-window (at t->t_vis): x_max/r_* = {xm_best/rs_vis:.3e}")

with open("a3_window.csv","w",newline="") as fh:
    w=csv.writer(fh); w.writerow(["t_obs_over_tcrit","z_c_center","x_max_comoving","r_star_comoving","x_max_over_rstar"])
    for r in rows: w.writerow([f"{v:.10e}" for v in r])

nfail=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nfail}/{len(checks)} checks passed")
sys.exit(1 if nfail else 0)
