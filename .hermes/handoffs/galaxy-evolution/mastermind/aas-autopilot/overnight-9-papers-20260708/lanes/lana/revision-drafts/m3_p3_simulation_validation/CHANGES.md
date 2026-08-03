# Lana selection-disclosure revision changes — m3_p3_simulation_validation

Marker: `LANA_MANUSCRIPT_TICK_20260708T161724Z`

Exactly what changed in the lane-local draft:
- Reframed the manuscript as a selection-flagged observed SDSS target vector, not a completed simulation-validation result.
- Rewrote the abstract to include the capped 60,000-row sample, the 249,917 public four-line S/N>=3 eligible count, and the two cached N<500 cells.
- Added exact recovered definitions for f_Q, f_BPT AGN, and high-excitation AGN: log sSFR<-11.0; BPT optical AGN; and BPT AGN plus log([OIII]/Hb)>0.25.
- Added a small-cell caution table with public parent/S/N/cached counts for the two N<500 cells: 300 cached of 1,252 S/N-eligible rows and 390 cached of 1,553 S/N-eligible rows.
- Rebuilt the 15-cell target-vector table with an explicit Flag column and rounded fractions to avoid false precision.
- Added discussion wording that no simulation is accepted, rejected, ranked, validated, or falsified without forward-modelled mocks through the same selection/aperture/noise filters.
- Deferred topic-specific simulation-validation bibliography insertion until Literature Wave-2 source grounding; retained only method/source anchors already present in the current manuscripts.

Files:
- TeX: `m3_p3_simulation_validation_lana_selection_revision.tex`
- Expected lane-local PDF after compile: `m3_p3_simulation_validation_lana_selection_revision.pdf`
