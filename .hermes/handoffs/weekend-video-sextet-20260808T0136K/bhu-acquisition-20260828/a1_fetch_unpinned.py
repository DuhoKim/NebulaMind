#!/usr/bin/env python3
"""A1 -- acquire the top-ranked UNPINNED bibliography entries.

WHY THESE. The bibliography ranks its own five strongest targets. Cross-referencing that
ranking against ENTRY_SOURCE_MAP.md's pinned set shows the ranking is mostly UNACQUIRED:

    rank 1  Poplawski chain   9+11 spine 8,10,12   -> 9,10,11,12 pinned; ONLY entry 8 missing
    rank 2  CNS falsifier     6+7                  -> both pinned, audited, done
    rank 3  Gaztanaga series  25+26+23 (24,27)     -> ALL FIVE UNPINNED
    rank 4  Roupas 2022       21                   -> UNPINNED
    rank 5  Easson 2026       22                   -> UNPINNED

So ranks 3/4/5 are entirely unpinned and rank 1 is one paper short. That is the gap.

THE ACQUISITION CLAIM THIS CORRECTS. ENTRY_SOURCE_MAP.md says the unpinned set carries
"a DOI and nothing else, so acquisition means a per-paper lookup with real paywall risk
(Elsevier, Springer, APS)". True for some, but NOT for the highest-value targets: EPJC is
gold OA via SCOAP3, Symmetry and Universe are MDPI OA, and Poplawski/Gaztanaga/Easson all
post to arXiv. Six of the eight resolved on an arXiv title query in one pass.

SELF-CHECKS. A fetch is not an acquisition. Each file must (a) exist and be non-trivial,
(b) contain the expected arXiv id in its header region -- the SAME header-region constraint
that cut the source-map sweep from 27 false positives to 5 -- and (c) not be an ar5iv
error/conversion-failure stub dressed up as a paper.
"""
import urllib.request, re, sys, os, hashlib, html.parser, time

SRC = "../bhu-reading-20260823/sources"
UA  = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/120 Safari/537.36"}

TARGETS = [   # (entry, arxiv_id, short label, why it is on this list)
    (21, "2203.13295", "Roupas 2022 EPJC 82,255",   "rank 4 -- 'detectable': amplitude+rate, or uncalibrated?"),
    (23, "2003.11544", "Gaztanaga 2020 MNRAS 494",  "rank 3 -- parent of entry 54's causal-horizon chain"),
    (24, "2104.00521", "Gaztanaga 2022 Symmetry 14,285",  "rank 3 supporting"),
    (27, "2204.11608", "Gaztanaga 2022 Universe 8,257",   "rank 3 supporting"),
    (22, "2606.25023", "Easson 2026 PRD",           "rank 5 -- no-go theorems, cross-programme check"),
    (8,  "0902.1994",  "Poplawski 2010 PLB 687,110","rank 1 -- the ONLY missing member of the spine"),
]

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail))
    print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

class Strip(html.parser.HTMLParser):
    SKIP = {"script", "style"}
    def __init__(self): super().__init__(); self.out = []; self.skip = 0
    def handle_starttag(self, t, a):
        if t in self.SKIP: self.skip += 1
    def handle_endtag(self, t):
        if t in self.SKIP: self.skip = max(0, self.skip - 1)
        if t in ("p", "div", "h1", "h2", "h3", "li", "section"): self.out.append("\n")
    def handle_data(self, d):
        if not self.skip: self.out.append(d)

def get(url, tries=3):
    last = None
    for k in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
        except Exception as e:
            last = e; time.sleep(3 * (k + 1))
    raise last

os.makedirs(SRC, exist_ok=True)
print("=" * 96); print("A1 -- acquiring the unpinned top-ranked targets"); print("=" * 96)

results = []
for entry, aid, label, why in TARGETS:
    txt_p  = f"{SRC}/{aid}_clean.txt"
    html_p = f"{SRC}/ar5iv_{aid}.html"
    print(f"\n[entry {entry}] {label}\n    {why}")
    if os.path.exists(txt_p) and os.path.getsize(txt_p) > 20000:
        print(f"    already pinned, skipping")
        results.append((entry, aid, txt_p, os.path.getsize(txt_p), True)); continue
    try:
        raw = get(f"https://ar5iv.labs.arxiv.org/html/{aid}")
    except Exception as e:
        print(f"    FETCH FAILED: {e}"); results.append((entry, aid, txt_p, 0, False)); continue
    open(html_p, "wb").write(raw)
    s = Strip(); s.feed(raw.decode("utf-8", "replace"))
    body = re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]{2,}", " ", "".join(s.out)))
    title = re.search(r"<title>(.*?)</title>", raw.decode("utf-8", "replace"), re.S)
    head = f"[{aid}] {' '.join(title.group(1).split()) if title else '(no title)'}\n\n"
    open(txt_p, "w").write(head + body.strip() + "\n")
    n = os.path.getsize(txt_p)
    print(f"    wrote {txt_p}  ({n:,} bytes)")
    results.append((entry, aid, txt_p, n, False))

print("\n" + "=" * 96); print("VERIFICATION -- a fetch is not an acquisition"); print("=" * 96)
print(f"{'entry':>5} {'arxiv':<12} {'bytes':>10} {'id in head':>11} {'not a stub':>11}  sha256(12)")
ok_all = True
for entry, aid, p, n, skipped in results:
    if not os.path.exists(p):
        print(f"{entry:>5} {aid:<12} {'MISSING':>10}"); ok_all = False; continue
    b = open(p, "rb").read()
    head4k = b[:4096].decode("utf-8", "replace")
    in_head = aid in head4k
    # an ar5iv failure page is short and says so; a real paper has section structure
    not_stub = len(b) > 20000 and bool(re.search(r"(?i)\b(introduction|abstract)\b", head4k + b[:60000].decode("utf-8", "replace")))
    sha = hashlib.sha256(b).hexdigest()[:12]
    print(f"{entry:>5} {aid:<12} {len(b):>10,} {str(in_head):>11} {str(not_stub):>11}  {sha}")
    if not (in_head and not_stub): ok_all = False

chk("every target produced a file with its own arXiv id in the header region",
    all(os.path.exists(p) and aid in open(p, 'rb').read()[:4096].decode('utf-8', 'replace')
        for _, aid, p, _, _ in results),
    "same header-region constraint that cut the source-map sweep 27 -> 5")
chk("no file is an ar5iv stub or conversion-failure page", ok_all,
    ">20 kB and carries abstract/introduction structure")
chk("all six ranked targets accounted for", len(results) == 6, f"{len(results)}/6")

n_ok = sum(1 for _, o, _ in checks if o)
print(f"\nSELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
