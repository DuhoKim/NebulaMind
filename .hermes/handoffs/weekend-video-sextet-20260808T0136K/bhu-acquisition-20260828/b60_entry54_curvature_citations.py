#!/usr/bin/env python3
"""B60 -- bind the B59 gate outcome: entry 54's source overstates its ACT/DESI curvature support,
verified against primary sources by BOTH seats, tier unchanged. Self-computing (the seats already
judged; this binds their concordant verdict + the record clarification + the pinned abstracts).

B59 was the first seat gate of the overnight run (Duho: "point both seats and keep work with those
papers"). agy and codex INDEPENDENTLY returned the same token,
`SOURCE_OVERSTATES_ACT_DESI_TIER_UNCHANGED`: entry 54's bounce paper (2505.23877) glosses ACT DR6
and DESI as "same-direction positive-curvature" support, but ACT DR6 states "no departure from
spatial flatness", DESI 2024 VI is "consistent with flat ΛCDM", and DESI DR2 fits an Ω_k extension
and finds no significant non-flat preference (central Ω_k on the OPEN side). Only Di Valentino 2020
genuinely argues closed, and is cited accurately. Citation-accuracy clarification, NOT a tier change
-- entry 54 stays QUALITATIVE-DIRECTIONAL (the tier rests on the model's own prediction).
"""
import re, os
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
LANE = _HERE
SRC = os.path.join(ROOT, "bhu-reading-20260823/sources")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
TOKEN = "SOURCE_OVERSTATES_ACT_DESI_TIER_UNCHANGED"

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B60 -- entry 54 ACT/DESI citation fidelity, both seats concur"); print("=" * 98)

def first_line(p):
    return open(p, errors="ignore").readline().strip() if os.path.exists(p) else ""
agy = first_line(os.path.join(LANE, "AGATE_B59_VERDICT.md"))
cdx = first_line(os.path.join(LANE, "CGATE_B59_VERDICT.md"))
chk("BOTH SEATS CONCUR: agy and codex both returned the exact same B59 token",
    agy == TOKEN and cdx == TOKEN, f"agy={agy!r} codex={cdx!r}")

pins = ["arxiv_1911.02087_divalentino2020_closed_universe_natastron_abs.html",
        "arxiv_2404.03002_desi2024vi_bao_cosmology_abs.html",
        "arxiv_2503.14452_act_dr6_2025_power_spectra_abs.html"]
chk("PRIMARY ABSTRACTS PINNED: Di Valentino 2020, DESI 2024 VI, ACT DR6 are documents in the corpus",
    all(os.path.exists(os.path.join(SRC, p)) for p in pins))

B = open(BIB).read(); cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b54 = " ".join(blocks[54].split())
chk("RECORD CLARIFIED: entry 54 now carries the B59-VERIFIED primary-source finding "
    "(ACT 'no departure from spatial flatness', source OVERSTATES) superseding the bare testimony line",
    "B59-VERIFIED" in b54 and "no departure from spatial flatness" in b54 and "OVERSTATES" in b54)
chk("TIER PRESERVED + FRAMED: the clarification states it is NOT a tier change and both seats concur, "
    "and entry 54 remains QUALITATIVE-DIRECTIONAL",
    "citation-accuracy clarification, NOT a tier change" in b54
    and "both seats concur" in b54 and "QUALITATIVE-DIRECTIONAL" in b54)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
