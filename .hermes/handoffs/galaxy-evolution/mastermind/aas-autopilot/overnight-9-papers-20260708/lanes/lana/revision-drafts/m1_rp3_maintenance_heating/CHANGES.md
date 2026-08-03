# Lana revision changes — M1 RP-3 maintenance-heating denominator

Timestamp: 20260708T140659Z

Source read:
- `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_aas.tex`
- `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/analysis_results.json`

Revision draft:
- `m1_rp3_maintenance_heating_lana_revision.tex`

Exactly what changed relative to the current linked source:
- Reframed the paper from a generic maintenance-heating pilot to an optical-AGN denominator for X-ray/radio maintenance-heating follow-up.
- Added quantitative abstract values for massive-host and massive-low-sSFR BPT AGN fractions, counts, and approximate binomial intervals.
- Expanded methods with the explicit massive threshold recorded in JSON: log(M*) >= 10.8.
- Added a deluxetable for the two denominator populations: N, BPT AGN count, AGN fraction, and approximate 95% interval.
- Added a dedicated interpretation-guard section separating optical AGN selection from jet power, cooling luminosity, and duty-cycle inference.
- Added a discussion outline focused on cross-matching to X-ray/radio follow-up with nondetection accounting.
- Preserved the original figure as a lane-local include path and rewrote the caption to identify it as a denominator diagnostic.

Open integration notes:
- Insert the exact low-sSFR threshold from analysis code before merging.
- Do not merge any wording that implies heating-to-cooling balance until X-ray/radio/halo data exist.
