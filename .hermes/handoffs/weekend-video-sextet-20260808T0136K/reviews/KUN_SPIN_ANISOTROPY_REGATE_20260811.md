# KUN SPIN-ANISOTROPY REGATE AFTER TORI PRIOR-ART READ

Timestamp: 2026-08-11 KST

Target facts packet: `reviews/TORI_SPIN_PRIOR_ART_20260811.md`

Prior Kun packet superseded in part: `reviews/KUN_SPIN_ANISOTROPY_PREMORTEM_20260811.md`

## Verdict

WORTH SCOPING, BUT ONLY AS A NARROW DESIGN BRIEF WITH HARD KILL SWITCHES.

My earlier `NOT_WORTH_DOING_YET` was too broad. Tori's full-methods read shows that Patel & Desmond 2024 is a strong label-level statistical reanalysis, not the image-pipeline study Lana proposed. It does not generate handedness labels from imaging, does not run its own mirrored-input classifier control, and does not perform preregistered fixed-axis tests at Longo's or Shamir's published axes. Therefore my prior-art blocker does not cover Lana's design as stated.

That correction does not make the design automatically safe. It makes the remaining gap smaller and sharper:

> Has anyone combined image-level handedness generation, end-to-end orientation custody, mirror/anti-equivariance controls, inherited-prior leakage controls, and preregistered fixed-axis tests at the two published claim axes?

Tori found no. That is a real gap, not merely a wording difference. It is also a thin enough gap that the next artifact must be a design brief, not a run.

## 1. Does The Original Blocker Survive?

Partly, but narrower.

The part that does **not** survive: "Patel & Desmond already did the direct public-data reanalysis" cannot be used to block Lana's image-pipeline design. They accept existing labels at face value and ask whether those labels support anisotropy under better statistics. That is not the same as generating new labels from raw imaging with a mirrored-input control.

The part that **does** survive: Patel & Desmond remains a strong warning that label-level free-axis claims are already heavily contested and that a loose reanalysis of public spin tables adds little. Any design that uses downstream labels as the primary instrument, or merely re-runs broad free-axis searches, should still be blocked as already-covered or too manipulable.

So the corrected gate is:

- label-table reanalysis: NOT_WORTH_DOING_YET;
- image-level, custody-audited, mirror-controlled, preregistered fixed-axis test: WORTH SCOPING;
- immediate empirical run before that design is frozen: BLOCK.

## 2. Is The Residual Gap Real Or Thin?

It is real, but thin.

It is real because Tori's matrix shows the components exist separately, not together:

- Shamir 2024 HSC: own HSC labels plus a reported mirrored rerun, but no published paired original/mirror outputs, no formal antisymmetry identity, unresolved image-format/orientation custody, and no preregistered fixed-axis tests.
- Jia, Zhu & Pen 2023: CE-ResNet enforces reflection equivariance, but uses SDSS/DESI JPEGs and Galaxy Zoo 1 training labels, with no anisotropy axis test.
- Tadaki et al. 2020: HSC CNN with flipped-label augmentation, but not an enforced reflection-equivariant architecture and no sky-axis anisotropy test.
- Stiskalek & Desmond 2024: label-level HSC reanalysis assuming Shamir labels are correct.
- Patel & Desmond 2024: broad label-level statistical adjudication, not image-level relabelling.

It is thin because a null at two historical axes after a broad free-axis null is not automatically interesting. Its value is not "we searched and found no dipole." Its value would be:

> At the exact axes where the claim papers reported signals, a newly generated, mirror-controlled, orientation-audited instrument either does or does not reproduce the sign and amplitude class.

That is a confirmatory test of specific published claims, not a discovery search. If the design drifts back to a free-axis dipole hunt, it becomes weak immediately.

## 3. CE-ResNet And The GZ1 Bias Problem

Reflection equivariance does **not** null inherited label bias by construction.

It nulls one important failure mode: the architecture cannot give different Z and S estimators merely because the image was reflected. For a given image and its mirror, the signed output is constrained to flip. That is a necessary property.

It does not prove that the classifier learned an unbiased physical handedness rule. A model trained on Galaxy Zoo 1 labels can still inherit the human training set's mistakes in at least three ways:

1. **Feature-conditioned label bias.** If humans mislabeled ambiguous, small, low-S/N, inclined, redder, or arm-poor spirals asymmetrically, the network can learn a decision boundary contaminated by those label errors while still flipping perfectly under mirroring.
2. **Confidence and abstention leakage.** The signed label may anti-equivariantly flip, while confidence, rejection rate, or effective sample membership varies with morphology, survey depth, Galactic foregrounds, or sky position. That can create a spurious dipole in the accepted sample.
3. **Sky-correlated training composition.** If the human-labelled training set or survey images carry sky-position-correlated quality/covariate structure, the model can learn a prior that is invisible to a per-image mirror flip test.

