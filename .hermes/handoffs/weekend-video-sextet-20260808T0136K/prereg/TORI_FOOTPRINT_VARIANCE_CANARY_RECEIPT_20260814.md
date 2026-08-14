# TORI — NOIRLab scheduler canary receipt

**Assembled UTC:** `2026-08-14T02:48:53Z`  
**Canary state:** **MONITORING / phase PENDING**  
**Scientific variance state:** **UNRESOLVED — THRESHOLD VERDICT NONE**  
**Full 67-partition auto-launches:** **0**

## Plain ruling

The 45-minute abort was the right call. The rerun submitted at `2026-08-14T01:45:26Z` left all three active jobs `PENDING` for exactly `2700` seconds with no completed partition and no scheduler progress. Tori's queue-watch stopped it at `2026-08-14T02:30:28Z`; all three jobs were explicitly aborted and independently rechecked `ABORTED`. That reduced recognition of the same no-throughput condition from an overnight run to forty-five minutes instead of continuing to hammer a service that was not scheduling this work.

Duho then authorized exactly one small scheduler canary and no data-run continuation. One existing frozen-manifest partition was submitted:

- BRICKID range: `1…10000`;
- UWS job: `https://datalab.noirlab.edu/tap/async/k6fqyi9nuzfds6pt`;
- query SHA-256: `0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98`;
- manifest SHA-256: `076131fff15c0338cce689b4742cd64631f855e2a04398dc2d527b0962edda93`;
- aggregate columns only: `n_cut6_dered`, `sum_cos_theta`, `sum_cos2_theta`;
- initial phase: `PENDING` at `2026-08-14T02:45:03Z`;
- current recorded state: `MONITORING / phase PENDING`;
- current result: no aggregate result has landed.

The canary is polled GET-only every 300 seconds. If it reaches `EXECUTING` or `COMPLETED`, the monitor reports queue opening and stops; it cannot launch the remaining 66 partitions. If it remains pending through the 10,800-second observation window, the monitor reports that state and leaves the remote job parked without an abort.

## Why `1…10000`

This is the first nonempty partition in the existing 67-partition manifest. It was selected instead of inventing a new subpartition or using the known-empty 2,174-key tail. If it completes, its additive moments remain a genuine exact partial contribution for the frozen population.

Prior count custody provides a fail-closed magnitude bracket without a new count query:

- exact dered Cut-6 `n(1…1000) = 2583`;
- exact dered Cut-6 `n(1001…11000) = 23881`;
- therefore `2583 <= n(1…10000) <= 26464`.

A completed canary outside that bracket is rejected rather than accepted as a landed partition.

## Guard lifecycle and executable closure

- opened UTC: `2026-08-14T02:43:51Z`;
- closed UTC: `2026-08-14T02:43:53Z`;
- state: **CLOSED**;
- submissions made / limit: `1/1`;
- ordinary guard SHA-256 before: `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`;
- ordinary guard SHA-256 after: `228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51`;
- hashes identical: **TRUE**;
- ordinary guard specifically verified to reject the trigonometric query before: **TRUE**;
- ordinary guard specifically verified to reject the trigonometric query after: **TRUE**;
- executed submitter SHA-256: `2b92b6a9b77202b800a438f3407064dc07c924158d55c88245ef32c7986c5d4a`;
- live POST path: **DISABLED AFTER ONE SUBMISSION**;
- retained monitor: **GET-ONLY**;
- full-manifest launch path in monitor: **NONE**.

## Two service-stall modes observed locally in under one day

This is a local operational observation, not a public NOIRLab status claim.

1. `HTTP_502_THEN_REMOTE_404`: the overnight partition attempt created nine UWS jobs; eight encountered HTTP 502 pressure and were later missing at their recorded phase URLs (HTTP 404), one was deadline-aborted, and zero result CSVs landed.
2. `HTTP_200_BUT_SCHEDULER_PENDING`: the morning endpoint preflight answered HTTP 200 in `0.508021` seconds, yet three accepted jobs stayed `PENDING` for 2700 seconds with zero scheduler progress and zero result CSVs.

Operational lesson: endpoint HTTP 200 proves reachability, not scheduler throughput. Multiple stationary `PENDING` jobs are queue saturation, not completed work. The standalone pattern record is `SERVICE_STALL_PATTERN_20260814.json`, SHA-256 `6d170f106af282e9f6301c7f2bb85222fd7b4409af536e2732f9c06bca2c08d8`.

## Custody hashes

- launch authorization: `435893973dc546cb328359e81942d6ed218a9bf82024c41f8bb316beb50fb97c`;
- submission record: `b0ae977b9e74152a3759245f614dd978faf34d9e3fc729a721869a4d6d4e99c1`;
- guard lifecycle: `a2b0e359a891d397a9f7fe15e2ae4ab90230c114125f9613e4e274fd5a3fdb72`;
- initial PENDING snapshot: `980238a4e649491034097caff1f3addff4edf78d4868393e872283ca17acbe62`;
- executed submitter: `2b92b6a9b77202b800a438f3407064dc07c924158d55c88245ef32c7986c5d4a`;
- executed GET-only monitor: `aa282350b2dec940778c8a72cacada0bce3db00794a9fc018bcf0660e524f290`;
- 45-minute queue-watch: `e551c3b04abc15f72d85beea8c5ae1be3c9df06ab73fd4d22b1eb2ca6a0d45f0`;
- 45-minute final outcome: `815a05f499bdf389f350d8554a910e6bfcda340860fb2ea0615a3edf0fce8e8f`;
- preserved global-attempt receipt: `ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e`;
- preserved partition-attempt receipt: `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289`;
- unresolved variance receipt, unchanged: `f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289`.

## Scientific status and boundary

This canary does not resolve the full-footprint statistic unless all 67 disjoint partitions eventually land and recombine exactly. A canary result, if returned, is labelled **PARTIAL**. It must not be presented as the full footprint or compared with the preregistered `0.15` threshold as a final verdict.

Current scientific status remains:

- `mean(cos theta)`: **UNMEASURED FOR FULL FOOTPRINT**;
- population `var(cos theta)`: **UNMEASURED FOR FULL FOOTPRINT**;
- threshold verdict: **NONE**;
- variance receipt superseded by canary: **NO**.

Boundary ledger:

- UWS canary submissions: **1**;
- replacement submissions: **0**;
- full-manifest auto-launches: **0**;
- aggregate result rows currently landed: **0**;
- object rows exported: **0**;
- positions exported: **0**;
- images requested: **0**;
- chirality computed: **0**;
- handedness, spin, or CW/CCW fields joined or referenced: **0**;
- angle bins or sky maps: **0**;
- dipole amplitude computed: **0**;
- publication/acceptance/commit/push: **0**.

## Exact next action

Let the one GET-only monitor observe this job. On `EXECUTING` or `COMPLETED`, report and stop; Duho decides whether and when to authorize a full run. On three hours still pending, report and leave the canary parked. This receipt grants no automatic full-manifest launch.
