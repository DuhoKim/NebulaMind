#!/usr/bin/env python3
"""P11: how far does Claim 1 (nothing is transmitted from beyond the boundary) actually reach?

REGATE4 gave Claim 1 a CONDITIONAL PASS and required repair 3:
  "Narrow claim 1 to regular finite-boost sources unless a general emitter-velocity/source
   bound is derived."
and, in the adjudication:
  "The receipt does not justify the unrestricted phrase 'for a source that is not comoving.'
   In general g=(-k.u_rec)/(-k.u_emit) depends on the emitter four-velocity."

Rather than only softening the prose, this file DERIVES the sharp threshold and computes it
from the lane's own integrated exterior. Self-computing: every number in
P11_CLAIM1_SCOPE_RECEIPT.md is printed here.

WHAT IS BEING TESTED
The transmitted-background term p6 actually integrates is
    I_transmitted = exp(-tau_tot) * Z_h**4
where Z_h = Z at the horizon end of the column, and the 4th power is Liouville: I_nu/nu**3 is
invariant, so bolometric intensity carries g**4.

For a COMOVING emitter the lane already has g ~ sqrt(N-1) -> 0. For a NON-comoving emitter,
boost the local frame by beta (Lorentz factor gam) relative to comoving. The photon frequency
picks up a Doppler factor D = 1/(gam*(1 - beta*cos(theta))), maximised head-on at
    D_max(beta) = sqrt((1+beta)/(1-beta)) -> 2*gam   as beta -> 1.
So the transmitted weight becomes  (D_max * Z_h)**4  and the question is entirely whether
D_max can outrun Z_h -> 0.

THE DERIVED THRESHOLD
    weight -> 0   iff   gam**2 * (N-1) -> 0   i.e.   gam = o((N-1)**(-1/2)).
"Finite boost" is SUFFICIENT but not necessary; the sharp condition is the one above. The
causal statement (a true event horizon transmits nothing from its forbidden side) is separate
and unconditional — it is not a redshift argument and nothing here bears on it.
"""
import math, sys
import numpy as np

src = open("p6_path_transfer.py").read().split('print("\\nP6 — depth-resolved')[0]
G = {}; exec(src, G)
exterior = G["exterior"]; ETAs = G["ETAs"]; i0 = G["i0"]
ETA_C = ETAs[i0]; W_J = 0.2456                      # junction-value closure

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, (bool, np.bool_)):
        raise TypeError("chk needs a computed predicate")
    checks.append((name, bool(pred), detail))
    print(("PASS " if pred else "FAIL ") + name + ("  " + detail if detail else ""))

def D_max(gam):
    """Head-on Doppler factor for Lorentz factor gam (exact, not the 2*gam limit).

    Written as gam*(1+beta), NOT sqrt((1+beta)/(1-beta)). They are algebraically identical —
    (1+beta)/(1-beta) = (1+beta)^2/(1-beta^2) = gam^2 (1+beta)^2 — but the naive form divides
    by 1-beta, and above gam ~ 1e8 float64 rounds beta to exactly 1 and it raises
    ZeroDivisionError. The boost ladder in section 4 reaches gam ~ 3e9, so this matters.
    """
    beta = math.sqrt(max(1.0 - 1.0/(gam*gam), 0.0))
    return gam*(1.0 + beta)

print("=" * 78)
print("P11 — the admissible-source scope of Claim 1")
print("=" * 78)

# ---- 1. confirm the comoving scaling from the lane's OWN integrated column ----------------
e = exterior(ETA_C, W_J)
if e is None:
    print("exterior() failed at the centre epoch — cannot proceed"); sys.exit(1)
