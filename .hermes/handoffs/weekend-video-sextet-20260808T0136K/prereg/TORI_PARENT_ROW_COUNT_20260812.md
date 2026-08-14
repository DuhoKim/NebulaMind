# TORI — DESI Legacy DR10.1 South Parent Row Count

**Receipt rendered:** `2026-08-12T10:55:58Z`  
**Status:** `STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND`  
**Authorization:** Duho: `authorize the parent row count` — server-side aggregate counts only.

## 0. Result boundary

This receipt reports catalogue **counts**, not a study sample and not a scientific result. It contains no object rows, identifiers, position list, images, handedness, chirality, dipole, axis-relative term, or other sky statistic. No bulk sweep download occurred. No literature fraction or Yui retention was multiplied into these counts.

Forbidden operations remained at zero:

- sample/catalogue rows exported: **0**
- identifiers or positions exported: **0**
- images requested for measurement: **0**
- handedness/chirality calls: **0**
- trigonometric or Longo-axis query terms: **0**
- sky statistics/results: **0**
- publication/acceptance/commit/push: **0**

## 1. Bound inputs and endpoint

- Goru frozen cuts: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md` — SHA-256 `df08a525ef7fbff4bae9dc0069b6d3cbda653454c678ccd00361e88dac654476`.
- Tori route binding: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/TORI_SURVEY_ROUTE_BINDING_20260812.md` — SHA-256 `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87`.
- Yui context only: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md` — SHA-256 `b4e2f5b5f92fc881ec2a0a35e84515fd05057c1051bff516cad7acae3609e18a`. Its one-sided lower 95% synthetic retention bound is 0.9615; **not multiplied here**.
- Catalogue: `ls_dr10.tractor_s` (DESI Legacy DR10 South served by NOIRLab Astro Data Lab).
- Photo-z: `ls_dr10.photo_z` joined on `(ls_id, release, brickid, objid)`.
- Endpoint: `https://datalab.noirlab.edu/tap/async` (IVOA UWS asynchronous TAP).
- Schema receipt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/schema_result.csv` — SHA-256 `02c36a69db2baddd5ac040a1b02809429baea4d9f6c5720ac7001c74771dbf76`.
- Live global base count endpoint/query receipt: `run00_base_count/receipt.json`.

The NOIRLab data page documented 2,825,807,500 `tractor_s` rows, while the live aggregate returned 2,827,055,986. This receipt uses the live server-side count and discloses the 1,248,486-row metadata drift.

## 2. Coverage and no-extrapolation rule

- Contiguous completed `BRICKID` range: `1..121000` of documented key range `1..662174`.
- Catalogue partition-key coverage: **121,000/662,174 = 18.273143%**.
- Not yet covered: `BRICKID 121001..662174`.
- This percentage is **BRICKID keyspace coverage, not an equal-area sky fraction**. No sky-area statistic was computed.
- Every running sum below is labeled **LOWER BOUND** until all disjoint partitions complete.
- No partition density is scaled up. Totals are sums of landed, non-overlapping aggregate results only.
- Authorized stopping rule: stop at the first of (a) the **dered Cut-5** contiguous lower bound reaching 200,000, (b) wall-clock deadline `2026-08-12T13:56:00Z`, or (c) keyspace exhaustion. The raw branch is still reported but does not gate stopping.
- The bounded manifest stopped cleanly at `2026-08-12T10:51:10Z` with stop reason `dered_cut5_contiguous_lower_bound_reached_200000`; no further partition was submitted after the stopping rule fired. Final process verification found no orchestrator, no TAP runner, and no lock holder.
- Detached-launch custody: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/partitions/DETACHED_LAUNCH_CUSTODY_20260812.json` — SHA-256 `e9a396c6ed7f576028aeaff7fef9d78dd460c8d2e4f8297aa76e2ac0e3324aa4`.
- Dered-stop-rule handoff custody: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/partitions/DERED_STOP_RULE_HANDOFF_CUSTODY_20260812.json` — SHA-256 `1e9c1cf7b081c30591e4e3a466423c0d064e5dfbc873988ee309eb8f886c2513`.
- Independent reconstruction: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/partitions/FINAL_THRESHOLD_INDEPENDENT_RECONSTRUCTION_20260812.json` — SHA-256 `31e1c4a461e3f3d6ebbbe3d3b21fc9fdb7b9f2b98e61c980540331e9258f24ab`. It independently summed the contiguous hash-matched one-row receipts rather than trusting `status.json` or this rendered Markdown.

