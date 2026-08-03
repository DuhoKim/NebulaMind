# Kun Verdict - P1 Massive-Galaxy Abundance Audit

## Overall Disposition

`PARTIAL__CLAIMS_REQUIRE_NARROWING`

The z~5 result is plausible as a descriptive calculation, but the served claim is not fully revision-ready under the brief's strict gates. The key blocker is source-role/statistic support: the audit required explicit `n(>Mstar)` evidence, and the observed anchor is not pinned here as a primary-source cumulative-density row with threshold, selection, completeness, scatter, Poisson, and cosmic variance all attached.

## Component Grades

| Dimension | Grade | Reason |
|---|---:|---|
| Query coverage | `PARTIAL` | The draft covers the intended axes but not with a complete row-by-row primary-source cumulative ledger. |
| Statistic identity | `PARTIAL` | It uses the right statistic in prose, but mixes primary SMF/Schechter/candidate-density source roles into cumulative-density anchors. |
| Population commensurability | `PARTIAL` | Total, UV-red/UV-blue, candidate, and quiescent populations are mostly caveated but not fully separated in the budget and ledger. |
| Simulation commensurability | `PARTIAL` | The 2Rhalf/all-bound aperture correction is clear, but TNG counts are not independently reproduced here and central/satellite/selection/box-variance gaps remain. |
| Primary-source support | `FAIL` | Strict `n(>Mstar)` support is not demonstrated for the observed z~5 anchor. |
| Source version | `PARTIAL` | Pinned artifact and key published source identities are checked; several systematic-budget sources remain unverified by exact version. |
| Claim strength | `PARTIAL` | "No robust TNG tension at z~5 under a 0.20 dex mass shift" is acceptable only with conditional language; "robust and IMF-independent consistency" is too strong. |

## 0.28 Dex Versus 0.20 Dex

The historical `0.28 dex` number belongs to the original raw TNG aperture comparison: `SubhaloMassInRadType` within `2 x R_half`, `N=15`, `n=1.11e-5 Mpc^-3`, observed/TNG excess about `2.7x`, and `log10(2.7)/1.58 = 0.27-0.28 dex`.

The later `0.20 dex` number belongs to the regenerated total-mass-footing comparison: `SubhaloMassType`, `N=20`, `n=1.47e-5 Mpc^-3`, observed/TNG excess `2.04x`, and `log10(2.04)/1.58 = 0.20 dex`.

The revision only partly landed. The abstract, results, caption, and conclusion use `0.20 dex`, but the rendered Figure 1 arrow still says `0.28 dex`. Preserve this as a failed partial finding.

## Required Narrowing Before Revision

Replace categorical language with conditional wording tied to a directly sourced cumulative density. A defensible form is:

> On the served draft's adopted z~5 total-mass footing, the TNG100-1 count and the claimed Weibel cumulative density imply a factor-two offset, corresponding to about 0.20 dex for the measured TNG massive-end slope. This suggests, but does not by itself prove, that the z~5 total-population comparison is not a robust TNG tension once mass-systematic and aperture uncertainties are included.

Do not claim the z~7-9 candidate point or the spectroscopic z>6 quiescent residual is resolved. Do not use the analytic baryon ceiling as native TNG efficiency. Do not combine individual-object maxima into the z~4-6 total-population systematic budget without covariance and sample fractions.

## No-Edit Statement

This packet is read-only with respect to the manuscript, project source, public routes, database, Lab records, cockpit, services, and Git state. No manuscript or public artifact was revised.
