# Kun PC-1 input-contract amendment gate — 2026-08-15 KST

## Verdict

**PASS_PC1_AMENDMENT_FOR_V3_DRAFTING. HOLD EXECUTION.**

Lana's PC-1 amendment passes as a documentation/input-contract amendment. The correct repair is to
amend PC-1 and the acquisition/input route to the frozen estimator's interface: **128x128, one band,
float32**, with no hidden 256->128 crop or grz->single-channel reduction. The estimator does **not**
need to be refrozen merely because the old route requested `grz`; it would need refreezing only if
the science decision were that multiband information is required for adequate sensitivity.

No fetch, no route execution, no v3 freeze, no commit, no push, no publication, and no acceptance
follows from this gate.

## Exact Artifacts Checked

Hashes recomputed from disk:

| Artifact | SHA-256 / mode |
|---|---|
| `_tmp_KUN_PC1_AMENDMENT_GATE_BRIEF.md` | `ebec9cf6af49b414cbd4a2e88dff267ae5995f3ad643f9af5f342ed115f6ea19` |
| `LANA_PC1_INPUT_AMENDMENT_20260815.md` | `c8fc19716ffb5619cf92c5b5d198918030f8a13cc7636b3a524a8cfb807e7a6e` |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md` | `62dad44dd92acf2781d2c8cf25161f7f344e3fe6f7fec35b7e04308bd1539c12`, mode `444` |
| `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` | `331a941a807eef2f02e821086230655505b332b90ff1e47ff128d034334f9fc3` |
| `TORI_SURVEY_ROUTE_BINDING_20260812.md` | `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87` |
| `acquisition/nm_acquire_cutouts.py` | `5f48066b8a7d56e6d595765cca7ea762197b0473fdde2820acaa0cf59862f400` |

The frozen v2 preregistration file is unchanged against the supplied hash and is read-only on disk.

## 1. The 256/grz To 128/one-Channel Defect

Confirmed. The reduction step was never frozen.

The old route binding freezes `bands=grz`, `size=256`, delivered planes as final analysis rasters,
and no post-delivery resize/reprojection/interpolation. The estimator appendix freezes a
single-channel `128x128` trunk and a mirror operation on the exact tensor consumed by the model.
The build-only acquisition source still encodes the old route and validates `[3, 256, 256]`.

There is no frozen rule for:

- choosing `g`, `r`, `z`, or combining them;
- cropping or downsampling `256x256` to `128x128`;
- background/normalization/clipping from survey nanomaggies into model tensor values;
- treating invalid pixels before inference.

Lana's replacement closes the structural defect by making delivered pixels equal consumed pixels:
`bands=r`, `size=128`, one image plane, float32 tensor `(1, 128, 128)`, no downstream reduction step.

## 2. Parity Argument

The parity argument is sound for the question it needs to answer: **can colour manufacture the
chirality sign under the frozen antisymmetric estimator?** No.

A multiband image is a stack of scalar fields on the same pixel grid. A pure mirror reverses the
spatial index and preserves the per-pixel band values as values. The chirality sign is carried by
the handed spatial arrangement of structure. Colour can make arms easier or harder to identify, and
therefore can change attenuation, abstention, and power. It is not a separate parity-odd sign channel
that makes `grz` necessary to define clockwise versus counterclockwise.

This statement has an important boundary. It does **not** mean band choice is irrelevant. Colour can
affect sky-correlated sensitivity through extinction, sky brightness, depth, colour population, and
arm contrast. That is the uncovered channel Lana identifies as monopole x sensitivity-gradient
coupling. Those effects can bias a dipole test through sample weighting or attenuation if the
controls fail. The amendment handles this correctly by routing the issue to the R1-R5 rerun, HC-1H
attenuation, HC-5/HC-6 floors, and the covariate battery, rather than pretending parity alone proves
equal power.

So the one-band choice is admissible as a bias-control decision. A bad band can make the run
INCONCLUSIVE-BY-POWER; it does not by itself create a hidden chirality-sign convention. If the rerun
or HC-1H shows inadequate sensitivity, the correct next step is the stated one: stop and refreeze a
three-channel `128x128` estimator before sky access.

## 3. Choice Of `r`

`r` is a defensible primary band for this amendment, but the strength of the justification must not be
overstated. The solid reasons are:

- the parent selection is already `r`-anchored through `flux_r`, dereddened `r`, and size cuts;
- `r` avoids the strongest blue-band extinction sensitivity and the redder-band sky/airglow extreme;
- if `g` or `z` would improve arm contrast or reduce systematics, that would appear as measured
  sensitivity/retention/covariate behavior before sky access.

The `[VERIFY]` markers on exact extinction coefficients, arm-contrast ordering, and GZ DECaLS
selection imagery are acceptable in this amendment draft because the amendment does not quote exact
values and does not authorize sky access. They must be filled from primary sources, or the associated
sentence must be removed, before the text is incorporated into a frozen v3 or used downstream as a
source-backed rationale.

## 4. Condition 2 Coverage

Condition 2 is covered at the right level for an amendment draft:

- band: frozen to `r`;
- shape: frozen to one `128x128` plane;
- units: delivered nanomaggies before scaling;
- background: no extra background estimation/subtraction beyond survey product;
- invalid pixels: NaN/Inf replacement and invalid-fraction cap named;
- scaling: monotone nanomaggy-to-tensor map named as a binding slot;
- byte order/layout: float32 little-endian C-order `(1, 128, 128)`;
- mirror point: pure width-axis index reversal after tensor formation.

Open slots remain, but they are named and have pre-sky fill rules:

- exact image HDU/plane for the single-band FITS response;
- invalid-fraction cap;
- exact monotone scaling function and constants;
- synthetic equivalence/background behavior through the new input function.

Those slots are not cosmetic. They must be filled and hash-pinned before sky access.

## 5. Rerun Prerequisite

The R1-R5 / retention / calibration rerun is stated as binding, not merely mentioned. Lana explicitly
says the old receipts were produced on the old input path, are invalid as evidence about the new
instrument-as-consumed, and must be rerun through the exact IC-1...IC-7 function before sky access
and before Kun gates that successor receipt.

That closes my condition 3 at the amendment level. It does not close the future rerun itself.

## 6. Boundaries Carried

The amendment correctly preserves the surrounding gates:

- BS-1 still FAILED as written;
- F-10 and BS-11 remain untouched;
- HC-1H remains untouched;
- STOP remains before any real image access;
- K-1...K-14 remain binding;
- K-8 is explicitly stated as untripped because no real-sky statistic, chirality label, or sky
  estimand exists.

It also correctly says it fixes the input contract, **not** the delivery route. The acquisition
channel still requires a separate route decision and operator/near-data receipt.

## Repairs Required Before Freeze Or Execution

These are not blockers to this amendment gate, but they are blockers to any v3 freeze or sky access:

1. Fill or remove the `[VERIFY]` rationale claims from primary sources before the amendment text is
   presented as source-backed frozen rationale.
2. Produce Tori's successor route binding for the exact single-band FITS schema, including HDU/plane
   identity.
3. Produce Yui's hash-pinned input-function receipt: invalid-pixel cap, monotone scaling map, code
   hash, tensor layout, and R1-R5 / retention / calibration rerun through that exact function.
4. If local cutting from bricks replaces service cutouts, re-gate PC-3/PC-4 on that local path before
   any real-image run.
5. Do not execute the existing `nm_acquire_cutouts.py` route until its hardcoded `grz`, `256`, and
   `[3, 256, 256]` assumptions are replaced or superseded by a separately gated implementation.

## Final Ruling

The amendment answers the core question correctly: the old PC-1 route is wrong; the current estimator
does not need refreezing on parity grounds. Colour can affect sensitivity and power, but under the
antisymmetric mirror construction it is not an independent chirality-sign channel. Therefore one-band
`r` is admissible as the amended input contract, subject to the named pre-sky rerun and custody
receipts.

Proceed to v3 drafting and successor route/input-function receipts. Hold all execution.