## 3. Survival chain

Goru Cut 4 is ambiguous in the served data model. His wording says `flux_r` converted to magnitude, which maps literally to `mag_r < 17.7`; Tori's route binding described extinction-corrected `dered_mag_r < 17.7`. Both readings are counted through Cut 5 and availability checks; neither is silently selected.

| Stage | Predicate | Count | Custody status |
|---|---|---:|---|
| Base | all `ls_dr10.tractor_s` rows | 2,827,055,986 | exact live global aggregate |
| Cut 1 | `brick_primary=1 AND maskbits=0` | 674,896,997 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |
| Cut 2 | Cut 1 + `type<>'PSF' AND flux_r>0` | 338,508,894 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |
| Photo-z join availability after Cut 2 | matching `(ls_id,release,brickid,objid)` | 338,508,894 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |
| Cut 3 | Cut 2 + `0<=z_phot_median<0.15` | 2,618,678 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |
| Cut 4 raw branch | Cut 3 + `mag_r<17.7` | 208,996 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |
| Cut 4 dered branch | Cut 3 + `dered_mag_r<17.7` | 238,922 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |
| Cut 5 raw parent | raw Cut 4 + `shape_r>1.5` | 185,345 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |
| Cut 5 dered parent | dered Cut 4 + `shape_r>1.5` | 208,407 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |

These are parent counts only. Tori does not decide whether either branch supplies the requested accepted yield and does not multiply spiral, inclination, or estimator-retention factors.

## 4. Countable availability losses

All loss counts below are relative to the corresponding Cut-5 parent within the completed contiguous partitions. Overlapping failure modes are not added.

| Availability reading | Raw surviving | Raw loss | Dered surviving | Dered loss |
|---|---:|---:|---:|---:|
| all-band `nobs_g,r,z>0` | 185,345 | 0 (0.0000%) | 208,407 | 0 (0.0000%) |
| all-band `ngood_g,r,z>0` | 185,344 | 1 (0.0005%) | 208,406 | 1 (0.0005%) |
| all-band `flux_ivar_g,r,z>0` | 185,345 | 0 (0.0000%) | 208,407 | 0 (0.0000%) |
| valid shape IVARs + `e1^2+e2^2<1` | 177,606 | 7,739 (4.1755%) | 199,035 | 9,372 (4.4970%) |
| native depth/PSF/dust/flux/fit/coordinate covariates | 185,345 | 0 (0.0000%) | 208,406 | 1 (0.0005%) |
| all countable requirements together | 177,606 | 7,739 (4.1755%) | 199,034 | 9,373 (4.4974%) |

Not countable in this authorized catalogue-only pass:

- **WCS/parity availability:** requires per-object image/header requests. Measurement-image acquisition is forbidden; count remains `NOT COUNTED`.
- **Gaia DR3 density covariate:** Gaia DR3 is a separate ESA TAP product; Legacy embedded Gaia fields are EDR3. No cross-service positional sample or position export was authorized; count remains `NOT COUNTED`.
- **Image-derived arm contrast/visibility:** requires measurement images and is forbidden; count remains `NOT COUNTED`.
- **Sky-area footprint variance:** no sky statistic was computed. Operational partition densities are documented below without extrapolation.

## 5. Partition density and gradient

`Cut-2 rows per BRICKID` and both Cut-5 parent rows per BRICKID are recorded for every landed database partition to document nonuniform catalogue density. These are aggregate operational densities, not axis-relative statistics and not a basis for extrapolation.

