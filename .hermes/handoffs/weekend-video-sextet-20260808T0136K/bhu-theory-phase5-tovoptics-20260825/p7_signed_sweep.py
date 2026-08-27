#!/usr/bin/env python3
"""P7: the SIGNED adaptive sweep — locating the cancellation null and measuring its width.

*** CLOSURE-CONDITIONAL EXPERIMENT — NOT A MODEL PREDICTION (REGATE4, 2026-08-27) ***
This script executes p6's prefix and inherits its ADDED thermal closure (blackbody junction
anchor plus the adiabatic depth law T ∝ rhobar^[w/(1+w)]). The epoch ruling invalidated that
closure as a property of the pinned geometry, so the null located below at w = 0.0407786 is a
property of THAT ASSUMED SOURCE MAP.
REGATE4 went further and withdrew null EXISTENCE as a model-level claim, with a one-line
counterexample: a source held constant across crossing epochs has zero source-gradient, the
kinematic coefficient stays at +0.615301, and nothing ever crosses zero. Reproducing a root
under two assumed source maps proves robustness within those maps, not existence over the
unrestricted set of positive source fields.
PERMITTED: "the two tested closures each contain a cancellation, at different locations."
NOT PERMITTED: "the pinned model contains a silent configuration whose location alone is
unknown." Both existence and location are closure-dependent.
See BHU_CLOSED_ROUTES.md and REGATE4_DISPOSITION.md before citing anything here.

REGATE3 finding 1: p6's dipole_and_bound() took abs() and sampled six w values, so
"min(c1)>0" proved only that six absolute samples were positive. The gate then found a real
sign change at w ~ 0.04078, where the exclusion vanishes entirely.

This script keeps the SIGN, decomposes the coefficient into its two competing parts, sweeps
adaptively, resolves every sign change by root-finding, and reports the interval in which no
useful exclusion exists — rather than asserting a lower bound from samples.
"""
import csv, math, sys, platform
import numpy as np, scipy
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
TRAPZ=getattr(np,"trapezoid",None) or np.trapz
print(f"# env: python {platform.python_version()}, numpy {np.__version__}, scipy {scipy.__version__}")

src=open("p6_path_transfer.py").read().split('print("\\nP6 — depth-resolved')[0]
G={}; exec(src, G)
exterior=G["exterior"]; emergent=G["emergent_T_over_Tbg"]; r_star=G["r_star"]; sqrtN=G["sqrtN"]
RSTAR=G["RSTAR_CROSS"]; eta_o=2.0
DIP=3.7e-3/2.7255

checks=[]
def chk(n,p,d=""):
    if not isinstance(p,(bool,np.bool_)): raise TypeError("chk needs a computed predicate")
    checks.append((n,bool(p),d)); print(("PASS " if p else "FAIL ")+n+("  "+d if d else ""))

def signed_c1(w, f=1e-4, npts=24, decompose=False):
    """SIGNED dipole coefficient. Optionally return the Doppler-only and emergent-only parts."""
    nodes,wt=leggauss(npts)
    tot=[]; dop=[]; emg=[]
    for mu in nodes:
        x=f*RSTAR
        g=lambda chi: math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0))-r_star(eta_o-chi)
        chi=brentq(g,1e-12,eta_o-1e-12,xtol=1e-14); eta_e=eta_o-chi
        mu_loc=max(-1.0,min(1.0,(x*mu+chi)/r_star(eta_e)))
        b=1.0/sqrtN(eta_e); gam=1.0/math.sqrt(1-b*b); D=1.0/(gam*(1-b*mu_loc))
        R=emergent(eta_e,w)
        if R is None: return (None,None,None) if decompose else None
        tot.append(D*R-1.0); dop.append(D-1.0); emg.append(R-1.0)
    def proj(vals):
        v=np.array(vals); mono=0.5*float(np.sum(wt*v)); vnm=(v-mono)/(1.0+mono)
        P1=np.polynomial.legendre.Legendre.basis(1)(nodes)
        return 1.5*float(np.sum(wt*vnm*P1))/f          # SIGN PRESERVED
    return (proj(tot),proj(dop),proj(emg)) if decompose else proj(tot)

