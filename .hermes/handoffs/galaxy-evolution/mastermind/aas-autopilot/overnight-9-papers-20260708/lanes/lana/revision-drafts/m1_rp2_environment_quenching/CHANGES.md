# Lana revision changes — M1 RP-2 environment quenching

Timestamp: 20260708T140659Z

Source read:
- `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_aas.tex`
- `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp2_environment_quenching/analysis_results.json`

Revision draft:
- `m1_rp2_environment_quenching_lana_revision.tex`

Exactly what changed relative to the current linked source:
- Replaced the generic abstract with a quantitative abstract naming the 60,000-galaxy denominator, high/low density quartile counts, quenched fractions, bootstrap interval, and adjusted linear-probability diagnostic.
- Split the single `Scope` paragraph into `Purpose and Scope`, `Data and Operational Definitions`, `Statistical Summary`, `Results`, `Discussion Outline for Integration`, and `Conclusions`.
- Added a manuscript-ready deluxetable for low-density versus high-density quartile results and the mass-redshift adjusted LPM coefficient.
- Tightened scope guards: 10th-neighbour density is explicitly a within-sample proxy, not halo mass, group membership, central/satellite status, or causal environment.
- Added a merge note that the exact quenched sSFR threshold should be inserted from the analysis code because it is not named in the JSON summary.
- Preserved the original figure as a lane-local include path and rewrote the caption to identify it as a proxy diagnostic.

Open integration notes:
- Insert the exact quenched threshold from the preserved analysis code before merging.
- If a later Goru pass provides density-definition details, replace the current cautious wording with the exact formula and edge/mask limitations.
