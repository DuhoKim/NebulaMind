#!/usr/bin/env python3
"""B64 -- bind the reads of entries 3 (Stuckey 1994) and 18 (Dymnikova 1992), which Duho asked for
("read 3 and 18"). Both were previously tiered CONSISTENCY-ONLY from characterization/abstract only.
Self-computing (a benign tier CONFIRMATION, not a contested adjudication -> no seat gate).

ENTRY 18 = Dymnikova "Vacuum nonsingular black hole" (GRG 1992). The 1992 primary is paywalled, so
read via the author's own free content-identical restatement (arXiv gr-qc/0201058, pinned): it
CONSTRUCTS a family of globally regular de Sitter-Schwarzschild black holes (de Sitter core,
dominant energy condition, finite ADM mass) -- exhibits solutions, no no-go, no observational
discriminant -> CONSISTENCY-ONLY confirmed, full-content read (caveat: restatement, not 1992 bytes).

ENTRY 3 = Stuckey "The observable universe inside a black hole" (AJP 1994). Primary full text not
free-via-curl (RG login-walled, ADS unreachable, not on arXiv). Confirmed CONSISTENCY-ONLY from the
definitive abstract + pedagogical AJP nature (Friedmann dust embeds in Schwarzschild, null at
R_n=2GM/c^2) -- ABSTRACT-level, not a full-text read (flagged to Duho). Neither is a tier change.
"""
import re, os
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
DYM = os.path.join(ROOT, "bhu-reading-20260823/sources/ar5iv_gr-qc_0201058_dymnikova_restatement.html")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B64 -- entries 3 & 18 read (Duho: 'read 3 and 18')"); print("=" * 98)

chk("ENTRY 18 SOURCE PINNED: the Dymnikova free restatement (gr-qc/0201058) is a document in the corpus",
    os.path.exists(DYM) and "globally regular" in open(DYM, errors="ignore").read().lower())

B = open(BIB).read(); cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b18 = " ".join(blocks[18].split()); b3 = " ".join(blocks[3].split())

chk("ENTRY 18 READ RECORDED: full-content read via the pinned restatement, CONSISTENCY-ONLY confirmed",
    "READ 2026-08-30" in b18 and "gr-qc/0201058" in b18 and "710e36274fe0" in b18
    and "CONSISTENCY-ONLY CONFIRMED" in b18 and "globally regular" in b18)
chk("ENTRY 3 READ RECORDED: abstract-level confirmation with the R_n=2GM/c² embedding, honest caveat "
    "that it is NOT a full-text read",
    "READ (abstract-level) 2026-08-30" in b3 and "2GM/c" in b3
    and "CONSISTENCY-ONLY CONFIRMED" in b3 and "ABSTRACT-level" in b3)
chk("NO TIER CHANGE: both entries remain CONSISTENCY-ONLY (a confirmation, not a re-tier)",
    "**CONSISTENCY-ONLY**" in " ".join(blocks[18].split()) and "**CONSISTENCY-ONLY**" in " ".join(blocks[3].split()))

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
