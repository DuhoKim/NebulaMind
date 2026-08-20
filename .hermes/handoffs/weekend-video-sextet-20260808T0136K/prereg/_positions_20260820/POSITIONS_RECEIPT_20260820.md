# GPT1 position-provisioning receipt — 2026-08-20

Status: **COMPLETE**  
Custody closed UTC: `2026-08-20T04:15:08Z`  
Network boundary: **only `https://datalab.noirlab.edu/tap/async` was used. `portal.nersc.gov` was never touched.**

## 1. Frozen authorities and hashes

- `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`: `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361` — matches the required `5ff7f454…` law.
- `TORI_BS1_CLOSURE_PACKET.md`: `50bf06b0f28c690360751d60cb150387446fee1c5f3629036515234b0301b8f5`.
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`.
- `TORI_PARENT_ROW_COUNT_20260812.md`: `df9357085d4cfd35320ab34346a1fb3080dc1e5ba1e3d86e2dc6231dbbf534f3`.
- R1 fixed-range independent reconstruction: `_tori_parent_row_count_evidence/partitions/FINAL_THRESHOLD_INDEPENDENT_RECONSTRUCTION_20260812.json`, `31e1c4a461e3f3d6ebbbe3d3b21fc9fdb7b9f2b98e61c980540331e9258f24ab`.
- Full-keyspace independent reconstruction: `_tori_parent_row_count_evidence/partitions/remaining_121001_662174/FINAL_FULL_KEYSPACE_INDEPENDENT_RECONSTRUCTION_20260813.json`, `beb89247c908a42b16bcb944df8e0fa1bcb7398bfdc514bfa80781b890ab7154`.
- Working set: `_tori_r1_workingset_evidence/workingset_bricks.csv`, `78ee99d6824bf4f5126b9ffd9eb622ad8201df2c64c3f232d99c1791b5f36b74`, 60,308 data rows.

The frozen predicates were carried with the same qualified-column spelling used by the receipted TAP precedent: `t.brick_primary = 1`, `t.maskbits = 0`, `t.type <> 'PSF'`, `t.flux_r > 0`, the exact `(ls_id, release, brickid, objid)` join, `p.z_phot_median >= 0`, `p.z_phot_median < 0.15`, `t.dered_mag_r < 17.7`, `t.shape_r > 1.5`, and, for Cut 6, `POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551`.

## 2. Hard count cross-checks

The hash-pinned independent reconstructions were parsed directly, rather than trusting prose totals.

### Exact full-keyspace frozen chain

| Stage | Required | Reconstructed | Verdict |
|---|---:|---:|---|
| Cut 1 primary + mask | 2,584,542,900 | 2,584,542,900 | MATCH |
| Cut 2 extended + positive r flux | 1,317,374,704 | 1,317,374,704 | MATCH |
| exact photo-z join after Cut 2 | 1,317,374,704 | 1,317,374,704 | MATCH |
| Cut 3 photo-z window | 11,762,815 | 11,762,815 | MATCH |
| Cut 4 dered magnitude | 1,162,237 | 1,162,237 | MATCH |
| Cut 5 dered parent | 1,015,881 | 1,015,881 | MATCH |
| Cut 6 dered inclination parent | **832,393** | **832,393** | **MATCH** |

### Frozen R1 study-parent chain, `BRICKID 1..121000`

| Stage | Required | Reconstructed | Verdict |
|---|---:|---:|---|
| Cut 1 primary + mask | 674,896,997 | 674,896,997 | MATCH |
| Cut 2 extended + positive r flux | 338,508,894 | 338,508,894 | MATCH |
| exact photo-z join after Cut 2 | 338,508,894 | 338,508,894 | MATCH |
| Cut 3 photo-z window | 2,618,678 | 2,618,678 | MATCH |
| Cut 4 dered magnitude | 238,922 | 238,922 | MATCH |
| Cut 5 dered study parent | **208,407** | **208,407** | **MATCH** |

A fresh focused async count independently returned `208407` from one aggregate row. No count mismatch occurred, so the STOP condition did not fire.

## 3. Async TAP query ledger

Every submitted query has its exact ADQL, immutable query file, SHA-256, job URL, submission time, terminal/completion evidence, and returned row count below. Every run has `submission.json` and `poll_log.jsonl`; completed runs additionally have `job.xml` and `receipt.json`. Results were retrieved only after `COMPLETED` appeared in the poll log.

### Q1 — attempted fresh full Cut-6 aggregate

Query SHA-256: `11f50baaf733ee9cef88c7c226665642cc6c25d59f1e3f5cd5d06cf5e2af3228`  
Job: `https://datalab.noirlab.edu/tap/async/k22veje696e91hmr`  
Submitted: `2026-08-20T03:06:47Z`  
Last observed: `EXECUTING` at `2026-08-20T03:59:43Z`  
Settlement: remote UWS record returned HTTP 404 at `2026-08-20T04:02:21Z`; 199 poll events; **0 rows retrieved**. This was a lost job, not a count mismatch. Evidence: `run_count_full_cut6/remote_job_lost.json`; poll-log SHA-256 `08aa605cbac8c0064af485a2839dc0a4ef9c46a922bada11630a76d646744a91`.

