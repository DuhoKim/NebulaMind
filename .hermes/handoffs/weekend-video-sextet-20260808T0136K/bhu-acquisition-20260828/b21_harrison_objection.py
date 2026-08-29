#!/usr/bin/env python3
"""B21 -- Harrison 1995 is not what our record's citation implies, and its objection is sharper.

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
    hashlib.sha256(raw).hexdigest().startswith("ea3e8d081592") and d.page_count==11,
    "11 pages for QJRAS 36, 193-203")
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

2. A CROSS-ENTRY TENSION -- MINE, UNGATED, AND FLAGGED AS SUCH

   Harrison's objection is CONDITIONAL ON SPATIAL CLOSURE. It says a CLOSED universe gives Smolin's
   theory at most one offspring, destroying selection.

   ENTRY 54 OF THIS CORPUS PREDICTS A CLOSED UNIVERSE -- Omega_k < 0, "Inflation preceded by a
   bounce requires Omega_k < 0", and a weekly cron watches DESI for exactly that sign.

   So if entry 54's prediction were confirmed, Harrison's argument says entry 31's mechanism fails.
   TWO ENTRIES IN THIS CORPUS WOULD BE IN TENSION, and the corpus does not record it.

   THIS IS AN INFERENCE OF MINE AND IT IS EXACTLY THE SHAPE THAT PRODUCED DEFECT 1z: a tidy story
   linking two things I worked on the same evening. It is NOT written into the bibliography and is
   going to both gate seats first. Specific ways it could be wrong: Harrison's argument may not
   survive scrutiny; it may not apply to entry 54's bounce cosmology, which is not a simple closed
   FRW recollapse; entry 31's CNS may not require the offspring-count variation the argument
   removes; and "closed" in the two papers may not mean the same thing.

3. NO TIER CHANGE, and none is proposed for 31, 54 or anything else.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed   [provenance limit above governs everything else]")
sys.exit(0 if n==len(checks) else 1)
