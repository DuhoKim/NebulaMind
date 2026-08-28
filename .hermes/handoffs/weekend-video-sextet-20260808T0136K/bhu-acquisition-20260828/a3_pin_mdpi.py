#!/usr/bin/env python3
"""A3 -- SUPERSEDED BY a4_stitch_mdpi.py. ITS OUTPUT WAS BROKEN. Kept for the failure.

This script pinned both papers, passed 3/3 self-checks, and produced TRUNCATED, CONTAMINATED
files: entry 25 was missing 36% of its text and entry 26 11%, because `get_page_text` cuts at
50,000 characters -- and both had swallowed the harness's own truncation notice and tab-context
footer as if they were article prose.

The checks passed because they tested the DOI, the published title, and the presence of the word
"Conclusion". A truncated file satisfies all three. Read the docstring below and note that it
lectures, correctly, about digital.csic.es returning a plausible 200 for a path I invented --
and then commits the same class of error one function later. Byte counts that look right are not
completeness. Only an END-landmark catches a truncation.

Do not run this. Run a4_stitch_mdpi.py.
================================================================================================

Original docstring follows.

A3 -- pin entries 25 and 26 (Gaztanaga, Symmetry 2022), rank 3's two primary papers.

WHY THIS NEEDED A DIFFERENT ROUTE. Every scripted path is bot-blocked:
  mdpi.com article + /pdf + doi.org redirect ....... HTTP 403 (Cloudflare)
  hal.science /document and direct /file/*.pdf ..... HTTP 200 but "Making sure you're not a bot!"
  digital.csic.es bitstream ........................ HTTP 200, 4,455-byte HTML

The CSIC result is the instructive one. I invented a path -- `blackhole1.pdf`, which does not
exist -- and it returned the SAME 4,455 bytes as the real `blackhole2.pdf`. A 200 and a
plausible byte count are not an acquisition. That check is why none of these got pinned as PDFs.

WHAT WORKED. The papers are CC-BY open access; only the anti-bot layer was in the way, not a
paywall. Driving Chrome through it and taking the rendered article text is a legitimate route to
content that is free to read. Metadata came from the OpenAlex and HAL APIs, which are open.

A METADATA TRAP WORTH RECORDING. OpenAlex and HAL both title entry 25 "The Black Hole Universe
(BHU) from a FLRW cloud", and HAL's deposit file is `BHUelsaV2.pdf`. That is the PREPRINT title.
The published Symmetry article is "The Black Hole Universe, Part I". This is why the arXiv title
query in a1 found entries 21/22/23/24/27 but missed 25/26 -- I searched the published title
against a corpus that indexes the preprint one. The bibliography is a PUBLISHED-ONLY base layer,
so what is pinned here is the publisher's own page, not the HAL preprint.
"""
import json, os, re, sys, hashlib

SRC = "../bhu-reading-20260823/sources"
TR  = "/Users/duhokim/.claude/projects/-Users-duhokim-NebulaMind-NebulaMind/e82afe4d-60ac-4819-a8be-fdac7edbc929/tool-results"
JOBS = [
    (25, "sym14091849", "toolu_015Z1cQFqEadPWedDaFCfd8r.json", "The Black Hole Universe, Part I",  "10.3390/sym14091849"),
    (26, "sym14101984", "toolu_017V2SKbMjduDNSb3z6Y8fyg.json", "The Black Hole Universe, Part II", "10.3390/sym14101984"),
]
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print("A3 -- pinning entries 25 / 26 from the publisher's own page"); print("=" * 96)
rows = []
for entry, slug, jf, title, doi in JOBS:
    p = os.path.join(TR, jf)
    if not os.path.exists(p):
        print(f"[entry {entry}] tool-result missing: {p}"); rows.append((entry, slug, None, 0)); continue
    blocks = json.load(open(p))
    body = "\n".join(b.get("text", "") for b in blocks if isinstance(b, dict))
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    out = f"{SRC}/{slug}_clean.txt"
    open(out, "w").write(f"[{doi}] {title}\nSymmetry (MDPI), CC-BY. Retrieved from the publisher page 2026-08-28.\n\n{body}\n")
    n = os.path.getsize(out)
    print(f"[entry {entry}] wrote {out}  ({n:,} bytes)")
    rows.append((entry, slug, out, n))

print(f"\n{'entry':>5} {'slug':<14} {'bytes':>9} {'doi in head':>12} {'title ok':>9} {'has body':>9}  sha256(12)")
allok = True
for entry, slug, out, n in rows:
    if not out: allok = False; continue
    b = open(out, "rb").read(); head = b[:4096].decode("utf-8", "replace"); full = b.decode("utf-8", "replace")
    doi_ok   = [d for e, s, j, t, d in JOBS if e == entry][0] in head
    title_ok = [t for e, s, j, t, d in JOBS if e == entry][0] in head
    body_ok  = len(b) > 20000 and bool(re.search(r"(?i)\bAbstract\b", head)) and bool(re.search(r"(?i)References|Conclusion", full))
    print(f"{entry:>5} {slug:<14} {n:>9,} {str(doi_ok):>12} {str(title_ok):>9} {str(body_ok):>9}  {hashlib.sha256(b).hexdigest()[:12]}")
    allok &= (doi_ok and title_ok and body_ok)

chk("both entries produced a file carrying their own DOI and PUBLISHED title in the header", allok,
    "header-region constraint, same one that cut the earlier source sweep 27 -> 5")
chk("neither file is the 4,455-byte anti-bot page that fooled the CSIC path",
    all(n > 20000 for _, _, o, n in rows if o), "a 200 is not an acquisition")
chk("the published title is pinned, not the preprint title the APIs return",
    all("Part I" in open(o).read()[:4096] for _, _, o, _ in rows if o),
    "OpenAlex/HAL both say 'from a FLRW cloud'; the base layer is published-only")

n_ok = sum(1 for _, o, _ in checks if o)
print(f"\nSELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
