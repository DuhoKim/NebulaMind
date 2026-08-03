# M2 P3 / M3 P1 selection-CI revision summary — 20260708T193507Z

Marker: `TORI_M2P3_M3P1_SELECTION_CI_REVISION_20260708T193507Z`

## What changed

This tick addressed the external review blockers for the two Wave-3 active-9 drafts that remained table addenda:

- **M2 P3 — mass transition in quenching and optical AGN incidence** now has a lane-local AASTeX revision with explicit quenching threshold (`log(sSFR/yr^-1) < -11.0`), Wilson 95% intervals for every mass-bin fraction, a 15-row mass-redshift descriptive check, a selection-function disclosure table, and in-text citations from the Wave-3 literature packet.
- **M3 P1 — common-denominator optical tracer census** now has a lane-local AASTeX revision with explicit thresholds for BPT AGN, high [N II]/Halpha, high [O III]/Hbeta, red emission-line, and low-sSFR emission-line tracers; Wilson intervals for 15 S/N/tracer rows; a paragraph explaining why S/N>=10 makes high-[O III]/Hbeta prevalence rise while BPT-AGN prevalence falls; a selection-function disclosure table; and in-text citations from the Wave-3 literature packet.

## Data/source grounding

- Numerical fractions, Wilson intervals, and redshift/tracer rows were recomputed locally from the cached source sample `runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv`; selection-function counts come from `lanes/goru/tables/selection_caution_overlay_20260708T162615Z.csv`.
- Literature/source placement follows `lanes/literature/literature_source_packet_wave3_missing_active9_20260708T170557Z.md`.
- No new web queries, DB writes, public page edits, or live mirroring were performed.

## Verification

- M2 P3 mass-bin rows: **5**; first mass bin with `f_Q >= 0.5`: **11.0-12.5**.
- M2 P3 redshift-stratified rows: **15**.
- M3 P1 tracer/SN rows: **15**.
- Selection-stage rows included: **7**.
- Compiled PDFs: **2/2** start with `%PDF` and have no fatal LaTeX markers.
- Original public-linked M2 P3 and M3 P1 PDF hashes still match the 8-paper manifest: **True**.

## Key compiled outputs

- `lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/aastex/m2_p3_feedback_transition_mass_selection_ci_20260708T193507Z.pdf` — 100051 bytes — SHA256 `984974f83f5d7cf63aa567e0c3b09fb88bb60cffeadf9f0962fa2ab57431ff87`
- `lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/aastex/m3_p1_multiphase_census_selection_ci_20260708T193507Z.pdf` — 93799 bytes — SHA256 `eb825726003b88cc69cca488c4076bb679cfaa52e00aac0a93f80ded9d081826`

Manifest: `lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/m2p3_m3p1_selection_ci_manifest_20260708T193507Z.json`

Safety: No public pages, live roots, product DB, SQL, /api/pages, page_versions, trust recompute, deploy/restart, git commit/push/merge/rebase, billing/OAuth changes, new cron jobs, or external submissions. No active execution phrase.
