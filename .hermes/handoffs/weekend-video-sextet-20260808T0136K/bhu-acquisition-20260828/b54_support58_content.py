#!/usr/bin/env python3
"""B54 -- support entry 58 content bound to source: Longo's spin-handedness dipole, the
adjudication instrument for the BHU family's preferred-axis prediction (the amplitude the DESI
spin-parity campaign tests). Self-computing string-presence (no seat gate).

ENTRY 58 = M. J. Longo, "Detection of a dipole in the handedness of spiral galaxies with redshifts
z ~ 0.04," PLB 699 (2011) 224. Until now entry 58 carried only byline VERIFICATION (Crossref) +
"kimi recall R10"; the paper itself was not pinned. Acquired 2026-08-30 from arXiv (1104.2815);
ar5iv has no full LaTeX render for this 2011 paper, so the pin is the arXiv abstract page
`arxiv_1104.2815_abs.html` (same precedent as entry 33's Phys.Rept.381 abstract pin). The abstract
carries the complete load-bearing content the record imports:
  - dipole asymmetry AMPLITUDE = -0.0408 ± 0.011 (chance probability 7.9 x 10^-4);
  - preferred AXIS at (l, b) ≈ (52°, 68.5°), near the WMAP CMB alignments;
  - SDSS sample of 15158 spiral galaxies (z < 0.085; the title's z ~ 0.04 is the effective depth).
No over-attribution: Longo states exactly the handedness-dipole detection the record cites.
"""
import re, os, html
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PIN = os.path.join(ROOT, "bhu-reading-20260823/sources/arxiv_1104.2815_abs.html")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

def norm(path):
    t = re.sub(r"<[^>]+>", " ", open(path, errors="ignore").read())
    return " ".join(html.unescape(t).split())

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B54 -- support entry 58 content bound to source"); print("=" * 98)

S = norm(PIN).lower()
chk("IDENTITY: pinned source is Longo's spiral-galaxy handedness-dipole paper (1104.2815)",
    "longo" in S and "handedness" in S and "spiral galaxies" in S and "dipole" in S)
chk("AMPLITUDE: the dipole asymmetry -0.0408 ± 0.011 (the tested amplitude) is in the source",
    "-0.0408" in S and "0.011" in S)
chk("SIGNIFICANCE: the chance probability 7.9 x 10^-4 is in the source",
    "7.9" in S and "10-4" in S)
chk("AXIS + SAMPLE: preferred axis (l,b)=(52°,68.5°) and the SDSS 15158-spiral sample are present",
    "68.5" in S and "15158" in S)

B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b58 = " ".join(blocks[58].split())
chk("RECORD: entry 58 cites Longo/PLB699/DOI and is now content-bound to the pin with the amplitude",
    "Longo" in b58 and "10.1016/j.physletb.2011.04.008" in b58
    and "0.0408" in b58 and "1104.2815" in b58)  # magnitude, sign-agnostic (record uses U+2212)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
