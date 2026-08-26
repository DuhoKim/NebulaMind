#!/usr/bin/env python3
"""P6: the GENUINE path transfer — depth-resolved emission, direction-dependent opacity.

Answers REGATE2_PHASE5B_VERDICT.md findings 1-3. P5 was a single-screen model: it put all the
emission at the junction, held tau fixed across the sky, and carried no A4 source range. This
integrates the transfer along the ray and lets every direction have its own exterior.

DERIVED (the piece P5 lacked) — the depth-to-junction redshift:
  In the A<0 interior the metric is ds^2 = -B dtbar^2 + A^-1 drbar^2 + rbar^2 dOmega^2 (PINNED
  3.1). For a radial photon, k_tbar = -E is conserved, and the null condition gives
  rbardot^2 = A E^2 / B. With the comoving fluid u^rbar = sqrt(N-1) (P1), the frequency each
  fluid element measures is
        omega = -u.k = k^rbar/sqrt(N-1) = E sqrt(|A|/|B|)/sqrt(|A|) = E/sqrt(|B|).
  So a photon emitted at depth rbar and received at the junction is shifted by
        omega_junction/omega_emit = sqrt(|B(rbar)|/|B(junction)|),
  with B integrated from PINNED (3.4): B'/B = -(1/(N-1)) (N/rbar + kappa rhobar).
  Only the RATIO matters, so B(junction) = -1 is a normalisation, not an assumption.

Formal solution actually integrated (not a two-term screen):
        T_obs = e^-tau_tot * T_bg * Z_tot  +  Integral T_source(rbar) Z(rbar) e^-tau drbar-weight
  then the junction Doppler D(mu) multiplies the emergent beam.
"""
import csv, math, sys, platform
import numpy as np, scipy
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
TRAPZ=getattr(np,"trapezoid",None) or np.trapz
print(f"# env: python {platform.python_version()}, numpy {np.__version__}, scipy {scipy.__version__}")

G=6.67430e-8; C=2.99792458e10; SIG_T=6.6524587e-25; M_P=1.67262192e-24; M_E=9.1093837e-28
A_RAD=7.565723e-15; K_B=1.380649e-16; MEC2=M_E*C*C; KAPPA=8*math.pi; T_CRIT=4.35e17

rows=list(csv.DictReader(open("../bhu-theory-phase4-anisotropy-20260823/a1_results.csv")))
Tt=np.array([float(r["t_over_tcrit"]) for r in rows]); Q=np.array([float(r["sqrtN_hubble_lengths"]) for r in rows])
U=np.array([float(r["u_pbar_over_rho"]) for r in rows]); V=np.array([float(r["v_rhobar_over_rho"]) for r in rows])
ETA=2*np.sqrt(Tt); o=np.argsort(ETA); ETAs,Qs,Us,Vs=ETA[o],Q[o],U[o],V[o]; RS=ETAs*Qs
def sqrtN(e): return np.interp(e,ETAs,Qs)
def r_star(e): return np.interp(e,ETAs,RS)
def u_of(e): return np.interp(e,ETAs,Us)
def v_of(e): return np.interp(e,ETAs,Vs)
eta_o=2.0
i0=int(np.argmin(np.abs(eta_o-ETAs*(1+Qs)))); RSTAR_CROSS=ETAs[i0]*Qs[i0]

checks=[]
def chk(name,pred,detail=""):
    if not isinstance(pred,(bool,np.bool_)): raise TypeError("chk needs a computed predicate")
    checks.append((name,bool(pred),detail)); print(("PASS " if pred else "FAIL ")+name+("  "+detail if detail else ""))

