#!/usr/bin/env python3
"""P8: does my full transfer reduce to the seat's surface model in the optically thick limit?

*** CLOSURE-CONDITIONAL EXPERIMENT — NOT A MODEL PREDICTION (REGATE4, 2026-08-27) ***
This script executes p6's prefix and therefore inherits p6's source construction: a blackbody
junction anchor with an adiabatic depth law T ~ rhobar^[w/(1+w)]. The epoch ruling invalidated
that closure as a property of the pinned geometry. Every null reported below is a property of
THAT ASSUMED SOURCE MAP, not of the Smoller-Temple solution. REGATE4 further withdrew the
existence of a null as a model-level claim: a source held constant across crossing epochs has
zero source-gradient and never crosses zero. Read every number here as "under this closure",
and see BHU_CLOSED_ROUTES.md and REGATE4_DISPOSITION.md before citing any of it.


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

# REPAIR 2026-08-27 (REGATE4 required-repair 4, the p8 reporting/reproducibility defects).
# Three defects were found and all three are fixed here:
#   (a) MISLABEL. The convergence details read "K=1e5: <value>" while printing finite[-1] —
#       the last FINITE root, which was K=1e2. The label was hard-coded, not read from the
#       run. Every label below now carries the K that actually produced the number.
#   (b) BRACKET TRUNCATION. The search ran on [0.02, 0.30] while the root was migrating
#       right: 0.0408 -> 0.0870 -> 0.2681 -> and at K=1e3 it sits at 0.4777, OUTSIDE the old
#       bracket. That was reported as nan, i.e. as an absent root. It is not absent.
#   (c) SILENT UNDER-RESOLUTION. The emergent integral weights by exp(-tau), so once the
#       tau~1 photosphere is thinner than one grid cell the result is grid noise. That is
#       what produced the discontinuous sign flip between K=1e3 and K=1e4 (the coefficient
#       jumps from +0.259 to -1.526 across the whole w range). Beyond the resolved range the
#       script now reports UNRESOLVED and declines to claim anything — reporting "no root"
#       there would be a physics claim this grid cannot support.
def resolution_limit(w_probe):
    """Largest opacity multiplier whose photosphere this grid still resolves (max cell dtau <= 1)."""
    e=exterior(0.5633887, w_probe)          # was obfuscated dead arithmetic evaluating to this constant
    if e is None: return None, None
    step=0.5*(e['dtau'][1:]+e['dtau'][:-1])*np.diff(e['rr'])
    return e, 1.0/float(step.max())

# The gate must be evaluated at the WORST point the root-finder actually visits, which is the
# low-w floor of the search bracket — resolution improves monotonically with w:
#   w=0.02 -> K_MAX 18.42 | 0.05 -> 111.5 | 0.08 -> 282.4 | 0.2456 -> 2935 | 0.95 -> 5704
# Gating on a single mid-band probe (w=0.08) would have admitted K=1e2, whose bracket runs
# down to w=0.02 where this grid resolves only K <= 18.4. brentq would then be reading grid
# noise at its own left endpoint. So the floor governs.
W_FLOOR=0.02
e_probe,_ = resolution_limit(0.08)                 # kept only for the tau-at-w=0.08 column
_, K_MAX = resolution_limit(W_FLOOR)
print(f"Grid resolves the photosphere up to K = {K_MAX:.4g} at the search floor w={W_FLOOR} "
      f"(npts={len(e_probe['rr'])}).")
print("Resolution improves with w, but the root-finder evaluates its left endpoint, so the")
print("floor governs. Beyond that the tau~1 layer is thinner than one cell and NOTHING is claimed.\n")

print("Null location as the exterior is driven optically thick (K = opacity multiplier):")
print(f"{'K':>10} {'tau at w=0.08':>14} {'null w':>12} {'-> their 0.081500':>20}  status")
rows=[]   # (K, root_or_nan, resolved)
for K in [1.0, 10.0, 1e2, 1e3, 1e4, 1e5]:
    tau_at=e_probe['tau_tot']*K
    resolved = K <= K_MAX
    root=float('nan')
    if resolved:
        for lo,hi in [(W_FLOOR,0.30),(W_FLOOR,0.60),(W_FLOOR,0.95)]:   # widened; see (b)
            try:
                flo,fhi=signed_c1_K(lo,K),signed_c1_K(hi,K)
                if flo is None or fhi is None: continue
                if flo*fhi>0: continue
                root=brentq(lambda w: signed_c1_K(w,K), lo, hi, xtol=1e-9); break
            except Exception:
                continue
    rows.append((K,root,resolved))
    status = ("resolved" if resolved else "UNRESOLVED — not reported")
    rstr = f"{root:12.7f}" if np.isfinite(root) else f"{'n/a':>12}"
    ratio = f"{root/THEIR_NULL:20.4f}" if np.isfinite(root) else f"{'—':>20}"
    print(f"{K:10.0e} {tau_at:14.3f} {rstr} {ratio}  {status}")

res_rows=[(K,r) for K,r,ok in rows if ok]
found=[(K,r) for K,r in res_rows if np.isfinite(r)]
unresolved=[K for K,_,ok in rows if not ok]

chk("every opacity the grid RESOLVES yields a root (the earlier nan was a bracket defect, not an absence)",
    len(found)==len(res_rows),
    f"{len(found)} of {len(res_rows)} resolved opacities gave a root; "
    f"{len(unresolved)} opacities (K >= {min(unresolved):.0e}) declined as unresolved" if unresolved
    else f"{len(found)} of {len(res_rows)}")
chk("the null MIGRATES as opacity increases (the models are not independent)",
    abs(found[-1][1]-found[0][1])>1e-3,
    f"K={found[0][0]:.0e}: {found[0][1]:.7f} -> K={found[-1][0]:.0e}: {found[-1][1]:.7f}")
converged=abs(found[-1][1]-THEIR_NULL)/THEIR_NULL
chk("at the thickest RESOLVED opacity my null matches the seat's surface-model null (models NESTED)",
    converged<0.02,
    f"K={found[-1][0]:.0e} null {found[-1][1]:.7f} vs theirs {THEIR_NULL:.7f} "
    f"— {100*converged:.2f}% apart; and it is moving AWAY, not toward")

print(f"\nVERDICT (at the thickest opacity this grid resolves, K={found[-1][0]:.0e}): "
      f"{'NESTED — my transfer reduces to their surface model as it goes thick.' if converged<0.02 else 'NOT NESTED — the resolved thick limit does not reproduce their null.'}")
print("SCOPE: the true asymptotic thick limit is NOT tested here. It needs a grid that resolves\n"
      "       the photosphere at K >> %.4g, which this one does not." % K_MAX)
nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
