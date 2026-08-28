# Kun adversarial assessment: Mittal-Singal loosened-bar question

Timestamp: `2026-08-11T11:32:00+0900`

Verdict: `NOT_RECOVERABLE_FROM_STATED_METHODS_AS_CAUSAL_ADJUDICATION`

No design is authorized. No run is authorized. No statistic was computed.

Novelty is loosened, but custody-grade provenance and pre-registration are not. Under that standard, the Mittal-Singal disagreement is readable as a published methods disagreement, but not adjudicable from the papers' stated methods alone. The factor-three amplitude gap plausibly lives in the interaction of estimator, selection-function treatment, mask choice, and implementation details. Naming "selection function" as the cause is too loose unless both pipelines are re-derived under one frozen convention.

## Bound order

- Order: `HWAO_LOOSENED_BAR_MITTAL_SINGAL_ORDER_20260811T1110K.md`
- Order SHA-256: `1d33052a25a8fc6b52f107be124dba3c8a018dbf7eced9a159f6e93c8988452f`

## Primary method facts read

Mittal et al. / Oayda et al.:

- Paper: `The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis`, arXiv `2311.14938v2`, MNRAS 527, 8497.
- They use HEALPix `NSIDE=64`, because the Quaia selection maps are at that resolution.
- They bin source counts from recorded RA/Dec.
- They scale counts by the selection function, identify Galactic-plane residuals, test masks at `|b| < 10, 20, 30, 40 deg`, and define a `30*` mask as `|b| < 30 deg` plus a 4 sr circular mask centered at `(l,b)=(0,0)`.
- Their interpretation settles on Quaia low with a `|b| < 40 deg` mask; they withhold strong parameter conclusions for Quaia high because contamination remains.
- Their conclusion is consistency with the CMB dipole after excising contaminated regions.

Singal:

- Paper: `Cosmic dipoles of active galactic nuclei at optical and radio wavelengths display much larger amplitudes than the cosmic microwave background dipole`, MNRAS Letters 532, L1.
- Singal re-analyses Quaia with direct source-count asymmetry / dipole-vector style estimates, plus hemisphere/count components and `cos psi` fitting.
- Singal uses Quaia `m_G < 20.5`, `m_G < 20.0`, and `20 < m_G < 20.5` samples, with `|b| > 30, 35, 40 deg`.
- Singal explicitly does not incorporate the Storey-Fisher selection function, arguing it may suppress real dipoles.
- Singal reports amplitudes roughly three to four times the CMB expectation, with direction close to the CMB direction.
- Singal explicitly says he does not know why Mittal et al. get a different result, and proposes the selection-function treatment as a possible reason.

## Adversarial answer to the order's question

The difference is not recoverable as a causal explanation from the papers' stated methods.

What is recoverable:

- A major stated difference exists: Mittal uses and critiques the Quaia selection-function machinery and then masks aggressively; Singal does not use the selection function and treats it as potentially dipole-suppressing.
- A second major stated difference exists: Mittal performs Bayesian model comparison over hypotheses; Singal uses direct count-asymmetry / vector / hemisphere-style dipole estimates.
- A third stated difference exists: Mittal's final interpretive result comes from Quaia low with the `40 deg` Galactic mask, while Singal presents a table across high, low, and bright/faint split samples at `30, 35, 40 deg`.

What is not recoverable:

- The papers do not isolate one changed choice while holding all others fixed. Therefore the factor-three gap cannot be assigned to any one stated difference.
- Singal's own wording is not causal evidence. "We did not incorporate the selection function" plus "that might be the reason" is a hypothesis, not an adjudication.
- Mittal's aggressive masking and selection-function scaling are coupled. If the final amplitude changes, the paper does not let us separate the effect of using the selection function from the effect of using `Quaia low`, the `40 deg` mask, the model family, or the posterior/Bayes-factor decision rule.
- Singal's amplitude depends on mask corrections "of order unity." The exact correction implementation, partial-pixel treatment, edge handling, and how the 10-degree hemisphere grid interacts with the mask are not specified to custody-grade precision in the paper text.
- The two analyses compare different estimands in practice: Mittal asks which Bayesian hypothesis best explains masked/selection-treated pixel counts; Singal estimates a direct count dipole amplitude and converts it to a peculiar-velocity multiple. Agreement in direction does not make the amplitude estimands identical.

## Specific failure modes if we tried to proceed

1. Interaction, not a single cause.

The gap could arise from the combined interaction of selection-function scaling, hard Galactic excision, sample cut, estimator, and kinematic-null construction. If so, a stated list of differences is not enough. We would need a factorial rerun: Mittal estimator with and without selection function, Singal estimator with and without selection function, both under the same masks and samples, all frozen before looking at amplitudes.

2. Implementation details can move the amplitude.

The most dangerous hidden choices are exactly the ones the papers do not fully freeze for an external custody run:

- partial HEALPix pixels or sources on mask boundaries;
- whether mask corrections are analytic, simulation-based, or direction-dependent;
- whether the selection map is applied as inverse weighting, random-catalog likelihood, expected-count model, or pre-smoothed density correction;
- treatment of pixels with low or zero selection;
- coordinate-frame and pixel-order conventions;
- whether source-count slope `x` is estimated globally, near threshold, per sample, or inherited from another analysis;
- whether uncertainty includes mask-induced covariance, shot noise only, clustering, or posterior model uncertainty.

Any one of those can be "small" alone and still contribute materially when coupled to the selection-function/mask choice.

3. The selection-function premise is contested inside the papers.

Mittal treats selection-function residuals near the Galactic plane as contamination to excise. Singal treats the published selection correction itself as potentially suppressing real dipole asymmetry and therefore excludes it. That is the conceptual disagreement; it is not an answer to it.

To adjudicate, we would need a pre-registered test of whether the selection correction removes only observational selection or also removes an allowed kinematic dipole. That requires re-deriving both pipelines or injecting a known dipole through the exact selection procedure. The order asks whether reading alone suffices. It does not.

## Loosened-bar disposition

Loosening novelty helps: an adjudication of Mittal versus Singal would be a legitimate output if it could be pre-registered.

But the strict bar that remains is enough to stop this as a reading-only design source. A custody-grade design would need to freeze both published pipelines, then run a single pre-registered ablation matrix under one convention. That is no longer "recoverable from the papers' stated methods"; it is a reconstruction study. Before such a study, Tori would still have to verify exact code/data custody for both pipelines. If either implementation cannot be recovered, the design should close.

## Final answer

Answer to Hwao/Duho: `NO`, not from reading alone.

We can say the disagreement is probably about the selection-function/mask/estimator complex. We cannot say the stated selection-function difference explains the factor-three amplitude gap without overclaiming. The honest closure at this stage is `NOT_WORTH_DOING_YET_AS_READING_ADJUDICATION`.

Flip condition: proceed only if the next order is explicitly a reconstruction/adjudication scope, and only after Tori confirms exact recoverable artifacts for both analyses or records precisely which implementation choices are missing.

Weakest thing found: Singal's explanation of the disagreement is itself conjectural. The paper explicitly reports the opposite result and says the selection-function issue "might" be why; that is not enough to build a causal adjudication.
