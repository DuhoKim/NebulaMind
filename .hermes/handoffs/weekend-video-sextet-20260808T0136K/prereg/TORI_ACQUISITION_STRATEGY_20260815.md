# Tori acquisition-strategy audit — cheapest correct route

- Date: 2026-08-15 KST
- Scope: documentation, already-held aggregate brick counts/geometry, and arithmetic only
- Empirical boundary: **zero new survey-product requests; zero cutouts; zero bricks; zero service probes**
- Status: **STRATEGY COMPLETE; ACQUISITION CLOSED**
- Acceptance: Duho only; a fresh Kun gate is required before any empirical execution

## Executive verdict

Duho's revised magnitude check is right. Under the stated four-byte-pixel assumption, downloading g+r+z images for all 270,577 occupied 3600×3600 bricks would carry **42.080 TB decimal = 38.272 TiB** of uncompressed image pixels. The frozen 256×256 g+r+z cutout population carries **654.620 GB decimal = 609.663 GiB** of pixels. Bulk bricks are therefore **64.2817× larger**, not cheaper.

The original request-count argument is not right for direct web files. The documented brick product is one `image-<filter>.fits.fz` file per filter, so g+r+z means **811,731 files**, not 270,577. That is only 20,662 fewer file operations than 832,393 three-band cutout calls: a **2.482%** reduction. The apparent threefold request saving exists only if “one Globus transfer task” is substituted for “one HTTP file request”; those are not equivalent units. The product is explicitly filter-separable and the brick stacks are 3600×3600 TAN images at 0.262 arcsec/pixel. [1][2]

The density-based hybrid is not worth a second acquisition path. Only one locally counted brick crosses either byte threshold. It saves 0.801 GB at 256 g+r+z or 0.084 GB at 128 g+r+z—at most **0.122%** of the cutout volume—while adding local WCS/cropping, DR10.1-version, and custody risk.

There is a more important blocker: the existing frozen documents do not define an executable estimator input. `TORI_SURVEY_ROUTE_BINDING_20260812.md` freezes a **256×256 raster per g/r/z band**, prohibits resize, and calls the delivered pixels final. `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` freezes a **single-input-channel 128×128** network; its production receipt tests a **128×128 float32** raster. The controlling documents specify neither a 256→128 crop nor a g+r+z→one-channel mapping. They also do not specify how nanomaggy sky pixels are background-treated, normalized, clipped, or converted to the synthetic estimator's tensor range. The current 256-g+r+z route is therefore not “correct but slow”; it is **interface-incomplete and must not run**.

The cheapest candidate that can be made scientifically and operationally correct is:

1. amend PC-1 before sky access to an exact **128×128, one-band, float32** input contract;
2. freeze the chosen band and the complete nanomaggy→estimator normalization/background/invalid-pixel procedure on synthetics only;
3. if collaborator compute access beside the NERSC coadds exists, run the exact hash-pinned cutout generator there, stage sharded outputs, and transfer only the resulting cutouts with Globus;
4. otherwise use public 128×128 cutouts only after the Legacy Survey operator approves a batch/rate plan for 832,393 calls.

The byte-minimal one-band candidate carries **54.552 GB** of pixel data and at least **57.535 GB** as one-HDU FITS files. It is twelve times smaller than the currently frozen 256-g+r+z payload and 257.127 times smaller than one-band full bricks. However, **`r` is only a proposed band, not an authorized scientific choice**. If the primary instrument truly needs all g+r+z information, it must instead be refrozen as a three-channel 128×128 instrument; that route carries 163.655 GB of pixels and at least 167.810 GB as FITS.

No acquisition route is open today. The exact next action is a paper-only PC-1/input-interface amendment plus an operator query; not a canary and not a download.

## 1. Controlling local evidence

This audit used only the following already-held artifacts:

