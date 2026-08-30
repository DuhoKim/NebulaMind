#!/usr/bin/env python3
"""B42 -- byline sweep extended to the SUPPORT entries (29, 30, 32, 33, 34, 35, 58).

B40 verified the 39 readable BHU-paper records against their pinned artifacts; the seven support
entries (the measurement/mechanism papers the falsifiers import) were outside its scope and had
never been byline-checked. This closes the metadata layer over the whole 58-entry collection.

RESOLUTION HONESTY. Three resolution classes, printed per entry:
  RECORDED  -- the bibliography names the pin path (30, 34, 35, and 33 after today's acquisition);
               bound here by asserting the filename occurs in the entry's block.
  LOCATED   -- the record carries DOIs but no pin path (29, 58); the artifact was found by repo
               search and is tied to the record by an IDENTITY anchor asserted against its head
               (paper title / subject fragment), not just by the surname itself.
  SCAN      -- an image-only page scan (32, Brown & Bethe ApJ 423, 1994; REPAIRED 2026-08-30).
               The original NONE state (arXiv API found nothing -- pre-1995, never posted) was
               closed by fetching the NASA ADS classic scan (articles.adsabs.harvard.edu, direct,
               no verification wall on that route). The scan is the COMPLETE six-page article
               (659-664) with no article-content or OCR text layer -- only a 20-character
               ADS-bibcode overlay is extractable (CGATE_B42V2's narrowing) -- so surname
               containment cannot machine-check it; page 1 was rendered and read VISUALLY
               (2026-08-30, Tori): journal header "423:659-664, 1994 March 10", full title, and
               the byline "G. E. Brown and H. A. Bethe". The check below asserts the pin's
               existence, PDF magic, sha256, and the record's disclosure -- the byline fact
               itself is the recorded visual testimony, and the check says so. The old NONE
               state was deliberately never a chk, so this repair inverts nothing green (the
               1ab lesson applied at design time); the MEASURED predicate's none_entries
               assertion flips to empty in this same change.

ACQUISITION IN THIS CHANGE: entry 33's pair was located by journal-ref match in the arXiv API
(refs taken from the record, no ids from memory) and pinned: ar5iv_0010207.html (full text,
title + both bylines verified) and arxiv_0302103_abs.html (abs-page receipt; ar5iv 503s on the
233-page Phys.Rept.). The record edit and this check land together, so the check asserts the
REPAIRED state (both pins named in the block), never the gap.

CLAIM SHAPE, same as b40: one-way surname containment -- every recorded surname occurs with a
word boundary in the deaccented artifact text. NOT full-byline verification, NOT author-order,
NOT completeness of the artifact's author list against the journal's.
"""
import re, os, unicodedata
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

STROKED = str.maketrans({"ł": "l", "Ł": "L", "đ": "d", "Đ": "D", "ø": "o", "Ø": "O"})
def deacc(s):
    s = s.translate(STROKED)
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))

