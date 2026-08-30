#!/usr/bin/env python3
"""B53 -- support entry 33 content bound to source: the vector-manifestation (VM) prediction that
link (1) of entry 7's CNS falsifier chain imports. Self-computing string-presence (no seat gate).

ENTRY 33 = the Harada-Yamawaki "vector manifestation" pair: PRL 86, 757 (2001) = hep-ph/0010207
and Phys. Rept. 381 (2003). The Phase-3 Track-A audit marked this falsifier link B-2 as
ASSUMED-FROM-CITATION -- the chain leaned on it without the auditor having found the prediction in
the source. Entry 33's record had verified only the PRL's title and bylines in the pinned ar5iv
body, not the claim. This binds the CLAIM: the hidden-local-symmetry (HLS) prediction that the
gauge coupling VANISHES near chiral restoration -- Harada & Yamawaki's "vector manifestation."

Money quote located in the pinned PRL body (`ar5iv_0010207.html`, tag-normalized):
  "... gauge coupling approaching to zero: g^2(Lambda_f, N_f) = ..."
plus the VM named and the "bare HLS gauge coupling" defined. A FAILURE here -- the source NOT
containing the VM/vanishing-coupling prediction -- would undermine link (1) of entry 7's chain and
is a STOP-for-Duho item. It does contain it: benign confirmation, no chain change.
"""
import re, os, html
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PRL = os.path.join(ROOT, "bhu-theory-phase3-cns-20260821/sources/ar5iv_0010207.html")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

def norm(path):
    t = open(path, errors="ignore").read()
    t = re.sub(r"<[^>]+>", " ", t)
    return " ".join(html.unescape(t).split())

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B53 -- support entry 33 content bound to source"); print("=" * 98)

S = norm(PRL)
chk("IDENTITY: pinned PRL source is the Harada & Yamawaki vector-manifestation paper",
    "Harada" in S and "Yamawaki" in S and "vector manifestation" in S.lower())
chk("VM NAMED: the source presents the 'vector manifestation' of chiral symmetry",
    "vector manifestation" in S.lower() and "chiral" in S.lower())
chk("LOAD-BEARING CLAIM: the source states the HLS gauge coupling VANISHES toward the critical "
    "point -- 'gauge coupling approaching to zero' -- and defines the 'bare HLS gauge coupling'",
    "gauge coupling approaching to zero" in S.lower() and "hls gauge coupling" in S.lower())

B = open(BIB).read()
cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b33 = " ".join(blocks[33].split())
chk("RECORD MATCHES: entry 33 attributes exactly this VM/gauge-coupling-vanishes prediction, "
    "pins hep-ph/0010207, and now records it CONTENT-bound (not title/byline-only)",
    "gauge coupling vanishes near chiral restoration" in b33
    and "hep-ph/0010207" in b33 and "b53" in b33)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