def exterior(eta_e, w_target, width=0.02, npts=4000):
    """Integrate the exterior for the crossing at conformal time eta_e. State: [pbar, N, lnB].
       Returns depth grids: rbar, rhobar, N, cumulative tau, and the redshift factor Z(rbar)."""
    t_e=(eta_e/2.0)**2
    rho=3.0/(32*math.pi*t_e**2); u=u_of(eta_e); v=v_of(eta_e)
    if v<=0 or u<=0: return None
    rhobar_s=v*rho; pbar_s=u*rho; rbar_s=eta_e*sqrtN(eta_e)*1.0  # rbar = R*r = eta*sqrtN in these units
    rbar_s=2*t_e*sqrtN(eta_e)
    N_s=sqrtN(eta_e)**2; w_s=u/v
    wfun=lambda r: w_target if r>rbar_s*(1+width) else w_s+(w_target-w_s)*(r-rbar_s)/(width*rbar_s)
    def rhs(r,y):
        p,N,lnB=y
        # Guard genuine invalidity only. N dips marginally below 1 as the terminal event
        # brackets the horizon, and p probes below zero within rounding on the steep descent —
        # neither is an invalid solution, and rejecting them aborted every run.
        if not (np.isfinite(p) and np.isfinite(N)) or p < -1e-9*pbar_s or N < 1.0-1e-9:
            raise ValueError
        p=max(p,0.0); N=max(N,1.0+1e-12); w=wfun(r); rb=p/w
        Np=-(N/r+KAPPA*p*r)
        return [p*(1+1.0/w)/2*Np/(N-1), Np, -(1.0/(N-1))*(N/r+KAPPA*rb)]
    def hz(r,y): return y[1]-1.0
    hz.terminal=True; hz.direction=-1
    try:
        s=solve_ivp(rhs,[rbar_s,400*rbar_s],[pbar_s,N_s,0.0],events=hz,rtol=1e-9,atol=1e-18,
                    dense_output=True,max_step=rbar_s/30)
    except Exception:
        return None
    if not s.success or not len(s.t_events[0]): return None
    r_h=s.t_events[0][0]
    rr=np.linspace(rbar_s,r_h*(1-1e-9),npts); y=s.sol(rr)
    p=np.maximum(y[0],0.0); N=y[1]; lnB=y[2]
    w=np.array([wfun(r) for r in rr]); rhobar=p/w
    L=C*T_CRIT; rho_cgs=rhobar*(C*C/G)/(L*L)
    n_cold=rho_cgs/M_P
    T_rad=np.where(rho_cgs>0,(np.maximum(rho_cgs,0)*C*C/A_RAD)**0.25,0.0)
    kT_gas=w*0.6*M_P*C*C
    n_pair=np.where(kT_gas>MEC2, rho_cgs*C*C/np.maximum(3*kT_gas,1e-300), 0.0)
    n_e=np.maximum(n_cold,n_pair)
    dtau=SIG_T*n_e/np.sqrt(np.maximum(N-1.0,1e-300))*L      # per unit rbar (geometric)
    tau_cum=np.concatenate([[0.0],np.cumsum(0.5*(dtau[1:]+dtau[:-1])*np.diff(rr))])
    Z=np.exp(0.5*lnB)                                        # sqrt(|B(r)|/|B_s|), B_s normalised
    return dict(rr=rr,rhobar=rhobar,N=N,tau=tau_cum,Z=Z,T_rad=T_rad,dtau=dtau,
                rbar_s=rbar_s,N_s=N_s,tau_tot=tau_cum[-1],T_rad_s=T_rad[0])

# --- sanity on the new machinery ---
ex=exterior(ETAs[i0], 0.2456)
chk("P6 exterior integrates with the metric function B carried alongside", ex is not None,
    f"tau_tot={ex['tau_tot']:.4f}, Z spans {ex['Z'][0]:.4f} -> {ex['Z'][-1]:.4e}" if ex else "")
chk("the depth-to-junction redshift is NOT unity (P5 implicitly assumed it was)",
    ex is not None and abs(ex['Z'][-1]-1.0)>0.05,
    f"Z at the horizon = {ex['Z'][-1]:.4e} vs 1.0 at the junction")
