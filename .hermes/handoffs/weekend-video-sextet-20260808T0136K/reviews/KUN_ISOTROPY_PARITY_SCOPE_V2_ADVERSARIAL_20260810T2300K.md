# KUN — Isotropy/Parity Scope v2 Adversarial Review

Filed: 2026-08-10 23:28 KST  
Order: `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_V2_20260810T2300K.md`  
Role: attack v2 as written; no run authorized.

## Governing Bytes

- `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_V2_20260810T2300K.md`
  - SHA-256: `99a1519aa070b9fb42ef65c855b978bbb1b14b7ae08341143141b42515c79c99`
- Superseded v1 reviewed only as prior context, not authority:
  - `reviews/KUN_ISOTROPY_PARITY_SCOPE_ADVERSARIAL_20260810T2245K.md`
  - SHA-256: `bf0ac0fab619916c20bf35b6f3235ea86697f3a6825e022e2e2cf707d68092de`

## Boundary

This remains a large-scale galaxy-spin isotropy/parity scope. It is not a BHU test. BHU may be absent or a labelled personal-interest footnote only. No result, run, claim, video, publication, lane unlock, or public surface is authorized.

## Transcription Check

Hwao transcribed the seven hardenings faithfully:

1. mirror anti-equivariance necessary but not sufficient — present.
2. inherited-prior / selection-bias control on confidence and abstention after mirror-pair accounting — present.
3. GZ DESI/DECaLS `spiral-winding` forbidden as chirality — present.
4. WCS parity gate with Jacobian sign receipts and injected asymmetric test images — present.
5. expanded null covariates plus joint preservation or adversarial sky-position-predictability tests — present.
6. two instrument families as floor, not sufficiency; independence of imaging, footprint, preprocessing, classifier — present.
7. explicit `NOT_WORTH_DOING_YET` if no public chirality estimator can be frozen without new labelling — present.

I do not see a softening of my prior seven points.

## New Attack: The Inherited-prior Control Is Still Not Sufficient

The v2 inherited-prior control tests whether classifier confidence and abstention depend on sky-position-correlated covariates after mirror-pair accounting. That is necessary, but not sufficient.

A classifier can pass:

- mirror anti-equivariance: original label flips on mirrored input;
- confidence control: confidence distribution is matched across sky-position-correlated covariates;
- abstention control: abstention rate is matched across those covariates;

and still leak a sky-correlated prior through the **signed label residual** among non-abstained galaxies.

Example failure mode: in two sky regions with matched seeing, depth, redshift, size, colour, inclination, and confidence, the classifier assigns `CW` to 51.5% of borderline spirals in one region and 48.5% in another. Every object still flips under mirroring. Confidence and abstention are flat. The leakage is only visible in the conditional signed label probability after all covariates are accounted for. That is exactly the statistic a dipole test would amplify.

Therefore v2 needs a third first-class control:

**Signed-label residual / sky-predictability control.** After mirror-pair anti-equivariance and confidence/abstention balancing, the residual signed handedness must be tested for predictability from sky position or survey-region identifiers under the null. If sky position, tile/brick/camera, Galactic/systematics maps, or their low-order harmonics predict the signed label above a frozen threshold after astrophysical/covariate controls, the result is `INCONCLUSIVE`.

This is not optional. It is the actual leakage channel left open by v2.

## What the Third Control Must Freeze

A gateable v3 must specify before any statistic:

- the signed response variable, preferably pair-antisymmetrized from original/mirror logits rather than a hard label;
- the exact covariate-adjustment model or matching/binning scheme;
- the exact sky-position predictors tested: RA/Dec harmonics, Galactic coordinates, survey tile/brick/camera, footprint labels, extinction/stellar-density maps, depth/seeing/PSF maps;
- the exact adversarial sky-predictability test: e.g. can a held-out model predict signed residuals or inferred dipole contribution from non-astrophysical survey/systematics features;
- the exact threshold for declaring leakage, with leakage forcing `INCONCLUSIVE`;
- a negative-control target that should not carry chirality but shares morphology/classification difficulty;
- preservation of all failed controls and no parameter revision after seeing any leakage statistic.

If no public-data-only design can freeze that third control, the answer should be `NOT_WORTH_DOING_YET`.

## Dataset Consequence

This makes a public catalogue-only route effectively dead:

- GZ DESI/DECaLS morphology columns are not chirality and predict volunteer-style morphology.
- A volunteer-trained public model can pass mirror and confidence/abstention tests while still leaking signed residuals.
- Without either public chirality labels suitable for training or a non-learning geometric chirality estimator with frozen failure modes, a public-data-only design may not be able to close the inherited-prior problem.

The study is still scopeable, but the scope should not imply that a viable executable design already exists.

## WCS / Null / Replication Notes

- WCS parity gate remains mandatory and catastrophic: a parity sign bug silently inverts every downstream number.
- The expanded null-control covariates in v2 are good, but "joint preservation or adversarial sky-position-predictability tests" must be elevated from alternative wording to a required adversarial residual test. Joint preservation alone can miss nonlinear sky leakage.
- Two instrument families remain a floor. Preferred-axis language still requires independence of imaging, footprint, preprocessing, classifier, and training labels. If both families use the same volunteer-trained model lineage, they are not independent on the failure mode that matters.

## Verdict

V2 is materially better and faithfully carries my seven hardenings. It still needs an eighth hardening: signed-label residual / sky-predictability control after mirror, confidence, and abstention controls. Without that, a classifier can pass both v2 controls and still leak a sky-correlated prior into the parity statistic.

The next admissible product is a v3 design brief with that control frozen, or a plain `NOT_WORTH_DOING_YET` if no public-data-only route can satisfy it.

SCOPE_V2_HOLD_ADD_SIGNED_RESIDUAL_CONTROL
