# Kun acquisition-strategy gate — 2026-08-15 KST

## Verdict

**PASS_WITH_REPAIRS_FOR_STRATEGY_ONLY. HOLD EXECUTION.**

The acquisition strategy is usable only after a PC-1/input-interface amendment. The current frozen
route and the frozen estimator genuinely disagree:

- `TORI_SURVEY_ROUTE_BINDING_20260812.md` freezes `bands=grz`, `size=256`, and says the delivered
  planes are the final analysis raster.
- `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` freezes a ResNet-18-class estimator with
  **single input channel, 128x128** and a pure width-axis index-reversal mirror on the production
  raster.
- `prereg/acquisition/nm_acquire_cutouts.py` encodes the old route in source as
  `bands=grz`, `size=256`, and validates FITS shape `[3, 256, 256]`.

That is not an efficiency mismatch. It is an instrument-interface contradiction. Running the current
acquisition route would acquire pixels that the frozen estimator is not specified to consume, and
any later 256->128 or grz->one-channel transform would be an unfrozen decision made after access to
real images.

## Exact Artifacts Checked

I recomputed these hashes from disk:

| Artifact | SHA-256 |
|---|---|
| `_tmp_KUN_STRATEGY_GATE_BRIEF.md` | `5ae487b573dac97d59bc38101c9c967e5ce8ea9e5db798859af8019411badfbf` |
| `TORI_ACQUISITION_STRATEGY_20260815.md` | `e5c2aae73b672eb902f042596a380dcd9be92d3fec5b41e609a4acd622a9f481` |
| `GORU_SURVEY_ACCESS_FACTS_20260815.md` | `eea2bad24303a415b4d912ea8af51ba1b5bb17abb539141891620d708c05854c` |
| `TORI_SURVEY_ROUTE_BINDING_20260812.md` | `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87` |
| `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` | `331a941a807eef2f02e821086230655505b332b90ff1e47ff128d034334f9fc3` |
| `acquisition/nm_acquire_cutouts.py` | `5f48066b8a7d56e6d595765cca7ea762197b0473fdde2820acaa0cf59862f400` |

No survey fetch, transport, freeze, amendment, commit, push, publication, or empirical run was
performed.

## Which Side Is Wrong

**PC-1 / acquisition route is wrong for the currently frozen instrument.** The estimator appendix is
the measurement instrument: it binds the tensor size, channel count, mirror operation, deterministic
inference path, weights-freeze policy, and the synthetic identity receipts. Acquisition must deliver
exactly the estimator's input contract, not a larger product followed by an implicit conversion.

This is not a scientific endorsement of `r` band. It means:

1. If the study proceeds with the current one-channel estimator, PC-1 must be amended to an exact
   **128x128, one-band, float32 tensor contract** before any real image access.
2. The chosen band, FITS plane/HDU, nanomaggy-to-tensor conversion, background treatment,
   invalid-pixel rule, clipping/scaling, byte order, memory layout, and mirror point must be frozen.
3. Synthetic R1-R5 / retention / calibration checks must be rerun through that exact input function.
4. If the science seat determines that `g+r+z` information is required, then the estimator appendix
   is the document that must be refrozen as a three-channel 128x128 instrument before sky access.
   The present 256x256 grz route still would not be acceptable without a frozen 256->model interface.

So the default repair is PC-1, not the estimator. Changing the estimator is a separate scientific
decision, not an acquisition optimization.

## Corrected Arithmetic

I recomputed the main byte counts rather than inheriting either prior arithmetic:

| Route | Count basis | Bytes | Decimal / binary |
|---|---:|---:|---:|
| 256x256 grz cutout pixels | 832,393 objects | 654,620,491,776 | 654.620 GB / 609.663 GiB |
| 128x128 grz cutout pixels | 832,393 objects | 163,655,122,944 | 163.655 GB / 152.416 GiB |
| 128x128 one-band cutout pixels | 832,393 objects | 54,551,707,648 | 54.552 GB / 50.805 GiB |
| 128x128 one-band minimal FITS | 832,393 objects | 57,535,004,160 | 57.535 GB / 53.584 GiB |
| one-band brick raw pixels | 270,577 bricks | 14,026,711,680,000 | 14.027 TB / 12.757 TiB |
| grz brick raw pixels | 270,577 bricks | 42,080,135,040,000 | 42.080 TB / 38.272 TiB |
| one-band bricks using Goru's representative HEAD size | 270,577 x 11,911,680 | 3,223,026,639,360 | 3.223 TB / 2.931 TiB |
| grz bricks using the same representative r-band size x3 | 811,731 files | 9,669,079,918,080 | 9.669 TB / 8.794 TiB |

