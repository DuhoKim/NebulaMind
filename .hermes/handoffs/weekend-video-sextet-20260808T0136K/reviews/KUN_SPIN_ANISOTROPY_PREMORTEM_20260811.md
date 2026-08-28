# KUN SPIN-ANISOTROPY DISPUTE PRE-MORTEM

Timestamp: 2026-08-11 KST

## Verdict

NOT_WORTH_DOING_YET as a new empirical public-data study.

Worth doing only as a short source-bound methods/dispute note if Duho wants the record explained. I would not commission a design brief for a new measurement now.

Reason: the direct public-data reanalysis already exists. Patel & Desmond 2024, *No evidence for anisotropy in galaxy spin directions*, collate the publicly available spin-classification data sets, test dipole/quadrupole/hemisphere anisotropy with Bayesian and frequentist methods, account for axis freedom/look-elsewhere effects and parameter degeneracies, and find consistency with isotropy. That paper is not a BHU answer; it is a spin-anisotropy-dispute answer. A new internal study would either reproduce their result or require a new mirror-controlled annotation pipeline, which is exactly the hard thing our GZ1 lane showed cannot be obtained from old public label products alone.

## Sources Checked

- Longo 2011, *Detection of a Dipole in the Handedness of Spiral Galaxies with Redshifts z ~ 0.04*, Phys. Lett. B 699, 224. Public abstract/full PDF reports the quoted `-0.0408 +/- 0.011` and `7.9 x 10^-4`.
- Land et al. 2008, *Galaxy Zoo: the large-scale spin statistics of spiral galaxies in the Sloan Digital Sky Survey*, MNRAS 388, 1686. Abstract says they correct handedness bias and find consistency with statistical isotropy.
- Shamir 2012 and later Shamir papers, including DESI Legacy/JWST spin-direction claims, as represented in public abstracts/full-text pages.
- Iye, Yagi & Fukumoto 2021 as part of the rebuttal set cited in Shamir and Patel/Desmond.
- Patel & Desmond 2024, *No evidence for anisotropy in galaxy spin directions*, MNRAS 534, 1553, DOI `10.1093/mnras/stae2158`.
- Local GZ1 frame/bias records, especially `reviews/LANA_SPIN_FRAME_PROVENANCE_FINDING_20260810.md`, `reviews/LANA_SPIN_LANE_CLOSURE_20260810.md`, and prior Kun isotropy-scope packets.

## 1. Look-Elsewhere / Axis Freedom

This is a real threat to the claimed significances.

Longo's abstract says the unbinned analysis made no prior assumptions for the dipole axis, and the paper reports Monte Carlo random-handedness trials with the lowest chi-square across randomly chosen axes. That is at least an attempt to include axis search. But the practical question is not whether Longo attempted it; it is whether the exact statistic, axis grid, sample cuts, and randomization convention remain the right null for incomplete SDSS sky coverage and later datasets.

Shamir-style significances are more exposed: axes and hemispheres are searched from the data, datasets and cuts vary across papers, and several reported p-values are tied to author-specific statistics. A nominal p-value is not enough unless the full search path is frozen.

Can we assess this from published information without rerunning pipelines? For the old claim papers, not cleanly. But the reason this does not automatically become "worth scoping" is that Patel & Desmond already did the public-data statistical adjudication. They model monopole/dipole/quadrupole/hemisphere terms, use uniform axis priors, compare against an isotropic baseline, report BIC/p-values, and explicitly say their methods account for the look-elsewhere effect and parameter degeneracies. They trace the contrary claims to ad hoc or biased statistics.

So the look-elsewhere problem is not an open invitation for us; it is the exact problem the 2024 rebuttal paper already attacks.

## 2. Mirror / Annotation Bias

This is the real wall for a new result.

Our GZ1 lane found the scar in concrete form: the mirrored condition flips labels as expected, but the flip counts are unbalanced, roughly 3,290 CW-to-ACW versus 3,618 ACW-to-CW, `dA_paired approx 0.095` with SE `approx 0.024`, repeating across scored cells. That is a sorter asymmetry. Mirroring cancels a genuine sky signal by construction, so any residual imbalance is a labeler/procedure effect, not a sky effect.

Any machine catalogue has the analogous problem. A classifier can carry a handedness preference, and a public column alone does not prove that the pipeline is anti-equivariant under mirroring, unbiased in confidence/abstention, and free of sky-correlated priors.

Can public products control this?

