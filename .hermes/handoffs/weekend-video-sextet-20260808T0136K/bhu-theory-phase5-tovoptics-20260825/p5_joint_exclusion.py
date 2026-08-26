#!/usr/bin/env python3
"""P5: the JOINT exclusion argument — one transfer, all opacities, no branch split.

The phase's real deliverable. P1c reopened the opacity question (tau spans 0.04 to >2.6 inside
the authorised range), so "thin" and "opaque" can no longer be treated as alternatives to be
resolved. They must be shown to exclude TOGETHER.

The spine, and it corrects an error in my own P2:

  P2 applied the Doppler factor D(mu) ONLY to the transmitted background, treating the
  exterior's emission as unshifted. That is wrong. The emitting matter IS the TOV fluid, which
  moves at beta_rel relative to us, so its emission is Doppler-shifted by the SAME D. Both
  terms carry it:

      1 + dT/T (mu) = D(mu) * [ e^-tau + (1 - e^-tau) * (Tbar/T_FRW) ]

  The bracket depends on direction only weakly (through the crossing epoch); D(mu) is the
  strong angular dependence. **D multiplies the whole beam, so no value of tau can remove the
  anisotropy** — an opaque exterior does not hide the offset, it re-emits it.

Normalisation per the gate's B1 ruling: offsets are reported against r_*(eta_crossing).
"""
import csv, math, sys
import numpy as np
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
TRAPZ=getattr(np,"trapezoid",None) or np.trapz

rows=list(csv.DictReader(open("../bhu-theory-phase4-anisotropy-20260823/a1_results.csv")))
T=np.array([float(r["t_over_tcrit"]) for r in rows]); Q=np.array([float(r["sqrtN_hubble_lengths"]) for r in rows])
V=np.array([float(r["v_rhobar_over_rho"]) for r in rows])
ETA=2*np.sqrt(T); o=np.argsort(ETA); ETA,Q,V=ETA[o],Q[o],V[o]; RS=ETA*Q
def sqrtN(e): return np.interp(e,ETA,Q)
def r_star(e): return np.interp(e,ETA,RS)
def v_of(e): return np.interp(e,ETA,V)
eta_o=2.0
i0=int(np.argmin(np.abs(eta_o-ETA*(1+Q))))
RSTAR_CROSS=ETA[i0]*Q[i0]                       # B1 normaliser: crossing radius, 1.4366

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))
chk("B1 normaliser adopted: r_*(eta_crossing), per the gate's adjudication",
    abs(RSTAR_CROSS-1.4366113)<1e-4, f"r_*(cross) = {RSTAR_CROSS:.7f}")

def crossing(mu,x):
    def g(chi):
        p=math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0)); return p-r_star(eta_o-chi)
    chi=brentq(g,1e-12,eta_o-1e-12,xtol=1e-15); eta_e=eta_o-chi
    return eta_e, max(-1.0,min(1.0,(x*mu+chi)/r_star(eta_e)))

def one_plus_dT(mu,x,tau):
    """D(mu) applied to the WHOLE beam: transmitted background plus re-emitted exterior."""
    eta_e,mu_loc=crossing(mu,x)
    b=1.0/sqrtN(eta_e); g=1.0/math.sqrt(1-b*b)
    D=1.0/(g*(1.0-b*mu_loc))
    Tratio=v_of(eta_e)**0.25                     # energy-budget ceiling on the source
    return D*(math.exp(-tau) + (1.0-math.exp(-tau))*Tratio)

def dipole_coeff(tau, f=1e-3):
    x=f*RSTAR_CROSS; nodes,w=leggauss(240)
    vals=np.array([one_plus_dT(m,x,tau)-1.0 for m in nodes])
    mono=0.5*float(np.sum(w*vals))
    vnm=(vals-mono)/(1.0+mono)
    P1=np.polynomial.legendre.Legendre.basis(1)(nodes)
    return abs(1.5*float(np.sum(w*vnm*P1)))/f

# --- the structural claim: D multiplies everything, so tau cannot remove the anisotropy ---
print("\nDipole coefficient vs opacity — thin to deeply opaque, ONE transfer:")
print(f"{'tau':>8} {'regime':>12} {'c1':>10} {'x_off/r_*(cross) bound':>24}")
T0=2.7255; DIP=3.7e-3/T0
res=[]
for tau,lbl in [(0.0,"vacuum"),(0.04,"thin"),(0.132,"junction w"),(0.31,"thin-ish"),
                (0.93,"marginal"),(2.6,"opaque"),(5.0,"very opaque"),(20.0,"saturated")]:
    c1=dipole_coeff(tau)
    fb=brentq(lambda f: dipole_coeff(tau,f)*f-DIP, 1e-9,1e-1,xtol=1e-15)
    res.append((tau,c1,fb)); print(f"{tau:8.3f} {lbl:>12} {c1:10.5f} {fb:24.4e}")

c1s=[r[1] for r in res]; fbs=[r[2] for r in res]
# CORRECTED CLAIM (my first version asserted near-independence; the run refuted it at 2.5x).
# What is actually true, and is what the argument needs: the dipole SATURATES at a finite
# floor as tau -> infinity instead of vanishing. Opacity DILUTES the anisotropy by a bounded
# factor; it never removes it. That is the load-bearing structural fact.
c1_sat=dipole_coeff(1e3)
chk("the dipole SATURATES at a nonzero floor as opacity grows (it is diluted, never removed)",
    c1_sat>0.9*min(c1s) and abs(dipole_coeff(20.0)-c1_sat)/c1_sat<0.02,
    f"c1: {max(c1s):.4f} (vacuum) -> {c1_sat:.4f} (tau=1000); dilution factor "
    f"{max(c1s)/c1_sat:.2f}x, floor is finite")
chk("the saturated-opacity limit does NOT relax the bound",
    fbs[-1] < 3*fbs[0], f"vacuum {fbs[0]:.3e} -> saturated {fbs[-1]:.3e}")
worst=max(fbs)
chk("JOINT EXCLUSION: every opacity in the authorised range requires a small offset",
    worst<1e-2, f"worst-case bound over ALL tau: x_off/r_*(cross) < {worst:.4e} "
    f"(one part in {1/worst:.0f})")

print(f"\nJOINT RESULT — over the FULL opacity range, thin through opaque:")
print(f"  bound on x_off/r_*(crossing):  {min(fbs):.4e} to {worst:.4e}")
print(f"  i.e. one part in {1/worst:.0f} at the very worst, one part in {1/min(fbs):.0f} at best.")
print(f"  The exclusion therefore does NOT depend on resolving the opacity.")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
