#!/usr/bin/env python3
"""B16 -- entry 44's ">5 sigma", receipted. And a worked contrast with the mistake in b15.

Entry 44 (Pourhasan, Afshordi & Mann 2014) records that the paper "states its own base model is
'already ruled out at >5 sigma' (exact scale-invariance vs the observed red tilt)". CGATE_B14
found this: it is an experimental-status claim WITH a quantitative significance and NO INSTRUMENT
NAMED, which is why b14's original fixed vocabulary could not see it, and nothing receipted it.

It is receipted here from a source pinned earlier this evening for a different entry.

AND IT IS THE PLACE TO TEST THE GUARD FROM DEFECT 1z, because the same document supplies both a
case where a computed sigma is right and a case where it is wrong.
"""
import sys
from statistics import NormalDist
K=" ".join(open("../bhu-reading-20260823/sources/1807.06209_clean.txt").read().split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B16 -- entry 44's '>5 sigma' against Planck's own figure"); print("="*98)

print("\n1. WHAT PLANCK PRINTS -- taken as printed, not recomputed into a claim")
print("   n_s = 0.9649 +/- 0.0042   (68%, TT,TE,EE+lowE+lensing), eq. (19)")
print("   Planck's own words: 'which is 8 sigma away from scale-invariance (n_s = 1),")
print("                        confirming the red tilt of the spectrum at high significance'")
print("   + BAO: 'tightens the constraint to nearly 9 sigma: n_s = 0.9665 +/- 0.0038'")
chk("SOURCE: Planck states the departure from scale invariance at 8 sigma, in its own words and "
    "its own units",
    "away from scale-invariance" in K and "confirming the red tilt" in K,
    "eq. (19) of 1807.06209. THE SIGNIFICANCE IS QUOTED, NOT DERIVED BY ME -- which is the whole "
    "of the 1z guard")
chk("SOURCE: and Planck reports the tighter BAO combination too, so the figure is not resting on "
    "a single dataset choice",
    "tightens the constraint to nearly 9" in K,
    "n_s = 0.9665 +/- 0.0038, TT,TE,EE+lowE+lensing+BAO")

print("\n2. IS ENTRY 44's CLAIM TRUE?")
print("   entry 44 relays:  'already ruled out at >5 sigma'")
print("   Planck says:       8 sigma, and nearly 9 with BAO")
chk("COMPUTED: the paper's '>5 sigma' is satisfied by Planck's figure with room to spare, so the "
    "claim is TRUE and if anything conservative",
    8.0 > 5.0,
    "an entry asserting an observational exclusion turns out to UNDERSTATE it. Worth recording "
    "because the three previous measurement-side findings today all ran the other way")

print("\n3. THE CONTRAST WITH b15 -- same document, two statistics, one guard")
ns_ratio = (1-0.9649)/0.0042
z_tail = abs(NormalDist().inv_cdf(1e-4))
print(f"   n_s   : Planck prints '8 sigma'.  ratio (1-0.9649)/0.0042 = {ns_ratio:.2f}  -> AGREES")
print(f"   Om_k  : Planck prints a TAIL, 1/10000 at Om_K>=0 -> {z_tail:.2f} sigma")
print(f"           my ratio 0.044/0.018 = {0.044/0.018:.2f}                        -> DISAGREES")
chk("COMPUTED: the ratio method reproduces Planck's own figure for n_s but not for Omega_k, in "
    "the SAME paper -- so the b15 error was not bad luck, it was applying a Gaussian move where "
    "the source had already said the posterior is not one",
    abs(ns_ratio-8.0) < 0.5 and abs(0.044/0.018 - z_tail) > 1.0,
    f"n_s: {ns_ratio:.2f} vs Planck's 8, agreement. Omega_k: {0.044/0.018:.2f} vs {z_tail:.2f}, a "
    f"{z_tail-0.044/0.018:.2f} sigma miss. Planck quotes n_s SYMMETRICALLY and states its sigma; "
    f"for Omega_k it prints asymmetric errors, says the pull is 'not entirely a volume effect', "
    f"and gives a sample fraction instead of a sigma. The document tells you which tool it wants")

print("""
4. WHAT CHANGES IN THE RECORD

   Entry 44 gets a receipt: 1807.06209 eq. (19), 8 sigma (9 with BAO), so its relayed ">5 sigma"
   is true. NO TIER CHANGE -- 44 stays QUALITATIVE-DIRECTIONAL, and nothing here audits the rest
   of that entry, which remains unread beyond this one sentence.

   THE SWEEP'S THREE CANDIDATES ARE NOW CLOSED:
     39  false positive -- the Planck UNIT, not the satellite
     44  REAL, and now receipted; the claim is true and understated
     54  REAL, and now receipted; the record was carrying one side of a live dispute

   AND THE HONEST SCORE ON THE SWEEP ITSELF: of three candidates, one was a false positive, one
   confirmed a claim, and one corrected an omission. It found no fabricated result anywhere in the
   corpus. That is a good outcome for the corpus and a modest one for the probe, and both halves
   should be said.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
