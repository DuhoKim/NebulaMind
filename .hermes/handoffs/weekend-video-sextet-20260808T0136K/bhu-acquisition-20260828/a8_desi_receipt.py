#!/usr/bin/env python3
"""A8 -- convert the A6 FIRES split from testimony into a receipt.

At the A6 gate the seats split on whether entry 25's w != -1 test currently fires. AGATE said
YES citing ~3 sigma from the DESI collaboration; CGATE said UNDETERMINED. BOTH reached the
collaboration paper by web search. Nothing in our corpus supported either number, so I adopted
neither and marked the whole thing testimony.

arXiv:2503.14738 (DESI DR2 Results II) is now PINNED. The empirical half is settled here from
the source. What remains unsettled is the paper's, not ours.

Pinned: ../bhu-reading-20260823/sources/2503.14738_clean.txt
        ../bhu-reading-20260823/sources/sym14091849_clean.txt   (entry 25)
"""
import re, sys, hashlib

D = " ".join(open("../bhu-reading-20260823/sources/2503.14738_clean.txt").read().split())
G = " ".join(open("../bhu-reading-20260823/sources/sym14091849_clean.txt").read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print("A8 -- the DESI receipt"); print("=" * 96)

is_desi = "DESI DR2 Results II" in D and "Baryon Acoustic Oscillations" in D
print(f"\n1. WHAT IS PINNED")
print(f"   title line: {open('../bhu-reading-20260823/sources/2503.14738_clean.txt').readline().strip()[:110]}")
chk("the pinned document is the DESI collaboration's own DR2 cosmology paper",
    is_desi, "not a third-party fit -- this is the source both seats reached by search")

# the collaboration's own significance statements, extracted not quoted from memory
key = "3.1\\sigma evidence in favor of dynamical dark energy from DESI+CMB alone" in D.replace("1​σ3.1","3.1")
alt = "3.1" in D and "2.8" in D
print(f"\n2. WHAT IT REPORTS")
for pat, lbl in [(r"(\d\.\d)\s*(?:\\sigma|σ)\s*evidence in favor of dynamical dark energy", "evidence, DESI+CMB alone"),
                 (r"significance of rejection of .{0,20}CDM is (\d\.\d)", "rejection of LCDM"),
                 (r"preference of just (\d\.\d)", "weakest combination quoted"),
                 (r"can be up to (\d\.\d)", "DESI+SNe without CMB")]:
    m = re.search(pat, D)
    print(f"   {lbl:<32} {m.group(1) + ' sigma' if m else '(not located)'}")
chk("the collaboration reports a 3.1 sigma preference for evolving dark energy from DESI+CMB",
    bool(re.search(r"3\.1\s*(?:\\sigma|σ)", D)) and "dynamical dark energy" in D,
    "this is the number both seats reported from search; it is now read from the pinned paper")

spread = sorted(set(re.findall(r"(\d\.\d)\s*(?:\\sigma|σ)", D)))
print(f"\n3. BUT IT IS NOT ONE NUMBER")
print(f"   sigma values appearing in the paper: {spread}")
chk("the significance is combination-dependent, spanning well below and above 3 sigma",
    len([x for x in spread if float(x) < 2.5]) > 0 and len([x for x in spread if float(x) > 3.0]) > 0,
    "'a preference of just 1.7 sigma' for one combination, 'up to 3.3' for another -- so "
    "'does it fire' has no single answer even before asking the BHU paper")

# ---- the half that is NOT ours to settle ---------------------------------------------------
has_threshold = re.search(r"(?:rule out|reject|exclude|falsif\w*)[^.]{0,60}(?:at|to)\s*\d(?:\.\d)?\s*(?:\\sigma|σ)", G)
print(f"\n4. DOES ENTRY 25 STATE A REJECTION THRESHOLD?")
print(f"   search for a sigma-level rejection rule in entry 25: {'FOUND' if has_threshold else 'none'}")
chk("ABSENCE CLAIM (weakest form): no sigma-level rejection rule matches in entry 25. The "
    "pattern would miss a rule stated in words, in a figure, or via a Bayes factor",
    has_threshold is None,
    "CGATE's UNDETERMINED was right, and this is now grounded in the source rather than inferred")

print("""
5. THE SPLIT, RESOLVED AS FAR AS IT CAN BE

   EMPIRICAL HALF -- SETTLED, and it is now a receipt. The DESI collaboration reports 3.1 sigma
   for evolving dark energy from DESI+CMB alone, with the value moving across dataset
   combinations (as low as 1.7, as high as 3.3 for DESI+SNe without CMB). AGATE's "~3 sigma" and
   CGATE's citation were both accurate. My earlier "does not fire", resting on a third-party
   1.7-sigma fit, understated what was reachable -- CGATE said so and was right.

   LOGICAL HALF -- NOT SETTLED, AND NOT OURS TO SETTLE. Entry 25 states no rejection threshold
   (check 4). My A6 script invented 3 sigma. Absent a rule from the author, "fires" is a
   judgement we would be imposing, and the paper's stated consequence is only that acceleration
   is "not solely caused by" r_S -- which an added component absorbs anyway.

   SO, AS OF 2026-08-29: FIRES is no longer UNDETERMINED. Duho ruled that where the author states
   no threshold, WE set one case by case, with an owner and a justification, recorded as ours --
   because "no bar chosen" meant nothing in the corpus could ever be declared failed.

   The bar for entry 25 is now set (RULE_FALSIFIER_THRESHOLD.md): >=3 sigma in a CMB-independent
   AND a CMB-dependent combination, chosen by Tori, justified by the prediction's sharpness
   against DESI's 1.7-4.2 sigma spread.

   THAT BAR IS MET: 3.1 sigma DESI+CMB, 3.3 sigma DESI+SNe.
   AND THE CLAIM STILL DOES NOT FIRE -- the "not solely caused by" auxiliary means w != -1
   refutes only the whole-cause claim. Entry 25 survives a bar it meets, structurally rather than
   evidentially. That is a sharper entry than "undetermined" and it is the one the corpus keeps.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
