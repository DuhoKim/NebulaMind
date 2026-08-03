# Selection-function attrition check — 20260708T155514Z

Marker: `SELECTION_FUNCTION_ATTRITION_TICK_20260708T155514Z`

## What this tick did

- Ran public/read-only SDSS DR17 SkyServer `COUNT(*)` queries only.
- Quantified the parent-to-four-line-S/N selection cascade behind the cached 60,000-row SDSS sample used by the 9 active AAS-style pilots.
- Focused downstream checks on the external-review blockers: M3 P2 gas-denominator attrition, massive-host denominator attrition for M1 RP-3/M2 P2, sSFR-dependent line-selection bias, and small M3 P3 target-vector cells.
- Wrote lane-local CSV/JSON/Markdown/AASTeX-fragment artifacts only; no public-linked manuscript/PDF was overwritten.

## Key results

1. Public SDSS DR17 has **249,917** rows satisfying the same four-line S/N$\geq$3 redshift/mass/sSFR cuts; the cached sample has 60,000 rows, so it covers **24.0%** of the strict eligible set and is a `TOP 60000 ... ORDER BY s.specObjID` capped subset, not a random sample.
2. The four-line S/N selection is sSFR-dependent: S/N$\geq$3 keeps **33.56%** of the `-12.0_to_-11.0` sSFR parent bin versus **94.85%** of the `-10.0_to_-9.5` bin.
3. M3 P2 default (`logM>=10.6`, `log sSFR<-10.7`): **121,533** public parent rows, **40,797** four-line S/N$\geq$3 rows, **10,270** cached rows.
4. M3 P2 strict (`logM>=11.0`, `log sSFR<-11.0`): **33,125** public parent rows, **11,288** four-line S/N$\geq$3 rows, **2,941** cached rows.
5. M3 P3 cached target-vector cells with `N<500` checked against public DR17: **2** cells; these need minimum-N/uncertainty flags before manuscript merge.

## Files

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/tables/selection_stage_counts_20260708T155514Z.csv`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/tables/m3_p2_massive_low_ssfr_attrition_20260708T155514Z.csv`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/tables/massive_host_attrition_m1rp3_m2p2_20260708T155514Z.csv`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/tables/ssfr_bin_line_selection_attrition_20260708T155514Z.csv`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/tables/m3_p3_small_cell_attrition_20260708T155514Z.csv`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/selection_attrition_table_fragment_20260708T155514Z.tex`
- Raw SQL/JSON payloads: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/raw_sdss_payloads`

## Interpretation guard

Selection-function counts improve denominator honesty only. They do not establish causal AGN feedback, gas depletion, radio-jet coupling, outflow escape/recycling, or simulation-validation conclusions.

## Safety

No NebulaMind/product DB writes, SQL apply packets, `/api/pages`, page_versions, live wiki publish, trust recompute, public/live frontend mirroring, deploy/restart, git commit/push/merge/rebase, cron creation, billing/cloud/OAuth/API-key changes, or external submission actions were performed.
