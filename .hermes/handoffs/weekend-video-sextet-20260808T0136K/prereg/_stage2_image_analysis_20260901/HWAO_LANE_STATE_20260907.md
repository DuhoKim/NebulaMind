# HWAO lane state — 2026-09-07 23:00 KST (supersedes HWAO_LANE_STATE_20260905.md)
Stamped from `date`.

## The run: CLOSED by its own rules
The A1 agreement run began (input anchored, round 6445084 designated, planes accessed) and is over.
Two independent grounds, both recorded and anchored:
* **Tuning stopped** at `MEDIUM-WCS-LOSSY` — no `tuning.json`, no verdict, no `m`, no winner, no
  objective. Commit `0ccbc25e9`, activity `42819213926`, 12:50:03Z.
* **Access incident** — the whole-brick fetch put the pixels of **2 holdout and 24 validation objects**
  on the developing account. Under signed V15 E5(d) that **voids attempt 2 and closes option (A)**;
  A1 line 94 independently invalidates on holdout early access. Commit `d61ca76b1`, activity
  `42822783701`, 13:39:15Z; anchor record `776633239`.

No restart, amendment or exclusion list can lift either — A1 line 125 forbids curing prior exposure or
restoring an expended attempt. **Nothing in this lane is waiting on a human decision.**

## Preserved, verified after all of today's work
Adopted bytes untouched: run path `1c4f96fb…`, producer `ea46478e…`, both test modules.
`OUT_A1_REPAIRED/tuning.abort.json` = `a0ea7e7d…`. Both earlier failed journals (`OUT_A1/`,
`OUT_A1_FRESH/`), the 400 exposed tuning labels, all drawn lists and the 398 fetched bricks stay as
they are. Nothing deleted. Holdout and validation **labels** were never opened, and no protected data
was read to produce any of today's records.

## Parked, not adopted
The WCS preservation candidate (`/Users/duhokim/work/Trio/wcs-repair-candidate-20260907/`) is finished
technical work: 4 changed files, 398/398 headers accepted at `tolerance=0.0` with a bit-identical
transform, 40/35/42/5 tests, review packet indexed with digests. It is correct as far as the evidence
goes and **there is no run left to adopt it into.** It stays where it is until someone designs a
successor; its diffs and evidence are ready for focused changed-byte review on request.

## Safety check done this tick
Nothing can still touch the closed run. No seat is running. My own lane watcher (pid 78401, up 3d23h)
was read this tick: it only polls Tier-C sweep receipts and `/bin/ps`, writes its own state and event
files, and cannot start a stage, fetch a brick or invoke the run path. Left running; it is not a risk.

## The one design finding worth carrying forward
Fetch granularity is the whole brick while the draw partitions **objects**, so any draw over a
brick-sharing catalogue puts the other sets' pixels on disk at first fetch, and nothing in the run path
checks it. A successor must fetch per-object cutouts or partition the draw by brick, checked **at draw
time, before any fetch**. Recorded as preparation only.
