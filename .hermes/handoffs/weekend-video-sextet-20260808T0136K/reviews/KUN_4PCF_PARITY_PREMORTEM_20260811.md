# KUN 4PCF PARITY PRE-MORTEM

Timestamp: 2026-08-11 KST

## Verdict

NOT_WORTH_DOING_YET as a result-bearing public-data study.

This is materially more tractable than the closed galaxy-spin line on the measurement side, because it does not require human/CNN chirality labels. But it is not materially more tractable on the decisive inference side. The disputed object is not just "the parity-odd 4PCF"; it is the significance of that vector under a covariance model. The covariance is exactly where the live literature fight sits, and public data does not give us a new decisive covariance control beyond what the competent teams have already tried.

I would allow only a narrow literature/provenance scope, not a design brief that promises a measurement.

Black-hole-universe cosmology remains Duho's standing personal research interest, not a field motivation for this probe. A 4PCF parity signal, even if real, would be degenerate among early-universe parity violation, survey/systematics, and covariance failure; it would not support BHU specifically.

## Sources Checked

- Goru inventory: `reviews/GORU_COSMIC_ANISOTROPY_PUBLIC_DATA_INVENTORY_20260810T2340K.md`
- Lana probe memo: `reviews/LANA_COSMIC_ANISOTROPY_PROBES_20260810.md`
- Philcox 2022, "Probing Parity-Violation with the Four-Point Correlation Function of BOSS Galaxies", PRD 106, 063501 / arXiv:2206.04227: https://arxiv.org/abs/2206.04227
- Hou, Slepian, Cahn 2022, "Measurement of Parity-Odd Modes in the Large-Scale 4-Point Correlation Function of SDSS BOSS DR12 CMASS and LOWZ Galaxies", arXiv:2206.03625: https://arxiv.org/abs/2206.03625
- Philcox and Slepian 2021, "encore: an O(N_g^2) estimator for galaxy N-point correlation functions", MNRAS 509, 2457: https://academic.oup.com/mnras/article/509/2/2457/6406518
- Philcox and Ereza 2024, "Could Sample Variance be Responsible for the Parity-Violating Signal Seen in the BOSS Galaxy Survey?", arXiv:2401.09523: https://arxiv.org/abs/2401.09523
- Krolewski, May, Smith, Hopkins 2024, "No evidence for parity violation in BOSS", arXiv:2407.03397: https://arxiv.org/abs/2407.03397
- DESI DR1 public data documentation, LSS catalogs and mocks: https://data.desi.lbl.gov/doc/releases/dr1/

## 1. Computational Wall

The naive computation is dead: counting all galaxy quadruplets is not an option. But the published estimator means this is not the first-order blocker.

Philcox and Slepian's `encore` estimator reduces the problem to pair counting / basis decomposition. The paper reports O(N_g^2) scaling, FFT alternatives, public code, and roughly 100 CPU-hours for 3PCF/4PCF/5PCF/6PCF on a BOSS-like survey including survey-geometry corrections. Their GPU/CPU timing table also shows 4PCF timings on test catalogues that are seconds to minutes, not weeks, at smaller scale.

Order-of-magnitude conclusion:

- One BOSS-like 4PCF measurement is feasible on a workstation or modest local compute if the code builds and dependencies behave.
- A full reanalysis over data plus hundreds/thousands of mocks is not a casual workstation task. If one 4PCF costs even 30-100 CPU-hours end-to-end after geometry/random corrections, 1000 mocks becomes 30,000-100,000 CPU-hours before analysis iteration. That is cluster work, not "overnight local" work.
- The computational wall is therefore real for a full covariance campaign, but it is not the clean kill. Existing public measurements/data products may avoid recomputing every catalogue. The kill is the covariance adequacy.

## 2. Covariance Problem

This is the blocker.

The claimed detection significance is covariance-dominated. Hou/Slepian/Cahn report high significance in BOSS CMASS/LOWZ, explicitly conditioned on mocks capturing the true covariance. Philcox reports a lower blind-test significance and explicitly leaves open that simulations may not faithfully represent BOSS statistical properties. The 2024 reanalyses do not merely quibble over implementation; they attack the covariance/significance machinery itself.

The fatal pattern:

- The statistic is high-dimensional. Hou/Slepian/Cahn's BOSS analysis is described in later work as having about 18,000 degrees of freedom.
- Full covariance estimation would require enough mocks to control a dense high-dimensional matrix; the available mock ensemble is not large enough for a brute-force covariance at that dimension.
- Krolewski et al. argue that the chi-square statistic is biased if parity-even 8PCF structure differs between data and mocks. Their reported result separates parity-odd signal from an 8PCF bias term and finds the signal can range from null to modest significance depending on choices.
- Philcox/Ereza replace MultiDark-PATCHY with GLAM-Uchuu N-body mocks and find no significant evidence, showing the conclusion moves when the mock family changes.

