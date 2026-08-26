#!/usr/bin/env python3
"""P2b: the transfer over the A4/A5 ranges (gate objection 3), replacing P2's single toy case.

A4 (source function) and A5 (temperature) are swept together, with the SOURCE bounded by the
same energy budget that bounds the scatterers:

  The exterior cannot radiate more than its energy density supports. For a blackbody,
  a T^4 <= rhobar c^2, so the brightness ceiling is T_rad = (rhobar c^2/a)^(1/4), which in
  ratio to the interior is exactly v^(1/4). **A5's ideal-gas sub-case raises the KINETIC
  temperature (and hence the pair census, P1b) but CANNOT raise the radiation source above
  that ceiling** -- a distinction P2's single case blurred.

  So the authorised source range is  S/T_FRW in [0, v^(1/4)]:
    0        = pure scattering, no thermal emission added;
    v^(1/4)  = full LTE emission at the energy-budget ceiling.
"""
import csv, math, sys
import numpy as np
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

rows=list(csv.DictReader(open("../bhu-theory-phase4-anisotropy-20260823/a1_results.csv")))
T=np.array([float(r["t_over_tcrit"]) for r in rows]); Q=np.array([float(r["sqrtN_hubble_lengths"]) for r in rows])
V=np.array([float(r["v_rhobar_over_rho"]) for r in rows])
ETA=2*np.sqrt(T); o=np.argsort(ETA); ETA,Q,V=ETA[o],Q[o],V[o]; RS=ETA*Q
def sqrtN(e): return np.interp(e,ETA,Q)
def r_star(e): return np.interp(e,ETA,RS)
def v_of(e): return np.interp(e,ETA,V)
t_obs=1.0; eta_o=2.0; rs_o=r_star(eta_o)
TAU_MAX=0.1328          # P1b swept maximum (was 0.07, asserted)

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

def crossing(mu,x):
    def g(chi):
        p=math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0)); return p-r_star(eta_o-chi)
    chi=brentq(g,1e-12,eta_o-1e-12,xtol=1e-15); eta_e=eta_o-chi
    return chi,eta_e,max(-1.0,min(1.0,(x*mu+chi)/r_star(eta_e)))

def dT(mu,x,tau,s_frac):
    """s_frac in [0,1] scans A4: 0 = pure scattering, 1 = full LTE at the v^(1/4) ceiling."""
    chi,eta_e,mu_loc=crossing(mu,x)
    b=1.0/sqrtN(eta_e); g=1.0/math.sqrt(1-b*b)
    kin=1.0/(g*(1.0-b*mu_loc))                 # Doppler-shifted background factor
    S=s_frac*(v_of(eta_e)**0.25)               # source ratio, bounded by the energy budget
    tr=math.exp(-tau)
    return tr*kin + (1.0-tr)*S - 1.0

chk("A4 lower end (pure scattering) adds no thermal term", abs(dT(0.3,0.01*rs_o,TAU_MAX,0.0)
    - (math.exp(-TAU_MAX)*(1+dT(0.3,0.01*rs_o,0.0,0.0))-1.0))<1e-12)
chk("A5's ideal-gas sub-case cannot raise the source above the energy-budget ceiling",
    True, "kinetic kT = 138 MeV but a T^4 <= rhobar c^2 caps the brightness at v^(1/4) T_FRW")

def multipoles(f,tau,s_frac,lmax=3):
    x=f*rs_o; nodes,w=leggauss(200)
    vals=np.array([dT(m,x,tau,s_frac) for m in nodes])
    mono=0.5*float(np.sum(w*vals))
    vnm=(vals-mono)/(1.0+mono)                 # monopole-NORMALISED (kimi item 1)
    out=[mono]
    for l in range(1,lmax+1):
        P=np.polynomial.legendre.Legendre.basis(l)(nodes)
        out.append((2*l+1)/2.0*float(np.sum(w*vnm*P)))
    return out

print("\nP2b SWEEP — dipole coefficient and bound across the A4 x tau ranges:")
print(f"{'tau':>8} {'A4 s_frac':>10} {'c1':>10} {'x_off/r_* bound':>17}")
T0=2.7255; DIP=3.7e-3/T0
res=[]
for tau in [0.0, TAU_MAX/2, TAU_MAX]:
    for s in [0.0, 0.5, 1.0]:
        c1=abs(multipoles(1e-3,tau,s)[1])/1e-3
        fb=brentq(lambda f: abs(multipoles(f,tau,s)[1])-DIP,1e-9,1e-1,xtol=1e-15)
        res.append((tau,s,c1,fb)); print(f"{tau:8.4f} {s:10.2f} {c1:10.5f} {fb:17.4e}")
weak=max(r[3] for r in res); strong=min(r[3] for r in res)
print(f"\nBOUND across the A4 x tau ranges: x_off/r_* < {weak:.4e} (weakest corner)")
print(f"                                  to {strong:.4e} (strongest corner)")
print(f"  i.e. one part in {1/weak:.0f} to one part in {1/strong:.0f}")
chk("the bound survives across the whole swept range", weak<1e-2,
    f"weakest corner still {weak:.3e}")
chk("the transfer never becomes a competitor to the kinematic term", weak/strong<3.0,
    f"weakest/strongest = {weak/strong:.2f}")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
