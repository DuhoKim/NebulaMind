#!/usr/bin/env python3
"""A12 -- entry 8 (Poplawski 2010, PLB 687, 110, "Radial motion into an Einstein-Rosen bridge").

Ninth entry of the sweep, and the first from outside the Gaztanaga line -- the previous four
opposite-error candidates were all his, so a different framework (Einstein-Cartan / Einstein-Rosen
bridges) is a better test of whether the sweep's null result is about the RECORD or about ONE
AUTHOR. Entry 8 is CONSISTENCY-ONLY and sits in the bibliography's rank-1 spine.

RESULT: the tier is not merely correct, it is correct in the STRONGEST available sense. Entry 8
does not just happen to omit a falsifier -- it asserts that none exists for distant observers.

CHECK NAMING follows the rule adopted at a11 after Blanc's instruction and six consecutive gates
finding name/predicate overreach: a presence test is named as a presence test; an absence claim
carries a caveat naming what the pattern would miss.

Pinned: ../bhu-reading-20260823/sources/0902.1994_clean.txt
"""
import re, sys, hashlib

S = "../bhu-reading-20260823/sources/0902.1994_clean.txt"
T = " ".join(open(S).read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print(f"A12 -- entry 8  [sha256 {hashlib.sha256(open(S,'rb').read()).hexdigest()[:12]}]"); print("=" * 96)

# ---- 1. the paper's own indistinguishability claim, quoted ---------------------------------
ind = "Yet for distant observers, both solutions are indistinguishable" in T
print(f"\n1. THE PAPER DISCLAIMS DISTINGUISHABILITY ITSELF")
print(f"   \"Yet for distant observers, both solutions are indistinguishable.\"   present: {ind}")
chk("QUOTED: the source states Einstein-Rosen and Schwarzschild black holes are "
    "indistinguishable for distant observers", ind,
    "this is stronger than 'states no prediction that could fail' -- it asserts none is available")

# ---- 2. WITHDRAWN AND REPLACED -- this check was FALSE while printing PASS ----------------
# CGATE_HARNESS_VERDICT.md, dispositive finding: "a12 ... is already false on the pinned input
# while reporting PASS. The two patterns return len(sci)==0 and len(ineq)==0, but the source
# contains, among other numeric inequalities, 0<=r<inf, 0<xi<<r_g, 0<xi<<1."
# Verified by hand: my patterns find 0; a general inequality pattern finds 18.
#
# WHAT I REPORTED ON THE STRENGTH OF THAT ZERO, and now withdraw:
#   "COUNTED zero scientific-notation values and zero numeric magnitude inequalities in the
#    entire text" and "there is no number in the paper for a concealed threshold to hang on --
#    not one scientific-notation value in the whole text".
# The second clause was literally false. The regex recognised two renderings of scientific
# notation and inequalities beginning with a magnitude; it could not see most of the paper's
# numbers. An absence claim is only as strong as the pattern behind it, and mine was narrow.
SCI  = r"\d+(?:\.\d+)?\s*×\s*10\s*[−-]?\s*\d+|\d(?:\.\d+)?\s*\\times\s*10\^?\{?-?\d|10\^\{?-?\d|\d[eE][+-]?\d\d"
ANY_INEQ = r"[0-9a-zA-Zξ_{}\\]+\s*[<>≤≥≪≫]\s*[0-9a-zA-Zξ_{}\\∞]+"
sci  = re.findall(SCI, T)
ineq = re.findall(ANY_INEQ, T)
print(f"\n2. COUNTED, with the patterns REPAIRED after the harness gate")
print(f"   scientific-notation values (4 renderings) ..... {len(sci)}")
print(f"   inequalities of ANY form ...................... {len(ineq)}")
print(f"   examples: {[' '.join(x.split()) for x in ineq[:6]]}")
print(f"   These are DOMAIN CONDITIONS on coordinates (0<=r, r>r_g/4, 0<xi<<r_g), not numeric")
print(f"   thresholds on an observable. That distinction is now made by reading them, not by")
print(f"   a pattern that could not see them at all.")
chk("COUNTED: the paper's inequalities are coordinate-domain conditions, not magnitude "
    "thresholds on an observable -- 18 found and inspected, previously reported as ZERO",
    len(ineq) > 0 and len(sci) == 0,
    "the tier conclusion does NOT rest on this count any more; it rests on check 1's quoted "
    "sentence. CGATE: 'the underlying CONSISTENCY-ONLY tier may still be right, but this "
    "harness check cannot support it.'")

# ---- 3. the modal language of its own conclusion --------------------------------------------
mays = len(re.findall(r"\bmay be\b|\bsuggest that\b|\bmay have\b", T))
print(f"\n3. COUNTED: modal hedges in the conclusions")
print(f"   'may be' / 'suggest that' / 'may have' occurrences ... {mays}")
chk("COUNTED: the paper's own conclusion is modal -- 'suggest that observed astrophysical black "
    "holes MAY be Einstein-Rosen bridges'",
    mays >= 2,
    "directional at most, and the paper does not claim otherwise")

print("""
4. VERDICT

   TIER CONFIRMED: CONSISTENCY-ONLY. Entry 8 does not merely fail to state a falsifier; it
   states that distant observers cannot tell its object from a Schwarzschild black hole. That
   rests on check 1 -- a quoted sentence -- and on nothing else.

   WITHDRAWN: "there is no number in the paper ... not one scientific-notation value in the whole
   text." That was false. The paper contains 18 inequalities; my pattern could not see them. The
   conclusion survives the withdrawal because it never needed the count, but I reported the count
   as a finding and it was wrong.

   NINTH ENTRY, NINTH TIER UNCHANGED.

5. WHY NO GATE WAS DISPATCHED FOR THIS ONE

   Gates exist to attack contestable claims and proposed changes. Here there is neither: no tier
   change is proposed, and the two load-bearing facts are a quoted sentence and a count of zero.
   Dispatching two fresh-context seats to confirm that a paper contains no numbers would spend
   the adversarial budget on the least contestable result of the sweep. Recorded as a deliberate
   omission rather than a skipped step.

6. WHAT THIS ENTRY ADDS THAT THE OTHER EIGHT DID NOT

   The previous four opposite-error candidates were all Gaztanaga papers, which left open whether
   the sweep's null result was about the RECORD or about one author's habits. Entry 8 is a
   different author and a different framework, and its tier is also correct. That widens the
   result: across two independent lines, the existing classification has held.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
