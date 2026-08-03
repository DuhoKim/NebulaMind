# Source Role Audit

## Pinned Artifact And Review

- `input/served-p1.pdf`: 4 pages, 123312 bytes, SHA-256 `189a2764a0b8e310802fb31bd53db3a64be49ac6411fe5f5b38af62cefa23f5d`.
- `input/served-review.md`: automated referee log, SHA-256 `330fe138acf79cf3bd4d3c43c7fe6a3026b111708db70a0efd02fa4254d818e0`.
- `input/served-history.json`: human-directed revision history, SHA-256 `d072698ef6efab8cb0ae039bd36aa97a2bddf525a848204fcf65e0cbb1d2b8b9`.

The review loop describes Cycle 1 as accepting a `~2.7x` excess erased by `0.28 dex`. The history then says the regenerated manuscript applied edits that changed the aperture basis and strengthened the result from `0.28` to `0.20 dex`. The served PDF partly reflects that revision, but Figure 1 retains the stale `0.28 dex` arrow label.

## Load-Bearing Sources

| Source | Correct Role | What It Can Support | What It Cannot Support Here | Audit |
|---|---|---|---|---|
| Weibel et al. 2024, MNRAS 533, 1808, DOI `10.1093/mnras/stae1891` | Observed JWST rest-optical-selected stellar mass functions at z~4-9 | Published SMF measurements, sample selection over CEERS/PRIMER/JADES, uncertainty components including Poisson, SED posterior sampling, and cosmic variance; UV-red dominance at high masses out to z~6 | A directly quoted primary-source cumulative `n(>10^10.5 Msun)` row unless explicitly integrated and documented | `PARTIAL` |
| Labbé et al. 2023, Nature 616, 266, DOI `10.1038/s41586-023-05786-2` | Candidate massive red galaxies and cumulative stellar-mass density stress case at z~7-9 | Candidate identities/masses and a high-z photometric residual that must remain separate | A robust total-population z~4-6 cumulative GSMF anchor, or a confirmed quiescent residual | `FAIL` if used for the headline; `PASS` as separate caveat |
| Boylan-Kolchin 2023, Nature Astronomy 7, 731, DOI `10.1038/s41550-023-01937-7` | LCDM halo abundance / baryon-ceiling stress test | Analytic HMF equations, baryon-conversion ceiling, interpretation of extreme candidate masses | Native TNG stellar-mass function or native achieved TNG efficiency | `PARTIAL` |
| Nelson et al. 2019, Computational Astrophysics and Cosmology 6, 2 | TNG public data release and simulation identity | TNG suite identity, data availability, cosmology, public catalog context | The exact `N=15` or `N=20` high-z threshold counts unless computed from catalog data | `PARTIAL` |
| TNG/Illustris forum definitions | Named-field convention support | Distinction between `SubhaloMassInRadType`, `SubhaloMassType`, and common 30 pkpc apertures | A peer-reviewed observational match or published high-z GSMF comparison | `PASS` for convention definitions only |
| Table 1 systematic sources in served PDF | Systematic-budget ingredients | Plausible mass shifts for specific SED/model/object classes | A covariance-aware consensus budget for all z~4-6 massive galaxies | `PARTIAL` |

## Source-Version Findings

- The public artifact identity for the served P1 PDF/review/history is pinned by `input/PUBLIC_ARTIFACT_IDENTITY.json`.
- Weibel et al. is the published MNRAS version with corrected/typeset date visible in the public article metadata.
- Labbé et al. is the Nature version of record, but the browser-accessible page exposed only preview/metadata due subscription gating. No paywall route was used.
- Several served bibliography entries are dated 2025-2026. I did not promote them to fully verified source support because this lane did not retrieve and compare their exact journal/preprint versions.

## Claim-Role Failures To Preserve

1. Schechter fits or differential SMF points are not the same as an explicit primary-source cumulative density row.
2. Labbé candidate objects and stellar-mass-density ceilings cannot be treated as a z~4-6 total-population `n(>M*)` anchor.
3. Analytic abundance-matched `epsilon` is not a native TNG galaxy efficiency.
4. Maximum mass shifts from unrelated SED samples cannot be linearly or quadrature-added into a consensus population budget without covariance and population fractions.

## Narrow Claim That Survives

The artifact supports a descriptive, internally calculated statement: if the Weibel z~5 total-population cumulative density is indeed `~3e-5 Mpc^-3` at `Mstar > 10^10.5 Msun`, and if the TNG100-1 all-bound count `N=20` is accepted, then the resulting factor `2.04` offset maps to a `~0.20 dex` mass shift for slope `-1.58`. That is narrower than the served title/abstract claim because the source-role and direct-cumulative-density gates are not fully passed.