| Artifact | SHA-256 | Use |
|---|---|---|
| `_tmp_TORI_ACQUISITION_STRATEGY_BRIEF.md` | `e5cf311148f87deefdac124bc02ba4e686e60ab61a587586d649b32d0baecccc` | controlling task and no-fetch rule |
| `TORI_SURVEY_ROUTE_BINDING_20260812.md` | `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87` | current PC-1/PC-3/PC-4 route |
| `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` | `331a941a807eef2f02e821086230655505b332b90ff1e47ff128d034334f9fc3` | frozen 128×128, one-channel architecture |
| `YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md` | `b4e2f5b5f92fc881ec2a0a35e84515fd05057c1051bff516cad7acae3609e18a` | frozen 128×128 float32 identity receipts |
| `acquisition/nm_acquire_cutouts.py` | `5f48066b8a7d56e6d595765cca7ea762197b0473fdde2820acaa0cf59862f400` | build-only request/WCS/custody implementation |
| `combined_per_brick_counts.csv` | `4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0` | aggregate `BRICKID, COUNT(*)` density only |
| `STATIC_PRODUCT_CUSTODY.json` | `5e969bf623ec07a0366355fb5f723b31e4365fd7e03ccc07e1addd32f379881a` | already-held South brick geometry custody |
| `legacy_dr10_south_header_verification_r_16px.receipt.json` | `a573d8993b40cfbde143f9bd653cf7579dc1e73467a04fb9ed36b716efbc77e6` | prior permitted generated-FITS shape/dtype receipt |
| `_tmp_HWAO_ACQUISITION_STRATEGY_RELAY_RECEIPT.md` | `0eb3929433919cfae06dc9dd7663330379e5b60be90e85b41cbbd3bcd47b808f` | coordinator scope receipt |
| `_tmp_acquisition_strategy_arithmetic.json` | `18b1c420261db80dca051483285b19d35ea48ecc442f9b8275c3f31287fdc1dc` | machine-reproducible arithmetic |
| `_tmp_acquisition_strategy_citations.json` | `dc0fbd27bd708f64211a67529918ff60731f650b5b928a5853f803dab59c11c9` | quote-backed web-source ledger |

The aggregate file contains no object positions. Its 270,577 rows sum exactly to 832,393 selected objects. The already-held brick-geometry receipt records 366,912 unique South brick IDs and states that it was acquired for local brick-centre geometry only; this audit did not reopen it or export coordinates.

The prior permitted 16×16, one-band generated-FITS receipt records `dtype=>f4`, a TAN WCS, no distortion keywords, and 5,760 bytes. This supports four bytes per generated-cutout pixel. It does **not** prove the compressed transfer size or on-disk dtype of every brick image, so the brick totals below remain explicitly conditional on four bytes per uncompressed pixel.

## 2. What the survey documentation establishes

### 2.1 Bricks

The DR10 documentation states that image stacks are TAN projections, 3600×3600 pixels at 0.262 arcsec/pixel, North-up, and overlap adjacent images by approximately 130 pixels. [1][2] The documented coadd image filename contains `<filter>`, and each file covers a 0.25°×0.25° brick. [2] Therefore:

- g+r+z is three brick image files, not one;
- a one-band brick variant is technically separable;
- nominal full-image pixels per band are `3600² = 12,960,000`;
- the existing overlap is ample in width for a 128-pixel crop from a correctly assigned primary brick, but bounds still must be checked per object rather than assumed.

The official DR10 description lists the **entire South `coadd/` tree at 60 TB**. That tree contains more than the selected g/r/z image subset, so 60 TB is context—not an estimate of the proposed subset. [1]

Brick images are published as `.fits.fz`, but the checked documentation does not publish an image-only compression ratio for these 270,577 selected bricks. [2] No file-size crawl, HEAD sweep, sample brick, or product request was performed. Consequently:

- **42.080 TB** is the exact uncompressed g+r+z pixel total under float32;
- **14.027 TB** is the corresponding one-band total;
- actual compressed transfer volume is **unknown**;
- compressed bricks would have to be below 1.556% of raw size (>64.28:1 compression) to beat 256-g+r+z cutout pixels, or below 0.389% (>257.13:1) to beat 128 cutouts. No checked documentation supports either ratio.

The DR10 known-issues page says affected coadd files were completely replaced for DR10.1 and recommends using the latest versions. [8] A brick path therefore creates an additional fail-closed requirement: bind the current published file hash/version for every selected brick rather than inferring “DR10.1” from an old local filename.

### 2.2 Viewer cutouts