Tori's 42 TB rejection of downloaded bricks is superseded as a compressed-transfer estimate, because
Goru measured a representative compressed `image-r.fits.fz` size. But that correction does not make
bulk bricks the cheapest external-byte route. The representative one-band brick transfer is still
about **59.1x** the 128x128 one-band cutout pixel payload, and raw one-band bricks are about
**257.1x**.

The request-count argument also does not rescue grz bricks: `270,577 * 3 = 811,731` filter files
versus `832,393` object cutout calls, only **20,662 fewer operations** or **2.482%** fewer. A Globus
task may be operationally better than HTTP calls, but it is not the same unit as a file request.

## Public Cutouts Versus Bricks

**832,393 public cutout calls are not defensible without operator approval.** Even after the PC-1
repair to 128x128 one-band, the call count is the same. Goru's policy fact and Tori's strategy point
in the same direction: bulk automated cutouts must not proceed merely because the endpoint is public.

The correct route order is:

1. **Preferred if legitimately available:** compute beside the DR10.1 coadds, generate the exact
   amended 128x128 object products with hash-pinned code, shard and verify them, then transfer
   cutout shards with Globus. This avoids public cutout-service load and avoids transferring full
   bricks offsite.
2. **Fallback:** use public generated FITS cutouts only after a Legacy Survey operator approves the
   exact job scale, request shape, rate/concurrency, retry/backoff, and resume plan. Until then the
   old 5-second single-request policy is only an internal conservative cap, not provider permission.
3. **Rejected as default:** download all selected bricks locally and crop offsite. It is policy-cleaner
   than hammering the cutout server, but it is still much larger in external bytes and transfers WCS
   generation/cropping custody onto us.

If the operator explicitly says to use Globus bricks rather than cutouts and near-data compute is
unavailable, that becomes a new route requiring its own PC-1/PC-3/PC-4 amendment. It is not implied
by this PASS.

## PC-1 Amendment Requirements

The amendment must say at least:

- product family and version: DR10.1 South, exact source product route;
- spatial raster: exactly 128x128 at `pixscale=0.262`, or an explicitly frozen alternative if the
  estimator is refrozen;
- channel: exactly one named band, or a refrozen multichannel estimator;
- tensor conversion: FITS HDU/plane, row order, endian conversion, float32 cast, normalization,
  background, invalid-pixel, clipping, padding/no-padding, and contiguous layout;
- mirror: pure width-axis index reversal after final tensor construction, never an interpolating or
  affine transform;
- no post-delivery crop/resize/reprojection unless that transform is itself the frozen measurement
  product and has synthetic receipts;
- rerun synthetic identity/retention/calibration receipts through the exact input function before
  real image access.

## PC-3 and PC-4 If Cutting Moves Local

Local generation from bricks is not a harmless transport substitution. It moves custody from the
viewer-generated FITS product to our own cutout generator. If that route is used:

- every source brick version/hash must be pinned before use;
- object-to-brick assignment and overlap-edge rules must be exact;
- any resampling kernel, WCS target, centering convention, and pixel origin must be frozen;
- PC-3 must log the per-object WCS linear matrix, determinant, row-order transform, combined
  determinant sign, and North-up/East-left result;
- PC-4 must remain fail-closed on SIP/PV/CPDIS/D2IM/DET2IM/distortion-bearing or ambiguous WCS
  unless a separately frozen local-Jacobian-sign receipt replaces that rule;
- no nearest-pixel native crop, integer crop, or local reprojection is allowed by assumption.

This is the main way a "cheaper" route can become scientifically wrong: it can silently change the
measurement pixels or invert chirality custody.

## STOP Rule and F-10 Boundary

Nothing in the acquisition strategy weakens the STOP rule or F-10 output boundary.

- The route still stops before any real galaxy image access unless PC-1 is amended and the acquisition
  method is explicitly authorized.
- Acquisition artifacts remain private measurement inputs, not public release products.
- F-10/BS-11 still govern any future public package cumulatively. A clean acquisition route is not a
  licence decision, release approval, publication approval, Duho acceptance, or sky-result authority.
- The known BS-1/public-output boundary remains separate from the engineering route.

## Weakest Thing

The weakest remaining thing is not byte arithmetic; it is the unresolved provider/compute route. The
scientifically cleanest and lowest-load path is near-data generation beside the coadds, but that
depends on legitimate collaborator/project access or an operator-approved batch route. Without that
receipt, the acquisition plan is still a design, not an executable route.

## Final Ruling

Proceed to draft a PC-1/input-interface amendment and an operator/near-data access query. Do not fetch
pixels. Do not run the existing 256x256 grz acquisition code. Do not freeze the acquisition strategy
until the amended estimator input contract, WCS/parity custody path, and provider-approved execution
route are all hash-pinned.

This PASS authorizes only paper strategy work. It does not authorize a real image request, transport,
freeze, sky run, result, publication, commit, push, or acceptance.
