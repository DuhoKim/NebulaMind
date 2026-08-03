# SDSS AGN/sSFR pilot methods and scope

Marker: `SDSS_AGN_SFR_PILOT_20260708T122000Z`

This run is a bounded pilot execution of the AGN-feedback research proposal. It uses public SDSS DR17 spectroscopy and derived quantities to test whether optically selected BPT AGN hosts show a specific-SFR offset relative to nearest star-forming controls matched in stellar mass proxy and redshift.

Data source: SDSS DR17 SkyServer queried through `astroquery.sdss`.

Main cuts:
- spectroscopic class `GALAXY`
- redshift 0.02--0.12
- positive Halpha, Hbeta, [O III] 5007, [N II] 6584 line fluxes
- S/N >= 3 in all four BPT lines
- `lgm_tot_p50` between 8.0 and 12.5
- `specsfr_tot_p50` between -14 and -7

Classification: BPT line-ratio cuts using Kauffmann et al. (2003) and Kewley et al. (2001) demarcations. AGN includes the high-excitation optical AGN/LINER side as a single pilot class.

Matched-control test: every BPT AGN host is paired to the nearest BPT star-forming galaxy in standardized `(logM, z)` space, with replacement. The primary statistic is the median difference `log sSFR_AGN - log sSFR_control`.

Key result from this run:
- analysis rows: 60000
- BPT AGN rows: 8146
- BPT star-forming rows: 39553
- matched pairs: 8146
- median matched delta log sSFR: -1.309 dex
- 95% bootstrap CI for median delta: -1.334, -1.282 dex

Scope guard: this pilot measures an optical-classification-associated sSFR offset. It does not establish causal AGN feedback, duty-cycle timing, molecular-gas depletion, or halo-scale energy coupling.

SDSS_AGN_SFR_PILOT_20260708T122000Z
