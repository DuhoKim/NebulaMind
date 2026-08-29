#!/usr/bin/env python3
"""B21 -- Harrison 1995 is not what our record's citation implies, and its objection is BOUNDED.

GATED 2026-08-29. Both seats rendered all 11 pages and read the body.
  AGATE_B21  HARRISON_REFUTED_TENSION
  CGATE_B21  HARRISON_REFUTED_CROSS_ENTRY_TENSION

CLAIM 1 CONFIRMED, one qualification. The note-(11) transcription is word-for-word accurate; ref
(10) is Smolin 1992; neither seat found any observational confrontation on pp. 194-201.
QUALIFICATION (CGATE): Harrison DOES criticise Smolin in the body, at p. 196 -- conceptually, that
the proposal falls short of his condition (3) and lacks an unequivocal black-hole/organic-life
connection, citing Rothman & Ellis for the reservation that maximising black holes need not
maximise life. So "its objection" must mean THIS objection, not every objection he makes.

CLAIM 2 REFUTED -- THE CROSS-ENTRY TENSION IS DEAD, and it died on the distinction I listed as the
fourth way it could fail. Harrison's premise is not the SIGN of curvature; it is a globally closed
universe that RECOLLAPSES TO ONE FUTURE SINGULARITY, swallowing every black hole into a common
crunch. Entry 54 predicts a closed universe WITH A BOUNCE, and a bounce averts the global future
singularity entirely. AGATE: "the universe never collapses to a point that would merge all
individual black holes ... The two entries are compatible." CGATE adds that inflation and late-time
acceleration make the omitted dynamics decisive, and that Harrison's own wording is tentative
("This argument suggests") and imports a coordinate-sensitive horizon description into a global
collapsing spacetime without the causal derivation it needs.

SO THE CORPUS IS NOT IN TENSION WITH ITSELF, and the useful result is the BOUND: Harrison's
objection bites only on recollapsing closed cosmologies, which is a class this corpus's bounce
models are not in. That is worth more than the tension would have been.

THE PROCESS IS THE POINT. I distrusted this inference on sight -- it was the 1z shape, a tidy story
linking two things worked the same evening -- listed four specific ways it could fail, asked both
seats to break it, and it broke on one of the four. Flagging beat suppressing and beat asserting.


Read tonight from the ADS scan pinned earlier. SAME PROVENANCE LIMIT AS B20: JBIG2 images, no text
layer, so every quotation here is MY TRANSCRIPTION from rendered pages and cannot be grep-verified.
Treat quotations as testimony. The checks verify artifacts only.

WHAT SMOLIN'S CITATION IMPLIES. Smolin 2004 groups [13,14,30,31] as "arguments ... that S is in
fact contradicted by present observation". [30] is Harrison.

WHAT HARRISON 1995 ACTUALLY IS. "The Natural Selection of Universes Containing Intelligent Life",
QJRAS 36, 193-203. Its summary proposes that our universe was CREATED BY INTELLIGENT LIFE in a
parent universe -- a RIVAL natural-selection cosmology, not a refutation of Smolin's. Smolin 1992
appears as his reference (10), so he does engage it, but the paper's purpose is to advance an
alternative.

THE OBJECTION IS IN A FOOTNOTE, AND IT IS NOT OBSERVATIONAL -- IT IS TOPOLOGICAL. Reference (11):

  "Spatially closed universes have a single future singularity ... object A in a distant galaxy
   recedes while object B in our Galaxy falls into a nearby black hole ... When the rising density
   of the collapsing universe approaches the density of the black hole, the black hole loses its
   event horizon and A and B in company with the rest of the universe collapse together into a
   common singularity ... THIS ARGUMENT SUGGESTS THAT THE BLACK HOLE POPULATION FAILS TO AFFECT THE
   REPRODUCTIVE RATE OF UNIVERSES, AND EACH CLOSED UNIVERSE IN SMOLIN'S THEORY PRODUCES AT MOST ONE
   OFFSPRING UNIVERSE."

That is an attack on the SELECTION MECHANISM ITSELF: natural selection needs variation in offspring
count, and this says a closed universe has none. It is upstream of every prediction CNS makes.
"""
import fitz, hashlib, os, sys
S="../bhu-reading-20260823/sources/"
F=S+"harrison_1995_qjras36_193.pdf"
BIB=open("../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md").read()
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B21 -- Harrison 1995 read"); print("="*98)
raw=open(F,"rb").read(); d=fitz.open(F)
print(f"\n  {os.path.basename(F)}  {len(raw)} b  sha256 {hashlib.sha256(raw).hexdigest()[:12]}  {d.page_count} pp")
chk("ARTIFACT: the file's sha256 is compared against the digest recorded when it was acquired",
    hashlib.sha256(raw).hexdigest()==
      "ea3e8d081592d063b3f87f693a86da9d25f0ae837d762ff1a320e2b06ba4ce54" and d.page_count==11,
    "11 pages for QJRAS 36, 193-203. CGATE flagged that this compared only a 12-character prefix "
    "while the prose said 'the digest'; the full digest it reproduced independently is now pinned")
