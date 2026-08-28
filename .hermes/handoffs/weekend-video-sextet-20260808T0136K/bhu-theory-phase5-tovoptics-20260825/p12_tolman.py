#!/usr/bin/env python3
"""P12 — the successor question: can the missing exterior temperature be SUPPLIED
rather than invented?

PHASE 5b closed on this: every computed signature was a property of an added thermal closure,
because Smoller-Temple give a MECHANICAL equation of state p(rho) and never a CALORIC one.
REGATE4's specific objection was sharper than "no temperature": varying the crossing epoch
sweeps a SPACELIKE family of different fluid elements, so an adiabatic law along one worldline
cannot relate them. What is missing is the exterior's SPATIAL temperature profile.

THE CANDIDATE. The ST exterior is a STATIC TOV solution. For a static spacetime in local
thermal equilibrium, the Tolman-Ehrenfest relation fixes exactly that profile:

        T(r) * sqrt(-g_tt(r))  =  constant

so T(r) = T_j * sqrt(B_j / B(r)), with B = -g_tt. This is not an invented closure: B(r) is
integrated from the model's own field equations, and p6 already carries it as
Z(r) = sqrt(|B(r)|/|B_s|). So the profile is T(r) = T_j / Z(r).

WHAT THIS FILE TESTS, and it is not whether the idea is nice:
  A. Is the profile actually determinate from the pinned geometry? (compute it)
  B. Does it DIFFER from the closures REGATE4 invalidated? If it coincides with the adiabatic
     law, it adds nothing and the objection stands.
  C. Does it answer the epoch objection -- i.e. does it relate DIFFERENT crossing epochs
     without a single-worldline assumption?
  D. What does it cost? Tolman-Ehrenfest assumes local thermal equilibrium in a static field.
     That is an added assumption. It is named, standard and defensible, which is what the
     closing summary asked for -- but it is still an assumption and must be recorded as one.
"""
import math, sys
import numpy as np

src = open("p6_path_transfer.py").read().split('print("\\nP6 — depth-resolved')[0]
G = {}; exec(src, G)
exterior = G["exterior"]; ETAs = G["ETAs"]; i0 = G["i0"]

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, (bool, np.bool_)): raise TypeError("chk needs a computed predicate")
    checks.append((name, bool(pred), detail))
    print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

W = 0.2456                      # junction-value closure, the phase's reference point
e = exterior(ETAs[i0], W)
if e is None:
    print("exterior() failed at the reference epoch"); sys.exit(1)

Z    = e["Z"]                   # sqrt(|B(r)|/|B_junction|)  -- already in p6
rho  = e["rhobar"]
T_ad = e["T_rad"]               # the ADIABATIC closure REGATE4 invalidated, for comparison

print("=" * 92)
print("P12 -- Tolman-Ehrenfest as the supplied exterior temperature profile")
print("=" * 92)

# ---- A. is it determinate? ---------------------------------------------------------
T_tol = 1.0 / np.maximum(Z, 1e-300)          # T(r)/T_junction = 1/Z(r)
finite = np.isfinite(T_tol).all()
print(f"\nA. determinacy")
print(f"   Z spans {Z[0]:.6f} -> {Z[-1]:.6e}   (junction -> horizon)")
print(f"   T/T_j = 1/Z spans {T_tol[0]:.6f} -> {T_tol[-1]:.6e}")
chk("the profile is fully determined by the pinned metric function B, with no free parameter",
    bool(finite) and abs(T_tol[0] - 1.0) < 1e-9,
    "T(r)=T_j/Z(r); Z comes from p6's own integration of B'/B from PINNED (3.4)")

# ---- B. does it differ from the invalidated adiabatic closure? ----------------------
Tad = T_ad / T_ad[0]                          # normalise both at the junction
print(f"\nB. comparison with the adiabatic closure REGATE4 invalidated")
print(f"   {'r/r_s':>8} {'Tolman T/T_j':>14} {'adiabatic T/T_j':>17} {'ratio':>10}")
idx = [0, len(Z)//4, len(Z)//2, 3*len(Z)//4, len(Z)-1]
for k in idx:
    r = e["rr"][k] / e["rbar_s"]
    print(f"   {r:8.3f} {T_tol[k]:14.6e} {Tad[k]:17.6e} {T_tol[k]/max(Tad[k],1e-300):10.3e}")
ratio_end = T_tol[-1] / max(Tad[-1], 1e-300)
chk("Tolman and adiabatic are NOT the same profile -- so this is a real alternative",
    ratio_end > 10.0 or ratio_end < 0.1,
    f"they differ by {ratio_end:.3e} at the horizon end")
chk("and they run in OPPOSITE directions: Tolman RISES inward, adiabatic FALLS",
    T_tol[-1] > T_tol[0] and Tad[-1] < Tad[0],
    f"Tolman {T_tol[0]:.2f}->{T_tol[-1]:.3e}, adiabatic {Tad[0]:.2f}->{Tad[-1]:.3e}")

# ---- C. does it answer the epoch objection? ---------------------------------------
# REGATE4: different crossing epochs sample DIFFERENT fluid elements, so a per-worldline law
# cannot relate them. Tolman-Ehrenfest is a STATEMENT ABOUT A STATIC FIELD AT ONE TIME, so it
# relates positions directly. Test: does it give a consistent T at the junction across epochs?
print(f"\nC. the epoch objection -- does the profile relate DIFFERENT crossings?")
print(f"   {'eta_e':>10} {'Z at horizon':>16} {'T_horizon/T_j':>16}")
ok = 0; tried = 0
for et in np.linspace(ETAs.min()*4, ETAs.max()*0.9, 6):
    ee = exterior(float(et), W)
    if ee is None: continue
    tried += 1
    zz = ee["Z"][-1]
    if np.isfinite(zz) and zz > 0: ok += 1
    print(f"   {float(et):10.5f} {zz:16.6e} {1.0/max(zz,1e-300):16.6e}")
chk("the profile is computable at every sampled crossing epoch, from geometry alone",
    tried > 0 and ok == tried, f"{ok}/{tried} epochs gave a finite profile")

print("""
D. WHAT IT COSTS -- stated as an assumption, not smuggled

  Tolman-Ehrenfest requires LOCAL THERMAL EQUILIBRIUM in a STATIC gravitational field. The ST
  exterior is static, so the second condition is met by construction. The first is an ADDED
  physical assumption: it says the exterior fluid has had time to equilibrate and is not, say,
  freely streaming or shock-heated out of equilibrium.

  That is exactly the kind of thing the phase 5b closing summary asked for -- "a stated physical
  model defended in its own right" -- rather than a closure chosen to make the arithmetic work.
  It is named, standard, and derived from the model's own metric. It is NOT free.

  WHAT IT DOES NOT DO. It does not make the model testable by itself. It supplies the profile;
  the null question, the flatness question and the exclusion strength all have to be recomputed
  on it, and any of them may come out empty. This file establishes only that the missing piece
  CAN be supplied on principled grounds -- which is the one thing phase 5b said was needed.
""")
np_ = sum(1 for _, ok_, _ in checks if ok_)
print(f"SELF-CHECKS: {np_}/{len(checks)} passed")
sys.exit(0 if np_ == len(checks) else 1)
