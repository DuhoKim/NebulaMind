#!/usr/bin/env python3
"""B66 -- bind the CORPUS SYNTHESIS MEMO to the record it synthesizes. Self-computing: the memo is
the durable deliverable, and receipts-discipline means its load-bearing figures must still match the
bibliography they were pulled from. This guards against a memo typo AND future source-drift (if a
tier or threshold changes in the record, this fails until the memo is updated).
"""
import re, os
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
MEMO = os.path.join(_HERE, "CORPUS_SYNTHESIS_MEMO_20260831.md")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B66 -- corpus synthesis memo bound to the record"); print("=" * 98)

memo = " ".join(open(MEMO, errors="ignore").read().split()) if os.path.exists(MEMO) else ""
bib = " ".join(open(BIB, errors="ignore").read().split())

chk("MEMO STRUCTURE: all four commissioned sections are present",
    "verdict structure" in memo and "live-falsifier ledger" in memo.lower()
    and "gated" in memo.lower() and "next falsifiers" in memo.lower())

# The five ledger figures, each must appear in the memo AND be corroborated in the record.
LEDGER = [
    ("entry 7 threshold", "2 M☉", "2 M☉"),
    ("entry 44 n_s", "0.9649", "0.9649"),
    ("entry 31 bar", "2.5 M☉", "2.5 M☉"),
    ("entry 51 floor", "10¹⁶ kg", "10¹⁶ kg"),
    ("entry 54 curvature", "0.0023", "0.0023"),
]
bad = [name for name, inmemo, inbib in LEDGER if inmemo not in memo or inbib not in bib]
chk("LEDGER FIGURES BOUND: every calibrated-falsifier + curvature threshold in the memo is "
    "corroborated verbatim in the bibliography",
    bad == [], f"unbound: {bad}" if bad else "")

# tier counts the memo asserts must match a live parse of the record
cut = bib.find("## Ranked:")
head = bib[:cut] if cut > 0 else bib
from collections import Counter
tiers = Counter()
raw = open(BIB).read(); rcut = raw.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", raw[:rcut], re.M)]
blocks = {n: raw[p:(st[i + 1][0] if i + 1 < len(st) else rcut)] for i, (p, n) in enumerate(st)}
for n in blocks:
    b = " ".join(blocks[n].split())
    t = re.search(r"Testability: \*\*([A-Z][A-Z /-]*[A-Z])\*\*", b)
    tiers[(t.group(1).split("/")[0].strip() if t else "support")] += 1
chk("TIER COUNTS MATCH: the memo's 32 consistency / 4 calibrated / 3 obstruction reflect the record (entries 27 + 42/47, 2026-09-01)",
    tiers["CONSISTENCY-ONLY"] == 32 and tiers["CALIBRATED-FALSIFIER"] == 4
    and tiers["THEORETICAL-OBSTRUCTION"] == 3
    and "CONSISTENCY-ONLY | 32" in memo and "entries 7, 31, 44, 51" in memo,
    f"record tiers={dict(tiers)}")

chk("RECEIPTS DISCIPLINE: the memo cites primary refs (Planck eq 19, Smolin §4, PRL 101 091101)",
    "eq (19)" in memo and "Smolin §4" in memo and "091101" in memo)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