The official viewer documentation allows an explicit FITS band list and image size. It says the normal cutout route resamples released brick products into the requested WCS grid; `subimage` instead returns unresampled pieces from every overlapping brick. [3]

For this preregistration, the normal generated-FITS route is the closer match to existing PC-1 because PC-1 already defines the delivered generated TAN raster as the measurement product. `subimage` is not a cheaper drop-in substitute: it may return multiple overlapping brick images, includes a different WCS/custody form, and would require a new assembly rule.

Spatially, **128×128 is the true minimum correct raster for the frozen estimator**. Smaller input would need padding or resizing, and 256 requires an undefined crop. Both would alter the frozen interface. The band minimum is not yet resolved: the estimator is one-channel, while PC-1 currently asks for three bands.

### 2.3 Published service guidance

The checked Legacy Survey documentation explains URL construction, arbitrary size/band selection, multiple cutouts via command-line tools, temporary-file custody, and the existence of rate limiting. A Legacy Survey operator states that rate limiting returns HTTP 429. [3][4]

None of the checked DR10 description, files, viewer tips, URL examples, contact page, or operator reply publishes a numeric safe spacing, requests/second quota, daily quota, or approved batch size. Therefore:

- the current **5-second interval is an internal conservative policy**, not a published NOIRLab/Legacy-approved rate;
- 48.171 days is the arithmetic floor under that internal policy, not a provider commitment;
- lowering the interval based on guesswork is not authorized;
- the documented escalation point is the Legacy Survey help desk. [7]

The operator also recommends writing to a temporary file and renaming only after successful completion, which agrees with the built acquisition pipeline's atomic response custody. [4]

## 3. Recomputed route table

All payload totals below use `832,393` objects and `270,577` occupied bricks. “Minimum FITS” assumes one 2,880-byte header block plus standard 2,880-byte data padding; actual headers may be larger. Brick transfer bytes remain unknown because `.fits.fz` compression was not sampled.

| Route | Public calls/files | Pixel payload | Minimum persistent FITS / raw brick disk | Pacing / wall evidence |
|---|---:|---:|---:|---|
| Current 256×256 g+r+z cutouts | 832,393 calls | 654.620 GB / 609.663 GiB | ≥659.255 GB / 613.979 GiB | 48.171 d at internal 5 s; provider rate unknown |
| 128×128 g+r+z cutouts | 832,393 calls | 163.655 GB / 152.416 GiB | ≥167.810 GB / 156.286 GiB | same call-count floor |
| 128×128 one-band cutouts | 832,393 calls | 54.552 GB / 50.805 GiB | ≥57.535 GB / 53.584 GiB | same call-count floor |
| Full g+r+z bricks | 811,731 filter files | 42.080 TB / 38.272 TiB raw | compressed transfer unknown; 42.080 TB if expanded float32 | no documented completion time |
| Full one-band bricks | 270,577 filter files | 14.027 TB / 12.757 TiB raw | compressed transfer unknown; 14.027 TB if expanded float32 | no documented completion time |

This resolves the unit confusion in the initial estimate:

- “~610 GB” is actually **609.663 GiB** or **654.620 GB**;
- “~38 TB” is actually **38.272 TiB** or **42.080 TB**;
- dividing like units gives **64.2817×**.

At a hypothetical sustained link rate, transfer-only time is `bytes×8/rate`; it is not an observed wall time. For example, 42.080 TB raw takes about 3.90 days at 1 Gbit/s, while 654.620 GB takes about 1.46 hours. Public cutout generation and pacing dominate the latter route, which is why near-data batch extraction is preferable if available.

## 4. Density and hybrid crossover

The local aggregate distribution is sparse:

- mean 3.076 objects per occupied brick;
- median 2;
- nearest-sample p90 6, p95 7, p99 11;
- maximum 1,216;
- 71,635 bricks contain one object;
- 66,128 contain two;
- 101,010 contain 3–5;
- 28,089 contain 6–10;
- only one contains 792 or more.

For equal band counts, bands and bytes/pixel cancel from the crossover:

- 256-pixel cutout threshold: `ceil(3600² / 256²) = 198` objects per brick;
- 128-pixel cutout threshold: `ceil(3600² / 128²) = 792` objects per brick.

