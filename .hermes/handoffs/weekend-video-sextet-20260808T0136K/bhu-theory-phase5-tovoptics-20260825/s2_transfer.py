#!/usr/bin/env python3
"""S2: the kinematic temperature pattern across the boundary-crossing cap.

Combines Phase 4's cap geometry (A2/A4, gated) with S1's crossing law beta = 1/sqrt(N).

 DATA     : the A1 orbit (gated Phase 4 output, read as data).
 DERIVED  : r_* = eta*sqrtN, eta = 2 sqrt(t) and the crossing condition are Phase-4 DERIVED
            geometry, NOT pinned published equations (gate objection 6).
 DERIVED  : beta_rel = 1/sqrt(N) at the crossing (S1_RECEIPT.md, proven).
 DERIVED  : local projection mu_loc = (x_off*mu + chi)/rho_s -- the cosine between the ray and
            the shock normal at the crossing point, from vector geometry.
 DERIVED  : kinematic shift  1 + z_cross = gamma (1 - beta*mu_loc);  DeltaT/T = 1/(1+z)-1
            for a beam whose radiation field is common to both sides.
 ASSUMPTION, STATED: both sides share one radiation bath, so the shift is purely kinematic and
            no absolute TOV temperature is needed. The ABSOLUTE brightness of the cap would
            require T_TOV, which the pinned metric does not fix -- that is kill-criterion K4
            territory and is NOT computed here.
"""
import csv, math, sys
import numpy as np
from scipy.optimize import brentq

SIGMA=1/3.0
rows=list(csv.DictReader(open("../bhu-theory-phase4-anisotropy-20260823/a1_results.csv")))
T =np.array([float(r["t_over_tcrit"]) for r in rows])
Q =np.array([float(r["sqrtN_hubble_lengths"]) for r in rows])
ETA=2*np.sqrt(T); o=np.argsort(ETA); ETA=ETA[o]; Q=Q[o]; RS=ETA*Q

def sqrtN(eta): return np.interp(eta, ETA, Q)
def r_star(eta): return np.interp(eta, ETA, RS)

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

def crossing(mu, x, t_obs):
    """Return (chi, eta_e, mu_loc, rho_s) for the sight line, or None if it never crosses."""
    eta_o=2*math.sqrt(t_obs)
    def g(chi):
        p=math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0))
        return p-r_star(eta_o-chi)
    lo,hi=1e-12, eta_o-1e-12
    if g(hi)<0 or g(lo)>0: return None
    chi=brentq(g,lo,hi,xtol=1e-15)
    eta_e=eta_o-chi
    rho_s=r_star(eta_e)
    mu_loc=(x*mu+chi)/rho_s
    return chi, eta_e, max(-1.0,min(1.0,mu_loc)), rho_s

def shift(mu, x, t_obs):
    c=crossing(mu,x,t_obs)
    if c is None: return None
    chi,eta_e,mu_loc,rho=c
    b=1.0/sqrtN(eta_e)                      # S1 law
    g=1.0/math.sqrt(1-b*b)
    one_plus_z=g*(1-b*mu_loc)
    return (1.0/one_plus_z)-1.0, mu_loc, b, eta_e

# --- limiting cases ---
t_obs=1.0
eta_o=2*math.sqrt(t_obs); rs_o=r_star(eta_o)
s0=shift(1.0, 0.0, t_obs)
chk("LC1 centred observer: the crossing is head-on (mu_loc = 1) in every direction",
    s0 is not None and abs(s0[1]-1.0)<1e-9, f"mu_loc={s0[1]:.12f}" if s0 else "no crossing")
sA=shift(1.0, 1e-6*rs_o, t_obs); sB=shift(-1.0, 1e-6*rs_o, t_obs)
chk("LC2 vanishing offset: the pattern becomes isotropic",
    abs(sA[0]-sB[0])<1e-4, f"|dT/T(+1) - dT/T(-1)| = {abs(sA[0]-sB[0]):.2e}")
b_at=1.0/sqrtN(shift(1.0,0.0,t_obs)[3])
chk("LC3 beta at the crossing equals 1/z_c (the two laws are reciprocal)",
    abs(b_at-1.0/(2.5496))<2e-3, f"beta={b_at:.6f} vs 1/z_c={1/2.5496:.6f}")

print(f"\nObserver at t_obs = t_crit; shock at comoving r_* = {rs_o:.6f}")
print("Kinematic Delta T / T across the sky, by offset (mu = +1 is toward the near wall):\n")
print(f"{'x_off/r_*':>10} {'mu':>7} {'mu_loc':>9} {'beta':>8} {'dT/T':>12}")
rows_out=[]
for f in [0.0, 0.001, 0.01, 0.05, 0.1]:
    x=f*rs_o
    vals=[]
    for mu in [1.0, 0.5, 0.0, -0.5, -1.0]:
        s=shift(mu,x,t_obs)
        if s is None:
            print(f"{f:10.3f} {mu:7.2f}    (no crossing in this direction)"); continue
        dT,mul,b,_=s; vals.append(dT)
        print(f"{f:10.3f} {mu:7.2f} {mul:9.6f} {b:8.5f} {dT:+12.6f}")
    if vals: rows_out.append((f,min(vals),max(vals),max(vals)-min(vals)))
    print()

print(f"{'x_off/r_*':>10} {'min dT/T':>12} {'max dT/T':>12} {'span':>12}  vs CMB 1e-5")
for f,lo,hi,span in rows_out:
    print(f"{f:10.3f} {lo:+12.6f} {hi:+12.6f} {span:12.6f}  {span/1e-5:10.1e}x")

# --- the observable is the ANISOTROPY, not the monopole ---
# A uniform shift merely rescales the mean temperature, which is not independently predicted,
# so it is absorbed. The observable is the span across the sky.
def span_of(f):
    x=f*rs_o; vals=[]
    for mu in np.linspace(-1,1,41):
        s_=shift(mu,x,t_obs)
        if s_ is None: return None
        vals.append(s_[0])
    return max(vals)-min(vals)

f1,f2=1e-4,1e-3
c1,c2=span_of(f1)/f1, span_of(f2)/f2
chk("LC4 anisotropy span is linear in the offset for small offsets",
    abs(c1/c2-1)<1e-2, f"span/f = {c1:.4f} at f=1e-4 vs {c2:.4f} at f=1e-3")

CMB=1e-5
f_lim=brentq(lambda f: span_of(f)-CMB, 1e-9, 1e-2, xtol=1e-14)
print("")
print(f"COEFFICIENT: anisotropy span = {c2:.3f} x (x_off / r_*) for small offsets.")
print("*** WITHDRAWN OUTPUT — the bound printed below is SUPERSEDED and NOT CLAIMED. ***")
print("*** It compares the full span against the l>=2 scale; the pattern is dipole-dominated,")
print("*** and it predates the monopole normalisation. Live value: P2_P4_RECEIPT.md. ***")
print(f"EXCLUSION: span exceeds the observed CMB anisotropy ({CMB:.0e}) unless")
print(f"           x_off / r_* < {f_lim:.3e}  -- i.e. the observer must sit within")
print(f"           {f_lim*1e6:.1f} parts per million of the exact centre.")
print("NOTE: the ~+0.51 monopole common to all directions is NOT an observable -- it rescales")
print("      the mean temperature, which the model does not independently predict.")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} limiting-case checks passed")
sys.exit(1 if nf else 0)