- Public spin-label tables alone: no. They are downstream labels, not a mirror-control experiment.
- Public claim-code plus labels: only partly. It can test the statistic, not the image-to-handedness bias.
- Public raw images plus a classifier we run: yes in principle, but then this becomes a new annotation pipeline, with WCS parity validation, original/mirror image generation, label anti-equivariance, confidence/abstention sky-predictability controls, and a negative-control target. That is the same control burden that closed the earlier public-data isotropy scope.
- Existing mirrored datasets: useful diagnostics, not enough by themselves. Patel & Desmond include GAN mirrored/non-mirrored products and note annotation biases. But accepting released annotations at face value can test whether those annotations imply anisotropy; it cannot prove the sky has or lacks a spin anisotropy.

Therefore a new result-bearing study would require owning the classifier pipeline. A public-products-only study cannot distinguish algorithmic/human annotation bias from a true sky signal.

## 3. Is It Already Settled?

For the available public spin-label products, effectively yes.

Patel & Desmond 2024 is directly on point. They collate all publicly available image data used in the literature, use the released spin annotations, run Bayesian and frequentist anisotropy tests, account for axis freedom and degeneracies, and find no significant anisotropy. They do not claim to prove every possible future annotation pipeline would give isotropy; they show the public record's existing annotated datasets do not support the claimed anisotropy under their tests.

That is enough to kill a new public-products reanalysis. If we rerun their code, we are validating custody or writing a methods note, not doing a new study.

Iye/Hayashi-style duplicate-object and selection criticisms are part of the dispute history, but they are not the best current endpoint. The current endpoint is the 2024 all-public-data analysis. Shamir has rebuttals and reproductions, but that means the disagreement is now about statistics, sample construction, and annotation trust. It does not expose a clean unexamined public control for us.

## 4. Honest Comparison To Closed Lines

This is more tractable than BHU because it has real numbers, real datasets, and a direct null: statistical isotropy of spin labels on the sky.

It is less tractable than it looks because the dominant systematic is the label-generation process. This is the same pattern as the spin closure, not an escape from it:

- Contested signal exists.
- Rebuttals exist.
- Public labels can be statistically reanalysed.
- But a physical sky claim needs control of the image-to-handedness pipeline.

If the goal is "do the published spin labels, as labels, still imply anisotropy under defensible statistics?", that has been done. If the goal is "does the sky have a spin anisotropy?", public labels are not enough without a mirror-controlled classifier pipeline.

## 5. Would A Positive Result Mean Anything?

Yes, but not BHU.

A clean detection would be about large-scale statistical isotropy / parity / angular-momentum alignment in the galaxy population. It would be a serious cosmology/systematics result because the cosmological principle predicts no preferred direction in the large-scale distribution of angular momentum. It could motivate early-universe parity/vorticity/anisotropic-cosmology model work, or expose a survey/annotation systematic.

It would not identify BHU. It would not support a parent black hole uniquely. The BHU closing record stands: Poplawski's rotating-parent paper supplies a qualitative handedness claim, but no calibrated BHU-specific target. A positive spin anisotropy would remain generic.

That means the spin-anisotropy dispute is scientifically worth caring about on its own terms, but only if we can add a control the literature has not already applied.

## What Would Reopen This

I would green-light a scope only if one of these exists:

1. A public image-to-handedness pipeline with frozen code, weights, preprocessing, original/mirror cutout generation, WCS parity receipts, and published mirror-control outputs.
2. A new public survey product with both spin labels and mirror-pair diagnostics, including confidence/abstention behavior and sky-position/covariate leakage checks.
3. A precise claim that Patel & Desmond missed an already-public dataset or made a recoverable statistical error, with source products sufficient to test that without reconstructing a full classifier.
4. A deliberately narrower methods note comparing Longo/Shamir/Iye/Patel-Desmond statistics and explaining why the record currently favors no anisotropy in public labels.

Without one of those, a new study repeats the same pattern: contested claim, systematics fight, public products insufficient for the dominant bias, and a likely terminal methods note.

## Plain Answer

Not worth doing yet as a new empirical study.

The honest result today is:

> The galaxy spin-anisotropy dispute is real and cosmologically meaningful independent of BHU, but the existing public spin-label record has already been reanalysed with look-elsewhere-aware methods and found consistent with isotropy. A stronger physical-sky test would require a mirror-controlled image-to-handedness pipeline, not just public downstream labels.

Safe to assert:

> A clean spin anisotropy detection would test statistical isotropy/parity of galaxy angular momenta, not BHU.

Not safe:

> The old Longo/Shamir p-values can be adopted as-is.

Not safe:

> Existing public spin-label catalogues can distinguish sky anisotropy from annotation bias without mirror-control provenance.
