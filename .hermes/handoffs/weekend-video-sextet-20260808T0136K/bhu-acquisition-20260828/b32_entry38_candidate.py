#!/usr/bin/env python3
"""B32 -- entry 38 carries unrecorded impossibility content, and its attribution needs checking.

FROM b31's census of the 20 unflagged readable papers the miss-rate sample did not draw. Entry 38
(Smoller & Temple, math-ph/0302036) scored highest on the widened pattern, 21 constructions.

WHAT IT SAYS, verbatim and grep-verifiable:

  "a standard TOV metric CANNOT BE CONTINUED INTO A BLACK HOLE, except in the special case when
   the pressure is zero, (WE PROVED THIS IN [15])"
  "we showed in [15] that the standard TOV metric cannot be continued into a Black Hole"
  "the infinite FRW metric CANNOT BE MATCHED to the Schwarzschild metric"

NONE OF THIS IS IN ENTRY 38's RECORD. Its tier is CONSISTENCY-ONLY and its note says nothing about
either impossibility.

THE ATTRIBUTION, AND WHY IT IS NOT SETTLED HERE. [15] resolves to "Arch. Rat. Mech. Anal. 138,
239-277 (1997)", which is entry 57 of this corpus by volume and pages -- and entry 57 IS PINNED AND
READABLE, unlike the entry 49 -> 48 case where the proof paper cannot be obtained. So the
ownership-of-proof convention adopted tonight has a second application and this time it is testable.

BUT I DID NOT FIND THE PROOF IN ENTRY 57. Its abstract is constructive -- "we constructed a class of
spherically symmetric fluid dynamical shock waves ... we derive an alternate version of these
ordinary differential equations" -- and the passages I sampled describe what their solutions model,
not what cannot exist. THAT IS AN ABSENCE CLAIM OVER A 39-PAGE PDF SAMPLED BY THREE REGEXES, which
is the weakest kind, and it is exactly the shape I have been wrong about repeatedly today. IT IS
FLAGGED, NOT CONCLUDED.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

E38=" ".join(open(os.path.join(D,"bhu-reading-20260823/sources/math-ph_0302036_clean.txt"),errors="ignore").read().split())
BIB=" ".join(open(os.path.join(D,"bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")).read().split())
print("="*98); print("B32 -- entry 38: unrecorded impossibility content"); print("="*98)

chk("SOURCE: entry 38 states that a standard TOV metric cannot be continued into a black hole "
    "except at zero pressure, and says it proved this in a cited paper",
    "cannot be continued into a Black Hole" in E38 and "we proved this in" in E38,
    "twice, in two separate passages. Neither appears anywhere in entry 38's record")
chk("SOURCE: and separately that the infinite FRW metric cannot be matched to the Schwarzschild "
    "metric",
    "cannot be matched to the Schwarzschild metric" in E38,
    "a second impossibility statement, also unrecorded")
i=E38.rfind("[15]")
chk("SOURCE: the citation resolves to Arch. Rat. Mech. Anal. 138, 239-277 (1997), which is entry "
    "57 of this corpus by volume and pages",
    "Arch. Rat. Mech. Anal., 138, 239-277 (1997)" in E38[i:i+200],
    "entry 57's own PDF running header reads 'Arch. Rational Mech. Anal. 138 (1997) 239-277'. The "
    "titles differ slightly between citation and paper, which is the alternate-title trap that cost "
    "b27 entry 41 -- so this is matched on volume and pages, not on title")
# INVERTED after the gate. This asserted the record LACKED both statements -- true when written,
# false the moment I recorded them. Defect 1ab, FOURTH occurrence, and the worst of the four: I had
# already BUILT a mechanical sweep for exactly this shape after the third, and did not run it.
chk("RECORD: entry 38's entry now carries both impossibility statements and the note that entry 57 "
    "does not own the attributed proof",
    "cannot be continued into a Black Hole" in BIB and
    "does not own this" in BIB,
    "PATTERN: the two verbatim phrases. ONE CLASS THIS MISSES: the record could paraphrase either "
    "result without quoting it. WHAT WAS DONE: entry 38's note was read directly -- it is a "
    "construction summary with no impossibility content at all")

print("""
WHAT IS PROPOSED, AND IT IS ONLY A READING TASK

  NOT a tier change. Under the ownership-of-proof convention adopted tonight, entry 38 REPORTS an
  impossibility it attributes elsewhere -- which is the entry 49 pattern, and the convention says
  that does not transfer the tier. So on its face entry 38 stays CONSISTENCY-ONLY and the finding
  goes into its prose.

  THE OPEN QUESTION IS WHETHER ENTRY 57 OWNS THE PROOF. If it does, entry 57 becomes an obstruction
  candidate and this is the first case where the proof paper is actually in hand. If it does not,
  then entry 38's "we proved this in [15]" points somewhere outside the corpus, and the claim has no
  owner here at all.

  I COULD NOT FIND THE PROOF IN ENTRY 57 and I do not trust that. Three regexes over 39 pages is
  not a search, entry 5 taught this lane that a paper's central impossibility can carry none of the
  expected words, and both seats have caught me concluding from partial reads today. THE GATE IS
  ASKED TO READ ENTRY 57 PROPERLY.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
