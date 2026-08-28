# KUN — Quasar Dipole Design Brief Gate

Filed: 2026-08-11 10:19 KST  
Order: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_ORDER_20260811T0845K.md`  
Gated artifact: `GORU_QUASAR_DIPOLE_DESIGN_BRIEF_20260811T0959K.md`

## Exact Bytes

- Order SHA-256: `26b6f2954e3a0fd2b28ec5635c67c7a3c3c0d2b20702239190c18e9fe6c1229f`
- Goru design brief SHA-256: `e11b72b14959bfa0cb83161bbc2f588e86a2a4a4c2cc717fc9c2110061443b7f`
- Tori superseding provenance correction v2 SHA-256: `89a0256617dd82ad35dd4d4a165c01356f2d86eca228d14324a765e2f30c41c2`
- Tori correction v2 receipt SHA-256: `bf12d1cf956debf25b56e623bf8eb2947f2e5d74122fd54f30bebf16341cc55d`
- Lana cosmic-anisotropy frame SHA-256: `701d1ae3b70b6a61cd17bc774ad063e92432d67cbb2ff8cdb21f15fb7fac210d`
- Goru overnight inventory SHA-256: `25324bfe7864422bdd136c8666a1cd657fe326e084e51459ef359df8cc084689`
- Kun overnight recommendation SHA-256: `63fbb79aec3c2f8251aaba76b40f7f9ffebcfe743878bd5e092b87df8b6df32c`

## Verdict

HOLD. Do not run from this design brief.

The brief has the right claim boundary and the right high-level null, but it does not yet satisfy the freeze standard. It still asks a loose enough question that catalogue identity, mask identity, thresholds, correction model, and decision rule can move the result.

## Blocking Defects

1. **Catalogue identity is not pinned.**

The brief names `CatWISE2020_Secrest_v3.fits` and says DOI `10.5281/zenodo.4431089` **"or the exact Zenodo repository matching the Secrest v3 release."** That "or" is a gate failure. A freeze must name one DOI/record/version, one file path, checksum, byte count, schema, and row count.

Tori's superseding correction v2 specifically names Zenodo record `8303800` for the Secrest v3 package. The brief does not bind that exact record, and it does not carry checksums or byte counts.

2. **Core catalogue choice conflicts with Tori's superseding recommendation.**

Tori v2 says `QUAIA_V1_PUBLIC_PACKAGE` is the provenance-side single design-brief recommendation, with CatWISE as `DOCUMENTED_CONDITIONAL_RECONSTRUCTION` and NVSS as `DOCUMENTED_CONDITIONAL_RECONSTRUCTION_SUPPORT`.

The brief instead makes CatWISE the core and uses NVSS only as a quoted convention source. That may be scientifically defensible later, but the brief does not explain why it overrules the stronger Quaia provenance package with released selection functions/randoms. If the core is CatWISE, the missing final-row manifest and flag policy must be frozen first. If the core is Quaia, this brief names the wrong catalogue.

3. **Mask identity is not frozen.**

`CatWISE_v3_mask_NSIDE64.fits` is named, but no source path, record, checksum, byte count, HEALPix ordering, coordinate frame, mask-value convention, or exact composition order is pinned. The prose describes Galactic and ecliptic cuts, but the order requires one exact versioned mask, not a reconstructed mask recipe.

4. **Flux-threshold ladder creates unclosed researcher degrees of freedom.**

The brief freezes three thresholds: `W1 < 16.5`, `W1 < 16.0`, and `W1 < 15.5`. It does not state which threshold is primary, how the three are combined, whether any one threshold exceeding `3.0σ` counts as rejection, or how multiplicity/look-elsewhere is handled.

This is exactly the classic route to a manufactured dipole amplitude. Tori also notes the published final CatWISE result applies `W1 < 16.4`; the brief does not justify substituting `16.5` or omitting `16.4`.

5. **Selection-function correction is not a pinned correction.**

The brief says "joint regression against three mapped priors" but does not freeze:

- regression model family
- link function
- pixelization and smoothing
- coefficients fit/frozen policy
- train/test split
- mask interaction terms
- treatment of zero-count pixels
- residual-systematics stopping threshold
- how uncertainty in the correction enters the dipole covariance

It names WISE artifact maps and SFD98 dust, but the order requires one selection-function correction with published systematics maps named. A vague regression is not a correction.

6. **Kinematic convention is not quoted verbatim from primary documentation.**

The brief labels the kinematic convention "quoted verbatim" but uses ellipsis and a generic flux-transform sentence. A quote with ellipsis is not an exact frozen convention, and the equation shown is not enough to define the number-count dipole expectation.

The freeze must quote the actual primary formula/convention, including the Ellis-Baldwin amplitude convention, source-count slope `x`, spectral index `α`, velocity vector, sign convention, and whether the comparison is map subtraction, mock injection, or posterior model comparison. Tori v2 warned these are load-bearing.

7. **Decision rule lacks INCONCLUSIVE gates.**

The brief has only rejection at `>=3.0σ` and consistency at `<3.0σ`. It does not state INCONCLUSIVE for:

- failed catalogue/mask/hash verification
- failed row-manifest reconstruction
- disagreement between threshold ladder elements
- excess disappearing under a required systematics sensitivity
- residual power in non-dipole multipoles
- correction model failing validation
- Quaia/CatWISE/NVSS disagreement
- covariance or mock failure

The order requires ambiguity to force INCONCLUSIVE. This brief still lets a marginal or systematics-sensitive value be narrated into a clean binary outcome.

8. **One-run receipt shape is underspecified.**

"Computed once" is stated, but the brief does not freeze the exact script path/hash, input manifest, output path, receipt fields, failed-run preservation rule, stdout/stderr capture, environment, random seeds, or prohibition on rerunning after a crash that printed partial statistics.

9. **NOT_WORTH_DOING_YET branch is backward.**

The brief says if it merely reproduces Secrest without a novel correction, declare `NOT_WORTH_DOING_YET`. That is correct in spirit, but it is decided after seeing the result. The brief must answer before run whether it adds a new control relative to published analyses. As written, it risks running first and then deciding whether the work was worth doing.

## Published-analyses Question

The published analyses do not settle the full quasar/radio dipole dispute. The live fight is specifically about measurable selection/systematics power and catalogue dependence. So I do not recommend `NOT_WORTH_DOING_YET` for the entire probe.

But this CatWISE-only brief may be `NOT_WORTH_DOING_YET` unless it adds a frozen control not already in Secrest/Abghari-style work. Tori's v2 evidence points toward a Quaia-centered design as the cleaner public-data next step because Quaia ships selection functions and randoms. CatWISE/NVSS can be reconstruction or support checks after their row/mask/flag identities are pinned.

## Required Before Re-gate

A gateable v2 brief must provide one of these two clean routes:

1. **Quaia core route:** one exact Quaia v1 package, checksums, one exact selection-function map/random package, one primary magnitude/redshift/sample cut, one kinematic convention with frozen `x`, `α`, vector/sign, and a single decision rule.

2. **CatWISE core route:** exact Zenodo record/file/checksum/schema, immutable final `W1 < 16.4` row manifest or a pre-justified alternate primary threshold, exact mask checksum, exact artifact/flag policy, and a frozen correction model that is demonstrably new relative to published CatWISE analyses.

Either route must freeze one primary threshold or a predeclared multi-threshold global test with multiplicity correction; exact INCONCLUSIVE conditions; exact one-run receipt; and no selectable "or" language.

Until then, no statistic should be computed.

HOLD_DESIGN_BRIEF_FREEZE_NOT_GATEABLE
