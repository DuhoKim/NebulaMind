#!/usr/bin/env python3
"""B3 -- a corpus-integrity defect, found by the depth-selection rule on its FIRST pick.

HOW IT WAS FOUND, which is the point. Blanc: "record what 'densest' means as a rule before you
pick the next entries, not after." The rule was written first (DEPTH_SELECTION_RULE.md), then run.
It ranked entry 1 top at 11.16 physical values per 1,000 words -- nearly double the next -- and
disagreed with my own earlier pick of entry 36, which it placed fourth.

I would not have chosen entry 1. The rule sent me there, and the paper was the wrong paper.

THE DEFECT

    ENTRY_SOURCE_MAP.md  entry 1  ->  1111.1017_clean.txt

    entry 1  is R. K. Pathria (1972), "The Universe as a Black Hole", Nature 240, 298-299,
             DOI 10.1038/240298a0. The bibliography's own note: the paywalled body "remains
             [VERIFY]" and a strict read "needs the full text first (still unobtained)".

    1111.1017 is "Quantization of the Universe as a Black Hole" (Alfonso-Faus), the preprint of
             ApSS 337, 19-20 (2012), DOI 10.1007/s10509-011-0909-1 -- which is ENTRY 46.

    The bibliography records entry 46 as: "Two pages of Bohr-quantization dimensional analysis --
    10^122 bits, no dynamics, no falsifier." The pinned file is exactly that paper.

HOW THE MAP GOT IT WRONG, in its own words: "12 auto-matched on title at score 1.00". The string
"The Universe as a Black Hole" is a SUBSTRING of "Quantization of the Universe as a Black Hole",
so a containment-scoring title matcher scores 1.00 on the wrong paper. A perfect score on a
subset match -- the matcher was honest about its score and the score meant something other than
what it was read as.
"""
import re, sys

SRC = "../bhu-reading-20260823/sources/"
MAP = "../bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md"
BIB = "../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md"
T   = " ".join(open(SRC + "1111.1017_clean.txt").read().split())
M   = open(MAP).read()
B   = open(BIB).read()
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print("B3 -- entry 1 is mis-mapped; the pinned file is entry 46's paper"); print("=" * 96)

title_is_quant = "Quantization of the Universe as a Black Hole" in T
bits = "10^{122}" in T or "10 122" in T
print(f"\n1. WHAT THE PINNED FILE ACTUALLY IS")
print(f"   title contains 'Quantization of the Universe as a Black Hole' : {title_is_quant}")
print(f"   contains the 10^122 bits result the bibliography attributes")
print(f"   to ENTRY 46                                                  : {bits}")
chk("the pinned file is the QUANTIZATION paper, not Pathria's 1972 Nature paper",
    title_is_quant and bits,
    "entry 46's bibliography note reads 'Two pages of Bohr-quantization dimensional analysis -- "
    "10^122 bits'. That is this document.")

mapped_to_1 = bool(re.search(r"\|\s*1\s*\|[^|]*\|\s*`1111\.1017_clean\.txt`", M))
e1_pathria  = 'R. K. Pathria (1972). "The Universe as a Black Hole." Nature 240' in B
e46_quant   = '"Quantization of the universe as a black hole." Astrophys. Space Sci. 337' in B
print(f"\n2. WHAT THE RECORD CLAIMS")
print(f"   ENTRY_SOURCE_MAP maps entry 1 -> 1111.1017      : {mapped_to_1}")
print(f"   bibliography entry 1  is Pathria 1972, Nature   : {e1_pathria}")
print(f"   bibliography entry 46 is the Quantization paper : {e46_quant}")
# INVERTED 2026-08-29. This check previously asserted mapped_to_1 -- i.e. it PASSED while the
# defect was present. The defect was repaired in commit 9de0d9039 and the check was never turned
# round, so from that moment its RED state meant SUCCESS. A battery run then reports it as a
# regression and a reader spends effort chasing a bug that was fixed. Registered as defect 1ab.
corrected = bool(re.search(r"~~1~~\s*\*\*46\*\*", M)) and "CORRECTED 2026-08-29" in M
chk("the map no longer credits entry 1 with entry 46's file, and records the correction "
    "explicitly rather than silently",
    corrected and not mapped_to_1 and e1_pathria and e46_quant,
    "the map row now reads '~~1~~ **46** | ... | `1111.1017_clean.txt` | CORRECTED 2026-08-29'. "
    "THE ORIGINAL DEFECT IS UNCHANGED AS HISTORY: a substring title match, 'The Universe as a "
    "Black Hole' inside 'Quantization of the Universe as a Black Hole', scoring 1.00 on the wrong "
    "paper. What changed is that this file now tests the REPAIR instead of the wound")

unobtained = "still unobtained" in B
listed_unpinned = re.search(r"Entries 2, 3, 4, 5, 13,.*?46", M, re.S) is not None
print(f"\n3. THE TWO CONSEQUENCES")
print(f"   bibliography says entry 1's full text is 'still unobtained' : {unobtained}")
print(f"   map lists entry 46 among the UNPINNED                       : {bool(listed_unpinned)}")
chk("entry 1 has NO pinned source and entry 46 is pinned but recorded as unpinned -- the count "
    "is unchanged, the IDENTITIES are swapped",
    unobtained and bool(listed_unpinned),
    "so the map's 'auditable corpus: 32 of ...' is right in number and wrong in composition. NOTE 2026-08-29: that line's denominator said 51; the corpus is 58, corrected in the map, and its numerator remains unverified")

print("""
4. THE SERIOUS PART

   ENTRY 1 WAS IN THE RANDOM-DRAW POOL. The selection-bias control drew from 20 pinned+unaudited
   entries and entry 1 was one of them. Had it been drawn, I would have depth-audited Alfonso-Faus
   under the label "Pathria 1972" and reported a tier verdict for a paper I had never opened.
   It was not drawn. That is luck, not method.

5. WHAT THIS SAYS ABOUT THE SELECTION RULE

   Blanc's instruction was to fix the density measure before it picked anything, so the depth pass
   would not inherit the selection bias the random draw fixed for the main sweep. The rule did
   more than avoid bias: it sent me to a paper my judgement would not have chosen -- I picked
   entry 36 by raw count, and the rule ranks entry 36 FOURTH -- and the first paper it chose was
   mis-filed.

   A selection rule fixed in advance is not only fairer. It reaches places taste does not.

6. FIX APPLIED

   ENTRY_SOURCE_MAP corrected: 1111.1017 -> entry 46. Entry 1 restored to unpinned, with the
   bibliography's own "still unobtained" as the reason. No tier changes: entry 1 and entry 46 are
   both CONSISTENCY-ONLY and both stay there. This is a provenance correction, not a
   reclassification.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
