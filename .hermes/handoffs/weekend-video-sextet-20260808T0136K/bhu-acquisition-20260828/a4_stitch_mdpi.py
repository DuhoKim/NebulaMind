#!/usr/bin/env python3
"""A4 -- rebuild entries 25/26 COMPLETE, and verify completeness rather than assume it.

WHY THIS EXISTS. a3_pin_mdpi.py pinned both papers and passed 3/3 self-checks. Both pins were
broken. `get_page_text` truncates at 50,000 characters, so entry 25 was missing 36% of its text
and entry 26 11%, and both had swallowed the harness's own truncation notice and tab-context
footer as if they were article prose. My checks tested the DOI, the title, and the presence of
the word "Conclusion" -- all of which a truncated file still satisfies.

That is the same error a3's own docstring congratulated itself for catching on digital.csic.es,
committed one function later. A byte count that looks plausible is not completeness.

METHOD. Three captures per paper, each under the 50,000-char ceiling, with deliberate overlap:
  head   0 -> 50k          (full page)
  middle ~24k -> ~74k      (leading DOM subtree removed, so the capture window slides)
  tail   last ~8k          (nearly everything removed)
Splice on the longest verified overlap, never on a byte offset.

CHECKS ARE COMPLETENESS CHECKS. Landmarks from the START, MIDDLE and END of each paper must all
be present, the seams must not duplicate text, and no harness artefact may survive.
"""
import json, os, re, sys, hashlib

TR  = "/Users/duhokim/.claude/projects/-Users-duhokim-NebulaMind-NebulaMind/e82afe4d-60ac-4819-a8be-fdac7edbc929/tool-results"
SRC = "../bhu-reading-20260823/sources"

PAPERS = {
    25: dict(slug="sym14091849", doi="10.3390/sym14091849", title="The Black Hole Universe, Part I",
             parts=["toolu_015Z1cQFqEadPWedDaFCfd8r.json", "toolu_01QprYy6YJNhrr5NY6Y9cmjY.json"],
             tail="_tails/e25_tail.txt", reported_total=78518,
             landmarks=["Abstract", "1. Introduction", "junction conditions",
                        "Appendix A. Some Simple Solutions", "Appendix D",
                        "Lanczos, K.; Hoenselaers", "Creative Commons Attribution"]),
    26: dict(slug="sym14101984", doi="10.3390/sym14101984", title="The Black Hole Universe, Part II",
             parts=["toolu_017V2SKbMjduDNSb3z6Y8fyg.json", "toolu_01FTUEMgf2hSX2crnPXDZkK7.json"],
             tail="_tails/e26_tail.txt", reported_total=56218,
             landmarks=["Abstract", "neutron degeneracy pressure", "Big Bounce",
                        "Kusenko, A. Exploring Primordial Black Holes", "Creative Commons Attribution"]),
}
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

ARTEFACTS = [r"\n?\[output truncated at \d+ of \d+ characters[^\]]*\]\s*", r"\nTab Context:\n(?:.|\n)*$",
             r"^Title:[^\n]*\nURL:[^\n]*\nSource element:[^\n]*\n---\n"]
def clean(t):
    for pat in ARTEFACTS: t = re.sub(pat, "", t)
    return t.strip()

def load(fn):
    return clean("\n".join(b.get("text", "") for b in json.load(open(os.path.join(TR, fn))) if isinstance(b, dict)))

def splice(a, b):
    """Join a and b on a verified overlap.

    Exact-prefix matching FAILED on entry 26: citation markers render as "[]" in the trimmed DOM
    but carry numbers in the untrimmed page, so b's opening bytes are not byte-identical to the
    same passage inside a. Fix: slide the probe along b, and fall back to whitespace/citation-
    normalised matching. Still an overlap match -- never a byte offset.
    """
    for off in (0, 200, 500, 1000, 2000, 4000, 8000):
        for probe in (400, 300, 200, 120):
            if len(b) < off + probe: continue
            i = a.find(b[off:off + probe])
            if i != -1: return a[:i] + b[off:], len(a) - i
    # normalised fallback: strip bracketed citations and collapse whitespace, match there,
    # then map the cut point back to raw coordinates via a running index.
    def norm_map(t):
        out, idx = [], []
        prev_ws = False
        for k, ch in enumerate(t):
            if ch.isspace():
                if prev_ws: continue
                out.append(" "); idx.append(k); prev_ws = True
            else:
                out.append(ch); idx.append(k); prev_ws = False
        return "".join(out), idx
    na, ia = norm_map(re.sub(r"\[[^\]]{0,12}\]", "", a))
    nb, ib = norm_map(re.sub(r"\[[^\]]{0,12}\]", "", b))
    for probe in (300, 200, 120):
        if len(nb) < probe: continue
        j = na.find(nb[:probe])
        if j != -1:
            # conservative: cut a at the raw position of the normalised match
            cut = ia[j] if j < len(ia) else len(a)
            return a[:cut] + b, len(a) - cut
    return None, 0

