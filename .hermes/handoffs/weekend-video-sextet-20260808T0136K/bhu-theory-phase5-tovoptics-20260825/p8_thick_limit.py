#!/usr/bin/env python3
"""P8: does my full transfer reduce to the seat's surface model in the optically thick limit?

FACTOR_OF_TWO_RESOLVED.md established that the two nulls belong to two models: theirs is
junction-Doppler times a shock-SURFACE source carried along the crossing epoch, with no opacity
and no depth redshift; mine integrates the whole column. If they are NESTED, then driving my
opacity up must make my emergent term approach theirs, and my null must migrate to theirs at
w = 0.0815000. If it does not, one of us has an error.

Opacity is scaled by a multiplier K applied to the scatterer density, holding the profile,
source and geometry fixed — so this isolates the thick limit rather than changing the model.
"""
import math, sys
import numpy as np
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
src=open("p6_path_transfer.py").read().split('print("\\nP6 — depth-resolved')[0]
G={}; exec(src,G)
exterior=G["exterior"]; r_star=G["r_star"]; sqrtN=G["sqrtN"]; RST=G["RSTAR_CROSS"]
TRAPZ=G["TRAPZ"]; C=G["C"]; G_=G["G"]; A_RAD=G["A_RAD"]; T_CRIT=G["T_CRIT"]
eta_o=2.0; THEIR_NULL=0.0815000315521189; MY_NULL=0.0407786

checks=[]
def chk(n,p,d=""):
    if not isinstance(p,(bool,np.bool_)): raise TypeError("chk needs a computed predicate")
    checks.append((n,bool(p),d)); print(("PASS " if p else "FAIL ")+n+("  "+d if d else ""))

def emergent_K(eta_e, w, K):
    """Emergent temperature ratio with the opacity scaled by K (profile/source unchanged)."""
    e=exterior(eta_e,w)
    if e is None: return None
    Tbg=(3.0/(32*math.pi*((eta_e/2)**2)**2)*(C*C/G_)/((C*T_CRIT)**2)*C*C/A_RAD)**0.25
    tau=e['tau']*K; dtau=e['dtau']*K; tau_tot=e['tau_tot']*K
    src_=e['T_rad']/Tbg
    I=math.exp(-tau_tot)*(e['Z'][-1]**4)+float(TRAPZ((src_**4)*(e['Z']**4)*np.exp(-tau)*dtau,e['rr']))
    return (max(I,0.0))**0.25

def signed_c1_K(w,K,f=1e-4,npts=24):
    nodes,wt=leggauss(npts); vals=[]
    for mu in nodes:
        x=f*RST
        g=lambda chi: math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0))-r_star(eta_o-chi)
        chi=brentq(g,1e-12,eta_o-1e-12,xtol=1e-14); eta_e=eta_o-chi
        mu_loc=max(-1.0,min(1.0,(x*mu+chi)/r_star(eta_e)))
        b=1.0/sqrtN(eta_e); gam=1.0/math.sqrt(1-b*b); D=1.0/(gam*(1-b*mu_loc))
        R=emergent_K(eta_e,w,K)
        if R is None: return None
        vals.append(D*R-1.0)
    v=np.array(vals); m=0.5*float(np.sum(wt*v)); vn=(v-m)/(1.0+m)
    P1=np.polynomial.legendre.Legendre.basis(1)(nodes)
    return 1.5*float(np.sum(wt*vn*P1))/f

print("Null location as the exterior is driven optically thick (K = opacity multiplier):")
print(f"{'K':>10} {'tau at w=0.08':>14} {'null w':>12} {'-> their 0.081500':>20}")
locs=[]
for K in [1.0, 10.0, 1e2, 1e3, 1e4, 1e5]:
    e=exterior(2*math.sqrt((eta_o/2)**2*0+0.0793517)*0+0.5633887, 0.08)
    tau_at=e['tau_tot']*K if e else float('nan')
    try:
        root=brentq(lambda w: signed_c1_K(w,K), 0.02, 0.30, xtol=1e-9)
    except Exception:
        root=float('nan')
    locs.append(root)
    print(f"{K:10.0e} {tau_at:14.3f} {root:12.7f} {root/THEIR_NULL:20.4f}")

finite=[r for r in locs if np.isfinite(r)]
chk("a null exists at every opacity (the phenomenon is not an artifact of one regime)",
    len(finite)==len(locs), f"{len(finite)} of {len(locs)} opacities gave a root")
chk("the null MIGRATES as opacity increases (the models are not independent)",
    abs(finite[-1]-finite[0])>1e-3, f"K=1: {finite[0]:.7f} -> K=1e5: {finite[-1]:.7f}")
converged=abs(finite[-1]-THEIR_NULL)/THEIR_NULL
chk("in the THICK limit my null converges to the seat's surface-model null (models NESTED)",
    converged<0.02, f"K=1e5 null {finite[-1]:.7f} vs theirs {THEIR_NULL:.7f} "
    f"— {100*converged:.2f}% apart")

print(f"\nVERDICT: {'NESTED — my transfer reduces to their surface model as it goes thick.' if converged<0.02 else 'NOT NESTED — the thick limit does not reproduce their null; one model has an error.'}")
nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