| BRICKID range | Width | Started UTC | Completed UTC | Elapsed | Cut 1 | Cut 2 | Cut-2/BRICKID | Cut 3 | Cut 5 raw | Raw/BRICKID | Cut 5 dered | Dered/BRICKID | Result bytes | Query SHA-256 | TAP job |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1..1000 | 1000 | 2026-08-12T09:26:59Z | 2026-08-12T09:28:45Z | 106s | 8,080,793 | 4,191,646 | 4191.646000 | 47,759 | 2,111 | 2.111000 | 3,002 | 3.002000 | 554 | 9eb65aa2e4131e6a7d0215bab5f473bf543abe28d7630624f3fb8cf0a09d3f78 | https://datalab.noirlab.edu/tap/async/p02obp8gmjlae5h1 |
| 1001..11000 | 10000 | 2026-08-12T07:58:38Z | 2026-08-12T08:17:21Z | 1123s | 73,937,875 | 30,551,627 | 3055.162700 | 364,425 | 20,579 | 2.057900 | 29,096 | 2.909600 | 575 | 29f8d7f58602b890157aa14391f62c55179882a4f5372b452a8d655d539a81a5 | https://datalab.noirlab.edu/tap/async/uiew24xthhfttin6 |
| 11001..21000 | 10000 | 2026-08-12T09:51:10Z | 2026-08-12T09:51:12Z | 2s | 59,532,452 | 21,038,101 | 2103.810100 | 275,120 | 15,232 | 1.523200 | 17,708 | 1.770800 | 575 | 98927bfabb5fc94d9bf1c4d6ffa1ec909ac44a9a8fcc646a79a1064468c4f2e7 | https://datalab.noirlab.edu/tap/async/eoj7o2mnvvimz0kh |
| 21001..31000 | 10000 | 2026-08-12T09:57:42Z | 2026-08-12T10:01:39Z | 237s | 48,297,933 | 21,015,894 | 2101.589400 | 185,928 | 13,253 | 1.325300 | 14,696 | 1.469600 | 575 | 73d17debdf03e499ef48e882a71881cb590a630d3b31592553f8912ae9e07993 | https://datalab.noirlab.edu/tap/async/rmw4uhda1pbq05wg |
| 31001..41000 | 10000 | 2026-08-12T09:57:42Z | 2026-08-12T10:02:10Z | 268s | 56,384,447 | 27,528,004 | 2752.800400 | 218,060 | 15,130 | 1.513000 | 16,379 | 1.637900 | 575 | 2a4f264462a1b9c4eaf93fc9892f652f00b08f7bd90236151dce7f1ac100ee1b | https://datalab.noirlab.edu/tap/async/kpuxrb89pfm4pgy9 |
| 41001..51000 | 10000 | 2026-08-12T09:57:42Z | 2026-08-12T10:00:23Z | 161s | 52,973,394 | 27,964,952 | 2796.495200 | 193,913 | 14,889 | 1.488900 | 16,170 | 1.617000 | 575 | 9538de9da4bf8275ce0cd544a4f9e41f5bbd384a187802167f0f1cf211c76e83 | https://datalab.noirlab.edu/tap/async/fn140tun0ld7p4j7 |
| 51001..61000 | 10000 | 2026-08-12T10:09:31Z | 2026-08-12T10:10:36Z | 65s | 54,780,121 | 30,200,881 | 3020.088100 | 200,153 | 15,192 | 1.519200 | 16,373 | 1.637300 | 575 | d908f1658bd97eddc21e1ac316842a6dc6a32c1b2c33fb61a32598708703a5cf | https://datalab.noirlab.edu/tap/async/d54qncvedefo971u |
| 61001..71000 | 10000 | 2026-08-12T10:09:31Z | 2026-08-12T10:12:10Z | 159s | 56,356,769 | 31,091,927 | 3109.192700 | 199,423 | 16,227 | 1.622700 | 17,317 | 1.731700 | 575 | 1ff173b4f3e01b4fb10ddc32944ddda0a5d59049b6de54fb01075fb7c1dc9909 | https://datalab.noirlab.edu/tap/async/n22wbqva768dhbjf |
| 71001..81000 | 10000 | 2026-08-12T10:09:31Z | 2026-08-12T10:12:10Z | 159s | 52,368,416 | 29,014,510 | 2901.451000 | 186,976 | 14,536 | 1.453600 | 15,451 | 1.545100 | 575 | 9da817343bafc8787b73f89fb5ab23ece86d00baa7b71b760eaa2a948fc2ee2e | https://datalab.noirlab.edu/tap/async/x41oyl29668hl1ru |
| 81001..91000 | 10000 | 2026-08-12T10:10:46Z | 2026-08-12T10:23:22Z | 756s | 52,291,610 | 29,740,409 | 2974.040900 | 184,915 | 13,991 | 1.399100 | 14,908 | 1.490800 | 575 | 7b1e21ca1ee8a56b214ed51ea0a8bd769a2f5edbd5ae4a206e4a9fa84fdf3f25 | https://datalab.noirlab.edu/tap/async/hfb1nobwzknr49o4 |
| 91001..101000 | 10000 | 2026-08-12T10:23:29Z | 2026-08-12T10:32:10Z | 521s | 49,134,051 | 27,425,764 | 2742.576400 | 178,915 | 14,262 | 1.426200 | 15,012 | 1.501200 | 575 | b0cdd6e615fff6fdc9ab21a3cf2265e2eae01135be3a2d4f6b49d01c8f5a8100 | https://datalab.noirlab.edu/tap/async/xl2vod7c82vzxxwx |
| 101001..111000 | 10000 | 2026-08-12T10:32:16Z | 2026-08-12T10:41:13Z | 537s | 52,861,253 | 28,768,562 | 2876.856200 | 184,137 | 14,512 | 1.451200 | 15,458 | 1.545800 | 575 | 8467cbcfbc7382af62908033454879b4ca43a8e29690218eff6d31aa56863063 | https://datalab.noirlab.edu/tap/async/qt9f3eotwdtxofwd |
| 111001..121000 | 10000 | 2026-08-12T10:41:23Z | 2026-08-12T10:51:07Z | 584s | 57,897,883 | 29,976,617 | 2997.661700 | 198,954 | 15,431 | 1.543100 | 16,837 | 1.683700 | 575 | 2744592ec072ab3e9908f320425432bc549cca8effb1daca94624ff3e8c5cf5b | https://datalab.noirlab.edu/tap/async/eazkwvs68xdl087e |

