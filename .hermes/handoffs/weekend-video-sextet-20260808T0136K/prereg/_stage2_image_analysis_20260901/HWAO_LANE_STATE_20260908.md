# HWAO lane state — 2026-09-08 00:04 KST (supersedes HWAO_LANE_STATE_20260907.md)
Stamped from `date`. Nothing in this lane waits on a human decision.

## The run: CLOSED, on two independently anchored grounds
* **Tuning stopped** at `MEDIUM-WCS-LOSSY` — no verdict, no `m`, no winner, no objective.
  Commit `0ccbc25e9`, activity `42819213926`, 12:50:03Z.
* **Access incident** — fresh-validation and holdout pixels sit on the developing account. Under signed
  V15 E5(d) that **voids attempt 2 and closes option (A)**; A1 line 94 invalidates independently.
  Commit `d61ca76b1`, activity `42822783701`, 13:39:15Z.
* **Scope correction** — the exposure is larger than first recorded and mostly predates the run:
  **149 validation (7.5%) and 14 holdout (7.0%)** objects have pixels on this account, 130 and 12 of
  them from the Tier-C `validation_bricks/` cache of 09-05, before this run's seed existed.
  Commit `0754865e9`, activity `42826737577`, 14:33:06Z.

A1 line 125 forbids curing prior exposure or restoring an expended attempt, so no amendment reopens it.

## The result Duho wanted, delivered
The approved 400-object exploratory comparison ran and is recorded: **388 scored**, 12 refused on data
integrity, machine sign **opposite** to the humans', **311/388 = 80.15%** agreement after one global
flip (77.75% counting refusals as misses). I recomputed every figure from the per-object data; the
majority-class baseline is 50.26% and agreement holds in both human classes (77.4% / 82.9%), so it is
not an artefact of class balance. Descriptive development-data number only — quote it as "80.15% after
one global sign convention", never as bare accuracy. Record `EXPLORATORY_COMPARISON_RECORD_20260907.md`,
commit `2192bb974`.

## Parked
The WCS preservation candidate is finished technical work — 398/398 headers accepted at `tolerance=0.0`
with a bit-identical transform, 40/35/42/5 tests, review packet indexed. **There is no run left to
adopt it into.** Its diffs are ready for focused changed-byte review whenever someone designs a
successor.

## Preserved and verified again this tick
Adopted bytes `1c4f96fb…` / `ea46478e…`, `tuning.abort.json` `a0ea7e7d…`, both earlier failed journals,
the 400 exposed tuning labels, the drawn lists, the fetched bricks and `validation_bricks/` — nothing
deleted, nothing moved. Holdout and validation **labels** were never opened. New this tick:
`EXTERNAL_EVIDENCE_MANIFEST_20260908.txt` pins the two out-of-repository evidence directories
(candidate + comparison, 429 files) by digest, since they live outside git and every record cites them.

## Carried forward for a successor
1. Fetch granularity is the whole brick while the draw partitions **objects**.
2. Worse, and the real lesson: **a fresh-validation custody boundary cannot be hosted in a lane that
   already caches survey bricks for another study.** Check cached-brick overlap **before the draw**.
3. The sign convention must be fixed and preregistered, not chosen after seeing the data.
