#!/usr/bin/env python3
"""B46 -- entry 14 read in full under the census rule (the ICTP scan acquired at 13:0x KST).

THE READ, scope stated exactly: the 21-sheet KEK scan of ICTP IC/88/91 (Frolov, Markov &
Mukhanov, "Black Holes as Possible Sources of Closed and Semiclosed Worlds", May 1988;
published as PRD 41, 383). The 13 TEXT sheets were read completely -- OCR is clean on prose
(the companion frolov_markov_mukhanov_ic8891_clean.txt holds it, headered as grep receipts) and
the equation-dense passages were checked against the rendered pages. The 8 FIGURE sheets are
hand-drawn conformal diagrams: every caption was read (sheet 13 lists all twelve), the sheets
carrying Figs. 5/6 and Figs. 11/12 were rendered and visually checked against their captions,
and the remaining figure sheets were inspected via captions only. That is the whole scope; the
gate should render whatever it distrusts.

RULE, unchanged from b28: does the paper PROVE that no member of a specified class of models
can satisfy a specified conjunction of conditions -- refutable by counterexample, not by
measurement?

VERDICT (mine, to the gate): NOT AN OBSTRUCTION -- constructive throughout, and the paper is
explicitly the ESCAPE-side of entry 48's theorem, not an exclusion of anything. Inventory:
  Sec. 2  Schwarzschild-interior -> de Sitter junction across a SPACELIKE Israel thin shell at
          r0 ~ (2m/l)^(1/3) l, under the LIMITING CURVATURE HYPOTHESIS (all invariants bounded
          Planckian; T -> -(Lambda/8pi) g at the limit -- "our second main hypothesis", a guess
          about an unknown theory). Construction + junction algebra; no exclusion.
  Sec. 3  collapse case: Kruskal/de Sitter/Friedmann regions glued; construction.
  Sec. 4  Vaidya evaporation endpoints: forbidden PARAMETER RANGES for sigma (intrinsic-geometry
          compatibility on the junction), stable Planck remnants, pinched-off closed worlds --
          family-delimiting conditions inside the construction, the entry-37 shape, nothing
          class-wide.
  Sec. 5  creation of closed/semiclosed/flat Friedmann universes inside the black hole; "an
          example of 'a creation of a closed or semiclosed world in laboratory'".
  TIER: triage had already filed entry 14 CONSISTENCY-ONLY; the full read CONFIRMS that tier.
  NO TIER CHANGE OCCURS IN THIS ARTIFACT -- the marker is untouched and the census obs set
  stays {22, 5}.

THE CROSS-LINK THAT MAKES THIS READ VALUABLE: the paper cites Farhi & Guth (its ref. [7] = our
entry 48) twice and claims the escape explicitly -- the junction shell carries S_t^t < 0, so
T_uv l^u l^v < 0 for some null l in the transition region ("the conditions which are necessary
for singularities (in accordance with Penrose theorem) are not fulfilled here"), and Sec. 5
says the global-Cauchy-surface and null-positivity conditions "used in [7] may be violated".
Entry 48's obstruction and entry 14's construction now corroborate each other's load-bearing
hypotheses from opposite sides: the obstruction holds under NEC + Cauchy development; the
escape construction violates exactly those, by design, at limiting curvature.
"""
import re, os, hashlib
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PDF = os.path.join(ROOT, "bhu-reading-20260823/sources/frolov_markov_mukhanov_ic8891_kekscan_2000_33_351.pdf")
TXT = os.path.join(ROOT, "bhu-reading-20260823/sources/frolov_markov_mukhanov_ic8891_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B46 -- entry 14 full read (ICTP IC/88/91 scan)"); print("=" * 98)

raw = open(PDF, "rb").read()
chk("PIN: scan present, PDF magic, sha256 1dcb755eb0af...",
    raw[:4] == b"%PDF" and hashlib.sha256(raw).hexdigest().startswith("1dcb755eb0af"))
S = " ".join(open(TXT, errors="ignore").read().split())
chk("OCR COMPANION: headered as grep receipts with the PDF as pin of record",
    S.startswith("[OCR EXTRACTION") and "pin of record" in S)
chk("IDENTITY LANDMARKS: title, all three authors, IC number, Trieste",
    "BLACK HOLES AS POSSIBLE SOURCES" in S and "Frolov" in S and "Markov" in S
    and "Mukhanov" in S and "IC/88/91" in S and "TRIESTE" in S.upper())
chk("CONSTRUCTION LANDMARKS: the limiting-curvature hypothesis, the de Sitter attachment, the "
    "Israel shell method, and the laboratory-creation sentence are in the source",
    "limiting curvature" in S and "de Sitter" in S and "Israel" in S
    and "creation of a closed or semiclosed" in S)
chk("ESCAPE LANDMARKS (the entry-48 cross-link): both escape statements are in the source, and "
    "ref [7] is Farhi-Guth PLB 183",
    "are not fulfilled here" in S and "may be violated" in S
    and "Farhi" in S and "183B (1987) 149" in S)
B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b14 = " ".join(blocks[14].split())
chk("RECORD: entry 14 carries the read scope (figure-sheet honesty included), the confirmed "
    "tier, and the named-escape cross-link to entry 48",
    "READ IN FULL 2026-08-30" in b14 and "captions only" in b14
    and "CONFIRMED by the source, not changed" in b14
    and "NAMED-ESCAPE construction against entry 48" in b14)
m = re.search(r"Testability: \*\*([A-Z-]+)\*\*", blocks[14])
chk("TIER UNCHANGED: entry 14 remains CONSISTENCY-ONLY (triage label now source-confirmed)",
    m is not None and m.group(1) == "CONSISTENCY-ONLY")
obs = set()
for n, b in blocks.items():
    mm = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b)
    if mm and mm.group(1) == "THEORETICAL-OBSTRUCTION": obs.add(n)
chk("CENSUS UNTOUCHED: the paper-level obstruction set is still exactly {22, 5}",
    obs == {22, 5})

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
