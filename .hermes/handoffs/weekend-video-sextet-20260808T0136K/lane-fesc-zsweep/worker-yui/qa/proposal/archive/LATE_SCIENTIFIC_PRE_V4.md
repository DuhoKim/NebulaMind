# Verdict: **MINOR**

Core numerical claims and scientific distinctions are correct. I found non-blocking representation and disclosure issues that should be fixed before adoption.

## Verified checks

- **Fiducial closure crossing:** independently reproduced  
  \(z_c=8.045284271240234\), where the **16th percentile of** \(\Delta=f_{\rm esc}^{req}-f_{\rm esc}^{inf}\) crosses zero—not the median. Displayed `8.045` is correct. Bootstrap 16–84% bounds are exactly `8.03008071899414–8.059269256591797`, correctly rounded to `8.030–8.059`.  
  Sources: `TREND_RESULTS.json:228-253`; `make_trend_figure.py:81-108,152-157`.

- **Median crossing:** independently reproduced  
  \(z_m=6.327877044677734\), correctly displayed as `6.328`. The source also contains a bootstrap interval `6.316171417236328–6.3362962341308595`.  
  Source: `TREND_RESULTS.json:255-262`.

- **No-SFRD-tail closure crossing:** independently reproduced  
  \(z_c=7.615345001220703\), correctly displayed as `7.615`; bootstrap bounds `7.601756134033203–7.631122589111328`, correctly rounded to `7.602–7.631`. This is explicitly one changed prior—not an all-assumptions or worst-case corner.  
  Sources: `TREND_RESULTS.json:264-265,475-482`; manuscript `MERGED_FESC_ZSWEEP.tex:89-94`.

- **Conditional shortfall fractions:** independently reproduced exactly:
  - \(z=7:\ 0.659525 \rightarrow 66\%\)
  - \(z=8:\ 0.833525 \rightarrow 83\%\)
  - \(z=9:\ 0.927475 \rightarrow 93\%\)  
  Sources: `TREND_RESULTS.json:60-77,108-125,156-173`; manuscript `MERGED_FESC_ZSWEEP.tex:65-73`.

- **Semantics pass:** `S04_closure_crossing.png` explicitly separates closure-envelope \(z_c\) from median \(z_m\); `S06_no_tail_scenario.png` says “ONE CHANGE”; `S02`, `S03`, and `S05` identify bands and percentages as conditional model quantities. “MODEL OUTPUT · NO NEW MEASUREMENT” appears on every state, with stronger repetition in S01, S07, and S08.

- **Custody pass:** the frozen numeric and canonical-figure hashes match the proposal; all eight PNG hashes and the contact-sheet hash match `visual_proposal_v2/manifest.json`.

## Exact MINOR findings

1. **Exact-root markers and the drawn polygonal curves do not have identical crossing geometry.**  
   The renderer draws only the 0.5-redshift grid arrays and connects them linearly, while crossing lines/markers use separately stored fine-root values (`render_static_states.py:111-139,163-184,219-230,260-268`). Independent interpolation of the geometry actually drawn gives:
   - fiducial 16th-percentile crossing: `8.042556`, versus marker `8.045284`;
   - median crossing: `6.309639`, versus vertical line `6.327877`;
   - no-tail 16th-percentile crossing: `7.606093`, versus marker `7.615345`.  
   These differences are visually near or below line width, but the claim that the marker is *exactly where the drawn edge touches zero* is not mathematically exact. Insert the frozen crossing point into each plotted polyline or draw the continuous model curve used by the canonical figure.

2. **The full-range plot omits the physical \(f_{\rm esc}=1\) boundary.**  
   The displayed top-panel band reaches \(f_{\rm esc}^{req}=1.0449\) at \(z=9.5\) and `1.3747` at \(z=10\), but no state marks \(f_{\rm esc}=1\) or explains that part of the band is unphysical. The manuscript explicitly says this means no physical escape fraction closes the budget for that part of the systematic space (`TREND_RESULTS.json:180-209`; manuscript `:84`). A paper-naive viewer could otherwise read the entire band as physically admissible.

3. **The “OUTSIDE THIS MODEL” disclosure is accurate but visually non-exhaustive.**  
   S07 prominently names proxy transport, correctly identified as the dominant untested systematic. However, the manuscript also excludes He II corrections, \(\kappa_{\rm UV}\)/IMF dependence, SFRD faint-end truncation, and redshift-dependent \(\xi_{\rm ion}\), the latter of which would tilt the trend and move \(z_c\) (`MERGED_FESC_ZSWEEP.tex:100-105`). The categorical box could be read as a complete outside-model inventory. Label it “dominant omitted systematic” or mention that additional assumptions are unpropagated.

4. **Bootstrap labels omit what the narrow intervals mean.**  
   S04/S06/S08 say only “bootstrap.” The source defines these as 16–50–84 percentiles from 200 resamplings of the 40,000 model draws (`make_trend_figure.py:99-108`), not observational confidence or total model uncertainty. “16–84% finite-MC bootstrap” would remove the ambiguity.

5. **The no-tail result is one-prior at the assumption level, but not a paired-draw counterfactual.**  
   Changing RNG-stream consumption also resamples the unchanged proxy distribution (`make_trend_figure.py:37-55`): fiducial proxy quantiles are `0.023405/0.062232/0.170264`, versus `0.023725/0.062380/0.174824` in the no-tail run. Holding the fiducial proxy draws fixed gives \(z_c=7.595287\), rather than `7.615345`. This does not threaten the much larger earlier-crossing direction, but `7.615` should be understood as the frozen independent Monte Carlo realization—not an exact paired one-variable counterfactual.

- **Files created or modified:** none.
- **Issues encountered:** none. MP4/audio were deliberately not evaluated because they are absent and outside scope.