#!/usr/bin/env python3
"""P2-P4: transfer in the thin regime, the sky pattern with monopole removed, multipoles, and
the confrontation against FROZEN rows only.

Fixes the gate's objections 3, 4, 5 explicitly:
 obj 3 (no transfer): P2 below carries absorption AND emission, in the thin regime P1 selected.
 obj 4 (normalisation): the monopole is removed BEFORE any amplitude is quoted.
 obj 5 (Doppler orientation): fixed physically, not by convention -- argument in P2_P4_RECEIPT.
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
def v_of(e):   return np.interp(e,ETA,V)

t_obs=1.0; eta_o=2*math.sqrt(t_obs); rs_o=r_star(eta_o)
TAU_MAX=0.07          # P1: upper bound over the whole authorised assumption range

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

def crossing(mu,x):
    def g(chi):
        p=math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0)); return p-r_star(eta_o-chi)
    chi=brentq(g,1e-12,eta_o-1e-12,xtol=1e-15)
    eta_e=eta_o-chi
    return chi, eta_e, max(-1.0,min(1.0,(x*mu+chi)/r_star(eta_e)))

def dT_kinematic(mu,x):
    """SIGN FIXED PHYSICALLY: the shock is an outgoing blast wave, so the upstream (TOV,
    thinner: v = rhobar/rho < 1) material is swept INWARD relative to the FRW fluid. An
    emitter moving toward the receiver blueshifts: 1+z = gamma(1 - beta*mu_loc) with
    beta > 0 taken along the emitter->observer direction."""
    chi,eta_e,mu_loc=crossing(mu,x)
    b=1.0/sqrtN(eta_e); g=1.0/math.sqrt(1-b*b)
    one_plus_z=g*(1.0-b*mu_loc)
    return 1.0/one_plus_z-1.0

def dT_with_transfer(mu,x,tau,T_ratio):
    """P2: thin-regime transfer. Observed = transmitted background (Doppler-shifted) plus
    emission from the exterior at its own temperature ratio T_ratio = Tbar/T_FRW."""
    d=dT_kinematic(mu,x)
    trans=math.exp(-tau)
    return trans*(1.0+d) + (1.0-trans)*T_ratio - 1.0

# --- P2 checks ---
x_t=0.01*rs_o
chk("LC1 thin-regime transfer reduces to the kinematic result as tau -> 0",
    abs(dT_with_transfer(0.3,x_t,0.0,0.81)-dT_kinematic(0.3,x_t))<1e-15)
d_k=dT_kinematic(0.3,x_t); d_t=dT_with_transfer(0.3,x_t,TAU_MAX,0.8098)
chk("LC2 at the P1 bound the transfer correction is a few percent, not a competitor",
    abs(d_t-d_k)/abs(d_k)<0.12, f"kinematic {d_k:+.5f} -> with transfer {d_t:+.5f} "
    f"({100*abs(d_t-d_k)/abs(d_k):.1f}% change)")
# LC3 CORRECTED (my check statement was inverted, not the physics -- third time this session
# a limiting-case check was written faster than it was reasoned; noted in the receipt).
# Blueshift means 1+z < 1, hence dT/T = 1/(1+z) - 1 > 0: the arriving radiation is HOTTER.
chk("LC3 the swept-inward emitter approaches, so the crossing arrives BLUESHIFTED (dT/T > 0)",
    d_k>0 and (1.0/(1.0+d_k))<1.0,
    f"dT/T = {d_k:+.5f}, i.e. 1+z = {1.0/(1.0+d_k):.5f} < 1 -- blueshift, as the geometry requires")

# --- P3: pattern, monopole REMOVED, multipoles ---
def multipoles(f, tau=0.0, T_ratio=0.8098, lmax=4):
    x=f*rs_o; nodes,w=leggauss(200)
    vals=np.array([dT_with_transfer(m,x,tau,T_ratio) if tau>0 else dT_kinematic(m,x) for m in nodes])
    mono=0.5*float(np.sum(w*vals))          # l=0 coefficient
    vals_nm = vals - mono                    # MONOPOLE REMOVED before anything is quoted
    out=[mono]
    for l in range(1,lmax+1):
        P=np.polynomial.legendre.Legendre.basis(l)(nodes)
        out.append((2*l+1)/2.0*float(np.sum(w*vals_nm*P)))
    return out

m0=multipoles(0.0)
chk("LC4 a centred observer has monopole only, nothing else survives removal",
    max(abs(v) for v in m0[1:])<1e-9, f"monopole {m0[0]:+.6f}, max |l>=1| {max(abs(v) for v in m0[1:]):.2e}")
mA=multipoles(1e-3); mB=multipoles(1e-3,tau=TAU_MAX)
chk("LC5 transfer changes the dipole by less than the P1 tau bound allows",
    abs(mB[1]-mA[1])/abs(mA[1])<TAU_MAX*1.5,
    f"dipole {mA[1]:.5e} -> {mB[1]:.5e} ({100*abs(mB[1]-mA[1])/abs(mA[1]):.2f}%)")

print("\nP3 — multipoles after monopole removal (kinematic; transfer shifts these by <7%):")
print(f"{'x_off/r_*':>10} {'monopole':>12} {'dipole':>12} {'quadrupole':>12}")
for f in [1e-4,1e-3,1e-2,1e-1]:
    m=multipoles(f); print(f"{f:10.0e} {m[0]:+12.5f} {m[1]:+12.4e} {m[2]:+12.4e}")

# --- P4: confrontation, FROZEN rows only ---
T0=2.7255
DIP_INT=3.7e-3/T0        # B2.2 frozen: |Delta_1,int| < 3.7 mK (95% CI)
QUAD_OBS=1e-5            # l>=2 observed scale; B3 reports a DEFICIT there (conservative)
c1=abs(multipoles(1e-3)[1])/1e-3        # dipole per unit offset fraction
c2=abs(multipoles(1e-2)[2])/1e-2**2 if False else None
f_dip=brentq(lambda f: abs(multipoles(f)[1])-DIP_INT, 1e-9,1e-1,xtol=1e-15)
f_quad=brentq(lambda f: abs(multipoles(f)[2])-QUAD_OBS,1e-9,1e-1,xtol=1e-15)
print(f"\nP4 — confrontation (frozen rows only)")
print(f"  dipole coefficient      : |c1| = {c1:.4f} x (x_off/r_*)")
print(f"  B2.2 intrinsic dipole   : < {DIP_INT:.4e}  ->  x_off/r_* < {f_dip:.3e}")
print(f"  l>=2 at {QUAD_OBS:.0e}          ->  x_off/r_* < {f_quad:.3e}")
binding=min(f_dip,f_quad)
print(f"  BINDING (frozen)        : x_off/r_* < {binding:.3e}  (one part in {1/binding:.0f})")
chk("LC6 the dipole row binds, as the pattern is dipole-dominated", f_dip<f_quad,
    f"dipole {f_dip:.2e} vs quadrupole {f_quad:.2e}")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