Three-point final-stage density series (landed aggregate receipts only):

| BRICKID range | Cut-5 raw | Raw/BRICKID | Cut-5 dered | Dered/BRICKID |
|---|---:|---:|---:|---:|
| `1..1000` | 2,111 | 2.111000 | 3,002 | 3.002000 |
| `1001..11000` | 20,579 | 2.057900 | 29,096 | 2.909600 |
| `11001..21000` | 15,232 | 1.523200 | 17,708 | 1.770800 |

- Dered series: `3.002000 -> 2.909600 -> 1.770800` parent rows/BRICKID.
- Dered decline from the second to third point: **39.139401%**; first to third: **41.012658%**.
- Raw series: `2.111000 -> 2.057900 -> 1.523200` parent rows/BRICKID.
- Raw decline from the second to third point: **25.982798%**; first to third: **27.844623%**.
- This third point overturns the earlier provisional reading that final-stage density was approximately flat across the first two adjacent ranges. The no-extrapolation rule is therefore load-bearing: neither the Cut-2 nor Cut-5 partition density is uniform enough to scale unqueried ranges.

Overlapping diagnostic (never added to full-chain totals):

- Run 10, `BRICKID 11001..61000`, Tractor-only Cut 1–2: Cut 2 = 127,747,832; density = **2554.956640 rows/BRICKID**.
- Compared with `BRICKID 1..1000` density 4191.646000, this is a **39.0465% decrease**.
- Because the partition density is not uniform, no partition is scaled to infer an unqueried total.
- Diagnostic receipt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/run10_tractor_011001_061000/receipt.json` — SHA-256 `905180a190034a03852c2710a98f6f9b50b76a340ddd21f048562a70f9d27222`.

## 6. Exact query custody

Every executed query is preserved verbatim at the absolute query path below and pinned by the SHA-256 in the partition table. The production query text is identical across partitions except for the final literal inclusive `BRICKID BETWEEN <lo> AND <hi>` bounds. This is exact reconstructible query text, not a paraphrase.

- Production template/example (literal range `1001..11000`): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/09_partition_benchmark_brickid_001001_011000.adql`.
- Remaining partition manifest: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/partitions/manifest.json` — SHA-256 `b72bf2a465ec331d322011277852718ddaeda0552808750aa3b7ca93b4282376`.
- Aggregate-only runner: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/run_aggregate_tap.py` — SHA-256 `7e59737785b6c136c3e64b1fadefa958eeefdaef4338a9b2b30e9fb02af66fcf`.
- Runner guard rejects row/export/mutation constructs and rejects `SIN`, `COS`, `TAN`, `RADIANS`, `DEGREES`, and `COSTHETA`.

