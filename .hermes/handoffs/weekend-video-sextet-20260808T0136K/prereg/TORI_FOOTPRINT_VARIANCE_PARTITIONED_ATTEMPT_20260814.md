# TORI — Longo-axis footprint-variance receipt

**Superseding receipt assembled UTC:** `2026-08-13T21:16:35Z`  
**Status:** **UNRESOLVED — PARTITIONED RE-RUN REACHED THE 06:00 KST DEADLINE WITH ZERO LANDED PARTITIONS**  
**Kun BS-1 threshold:** `var(cos theta) >= 0.15`  
**Threshold verdict:** **NONE — no additive moments were returned**

## Plain ruling

Duho freshly authorized a partitioned re-run of the same Longo-axis statistic over the same frozen dered Cut-6 population. The frozen manifest contained **67 disjoint BRICKID ranges covering `1…662174`**. Each query could return one aggregate row containing only `n`, `SUM(cos theta)`, and `SUM(cos theta * cos theta)`.

The service returned **zero partition aggregate rows** before the stop rule fired at `2026-08-14T06:00:04+09:00` (`2026-08-13T21:00:04Z`). Completed coverage is therefore **0 of 67 partitions / 0 of 662,174 BRICKID keyspace units**. No mean or variance can be reconstructed.

Accordingly:

- `mean(cos theta)`: **UNMEASURED**;
- population `var(cos theta)`: **UNMEASURED**;
- comparison with `0.15`: **NONE**;
- Kun's footprint-variance requirement: **UNRESOLVED**.

This is not a below-threshold result and not a pass. A value below `0.15` would have been reported as a real failure without changing the population, but no numeric value exists. No partial subset, friendlier range, extrapolation, density assumption, or rescaled result is used.

## Supersession and preserved history

This receipt supersedes the live filename previously occupied by the one-global-query attempt receipt. That attempt remains byte-for-byte at:

- `TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md` — SHA-256 `ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e`.

The original global job `v0d4e15lm8hkz7zv` was one authorized query, ran `03:09:56`, was explicitly aborted, and returned zero moments. It is history, not one of the nine partition UWS jobs below.

## Authorized statistic and exact recombination

Population: the same frozen dered Cut-6 catalogue population whose prior count certificate gives **832,393** objects. That number is an expected population check from `TORI_FULL_KEYSPACE_SWEEP_20260813.md`; it is **not** a returned contributing count from this variance run.

Axis: Longo's Galactic `(l,b)=(52°,68.5°)`.

For each object, `x = cos(theta)` used the same frozen axis-relative expression. Each disjoint partition requested only:

- `n = COUNT(x)`;
- `SUM(x)`;
- `SUM(x*x)`.

Had all 67 partitions landed, exact recombination would have been:

- `mean = sum(SUM(x)) / sum(n)`;
- `var_pop = sum(SUM(x*x)) / sum(n) - mean^2`.

This is exact additive-moment recombination, not approximation or extrapolation. It could not be performed because `sum(n)`, `sum(SUM(x))`, and `sum(SUM(x*x))` were all absent.

## Manifest and deadline custody

- manifest: `footprint_variance_partitioned_20260813/manifest.json` — SHA-256 `076131fff15c0338cce689b4742cd64631f855e2a04398dc2d527b0962edda93`;
- manifest partitions: `67`;
- frozen coverage: `BRICKID 1…662174`;
- expected prior Cut-6 count: `832393`;
- frozen full-query hash: `5d4c7812331419eff0ec7dca4e40f690203cb94cc71b6309d7b8694299249ff1`;
- frozen cos-expression hash: `ddf9bd2550fdde7d9d285e5e03833186bb9a9393fb5d45857b59873bf70b8663`;
- deadline: `2026-08-14T06:00:00+09:00` / `2026-08-13T21:00:00Z`;
- stop recorded: `deadline_reached` at `2026-08-13T21:00:04Z`;
- status record: SHA-256 `30a45429277b6f8dd5f40ee07b5e80a1ae5e0b7fb918824c7bb52ee4f65fc661`;
- final machine outcome: `FINAL_OUTCOME_20260814.json` — SHA-256 `f308d522480d9bc5b4d406e4b53d4b79014a2c64d0b0ff33a1bde59db20a92d5`.

Where BRICKID coverage is stated, **BRICKID keyspace is not sky area**.

## Service-pressure and job history

Nine unique partition UWS jobs were created across only the first three disjoint ranges. Eight jobs encountered HTTP 502 pressure, were later missing at their recorded phase URLs, and are preserved as `LOST_404_AFTER_502`. One final first-range job was explicitly aborted by the deadline handler and independently rechecked as remote phase `ABORTED`.