T = open(BIB).read(); cut = T.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", T[:cut], re.M)]
blocks = {n: T[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}

# entry -> (surnames, [(artifact, resolution, identity-anchor-or-None)])
E = {
    29: (["Demorest", "Fonseca"], [
        ("reviews/_tori_bhu_reverify_sources_20260811/arxiv_1010.5788v1_layout.txt", "LOCATED",
         "Shapiro delay measurement of a 2 solar mass"),
        ("bhu-reading-20260823/sources/2104.00880_clean.txt", "LOCATED",
         "Refined Mass and Geometric Measurements of the High-Mass PSR J0740+6620")]),
    30: (["Brown", "Lee", "Rho"], [
        ("bhu-theory-phase3-cns-20260821/sources/ar5iv_0708.3137.html", "RECORDED", None)]),
    32: (["Brown", "Bethe"], [
        ("bhu-theory-phase3-cns-20260821/sources/ads_1994ApJ_423_659_brown_bethe.pdf", "SCAN", None)]),
    33: (["Harada", "Yamawaki"], [
        ("bhu-theory-phase3-cns-20260821/sources/ar5iv_0010207.html", "RECORDED", None),
        ("bhu-theory-phase3-cns-20260821/sources/arxiv_0302103_abs.html", "RECORDED", None)]),
    34: (["Ferdman"], [
        ("bhu-theory-phase3-cns-20260821/sources/ar5iv_2007.04175.html", "RECORDED", None)]),
    35: (["Tauris"], [
        ("bhu-theory-phase3-cns-20260821/sources/ar5iv_1706.09438.html", "RECORDED", None)]),
    58: (["Longo"], [
        ("reviews/_tori_spin_prior_art_sources_20260811/arxiv_1104.2815v1_layout.txt", "LOCATED",
         "Detection of a Dipole in the Handedness of Spiral Galaxies")]),
}

print("=" * 98); print("B42 -- support-entry byline sweep"); print("=" * 98)

chk("BOUND: every hardcoded surname occurs in that entry's bibliography block",
    all(all(s in blocks[n] for s in sn) for n, (sn, _) in E.items()))
chk("BOUND: every RECORDED pin's filename is named in its entry's block",
    all(os.path.basename(a) in blocks[n]
        for n, (_, arts) in E.items() for a, res, _ in arts if res == "RECORDED"))

flags = []; checked = 0; none_entries = []; scan_ok = False
for n, (sn, arts) in sorted(E.items()):
    if not arts:
        none_entries.append(n)
        print(f"  {n:>3}  NONE      byline stays TESTIMONY")
        continue
    for a, res, anchor in arts:
        path = os.path.join(ROOT, a)
        if res == "SCAN":
            import hashlib
            raw = open(path, "rb").read()
            scan_ok = (raw[:4] == b"%PDF"
                       and hashlib.sha256(raw).hexdigest().startswith("4b1cbae677de"))
            print(f"  {n:>3}  {res:<9} {os.path.basename(a):<38} complete-article image scan; "
                  f"byline VISUAL per record (no article-content text layer -- disclosed)")
            continue
        body = deacc(open(path, errors="ignore").read())
        if anchor and anchor not in body[:4000]:
            flags.append((n, a, "IDENTITY-ANCHOR-MISSING")); continue
        missing = [s for s in sn if not re.search(r"(?<![A-Za-z])" + re.escape(deacc(s)) + r"(?![A-Za-z])", body)]
        # an artifact holding ONE paper of a pair need not name the other pair-member's authors;
        # here every surname set is per-ENTRY, so require each surname in >=1 of the entry's artifacts
        checked += 1
        print(f"  {n:>3}  {res:<9} {os.path.basename(a):<38} missing-here: {missing if missing else 'none'}")
for n, (sn, arts) in sorted(E.items()):
    texts = [a for a, res, _ in arts if res != "SCAN"]
    if not texts: continue
    bodies = [deacc(open(os.path.join(ROOT, a), errors="ignore").read()) for a in texts]
    for s in sn:
        if not any(re.search(r"(?<![A-Za-z])" + re.escape(deacc(s)) + r"(?![A-Za-z])", b) for b in bodies):
            flags.append((n, s, "SURNAME-IN-NO-ARTIFACT"))

chk("MEASURED: all 10 recorded surnames of the 6 TEXT-artifact-backed support entries occur in "
    "at least one of their entries' artifacts (8 text artifacts -- 29 and 33 are pairs), each "
    "identity-anchored or record-named -- one-way containment, per-entry across pairs",
    flags == [] and checked == 8 and none_entries == [],
    f"text artifacts checked: {checked}; flags: {flags if flags else 'none'}")
B2 = " ".join(open(BIB).read().split())     # 1ae: line wraps must not defeat the fragment
chk("SCAN RECEIPT (entry 32, repaired 2026-08-30): the ADS page scan is pinned (PDF magic + "
    "sha256 4b1cbae677de...), and the record discloses the complete-article scan and that its "
    "byline verification is VISUAL -- machine containment is impossible on an image and this "
    "check does not pretend otherwise",
    scan_ok and "ads_1994ApJ_423_659_brown_bethe.pdf" in B2
    and "byline checks are VISUAL" in B2
    and "COMPLETE article, pages 659–664" in B2)

print()
fails = [x for x, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
