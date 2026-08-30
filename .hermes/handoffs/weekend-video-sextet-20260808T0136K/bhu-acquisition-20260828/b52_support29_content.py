#!/usr/bin/env python3
"""B52 -- support entry 29 content bound to source: the two ~2 M_sun pulsar-mass measurements
that OPERATE entry 7's CNS falsifier. Self-computing string-presence (no seat gate).

ENTRY 29 = "The CNS test pair": Demorest et al. 2010 (Nature 467, 1081, PSR J1614-2230) and
Fonseca et al. 2021 (ApJL 915, L12, PSR J0740+6620). Entry 7's falsifier fires if a BHU/kaon-
softened equation of state cannot support a confirmed ~2 M_sun neutron star; these are the two
measurements that make that limb operable. Until now entry 29's record carried only byline
VERIFICATION (Crossref/DOI). This binds each to its pinned full text and confirms the load-bearing
number is present:
  - Demorest: PSR J1614-2230 = 1.97 ± 0.04 M_sun -- in the arXiv LaTeX source (1010.5788),
    `demorest-src/1614-nature-letter.tex`;
  - Fonseca:  PSR J0740+6620 = 2.08 M_sun (Shapiro-delay refinement) -- in `2104.00880_clean.txt`.
No over-attribution: both papers state exactly the ~2 M_sun measurement the record imports.
"""
import re, os
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
DEM = os.path.join(ROOT, "demorest-src/1614-nature-letter.tex")
FON = os.path.join(ROOT, "bhu-reading-20260823/sources/2104.00880_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B52 -- support entry 29 content bound to source"); print("=" * 98)

D = " ".join(open(DEM, errors="ignore").read().split())
chk("DEMOREST IDENTITY: pinned source is the J1614-2230 two-solar-mass Nature letter",
    "J1614" in D and ("Shapiro" in D or "two-solar" in D.replace("two solar", "two-solar")))
chk("DEMOREST CLAIM: the 1.97 M_sun mass (the limb-operating ~2 M_sun measurement) is in the source",
    "1.97" in D)

F = " ".join(open(FON, errors="ignore").read().split())
chk("FONSECA IDENTITY: pinned source is the refined high-mass PSR J0740+6620 measurement",
    "J0740+6620" in F and "Shapiro" in F)
chk("FONSECA CLAIM: the 2.08 M_sun mass (the second ~2 M_sun measurement) is in the source",
    "2.08" in F)

B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b29 = " ".join(blocks[29].split())
chk("RECORD NAMES BOTH: entry 29 attributes Demorest 2010 and Fonseca 2021 with correct DOIs",
    "Demorest" in b29 and "Fonseca" in b29
    and "10.1038/nature09466" in b29 and "10.3847/2041-8213/ac03b8" in b29)
chk("RECORD CONTENT-BOUND: entry 29 now cites the pinned full texts and the ~2 M_sun figures",
    "1.97" in b29 and "2.08" in b29 and "1614-nature-letter.tex" in b29 and "2104.00880" in b29)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
