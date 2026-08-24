#!/usr/bin/env python3
"""A4: the prediction functions of the anti-Copernican discriminant (sigma=1/3 model).

P1  z_c(mu; x_off, t_obs)   — boundary-crossing redshift (A2 solver; master geometry).
P2  regime(t_obs, x_off)    — HIDDEN / MARGINAL / EXCLUDED against a sky observed uniform
                              to z_ls (default 1100). Analytic backbone from A3.
P3  cap geometry            — where the last-scattering sphere pokes outside the shock:
      comoving LSS radius chi_ls = eta_o * z/(1+z); shock radius rho_s = eta_e*sqrtN(eta_e),
      eta_e = eta_o/(1+z). Cap edge: mu_c = (rho_s^2 - x^2 - chi_ls^2)/(2 x chi_ls);
      affected sky fraction f = (1-mu_c)/2, angular radius theta_c = arccos(mu_c).
    This makes "signature at the largest angular scales" a number: theta_c -> ell ~ pi/theta_c.

All quantities in A2 units (t in t_crit, eta = 2 sqrt(t), R(t_crit)=1).
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
    uu=u_of_S(1.0/(q*q))[0]; return [2.0/(q*(SIGMA-uu)/(1+uu)-q)]
QMAX=3e6
solt=solve_ivp(dlnt_dq,[1.0,QMAX],[0.0],method='LSODA',rtol=1e-12,atol=1e-14,dense_output=True)
assert solt.success
qg=np.logspace(0,np.log10(QMAX),30001)
tg=np.exp(solt.sol(qg)[0]); etag=2.0*np.sqrt(tg)
o=np.argsort(etag); eta_s=etag[o]; q_s=qg[o]
def sqrtN_of_eta(e): return np.interp(e,eta_s,q_s)
RSTAR0=(eta_s*q_s)[0]; T_VIS=(RSTAR0/2)**2
ZLS=1100.0

checks=[]; 
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

def zc_center(t_obs):
    eo=2*np.sqrt(t_obs)
    ee=brentq(lambda e: eo-e*(1.0+sqrtN_of_eta(e)),1e-9,eo-1e-15,xtol=1e-16)
    return eo/ee-1.0
T_1100=brentq(lambda t: zc_center(t)-ZLS, T_VIS*(1+1e-12),0.9999,xtol=1e-15)

def cap(t_obs, x, z=ZLS):
    """Return (mu_c, theta_c_deg, sky_frac). mu_c>=1 -> no cap (LSS fully inside shock).
       mu_c<=-1 -> whole sky affected."""
    eo=2*np.sqrt(t_obs); ee=eo/(1.0+z)
    chi=eo-ee; rho=ee*sqrtN_of_eta(ee)
    if x==0.0:
        return (np.inf,0.0,0.0) if rho>chi else (-np.inf,180.0,1.0)
    mu_c=(rho*rho-x*x-chi*chi)/(2*x*chi)
    if mu_c>=1.0:  return (mu_c,0.0,0.0)
    if mu_c<=-1.0: return (mu_c,180.0,1.0)
    return (mu_c, np.degrees(np.arccos(mu_c)), (1.0-mu_c)/2.0)

def x_max(t_obs, z=ZLS):
    eo=2*np.sqrt(t_obs); ee=eo/(1.0+z)
    return eo*((1.0+sqrtN_of_eta(ee))/(1.0+z)-1.0)

# checks: cap closes exactly at x=x_max; hidden regime has no cap for any x < r_*
tmid=T_VIS+0.5*(T_1100-T_VIS)
xm=x_max(tmid)
chk("cap vanishes at x = x_max", cap(tmid,xm*(1-1e-9))[1]<1e-3 and cap(tmid,xm*(1+1e-3))[1]>0,
    f"theta(x_max-)={cap(tmid,xm*(1-1e-9))[1]:.2e} deg, theta(x_max*1.001)={cap(tmid,xm*(1+1e-3))[1]:.2f} deg")
# CORRECTED CHECK: the first version asserted "hidden regime: no cap even at 30% offset"
# and FAILED (theta=97.4 deg) — correctly: an offset observer's LSS pokes out before the
# center's t_vis. The real invariant is that the cap opens exactly at x_max(t) at ALL t:
for tt in [T_VIS*0.5, T_VIS*0.99, tmid]:
    xmt=x_max(tt)
    ok = cap(tt,xmt*(1-1e-9))[1]<1e-3 and cap(tt,xmt*(1+1e-3))[1]>0
    chk(f"cap opens exactly at x_max(t) [t={tt:.4f}]", ok,
        f"x_max/r_*={xmt/np.interp(2*np.sqrt(tt),eta_s,eta_s*q_s):.3e}")
chk("t_1100 matches A3", abs(T_1100-0.27744174)<1e-6, f"T_1100={T_1100:.8f}")

# P2 regime map + P3 cap tabulation
rows=[]
t_grid = list(np.linspace(T_VIS*0.98, T_VIS, 5, endpoint=False)) + \
         list(T_VIS + np.linspace(0,1,21)[1:]*(T_1100-T_VIS)) + \
         list(np.linspace(T_1100, min(5*T_1100-4*T_VIS, 0.999), 12)[1:])
for t in t_grid:
    eo=2*np.sqrt(t); rs=np.interp(eo,eta_s,eta_s*q_s)
    xm_t = x_max(t) if t>=T_VIS else np.nan
    for fx in [0.0,1e-4,3e-4,1e-3,3e-3,1e-2,3e-2,0.1]:
        x=fx*rs
        mu_c,th,fsky=cap(t,x)
        # Dichotomy (pre-recombination universe is opaque: crossings at z>z_ls are
        # unobservable even when geometrically inside the past cone):
        if th==0.0: regime="NO-CAP(consistent, boundary unobservable)"
        elif fsky<1.0: regime="CAP(boundary-affected CMB patch)"
        else: regime="CAP-FULLSKY"
        rows.append([t,fx,x,xm_t,mu_c if np.isfinite(mu_c) else 9e9,th,fsky,regime])

with open("a4_regime_map.csv","w",newline="") as fh:
    w=csv.writer(fh)
    w.writerow(["t_obs_over_tcrit","x_frac_of_rstar","x_comoving","x_max_at_t","mu_c","theta_cap_deg","sky_frac_affected","regime"])
    for r in rows: w.writerow([f"{r[0]:.10e}",f"{r[1]:.1e}",f"{r[2]:.6e}", "" if np.isnan(r[3]) else f"{r[3]:.6e}",f"{r[4]:.6e}",f"{r[5]:.4f}",f"{r[6]:.6e}",r[7]])

# headline P3 numbers: cap size just past the bound
print("\nP3 cap growth just past x_max (t at band middle):")
for k in [1.001,1.01,1.1,1.5,2.0,5.0]:
    mu_c,th,fs=cap(tmid,xm*k)
    ell = 180.0/th if th>0 else np.inf
    print(f"  x = {k:5.3f} x_max: theta_cap = {th:7.3f} deg  sky frac = {fs:.4e}  ell~pi/theta = {ell:.0f}")

nfail=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nfail}/{len(checks)} checks passed; map rows={len(rows)}")
sys.exit(1 if nfail else 0)
