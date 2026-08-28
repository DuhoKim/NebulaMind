# KUN — Cosmic Anisotropy Beyond Galaxy Spin, Adversarial Probe Review

Filed: 2026-08-11 00:20 KST  
Order: `HWAO_COSMIC_ANISOTROPY_OVERNIGHT_ORDER_20260810T2340K.md`  
Role: per-probe dominant systematic and public-data controllability.

## Boundary

Scope only. No run, result, claim, video, publication, public surface, or lane unlock. This is separate from the spin lane; the spin freeze still excludes GRB, SN Ia, dark energy, quasar, H0, and parity topics from that video.

The spin study failed tonight on classifier chirality bias. These probes do not require a human/CNN left-right morphology judgment, so that specific failure mode is absent. That does not make them clean; it means their systematics have to be judged on their own.

## Verdict First

Single probe worth a design brief: **quasar/radio number-count dipole**, narrowly framed as a public-data systematics-bounded test of the reported excess over the CMB-kinematic expectation.

Reason: its dominant systematics are selection, flux calibration, masking, Galactic contamination, scan-pattern gradients, and source-density gradients. Those are not hidden priors like inherited spin chirality. They are measurable or at least stress-testable from public catalogues, masks, ecliptic/Galactic coordinates, WISE/Quaia selection functions, radio survey footprints, and published mock/systematics treatments.

Not a guaranteed detection. Not a claim. But it is the only probe in this set where the dominant systematic looks publicly controllable enough to justify a design brief tonight.

## Probe Assessments

### 1. Quasar / Radio Number-count Dipole

What is claimed: CatWISE quasar and radio-source number-count dipoles have been reported with amplitudes roughly a factor of two above the CMB-kinematic expectation. Recent papers continue to argue over significance, mask coupling, clustering, colour dependence, and catalogue systematics rather than whether the measurement is conceptually possible.

Public data: CatWISE2020-derived quasar samples, Quaia Gaia+unWISE quasars with documented selection-function models, NVSS/TGSS/RACS/LoTSS-style radio catalogues and masks in the literature, plus public WISE/Gaia/radio catalogues.

Dominant systematic: angular selection function. Specifically flux calibration/depth gradients, WISE ecliptic scan-pattern density trends, Galactic contamination, stellar contamination, masking, source confusion, local structure/clustering dipole, and mode coupling from partial/asymmetric masks.

Public-data controllability: **YES, with strict scope.** This is not an unmeasurable prior. Published CatWISE work explicitly models ecliptic latitude trends, masks the Galactic plane and bright/contaminated regions, and discusses mask-induced mode coupling. Quaia is especially attractive because it ships a documented selection function. Radio catalogues provide independent frequency/instrument checks.

Fatal caveat to freeze: the design brief must not ask "is there a dipole?" loosely. It must freeze one catalogue family, one mask, one flux threshold ladder, one selection-function correction, one mock/null construction including clustering and mask mode-coupling, and a cross-catalogue replication rule. If those cannot be frozen, return INCONCLUSIVE.

Disposition: **DESIGN_BRIEF_YES**, best candidate.

### 2. SN Ia Anisotropy / Directional H0

What is claimed: Pantheon+ analyses report disputed conclusions: some find dipolar variation in local Hubble expansion or directional H0; others find consistency with isotropy or argue current SN samples cannot robustly determine anisotropy directions. Several results depend strongly on frame choice and peculiar-velocity corrections.

Public data: Pantheon+ / Pantheon+SH0ES public release, covariance products, light-curve parameters, redshifts, sky positions; code exists for some anisotropy analyses.

Dominant systematic: calibration and sky coverage. SN Ia samples combine many surveys with different calibration systems, selection functions, cadence, dust treatment, host-galaxy correlations, peculiar-velocity corrections, and uneven sky coverage. Directional H0 is also dominated at low redshift by bulk flows and sample variance.

Public-data controllability: **PARTIAL, not design-brief winner.** The data and covariance are public, and many systematics are documented. But the anisotropy direction can be unstable because the sky is sparse and survey-composite. Calibration covariances are only as useful as their decomposition; Pantheon+ public products do not make every directional calibration uncertainty separable in the way an adversarial sky-split needs.

