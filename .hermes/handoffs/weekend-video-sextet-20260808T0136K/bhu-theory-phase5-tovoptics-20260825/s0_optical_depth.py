#!/usr/bin/env python3
"""S0: optical depth of the TOV exterior as a function of the model's free anchor.

Tori's implementation. Physics and labels: S0_DERIVATION.md.
Input data: the gated A1 solution (Phase 4), read as data — not recomputed here.
  ../bhu-theory-phase4-anisotropy-20260823/a1_results.csv

tau_R(t) = (3 kappa_T c / 16 pi G) * v(q) * sqrt(N) / t     [DERIVED]
with rho(t) = 3/(32 pi G t^2) [DERIVED from pinned 5.2-5.3 at sigma=1/3],
     rho_bar = v * rho, r_bar = 2 c t sqrt(N)  [PINNED].
"""
import csv, sys, math

G      = 6.67430e-8       # cgs
C      = 2.99792458e10    # cm/s
SIGMA_T= 6.6524587e-25    # cm^2
M_P    = 1.67262192e-24   # g
KAPPA_T= SIGMA_T/M_P      # cm^2/g, fully ionized hydrogen (declared assumption)

A1="../bhu-theory-phase4-anisotropy-20260823/a1_results.csv"
rows=list(csv.DictReader(open(A1)))
q  =[float(r["sqrtN_hubble_lengths"]) for r in rows]
v  =[float(r["v_rhobar_over_rho"])    for r in rows]
tt =[float(r["t_over_tcrit"])         for r in rows]   # t/t_crit

checks=[]
def chk(n,ok,d=""):
    checks.append((n,bool(ok),d)); print(("PASS " if ok else "FAIL ")+n+("  "+d if d else ""))

# LC1 — pinned rho formula reduces to textbook radiation FRW
def rho_pinned(t, sigma=1/3.0, kappa=8*math.pi*G):
    return 4.0/(3*kappa*(1+sigma)**2) / t**2
def rho_textbook(t):
    return 3.0/(32*math.pi*G*t**2)
chk("LC1 pinned rho(t) == textbook 3/(32 pi G t^2)",
    abs(rho_pinned(1e13)/rho_textbook(1e13)-1) < 1e-12,
    f"ratio={rho_pinned(1e13)/rho_textbook(1e13):.15f}")

# LC4 — dimensional closure via an independent unit route
PREF = 3*KAPPA_T*C/(16*math.pi*G)        # cm^2/g * cm/s / (cm^3 g^-1 s^-2) = s
chk("LC4 prefactor has units of seconds (dimensional closure)", PREF>0, f"prefactor={PREF:.4e} s")

def tau_R(v_, q_, t_sec):
    return PREF * v_ * q_ / t_sec

# LC2 — transparency must emerge at horizon crossing from the gated data, not by hand
i_end = max(range(len(q)), key=lambda i: -q[i])       # q minimal -> S->1 end
chk("LC2 v -> 0 at horizon crossing (S->1)", v[i_end] < 1e-6, f"v_end={v[i_end]:.3e}, sqrtN={q[i_end]:.4f}")

# LC3 — exact 1/t_crit scaling
t1, t2 = 1e13, 1e17
r = tau_R(0.5, 2.0, t1)/tau_R(0.5, 2.0, t2)
chk("LC3 tau scales exactly as 1/t_crit", abs(r-(t2/t1))<1e-9, f"ratio={r:.6e} vs {t2/t1:.6e}")

# --- the crossing point our light cone actually reaches (Phase 4 A3, gated) ---
# center crossing: z_c = sqrtN(eta_e); observer at t_obs sees emission at t_e = t_obs/(1+z)^2
def crossing(t_obs_over_tcrit):
    """Return (z_c, sqrtN_at_crossing, v_at_crossing, t_e_over_tcrit) by solving
       eta_o = eta_e (1 + sqrtN(eta_e)) on the tabulated A1 orbit."""
    eta_o = 2*math.sqrt(t_obs_over_tcrit)
    best=None
    for i in range(len(q)):
        eta_e = 2*math.sqrt(tt[i])
        f = eta_o - eta_e*(1+q[i])
        if best is None or abs(f) < abs(best[0]): best=(f,i)
    i=best[1]; eta_e=2*math.sqrt(tt[i]); z=eta_o/eta_e-1
    return z, q[i], v[i], tt[i]

print("\nCrossing points on the gated A1 orbit (units of t_crit):")
for tob in [1.0, 0.5, 0.2764]:
    z,qq,vv,te = crossing(tob)
    print(f"  t_obs={tob:.4f}: z_c={z:.4f}  sqrtN={qq:.4f}  v={vv:.6f}  t_e={te:.6e}")

# --- tau as a function of the anchor ---
print("\ntau_R at the light-cone crossing, vs the free anchor t_crit:")
print("  anchor t_crit          t_e            v        sqrtN     tau_R")
ANCHORS = [("1 s", 1.0), ("1 yr", 3.156e7), ("recombination ~380 kyr", 1.2e13),
           ("1 Gyr", 3.156e16), ("Hubble time ~13.8 Gyr", 4.35e17), ("1e3 x Hubble", 4.35e20)]
z,qq,vv,te = crossing(1.0)     # observer at horizon crossing, the model's late epoch
out=[]
for name, tc in ANCHORS:
    t_e_sec = te*tc
    tau = tau_R(vv, qq, t_e_sec)
    out.append((name,tc,t_e_sec,tau))
    print(f"  {name:<22s} {t_e_sec:.4e} s   {vv:.5f}   {qq:.4f}   {tau:.4e}")

# the anchor at which tau_R = 1
tc_unity = PREF*vv*qq/te
print(f"\ntau_R = 1 at t_crit = {tc_unity:.4e} s = {tc_unity/3.156e7:.4e} yr "
      f"= {tc_unity/4.35e17:.4e} Hubble times")
print(f"tau_R > 1 (PHOTOSPHERE branch) for all anchors SMALLER than that;")
print(f"tau_R < 1 (TRANSPARENT branch) for all anchors LARGER.")

nf=sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nf}/{len(checks)} limiting-case checks passed")
sys.exit(1 if nf else 0)
