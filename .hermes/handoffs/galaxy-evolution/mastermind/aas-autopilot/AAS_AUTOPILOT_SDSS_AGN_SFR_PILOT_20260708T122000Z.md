# AAS research autopilot packet — SDSS optical AGN/sSFR pilot

Marker: `AAS_AUTOPILOT_SDSS_AGN_SFR_PILOT_20260708T122000Z`

## User request

Make the autopilot do actual research from the research proposal using actual data, write the result in AAS journal format, and generate a PDF.

## Executed target

Proposal executed as first feasible pilot:

`RP-1 — Observational constraints on the suppression of star formation by AGN feedback`

Operational pilot question:

Do optically selected SDSS BPT AGN hosts show a specific-star-formation-rate offset relative to star-forming emission-line controls matched in stellar mass proxy and redshift?

## Data source

Public SDSS DR17 SkyServer queried through `astroquery.sdss`.

Tables joined:

- `SpecObj`
- `galSpecInfo`
- `PhotoObj`
- `galSpecLine`
- `galSpecExtra`

Read-only public query. No DB/product/API mutation.

## Actual analysis performed

Script:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_sdss_agn_sfr_pilot.py`

Main cuts:

- spectroscopic class `GALAXY`
- redshift `0.02 < z < 0.12`
- positive Halpha, Hbeta, [O III] 5007, [N II] 6584 line fluxes
- S/N >= 3 in all four BPT lines
- `8.0 < lgm_tot_p50 < 12.5`
- `-14 < specsfr_tot_p50 < -7`

Classification:

- BPT line-ratio cuts using Kauffmann et al. (2003) and Kewley et al. (2001).
- AGN side treated as a single optical-AGN pilot class.
- Intermediate/composite objects reported but not used as controls.

Matched-control test:

- Each optical AGN host matched to nearest star-forming galaxy in standardized `(logM, z)` space.
- Controls selected with replacement.
- Primary statistic: `log sSFR_AGN - log sSFR_control`.
- Bootstrap intervals from matched-pair resampling.

## Main result

- Raw SDSS rows: 60,000
- Analysis rows: 60,000
- BPT star-forming: 39,553
- BPT intermediate/composite: 12,234
- BPT optical AGN: 8,146
- BPT unclassified: 67
- Matched pairs: 8,146
- Median matched delta log sSFR: -1.309 dex
- 95% bootstrap CI for median delta: [-1.334, -1.282] dex
- Mean matched delta log sSFR: -1.202 dex
- 95% bootstrap CI for mean delta: [-1.219, -1.184] dex
- OLS AGN coefficient adjusted for logM and z: -1.199 ± 0.006 dex

Interpretation guard:

This is an association pilot, not causal evidence for AGN feedback. It does not control morphology, environment, aperture effects, retired/LINER-like ionization, gas reservoirs, AGN luminosity, or duty-cycle timing.

## Generated artifacts

Run root:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/`

Data:

- `data/query.sql`
- `data/sdss_dr17_emission_line_sample.csv`
- `data/analysis_sample_bpt.csv`
- `data/matched_agn_sf_pairs.csv`

Results:

- `analysis_results.json`
- `METHODS_AND_SCOPE.md`
- `run.log`

Figures:

- `figures/figure1_bpt.pdf`
- `figures/figure1_bpt.png`
- `figures/figure2_matched_offsets.pdf`
- `figures/figure2_matched_offsets.png`

AAS manuscript:

- Source: `aastex/sdss_agn_sfr_pilot_aas.tex`
- PDF: `aastex/sdss_agn_sfr_pilot_aas.pdf`

Final PDF SHA256 after wrapper verification:

`7f2832413b354023be6375e3a8c2bf4a9658c0791f9167a5056a9c5fc19d8e75`

## Reproduce

From repo root:

```bash
python3 .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_sdss_agn_sfr_pilot.py
cd .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex
tectonic sdss_agn_sfr_pilot_aas.tex
```

The first command uses the cached CSV if present; remove the run data directory to force a fresh SDSS query.

## Verification

Verified:

- SDSS public query returned actual rows.
- Analysis script completed with exit code 0.
- Figure PDFs/PNGs exist.
- AASTeX 6.3.1 class compiled through Tectonic.
- PDF exists, file command identifies it as PDF 1.5.
- Final PDF size after wrapper verification: 234,931 bytes.
- Final PDF SHA256 after wrapper verification: `7f2832413b354023be6375e3a8c2bf4a9658c0791f9167a5056a9c5fc19d8e75`.
- Note: PDF SHA can change across recompiles because Tectonic/PDF metadata can be regenerated; the source, data, figures, and analysis JSON are preserved for reproducibility.
- Tectonic had no fatal errors; only minor line-breaking warnings from AASTeX output.

## Safety boundary

No NebulaMind DB writes. No SQL against product DB. No `/api/pages`. No page_versions/live wiki publish. No trust recompute. No deploy/restart. No git commit/push/merge. No cron. No billing/cloud/OAuth/API-key changes.

## Next publish-quality extensions

For a submission-quality version, the autopilot should add:

1. Full parent sample count rather than `TOP 60000` pilot cap.
2. Morphology and environment matching.
3. Separate Seyfert, LINER/retired, composite, and star-forming classes.
4. Aperture-corrected or spatially resolved star-formation indicators.
5. AGN luminosity or line-luminosity controls.
6. Non-emission-line quiescent controls.
7. Reproducible uncertainty propagation for line fluxes and derived rates.
8. Human scientific review before any external submission or public claim promotion.

AAS_AUTOPILOT_SDSS_AGN_SFR_PILOT_20260708T122000Z