Nm1 = e["N"] - 1.0
Z = e["Z"]
tail = slice(-400, None)                              # the horizon-approach end of the column
lx, ly = np.log(Nm1[tail]), np.log(Z[tail])
slope, intercept = np.polyfit(lx, ly, 1)
print(f"\n1. Comoving frequency scaling, fitted on the last 400 samples of the column:")
print(f"   Z ~ (N-1)^p   ->   p = {slope:.6f}   (theory: 1/2)")
print(f"   N-1 spans {Nm1[-1]:.3e} to {Nm1[0]:.4f};  Z spans {Z[-1]:.6e} to {Z[0]:.4f}")
chk("the comoving frequency ratio really does scale as sqrt(N-1) in this lane's own column",
    abs(slope - 0.5) < 0.02, f"fitted exponent {slope:.6f} vs 1/2")

Z_h = float(Z[-1])
W_com = Z_h**4
print(f"\n   transmitted bolometric weight, comoving emitter: Z_h^4 = {W_com:.6e}")
chk("a comoving source beyond the boundary is suppressed to nothing",
    W_com < 1e-15, f"weight {W_com:.3e}")

# ---- 2. what boost would be needed to DEFEAT the suppression? -----------------------------
gam_needed = 0.5/Z_h                                  # D_max ~ 2*gam must reach 1/Z_h
print(f"\n2. Lorentz factor required to lift the transmitted weight to order unity:")
print(f"   need D_max ~ 1/Z_h = {1.0/Z_h:.6e}  ->  gam ~ {gam_needed:.6e}")
print(f"   check with the exact D_max: D_max({gam_needed:.4e}) * Z_h = "
      f"{D_max(gam_needed)*Z_h:.6f}")
chk("the required boost is enormous but FINITE at a finite horizon offset",
    np.isfinite(gam_needed) and gam_needed > 1e4, f"gam ~ {gam_needed:.3e}")

# ---- 3. the point that decides the claim: the requirement DIVERGES at the true horizon ----
print(f"\n3. Does that required boost stay finite as the true horizon is approached?")
print(f"   {'EPS_HZ':>10} {'N-1 at end':>14} {'Z_h':>14} {'gam required':>16}")
saved = G["EPS_HZ"]; needed = []
for eps in [1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10]:
    G["EPS_HZ"] = eps
    ee = exterior(ETA_C, W_J)
    if ee is None:
        print(f"   {eps:10.0e} {'—':>14} {'—':>14} {'exterior failed':>16}"); continue
    zh = float(ee["Z"][-1]); gn = 0.5/zh; needed.append((eps, gn))
    print(f"   {eps:10.0e} {ee['N'][-1]-1.0:14.3e} {zh:14.6e} {gn:16.6e}")
G["EPS_HZ"] = saved
growing = all(needed[k+1][1] > needed[k][1] for k in range(len(needed)-1))
ratio = needed[-1][1]/needed[0][1]
chk("the required boost DIVERGES as the horizon is approached (so no fixed gam ever suffices)",
    growing and ratio > 10.0,
    f"gam_required grows {ratio:.1f}x as eps falls from {needed[0][0]:.0e} to {needed[-1][0]:.0e}")

# ---- 4. the sharp threshold, tested rather than asserted ----------------------------------
def weight(nm1, p):
    """Transmitted bolometric weight for a boost family gam = (N-1)^(-p)."""
    gam = nm1**(-p) if p > 0 else 1.0
    return (D_max(max(gam, 1.0000000001)) * (nm1**0.5))**4 if gam > 1 else (nm1**0.5)**4

# NOTE ON THE FIRST VERSION OF THIS TEST, kept because the mistake is the lane's recurring one.
# I first asked "is the weight below 1e-3 at N-1 = 1e-9?" and called that a threshold test. It
# is not: the claim is about the LIMIT N-1 -> 0, and a magnitude at one point cannot see a
# limit. At p=0.49 the weight is 6.98 at N-1=1e-9 and still tends to zero — as (N-1)^0.04. The
# check reported FAIL on a case the theory gets right, because the check tested the wrong
# thing. Same defect class as REGATE3's finding: a test built so it cannot see its own claim.
# Replaced with a genuine limit test — evaluate down a sequence and check the TREND.
LADDER = [1e-6, 1e-9, 1e-12, 1e-15, 1e-18, 1e-21]
print(f"\n4. Sharp threshold: for gam = (N-1)^(-p) the weight goes as (N-1)^(2-4p), so it")
print(f"   vanishes iff p < 1/2. Tested as a LIMIT down N-1, not as a magnitude at one point:")
print(f"   {'p':>6} " + " ".join(f"{n:>11.0e}" for n in LADDER) + "   trend")
verdicts = {}
for p in [0.0, 0.25, 0.45, 0.49, 0.50, 0.55, 0.75]:
    ws = [weight(n, p) for n in LADDER]
    falling = all(ws[k+1] < ws[k] for k in range(len(ws)-1))
    rising  = all(ws[k+1] > ws[k] for k in range(len(ws)-1))
    verdicts[p] = ("-> 0" if falling else ("diverges" if rising else "flat"))
    print(f"   {p:6.2f} " + " ".join(f"{w:11.3e}" for w in ws) + f"   {verdicts[p]}")

