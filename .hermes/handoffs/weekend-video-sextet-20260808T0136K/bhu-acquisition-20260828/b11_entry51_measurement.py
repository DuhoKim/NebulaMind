#!/usr/bin/env python3
"""B11 -- entry 51's measurement side, pinned; and what the LHC route can still do.

WHY. Entry 51 is the corpus's other LIVE calibrated falsifier. Its unfired status rested on a
bibliography sentence carrying NO CITATION AT ALL: "CMS reports no evidence for microscopic black
holes as of 2025-12". No CMS or ATLAS search was pinned; the only pinned source mentioning micro
black holes was Poplawski's own paper. That is the same defect that cost the entry-31 study its
framing today -- a falsifier's status resting on unpinned testimony -- caught before it cost
anything here.

PINNED TODAY:
  2604.10732  CMS, microscopic black holes / string balls / sphalerons, 13 TeV, 138 fb^-1
  2511.10662  CMS, black holes and sphalerons via ML, same dataset
"""
import re, sys, math
S="../bhu-reading-20260823/sources/"
A=" ".join(open(S+"2604.10732_clean.txt").read().split())
P=" ".join(open(S+"0910.1181_clean.txt").read().split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B11 -- entry 51: the measurement side, pinned"); print("="*98)

null = "excluded at 95% CL" in A.replace("\\,"," ") or "excluded at 95%" in A
mdep = "semiclassical black holes and string balls with masses below" in A and "8.4–11.4" in A
print("\n1. WHAT THE SEARCH ACTUALLY REPORTS")
print("   CMS, 13 TeV, 138 fb^-1: 'exclude at 95% CL semiclassical black holes and string balls")
print("   with masses below 8.4-11.4 TeV' (string balls 9.0-10.7) -- a model-dependent RANGE, and limits\n   rather than a discovery. THIS FILE FIRST PRINTED '8.7 TeV', WHICH IS NOT IN THE SOURCE: an\n   extraction returned the digit truncated and I supplied it. Corrected 2026-08-29 after CGATE_B12.")
chk("PINNED: the 'no evidence' claim now rests on a CMS search in this corpus rather than on an "
    "uncited sentence in our own bibliography",
    mdep,
    "the bibliography asserted 'CMS reports no evidence ... as of 2025-12' with no DOI, no arXiv "
    "id, and nothing pinned. Same shape as entry 31's unpinned measurement side")

# ---- the quantitative gap, computed rather than quoted -----------------------------------------
c=2.99792458e8; J_per_GeV=1.602176634e-10
M_FLOOR_KG=1e16
E_floor_GeV=M_FLOOR_KG*c*c/J_per_GeV
E_floor_TeV=E_floor_GeV/1e3
CMS_TeV=8.4   # low end of the source's 8.4-11.4 TeV model-dependent range; was 8.7, a digit I invented
print("\n2. THE GAP, COMPUTED")
print(f"   Poplawski's minimum black-hole mass   ~{M_FLOOR_KG:.0e} kg")
print(f"   as an energy                          ~{E_floor_GeV:.1e} GeV = {E_floor_TeV:.1e} TeV")
print(f"   CMS excludes production below          {CMS_TeV}-11.4 TeV (model-dependent)")
print(f"   ratio                                 ~{E_floor_TeV/CMS_TeV:.1e}")
chk("COMPUTED: the mass-energy conversion reproduces the ~10^43 GeV figure the bibliography "
    "carries for the floor",
    abs(math.log10(E_floor_GeV)-43) < 0.5,
    f"{E_floor_GeV:.2e} GeV from E = mc^2 on 1e16 kg -- the record's number checks out")

print("""
3. WHAT THE NULL RESULT MEANS -- and it is not what "unfired" suggests

   Poplawski's claim is that NO black hole can exist below ~1e16 kg. CMS searched a range entirely
   inside that forbidden region and found nothing.

   SO THE NULL IS A WEAK CONFIRMATION, NOT A NON-EVENT. Every LHC null in this range is exactly
   what the theory predicts. The bibliography records the test as "one-sided and positive-detection
   only ... a null LHC search fires nothing", which is right about FIRING and understates what a
   null contributes: it is consistent evidence, not absence of evidence.

4. WHAT WOULD MOVE IT -- and the LHC route is BOUNDED, not merely unexhausted

   TO FIRE: a confirmed black hole anywhere below the floor. That is 39 orders of magnitude of
   forbidden territory, and the LHC sits deep inside it -- which is why the gap does NOT empty the
   threshold. A detection at 9 TeV would refute the theory as decisively as one at 1e39 TeV.

   BUT THE ROUTE HAS A CEILING. Each improvement in the CMS exclusion pushes the possible-detection
   window UPWARD, and the LHC's collision energy caps where that window can go. The route is
   therefore self-limiting: it can only ever exclude further, and it cannot exclude past ~14 TeV.
   That is the difference between a test not yet done and a test whose instrument is bounded.

   WHAT WOULD ACTUALLY SETTLE MORE: a higher-energy collider, or an astrophysical constraint on
   primordial black holes below 1e16 kg -- which probes the same forbidden region without a
   collider at all, and is the route the bibliography does not currently track.

5. LIMITS OF THIS NOTE

   The 8.4-11.4 TeV range is model-dependent (large extra dimensions, and it varies with the number
   of them). It is not a model-independent statement about all black holes below that mass. CGATE_B12
   adds a sharper point: CMS bounds PRODUCTION in a large-extra-dimensions model while Poplawski
   bounds DENSITY in four-dimensional ECKS, so the two are illustrative against each other, not a
   shared axis. The collider statement that does NOT depend on CMS is Poplawski's own: LHC beam
   energy ~1e4 GeV against a 1e43 GeV floor, "39 orders of magnitude". The primordial-black-hole
   route in section 4 is NAMED, NOT PINNED -- no such constraint is in this corpus, and nothing
   here asserts what one would say.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
