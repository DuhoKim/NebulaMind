# TORI — BS-1 closure packet against Kun's exact wording

**Assembled UTC:** `2026-08-13T21:20:23Z`  
**Controlling gate:** `KUN_PREREG_DRAFT_GATE_20260812.md` — SHA-256 `5d726380d64e34a1188a5bfb0b080962008bc80746e86fc5e39bde75a6264dff`  
**Campaign five-item status:** **4 CLOSED / 1 UNRESOLVED**  
**VARIANCE REQUIREMENT: UNRESOLVED — THRESHOLD VERDICT NONE**  
**OVERALL KUN BS-1 STATUS: HOLD — NOT CLOSED.**

## Plain ruling

The route, exact frozen cuts, actual catalogue counts, and counted accepted-yield feasibility bound are evidence-bearing. The fifth campaign item—actual Cut-6 `var(cos theta) >= 0.15` around Longo's axis—remains unresolved. The freshly authorized 67-partition run reached its 06:00 KST stop with **0 landed partitions and 0 returned moments**, so it supplied neither a pass nor a failure.

Kun's controlling gate has seven literal bullets. In addition to unresolved variance, the derived-catalogue publication-licence clause remains open. Therefore BS-1 is not closed and this packet does not clear the preregistration freeze.

Nothing published, accepted, committed, or pushed.

## Kun's exact seven requirements and disposition

Kun's controlling text at lines 94–102 requires:

1. exact DR10/DR10.1 product paths or records;
2. exact frozen parent cuts;
3. actual queried surviving counts after each cut, not only plausible extrapolation;
4. actual footprint variance around Longo's axis, meeting `var(cos theta) >= 0.15`;
5. actual parent count multiplied by measured BS-3 lower-bound retention, yielding `N_accepted >= 100,000`;
6. licence statement permitting derived-catalogue publication;
7. query/code receipt with hash and rerunnable command or script.

| Kun item | Disposition | Primary receipt custody |
|---|---|---|
| 1. DR10/DR10.1 paths or records | **CLOSED** | `TORI_SURVEY_ROUTE_BINDING_20260812.md`, SHA-256 `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87`; `TORI_FULL_KEYSPACE_SWEEP_20260813.md`, SHA-256 `9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020` |
| 2. exact frozen parent cuts | **CLOSED** | `TORI_PARENT_ROW_COUNT_20260812.md`, SHA-256 `df9357085d4cfd35320ab34346a1fb3080dc1e5ba1e3d86e2dc6231dbbf534f3`; `TORI_CUT6_INCLINATION_COUNT_20260812.md`, SHA-256 `ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651` |
| 3. actual per-cut counts | **CLOSED** | full-keyspace certificate SHA-256 `9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020`; independent reconstruction SHA-256 `beb89247c908a42b16bcb944df8e0fa1bcb7398bfdc514bfa80781b890ab7154` |
| 4. actual `var(cos theta) >= 0.15` | **UNRESOLVED — NONE** | `TORI_FOOTPRINT_VARIANCE_RECEIPT.md`, SHA-256 `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289`; final machine outcome SHA-256 `f308d522480d9bc5b4d406e4b53d4b79014a2c64d0b0ff33a1bde59db20a92d5` |
| 5. counted accepted yield ≥100,000 | **CLOSED AS FEASIBILITY LOWER BOUND** | `GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`, SHA-256 `bbe3bbaaedb7efaacb9bf1f214094115464dac81c9339df18e3223ff3dac9172`; authoritative retention SHA-256 `012cb5fd677e6a77427b592b362796f71fa837b7ccd93248559c48709e1e1073`; count certificate SHA-256 `9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020` |
| 6. derived-catalogue publication licence | **OPEN** | route receipt SHA-256 `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87` records that the image licence is not a derived-catalogue publication grant |
| 7. hashed rerunnable query/code | **CLOSED FOR CUSTODY; EXECUTION GATE CLOSED** | count and variance manifests, queries, runners, job reconciliation, and refusal-stub closure are hash-pinned; new variance execution requires new explicit authorization |

## 1. Exact DR10.1 product paths and records — CLOSED

Receipt: `TORI_SURVEY_ROUTE_BINDING_20260812.md`, SHA-256 `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87`.

Bound records and routes include `ls_dr10.tractor_s`, `ls_dr10.photo_z`, updated DR10.1 South sweeps, row-matched photo-z sweeps, and NOIRLab TAP async. The later sweep certificate records the actual aggregate jobs and hashes on those records. Image retrieval remains a separate future stage and was not used here.

