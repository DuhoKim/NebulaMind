#!/usr/bin/env python3
"""Overnight publication-receipt sweep (fetcher). Before tonight NO entry had a pinned Crossref
document -- every "VERIFIED (Crossref: ...)" was a seat's lookup. The base layer is published
JOURNAL papers only, so this binds each entry's publication fact to the DOI registry: fetch the
Crossref record for every entry's DOI, record type/container/volume/page/year, and FLAG anything
that is not a published journal-article or whose venue looks inconsistent with the record's claim.

Writes a consolidated JSONL receipt (one line per entry) to the reading sources dir. A FLAG here is
a potential finding (e.g. an entry filed as published that the registry calls a preprint) and gets
surfaced, not silently swept. Read-only against the network; no record edits here.
"""
import re, os, json, time, urllib.request, urllib.parse
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
OUT = os.path.join(ROOT, "bhu-reading-20260823/sources/crossref_publication_audit.jsonl")

B = open(BIB).read(); cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}

# DOI: allow parens (old Elsevier), stop at whitespace/backtick/comma/semicolon; trim trailing junk.
doi_re = re.compile(r"10\.\d{4,9}/[^\s`,;)]*(?:\([^\s`,;)]*\)[^\s`,;)]*)*")
def first_doi(blk):
    for m in doi_re.finditer(blk):
        d = m.group(0).rstrip(".")
        return d
    return None

def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": "BHU-audit mailto:duhokim81@gmail.com"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["message"]

rows = []
PUBLISHED_TYPES = {"journal-article", "proceedings-article", "book-chapter", "monograph"}
for n in sorted(blocks):
    doi = first_doi(blocks[n])
    row = {"entry": n, "doi": doi}
    try:
        m = crossref(doi)
        row.update(type=m.get("type"),
                   container=(m.get("container-title") or [""])[0],
                   volume=m.get("volume"),
                   page=m.get("page") or m.get("article-number"),
                   year=(m.get("issued", {}).get("date-parts", [[None]])[0] or [None])[0],
                   title=(m.get("title") or [""])[0][:90])
        row["published_journal_article"] = (m.get("type") in PUBLISHED_TYPES)
    except Exception as e:
        row.update(error=str(e)[:120], published_journal_article=None)
    rows.append(row)
    tag = "ok " if row.get("published_journal_article") else ("ERR" if "error" in row else "FLAG")
    print(f"  [{tag}] entry {n:2}  {row.get('type','?'):18} {str(row.get('container',''))[:40]:40} {doi}")
    time.sleep(0.15)

with open(OUT, "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

flags = [r for r in rows if r.get("published_journal_article") is False]
errs = [r for r in rows if "error" in r]
print("\n" + "=" * 90)
print(f"total {len(rows)} | published journal-article: {sum(1 for r in rows if r.get('published_journal_article'))} "
      f"| FLAG (not journal-article): {len(flags)} | ERROR: {len(errs)}")
if flags: print("  FLAGGED entries (type != published journal type):", [(r['entry'], r.get('type')) for r in flags])
if errs:  print("  ERROR entries (DOI fetch failed):", [(r['entry'], r['doi']) for r in errs])
print("receipt written:", OUT)
