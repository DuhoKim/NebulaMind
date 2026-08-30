#!/usr/bin/env python3
"""B62 -- bind the B61 gate outcome: entry 54's curvature falsifier is LIVE but NOT FIRED, both
seats concur, tier unchanged. Self-computing (the seats already judged; this binds their concordant
NOT-FIRED verdict + the tension note in the record).

B61 (Duho: "point a gate at the curvature falsifier implication") followed B59's finding that DESI's
central Ω_k is open-side. Both seats independently re-extracted DESI DR2 Table 5 and verified the
sign convention: DESI+CMB Ω_K = +0.0023 ± 0.0011 (~2.1σ OPEN) is a hint, not a confirmed detection
(DESI: "no significant preference for a non-flat ΛCDM"); Planck combined is ~1.6σ CLOSED; ACT is
flat. Entry 54's condition ("a confirmed Ω_k > 0 refutes") is NOT met -> DOES-NOT-FIRE. Adverse
tension (the tightest constraint leans open, opposite the closed prediction) is recorded, but there
is NO tier/status change: entry 54 stays QUALITATIVE-DIRECTIONAL and LIVE.
"""
import re, os
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
LANE = _HERE
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B62 -- entry 54 curvature falsifier NOT FIRED, both seats concur"); print("=" * 98)

def first_line(p):
    return open(p, errors="ignore").readline().strip() if os.path.exists(p) else ""
agy = first_line(os.path.join(LANE, "AGATE_B61_VERDICT.md"))
cdx = first_line(os.path.join(LANE, "CGATE_B61_VERDICT.md"))
chk("BOTH SEATS NOT-FIRED: agy and codex both returned a CURVATURE_FALSIFIER_NOT_FIRED token",
    agy.startswith("CURVATURE_FALSIFIER_NOT_FIRED") and cdx.startswith("CURVATURE_FALSIFIER_NOT_FIRED"),
    f"agy={agy!r} codex={cdx!r}")

B = open(BIB).read(); cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}
b54 = " ".join(blocks[54].split())
chk("RECORD TENSION NOTE: entry 54 records the B61 result — DESI+CMB 0.0023 ± 0.0011 (~2.1σ open), "
    "LIVE but UNFIRED, not refuting",
    "B61-VERIFIED" in b54 and "0.0023" in b54 and "0.0011" in b54
    and "LIVE but" in b54 and "UNFIRED" in b54)
chk("NO TIER/STATUS CHANGE: the note states Tier UNCHANGED with both seats, and entry 54 remains "
    "QUALITATIVE-DIRECTIONAL",
    "Tier UNCHANGED (both seats)" in b54 and "QUALITATIVE-DIRECTIONAL" in b54)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