txt="".join(p.get_text() for p in d)
chk("ARTIFACT: no usable text layer, so the quotations above are transcriptions and this file "
    "cannot grep-verify any of them",
    len(txt.strip()) < 400 and txt.count("1995QJRAS..36..193H")==11,
    f"{len(txt.strip())} chars, the ADS bibcode once per page. Same limit as b20, where both seats "
    "rendered the scan and confirmed every quotation word-by-word -- that is the only check "
    "available and it must be run again here")

print("""
1. WHAT THIS DOES TO SMOLIN'S CHARACTERISATION -- two of four, and neither fits cleanly

   [13] Rothman & Ellis: conceptual objections plus ONE observational limb rejection (COBE), and a
        closing endorsement of the programme.
   [30] Harrison:        a rival proposal, whose objection to Smolin is TOPOLOGICAL, not
        observational, and sits in a reference footnote rather than the body.

   Neither is primarily "contradicted by present observation". BUT I HAVE READ TWO OF FOUR, AND
   HARRISON ONLY IN SUMMARY AND REFERENCES. [14] Ellis 1993 is pinned and unread; [31] Silk 1997 is
   paywalled. NOTHING IS CONCLUDED about whether Smolin mischaracterised his critics.

   AND THIS IS THE THIRD TIME TONIGHT THE PULL HAS BEEN TOWARD "THE AUTHOR OVERSTATED IT" --
   defect 1z, then 1ad, and now a third opportunity. The restraint above is deliberate.

2. THE CROSS-ENTRY TENSION -- PROPOSED, GATED, REFUTED, WITHDRAWN

   I proposed: Harrison's objection is conditional on spatial closure; entry 54 predicts a closed
   universe; therefore confirming entry 54 would break entry 31's mechanism, and the corpus would
   be in tension with itself.

   IT DOES NOT FOLLOW, and both seats killed it the same way. "Closed" is not one premise. Harrison
   needs a universe that RECOLLAPSES to a single future singularity so that black holes merge into
   the common crunch. Entry 54 predicts closed geometry WITH A BOUNCE -- and a bounce removes the
   future singularity Harrison's argument requires. Geometric overlap, different dynamics.

   WHAT SURVIVES IS A BOUND, and it is more useful than the claim was: HARRISON'S OBJECTION APPLIES
   ONLY TO RECOLLAPSING CLOSED COSMOLOGIES. Every bounce model in this corpus is outside its scope.
   Recorded so that nobody later rediscovers the "tension" and files it.

3. NO TIER CHANGE, and none is proposed for 31, 54 or anything else.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed   [provenance limit above governs everything else]")
sys.exit(0 if n==len(checks) else 1)