Exact production query template:

```adql
SELECT
  COUNT(*) AS n_join_rows,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
        THEN 1 ELSE 0
      END) AS n_cut1_primary_mask,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
        THEN 1 ELSE 0
      END) AS n_cut2_extended_flux,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.ls_id IS NOT NULL
        THEN 1 ELSE 0
      END) AS n_photoz_joined_cut2,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
        THEN 1 ELSE 0
      END) AS n_cut3_photoz,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.mag_r < 17.7
        THEN 1 ELSE 0
      END) AS n_cut4_raw_mag,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.dered_mag_r < 17.7
        THEN 1 ELSE 0
      END) AS n_cut4_dered_mag,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.mag_r < 17.7
         AND t.shape_r > 1.5
        THEN 1 ELSE 0
      END) AS n_cut5_parent_raw,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.dered_mag_r < 17.7
         AND t.shape_r > 1.5
        THEN 1 ELSE 0
      END) AS n_cut5_parent_dered,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.nobs_g > 0 AND t.nobs_r > 0 AND t.nobs_z > 0
        THEN 1 ELSE 0
      END) AS n_raw_allband_nobs,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.dered_mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.nobs_g > 0 AND t.nobs_r > 0 AND t.nobs_z > 0
        THEN 1 ELSE 0
      END) AS n_dered_allband_nobs,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.ngood_g > 0 AND t.ngood_r > 0 AND t.ngood_z > 0
        THEN 1 ELSE 0
      END) AS n_raw_allband_ngood,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.dered_mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.ngood_g > 0 AND t.ngood_r > 0 AND t.ngood_z > 0
        THEN 1 ELSE 0
      END) AS n_dered_allband_ngood,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.flux_ivar_g > 0 AND t.flux_ivar_r > 0 AND t.flux_ivar_z > 0
        THEN 1 ELSE 0
      END) AS n_raw_allband_ivar,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.dered_mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.flux_ivar_g > 0 AND t.flux_ivar_r > 0 AND t.flux_ivar_z > 0
        THEN 1 ELSE 0
      END) AS n_dered_allband_ivar,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.shape_r_ivar > 0
         AND t.shape_e1_ivar > 0
         AND t.shape_e2_ivar > 0
         AND t.shape_e1*t.shape_e1 + t.shape_e2*t.shape_e2 < 1
        THEN 1 ELSE 0
      END) AS n_raw_shape_valid,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.dered_mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.shape_r_ivar > 0
         AND t.shape_e1_ivar > 0
         AND t.shape_e2_ivar > 0
         AND t.shape_e1*t.shape_e1 + t.shape_e2*t.shape_e2 < 1
        THEN 1 ELSE 0
      END) AS n_dered_shape_valid,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.psfdepth_r > 0
         AND t.psfsize_r > 0
         AND t.ebv >= 0
         AND t.mw_transmission_g > 0
         AND t.mw_transmission_r > 0
         AND t.mw_transmission_z > 0
         AND t.flux_g > 0
         AND t.fitbits IS NOT NULL
         AND t.ra IS NOT NULL
         AND t.dec IS NOT NULL
        THEN 1 ELSE 0
      END) AS n_raw_native_covariates,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.dered_mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.psfdepth_r > 0
         AND t.psfsize_r > 0
         AND t.ebv >= 0
         AND t.mw_transmission_g > 0
         AND t.mw_transmission_r > 0
         AND t.mw_transmission_z > 0
         AND t.flux_g > 0
         AND t.fitbits IS NOT NULL
         AND t.ra IS NOT NULL
         AND t.dec IS NOT NULL
        THEN 1 ELSE 0
      END) AS n_dered_native_covariates,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.nobs_g > 0 AND t.nobs_r > 0 AND t.nobs_z > 0
         AND t.shape_r_ivar > 0
         AND t.shape_e1_ivar > 0
         AND t.shape_e2_ivar > 0
         AND t.shape_e1*t.shape_e1 + t.shape_e2*t.shape_e2 < 1
         AND t.psfdepth_r > 0
         AND t.psfsize_r > 0
         AND t.ebv >= 0
         AND t.mw_transmission_g > 0
         AND t.mw_transmission_r > 0
         AND t.mw_transmission_z > 0
         AND t.flux_g > 0
         AND t.fitbits IS NOT NULL
         AND t.ra IS NOT NULL
         AND t.dec IS NOT NULL
        THEN 1 ELSE 0
      END) AS n_raw_all_countable_availability,

  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.dered_mag_r < 17.7
         AND t.shape_r > 1.5
         AND t.nobs_g > 0 AND t.nobs_r > 0 AND t.nobs_z > 0
         AND t.shape_r_ivar > 0
         AND t.shape_e1_ivar > 0
         AND t.shape_e2_ivar > 0
         AND t.shape_e1*t.shape_e1 + t.shape_e2*t.shape_e2 < 1
         AND t.psfdepth_r > 0
         AND t.psfsize_r > 0
         AND t.ebv >= 0
         AND t.mw_transmission_g > 0
         AND t.mw_transmission_r > 0
         AND t.mw_transmission_z > 0
         AND t.flux_g > 0
         AND t.fitbits IS NOT NULL
         AND t.ra IS NOT NULL
         AND t.dec IS NOT NULL
        THEN 1 ELSE 0
      END) AS n_dered_all_countable_availability

FROM ls_dr10.tractor_s AS t
LEFT OUTER JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brickid BETWEEN 1001 AND 11000
```