Observed result:

| Hybrid | Brick-selected groups | Objects replaced | Byte saving | Request/file saving |
|---|---:|---:|---:|---:|
| 256 g+r+z | 1 | 1,216 | 0.8008 GB (0.1223%) | 1,213 |
| 128 g+r+z | 1 | 1,216 | 0.0836 GB (0.0511%) | 1,213 |
| 128 one-band | 1 | 1,216 | 0.0279 GB (0.0511%) | 1,215 |

Verdict: **reject the hybrid**. Its negligible savings do not justify a second pixel-generation implementation, branch-specific WCS rules, local centering differences, extra source-version custody, or concentrated risk in the single highest-density brick. DR10 documentation specifically records processing and replacement issues in high-density/SUB_BLOB bricks, which raises rather than lowers the verification burden. [8]

## 5. Current contract defect and required PC-1 amendment

### 5.1 Contradiction

Current PC-1 says:

- `bands=grz`;
- `size=256`;
- each delivered band plane is the final analysis raster;
- no crop, resize, reprojection, interpolation, or WCS transform after delivery.

The frozen primary says:

- one input channel;
- 128×128;
- float32 deterministic inference;
- byte-exact index-reversal mirror on the exact production raster.

No governing document inspected by this audit defines:

- which one of g/r/z is the primary input;
- a deterministic three-band combination;
- a 256→128 crop;
- background subtraction;
- flux scaling or normalization from nanomaggies;
- clipping, NaN, infinity, missing-pixel, or padding behavior;
- endian/layout conversion into the exact float32 tensor.

Those are decision-bearing instrument semantics, not implementation details. Any choice made after real images are seen would violate the one-run preregistration rule.

### 5.2 Minimum amendment packet

Before any real image request, replace PC-1 with one exact interface and re-hash it. The cheapest candidate packet is:

1. **Product:** generated South-only FITS cutout from the documented viewer endpoint.
2. **Spatial grid:** `size=128`, `pixscale=0.262`, exact delivered TAN raster; no later spatial transform.
3. **Channel:** one named band fixed before access. `r` is the byte-minimal proposal because the network is single-channel and the parent selection is r-anchored, but that rationale must be reviewed and explicitly frozen; it is not inferred as acceptance here.
4. **Tensor conversion:** exact FITS plane/HDU, axis order, big-endian→native float32 conversion, invalid-pixel handling, background rule, scale/normalization, clipping, and contiguous-memory layout.
5. **Mirror:** byte-exact width-axis index reversal only after the final tensor is formed.
6. **Receipts:** rerun R1–R5 and retention/calibration checks on synthetics transformed through the exact new input function; hash the input function and all weights/thresholds.
7. **If g+r+z is scientifically required:** reject the one-band shortcut; define a three-channel 128×128 architecture, retrain only on a frozen multichannel synthetic generator, and refreeze weights/τ before sky access.

A smaller-than-128 cutout is not acceptable without refreezing the estimator. A 256 cutout is unnecessary once the exact 128 input is frozen.

## 6. Actually-cheapest operational design

### Route A — preferred: compute beside the coadds, transfer only cutouts

This is the lowest combined external-transfer and public-service-load design, conditional on legitimate collaborator/project access:

1. Use the documented NERSC CFS DR10 South coadd path, which the files page labels “At NERSC (for collaborators).” [2]
2. Run on a NERSC compute/workflow resource—not on a data-transfer node—the exact hash-pinned cutout-generation code matching amended PC-1.
3. Group the already-frozen object manifest by brick so each latest-version source image is opened once per band, but emit one independently hash-addressed 128×128 object product.
4. Preserve the service-equivalent TAN centering/resampling if that is what amended PC-1 freezes. Do not silently substitute integer native-pixel crops; that would change centering and WCS.
5. Apply PC-3 and PC-4 to every generated object: celestial two-axis WCS, North-up/East-left determinant/parity receipt, no partial linear terms, and fail-closed rejection of SIP/PV/CPDIS/D2IM/DET2IM or singular/ambiguous WCS.
6. Write outputs atomically into bounded shards (for example, deterministic tar shards plus per-object SHA-256 manifest), verify every member before shard closure, and retain append-only custody.
7. Transfer only completed shards and manifests. NERSC recommends Globus for significant data movement and documents gzip/tar preparation as intended transfer work. [5][6]