chk("every p below 1/2 drives the weight to zero — including the marginal p=0.49",
    all(verdicts[p] == "-> 0" for p in (0.0, 0.25, 0.45, 0.49)),
    f"p=0.45 {verdicts[0.45]}, p=0.49 {verdicts[0.49]}")
chk("p above 1/2 diverges, so the caveat is real and not decorative",
    all(verdicts[p] == "diverges" for p in (0.55, 0.75)),
    f"p=0.55 {verdicts[0.55]}, p=0.75 {verdicts[0.75]}")
chk("p = 1/2 exactly is the knife edge — weight neither falls nor diverges",
    verdicts[0.50] == "flat", f"p=0.50 {verdicts[0.50]} (weight fixed at 16)")

# How slowly does the marginal case actually converge? This is why the gate's coarser
# "finite relative boost" is the more USEFUL qualifier than my sharper one.
w049 = weight(1e-9, 0.49)
print(f"\n   Marginal case p=0.49: the limit is zero, but the weight at N-1=1e-9 is still "
      f"{w049:.3f}.\n   Convergence goes as (N-1)^0.04 — the sharp threshold is correct and "
      f"nearly useless\n   near p=1/2. Bounded boost is the qualifier worth stating.")

# ---- 5. what the caveat costs in practice -------------------------------------------------
print(f"\n5. Scale of the required boost, for context:")
for label, g_ in [("a fast astrophysical jet", 30.0), ("the most extreme blazar bulk flow", 50.0),
                  ("required here (eps=1e-9)", gam_needed)]:
    print(f"   {label:34s} gam = {g_:12.4e}   transmitted weight = {(D_max(g_)*Z_h)**4:.4e}")
chk("even the most extreme astrophysical bulk boost leaves the transmission negligible",
    (D_max(50.0)*Z_h)**4 < 1e-10, f"weight at gam=50 is {(D_max(50.0)*Z_h)**4:.3e}")

print("\n" + "=" * 78)
npass = sum(1 for _, ok, _ in checks if ok)
print(f"SELF-CHECKS: {npass}/{len(checks)} passed")
print("""
CONCLUSION — the defensible form of Claim 1, in two separable parts:

  (i) CAUSAL, UNCONDITIONAL. A true event horizon transmits nothing from its forbidden side,
      for any source whatsoever. This is not a redshift argument; nothing above bears on it,
      and nothing above is needed to support it.

 (ii) REDSHIFT SUPPRESSION, CONDITIONAL, with the condition now sharp. For sources at finite
      depth approaching the horizon, the transmitted bolometric weight vanishes iff
          gam**2 * (N-1) -> 0,   i.e.   gam = o((N-1)**(-1/2)),
      where gam is the emitter's Lorentz factor relative to the comoving frame. Every emitter
      of BOUNDED boost satisfies this, which is why the gate's 'finite relative boost' is the
      right qualifier — and the required boost DIVERGES as the horizon is approached, so no
      fixed gam ever defeats it.

 NOT CLAIMED: singular emissivity. A source whose emitted intensity diverges in its own frame
 is not covered by any of the above, was never derived, and is not bounded here.""")
sys.exit(0 if npass == len(checks) else 1)