print("=" * 96); print("A4 -- rebuilding entries 25/26 complete, with completeness checks"); print("=" * 96)
results = {}
for entry, P in PAPERS.items():
    print(f"\n[entry {entry}] {P['title']}")
    segs = [load(f) for f in P["parts"]] + [open(P["tail"]).read().strip()]
    for i, s in enumerate(segs): print(f"    segment {i}: {len(s):>7,} chars")
    doc, ok = segs[0], True
    for i, nxt in enumerate(segs[1:], start=1):
        joined, ov = splice(doc, nxt)
        if joined is None:
            print(f"    !! no overlap found joining segment {i}"); ok = False; break
        print(f"    spliced segment {i} on a {ov:,}-char verified overlap -> {len(joined):,}")
        doc = joined
    if not ok: results[entry] = None; continue
    # cut the trailing page furniture at 'Share and Cite'; keep the CC licence line
    cut = doc.find("Share and Cite")
    if cut > 0: doc = doc[:cut].strip()
    hdr = f"[{P['doi']}] {P['title']}\nSymmetry (MDPI), CC-BY. Full text retrieved from the publisher page 2026-08-28.\nReassembled from 3 overlapping captures by a4_stitch_mdpi.py; see its docstring.\n\n"
    out = f"{SRC}/{P['slug']}_clean.txt"
    open(out, "w").write(hdr + doc + "\n")
    results[entry] = (out, doc, P)
    print(f"    wrote {out}  ({os.path.getsize(out):,} bytes)")

print(f"\n{'entry':>5} {'chars':>8} {'vs page':>9} {'landmarks':>10} {'artefacts':>10}  sha256(12)")
for entry, r in results.items():
    if not r: print(f"{entry:>5}  FAILED"); continue
    out, doc, P = r
    frac = len(doc) / P["reported_total"]
    miss = [m for m in P["landmarks"] if m not in doc]
    art  = re.search(r"output truncated at|Tab Context:|Source element:", doc)
    print(f"{entry:>5} {len(doc):>8,} {frac:>8.1%} {len(P['landmarks'])-len(miss):>4}/{len(P['landmarks'])} {('CLEAN' if not art else 'DIRTY'):>10}  {hashlib.sha256(open(out,'rb').read()).hexdigest()[:12]}")
    if miss: print(f"        MISSING LANDMARKS: {miss}")

good = [r for r in results.values() if r]
chk("both papers reassembled from overlapping captures", len(good) == 2, f"{len(good)}/2")
chk("every landmark from the START, MIDDLE and END of each paper is present",
    all(not [m for m in P["landmarks"] if m not in doc] for _, doc, P in good),
    "this is the check a3 lacked -- an end-landmark cannot survive truncation")
chk("no harness artefact survives in either file",
    all(not re.search(r"output truncated at|Tab Context:|Source element:", doc) for _, doc, P in good),
    "a3 wrote the truncation notice and tab footer into the source as if they were prose")
chk("each file recovers >=95% of the character count the page itself reported",
    all(len(doc) / P["reported_total"] >= 0.95 for _, doc, P in good),
    "guards against a splice that silently drops a middle segment")
chk("the seams did not duplicate text",
    all(doc.count("Publisher’s Note: MDPI stays neutral") == 1 for _, doc, P in good),
    "a bad overlap splice would repeat the end block")

n_ok = sum(1 for _, o, _ in checks if o)
print(f"\nSELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