## 7. Abandoned global jobs (retained, not deleted)

These jobs produced no count result and are not included in any total:

| Role | TAP job | Final server phase | Reason | Result/sample/position rows | Receipt |
|---|---|---|---|---:|---|
| initial conditional global Cut 1–2 | `cufh26hignovtpss` | `ABORTED` | exceeded 3600-second window; unconstrained conditional scan | 0/0/0 | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/run01_cut1_cut2/abort_receipt.json` |
| global indexed Cut 1 | `ugcy42h6l52xbj8d` | `ABORTED` | exceeded 3600-second window | 0/0/0 | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/run04_cut1_indexed/abort_receipt.json` |
| Run 11 global low-z full-chain | `y74tcwewq9rp4fim` | `ABORTED`; method status **ABANDONED** | exceeded 3600-second window; Duho directed partition completion | 0/0/0 | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/run11_global_cut3_losses/abort_receipt.json` |

A locally drafted query containing Longo-axis `cos(theta)` moments was caught before submission, marked `DO NOT EXECUTE`, and is rejected by the hardened runner. It was never run and produced zero rows/statistics:

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/03_SUPERSEDED_DO_NOT_EXECUTE.md` — SHA-256 `54ff5ca3d6c5e9cb02d4a0099709f2f13f7762f92df671ac00c22af8617a3730`.

## 8. Freeze-condition interpretation and stop line

The authorized dered stop bound is reached without extrapolation: the contiguous partial-coverage Cut-5 lower bounds are raw `185,345` and dered `208,407`; the dered branch is at least `200,000`. This is a lower-bound certificate for the dered catalogue reading only. It does **not** estimate the unqueried remainder, choose the magnitude ambiguity, or claim an exact full-catalogue total.
Kun's freeze condition 2 may close on this hash-bound dered lower-bound certificate if his gate requires proof that the dered parent exceeds 200,000. Goru owns all multiplication by external spiral, inclination, or estimator-retention factors. Tori makes no accepted-yield or scientific-result claim.

Empirical Longo-amplitude execution remains blocked. This authorization did not open handedness, chirality, images, a sky statistic, a result, publication, or accepted status.
