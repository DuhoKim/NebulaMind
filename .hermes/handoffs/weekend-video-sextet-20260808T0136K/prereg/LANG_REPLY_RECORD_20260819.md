# Dustin Lang's reply — 2026-08-19 22:41 KST (filed 2026-08-20 00:0x)

Verbatim, the load-bearing lines:
> "Rongpu Zhou is once again producing the photo-z values for DR11. I asked for his timeline on
> Monday and he said 'It should be ready in 2 weeks, and optimistically by the end of this
> week.'"
> "I believe the remaining DataLab tables will follow soon"
> "DR11 does include the DR10.1 sub-blob fix."

## What this closes (the 08-17 open questions)

- Q2 (sub-blob fix in DR11): **answered YES, from the source.** The 08-16 assumption we refused
  to freeze ("the pipeline presumably carried the fix") is now a stated fact from the data team.
- Q3 (ls_dr11.photo_z timeline): **~2 weeks, optimistically this week** (Rongpu Zhou producing);
  remaining Data Lab tables to follow.

## What this changes about the running campaign: NOTHING

DR10.1 remains the operative release per the frozen `DR10_1_RETAINED_DECISION_20260817.md`; the
transfer executes under the frozen successor binding and completes on DR10.1. A DR11 migration
is a POSSIBLE FUTURE successor decision for Duho once photo_z actually lands — relevant context
for the eventual paper (a same-pipeline re-run on a larger, fix-carrying release becomes
feasible weeks after this study's data is in hand), not a reason to touch anything frozen.

The cosmo/Iris membership question was not addressed in the reply; it is moot for the campaign
(route B running) and the Iris request can idle.