External effects of this design after authorization:

- public viewer calls: zero;
- external bytes: approximately the amended cutout payload, not full bricks;
- public service CPU/load: zero;
- local offsite disk: cutout shards only;
- internal NERSC reads: selected latest brick images, grouped once per brick/band.

This route is **not currently available by assumption**. The Legacy file page limits the CFS wording to collaborators, and this audit did not inspect accounts, allocations, or permissions. [2]

### Route B — fallback: operator-approved public 128 cutouts

If near-data compute cannot be obtained:

1. send the Legacy Survey help desk the exact count (`832,393`), proposed amended URL, band count, expected payload, concurrency one, atomic-download policy, and resume/backoff design; request a supported bulk mechanism and a numeric rate/batch ceiling. [7]
2. accept only an explicit supported route/rate; do not infer permission from the endpoint being public;
3. if ordinary HTTP is approved, use one active request, atomic `.tmp`→final rename, append-only hashes, and terminal handling of HTTP 429/`Retry-After`; [4]
4. keep the existing 5-second minimum until a provider-approved alternative is recorded;
5. retain all current WCS/parity/distortion and no-refetch custody gates.

Under the existing 5-second internal interval, request spacing alone is 4,161,965 seconds = **48.171 days**, before response latency, retries, outages, or transfer time. That is the honest fallback cost.

### Rejected alternatives

- **All bricks locally:** rejected—64.28× or 257.13× raw pixel oversupply, almost no g+r+z HTTP-file reduction, unknown compressed subset size, and tens of TB of expanded storage.
- **One-band bricks:** rejected—fewer files, but still 257.13× the raw pixels of 128 one-band cutouts.
- **Density hybrid:** rejected—one brick and ≤0.122% savings.
- **Viewer `subimage`:** rejected—different multi-brick/unresampled custody and potentially more products; not a drop-in PC-1 match. [3]
- **Locally crop downloaded bricks at nearest pixel:** rejected unless separately preregistered—subpixel centering and WCS differ from normal generated cutouts.
- **Merge nearby targets into larger viewer cutouts:** not evaluable from aggregate per-brick counts alone and would require object positions plus a new slicing/custody contract; no positions were opened for this audit.
- **Reduce fixed delay by guess:** rejected—no numeric published safe rate was found; 429 existence is not a quota. [4]

## 7. Decision and exact next action

**Decision:** do not replace cutouts with bulk bricks. The 64× finding is correct for the current 256-g+r+z comparison; the threefold brick-request claim is not. Do not run the current cutout pipeline either, because PC-1's 256×256×3 output does not match the frozen 128×128×1 estimator and its real-pixel input transform is missing.

**Actually-cheapest correct design:** amend and refreeze an exact 128×128 single-channel input, then execute the same hash-pinned cutout generation beside the NERSC coadds and Globus-transfer only verified shards. If collaborator compute is unavailable, use operator-approved public 128 cutouts under a recorded numeric service plan.

**Exact next action, still no fetch:** Hwao should ask Yui/Kun to close the PC-1 input-interface defect (band, normalization, invalid-pixel behavior, 128 raster) and separately ask the Legacy Survey help desk for a supported near-data/batch path or explicit numeric limit for 832,393 FITS cutouts. No empirical gate opens from this report.

## Sources

[1] https://www.legacysurvey.org/dr10/description — DR10 Data Release Description
[2] https://www.legacysurvey.org/dr10/files — DR10 Legacy Surveys Files
[3] https://www.legacysurvey.org/svtips — Sky Viewer Tips and Tricks
[4] https://discuss.legacysurvey.org/t/legacy-survey-cutouts/15593 — Legacy Survey cutouts — operator forum reply
[5] https://docs.nersc.gov/services/globus — NERSC Globus Documentation
[6] https://docs.nersc.gov/systems/dtn — NERSC Data Transfer Nodes
[7] https://www.legacysurvey.org/contact — Legacy Survey Contacts
[8] https://www.legacysurvey.org/dr10/issues — DR10 Known Issues
