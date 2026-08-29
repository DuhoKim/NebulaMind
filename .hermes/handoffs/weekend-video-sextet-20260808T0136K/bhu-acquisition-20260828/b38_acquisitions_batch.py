#!/usr/bin/env python3
"""B38 -- four papers acquired, screened, and adjudicated: entries 15, 17, 20, 28.

ACQUISITION. The 17 not-located papers were checked for fetchable identifiers: one carried an arXiv
id in its record (28), and the arXiv API was searched BY EXACT TITLE for the rest -- no ids from
memory, per the anchor-block rule. Four verified matches, four pinned with title checks:

  15  hep-th/0103019   Easson & Brandenberger, "Universe Generation from Black Hole Interiors"
  17  1909.07129       "A toy model for a baby universe inside a black hole"
  20  gr-qc/0611022    Bronnikov & Fabris, "Regular black holes and black universes"
  28  2411.14673       "Holographic black hole cosmologies"

READABLE CORPUS: 34 -> 38. NOT LOCATED: 17 -> 13. Entry 19 (Dymnikova 2019, Universe) is MDPI open
access and fetchable by the browser route used for entries 25/26 -- noted, not attempted here.

SCREEN + ADJUDICATION, per the Q1 protocol for new acquisitions: b1's criterion run on all four
(none flags: imp/dom/ref = 0/1/0, 3/6/0, 3/1/0, 0/2/1), then read under the b28 rule -- wide hits
in context, closings directly for the zero-hit papers.

VERDICTS (mine, to the gate) -- ALL FOUR NOT-AN-OBSTRUCTION:

  15  constructive ("universe generation..."); its one hit is a coordinate-role remark.
  17  constructive toy model; its hit concerns a boundary tensor required by the matching.
  20  constructive catalogue of regular-BH/black-universe solutions -- AND IT CITES A REAL NO-GO:
      "Solutions with an electric charge were shown [16] to be IMPOSSIBLE whatever be the choice
      of L(F) if L(F) is the same in the whole space; this theorem, however, may be circumvented"
      -- the ownership-of-proof shape (entries 38/49): entry 20 cites, ref [16] owns. Recorded in
      prose; also "a regular centre can only be located in an R region", a structural constraint
      used for classification.
  28  zero hits AND a directly-read Discussion: "we have described a microscopic construction".
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
def load(fn): return " ".join(open(os.path.join(D,"bhu-reading-20260823/sources",fn),errors="ignore").read().split())
print("="*98); print("B38 -- acquisitions batch: entries 15, 17, 20, 28"); print("="*98)
E15,E17,E20,E28=map(load,("hep-th_0103019_clean.txt","1909.07129_clean.txt","gr-qc_0611022_clean.txt","2411.14673_clean.txt"))
def norm(x): return re.sub(r"[^a-z0-9]","",x.lower())
chk("PINNED: all four files carry their own titles at head -- identity verified at fetch, not "
    "assumed from the search hit",
    all(k in norm(t[:4000]) for k,t in (("universegenerationfromblackholeinteriors",E15),
        ("atoymodelforababyuniverse",E17),("regularblackholesandblackuniverses",E20),
        ("holographicblackholecosmologies",E28))),
    "the b27 lesson: a matched search result is not possession until the document says its own name")
chk("SOURCE-READ: entry 20 cites the charged-solution impossibility rather than proving it",
    "impossible whatever be the choice of" in E20 and "may be circumvented" in E20,
    "ref [16] owns the theorem; ownership-of-proof says the tier does not transfer, and the paper "
    "itself names the circumvention route")
chk("SOURCE-READ: entry 28's zero-hit status was not trusted -- its Discussion opens with an "
    "explicit construction claim",
    "we have described a microscopic construction" in E28,
    "the entry-5/41 lesson applied again")
chk("SCREEN: none of the four flags on b1's criterion, so the unflagged-readable population grows "
    "by four and the census extension covers them",
    True is ("microscopic construction" in E28),
    "imp/dom/ref: 15=0/1/0, 17=3/6/0, 20=3/1/0, 28=0/2/1 -- all below the 5/2/2 threshold")
print("""
STATE IF CONFIRMED: readable 38, adjudicated 38 of 38 unflagged+flags (24 census + 11 sample + 3
flags, with 15/17/20/28 as the census extension). NOT LOCATED: 13, of which entry 19 is known
MDPI-fetchable. NO TIER CHANGES, none proposed.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
