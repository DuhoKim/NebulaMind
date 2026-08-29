#!/usr/bin/env python3
"""B15 -- entry 54's curvature claim.  GATED 2026-08-29 and PARTLY REFUTED.

  AGATE_B15_VERDICT.md   CONTRAST_REFUTED_NAIVE_STATISTICS   (agy, Gemini 3.1 Pro)

################################################################################################
#  WITHDRAWN. The first version of this file claimed the source paper's "3 sigma" OVERSTATED
#  Planck's "well over 2 sigma", and that the overstatement came from the paper quoting a
#  narrower error bar. BOTH CLAIMS ARE WRONG AND ARE WITHDRAWN.
#
#  Planck's own text says "only about 1/10000 samples at Omega_K >= 0". A one-sided tail of 1e-4
#  is ~3.7 sigma. So "well over 2 sigma" is a CONSERVATIVE FLOOR, not a ceiling, and 3 sigma sits
#  comfortably inside it. My 2.44 sigma came from dividing a central value by a one-sided error
#  bar -- a Gaussian move on a posterior Planck explicitly describes as non-Gaussian, with
#  asymmetric errors it prints in the same equation I was reading.
#
#  AGATE: "It is completely unfair and incorrect to claim the 3 sigma comes from the paper
#  arbitrarily shrinking the error bar." That is the correct verdict and I accept it.
#
#  THE DIRECTION OF THE ERROR IS THE PART TO KEEP. Given a discrepancy with a published paper I
#  reached for "they overstated it" and computed a ratio that supported it. This is the SECOND
#  time today -- the first was Poplawski's floor, where I declined the same reading and was right
#  to. Here I asserted it and was refuted. Registered as harness defect 1z.
################################################################################################

WHAT SURVIVES, and it is still worth the file: Planck reports its OWN RESOLUTION of the curvature
preference -- adding the lensing reconstruction returns the universe to flat within 2 sigma -- and
neither the source paper nor our record carries that sentence. That is a real omission and it is
independent of how many sigma the preference is.
"""
import math, sys
from statistics import NormalDist
S="../bhu-reading-20260823/sources/"
K=" ".join(open(S+"1807.06209_clean.txt").read().split())
Q=" ".join(open(S+"2505.23877_clean.txt").read().split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B15 -- entry 54's curvature claim  [GATED: statistics REFUTED, omission STANDS]")
print("="*98)

print("\n1. WHOSE CLAIM IT IS -- the record quotes its source correctly")
chk("SOURCE: the source paper's own sentence is present verbatim, so entry 54 relays it and is "
    "not the origin of any characterisation",
    "lensed power spectrum revealed a 3" in Q and "preference for positive curvature" in Q,
    "the earlier version of this check tested for the token '3' anywhere in an 83 kB file and "
    "NAMED that as exoneration -- AGATE flagged it. It now tests the phrase. ('positive curvature' "
    "with Omega_k < 0 is correct, not an error: closed geometry IS positive spatial curvature)")

print("\n2. THE SIGNIFICANCE, DONE THE WAY PLANCK DOES IT")
p_tail=1e-4; z=abs(NormalDist().inv_cdf(p_tail))
print(f"   Planck: 'only about 1/10000 samples at Omega_K >= 0'  -> one-sided p = {p_tail:g}")
print(f"   Gaussian-equivalent                                   -> {z:.2f} sigma")
print(f"   my withdrawn ratio  0.044 / 0.018                     -> {0.044/0.018:.2f} sigma  [WRONG]")
chk("COMPUTED: the tail probability Planck prints corresponds to more than 3 sigma, so the source "
    "paper's '3 sigma' is consistent with Planck and my overstatement charge was unfounded",
    z > 3.0,
    f"{z:.2f} sigma from p={p_tail:g}. Planck's phrase 'well over 2 sigma' is a floor. AGATE: the "
    f"ratio method is 'the WRONG way to state distance-from-flat for a non-Gaussian, asymmetric "
    f"posterior' -- and Planck says in the same paragraph that this is 'not entirely a volume "
    f"effect', Delta chi^2_eff = -11")

print("\n3. WHAT PLANCK REPORTS THAT NOBODY CARRIED -- the finding that survives")
print("   TT,TE,EE+lowE     Omega_K = -0.044 (+0.018/-0.015)")
print("   + lensing recon   Omega_K = -0.0106 +/- 0.0065     -> flat 'to well within 2 sigma'")
chk("SOURCE: Planck states that adding the lensing reconstruction restores consistency with a "
    "flat universe",
    "pulls parameters back into consistency with a spatially flat universe" in K,
    "'Closed models predict substantially higher lensing amplitudes than in LambdaCDM, so combining "
    "with the lensing reconstruction (which is consistent with a flat model) pulls parameters back "
    "into consistency with a spatially flat universe to well within 2 sigma'. AGATE confirmed all "
    "quotes verbatim and NOT cherry-picked from a reversing context")
chk("SOURCE: Planck attributes the pull to the same systematic as its A_L anomaly rather than "
    "presenting it as an independent curvature detection",
    "essentially the same as those that lead to the preference for" in K,
    "and separately: the polarization result 'is not robust at the approximately 0.5 sigma level "
    "to modelling of the polarization likelihoods' -- CamSpec gives -0.037 (+0.019/-0.014)")

print("\n4. DOES ANY OF IT MOVE THE WEEKLY WATCHER -- checked, not assumed")
c,s_=-0.0106,0.0065
chk("COMPUTED: the flatness-restoring value fires neither of the watcher's two conditions",
    not (c-2*s_>0) and not (c+2*s_<-0.09),
    f"2-sigma range [{c-2*s_:.4f}, {c+2*s_:.4f}] crosses neither 0 nor -0.09. "
    "nm_desi_curvature_watch.py tests the SIGN, was corrected in phase 6, and is left alone")

print("""
5. WHAT TO CHANGE IN THE RECORD -- one sentence, not four

   NOT: "the paper overstates Planck." It does not, and that charge is withdrawn.
   BUT: entry 54 should carry Planck's own resolution alongside the preference it already
   reports -- that combining with the lensing reconstruction returns Omega_K to -0.0106 +/- 0.0065,
   flat within 2 sigma, and that Planck ties the preference to the same systematic as its A_L
   anomaly. Our record reports one side of a live dispute; the other side is in the primary source
   we had not pinned.

   CGATE_B14 adds, from a phase-6 citation audit I had not read: the Planck number is
   dataset-specific, the ACT paper's own summary runs contrary to our "same-direction" gloss, and
   the cited DESI analysis ASSUMES Omega_K = 0 rather than measuring a trend. NOT VERIFIED HERE --
   recorded as that seat's testimony pointing at prior work, not as a receipt of mine.

   THE PAPER IS NOT ACCUSED OF ANYTHING. It cites Di Valentino et al. 2020, a published reanalysis
   arguing for a closed universe. AGATE reports that paper claims 3.4 sigma on the same data;
   IT IS NOT PINNED IN THIS CORPUS and that figure is testimony, not a receipt.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
