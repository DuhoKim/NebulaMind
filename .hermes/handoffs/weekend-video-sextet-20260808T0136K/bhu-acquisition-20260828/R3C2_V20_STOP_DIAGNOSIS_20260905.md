# R3C2 — STOP at V20 under the lane's own cap: diagnosis and what is left (2026-09-05 22:08 KST)

**Status:** R3C2 is at **V20** (master `e8ba4a7438d61f02`, commit 4a3e42096). NOT frozen, NOT run. The lane has stopped design
churn by the cap it wrote into §10.14: "if V20's gate returns new non-escalated findings, the lane stops and files a diagnosis
instead of a V21." V20's gate returned four such items, all small, so this is that file. No tier, warrant, standing or stamp
moved. Nothing outward. Paper HOLD.

## 1. What the four gate rounds since Duho's 18:52 ruling established

| version | codex | kimi | leak line (both) | new non-escalated findings |
|---|---|---|---|---|
| V17 | UNSOUND | SOUND_WITH_REPAIRS | codex NONE; kimi "content-level only" (the accepted floor) | 4 + 4 |
| V18 | UNSOUND | SOUND_WITH_REPAIRS | NONE / NONE | 1 + 7 |
| V19 | UNSOUND | SOUND_WITH_REPAIRS | NONE / NONE | 2 + 5 |
| V20 | UNSOUND | SOUND_WITH_REPAIRS | NONE / NONE, kimi ORIGIN_PURPOSE=CANNOT_STATE | 2 + 3 |

Every codex UNSOUND from V18 on rests on the two items reserved to Duho. Both seats said CONSEQUENCE_VISIBLE=NO every round.
The ruling "hide the comparison, keep the taxonomy" did what it was meant to do: the seat can tell provenance is recorded and
checked, and cannot tell what it is compared with. C0 (two seats) passed at V17, V18, V19 and V20 with every verdict reachable.

## 2. Why stop rather than V21

The new findings are shrinking and are now of the kind a repair round produces rather than removes: one is a leftover of my own
five-counts edit ("print those four declared counts"), one asks that an infrastructure script be pinned or disclaimed, one names
the rounding convention at an exact midpoint, two are cosmetic. A V21 would fix these and, on the evidence of four rounds,
return a further two or three of the same size. The document cannot be frozen anyway until Duho rules on the split class.
So the right move is his rulings first, then **one** final version that applies the rulings and every pending small item
together, and one final C0 + gate.

## 3. Pending items, exact

**Duho's (unchanged since 19:48 KST):**
1. The class for a surviving per-claim outcome split — (a) add `CENSUS_OUTCOME_DISPUTED` after DENOMINATOR_DISPUTED
   [recommended by both engines and by me]; (b) widen DENOMINATOR_DISPUTED; (c) file as PARTIAL. Sub-option: "zero → PARTIAL"
   (a zero-denominator census files PARTIAL, not a vacuous COMPLETE).
2. The rename `REPRO_EXACT` → `REPRO_WITHIN_STATED_PRECISION` (and `DERIVED_ONLY` → a name that says STANDARD/MEASURED
   roots count as derived), asked by both engines every round since V10 — "rename", "rename both", or "keep".

**Small, ready to apply with the rulings (V21, one pass):**
- codex V20 D2: "print those four declared counts" → the five, named.
- codex V20 D4: the third-seat dispatcher — either pin `nm_referee_dispatch.sh` beside the master, or state that third-seat
  dispatch is an administrative action not claimed executable from the packet (my recommendation: the latter; it is
  infrastructure, and pinning a HermesOps script into a lane document invites drift).
- kimi V20 D3: rounding half away from zero at an exact midpoint.
- kimi V20 D4/D5: cosmetic (C2's artefact sentence; a "so" compression in §7).

**Still Duho's after all that:** whether R3C2 RUNS. It has not run; it will not without his word.

## 4. What the seat machinery now guarantees (for the check sheet, when written)

Seats see: the task, the taxonomy, the tools, the manifest; not the comparison, not the custody chain, not the history.
Builder-asserted forbidden list + machine-matched quotations + two independent seats + disputes carried + C6 audit with a printed
MATCH/MISMATCH artefact + two-receipt seal. Tools: seat `r3c2_ledger_tools.py` `8e286817…` (validate, census, census final);
lane `r3c2_lane_tools.py` `2aa1ea7d…` (merge with origin and parent disputes, compute); wrapper `fbb9bef7…`; builder
`f2f6c9ab…`. All controls pass in their positive and negative forms.

## 5. Disclosed process error today
The first V18 apply (commit dc884c637) lacked abort guards and dispatched C0 seats on a half-applied master; both stopped within
a minute, output archived unread. Recorded in §10.12 and the run log; the lesson is in memory.

R3C2_V20_STOP_DIAGNOSIS_COMPLETE
