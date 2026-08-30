#!/usr/bin/env python3
"""B55 -- support entry 32 (Brown & Bethe, ApJ 423, 1994): the CLOSING entry of the support sweep,
and the one that CANNOT be text-bound. The pin is a 6-page image scan with NO article-content /
OCR text layer, so the load-bearing number (M_max ≃ 1.5 M_sun) is not machine-greppable. The
honest disposition, per the describe-vs-compute discipline: bind what is COMPUTABLE -- custody and
the truth of the image-only claim -- and do NOT assert the abstract numbers are verified from the
source (they are VISUALLY attested only, Tori page-1, 2026-08-30, as the record states).

Every assertion below is positive-durable (no `not in` / `== 0` / `is None`):
  1. CUSTODY: the pin exists, is a real PDF (%PDF magic), matches the recorded sha256 prefix, and
     is a 6-page document.
  2. IMAGE-ONLY CONFIRMED: the entire extractable text layer IS the ADS bibcode overlay
     "1994ApJ...423..659B" and nothing else (pypdf yields 114 chars, all bibcode) -- which is what
     makes the byline/number checks visual, exactly as the record discloses.
  3. RECORD HONEST: entry 32's record calls the pin an image scan, states the visual attestation,
     and carries the b55 sweep marker binding it by custody rather than by (impossible) text-grep.
"""
import re, os, hashlib
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PDF = os.path.join(ROOT, "bhu-theory-phase3-cns-20260821/sources/ads_1994ApJ_423_659_brown_bethe.pdf")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
BIBCODE = "1994ApJ...423..659B"

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B55 -- support entry 32 custody + image-only honesty"); print("=" * 98)

raw = open(PDF, "rb").read()
sha = hashlib.sha256(raw).hexdigest()
import pypdf
pages = pypdf.PdfReader(PDF).pages
text = "".join((p.extract_text() or "") for p in pages)
chk("CUSTODY: pin is a real 6-page PDF matching the recorded sha256 prefix 4b1cbae677de, tracked",
    raw[:4] == b"%PDF" and sha.startswith("4b1cbae677de") and len(pages) == 6)
chk("IMAGE-ONLY CONFIRMED: the whole extractable text layer IS the ADS bibcode overlay and nothing "
    "else -- which is why byline/number checks are visual (self-computing confirmation)",
    BIBCODE in text and text.replace(BIBCODE, "").strip() == "")

B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b32 = " ".join(blocks[32].split())
chk("RECORD HONEST: entry 32 calls the pin an image scan, states VISUAL verification, and carries "
    "the b55 marker binding by custody (never claiming the numbers are computed from the source)",
    "image scan" in b32 and "VISUAL" in b32
    and "b55 support sweep" in b32 and BIBCODE in b32)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
