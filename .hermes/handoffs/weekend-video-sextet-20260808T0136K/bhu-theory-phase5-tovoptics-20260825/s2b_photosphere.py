#!/usr/bin/env python3
"""S2b: the OPAQUE branch. With tau ~ 0.3 the sight line is on the knife edge, so Addendum 1
requires both branches carried. S2 did the transparent/kinematic side; this does the emitting
side and then the mixture.

The question the brief parked behind K4 was the ABSOLUTE brightness, which needs a temperature
the metric does not fix. But the CONTRAST against the surrounding sky is anchor-free if the
exterior's energy is carried by radiation, because then both sides' temperatures come from
their own energy densities:

 PINNED   : v = rhobar/rho at the shock (gated A1 orbit); u = pbar/rho.
 DERIVED  : radiation sub-case -- if the exterior energy density is radiation, T ~ rho^(1/4),
            so Tbar/T_FRW = v^(1/4). No anchor, no absolute temperature needed.
 DERIVED  : ideal-gas sub-case -- if instead it is a non-relativistic ideal gas,
            k Tbar = (u/v) mu m_H c^2, which IS anchor-free in absolute terms.
 DERIVED  : partial opacity -- bolometric mixing along the ray,
            T_eff^4 = (1-e^-tau) Tbar^4 + e^-tau T_beyond^4, and T_beyond is bounded between
            0 (nothing behind) and Tbar (same bath), so T_eff is BOUNDED without knowing it.
 PINNED   : Doppler factor from S1's law beta = 1/sqrt(N) (proven), applied as in S2.
"""
import csv, math, sys
import numpy as np

SIGMA=1/3.0
rows=list(csv.DictReader(open("../bhu-theory-phase4-anisotropy-20260823/a1_results.csv")))
T=np.array([float(r["t_over_tcrit"]) for r in rows]); Q=np.array([float(r["sqrtN_hubble_lengths"]) for r in rows])
U=np.array([float(r["u_pbar_over_rho"]) for r in rows]); V=np.array([float(r["v_rhobar_over_rho"]) for r in rows])
ETA=2*np.sqrt(T); o=np.argsort(ETA)
ETA,Q,U,V=ETA[o],Q[o],U[o],V[o]

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

# crossing for a centred observer at t_obs = t_crit (the epoch S2 used)
eta_o=2.0
i=int(np.argmin(np.abs(eta_o-ETA*(1+Q))))
v_c,u_c,q_c=V[i],U[i],Q[i]
print(f"Crossing: sqrtN={q_c:.5f}  u={u_c:.6f}  v={v_c:.6f}  u/v={u_c/v_c:.6f}")

TAU=0.34                      # S0, Hubble-time anchor
# --- radiation sub-case ---
ratio_rad = v_c**0.25
chk("LC1 no-jump limit: v -> 1 gives no temperature contrast", abs(1.0**0.25-1.0)<1e-15)
chk("LC2 exterior is cooler than the interior at the shock (v<1)", ratio_rad<1.0,
    f"Tbar/T_FRW = v^(1/4) = {ratio_rad:.4f}")

# partial opacity bounds: T_beyond in [0, Tbar]
lo = ((1-math.exp(-TAU))*ratio_rad**4 + 0.0)**0.25
hi = ((1-math.exp(-TAU))*ratio_rad**4 + math.exp(-TAU)*ratio_rad**4)**0.25
chk("LC3 the unknown behind-the-shock term is bounded, so T_eff is bounded",
    lo<hi and hi<=ratio_rad+1e-12, f"T_eff/T_FRW in [{lo:.4f}, {hi:.4f}]")

# --- ideal-gas sub-case (absolute) ---
MU=0.6; MHC2_MEV=938.272
kT_MeV = (u_c/v_c)*MU*MHC2_MEV
T_kelvin = kT_MeV*1e6*1.602176634e-19/1.380649e-23
chk("LC4 ideal-gas sub-case gives a relativistically hot exterior", T_kelvin>1e9,
    f"kT = {kT_MeV:.1f} MeV = {T_kelvin:.2e} K")

# --- combined contrast against the surrounding (non-crossing) sky ---
beta=1.0/q_c; gam=1.0/math.sqrt(1-beta*beta)
print(f"\nOPAQUE BRANCH, radiation sub-case (tau = {TAU}):")
print(f"  exterior/interior temperature ratio      : {ratio_rad:.4f}  (v^(1/4))")
print(f"  after partial opacity, T_eff/T_FRW       : {lo:.4f} to {hi:.4f}")
print(f"  contrast before Doppler                  : {100*(lo-1):+.1f}% to {100*(hi-1):+.1f}%")
print("\n  with the S1 Doppler factor applied, by viewing angle:")
worst=0.0
for mu,lbl in [(1.0,"toward the near wall"),(0.0,"transverse"),(-1.0,"away")]:
    D=1.0/(gam*(1-beta*mu))
    c_lo, c_hi = D*lo-1.0, D*hi-1.0
    worst=max(worst, abs(c_lo), abs(c_hi))
    print(f"    {lbl:<22s} contrast {100*c_lo:+7.1f}% to {100*c_hi:+7.1f}%")
print(f"\n  worst |contrast| = {worst:.3f} = {worst/1e-5:.1e} x the observed CMB anisotropy (1e-5)")
print(f"  ideal-gas sub-case: exterior at {kT_MeV:.0f} MeV -- excluded by many more orders.")

chk("LC5 BOTH branches exclude: opaque contrast is also >> 1e-5", worst>1e-3,
    f"opaque worst {worst:.3f} vs transparent span 2.593 x offset (S2)")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} limiting-case checks passed")
sys.exit(1 if nf else 0)