This is not an unmeasurable-prior failure like spin, but the dominant systematic is close to the signal and already live in the literature. A design brief could reproduce published analyses, but Duho's rule says to believe and build on existing work, not rerun until a preferred answer appears.

Disposition: **HOLD / build on literature**, not the single overnight recommendation.

### 3. H0 Directional Variation

What is claimed: overlapping with SN Ia anisotropy, papers report hemispherical or dipolar H0 variation, sometimes aligned with local bulk flow/CMB dipole, while other studies argue current samples cannot robustly localize directions.

Public data: Pantheon+SH0ES, CosmicFlows-style velocity catalogues, SN catalogues, DESI/BAO public products for broader cosmology constraints.

Dominant systematic: sample variance and sky-split fragility. Once the sky is split into many regions, each region has too few calibrators/SNe, uneven redshift distributions, and strong dependence on peculiar-velocity modeling.

Public-data controllability: **PARTIAL but not sufficient for an independent design brief.** Public data can define the test, but the control for "direction remains meaningful after sky splitting" is not strong with current SN distributions. A negative control exists only as simulations/mocks or shuffled sky positions, which tests the statistic but not all calibration/selection coupling.

Disposition: **fold into SN Ia literature review if needed; do not select as standalone.**

### 4. GRB Angular Clustering

What is claimed: older BATSE/Swift/Fermi studies report possible short-GRB anisotropy or clustering; reanalyses emphasize localization uncertainty and detector exposure. Some papers find no significant violation once positional uncertainties/exposure are handled.

Public data: Fermi GBM burst catalogues, GBM daily data, HEALPix localization files, BATSE/Swift catalogues, spacecraft pointing/exposure products.

Dominant systematic: detector exposure and localization uncertainty. GBM sees the unocculted sky with detector response depending on spacecraft orientation, Earth occultation, triggering thresholds, detector viewing angles, spectral hardness, and burst duration. Short GRBs have fewer events and broader relative uncertainty problems.

Public-data controllability: **PARTIAL.** Public Fermi data include pointing, detector response products, GBM localizations, and catalogues; exposure can be modeled. But the actual trigger efficiency as a function of spectrum, duration, background, Earth occultation, and onboard thresholds is hard to reduce to a clean public sky mask. Some published work builds exposure maps, but the control is not as direct as quasar selection maps.

This is not a hidden human prior, but the negative control is weak: long GRBs are often used as a comparison, yet they differ astrophysically and observationally from short GRBs. That is not a clean null target sharing the same selection function.

Disposition: **NOT first design brief.** Use existing literature; possible later if Tori finds a public exposure/trigger-efficiency product strong enough.

### 5. Dark-energy Anisotropy / BAO Directional Tests

What is claimed: directional dark-energy/BAO anisotropy claims exist, and DESI DR1 public products now include BAO/full-shape cosmology chains, likelihood products, clustering measurements, covariance matrices, mocks, and systematics templates.

Public data: DESI DR1 spectra, LSS clustering products, BAO/full-shape likelihoods, mocks, covariance products, BAO cosmology chains; Pantheon+/Union3/DESY5 SN likelihood combinations in DESI products.

Dominant systematic: survey window, selection function, reconstruction/modeling choices, covariance/mocks, and direction-split degeneracies. BAO is designed for isotropic/anisotropic distance constraints relative to line of sight, not arbitrary sky-direction dark-energy dipoles.

Public-data controllability: **YES for standard DESI cosmology systematics; NO for a clean overnight anisotropy design.** DESI public products are unusually well documented, but converting them into an all-sky directional dark-energy anisotropy test is not just reading a public field. It requires a new statistic whose window-function and covariance behavior must be validated. That is design-heavy and not the clearest first probe.

Disposition: **watch / support for future**, not the recommendation.

### 6. Cosmological Parity Violation from Galaxy Four-point Functions

What is claimed: BOSS DR12 parity-odd 4PCF analyses reported ~7 sigma CMASS and ~3 sigma LOWZ evidence. Counter-analyses argue the signal is not compelling once covariance/mocks are reconsidered. GLAM-Uchuu and later work suggest the earlier significance may be covariance underestimation. DESI DR1 LRG parity-odd 4PCF work now reports signals consistent with zero or limited by completeness/covariance questions.

Public data: BOSS DR12 LSS catalogues and mocks, published data products for "No evidence" analyses, DESI DR1 LRG samples and public mocks/products, analytic and simulation covariance machinery in the literature.