No job produced a result CSV or partition receipt.

| BRICKID range | Attempt in range | UWS job id | Immutable query SHA-256 | Terminal custody | Independent remote recheck |
|---|---:|---|---|---|---|
| `1-10000` | 1 | `svrszxvl1897ra6h` | `0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98` | `LOST_404_AFTER_502` | HTTP 404 / no phase |
| `1-10000` | 2 | `hwmrvw0rnj4py5wb` | `0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98` | `LOST_404_AFTER_502` | HTTP 404 / no phase |
| `1-10000` | 3 | `y2yiv49zxrbyuj9y` | `0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98` | `LOST_404_AFTER_502` | HTTP 404 / no phase |
| `1-10000` | 4 | `rjr8jx9x2cr9dae3` | `0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98` | `LOST_404_AFTER_502` | HTTP 404 / no phase |
| `1-10000` | 5 | `b0do57zdhq0lsqeb` | `0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98` | `ABORTED` | HTTP 200 / ABORTED |
| `10001-20000` | 1 | `jawrn9xjdnwj3zsr` | `60b8be74115ae8acdc5392746bad2d0bb38a720b83df6d6d3b46e90e73c02748` | `LOST_404_AFTER_502` | HTTP 404 / no phase |
| `10001-20000` | 2 | `x6gbquc99uun0vi1` | `60b8be74115ae8acdc5392746bad2d0bb38a720b83df6d6d3b46e90e73c02748` | `LOST_404_AFTER_502` | HTTP 404 / no phase |
| `20001-30000` | 1 | `clw0f6k1tay2xr57` | `c3c8639a580d9db0b2aba24958bbc57827bd387f5d87885959699add17cef716` | `LOST_404_AFTER_502` | HTTP 404 / no phase |
| `20001-30000` | 2 | `bn47gqq7p0oxomju` | `c3c8639a580d9db0b2aba24958bbc57827bd387f5d87885959699add17cef716` | `LOST_404_AFTER_502` | HTTP 404 / no phase |

Final reconciliation:

- UWS submission records: **9**;
- unique UWS job URLs: **9**;
- lost after HTTP 502 and rechecked HTTP 404: **8**;
- deadline-aborted and rechecked `ABORTED`: **1**;
- landed result CSVs: **0**;
- partition receipts: **0**;
- reconciliation artifact: `FINAL_JOB_RECONCILIATION_20260814.json` — SHA-256 `a9a3344b19bc4a357074610ab8ce59a0981683fb0b8ec739bd06a17816309a9a`.

Concurrency was initially at most three, dropped to serial after pressure, and was later explicitly raised back to three after health checks. The raised jobs remained scheduler-pending; no fourth active range was added while three were pending. New pressure again forced serial. No landed partition was ever re-queried because none landed.

## Guard lift, restoration, and physical closure

- exception state: **CLOSED**;
- ordinary guard SHA-256 before: `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`;
- ordinary guard SHA-256 after: `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`;
- hashes identical: **YES**;
- ordinary guard independently verified to reject the trigonometric query after close: **YES**;
- guard lifecycle: SHA-256 `512773c212f5c37f8196e935e990757b15e9870ca51e6f0571e3d66bf2a9cc42`;
- executed orchestrator custody: SHA-256 `bc8e306e06361d510aef3d0acdd583b758ddbf9a14131ad6e6a3ccc1941b1196`;
- executed worker custody: SHA-256 `79fabbcfa0dd06f7e9d3d48733326317f36a46968aa8fad9d69ec253674c5214`;
- active Python variance processes after close: **0**;
- current orchestrator entry point: **disabled refusal stub**;
- current partition-worker entry point: **disabled refusal stub**.

The executed source bytes are retained under `footprint_variance_partitioned_20260813/executed_code_custody/` and match the manifest hashes. Retention is custody, not standing execution permission.

## Boundary ledger

- aggregate moment rows returned: **0**;
- object rows exported: **0**;
- positions exported: **0**;
- images requested: **0**;
- chirality computed: **0**;
- handedness fields joined or referenced: **0**;
- spin or CW/CCW fields joined or referenced: **0**;
- dipole amplitude computed: **0**;
- sky maps or angle bins: **0**;
- directional statistic beyond the authorized variance: **0**;
- population/axis/threshold change: **0**;
- publication/acceptance/commit/push: **0**.

## Exact next action

Kun's footprint-variance item remains open. This run has ended and grants no standing permission for another submission. Any later empirical attempt requires a new explicit authorization and a new closed-loop guard receipt. Until then, the BS-1/freeze packet must carry the variance item as **UNRESOLVED**, never as pass or fail.
