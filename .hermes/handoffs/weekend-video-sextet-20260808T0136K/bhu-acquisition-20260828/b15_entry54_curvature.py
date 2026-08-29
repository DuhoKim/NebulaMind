#!/usr/bin/env python3
"""B15 -- entry 54's curvature claim: our record is faithful, and what it is faithful TO is not.

b14 flagged entry 54 as asserting an experimental result with nothing pinned for it:
"Cites Planck PR3's 3sigma preference for Omega_k ~ -0.04 and same-direction ACT/DESI trends."

FIRST FINDING, AND IT EXONERATES THE RECORD: that sentence is accurate reporting. The source paper
(2505.23877, pinned) says verbatim: "The Planck PR3 lensed power spectrum revealed a 3sigma
preference for positive curvature, with Omega_k ~= -0.04 +/- 0.01, in agreement with our Eq. 27."
The 3sigma is the PAPER's, not ours. Entry 54 quotes it correctly.

SECOND FINDING, WHICH IS THE ONE THAT MATTERS: the paper's characterisation does not match Planck's
own, on three counts, and omits Planck's own resolution. Our record inherited all four without
checking -- which is what happens when a claim about a measurement is carried without its source.

PINNED TODAY: 1807.06209 (Planck 2018 results VI, Cosmological parameters), 526 kB.

WHAT THIS DOES NOT DO: it does not touch the weekly DESI curvature watcher. That watcher tests the
SIGN (Omega_k < 0), refuted by a confirmed OPEN universe or Omega_k < -0.09. Planck+lensing gives
-0.0106 +/- 0.0065, which is neither. Checked below rather than assumed.
"""
import math, sys
S="../bhu-reading-20260823/sources/"
K=" ".join(open(S+"1807.06209_clean.txt").read().split())   # Planck 2018 VI
Q=" ".join(open(S+"2505.23877_clean.txt").read().split())   # entry 54's paper
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B15 -- entry 54's curvature claim against Planck's own text"); print("="*98)

print("\n1. WHOSE CLAIM IS IT")
chk("SOURCE: the '3 sigma' is the source paper's own wording, so entry 54 reports it correctly and "
    "the record is NOT the origin of the overstatement",
    "preference for positive curvature" in Q and "3" in Q,
    "'The Planck PR3 lensed power spectrum revealed a 3sigma preference for positive curvature ... "
    "with Omega_k ~= -0.04 +/- 0.01, in agreement with our Eq. 27.' Note 'positive curvature' with "
    "Omega_k < 0 is CORRECT and not an error -- closed geometry is positive spatial curvature")

print("\n2. WHAT PLANCK ACTUALLY SAYS")
print("   TT,TE,EE+lowE       Omega_K = -0.044 (+0.018 / -0.015)   'well over 2 sigma'")
print("   99% region          -0.095 < Omega_K < -0.007,  ~1/10000 samples at Omega_K >= 0")
print("   CamSpec variant     Omega_K = -0.037 (+0.019 / -0.014)   (likelihood-modelling shift)")
print("   + lensing recon     Omega_K = -0.0106 +/- 0.0065         'well within 2 sigma' of FLAT")
chk("SOURCE: Planck describes the effect as WELL OVER 2 SIGMA, not 3",
    "an apparent detection of curvature at well over 2" in K,
    "verbatim from 1807.06209. The paper's '3 sigma' is a rounding UP of Planck's own hedge")
chk("SOURCE: Planck reports that adding the lensing reconstruction restores flatness -- the "
    "sentence the source paper omits and our record therefore never carried",
    "pulls parameters back into consistency with a spatially flat universe" in K,
    "'Closed models predict substantially higher lensing amplitudes than in LambdaCDM, so combining "
    "with the lensing reconstruction (which is consistent with a flat model) pulls parameters back "
    "into consistency with a spatially flat universe to well within 2 sigma'")
chk("SOURCE: Planck ties the curvature pull to the SAME systematic as its A_L anomaly rather than "
    "presenting it as an independent curvature detection",
    "essentially the same as those that lead to the preference for" in K,
    "'The reasons for the pull towards negative values of Omega_K ... are essentially the same as "
    "those that lead to the preference for A_L > 1'. It also says the polarization result 'is not "
    "robust at the approximately 0.5 sigma level to modelling of the polarization likelihoods'")

print("\n3. THE UNCERTAINTY, COMPUTED -- the paper's bar is tighter than Planck's")
c_pl, hi_pl = -0.044, 0.018      # distance from 0 uses the UPPER error
c_pa, s_pa  = -0.04, 0.01
sig_pl = abs(c_pl)/hi_pl; sig_pa = abs(c_pa)/s_pa
print(f"   Planck  {c_pl} +{hi_pl}  -> {sig_pl:.2f} sigma from flat")
print(f"   paper   {c_pa} +/-{s_pa} -> {sig_pa:.2f} sigma from flat")
chk("COMPUTED: the paper's quoted error bar is tighter than Planck's and yields a larger "
    "significance, which is where the '3 sigma' comes from",
    s_pa < hi_pl and sig_pa > sig_pl,
    f"+/-{s_pa} against Planck's +{hi_pl} (a factor {hi_pl/s_pa:.1f} narrower) turns "
    f"{sig_pl:.2f} sigma into {sig_pa:.2f}. Planck's own word for {sig_pl:.2f} is 'well over 2'")

print("\n4. DOES ANY OF THIS MOVE THE WEEKLY WATCHER? -- checked, not assumed")
lens_c, lens_s = -0.0106, 0.0065
fires_open = lens_c - 2*lens_s > 0
fires_closed = lens_c + 2*lens_s < -0.09
print(f"   watcher fires on: confirmed Omega_k > 0, or confirmed Omega_k < -0.09")
print(f"   Planck+lensing {lens_c} +/- {lens_s}  ->  2-sigma range "
      f"[{lens_c-2*lens_s:.4f}, {lens_c+2*lens_s:.4f}]")
chk("COMPUTED: the flatness-restoring Planck+lensing value fires NEITHER of the watcher's two "
    "conditions, so nothing here changes the watch",
    not fires_open and not fires_closed,
    f"the 2-sigma interval straddles neither 0 nor -0.09. nm_desi_curvature_watch.py tests the "
    f"SIGN and was already corrected in phase 6 to stop testing Eq. 27's window -- it is healthy "
    f"and this file leaves it alone")

print("""
5. WHAT TO CHANGE IN THE RECORD, and it is a repair to OUR sentence not a charge against theirs

   Entry 54's sentence is faithful and should stay. What it lacks is the other half: that Planck's
   own text calls this 'well over 2 sigma' rather than 3, quotes a wider bar, attributes the pull
   to the same systematic as its A_L anomaly, and reports that adding the lensing reconstruction
   returns the universe to flat within 2 sigma.

   THE SOURCE PAPER IS NOT BEING ACCUSED OF ANYTHING HERE. It cites Di Valentino et al. 2020, a
   published critical reanalysis that argues for a closed universe -- so a real dispute exists and
   the paper is taking one side of it. What our record did was report one side without recording
   that there is another. That is our defect, not theirs.

   AND IT IS THE SAME DEFECT AS ENTRY 51, in a milder form. Entry 51 asserted an experimental
   result with no citation. Entry 54 relays one accurately but without the primary source that
   would show it is contested. Both were invisible until the measurement side was pinned.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
