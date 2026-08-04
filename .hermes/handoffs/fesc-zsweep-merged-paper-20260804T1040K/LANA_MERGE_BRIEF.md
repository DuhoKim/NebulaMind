# LANA BRIEF — merged f_esc z-sweep paper (Duho: "go with the merged z-sweep paper")

Lane: `fesc-zsweep-merged-paper-20260804T1040K` (write ONLY here). You are Lana.

## Inputs (read-only)
- The three source drafts (AASTeX) in `.hermes/handoffs/galaxy-evolution/lab-runs/overnight-fesc-sweep-20260803T1330Z/` runs ovl6221700/01/02 — **z=9 (ovl6221702) is the spine** per Kun.
- `papers-overnight-20260803T2328K/LC-fesc-decision-packets/KUN_LC_REFEREE.md` — BINDING revision
  guidance: implement his F0 structure (one z-sweep paper; the trend is the central result) and
  fix every per-draft finding he lists.
- `MERIT_PANEL_SCORES.md` (same dir) — context for weaknesses to shore up.
- `TREND_DATA.json` + the 9 run JSONs in `trend-grid/` (z=6.0–10.0, Δz=0.5): required vs inferred
  f_esc posteriors per z. Compute in a lane script (`make_trend_figure.py`): shortfall fraction
  and Δ(required−inferred) vs z, the 16–84% band, and the **closure-crossing z** (where the
  interval stops spanning zero) — Kun located it between z=8 and 9; find it properly on the fine
  grid. Produce the central figure (matplotlib, lane-local PNG/PDF).
- `fesc-zsweep-photon-budget_history.json` — Duho's direction #1 is logged; do not edit history.

## Rules
- Every number in the draft comes from the run JSONs / your lane computation — nothing invented,
  nothing carried from the old drafts without re-verification against its run JSON.
- Modality: the z=9 title's honest hedging style extends to the whole paper; the trend claim
  states exactly what the MC supports. Uncertainties section mandatory (Kun's circularity-headroom
  points addressed explicitly).
- Single paper: no per-z repetition; z=7/8 material appears as sweep points.

## Deliverables (lane dir)
1. `MERGED_FESC_ZSWEEP.tex` (AASTeX, compilable structure) + the trend figure file(s).
2. `make_trend_figure.py` + computed `TREND_RESULTS.json` (shortfall/Δ/crossing with intervals).
3. `MERGE_CHANGELOG.md` — what came from which source draft, which Kun findings were fixed where.
4. `LANA_MERGE_REPORT.md` ending with marker: `LANA_FESC_MERGE_COMPLETE_20260804`.
Constraints: no network, no git/DB, lane-only writes, do not read C41/AGN lanes.