```adql
SELECT COUNT(*) AS n_cut6_dered
FROM ls_dr10.tractor_s AS t
JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brick_primary = 1
  AND t.maskbits = 0
  AND t.type <> 'PSF'
  AND t.flux_r > 0
  AND p.z_phot_median >= 0
  AND p.z_phot_median < 0.15
  AND t.dered_mag_r < 17.7
  AND t.shape_r > 1.5
  AND POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551
```

### Q2 — attempted fresh fixed-range multi-stage aggregate

Query SHA-256: `895b75d6171f024cfe0acfec8a37e54cba04265448e64633896205b06323228c`  
Job: `https://datalab.noirlab.edu/tap/async/cp1wq2hhm5x1ke61`  
Submitted: `2026-08-20T03:06:47Z`  
Last observed: `EXECUTING` at `2026-08-20T03:59:40Z`  
Settlement: remote UWS record returned HTTP 404 at `2026-08-20T04:02:21Z`; 199 poll events; **0 rows retrieved**. This was a lost job, not a count mismatch. Evidence: `run_count_study_chain/remote_job_lost.json`; poll-log SHA-256 `2cd2fadf0913ed6ab1155643b59c40c51e5041de77b90a4587deea9ac0a4a965`.

```adql
SELECT
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
         AND t.dered_mag_r < 17.7
         AND t.shape_r > 1.5
        THEN 1 ELSE 0
      END) AS n_cut5_parent_dered
FROM ls_dr10.tractor_s AS t
LEFT OUTER JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brickid BETWEEN 1 AND 121000
```

### Q3 — successful fresh focused study-parent count

Query SHA-256: `a1a3a07139671821b1fc4f751264a5fe07af7a7c8ecb044f7d7c223231f808a7`  
Job: `https://datalab.noirlab.edu/tap/async/npohnmsr1kxwiurr`  
Submitted: `2026-08-20T04:02:50Z`  
Terminal: `COMPLETED` at `2026-08-20T04:10:59Z`  
Retrieved/receipted: `2026-08-20T04:11:00Z`  
Returned rows: 1 aggregate row, `n_study_parent=208407`; result SHA-256 `992768a0428fb034ab5e29495567c9a3e1c49bac36727fe44d1b6fa03d11756c`; poll-log SHA-256 `5b53b97a8d7dc4a39051c80e2b898600a7d951dd099478516c1cf94c31b4bc78`.

```adql
SELECT COUNT(*) AS n_study_parent
FROM ls_dr10.tractor_s AS t
JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brickid BETWEEN 1 AND 121000
  AND t.brick_primary = 1
  AND t.maskbits = 0
  AND t.type <> 'PSF'
  AND t.flux_r > 0
  AND p.z_phot_median >= 0
  AND p.z_phot_median < 0.15
  AND t.dered_mag_r < 17.7
  AND t.shape_r > 1.5
```

### Q4 — export partition A

Query SHA-256: `7e016dc1f2f53942e079f765a3e1263b99d5e50cfc8b5a74277d7951a183b287`  
Job: `https://datalab.noirlab.edu/tap/async/l0jbiuupt7d5beqk`  
Submitted: `2026-08-20T04:11:45Z`; terminal `COMPLETED`: `2026-08-20T04:13:54Z`; retrieved/receipted: `2026-08-20T04:14:00Z`  
Rows: **95,380**; columns: exactly `(ls_id, ra, dec, brickname)`; part SHA-256 `c7bacf317aa250d7149cb12b6d714445c7ec5657460935d6b9e2de660864c676`; poll-log SHA-256 `7875eaac9fc3650f80f323e14d9408238b89058d0c1e67ee99203e03fc166416`.

