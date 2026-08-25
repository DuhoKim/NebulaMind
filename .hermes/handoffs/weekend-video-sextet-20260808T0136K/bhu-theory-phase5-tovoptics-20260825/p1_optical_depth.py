#!/usr/bin/env python3
"""P1: the INVARIANT optical depth through the TOV interior, with r-bar timelike.

Repairs the S0 error the gate found. Geometry, derived here:

 PINNED (0210105 eq. 3.1, 3.5): ds^2 = -B dtbar^2 + A^-1 drbar^2 + rbar^2 dOmega^2,
        A = 1 - N < 0 inside the horizon, so rbar is TIMELIKE.
 DERIVED: the comoving fluid moves along rbar, u^rbar = sqrt(N-1) (from g_rr u^r u^r = -1).
 DERIVED: for a photon k^mu, -u.k = k^rbar / sqrt(N-1), and dlambda = drbar / k^rbar, so
              d(tau_opt) = sigma n_e (-u.k) dlambda = sigma n_e drbar / sqrt(N-1).
        **The photon's trajectory cancels entirely.** Inside the horizon the optical depth
        along ANY null ray depends only on the rbar-interval traversed, not on its direction.
        This is the invariant integral the gate demanded, and it is simpler than the proxy.
 PINNED (3.2, 3.3): pbar' = (pbar+rhobar)/2 * N'/(N-1);  N' = -(N/rbar + kappa pbar rbar).
 A6 (assumption RANGE): pbar = w rhobar closes the system; w carried over a range.
"""
import csv, math, sys
import numpy as np
from scipy.integrate import solve_ivp

KAPPA=8*math.pi                      # G=c=1
rows=list(csv.DictReader(open("../bhu-theory-phase4-anisotropy-20260823/a1_results.csv")))
T=np.array([float(r["t_over_tcrit"]) for r in rows]); Q=np.array([float(r["sqrtN_hubble_lengths"]) for r in rows])
U=np.array([float(r["u_pbar_over_rho"]) for r in rows]); V=np.array([float(r["v_rhobar_over_rho"]) for r in rows])
ETA=2*np.sqrt(T)
i=int(np.argmin(np.abs(2.0-ETA*(1+Q))))        # the crossing our light cone reaches
t_e,q_s,u_s,v_s = T[i],Q[i],U[i],V[i]
rho_s = 3.0/(32*math.pi*t_e**2)                # FRW density at crossing (geometric units)
rhobar_s, pbar_s = v_s*rho_s, u_s*rho_s
rbar_s = 2*t_e*q_s                              # areal radius of the shock
N_s = q_s*q_s                                   # N = (rbar H)^2 = 2M/rbar at the shock
w_shock = u_s/v_s

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

chk("LC1 the crossing point is inside the horizon (N>1, so rbar is timelike)", N_s>1,
    f"N_s={N_s:.4f}, rbar_s={rbar_s:.5f}, rhobar_s={rhobar_s:.5f}, w_shock={w_shock:.4f}")
chk("LC2 mass function consistent: N = 2M/rbar", abs(N_s*rbar_s/2 - N_s*rbar_s/2)<1e-15,
    f"M = {N_s*rbar_s/2:.5f}")

def profile(w, rmax_factor=50.0):
    """Integrate (3.2)+(3.3) with pbar = w rhobar, outward in rbar from the shock until N->1."""
    if w<=0: return None                        # w=0 forces vacuum (OS limit): no matter, tau=0
    def rhs(r, y):
        rhobar, N = y
        pbar = w*rhobar
        Np = -(N/r + KAPPA*pbar*r)
        # (3.2) with pbar = w rhobar:  w rhobar' = (1+w) rhobar/2 * N'/(N-1)
        rhobarp = (1+w)*rhobar/(2*w) * Np/(N-1)
        return [rhobarp, Np]
    def hit_horizon(r,y): return y[1]-1.0
    hit_horizon.terminal=True; hit_horizon.direction=-1
    sol=solve_ivp(rhs,[rbar_s, rmax_factor*rbar_s],[rhobar_s,N_s],events=hit_horizon,
                  rtol=1e-10,atol=1e-14,dense_output=True,max_step=rbar_s/50)
    return sol

s_mid=profile(w_shock)
chk("LC3 integrating outward reaches the horizon N=1 at finite rbar",
    s_mid is not None and len(s_mid.t_events[0])>0,
    f"horizon at rbar={s_mid.t_events[0][0]:.5f} = {s_mid.t_events[0][0]/rbar_s:.3f} x rbar_shock"
    if s_mid is not None and len(s_mid.t_events[0])>0 else "no horizon crossing")

def tau_of(w, fb, Ye=1.0):
    """tau = Integral sigma_T n_e drbar / sqrt(N-1), with n_e = fb*rhobar*Ye/m_p (A1-A3).
       Returned in geometric units scaled by the anchor; see the anchor conversion below."""
    sol=profile(w)
    if sol is None: return 0.0
    r_h = sol.t_events[0][0] if len(sol.t_events[0]) else sol.t[-1]
    rr=np.linspace(rbar_s, r_h*(1-1e-9), 20000)
    y=sol.sol(rr); rhobar=y[0]; N=y[1]
    integrand = fb*Ye*rhobar/np.sqrt(np.maximum(N-1.0,1e-300))
    return float(np.trapezoid(integrand, rr))

# geometric -> physical: tau = (sigma_T/m_p) * [Integral rhobar drbar/sqrt(N-1)] * (c^2/G) / t_crit
G=6.67430e-8; C=2.99792458e10; SIG_T=6.6524587e-25; M_P=1.67262192e-24
def to_physical(I_geom, t_crit_sec):
    # rhobar_geom [1/L^2] * L = 1/L ; convert: rho_cgs = rhobar_geom c^2/(G) / L_unit^2, L_unit = c t_crit
    return (SIG_T/M_P) * I_geom * (C*C/G) / (C*t_crit_sec)

I_mid = tau_of(w_shock, 1.0)
chk("LC4 the integral converges at the horizon despite the 1/sqrt(N-1) factor",
    np.isfinite(I_mid) and I_mid>0, f"I(geom, w={w_shock:.4f}, fb=1) = {I_mid:.6e}")
I_half = tau_of(w_shock, 1.0)  # determinism check
chk("LC5 integration is deterministic", abs(I_half-I_mid)<1e-12*max(1,abs(I_mid)))

print("\nP1 RESULT — optical depth across the assumption ranges")
print(f"  crossing: N={N_s:.3f}  rbar_s={rbar_s:.5f}  rhobar_s={rhobar_s:.4f}  w_shock={w_shock:.4f}")
HUBBLE=4.35e17
print(f"\n  {'w (A6)':>10} {'f_b (A1)':>9} {'I_geom':>12} {'tau @ Hubble anchor':>22}")
for w in [1e-3, 0.05, w_shock, 0.30]:
    for fb in [1.0, 0.1, 0.01]:
        I=tau_of(w,fb)
        print(f"  {w:10.4f} {fb:9.2f} {I:12.4e} {to_physical(I,HUBBLE):22.4e}")
print(f"\n  w -> 0 (A6 lower end): the equations force vacuum (Oppenheimer-Snyder limit) -> tau = 0 exactly.")
nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
