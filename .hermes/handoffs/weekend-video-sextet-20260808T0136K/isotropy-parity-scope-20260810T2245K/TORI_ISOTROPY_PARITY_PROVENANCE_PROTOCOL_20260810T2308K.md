# Tori isotropy/parity provenance feasibility protocol

Marker: `TORI_ISOTROPY_PARITY_PROVENANCE_PROTOCOL_20260810T2308K`

Governing order: `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_20260810T2245K.md`, SHA-256 `681856e9b60bfb88c5d8c926a8089b930789355516c9b926f80661ca7bb01e7d`.

This is a large-scale galaxy-spin isotropy/parity study scope. It is a mainstream question with a live literature dispute. It is not a BHU test. BHU may appear only as a labelled personal-interest footnote or not at all; no detection would uniquely confirm it and no null would kill it.

Scope only: no data acquisition, inference run, statistic, result, claim, video, publication, cockpit/wiki mutation, lane activation, or Git/runtime action. Public data only; no new human labelling. Existing catalogue analyses are treated as constraints rather than rerun for a preferred answer.

## Candidate set

The gate covers every galaxy-study candidate named in the Hwao/Goru inventory or Kun review:

1. DESI Legacy Survey / DECaLS imaging.
2. Galaxy Zoo DECaLS + released Zoobot models.
3. Galaxy Zoo DESI + released Zoobot models.
4. SDSS DR17/DR18 imaging + public morphology models.
5. Euclid Q1 imaging + morphology products/models.
6. Rubin DP1 and EDP2 imaging.
7. HSC DR3 public spin catalogue.
8. DESI DR1/DR2 spectroscopy as a support layer.

Planck, ACT, and SPT are not galaxy-handedness candidates and are recorded only as out-of-scope contextual datasets.

## Required primary-documentation checks

For each candidate:

- immutable release/product identity and public access;
- coordinate frame and epoch;
- image product and per-image WCS metadata;
- image parity as delivered, or the documented information needed to derive the local pixel-to-sky Jacobian determinant sign;
- position-angle zero point, direction, and modulo convention where relevant;
- handedness field name, values, sign mapping, null/sentinel behavior, and mirror transformation where present;
- classifier target schema, public weights/code, preprocessing, augmentations, and whether the target is human-label prediction or independent geometry;
- footprint/instrument partition, row-selection and duplicate policy, and cross-match key.

Grades are exactly `DOCUMENTED`, `UNDOCUMENTED`, or `NOT-YET-CHECKED`. A product can be documented as ineligible because the required field is absent. Any missing load-bearing convention fails design admission regardless of catalogue size.

## Binding methodological split

Mirror anti-equivariance is necessary but not sufficient. The eventual scope, if any candidate survives, must separately control inherited human-label priors in confidence, abstention, and sample selection. A model can flip every mirrored label correctly while retaining sky-correlated selection bias.
