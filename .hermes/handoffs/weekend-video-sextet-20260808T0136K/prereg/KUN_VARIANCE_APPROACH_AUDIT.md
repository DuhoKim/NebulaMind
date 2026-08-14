# KUN_VARIANCE_APPROACH_AUDIT

Timestamp: 2026-08-14 KST

## Verdict

The current BS-1 artifact remains **UNRESOLVED**. Nothing presently in the workspace supplies the missing full-footprint `var(cos theta)` value, and the existing per-partition count evidence cannot be reinterpreted into one.

But my original BS-1 wording was narrower than the scientific purpose requires. The scientific purpose is not "run server-side trigonometry per object"; it is to prove the frozen selected footprint has enough angular spread around Longo's fixed axis for the fixed-axis amplitude test to be meaningful. A cheaper, rigorous footprint-adequacy statistic can satisfy that purpose if it is frozen explicitly and carries a conservative error bound.

## What BS-1 Was Trying To Protect

BS-1 was meant to stop a fake "enough sky" claim. A fixed-axis dipole test is not meaningful if the selected catalogue lies too close to one angular cap or one narrow stripe relative to the Longo axis. The `var(cos theta) >= 0.15` threshold was a geometry/conditioning check, not a measurement of handedness and not a result.

So the load-bearing requirement is:

> The frozen Cut-6 selected population must have enough object-weighted angular spread relative to Longo's axis.

The exact per-object population variance is one implementation of that requirement. It is not the only scientifically valid implementation.

## Audit Of The Current Query

The current global and partitioned queries compute

`x = cos(theta) = a dot r(ra,dec)`

inside NOIRLab TAP using repeated `COS`, `SIN`, and `RADIANS` calls per selected row, then aggregate `COUNT(x)`, `SUM(x)`, and `SUM(x*x)`. The partitioned version is better than the global version because additive moments are exact, but it still asks the service to evaluate trigonometry over object rows.

The contrast with the earlier successful counting sweep is meaningful: the successful sweep was the same catalogue/filter/join shape without per-row trig. The failures therefore plausibly implicate one or both of:

- the trigonometric expression making the jobs expensive enough to sit unscheduled or be killed;
- queue/account state after many async submissions and aborts.

I cannot prove a NOIRLab policy threshold from local evidence. But operationally the current approach has failed three times plus a canary, and further identical submissions are not a debugging strategy. Stop treating "endpoint HTTP 200" as evidence that this work will schedule.

## Brick-Centre Hypothesis

A count-weighted brick-centre variance is **not the same quantity** as the per-object variance.

It becomes a valid substitute only under a stated, bounded approximation:

1. Freeze exact post-Cut-6 object counts per brick, `n_b`, not just per partition.
2. Freeze each brick centre position, `c_b`, and Longo axis unit vector, `a`.
3. Compute `y_b = a dot c_b`.
4. Compute the object-count-weighted centre variance:

   `V_center = SUM(n_b * y_b^2) / SUM(n_b) - (SUM(n_b * y_b) / SUM(n_b))^2`

5. Bound intra-brick error. For each brick, define `delta_b` as the maximum angular separation in radians between the brick centre and any point in that brick. Then for any selected object in brick `b`,

   `|cos(theta_object) - y_b| <= delta_b`.

6. Let `eta = SUM(n_b * delta_b) / SUM(n_b)`. A conservative variance bound is:

   `|V_object - V_center| <= 4 * eta`.

Decision rule:

- `PASS` if `V_center - 4*eta >= 0.15`.
- `FAIL` if `V_center + 4*eta < 0.15`.
- `INCONCLUSIVE` otherwise; then exact per-object variance or a finer safe approximation is required.

For Legacy bricks of roughly 0.25 degrees on a side, a crude global half-diagonal bound is about `0.177 deg = 0.00309 rad`, giving `4*eta <= 0.0124` if that bound is used for every brick. A per-brick corner-based `delta_b` would be better and should be used if brick geometry is available.

## What Does Not Work

The existing counting-sweep partitions do not close this. Counts over broad `BRICKID` ranges are not enough because `BRICKID` keyspace is not sky area and range-level counts do not identify where objects lie inside each range. A range-weighted centre or keyspace-weighted approximation would be a new, weak statistic and should not be accepted.

An unweighted brick-centre variance also does not close it. The selected population is object-weighted; empty and sparse bricks cannot count the same as dense bricks.

A brick-table-only computation does not close it unless the table already contains exact post-Cut-6 selected counts per brick. A brick table with centres but no frozen selected-object counts only describes the tiling, not the selected catalogue footprint.

## Cheaper Route That Would Satisfy The Purpose

If Duho authorizes a new empirical route later, the least bad route is not server-side trig. It is:

1. Query exact post-Cut-6 counts per brick:

   `SELECT t.brickid, COUNT(*) AS n_cut6_dered FROM ... WHERE [frozen Cut-6] GROUP BY t.brickid`

2. Do not request RA/Dec rows, images, chirality, spin labels, or object exports.
3. Join the resulting per-brick counts to a frozen brick-centre table locally.
4. Compute `V_center`, `eta`, and the conservative pass/fail/inconclusive rule above.
5. Preserve the full per-brick count table and code hash.

This route is much closer to the successful counting sweep: it keeps the expensive catalogue join and cuts, but removes all per-row trigonometry. It returns at most one row per nonempty brick, not one row per object.

If the service still refuses a grouped count query, then the issue is no longer trig alone; it is either grouping cost, queue/account policy, or service health. But that failure would be more informative than a fourth trigonometric submission.

## Requirement Revision I Would Accept

Replace BS-1 item 4 with:

> The frozen Cut-6 footprint must pass an object-count-weighted Longo-axis spread check. Preferred exact statistic is per-object `var(cos theta) >= 0.15`. A bounded brick-centre substitute is acceptable if it uses exact post-Cut-6 counts per brick, frozen brick centres, a deterministic intra-brick angular error bound `eta`, and the conservative rule `V_center - 4*eta >= 0.15`. If the bounded statistic falls within the uncertainty band, the result is `INCONCLUSIVE`, not a pass.

This preserves the scientific purpose and removes the accidental dependency on server-side trigonometric scheduling.

## Final Answer To The Four Audit Questions

1. The query may be the problem. The trig expression is the obvious difference from the successful counting sweep, and repeated object-row trig is exactly the kind of cost that can turn a count query into an unscheduled aggregate. This is plausible, not proven.

2. A queue/account policy may also be involved. Local evidence proves no-throughput states, HTTP 502/404 loss, and long PENDING jobs; it does not prove a documented abuse threshold. Do not submit more identical jobs to test it.

3. Count-weighted brick-centre variance is not the same number as per-object variance. It can satisfy the same scientific purpose only with exact per-brick selected counts and a conservative intra-brick error bound. Existing per-partition counts are insufficient.

4. The scientific purpose does not require per-object server-side variance specifically. It requires an object-weighted footprint-adequacy check around Longo's axis. I would accept the bounded brick-centre version above as a BS-1 replacement, with fail-closed `INCONCLUSIVE` semantics.

Current status remains: **BS-1 unresolved until an exact object variance or bounded brick-centre pass is actually produced under fresh authorization.**
