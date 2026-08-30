#!/usr/bin/env python3
"""B65 -- overnight research: bind entry 1 (Pathria 1972) to its pinned Nature abstract,
CONSISTENCY-ONLY confirmed. Self-computing (a benign tier confirmation, not a re-tier -> no seat).

Entry 1 was tiered CONSISTENCY-ONLY from characterization. The full Nature 1972 body is paywalled
and not freely obtainable (not on arXiv/INSPIRE; ADS unreachable from the agent context), but the
Nature ABSTRACT is pinned + git-tracked (`reviews/.../pathria-nature.txt`) and independently
audited. It asserts a closed universe that "may also be a black hole, confined to a localized region
of space which cannot expand" -- a bounded closed-universe-inside-a-BH construction: no no-go, no
distinguishing observational statistic. So CONSISTENCY-ONLY holds at the abstract level (full-text
read still needs the browser/ILL). Same abstract-level treatment given to entry 3.
"""
import re, os
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PATH = os.path.join(ROOT, "reviews/bhu-citation-custody-evidence-20260811/pathria-nature.txt")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B65 -- entry 1 (Pathria) abstract-confirmed CONSISTENCY-ONLY"); print("=" * 98)

src = " ".join(open(PATH, errors="ignore").read().split()) if os.path.exists(PATH) else ""
chk("SOURCE PINNED: the Nature abstract page is present and states the closed-universe-in-a-BH claim",
    os.path.exists(PATH) and "closed" in src.lower()
    and ("black hole" in src.lower()) and "cannot expand" in src.lower())

B = open(BIB).read(); cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b1 = " ".join(blocks[1].split())
chk("RECORD: entry 1 now records the abstract-level read (pinned source + audit) with the honest "
    "not-a-full-text-read caveat, CONSISTENCY-ONLY confirmed",
    "READ (abstract-level) 2026-08-31" in b1 and "pathria-nature.txt" in b1
    and "CONSISTENCY-ONLY CONFIRMED" in b1 and "abstract-level, not a full-text read" in b1)
chk("NO TIER CHANGE: entry 1 remains CONSISTENCY-ONLY",
    "**CONSISTENCY-ONLY**" in " ".join(blocks[1].split()))

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