That is not a nuisance correction we can freeze away. It is the central uncertainty. A result without a defensible covariance is not a result; it is a measured vector with no trustworthy tail probability.

Public DESI DR1 does release LSS catalogues, randoms, 1000 EZmocks, and 25 AbacusSummit mocks. That helps for ordinary two-point work. It does not automatically solve a parity-odd 4PCF covariance problem. The approximate 1000-mock path risks reproducing the same PATCHY failure mode; the 25 high-fidelity mocks are nowhere near enough to estimate or validate a high-dimensional 4PCF covariance. A compressed statistic may help, but then the study is no longer "rerun the BOSS 4PCF parity test"; it becomes a new estimator-design project with its own gates.

## 3. Circularity / Public Randoms and Weights

The random catalogues and imaging weights do not obviously encode a cosmological parity prior. They are designed to model survey selection, geometry, fiber assignment, target completeness, and imaging systematics. That is better than spin, where the fatal confound was a hidden chirality classifier prior.

But there is still a circularity-adjacent hazard: a parity-odd 4PCF result is exquisitely sensitive to how geometry, masks, fiber collisions, target completeness, and weights are transported into the randoms and mocks. If the correction pipeline removes angular structure too aggressively, it can erase signal; if it under-models higher-order covariance, it can create significance. Both failure modes are plausible and already appear in the literature dispute.

So the public randoms are necessary but not sufficient. They let us reproduce a convention; they do not prove that convention is the right null distribution for a parity-odd high-order statistic.

## 4. What Would We Add?

For BOSS: almost nothing decisive.

The obvious checks are already done by the papers on both sides: BOSS samples, PATCHY mocks, alternative significance constructions, GLAM-Uchuu mocks, data-mock mismatch arguments, and systematics discussion. A new internal run would likely choose sides by choosing a mock family or compression convention. That is not adjudication unless the convention is independently decisive, and I do not see that from public data.

For DESI: something might be scientifically interesting later, but not yet gateable here.

Possible unexamined angles:

- Apply the Krolewski-style bias-separated statistics to DESI-like public mocks and DESI DR1 LSS catalogues.
- Use a compressed parity-odd power-spectrum statistic instead of the full 4PCF vector to reduce covariance dimensionality.
- Pre-register a deliberately low-dimensional parity-odd statistic with a covariance validation hierarchy: EZmocks for volume, Abacus for high-fidelity cross-check, jackknife/null rotations for diagnostics, and an automatic INCONCLUSIVE branch if mock family dependence is order-unity.

The problem is that each of these is a research-program scope, not a cheap public-data result. The negative control is again weak: we need a public way to prove the covariance/null ensemble captures parity-even high-order structure of the real survey. That is the exact thing disputed in BOSS.

## 5. Comparison To Closed Spin / Isotropy Lines

Compared with galaxy spin:

- Better: no morphology handedness classifier; no human-label inheritance path; no WCS mirror-sign trap.
- Worse: significance depends on high-order covariance rather than a directly inspectable signed-label residual.

Compared with the Quaia/isotropy line:

- Better: different observable and different data, so it obeys Duho's instruction to move on.
- Worse: the null is less sharp operationally. Quaia at least had a specific kinematic amplitude target; 4PCF parity has no comparable fixed amplitude, and a detection's meaning is covariance-conditional.

The pattern would repeat unless we weaken the output to "we recomputed a parity-odd vector under a named covariance convention." That is not a claim Duho needs; the field already has stronger versions of it.

## Stop Conditions For Any Future Reopen

Do not commission a design brief unless at least one of these becomes true:

1. A public DESI parity-odd 4PCF / POP data product exists with documented covariance products and mock-family validation.
2. A public high-fidelity mock suite large enough for the chosen compressed statistic exists, with a predeclared leakage test showing covariance stability across mock families.
3. The study is explicitly narrowed to a methods note comparing published covariance assumptions, not a measurement.
4. The estimator is changed to a low-dimensional compressed parity statistic, and the brief freezes the compression before any data statistic is seen.

## Final Answer

Not worth doing yet.

The computation is not prohibitive for one measurement, but the covariance is the real wall. Public data can provide catalogues, randoms, systematics maps, and some mocks; it cannot currently give us a decisive public control proving that the covariance/null ensemble represents the data's parity-even high-order structure. Without that, any significance claim is exactly the disputed assumption in a new wrapper.
