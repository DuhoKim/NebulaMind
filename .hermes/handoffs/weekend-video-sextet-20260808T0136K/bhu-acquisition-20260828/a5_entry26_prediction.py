#!/usr/bin/env python3
"""A5 -- entry 26 (Gaztanaga, Symmetry 14, 1984): is the stated prediction a falsifier?

THE ABSTRACT PROMISES ONE: "We present a simple prediction to explain the observed value of
M ~ 6e22 Msun or equivalently Omega_Lambda ... and the coincidence problem Omega_m ~ Omega_Lambda."
A number on a measured observable. That is what a calibrated falsifier looks like from outside.

THE CHAIN, quoted from Section 4:
  "the maximum probability corresponds to observers that appear in BHs with Lambda_O/9 < Lambda
   < Lambda_O, where Lambda_O = 4/(3 tau_O^2) is the value corresponding to r_S ~ 3 tau_O/2 ...
   for the minimum time tau_O needed for observers to exit. If we assume that this time tau
   agrees with the age of our galaxy, we find good agreement between this prediction and the
   observed Lambda measurements (Omega_Lambda ~ 0.75)."

Supporting numbers the paper supplies itself: "M ~ 6e22 Msun ... has a typical collapse time of
tau ~ 11 Gyr", and "tau = 4GM/3".

Everything below is COMPUTED. The lane's describe-vs-compute law: no check here is satisfied by
prose. Pinned source: ../bhu-reading-20260823/sources/sym14101984_clean.txt
"""
import re, sys, hashlib

SRC = "../bhu-reading-20260823/sources/sym14101984_clean.txt"
T = open(SRC).read(); SHA = hashlib.sha256(T.encode()).hexdigest()[:12]
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

c, G, Msun = 2.99792458e8, 6.674e-11, 1.98892e30
GYR = 3.155760e16                      # seconds
KMSMPC_PER_INV_GYR = 977.792           # 1/Gyr -> km/s/Mpc

print("=" * 96); print(f"A5 -- entry 26, the stated prediction  [source sha256 {SHA}]"); print("=" * 96)

# ---- 0. POSITIVE CONTROL on the unit chain ------------------------------------------------
GMsun_c3 = G * Msun / c**3
print(f"\n0. POSITIVE CONTROL -- the mass-to-time conversion this whole audit rests on")
print(f"   G*Msun/c^3 = {GMsun_c3*1e6:.4f} microseconds   (textbook value 4.9255 us)")
chk("the mass->time unit chain reproduces the textbook solar mass in time units",
    abs(GMsun_c3*1e6 - 4.9255) < 0.005, "so tau = 4GM/3 can be trusted below")

# ---- 1. the paper's algebra is internally consistent --------------------------------------
# Part I: Lambda = 3/r_S^2. Paper: r_S = 3 tau_O/2  =>  Lambda_O = 3/(3 tau_O/2)^2 = 4/(3 tau_O^2)
tau_sym = 7.0
lhs = 3.0 / (1.5 * tau_sym)**2
rhs = 4.0 / (3.0 * tau_sym**2)
print(f"\n1. THE ALGEBRA CHECKS OUT")
print(f"   Lambda = 3/r_S^2 with r_S = 3tau/2  ->  {lhs:.10f}")
print(f"   the paper's Lambda_O = 4/(3 tau^2)  ->  {rhs:.10f}")
chk("Lambda_O = 4/(3 tau_O^2) follows exactly from Lambda = 3/r_S^2 and r_S = 3 tau_O/2",
    abs(lhs - rhs) < 1e-12, "the derivation is not where this fails")

# ---- 2. but the paper's OWN M and OWN tau disagree by 13% ----------------------------------
M_paper = 6e22
tau_from_M = (4.0/3.0) * GMsun_c3 * M_paper / GYR
print(f"\n2. THE PAPER'S TWO STATED NUMBERS ARE NOT CONSISTENT WITH EACH OTHER")
print(f"   tau = 4GM/3 at the paper's M = 6e22 Msun   ->  {tau_from_M:.2f} Gyr")
print(f"   the paper states                            ->  11 Gyr")
print(f"   M that WOULD give 11 Gyr                    ->  {11*GYR*3/(4*GMsun_c3)/1e22:.2f}e22 Msun")
chk("M = 6e22 Msun does NOT give the paper's own tau ~ 11 Gyr",
    abs(tau_from_M - 11.0) > 1.0,
    f"it gives {tau_from_M:.2f} Gyr, {100*(tau_from_M-11)/11:.0f}% high; 11 Gyr needs M = 5.3e22")

# ---- 3. the band, converted into a window on tau_O ----------------------------------------
def tau_window(H0, OL):
    H_L = H0 * OL**0.5 / KMSMPC_PER_INV_GYR      # 1/Gyr
    return 2.0/(9.0*H_L), 2.0/(3.0*H_L), H_L
