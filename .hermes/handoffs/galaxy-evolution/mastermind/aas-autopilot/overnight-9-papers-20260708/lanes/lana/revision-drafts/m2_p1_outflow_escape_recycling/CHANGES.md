# Lana revision changes — M2 P1 outflow escape/recycling denominator

Timestamp: 20260708T140659Z

Source read:
- `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_aas.tex`
- `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/analysis_results.json`

Revision draft:
- `m2_p1_outflow_escape_recycling_lana_revision.tex`

Exactly what changed relative to the current linked source:
- Reframed the manuscript as a high-excitation optical-AGN denominator for resolved escape/recycling follow-up, not an outflow-fate measurement.
- Added a quantitative abstract with 4,440/60,000 high-excitation candidates, candidate fraction 0.074, approximate interval, and median sSFR contrast.
- Expanded the data section to state the parent SDSS emission-line selection and BPT recomputation context.
- Added a deluxetable for parent denominator size, candidate count/fraction, full-sample median sSFR, candidate median sSFR, and the -1.39 dex median offset.
- Added an explicit methods caveat: the exact high-excitation line-ratio criterion is not present in the JSON summary and must be inserted from analysis code before integration.
- Added a three-layer interpretation guard separating measured candidate counts from escape observables and recycling observables.
- Preserved the original figure as a lane-local include path and rewrote the caption to identify it as a target-selection baseline.

Open integration notes:
- Recover the exact high-excitation criterion from the preserved analysis code before merging.
- Avoid all escape/recycling claims until resolved kinematics, halo potentials, and multiphase gas/CGM tracers are added.