Dominant systematic: covariance/model mismatch, especially whether mocks correctly capture the parity-even higher-order functions controlling the variance of parity-odd 4PCF statistics. Survey geometry and completeness also matter, but the decisive dispute is covariance.

Public-data controllability: **YES in principle, but not as a quick public-control design.** The data and mocks are public, and this is a serious mainstream probe. But the dominant systematic is not a map-like nuisance one can bound with public metadata; it is whether the mock/analytic covariance is faithful for a high-dimensional 4PCF. That requires expert replication of covariance methods and likely new or carefully chosen simulation suites. Existing papers have already done the key dispute work, and the latest direction appears to be "not compelling / consistent with zero" rather than an unworked opportunity.

Disposition: **do not select for overnight design brief.** Treat as literature-frontier monitoring unless a Tori/Goru packet identifies a public covariance product that cleanly answers the dispute.

## Recommendation

Recommend exactly one design brief: **quasar/radio number-count dipole**.

Why this one: the dominant systematic is a selection function rather than an unobservable classifier prior, and the public data ecosystem already includes the ingredients needed to freeze controls: catalogues, masks, selection models, flux thresholds, sky-density maps, Galactic/ecliptic coordinates, and independent catalogue families.

Design-brief constraints I would require:

1. Freeze one primary public catalogue and one independent replication catalogue before analysis.
2. Freeze masks, flux cuts, colour cuts, and source-quality cuts.
3. Freeze systematics maps: Galactic latitude/extinction/stellar density, ecliptic latitude, depth/coverage, flux-calibration proxy, and local-structure/clustering mocks.
4. Freeze the dipole estimator, kinematic expectation, and uncertainty construction including shot noise, clustering, and mask mode-coupling.
5. Require the excess to survive cut ladders and independent catalogue families; otherwise INCONCLUSIVE.
6. Do not claim new cosmology from one catalogue. Phrase only as "public-data design for testing the reported number-count dipole anomaly."

## Sources Checked

- CatWISE quasar dipole reassessment and systematics: https://doi.org/10.3847/1538-4357/ae6588
- CatWISE clustering/systematics discussion: https://doi.org/10.1093/mnras/stag201
- CatWISE colour-dependence/systematics: https://doi.org/10.1093/mnrasl/slae093
- Quaia public catalogue and selection functions: https://irsa.ipac.caltech.edu/data/Quaia/overview.html
- MNRAS review of cosmic dipole tensions: https://academic.oup.com/mnras/article-abstract/543/4/3229/8266509
- Pantheon+ anisotropy: https://link.springer.com/article/10.1140/epjc/s10052-025-14222-w
- Pantheon+ public data release: https://github.com/PantheonPlusSH0ES/DataRelease
- Pantheon+ isotropy counter-result: https://cpc.ihep.ac.cn/article/doi/10.1088/1674-1137/acfaf0
- SN anisotropy intrinsic-limit preprint: https://inspirehep.net/arxiv/2605.18470
- Fermi public data/products: https://fermi.gsfc.nasa.gov/ssc/data/access/index.html
- Fermi GBM data products/localizations: https://fermi.gsfc.nasa.gov/ssc/data/access/data_products.html
- GRB anisotropy and Fermi/GBM: https://academic.oup.com/mnras/article/472/4/4819/4157286
- GRB isotropy reanalysis with position uncertainties: https://academic.oup.com/mnras/article/490/4/4481/5586572
- DESI DR1 public release: https://data.desi.lbl.gov/doc/releases/dr1/
- DESI DR1 BAO cosmology products: https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/
- DESI DR1 full-shape/BAO clustering products: https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/
- BOSS parity-odd 4PCF claim: https://academic.oup.com/mnras/article/522/4/5701/7169316
- No-evidence parity reanalysis data/covariance issue: https://www.researchgate.net/publication/382065285_No_evidence_for_parity_violation_in_BOSS
- GLAM-Uchuu covariance reanalysis summary: https://pubmed.ncbi.nlm.nih.gov/39938550/
- DESI DR1 parity-odd 4PCF summary: https://inspirehep.net/literature/3095360

## Final Disposition

QUASAR_RADIO_DIPOLE_DESIGN_BRIEF_RECOMMENDED