print(f"\n3. THE PREDICTION, SOLVED FOR tau_O")
print(f"   Lambda_O/9 < Lambda_obs < Lambda_O   <=>   2/(9 H_L) < tau_O < 2/(3 H_L)")
print(f"   {'cosmology':<34} {'H_Lambda':>12} {'allowed tau_O (Gyr)':>26}")
WINDOWS = {}
for lbl, H0, OL in [("Planck 2018 (67.36, 0.6847)", 67.36, 0.6847),
                    ("the paper's own quoted 0.75", 67.36, 0.75),
                    ("SH0ES-like (73.04, 0.6847)", 73.04, 0.6847)]:
    lo, hi, H_L = tau_window(H0, OL); WINDOWS[lbl] = (lo, hi)
    print(f"   {lbl:<34} {H_L*KMSMPC_PER_INV_GYR:>9.2f} km/s/Mpc   {lo:>8.2f} -> {hi:<8.2f}")
lo_p, hi_p = WINDOWS["the paper's own quoted 0.75"]
chk("the allowed window is a FACTOR OF 3 wide in tau_O (factor 9 in Lambda)",
    abs((hi_p/lo_p) - 3.0) < 0.01, f"{lo_p:.2f} -> {hi_p:.2f} Gyr; galaxy ages sit inside almost regardless")

# ---- 4. and now the verdict on each candidate tau_O ----------------------------------------
CANDS = [("the paper's stated tau", 11.0),
         ("tau implied by the paper's own M = 6e22", tau_from_M),
         ("Milky Way oldest stars / globular clusters", 13.6),
         ("Milky Way thin disk", 8.8),
         ("epoch of the Sun's formation", 9.2)]
print(f"\n4. WHICH tau_O ACTUALLY SATISFIES THE PREDICTION?")
print(f"   {'candidate':<44} {'tau (Gyr)':>10} {'Planck':>9} {'0.75':>7}")
for lbl, tv in CANDS:
    a = WINDOWS["Planck 2018 (67.36, 0.6847)"]; b = WINDOWS["the paper's own quoted 0.75"]
    print(f"   {lbl:<44} {tv:>10.2f} {('IN' if a[0]<=tv<=a[1] else 'OUT'):>9} {('IN' if b[0]<=tv<=b[1] else 'OUT'):>7}")
a = WINDOWS["Planck 2018 (67.36, 0.6847)"]
chk("the paper's stated tau = 11 Gyr DOES satisfy its own prediction",
    a[0] <= 11.0 <= a[1], f"but with only {100*(a[1]-11)/11:.0f}% margin to the upper edge")
chk("the tau implied by the paper's OWN mass does NOT",
    not (a[0] <= tau_from_M <= a[1]), f"tau({M_paper:.0e} Msun) = {tau_from_M:.2f} Gyr > {a[1]:.2f} Gyr")
chk("'the age of our galaxy' -- the justification the paper gives -- does NOT either",
    not (a[0] <= 13.6 <= a[1]),
    f"13.6 Gyr (oldest stars) exceeds the upper edge {a[1]:.2f} Gyr; only the YOUNGER galaxy ages fit")

# ---- 5. the circularity ---------------------------------------------------------------------
print("""
5. WHY THIS IS A CONSISTENCY STATEMENT AND NOT A PREDICTION

   tau is not an independent input. The chain runs:
       observed Lambda  ->  r_S = sqrt(3/Lambda)  ->  M = r_S/2G  ->  tau = 4GM/3
   so tau ~ 11 Gyr is COMPUTED FROM the very Lambda the argument sets out to explain. The only
   external quantity is "the age of our galaxy", which enters with no number, no uncertainty,
   and no statement of WHICH age -- and the candidates span 8.8 to 13.6 Gyr (check 4), which is
   most of the factor-of-3 window (check 3). A target that wide is hit by construction.

6. THE ANTHROPIC SHIELD, which is the deeper reason this cannot fail

   Equation (11) is a probability P(Delta) over observers: the claim is where MOST observers
   live. A single observation -- ours -- falling outside the peak is not a refutation, because
   an atypical observer is permitted by the distribution. The paper states no confidence
   threshold at which our own position would count against the model. Without one, no
   measurement of Lambda can refute it.

   This is the same structure found in entry 21 (Roupas) an hour earlier: a real number that
   cannot fail, because the auxiliary that absorbs a discrepancy is supplied by the author.
   There it was an uncomputed amplitude; here it is observer typicality.

7. VERDICT ON THE TIER

   NOT a calibrated falsifier. Entry 26 stays QUALITATIVE-DIRECTIONAL, and the bibliography's
   existing tier is CONFIRMED -- the second such confirmation today, against a classifier bias
   that runs the other way (METHODS_NOTE_CLASSIFIER_BIAS.md).

   The band Lambda_O/9 < Lambda < Lambda_O IS an inequality with numbers, which is what makes
   this worth the audit rather than a glance. What it lacks is a refutation condition: tau_O is
   derived from the observable it explains, the window is a factor of 3 wide, and the anthropic
   framing licenses any miss.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("\nSTATUS: UNGATED. Checks 2 and 4 are quantitative criticisms of a published paper and\n"
      "must not leave this lane until an adversarial seat has attacked them.")
sys.exit(0 if n_ok == len(checks) else 1)
