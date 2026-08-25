#!/usr/bin/env python3
"""S3: project the crossing pattern onto multipoles and confront the FROZEN bounds.

No new observational input: every number confronted comes from TRACK_B_FREEZE.md (gated
PASS both engines, verifier v8). Pattern from S2 (kinematic branch, blind-double confirmed).
"""
import csv, math, sys
import numpy as np
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

rows=list(csv.DictReader(open("../bhu-theory-phase4-anisotropy-20260823/a1_results.csv")))
T=np.array([float(r["t_over_tcrit"]) for r in rows]); Q=np.array([float(r["sqrtN_hubble_lengths"]) for r in rows])
ETA=2*np.sqrt(T); o=np.argsort(ETA); ETA,Q=ETA[o],Q[o]; RS=ETA*Q
def sqrtN(e): return np.interp(e,ETA,Q)
def r_star(e): return np.interp(e,ETA,RS)

t_obs=1.0; eta_o=2*math.sqrt(t_obs); rs_o=r_star(eta_o)
def dT(mu,x):
    def g(chi):
        p=math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0)); return p-r_star(eta_o-chi)
    chi=brentq(g,1e-12,eta_o-1e-12,xtol=1e-15)
    eta_e=eta_o-chi; mu_loc=max(-1,min(1,(x*mu+chi)/r_star(eta_e)))
    b=1.0/sqrtN(eta_e); g_=1/math.sqrt(1-b*b)
    return 1.0/(g_*(1-b*mu_loc))-1.0

def multipoles(f, lmax=6):
    """a_l0-equivalent: c_l = (2l+1)/2 * Integral dT(mu) P_l(mu) dmu  (axisymmetric)."""
    x=f*rs_o
    nodes,w=leggauss(200)
    vals=np.array([dT(m,x) for m in nodes])
    out=[]
    for l in range(lmax+1):
        P=np.polynomial.legendre.Legendre.basis(l)(nodes)
        out.append((2*l+1)/2.0*float(np.sum(w*vals*P)))
    return out

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

c0=multipoles(0.0)
chk("LC1 centred observer has only a monopole", max(abs(v) for v in c0[1:])<1e-9,
    f"max |c_l>=1| = {max(abs(v) for v in c0[1:]):.2e}")
c_small=multipoles(1e-4)
chk("LC2 the offset pattern is dipole-dominated", abs(c_small[1])>10*abs(c_small[2]),
    f"c1={c_small[1]:.3e} c2={c_small[2]:.3e}")

print("\nMultipole content of the kinematic crossing pattern (monopole excluded as unobservable):")
print(f"{'x_off/r_*':>10} {'c1 (dipole)':>14} {'c2 (quad)':>14} {'c3':>12}")
for f in [1e-4,1e-3,1e-2,1e-1]:
    c=multipoles(f); print(f"{f:10.0e} {c[1]:14.4e} {c[2]:14.4e} {c[3]:12.4e}")

# --- confrontation with FROZEN numbers only ---
# The pattern is DIPOLE-DOMINATED (c2/c1 ~ 4e-4), so the binding frozen bound is not the
# 1e-5 anisotropy scale -- an observed dipole exists at the 1e-3 level. The right frozen row
# is B2.2, the published bound on the INTRINSIC (non-kinematic) dipole, which is exactly what
# this effect would be:
#   B2.2 (frozen): |Delta_1,int| < 3.6-3.7 mK (95% CI), Ferreira & Quartin PRL 127, 101301.
T0=2.7255
DIP_INT = 3.7e-3/T0            # frozen intrinsic-dipole bound, fractional
DIP_TOT = 3362.08e-6/T0        # frozen B2.1 total solar dipole, for context only
QUAD_SCALE = 1e-5              # l>=2 observed anisotropy scale (B3 reports a DEFICIT: conservative)

f_int = brentq(lambda f: abs(multipoles(f)[1])-DIP_INT, 1e-9, 1e-1, xtol=1e-15)
f_tot = brentq(lambda f: abs(multipoles(f)[1])-DIP_TOT, 1e-9, 1e-1, xtol=1e-15)
f_quad= brentq(lambda f: abs(multipoles(f)[2])-QUAD_SCALE, 1e-9, 1e-1, xtol=1e-15)

print("\nCONFRONTATION (frozen rows only):")
print(f"  B2.2 intrinsic-dipole bound 3.7 mK / {T0} K = {DIP_INT:.4e}  -> x_off/r_* < {f_int:.3e}")
print(f"  B2.1 total solar dipole (context only)      = {DIP_TOT:.4e}  -> x_off/r_* < {f_tot:.3e}")
print(f"  l>=2 at {QUAD_SCALE:.0e}                                        -> x_off/r_* < {f_quad:.3e}")
print(f"\n  BINDING BOUND: x_off/r_* < {f_int:.3e}  (about one part in {1/f_int:.0f})")
print( "  from B2.2, the published INTRINSIC-dipole limit -- the correct row, because this")
print( "  effect produces a non-kinematic dipole, and it is not degenerate with our motion.")
chk("LC3 the pattern is dipole-dominated, so the dipole rows bind and l>=2 does not",
    f_int < f_quad, f"intrinsic-dipole bound {f_int:.2e} < quadrupole bound {f_quad:.2e}")
chk("LC4 the binding bound is weaker than a naive span-vs-1e-5 comparison would give",
    f_int > 3.9e-6, f"{f_int:.2e} vs the naive 3.9e-6 -- the naive figure was an OVERCLAIM")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