So CE-ResNet is a good component, but not a sufficient instrument for this study if used as trained on GZ1 labels without additional leakage tests. This is exactly the inherited-prior problem from the isotropy scope, in a more concrete form.

There is a possible contribution here separate from the axis test: showing, with frozen diagnostics, whether a human-label-trained equivariant classifier suppresses or preserves the GZ1 handedness asymmetry. But that would be a classifier-bias study, not a cosmological anisotropy result.

## 4. What Would Have To Be True For A Green-Lit Design Brief

I would green-light a design brief if it freezes all of the following before any result statistic:

1. **Instrument choice.** Primary instrument must not be a human-label-trained classifier unless the design is explicitly a bias-transfer study. For the anisotropy test, prefer a deterministic/geometric arm-winding estimator or a classifier trained without GZ1-style human chirality labels. If CE-ResNet is used, it must be secondary or must come with a frozen inherited-prior leakage plan strong enough to disqualify it.
2. **Image custody.** One public imaging source, one cutout route, exact versions, FITS/WCS parity validation, row-order handling, and injected asymmetric test images. A silent parity inversion is fatal.
3. **Mirror evidence.** Publish or freeze paired original/mirror outputs, not just a prose statement that mirroring works. Required receipts: mismatch rate, flip-balance statistic, confidence/abstention deltas, and exclusion-rate deltas.
4. **Inherited-prior and selection controls.** Test label, confidence, and abstention dependence on sky-correlated covariates after mirror-pair accounting: survey footprint, depth, seeing/PSF, Galactic extinction, stellar density, crowding/deblending, angular size, inclination proxy, colour/arm-contrast proxies, and redshift/magnitude where available. Ambiguous leakage returns INCONCLUSIVE.
5. **Fixed axes first.** Primary tests are preregistered at Longo `(l,b)=(52,68.5)` and Shamir `(RA,Dec)=(132,32)`, with coordinate conversion and sign convention frozen. No free-axis result may be interpreted until the fixed-axis tests are reported.
6. **Multiplicity and stopping.** If any exploratory or global search is included, it is secondary, multiplicity-corrected, and cannot rescue a failed fixed-axis test. One run, no parameter revision after any statistic.
7. **Prior-art boundary.** The brief must state plainly that Shamir HSC 2024 and Jia/Zhu/Pen 2023 already cover major components. Our contribution is only the combination plus preregistration and custody, not invention of mirror control or reflection-equivariant classification.

If any of these cannot be frozen, the correct verdict returns to NOT_WORTH_DOING_YET.

## 5. Answer To The Main Judgment Call

The residual gap is worth a design brief, not because a two-axis null would be dramatic, but because it is the first clean way to separate two claims that have been mixed throughout this literature:

- "These public labels imply a dipole under some statistic."
- "The sky has a spin anisotropy that survives an instrument designed not to create it."

Patel & Desmond addresses the first. Lana's corrected design aims at the second. Tori's facts show that no reviewed prior paper combines every required element.

The weakest thing remains the classifier. If the primary handedness instrument is trained on GZ1 or similar human labels, mirror equivariance is not enough. The study could pass the mirror self-test and still carry a sky-correlated inherited prior through confidence, abstention, or morphology-dependent label errors. That must be treated as the central kill switch, not as an implementation detail.

## Plain Verdict For Duho

Change my prior verdict.

WORTH SCOPING as a narrow design brief for a preregistered fixed-axis, image-level, mirror-controlled spin-anisotropy test. Not worth running yet. Not worth doing as another label-table reanalysis. Not a BHU test.

Safe to claim now:

> Patel & Desmond 2024 does not exhaust the image-level, mirror-controlled, fixed-axis design; it exhausts much of the public-label statistical reanalysis route.

Safe design target:

> Test whether a newly generated, orientation-custodied, mirror-controlled handedness instrument reproduces or rejects the Longo and Shamir published-axis signals under preregistered statistics.

Not safe:

> CE-ResNet's reflection equivariance alone removes inherited Galaxy Zoo handedness bias.

Not safe:

> A null from broad free-axis label reanalysis settles every possible image-level spin-anisotropy test.

Not safe:

> Any positive spin result supports BHU. It would be a spin-anisotropy/statistical-isotropy result only.
