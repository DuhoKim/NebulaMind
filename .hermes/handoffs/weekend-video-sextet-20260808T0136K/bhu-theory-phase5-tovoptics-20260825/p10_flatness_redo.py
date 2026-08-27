#!/usr/bin/env python3
"""P10: Redo the flatness measurement using the correct quantities (signed c1 and 1-R)."""
import math, sys
import numpy as np
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

src=open("p6_path_transfer.py").read().split('print("\\nP6 — depth-resolved')[0]
G={}; exec(src,G)
exterior=G["exterior"]; r_star=G["r_star"]; sqrtN=G["sqrtN"]; RST=G["RSTAR_CROSS"]
TRAPZ=G["TRAPZ"]; C=G["C"]; G_=G["G"]; A_RAD=G["A_RAD"]; T_CRIT=G["T_CRIT"]
eta_o=2.0

checks=[]
def chk(n,p,d=""):
    if not isinstance(p,(bool,np.bool_)): raise TypeError("chk needs a computed predicate")
    checks.append((n,bool(p),d)); print(("PASS " if p else "FAIL ")+n+("  "+d if d else ""))

def emergent_K(eta_e, w, K):
    e=exterior(eta_e,w)
    if e is None: return None
    Tbg=(3.0/(32*math.pi*((eta_e/2)**2)**2)*(C*C/G_)/((C*T_CRIT)**2)*C*C/A_RAD)**0.25
    tau=e['tau']*K; dtau=e['dtau']*K; tau_tot=e['tau_tot']*K
    src_=e['T_rad']/Tbg
    I=math.exp(-tau_tot)*(e['Z'][-1]**4)+float(TRAPZ((src_**4)*(e['Z']**4)*np.exp(-tau)*dtau,e['rr']))
    return (max(I,0.0))**0.25

def signed_c1_K(w,K,f=1e-3,npts=24):
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

def get_R(w, K, mu, f):
    x=f*RST
    g=lambda chi: math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0))-r_star(eta_o-chi)
    chi=brentq(g,1e-12,eta_o-1e-12,xtol=1e-14); eta_e=eta_o-chi
    R_emerg=emergent_K(eta_e,w,K)
    return R_emerg

def resolution_limit(w_probe):
    """Largest opacity multiplier whose photosphere this grid still resolves (max cell dtau <= 1)."""
    e=exterior(0.5633887, w_probe)
    if e is None: return None, None
    step=0.5*(e['dtau'][1:]+e['dtau'][:-1])*np.diff(e['rr'])
    return e, 1.0/float(step.max())

w_val = 0.2456
f_val = 1e-3

_, K_MAX = resolution_limit(w_val)
print(f"Grid resolves the photosphere up to K = {K_MAX:.4g} at w = {w_val}.")
print("Beyond this, max per-cell d(tau) > 1, so the result is unresolved.\n")

K_list = [1e-2, 1e-1, 1.0, 1e1, 1e2, 1e3]

print(f"{'K':>10} {'R(+1)/R(-1)':>15} {'1-R':>15} {'signed_c1':>15}  status")
results = {}
for K in K_list:
    if K > K_MAX:
        print(f"{K:10.0e} {'—':>15} {'—':>15} {'—':>15}  UNRESOLVED")
        continue
    R_p = get_R(w_val, K, 1.0, f_val)
    R_m = get_R(w_val, K, -1.0, f_val)
    R_ratio = R_p / R_m
    c1 = signed_c1_K(w_val, K, f=f_val)
    results[K] = (R_ratio, c1)
    print(f"{K:10.0e} {R_ratio:15.9f} {1.0-R_ratio:15.9f} {c1:15.6f}  resolved")

print()
if 0.01 in results:
    r_001 = results[0.01][0]
    c1_001 = results[0.01][1]
    chk("R anchor K=0.01 reproduces", abs(r_001 - 0.997726210) < 1e-8, f"got {r_001:.9f}")
    chk("c1 anchor K=0.01 reproduces", abs(c1_001 - (-0.522912)) < 1e-6, f"got {c1_001:.6f}")

if 100.0 in results:
    r_100 = results[100.0][0]
    c1_100 = results[100.0][1]
    chk("R anchor K=100 reproduces", abs(r_100 - 0.998857603) < 1e-8, f"got {r_100:.9f}")
    chk("c1 anchor K=100 reproduces", abs(c1_100 - 0.043763) < 1e-6, f"got {c1_100:.6f}")

nf = sum(1 for _, ok, _ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
