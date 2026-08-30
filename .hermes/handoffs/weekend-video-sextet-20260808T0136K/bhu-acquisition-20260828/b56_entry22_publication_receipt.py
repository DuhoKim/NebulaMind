#!/usr/bin/env python3
"""B56 -- convert entry 22's PUBLICATION fact from a seat's testimony into a pinned receipt.
Self-computing (no seat gate: this binds authoritative DOI-registry metadata to a pinned document,
a deterministic value check).

ENTRY 22 = Easson, "Obstructions to Minimal Regular Black Hole Cosmologies" (arXiv 2606.25023),
THEORETICAL-OBSTRUCTION tier. Its paper text was pinned and read, but the PUBLICATION metadata
(PRD 114, 044077) rested only on "a seat's APS lookup, not a document in this corpus" -- and when
the entry was first written the Crossref deposit was still anonymized (no volume/article). It is no
longer: the Crossref DOI-registry record for 10.1103/qs86-npwk now carries the full bibliographic
data, saved 2026-08-30 as `crossref_10.1103_qs86-npwk_entry22.json`. This binds the publication
fact -- which matters because the base layer is published journal papers only -- to that pinned
authoritative document. No tier implication: confirming publication only strengthens inclusion.
"""
import os, json
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PIN = os.path.join(ROOT, "bhu-reading-20260823/sources/crossref_10.1103_qs86-npwk_entry22.json")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B56 -- entry 22 publication receipt (Crossref, pinned)"); print("=" * 98)

m = json.load(open(PIN))["message"]
title = (m.get("title") or [""])[0].lower()
authors = [((a.get("given", "") + " " + a.get("family", "")).strip()) for a in m.get("author", [])]
issued = m.get("issued", {}).get("date-parts", [[None]])[0]
chk("RECEIPT PARSES + IDENTITY: the pinned Crossref record is this exact Easson obstruction paper",
    "obstructions to minimal regular black hole cosmologies" in title
    and any("Easson" in a for a in authors))
chk("PUBLICATION BOUND: container=Physical Review D, volume 114, article 044077, APS journal-article",
    (m.get("container-title") or [""])[0] == "Physical Review D"
    and m.get("volume") == "114" and (m.get("article-number") or m.get("page")) == "044077"
    and m.get("type") == "journal-article")
chk("DATE BOUND: published 2026-08-24 (the publication date the seat's APS lookup had asserted)",
    issued[:3] == [2026, 8, 24])

B = open(BIB).read()
import re
cut = B.find("## Ranked:")
st = [(mm.start(), int(mm.group(1))) for mm in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b22 = " ".join(blocks[22].split())
chk("RECORD SUPERSEDES TESTIMONY: entry 22 now cites the pinned receipt (path+sha+b56) and the "
    "bound volume/article, replacing 'a seat's lookup' with a document",
    "RECEIPT PINNED 2026-08-30 (b56)" in b22
    and "crossref_10.1103_qs86-npwk_entry22.json" in b22
    and "volume 114, article 044077" in b22 and "54269cc6f8e6" in b22)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