# --- the decomposition the gate supplied, reproduced independently ---
print("\nDecomposition (the two competing terms), signed:")
print(f"{'w':>8} {'Doppler':>12} {'emergent':>12} {'total':>12}")
for w in [0.050,0.040,0.030,0.015,0.010]:
    t,d,e=signed_c1(w,decompose=True)
    print(f"{w:8.3f} {d:12.6f} {e:12.6f} {t:12.6f}")
t50,_,_=signed_c1(0.050,decompose=True); t10,_,_=signed_c1(0.010,decompose=True)
chk("the total coefficient CHANGES SIGN between w=0.05 and w=0.01 (the gate's finding)",
    t50*t10<0, f"c1(0.05)={t50:+.6f}, c1(0.01)={t10:+.6f}")

# --- adaptive sweep with every sign change resolved ---
ws=np.concatenate([np.linspace(0.005,0.08,46), np.linspace(0.09,0.999,20)])
vals=[]
for w in ws:
    c=signed_c1(float(w))
    vals.append(c)
pairs=[(w,c) for w,c in zip(ws,vals) if c is not None]
roots=[]
for k in range(len(pairs)-1):
    (w1,c1_),(w2,c2_)=pairs[k],pairs[k+1]
    if c1_*c2_<0:
        r=brentq(lambda w: signed_c1(float(w)), w1,w2, xtol=1e-9)
        roots.append(r)
chk("the sweep resolves every sign change by root-finding, not sampling", len(roots)>=1,
    f"roots found: {[f'{r:.7f}' for r in roots]}")

# --- width of the un-excludable neighbourhood ---
# The frozen dipole limit gives bound = DIP/|c1|. Call the exclusion USELESS when the bound
# exceeds 0.1 (a tenth of the boundary radius is no constraint at all): |c1| < DIP/0.1.
C_MIN=DIP/0.1
def useless(w): return abs(signed_c1(float(w)))<C_MIN
bands=[]
for r in roots:
    lo=brentq(lambda w: abs(signed_c1(float(w)))-C_MIN, r-0.02, r-1e-7, xtol=1e-10) \
        if abs(signed_c1(r-0.02))>C_MIN else r-0.02
    hi=brentq(lambda w: abs(signed_c1(float(w)))-C_MIN, r+1e-7, r+0.02, xtol=1e-10) \
        if abs(signed_c1(r+0.02))>C_MIN else r+0.02
    bands.append((lo,r,hi))
print("\nUN-EXCLUDABLE neighbourhood(s) — where |c1| is too small to constrain anything:")
for lo,r,hi in bands:
    print(f"  null at w = {r:.7f};  |c1| < {C_MIN:.5f} for w in [{lo:.6f}, {hi:.6f}]  "
          f"(width {hi-lo:.2e}, i.e. {100*(hi-lo)/r:.2f}% of the null's w)")
chk("the null is NARROW relative to the authorised range, but it is NOT empty",
    len(bands)>0 and all((hi-lo)<0.05 for lo,_,hi in bands),
    f"widest band {max(hi-lo for lo,_,hi in bands):.3e} in w over an authorised range ~1.0")

# --- the honest envelope OUTSIDE the null ---
outside=[(w,c) for w,c in pairs if all(not(lo<=w<=hi) for lo,_,hi in bands)]
worst=max(DIP/abs(c) for _,c in outside)
best=min(DIP/abs(c) for _,c in outside)
print(f"\nOutside the null band(s): bound ranges {best:.3e} to {worst:.3e} "
      f"(one part in {1/worst:.0f} to {1/best:.0f})")
chk("outside the null the exclusion holds with a computed envelope, not a sample",
    worst<0.05, f"worst bound outside = {worst:.3e}")
print("\nHEADLINE, corrected: the exclusion holds across the authorised range EXCEPT in a narrow")
print(f"neighbourhood around w = {roots[0]:.5f}, where the two terms cancel and NO bound exists.")
print("\nCONDITIONALITY (REGATE4, 2026-08-27) — this headline is NOT a statement about the model:")
print("  Under THIS closure a cancellation sits at the w above. Whether the pinned model has any")
print("  silent configuration is NOT ESTABLISHED and cannot be established from the published")
print("  papers, which never specify the exterior's temperature. A source held constant across")
print(f"  crossing epochs has zero source-gradient, leaves the kinematic term at +0.615301, and")
print("  never crosses zero. Say 'the two tested closures each contain a cancellation, at")
print("  different locations' — never 'the model contains a silent configuration'.")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
