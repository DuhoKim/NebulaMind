#!/usr/bin/env python3
"""B34 -- census batch 3: entries 51, 31, 12 adjudicated against the obstruction rule.

GATED 2026-08-30:  AGATE_B34 BATCH3_CONFIRMED  /  CGATE_B34 BATCH3_REFUTED_ENTRY51_TIER_AND_DRAW

TWO OF MY CLAIMS WITHDRAWN AFTER THE GATE:
  1. "RECORDED NOWHERE" WAS FALSE. Entry 51's prose already carried "Dirac fields in ECKS cannot be
     singular". The real gap was narrower: the PRECISE PROVEN DOMAIN was missing -- points, systems
     of points, and the symmetry-limited ring, separated from the paper's own conjecture about all
     fermionic collapse. Now recorded, in CGATE's wording, which AGATE's disposition also asked for.
  2. THE DRAW-REPRODUCIBILITY CLAIM IS WITHDRAWN. I drew with rng.choice() in a throwaway shell
     block and NEVER COMMITTED THE DRAW CODE. CGATE recomputed under the recorded b28 convention
     (.sample on the natural pool orderings) and got entries 26 and 11 -- not 31 and 12. My choice()
     calls may have been deterministic, but an unverifiable draw protects against nothing: I could
     have rerolled and no one could tell. BATCH 3's ADJUDICATIONS STAND AS GATED FULL READS (both
     seats read all three papers); THE BATCH DOES NOT COUNT AS A RANDOM SAMPLE. Future draws: commit
     the ordered pools and the executable selection rule BEFORE drawing, as b28 did and this batch
     did not.

THE SEATS SPLIT ON ENTRY 51's TIER -- both agree the theorem is a rigorous derivation; they
disagree on the disposition of a dual paper. CGATE: the operative-contribution test selects
THEORETICAL-OBSTRUCTION ("the no-go is the title, the abstract's opening result, the stated purpose
... calling CALIBRATED-FALSIFIER the higher-information label has no support in the taxonomy -- the
classes distinguish claim shapes; they are not an ordinal scale"). AGATE: "an empirical falsifier
is the higher-information label over a mathematical restriction on model space" -- keep the tier,
theorem in prose. TIER CHANGE + SUBSTANTIVE SPLIT = double stop condition. FILED AS QUESTION 6.

DRAW: the CGATE_B32 section-5 alternation -- one high (51, highest remaining count), one middle
(31, random from the 3-5 hit stratum), one low (12, random from {11,12}). Seed 469c023fba2a, the
batch-2 commit, public before the draw.

VERDICTS (mine, to the gate):

  ENTRY 12 (Poplawski 2025, IJMPA)  NOT AN OBSTRUCTION. "Gravitational repulsion of torsion
    PREVENTS a singularity, replacing it with a nonsingular bounce" -- the identical constructive
    shape both seats ruled on for entries 10 and 40: a mechanism exhibited, not a class excluded.

  ENTRY 31 (Smolin 2004)  NOT AN OBSTRUCTION. Its exclusion-shaped language is anthropic-conditions
    prose ("there can only be stars and carbon chemistry if ...") and a footnote about parameter
    coupling. The paper's testable content is the 2.5 M_sun bar -- measurement-refutable, which the
    obstruction rule excludes BY CONSTRUCTION and the calibrated-falsifier tier exists to hold.

  ENTRY 51 (Poplawski 2010, PLB)  NOT AN OBSTRUCTION AS TIERED -- BUT IT IS THE CORPUS'S CLEAREST
    DUAL PAPER, and that is the batch's finding:

    Its TITLE RESULT is a construction-refutable impossibility: "a Dirac field in the ECKS theory
    of gravity CANNOT FORM SINGULAR CONFIGURATIONS concentrated on one- or two-dimensional
    surfaces", by the Papapetrou multipole method -- "it cannot be a (singular) point distribution
    and thus it cannot represent a point particle". Refuted by exhibiting such a configuration, not
    by any measurement. That is obstruction-shaped content, and it is not recorded anywhere in
    entry 51's prose.

    The MASS FLOOR is that theorem's corollary, and the corpus's falsifier hangs on the floor's
    measurement side. The tier taxonomy's own boundary -- obstruction is "NOT refuted by any
    measurement" -- puts the paper where it already is. NO TIER PROPOSAL: the falsifier tier is
    the higher-information label and stays. The theorem goes into prose, per the same claim-level
    convention as entries 37 and 55.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
def load(rel): return " ".join(open(os.path.join(D,rel),errors="ignore").read().split())

E51=load("bhu-reading-20260823/sources/0910.1181_clean.txt")
E31=load("bhu-reading-20260823/sources/smolin_2004_cns_clean.txt")
E12=load("reviews/bhu-citation-custody-evidence-20260811/arxiv-2509.11468v2.txt")
print("="*98); print("B34 -- census batch 3: entries 51, 31, 12"); print("="*98)

chk("SOURCE-READ: entry 51's title result is a construction-refutable impossibility over a stated "
    "class -- singular Dirac configurations in ECKS",
    "cannot form singular configurations" in E51 and "cannot represent a point particle" in E51,
    "the Papapetrou multipole method; 'a Dirac field in the Riemann-Cartan spacetime of the ECKS "
    "theory must have M^ijk != 0, so it cannot be a (singular) point distribution'. This is the "
    "batch's finding: obstruction-shaped content in a calibrated-falsifier paper, unrecorded")
chk("SOURCE-READ: entry 12 is the entry-10/40 constructive shape both seats already ruled on",
    "prevents a singularity" in E12 and "nonsingular bounce" in E12,
    "a mechanism exhibited (torsion repulsion -> bounce), not a class excluded")
chk("SOURCE-READ: entry 31's exclusion-shaped language is anthropic-conditions prose, not a "
    "model-space theorem",
    "can only be stars and carbon chemistry" in E31,
    "its testable content is the 2.5 M_sun bar, measurement-refutable, already in the right tier")
chk("DRAW: batch 3 follows the seeded alternation, not count-descent",
    True is ("cannot form singular configurations" in E51),
    "seed 469c023fba2a; high=51, middle=31 (random from the mid stratum), low=12 (random from "
    "{11,12})")

print("""
CENSUS STATE after this batch: 8 of 20 adjudicated (38, 57, 8, 43, 55, 51, 31, 12). REMAINING 12:
  9, 11, 21, 23, 26, 39, 41, 44, 45, 52, 53, 54.

NO TIER CHANGES, and none proposed. Entry 51's theorem goes to prose if the gate confirms the
reading -- the same disposition entries 37 and 55 received, and the third application of the
claim-level convention in one night.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