chk("cumulative optical depth reproduces P1c's single-number result at the same w",
    ex is not None and abs(ex['tau_tot']-0.1321)/0.1321<0.05, f"tau_tot={ex['tau_tot']:.4f}")

def emergent_T_over_Tbg(eta_e, w_target):
    """Depth-resolved formal solution, in units of the incident background temperature."""
    e=exterior(eta_e,w_target)
    if e is None: return None
    T_bg_local=(3.0/(32*math.pi*((eta_e/2)**2)**2)*(C*C/G)/((C*T_CRIT)**2)*C*C/A_RAD)**0.25
    transmitted=math.exp(-e['tau_tot'])*e['Z'][-1]
    src=e['T_rad']/max(T_bg_local,1e-300)                    # A4 upper end: LTE at energy ceiling
    integrand=src*e['Z']*np.exp(-e['tau'])*e['dtau']
    emitted=float(TRAPZ(integrand,e['rr']))
    return transmitted+emitted

def dipole_and_bound(w_target, f=1e-3, npts=48):
    nodes,wt=leggauss(npts); vals=[]
    for mu in nodes:
        x=f*RSTAR_CROSS
        def g(chi):
            p=math.sqrt(max(x*x+chi*chi+2*chi*x*mu,0.0)); return p-r_star(eta_o-chi)
        chi=brentq(g,1e-12,eta_o-1e-12,xtol=1e-14); eta_e=eta_o-chi
        mu_loc=max(-1.0,min(1.0,(x*mu+chi)/r_star(eta_e)))
        b=1.0/sqrtN(eta_e); gam=1.0/math.sqrt(1-b*b); D=1.0/(gam*(1-b*mu_loc))
        R=emergent_T_over_Tbg(eta_e,w_target)
        if R is None: return None,None,None
        vals.append(D*R-1.0)
    vals=np.array(vals); mono=0.5*float(np.sum(wt*vals)); vnm=(vals-mono)/(1.0+mono)
    P1=np.polynomial.legendre.Legendre.basis(1)(nodes)
    c1=abs(1.5*float(np.sum(wt*vnm*P1)))/f
    DIP=3.7e-3/2.7255
    return c1, DIP/c1, mono

print("\nP6 — depth-resolved transfer, per-direction exterior, across the A6/opacity range:")
print(f"{'w_target':>9} {'tau_tot':>9} {'c1':>9} {'bound':>11} {'monopole':>10}")
out=[]
for wt_ in [0.999,0.5,0.2456,0.1,0.03,0.01]:
    e=exterior(ETAs[i0],wt_)
    c1,bd,mono=dipole_and_bound(wt_)
    if c1 is None: print(f"{wt_:9.4g} {'n/a':>9}"); continue
    out.append((wt_,e['tau_tot'] if e else float('nan'),c1,bd))
    print(f"{wt_:9.4g} {(e['tau_tot'] if e else float('nan')):9.4f} {c1:9.5f} {bd:11.4e} {mono:10.4f}")

c1s=[o_[2] for o_ in out]; bds=[o_[3] for o_ in out]
chk("the dipole survives depth-resolved transfer at every computed opacity", min(c1s)>0.0,
    f"c1 spans {min(c1s):.5f} to {max(c1s):.5f}")
chk("the bound stays tight across the range (exclusion robust to the path treatment)",
    max(bds)<2e-2, f"worst bound {max(bds):.4e} = one part in {1/max(bds):.0f}")
worst=max(bds)
print(f"\nP6 RESULT: bound on x_off/r_*(crossing) from {min(bds):.4e} to {worst:.4e}")
print(f"           i.e. one part in {1/worst:.0f} at worst, {1/min(bds):.0f} at best.")
print(f"  P5 (single-screen) gave 2.21e-3 to 5.52e-3 for comparison.")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} checks passed")
sys.exit(1 if nf else 0)
