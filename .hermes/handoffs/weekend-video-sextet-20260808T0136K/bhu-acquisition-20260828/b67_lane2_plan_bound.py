#!/usr/bin/env python3
"""B67 -- bind the BHU Lane 2 research plan to the corpus it is seeded from.

Self-computing. The plan (BHU_LANE2_RESEARCH_PLAN_20260831.md) is a decision packet Duho picks from,
so its load-bearing corpus facts must still match the record: tier counts, the four calibrated
falsifiers and their FIRED/LIVE split, the candidate-entry tiers, and the gated trio's status. This
FAILS the moment a future tier change (e.g. when a Lane-2 RQ is pursued and an entry is re-tiered)
makes the plan stale -- forcing the plan to be updated rather than drifting silently. Same discipline
as b66 for the synthesis memo. Every predicate is computed from a live parse of the record, never a
literal.
"""
import re, os
from collections import Counter
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(_HERE, ".."))
PLAN = os.path.join(_HERE, "BHU_LANE2_RESEARCH_PLAN_20260831.md")
BIB = os.path.join(ROOT, "bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")

checks = []
def chk(n, p, d=""):
    if not isinstance(p, bool): raise TypeError("chk needs a computed predicate")
    checks.append((n, p, d)); print(("PASS " if p else "FAIL ") + n + ("  -- " + d if d else ""))

print("=" * 98); print("B67 -- BHU Lane 2 plan bound to the corpus"); print("=" * 98)

plan = " ".join(open(PLAN, errors="ignore").read().split()) if os.path.exists(PLAN) else ""
bibraw = open(BIB, errors="ignore").read()
bib = " ".join(bibraw.split())

# --- parse the record's entry blocks + tiers (same method as b66) ---
rcut = bibraw.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", bibraw[:rcut], re.M)]
blocks = {n: bibraw[p:(st[i + 1][0] if i + 1 < len(st) else rcut)] for i, (p, n) in enumerate(st)}
tiers = Counter(); tier_of = {}
for n in blocks:
    b = " ".join(blocks[n].split())
    t = re.search(r"Testability: \*\*([A-Z][A-Z /-]*[A-Z])\*\*", b)
    base = t.group(1).split("/")[0].strip() if t else "support"
    tiers[base] += 1; tier_of[n] = base

# 1. structure -- the five RQ cards + gated-trio + recommendation
chk("PLAN STRUCTURE: five RQ cards + gated-trio + recommendation present",
    all(s in plan for s in ["RQ-A", "RQ-B", "RQ-C", "RQ-D", "RQ-E"])
    and "gated trio" in plan.lower() and "Recommendation & sequencing" in plan)

# 2. tier counts the plan prints must match a live parse of the record
chk("TIER COUNTS MATCH: plan's 32/8/4/3 reflect the record (entries 27 + 42/47, 2026-09-01)",
    tiers["CONSISTENCY-ONLY"] == 32 and tiers["QUALITATIVE-DIRECTIONAL"] == 8
    and tiers["CALIBRATED-FALSIFIER"] == 4 and tiers["THEORETICAL-OBSTRUCTION"] == 3
    and "32 consistency-only" in plan and "4 calibrated-falsifier" in plan,
    f"record={dict(tiers)}")

# 3. the calibrated four + their FIRED/LIVE split, computed from the entry blocks
calibrated = sorted(n for n in tier_of if tier_of[n] == "CALIBRATED-FALSIFIER")
chk("CALIBRATED SET is {7,31,44,51}",
    calibrated == [7, 31, 44, 51], f"calibrated={calibrated}")
# authoritative FIRED/LIVE: the §0 standing-table rows, cross-checked against the §0 summary line.
# (Scanning entry BODIES is unsound -- they mention other entries' statuses; b67's own first defect.)
tbl = {int(m.group(1)): m.group(2) for m in
       re.finditer(r"\|\s*(\d+)\s*\|\s*CALIBRATED-FALSIFIER\s*\|\s*\*\*(FIRED|LIVE)\*\*", bibraw)}
fired = sorted(n for n, s in tbl.items() if s == "FIRED")
live = sorted(n for n, s in tbl.items() if s == "LIVE")
sm = re.search(r"FIRED\D+?([\d,\s]+?);\s*\d+\s*LIVE\D+?([\d,\s]+?)\)", bib)
fired_sum = sorted(int(x) for x in re.findall(r"\d+", sm.group(1))) if sm else []
live_sum = sorted(int(x) for x in re.findall(r"\d+", sm.group(2))) if sm else []
chk("FIRED/LIVE SPLIT: standing table AND §0 summary agree (7,44 FIRED / 31,51 LIVE); plan says two live",
    fired == [7, 44] and live == [31, 51] and fired_sum == [7, 44] and live_sum == [31, 51]
    and "live calibrated falsifiers (31 and 51)" in plan,
    f"table:{fired}/{live} summary:{fired_sum}/{live_sum}")

# 4. candidate-entry tiers the plan leans on (the seedbed)
chk("CANDIDATES: entry 21 PROSPECT, 22 THEORETICAL-OBSTRUCTION -- as the plan uses them",
    tier_of.get(21) == "PROSPECT" and tier_of.get(22) == "THEORETICAL-OBSTRUCTION"
    and "entry 21" in plan and "entry 22" in plan and "entry 58" in plan,
    f"tier(21)={tier_of.get(21)} tier(22)={tier_of.get(22)} tier(58)={tier_of.get(58)}")

# 5. corpus fully read -- 42 & 47 read 2026-09-01; no UNREAD entries remain (plan's gated list 2/42/47 is historical)
unread = sorted(n for n in tier_of if tier_of[n] == "UNREAD")
chk("FULLY READ: no UNREAD entries remain (42/47 read 2026-09-01); plan's historical gated list 2/42/47 present",
    unread == [] and "2/42/47" in plan, f"unread={unread}")

# 6. the live-falsifier figures the plan leans on are bound in the record too
chk("FALSIFIER FIGURES BOUND: 2.5 M and 2.35 appear in BOTH plan and record",
    "2.5 M" in plan and "2.5 M" in bib and "2.35" in plan and "2.35" in bib)

print()
fails = [n for n, p, _ in checks if not p]
print(f"{len(checks) - len(fails)}/{len(checks)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
