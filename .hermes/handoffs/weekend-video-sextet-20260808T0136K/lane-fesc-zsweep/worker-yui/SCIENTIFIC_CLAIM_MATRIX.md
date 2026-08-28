# Scientific claim matrix

Source line references are to `MERGED_FESC_ZSWEEP.tex`; exact machine values are from `TREND_RESULTS.json`.

| Scene | Proposed claim | Exact source anchor | Verdict | Required display condition |
|---|---|---|---|---|
| S01 | Compare the escape fraction required by the maintenance budget with a proxy-inferred fraction; no new measurement. | lines 10–19 | PASS | Keep `MODEL OUTPUT · NO NEW MEASUREMENT` visible. |
| S02 | Required fraction rises over z=6–10; proxy-inferred fraction is z-independent because the same low-z calibrations are transported to every grid redshift. | lines 29, 39, 52–55, 78 | PASS_WITH_DISCLOSURE_MINOR | Label both curves and both 16–84% bands; say “fixed in redshift by construction”; draw physical `f_esc=1` and explain that required values above one cannot be physically supplied. |
| S03 | `Delta = required − inferred`; closure remains allowed while the 16–84% Delta interval spans zero. | lines 41, 55, 80–83 | PASS | Show Delta axis, zero line, median, full band, and lower edge. Do not call the band observational error. |
| S04 | Fiducial closure-envelope crossing `z_c=8.045` with finite-Monte-Carlo 16–84% resampling bounds `8.030–8.059`; median crossing is separate at `z_m=6.328`. | lines 75, 80–83; `closure_crossing_fiducial`; `median_crossing_fiducial` | PASS_WITH_RENDER_GEOMETRY_MINOR | Attach 8.045 to the 16th-percentile Delta edge at zero; insert the fine root into the displayed polyline or use the same continuous geometry for drawing and root finding; do not attach it to median required/inferred curves or describe the narrow bounds as total uncertainty. |
| S05 | Conditional shortfall fraction is 66% at z=7, 83% at z=8, and 93% at z=9. | lines 67, 69, 71; exact fractions 0.659525/0.833525/0.927475 | PASS_WITH_REPRESENTATION_MINOR | Show percent signs, redshift keys, `Delta>0`, and “conditional model mass, not real-world probability.” Encode the fractions in a dedicated probability strip/panel or x-keyed rail/table, not at median-Delta y-coordinates. |
| S06 | A separate run removing the JWST-motivated SFRD-tail prior family strengthens the shortfall and moves the closure crossing earlier to `z_c=7.615`, with finite-Monte-Carlo 16–84% bounds `7.602–7.631`. | lines 38, 55, 89–94; `corner_boost_none`; `make_trend_figure.py` | PASS | Name the removed prior family, disclose that draws are unpaired, compare with fiducial 8.045, and never call this every assumption, an all-systematics corner, or a paired one-variable counterfactual. |
| S07 | Proxy transportability from z≈0.3 to z>6 is the dominant omitted systematic outside the Monte Carlo; other structural assumptions are also unpropagated; the study contains no survey measurement. | lines 43–47, 96–105 | PASS | Keep the evidence plot, label propagated terms as examples, and state that the outside-model rail is not an exhaustive uncertainty inventory. |
| S08 | The crossing is conditional on frozen anchors; measuring high-z proxy transport is the next empirical test. | lines 101, 104, 108–109 | PASS | Close with finding, geometry/evidence, model boundary, and next test; no URL-only or brand-only close. |

## Values that must not drift

- `z_c(fiducial) = 8.045284271240234`
- fiducial bootstrap 16/50/84 = `8.03008071899414 / 8.045955657958984 / 8.059269256591797`
- `z_m(fiducial) = 6.327877044677734`
- `z_c(no SFRD tail) = 7.615345001220703`
- no-tail bootstrap 16/50/84 = `7.601756134033203 / 7.61572265625 / 7.631122589111328`
- shortfall fraction at z=7 = `0.659525` → 66%
- shortfall fraction at z=8 = `0.833525` → 83%
- shortfall fraction at z=9 = `0.927475` → 93%

## Known wording vetoes

- VETO: “where the required and inferred median curves cross” for 8.045.
- VETO: “required and inferred part company at 8.045” without the interval-detachment definition.
- VETO: “where every assumption is set against the result” for 7.615.
- VETO: “probability that a real cosmic shortfall exists” for 66/83/93%.
- VETO: observational confidence/error language for the model systematic bands.
