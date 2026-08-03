# Flagship review and package decision

Marker: `FLAGSHIP_REVIEW_DECISION_20260709T013510Z`

## User directive

Proceed with the recommended next decision after the 9-paper local integration run.

## Reviewed artifacts

- Integration handoff: `INTEGRATION_HANDOFF.md`
- Integration audit: `INTEGRATION_AUDIT.md`
- RP-1 integrated TeX/PDF/source JSON
- 8 guarded proxy/denominator TeX/PDF/source JSON records
- Shared selection-function, representativeness, and Goru robustness outputs already folded into the integration run

## Decision

Proceed with **one flagship paper plus one supplementary denominator/proxy atlas**, not 9 standalone papers.

### Approved flagship candidate

`m1_rp1_sdss_agn_sfr`

Why:

- It has the clearest direct measurement in the available data: a catalog-sSFR offset for broad optical BPT AGN hosts relative to mass-redshift matched star-forming controls.
- It has a real row-level SDSS DR17 analysis table, BPT classifications, matching design, robustness checks, and figures.
- It can be written honestly as an association/selection-aware SDSS short paper.
- The result is strong enough to polish locally: median delta log sSFR = -1.309 dex for 8,146 matched pairs, with bootstrap interval [-1.334, -1.283] dex.

Required flagship guard:

- The paper must not claim causal AGN feedback.
- It must foreground the capped/non-random cache and four-line emission-line selection.
- It must explicitly state subclass and S/N sensitivity: S/N>=10 and narrower Seyfert-like proxies reduce the median offset magnitude.

### Not approved as standalone physical-feedback papers

The other 8 drafts should not stay as independent papers because each lacks at least one core physical observable required by its original proposal:

- `m1_rp2_environment_quenching`: lacks group/halo and central-satellite information.
- `m1_rp3_maintenance_heating`: lacks radio jets, X-ray cavities, cooling luminosity, and halo gas.
- `m2_p1_outflow_escape_recycling`: lacks resolved outflow velocities and multiphase gas/CGM tracers.
- `m2_p2_radio_jet_environment`: lacks radio jet and hot-gas coupling measurements.
- `m2_p3_feedback_transition_mass`: lacks gas fractions, baryon deficits, halo masses, and high-redshift extension.
- `m3_p1_multiphase_census`: lacks molecular/neutral/X-ray/radio phases.
- `m3_p2_gas_depletion_efficiency`: lacks CO/HI/dust gas masses and aperture-matched gas depletion times.
- `m3_p3_simulation_validation`: lacks forward-modelled simulation mocks.

### Packaging decision

Package the other 8 as **supplementary denominator/proxy notes under one combined atlas**, not standalone claims.

Reason:

- Their shared value is methodological: they define denominators, target vectors, proxy baselines, and missing-observable checklists for follow-up.
- A combined supplement prevents overclaiming while preserving the useful work.
- It keeps the public/science narrative simple: one flagship SDSS result, one transparent atlas of what the current data can and cannot support.

## Action authorized locally by this decision

Create a local-only decision package with:

1. A polished RP-1 flagship AASTeX source/PDF.
2. A combined supplementary denominator/proxy atlas AASTeX source/PDF for the other 8.
3. A compile/audit manifest with hashes.

Do not publish, mirror, replace public PDFs, write DB/API/page_versions, deploy/restart, git commit/push/merge, create cron jobs, change billing/OAuth/API keys, or externally submit.