## 2. Exact frozen parent cuts — CLOSED

The authoritative dered Cut-6 population is:

1. `brick_primary = 1`;
2. `maskbits = 0`;
3. `type <> 'PSF'`;
4. `flux_r > 0`;
5. exact photo-z join on `(ls_id, release, brickid, objid)`;
6. `0 <= z_phot_median < 0.15`;
7. `dered_mag_r < 17.7`;
8. `shape_r > 1.5`;
9. `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`.

Custody: parent SHA-256 `df9357085d4cfd35320ab34346a1fb3080dc1e5ba1e3d86e2dc6231dbbf534f3`; Cut-6 SHA-256 `ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651`; full-keyspace certificate SHA-256 `9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020`. No cut was selected after observing variance because no variance was returned.

## 3. Actual queried surviving counts — CLOSED

Final exact full-keyspace counts from `TORI_FULL_KEYSPACE_SWEEP_20260813.md`, SHA-256 `9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020`:

| Stage | Actual server-side aggregate count |
|---|---:|
| joined catalogue rows | 2,827,055,986 |
| Cut 1: primary + mask | 2,584,542,900 |
| Cut 2: extended + positive R flux | 1,317,374,704 |
| exact photo-z join after Cut 2 | 1,317,374,704 |
| Cut 3: valid `0 <= z_phot_median < 0.15` | 11,762,815 |
| Cut 4 raw `mag_r < 17.7` | 1,015,450 |
| Cut 4 dered `dered_mag_r < 17.7` | 1,162,237 |
| Cut 5 raw parent | 903,913 |
| Cut 5 dered parent | **1,015,881** |
| Cut 6 raw | 749,914 |
| Cut 6 dered | **832,393** |

The direct full-chain queries measured `BRICKID 1…541000`, **81.700580%** of the documented BRICKID keyspace, and a separate existence aggregate proved `541001…662174` had zero joined parent rows. Therefore these are exact catalogue totals. **BRICKID keyspace is not sky area**; no density or sky-area extrapolation enters them.

Independent reconstruction: SHA-256 `beb89247c908a42b16bcb944df8e0fa1bcb7398bfdc514bfa80781b890ab7154`.

## 4. Actual footprint variance — UNRESOLVED

Receipt: `TORI_FOOTPRINT_VARIANCE_RECEIPT.md`, SHA-256 `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289`.

- intended population: frozen dered Cut-6; prior exact count `832,393`;
- Longo axis: Galactic `(l,b)=(52°,68.5°)`;
- frozen manifest: 67 disjoint BRICKID ranges covering `1…662174`;
- exact additive outputs per partition: `n`, `SUM(x)`, `SUM(x*x)` for `x=cos(theta)`;
- completed partitions: **0 of 67**;
- completed keyspace units: **0 of 662,174**;
- returned contributing count: **NONE**;
- returned `SUM(x)`: **NONE**;
- returned `SUM(x*x)`: **NONE**;
- `mean(cos theta)`: **UNMEASURED**;
- population `var(cos theta)`: **UNMEASURED**;
- frozen threshold verdict: **NONE**.

Nine unique UWS jobs were created across the first three ranges: eight were lost after HTTP 502 pressure and independently rechecked as HTTP 404; one final first-range job was aborted by the 06:00 KST deadline and independently rechecked `ABORTED`. Zero result CSVs and zero partition receipts exist. The guard is `CLOSED`, the ordinary guard hash is unchanged, both exception entry points are disabled refusal stubs, and no active Python variance process remains.

This is not a failing below-threshold result and not a pass. The population, axis, threshold, and framing remain unchanged. No partial subset or extrapolation is accepted.

## 5. Parent × measured retention yielding N accepted ≥100,000 — CLOSED AS FEASIBILITY LOWER BOUND

Current Goru receipt: `GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`, SHA-256 `bbe3bbaaedb7efaacb9bf1f214094115464dac81c9339df18e3223ff3dac9172`.

Its counted chain is:

- exact post-Cut-6 parent: `832,393`;
- frozen restricted GZD-5 spiral fraction: `18.23%` (`25,482 / 139,758` at the frozen vote floor), `LANA_SPIRAL_FRACTION_SOURCED_20260812.md`, SHA-256 `46e10c6a028d2a2047b6af1c2103b38337f93fc5ccc8466c3f61ff1045214bef`;
- measured classifier-retention lower bound: `85.72%`;
- displayed arithmetic: `832,393 × 0.1823 × 0.8572 = 130,076.02307108`, rounded in Goru's receipt to **130,076**.

