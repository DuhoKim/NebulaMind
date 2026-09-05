#!/usr/bin/env python3
"""STAGED, NOT APPLIED until kimi's V10 list is in. Leak-first edits for R3C2 V11 (Duho 14:31: strip consequence,
not just content). Each edit: exact anchor -> replacement; asserts count==1; stops on any miss."""
import io,sys
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read()
E=[
 # C0: stake language -> neutral, and the two-seat procedure replacing "verified by Tori"
 ("— and for **any condition whose failure would refute this lane's own expectation** — ",
  "— and for **every declared condition** — "),
 ("**The exhibitions are authored by a seat and only\n  verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the author does\n  not decide it.",
  "**The exhibition is authored independently by one pattern-blind seat and independently verified by a second\n  pattern-blind seat; both must return `C0_REACHABILITY=PASS`. The lane owner checks only that every declared outcome\n  and condition has a row and does not judge reachability.**"),
 # C6: consequence language -> neutral
 ("**(i) every claim whose filed\n  outcome asserts that the arithmetic reproduced the number** — the class in which a result unreproduced from the stated inputs is both consequential\n  and invisible, so it gets no sampling discount — and **(ii)",
  "**(i) every claim in the arithmetic group** — no sampling discount — and **(ii)"),
 ("outside this lane supplies a seed generated independently and unavailable to Tori before that receipt**",
  "outside this lane supplies a seed generated independently and unavailable to the lane before that receipt**"),
 ("  *(Seeding from the tally's own digest let the tally's producer reshape non-semantic content — ordering, spacing,\n  metadata — until a favourable sample appeared. A seed must not be a function of the thing being audited.)*",
  "  <!--SEAT-REDACT-->*(Seeding from the tally's own digest let the tally's producer reshape non-semantic content — ordering, spacing,\n  metadata — until a favourable sample appeared. A seed must not be a function of the thing being audited.)*<!--/SEAT-REDACT-->"),
 ("verified by Tori after the run and not on the seat's","verified by the lane owner after the run and not on the seat's"),
 ("Tori re-runs every script","the lane owner re-runs every script"),
]
for o,n in E:
    c=s.count(o); assert c==1, f"anchor count {c}: {o[:70]!r}"
    s=s.replace(o,n); print("  - leak edit ok:",o[:60].replace("\n"," "))
io.open(p,'w',encoding='utf-8').write(s); print("leak-first edits applied")