```adql
SELECT t.ls_id, t.ra, t.dec, t.brickname
FROM ls_dr10.tractor_s AS t
JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brickid BETWEEN 1 AND 50000
  AND t.brick_primary = 1
  AND t.maskbits = 0
  AND t.type <> 'PSF'
  AND t.flux_r > 0
  AND p.z_phot_median >= 0
  AND p.z_phot_median < 0.15
  AND t.dered_mag_r < 17.7
  AND t.shape_r > 1.5
ORDER BY t.brickid, t.objid
```

### Q5 — export partition B

Query SHA-256: `b80321f57878844aa6b13fb35a8a244c9caf5c82aa0b37e9bea7289c84a2f0d9`  
Job: `https://datalab.noirlab.edu/tap/async/i0oorac153iw9yft`  
Submitted: `2026-08-20T04:11:45Z`; terminal `COMPLETED`: `2026-08-20T04:13:23Z`; retrieved/receipted: `2026-08-20T04:13:28Z`  
Rows: **79,272**; columns: exactly `(ls_id, ra, dec, brickname)`; part SHA-256 `3b0766becabc74f0fd4df80c6bd3b04285962e80877964d09de972cffcc8bccd`; poll-log SHA-256 `12d7ca466c6bab664abd01d1dca824f31b9d153814b59cba0d591446c42b0eeb`.

```adql
SELECT t.ls_id, t.ra, t.dec, t.brickname
FROM ls_dr10.tractor_s AS t
JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brickid BETWEEN 50001 AND 100000
  AND t.brick_primary = 1
  AND t.maskbits = 0
  AND t.type <> 'PSF'
  AND t.flux_r > 0
  AND p.z_phot_median >= 0
  AND p.z_phot_median < 0.15
  AND t.dered_mag_r < 17.7
  AND t.shape_r > 1.5
ORDER BY t.brickid, t.objid
```

### Q6 — export partition C

Query SHA-256: `e9ba417ae44999b158b16d2ac8f65eaaf0cb27b4634b20b9afe8c3458b2ba0c6`  
Job: `https://datalab.noirlab.edu/tap/async/lxkp3nilg4ps6u6a`  
Submitted: `2026-08-20T04:11:45Z`; terminal `COMPLETED`: `2026-08-20T04:12:51Z`; retrieved/receipted: `2026-08-20T04:12:56Z`  
Rows: **33,755**; columns: exactly `(ls_id, ra, dec, brickname)`; part SHA-256 `06eb3cb81db68fe04ced55ac8d4afd311f244515313e6a13e45399e5bf9f0515`; poll-log SHA-256 `141a4297b1c7f3ce85d2d634bc445cd6d4b47bf1a1cf2953b4a509a41d5eb754`.

```adql
SELECT t.ls_id, t.ra, t.dec, t.brickname
FROM ls_dr10.tractor_s AS t
JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brickid BETWEEN 100001 AND 121000
  AND t.brick_primary = 1
  AND t.maskbits = 0
  AND t.type <> 'PSF'
  AND t.flux_r > 0
  AND p.z_phot_median >= 0
  AND p.z_phot_median < 0.15
  AND t.dered_mag_r < 17.7
  AND t.shape_r > 1.5
ORDER BY t.brickid, t.objid
```

## 4. Final export assembly and verification

The three disjoint, ordered BRICKID partitions were concatenated with one header:

- 95,380 + 79,272 + 33,755 = **208,407 data rows**.
- File line count: 208,408 including header.
- Header and only columns: `ls_id,ra,dec,brickname`.
- Distinct `ls_id`: 208,407; duplicate `ls_id` rows: 0.
- Blank-field rows: 0.
- RA outside `[0,360)`: 0; Dec outside `[-90,90]`: 0.
- Distinct exported primary bricknames: **58,009**.
- Working-set bricknames: **60,308**.
- Exact overlap: **58,009 / 58,009 exported bricknames are in the working set**; missing from working set: **0**.
- Therefore `exported_brickname_set ⊆ workingset_bricks.csv` is **TRUE**.
- Working-set bricknames not serving as a primary brick in this export: 2,299; these are the allowed margin-only remainder of the union working set.
- Machine verification: `_positions_20260820/export_verification.json`, SHA-256 `8d254c33b9fb9d3eb7a421db348ce6cdba3d37fd83427e69692750dfbfb6124c`.

## 5. Hash-pinned deliverable

- `_positions_20260820/positions_parent_20260820.csv`
- SHA-256: **`90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`**
- Sidecar: `_positions_20260820/positions_parent_20260820.csv.sha256`
- Sidecar content: `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9  positions_parent_20260820.csv`

No images, chirality labels, handedness fields, sky statistics, NERSC routes, database writes, publication, commits, or pushes were used.