**130,076 ≥ 100,000.** This is a counted preregistration feasibility lower bound, not 130,076 observed classifier-accepted real objects and not a handedness result.

### Mandatory retention supersession

- **SUPERSEDED:** `YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md`, SHA-256 `b4e2f5b5f92fc881ec2a0a35e84515fd05057c1051bff516cad7acae3609e18a` — one-sided lower 95% **96.15%**, from an inclination-only `0–60°` synthetic population.
- **AUTHORITATIVE:** `YUI_INCLINATION_RETENTION_REMEASURE_20260812.md`, SHA-256 `012cb5fd677e6a77427b592b362796f71fa837b7ccd93248559c48709e1e1073` — full Cut-6-admitted range sampled uniformly in `cos(i)`; 10,349/12,000 = 86.24%, one-sided lower 95% **85.72%**.

The freeze candidate must carry 85.72%, not 96.15%.

## 6. Derived-catalogue publication licence — OPEN

Route receipt SHA-256 `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87` records:

- Viewer images are CC BY 4.0 with required credit;
- Legacy data use has acknowledgment/citation requirements;
- the primary catalogue pages did not supply a separate derived-catalogue publication grant;
- the image licence must not be silently extended to a derived catalogue.

No later hash-bound licence artifact closing this clause was found in the handoff workspace. This packet publishes nothing and cannot manufacture a licence grant.

## 7. Hashed rerunnable query/code custody — CLOSED; execution permission CLOSED

Count custody:

- count manifest SHA-256 `665738a20a9e754ee190297a421a1438d33bb563e53ea67b64feb634c250b7ef`;
- base query SHA-256 `2744592ec072ab3e9908f320425432bc549cca8effb1daca94624ff3e8c5cf5b`;
- count runner SHA-256 `7b997f5755b42c12b73c874669e0f5fa09487818b8bd3b0fec7122e385b513a8`;
- independent reconstruction SHA-256 `beb89247c908a42b16bcb944df8e0fa1bcb7398bfdc514bfa80781b890ab7154`.

Variance custody:

- footprint receipt SHA-256 `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289`;
- preserved original attempt `TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md` SHA-256 `ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e`;
- final outcome SHA-256 `f308d522480d9bc5b4d406e4b53d4b79014a2c64d0b0ff33a1bde59db20a92d5`;
- partition manifest SHA-256 `076131fff15c0338cce689b4742cd64631f855e2a04398dc2d527b0962edda93`;
- final partition status SHA-256 `30a45429277b6f8dd5f40ee07b5e80a1ae5e0b7fb918824c7bb52ee4f65fc661`;
- guard lifecycle SHA-256 `512773c212f5c37f8196e935e990757b15e9870ca51e6f0571e3d66bf2a9cc42`;
- job reconciliation SHA-256 `a9a3344b19bc4a357074610ab8ce59a0981683fb0b8ec739bd06a17816309a9a`;
- executed orchestrator SHA-256 `bc8e306e06361d510aef3d0acdd583b758ddbf9a14131ad6e6a3ccc1941b1196`;
- executed worker SHA-256 `79fabbcfa0dd06f7e9d3d48733326317f36a46968aa8fad9d69ec253674c5214`;
- ordinary guard SHA-256 `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`.

Reconstruction custody is rerunnable locally, but no variance reconstruction is possible because no moments landed. The current variance entry points refuse execution. Reproducibility evidence is not standing authorization to query again.

## Boundary ledger

- aggregate variance rows returned: **0**;
- sample rows exported: **0**;
- positions exported: **0**;
- images requested: **0**;
- chirality computed: **0**;
- handedness joined or referenced: **0**;
- spin or CW/CCW fields joined or referenced: **0**;
- dipole amplitude computed: **0**;
- sky map or angular bins: **0**;
- publication/acceptance/commit/push: **0**.

## Exact next action

1. Do not change the frozen population, Longo axis, `0.15` threshold, 85.72% retention, or counted 130,076 feasibility bound.
2. Carry Kun item 4 as **UNRESOLVED** and item 6 as **OPEN**; do not clear BS-1 or the freeze.
3. Any later variance attempt requires a new explicit authorization and new guard lifecycle; this packet grants none.
4. Resolve the licence clause with a primary, hash-pinned permission/terms artifact.
5. Return this packet to Kun/Hwao as a HOLD result; it is not publication or acceptance.
