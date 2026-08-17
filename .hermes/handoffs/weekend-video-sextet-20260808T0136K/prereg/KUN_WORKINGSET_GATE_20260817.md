PASS_WORKINGSET

# Kun working-set gate

Date: 2026-08-17 KST
Scope: document and local evidence review only. No network, no HEAD, no TAP query, no checksum GET, no download, no endpoint, no commit, no push.

## 1. Creation Digests

The creation-digest fix is genuine in the mechanism. `_tmp_r1_margin_20260817/_tmp_pull_with_creation_digests.sh` runs each TAP partition, then immediately computes SHA-256 and row count for the just-written `positions_part_<part>.csv`, records the timestamp, and only after all three creation records are written does it call `_tmp_workingset.py`.

That ordering closes the clause-4 failure from R1. The retained `position_creation_digests.json` records:

- `positions_part_a.csv`: 95,380 rows, `4583bd62832c1174a2470f46624bee47b7da4915a797cb03115160794a680199`, `2026-08-17T10:22:35Z`
- `positions_part_b.csv`: 79,272 rows, `78ef1e9a82f60b7eec8bb1e43ba81ac75305f1d5d86d335c63a09d2c828c1f11`, `2026-08-17T10:29:08Z`
- `positions_part_c.csv`: 33,755 rows, `49c8a3f6da7548814e36d094b8adcbf44f845aca50c4bd110fdb2ff2a74a9a18`, `2026-08-17T10:31:15Z`

## 2. Working-Set Derivation

The 60,308-brick working set is correctly derived for this gate. `_tmp_workingset.py` imports the gated adapter, uses `build_output_wcs`, `angular_separation_deg`, `output_overlap_area_in_source_pixels`, `CANDIDATE_PREFILTER_DEG`, and `INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2`, and accumulates the union of every planned brick over all 208,407 parent objects. This is primaries plus all margin/neighbour bricks, not primaries only.

The surrounding candidate indexing is local acceleration, but the inclusion predicate itself is the gated adapter rule: overlap area in source pixels greater than `1e-8` after the 0.21 degree prefilter. This matches the R1 rule and the adapter’s production planning semantics.

The retained CSV verifies as 60,308 unique bricknames, all with valid coverage class:

- rows excluding header: 60,308
- duplicate bricknames: 0
- `required`: 60,308
- `absent-by-coverage`: 0

## 3. Parent Counts And Reproduction

The row counts reproduce the frozen parent count exactly:

`95,380 + 79,272 + 33,755 = 208,407`

The contributing-brick distribution also reappears bit-for-bit from the second pull:

`1: 172,983; 2: 32,320; 3: 2,939; 4: 165`

This is meaningful corroboration of the second pull and working-set computation. It is not circular with the prior R1 aggregate files: `_tmp_workingset.py` reads the fresh position partitions and brick feature table, not R1’s aggregate JSON, to produce the distribution.

## 4. R2 Classification

The R2 classification is consistent with the R1 pass and is falsifiable at harvest time. The working set classifies each retained brick by the exact indicator (`nexphist_r sum > 0`), yielding `required = 60,308` and `absent-by-coverage = 0`.

The checksum harvest can contradict this: a required brick whose `.sha256sum` listing lacks `image-r` becomes a missing/unexpected contradiction to receipt and gate, not a silent skip. That preserves R2’s distinction between planning classification and proof from survey-published checksum listings.

## 5. Deletion And Aggregate Status

Position deletion is auditable this time. `workingset_summary.json` binds all three deleted filenames to their creation-time digests and marks each `deleted: true`.

I found no surviving `positions_part*.csv` or `_tmp_rless_implicated.txt` under the workspace or the writable temp roots checked. `git ls-files` reports no working-set report/evidence files or transient position files as tracked. The retained working-set artifact contains brick identifiers and coverage classes, not per-object rows, positions, or object identifiers.

## 6. Harvest Arithmetic

The harvest arithmetic is correct:

- `60,308 * 1.2 s = 72,369.6 s = 20.10 h`
- `60,308 * 1.0 s = 60,308 s = 16.75 h`
- `60,308 * ~6 KB ≈ 0.36 GB` of checksum text

The frozen successor’s tier-2 checksum/metadata pacing is 1.0 s/request, so 16.8 h continuous is the binding-floor arithmetic. Using 1.2 s/request gives the more conservative 20.1 h figure. “Roughly two calendar days” inside the 20:00-08:00 US/Pacific weekday windows is plausible and not optimistic in the direction that matters for Duho’s authorization.

## 7. Pinned Checks

- `WORKINGSET_20260817.md`: `70c81543b6508c9e7ea4ba4cd25072b81c1178d7ba76bed38d809753ba086f3b`
- `_tori_r1_workingset_evidence/workingset_bricks.csv`: `78ee99d6824bf4f5126b9ffd9eb622ad8201df2c64c3f232d99c1791b5f36b74`, 60,308 rows plus header
- `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md`: `1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b`, mode `444`
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, mode `444`
- `adapter/nm_brick_cutout_adapter.py`: `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- `R1_EXACT_INDICATOR_20260817.md`: `dfc65b03a272d12129ca543d5aa0da1671da07a11bedaa6c91facf2b5e05648e`
- amended `R1_MARGIN_COVERAGE_20260817.md`: `2e27a414ced2a6ca091c52fcf851dd2bae7014136bfd99298fd6ff21dc7c69a7`
- `KUN_R1_MARGIN_COVERAGE_GATE_20260817.md`: `4562a0cfbdee84ff7b05efa481a62bf4bd9c0ab995b83988c1a6f1f82f447841`
- `KUN_R1_REGATE_20260817.md`: `e1f3869ab0cbf6048064dbc129e21d05fc9d06791bdc93c8dec114fb345d8796`

## Boundary

Network calls: 0. HEAD requests: 0. TAP queries: 0. Checksum GETs: 0. Downloads: 0. Image bytes touched: 0. FITS files fetched: 0. Checksum harvest: 0. Manifests built: 0. Endpoints activated: 0. Commit/push/publication: 0. This gate authorizes no harvest by itself.
