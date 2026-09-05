# Standing-watch positive controls — Duho's overnight order item 4 (2026-09-06 00:18 KST)

"A watch nobody has tested is a watch that fires never." Both watches were tested tonight; results below. Nothing was
edited in either watch; no ledger, standing, tier or stamp moved.

## 1. b68 — the battery tripwire on entry 31's 2.5 M☉ bar (`b68_entry31_massbar_tripwire.py`)
- **Real ledger:** 3/3 checks PASS — heaviest secure PSR J0952−0607 at 2.35 ± 0.11 (1.36 σ below the bar), GW190814 secondary
  tracked as conditional, ledger↔record binding holds. Falsifier LIVE, NOT FIRED. Exit 0.
- **Positive control (temp copy of the ledger with a planted secure row CTL_PLANTED_2p60 at 2.60 ± 0.05):** the tripwire FAILS
  with the exact expected set — `MASS-BAR TRIPWIRE` (message "TRIPPED by ['CTL_PLANTED_2p60'] … MUST-STOP") and
  `LEDGER<->RECORD BINDING` (gap −2.00 σ ≠ recorded 1.36 σ); `CONDITIONAL TRACKED` still passes. 1/3 checks pass. The
  planted copy lives in `_tmp_b68_ctl/`; the real ledger was not touched.
- **Finding, not fixed:** the script exits **0** even when tripped; the loud halt is in stdout ("FAILING: […]"), which is the
  battery's convention (every b-script prints "n/m checks pass … FAILING"). Any consumer keyed on exit status would miss a trip.
  Recommendation for the battery owner: `sys.exit(1)` when any check fails, across the battery, in one change. Not done tonight —
  it is a battery-wide convention, not this lane's to change alone.

## 2. The Tuesday cron watch (`~/.hermes/scripts/nm_ns_mass_watch.py`, hermes job 146e36d34237, `0 10 * * 2`, next 2026-09-08)
- **Positive control (temp copy with state, hits and feed paths redirected):** run 1 on an empty state reported **25 new
  papers** with the preregistered criteria printed and wrote 25 hit rows and 1 feed event; run 2 was **silent**; `last_run` stamped.
  The arXiv query path works from this machine.
- **Real state:** seeded — 27 ids seen, last run 2026-09-04T18:04:47Z (the 09-03/09-04 readings came from it), so the first cron
  firing will not dump stale hits.
- **Scheduler path:** `hermes cron run 146e36d34237` was issued at 2026-09-06 00:18 KST to run the real job on the next tick (harmless: seeded
  state, so it prints nothing new and stamps `last_run`). Result: state `last_run` before 2026-09-04T18:04:47Z → after 2026-09-05T15:18:29Z.
- **Verdict:** ARMED. The job is active, the script runs, the state is seeded, the criteria are the preregistered ones, and the
  scheduler executes it.

## 3. Also standing
- b63 curvature tripwire and the Monday DESI curvature watch (job 4e6635005855, last run 2026-08-31 ok) — Hwao's lane's cron,
  BHU's tripwire; not re-tested tonight beyond confirming the job is active.

WATCH_POSITIVE_CONTROLS_COMPLETE
