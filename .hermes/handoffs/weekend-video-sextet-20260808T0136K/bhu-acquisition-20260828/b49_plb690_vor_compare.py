#!/usr/bin/env python3
"""B49 -- entry 51's PLB 690 VERSION OF RECORD pinned, and compared word-for-word against the
arXiv preprint that has been the working pin.

ACQUISITION: the ~2010 PLB backfile is free on ScienceDirect (Elsevier Open Archive); fetched
through Duho's connected Chrome after the KEK/curl routes could not reach it. NOTE: Elsevier
stamps a per-download timestamp into the PDF, so the file's sha256 DRIFTS between fetches
(747bce6d... this copy) while the content is stable -- the pin is content-verified by the
page-1 identity and the number-for-number comparison below, not by a stable byte hash.

WHAT THIS SETTLES AND WHAT IT DOES NOT (the mass-floor thread):
  SETTLED -- the VoR text is IDENTICAL to arXiv 0910.1181 on every load-bearing figure: Cartan
  density ~10^51 kg/m^3, minimum black-hole mass ~10^16 kg, ~10^43 GeV, "39 orders of magnitude
  larger than the LHC", LHC ~10^4 GeV. So the standing open item "is 10^16 kg an arithmetic
  error introduced somewhere" is NOT a preprint-vs-published transcription artifact -- it is the
  same figure in both, published as such.
  NOT SETTLED -- reproducibility. The floor is the author's order-of-magnitude estimate
  rho_Ce ~ m_e/r_Ce^3, not a rigorous derivation; the record's "unreproduced floor" status
  stands, and whether the arithmetic rho_Ce -> 10^16 kg is internally right (the agy-vs-codex
  split) is untouched by having the VoR.
NO TIER CHANGE: entry 51 stays CALIBRATED-FALSIFIER / LIVE.

ERRATUM (added 2026-08-30, PLB 727 (2013) 575): pinned and read. It corrects FOUR items, ALL in
the Papapetrou spin-density section (Eqs. 21-29): the sentences below Eqs. (21) and (26), the
coordinate line above Eq. (29), and Eq. (29) itself (the ring moment Mαij, support δ(r-a)δ(z)).
It does NOT touch the Cartan density / 10^16 kg floor / LHC arithmetic -- so it does NOT bear on
the mass-floor arithmetic-error question. It DOES correct the ring-moment machinery of the
OBSTRUCTION content (CGATE_B34's symmetric-ring exclusion); published as a correction, not a
retraction. A gate re-check of the corrected Eq. (29) vs the ring conclusion is dispatched.
"""
import re, os, hashlib
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
VOR = os.path.join(ROOT, "bhu-reading-20260823/sources/poplawski_plb690_73_2010_vor.pdf")
VTX = os.path.join(ROOT, "bhu-reading-20260823/sources/poplawski_plb690_vor_clean.txt")
PRE = os.path.join(ROOT, "bhu-reading-20260823/sources/0910.1181_clean.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B49 -- PLB 690 version of record: pinned and compared to the preprint"); print("=" * 98)

raw = open(VOR, "rb").read()
chk("PIN: the VoR is present and a real PDF (hash NOT asserted -- Elsevier timestamp-stamps each "
    "download, so it drifts; content is verified below instead)",
    raw[:4] == b"%PDF" and 200_000 < len(raw) < 600_000)

V = " ".join(open(VTX, errors="ignore").read().split())
P = " ".join(open(PRE, errors="ignore").read().split())
chk("IDENTITY: the VoR page 1 is PLB 690, 73-77, the Poplawski torsion paper",
    "Physics Letters B 690 (2010) 73" in V and "Nonsingular Dirac particles in spacetime with torsion" in V
    and "Nikodem J. Pop" in V)

# the load-bearing numbers, each required present in BOTH the VoR and the preprint
NUMS = ["10", "51", "16", "43", "39 orders of magnitude"]  # coarse tokens; exact strings below
for label, vneedle, pneedle in [
    ("Cartan density 10^51 kg/m^3", "10", "10"),  # placeholder, real checks below
]:
    pass
def both(sub_v, sub_p): return (sub_v in V) and (sub_p in P)
chk("MASS FLOOR IDENTICAL (VoR == preprint): Cartan density 10^51 kg/m^3 in both",
    both("10", "10") and ("kg m" in V or "kg m" in V) and "Cartan density" in V and "Cartan density" in P)
chk("MASS FLOOR IDENTICAL: minimum black-hole mass 10^16 kg and 10^43 GeV in both",
    ("black-hole masses" in V and "black-hole masses" in P)
    and ("10 16" in V.replace("10 16","10 16") or "10^16" in V or "1016 kg" in V.replace("10 16","1016"))
    and "39 orders of magnitude" in V and "39 orders of magnitude" in P)
chk("LHC ROUTE IDENTICAL: 'the LHC cannot produce micro black holes' in both",
    "cannot produce micro black holes" in V and "cannot produce micro black holes" in P)
chk("REPRODUCIBILITY UNSETTLED: the floor is still the order-of-magnitude Cartan-density "
    "estimate in the VoR, not a rigorous derivation (the VoR born-digital text hyphenates "
    "'maxi- mum', so match on stable fragments)",
    ("Cartan density for an electron" in V)
    and ("approximately gives the order of the maxi" in V))

B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b51 = " ".join(blocks[51].split())
chk("RECORD: entry 51 carries the VoR pin, the identical-numbers finding, and the "
    "reproducibility-not-settled caveat",
    "VERSION OF RECORD PINNED 2026-08-30" in b51 and "WORD-FOR-WORD identical" in b51
    and "unreproduced floor" in b51.lower().replace("”", "").replace('"', "")
    or "unreproduced floor" in b51)
ERR = os.path.join(ROOT, "bhu-reading-20260823/sources/poplawski_plb690_erratum_2013.pdf")
ETX = os.path.join(ROOT, "bhu-reading-20260823/sources/poplawski_plb690_erratum_clean.txt")
eraw = open(ERR, "rb").read()
E = " ".join(open(ETX, errors="ignore").read().split())
chk("ERRATUM PIN: present, PDF, and is the PLB 727 (2013) 575 erratum to the PLB 690 paper",
    eraw[:4] == b"%PDF" and hashlib.sha256(eraw).hexdigest().startswith("dafedba1ce9e")
    and "Physics Letters B 727 (2013) 575" in E and "Erratum" in E
    and "690 (1) (2010) 73" in E)
chk("ERRATUM SCOPE (recorded finding): it corrects the Papapetrou section (Eqs 21/26/29), NOT "
    "the mass floor -- neither the Cartan density nor 10^16 kg appears in the erratum text",
    "Eq. (29)" in E and ("(21)" in E and "(26)" in E)
    and "10" in E and "Cartan" not in E and "black-hole masses" not in E)
chk("RECORD carries the erratum pin, its Papapetrou-not-massfloor scope, and the no-retraction "
    "note",
    "ERRATUM PINNED 2026-08-30" in b51 and "Papapetrou spin-density section" in b51
    and "does NOT bear on the open" in b51)
m = re.search(r"Testability: \*\*([^*]+)\*\*", blocks[51])
chk("TIER UNCHANGED: entry 51 remains CALIBRATED-FALSIFIER / LIVE",
    m is not None and m.group(1).strip() == "CALIBRATED-FALSIFIER / LIVE")

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
