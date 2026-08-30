#!/usr/bin/env python3
"""B45 -- entry 48 ACQUIRED (second free frontier, route 2: KEK scanned preprints) and READ IN
FULL. The proof-owner the entry-49 obstruction thread has waited for since CGATE_B30.

ACQUISITION RECEIPT. Duho's institutional login did not cover the backfiles; Blanc relayed the
five-route free-frontier directive at 12:54 KST. Route 2 landed on the first try: Inspire-HEP
record 234505 carries KEKSCAN 2000-36-705 and report number MIT-CTP-1400; the KEK scan-server
URL pattern for that id served a 6-page PDF directly (no login, no wall). Identity verified
visually on page 1: title "AN OBSTACLE TO CREATING A UNIVERSE IN THE LABORATORY", Edward Farhi
(MIT CTP) and Alan H. Guth (MIT CTP + Harvard-Smithsonian), "Submitted to: Physics Letters B",
CTP #1400, October 1986, and the KEK stamp matching the KEKSCAN id. CAVEAT, stated not buried:
this is the PREPRINT scan; the PLB 183, 149 VERSION OF RECORD remains unheld, and content
identity with the VoR is testimony until compared.

THE READ. All 6 scan pages (10 preprint pages including references) rendered at 130 dpi and
read VISUALLY page by page, 2026-08-30, Tori -- the OCR layer is noisy (stamps, marginalia,
garbled equations) and exists only for grep receipts (farhi_guth_mitctp1400_clean.txt, headered
as such).

RULE, unchanged from b28: does the paper PROVE that no member of a specified class of models
can satisfy a specified conjunction of conditions -- refutable by counterexample, not by
measurement?

VERDICT (mine, to the gate): **YES -- this is the corpus's cleanest specimen of a paper whose
OPERATIVE CONTRIBUTION IS the no-go derivation.** The title names the obstacle; the abstract
states the theorem; SS II proves it:
  no spacetime satisfies all of
    (a) asymptotically flat parent with well-defined noncompact Cauchy development;
    (b) T_uv k^u k^v >= 0 for all null k -- the paper's own "very weak energy condition"
        (the null EC; expressly WEAKER than the WEC our entry-49 testimony attributed, so the
        theorem is STRONGER than the corpus recorded);
    (c) a spherically symmetric false-vacuum region (part of de Sitter via the Birkhoff
        analogue) valid to some r > 1/chi, chi^2 = (8pi/3) G rho_f;
    (d) nonsingular initial data (no past-inextendible null geodesic).
  Proof owned in-text: theta_in = -(1/r)(1 - r^2 chi^2) and theta_out = 2/r computed from the
  tailored (r,v) coordinates, so 2-spheres with r > 1/chi are ANTI-TRAPPED; Penrose 1965
  [ref 7, PRL 14, 57] applied in its time-reversed anti-trapped form, hypotheses (noncompact
  Cauchy surface, null convergence, anti-trapped surface) individually verified for the
  laboratory class.

DELIMITATIONS THE AUTHORS STATE (recorded, not smoothed): the nonspherical case is UNDECIDED --
SS III derives only a NECESSARY avoidance condition (every constant-r 2-surface must carry a
point of negative theta_in despite the positive AVERAGE forced by Hartle-Wilkins + Gauss-Bonnet
once (1/r) int a dr > 4pi/3chi^2; "we have not succeeded in finding a geometry which has this
property", yet a "sufficiently weird bubble geometry" is not excluded); classical GR only --
quantum <T_uv> "will not in general obey" the condition (the named escape, pursued in entry
50); the white-hole footnote -- creation from a pre-existing white hole "is not excluded by our
arguments"; the compact-Cauchy extension is argued, not proven at the same rigor.

TIER: **NOT ASSIGNED HERE.** The shape is THEORETICAL-OBSTRUCTION under the adopted
ownership-of-proof convention, and the entry-49 -> 48 delegation chain is now source-confirmed.
But ANY tier change is Duho's under standing orders; the record carries "TIER PENDING DUHO
(question 8)" and OPEN_QUESTIONS_FOR_DUHO.md holds the question. The census frame extension
(readable 39 -> 40) likewise waits for that ruling; b41 v5 remains the closed-census record of
its frame.
"""
import re, os, hashlib
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PDF = os.path.join(ROOT, "bhu-reading-20260823/sources/farhi_guth_mitctp1400_kekscan_2000_36_705.pdf")
TXT = os.path.join(ROOT, "bhu-reading-20260823/sources/farhi_guth_mitctp1400_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B45 -- entry 48 acquired and read in full (KEK preprint scan)"); print("=" * 98)

raw = open(PDF, "rb").read()
chk("PIN: the KEK scan is present, PDF magic, sha256 573ff9751cec..., ~362 KB",
    raw[:4] == b"%PDF" and hashlib.sha256(raw).hexdigest().startswith("573ff9751cec")
    and 300_000 < len(raw) < 450_000)

S = " ".join(open(TXT, errors="ignore").read().split())
chk("OCR COMPANION: headered as noisy-OCR grep receipts with the PDF as pin of record",
    S.startswith("[OCR EXTRACTION") and "read VISUALLY" in S and "grep" in S.lower())
chk("IDENTITY LANDMARKS (OCR, noisy -- the VISUAL page-1 read is the identity receipt; the "
    "italic 'Physics Letters B' line is OCR-garbled and deliberately NOT asserted): title, "
    "both authors, 'Letters', CTP number",
    "OBSTACLE TO CREATING A UNIVERSE" in S and "Farhi" in S and "Guth" in S
    and "Letters" in S and "1400" in S)
chk("THEOREM LANDMARKS: the abstract's class-exclusion sentence, the null-EC condition, the "
    "anti-trapped construction and the Penrose attribution are all in the source text",
    "spherically symmetric false vacuum bubble" in S and "must have emerged from an initial singularity" in S
    and "for all null" in S and "anti-trapped" in S and "Penrose" in S)
chk("DELIMITATION LANDMARKS: the necessary-condition-only status of the nonspherical case and "
    "the quantum escape are in the source text",
    "necessary condition" in S and "quantum" in S)

B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b48 = " ".join(blocks[48].split())
chk("RECORD: entry 48 carries the read, the pin+sha, the preprint-not-VoR caveat, the theorem "
    "with the null-EC precision correction, and all four author-stated delimitations",
    "573ff9751cec" in b48 and "PREPRINT, not the PLB version of record" in b48
    and "very weak energy condition" in b48 and "WEAKER than the WEC" in b48
    and "NOT decided" in b48 and "white" in b48.lower()
    and "question 8" in b48
    # CGATE_B45's two repairs, asserted in their repaired state:
    and "secondary corroboration only" in b48
    and "PARENT need not be spherical" in b48)
m = re.search(r"Testability: \*\*([A-Z-]+)", blocks[48])
chk("TIER SET BY QUESTION 8 (2026-08-30, the delegated ruling -- NOT by this artifact, which "
    "held READ/pending until Duho returned the question): the marker now reads "
    "THEORETICAL-OBSTRUCTION with the basis and the revisit-on-VoR clause printed in the entry",
    m is not None and m.group(1) == "THEORETICAL-OBSTRUCTION"
    and "question 8" in b48 and "REVISITED" in b48)
obs = set()
for n, b in blocks.items():
    mm = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b)
    if mm and mm.group(1) == "THEORETICAL-OBSTRUCTION": obs.add(n)
chk("OBSTRUCTION SET CURRENT: {22, 5, 48} after the question-8 ruling",
    obs == {22, 5, 48})

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
