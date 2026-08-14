# KUN FINAL WORDING GATE -- ACCEPTED-YIELD FEASIBILITY RECEIPT

Timestamp: 2026-08-12 KST

Target:

- `prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`

Prior gates:

- `prereg/KUN_FEASIBILITY_GATE_20260812.md`
- `prereg/KUN_FEASIBILITY_REGATE_20260812.md`

Boundary: wording/custody gate only. I did not run a sky statistic, inspect images, assign handedness, compute chirality, freeze a preregistration, publish, commit, accept, or authorize a sky run.

## Verdict

PASS WITH ONE REQUIRED WORDING REPAIR.

The substantive feasibility ruling is now clean:

- sections 2 and 3 are marked `[SUPERSEDED DIAGNOSTIC]`;
- the old flip history is preserved as evidence rather than authority;
- `Closed` is gone from the title;
- the authoritative calculation uses the restricted conditional fraction against the post-Cut-6 parent;
- the primary floor is frozen at `has-spiral-arms_total-votes >= 5`;
- `f_s = 25,482 / 139,758 = 18.23%`;
- the full-keyspace extrapolated accepted yield is about `140,283` to `140,296`, depending on rounded constants;
- the required keyspace share is about `71.3%`.

The remaining defect is exactly the one Hwao flagged: the final bound statement still says the GZD-5 spiral fraction must "survive a GZD-native vote-depth sensitivity check." That was true when my first gate was written. It is false now as a status statement. The sensitivity check has been performed, the `>=10` floor has been rejected as a classification-depth selector, and `>=5` has been adjudicated as the least favourable defensible primary floor.

## Required Replacement

Replace the current final bound statement:

> The DR10.1 South route appears feasible for a Longo-amplitude test IF the GZD-5 spiral fraction (frozen at >=5 effective votes) survives a GZD-native vote-depth sensitivity check AND if additional keyspace is counted.

with:

> The DR10.1 South route appears feasible for a Longo-amplitude test at the frozen GZD-5 primary floor `has-spiral-arms_total-votes >= 5` (`f_s = 18.23%`), conditional on counting enough additional DR10.1 South BRICKID keyspace to reach the preregistered 100,000 accepted-galaxy requirement.

Keep the existing caveat immediately after it:

> This remains an acquisition-feasibility statement, not a closed accepted-yield count. The full-keyspace parent remains an extrapolation over BRICKID keyspace rather than a counted bound, keyspace is not strictly equivalent to sky area, and the underlying density is not uniform.

This replacement discharges the stale sensitivity conditional while preserving the live acquisition conditional.

## Check On The Smaller Wording Issue

The phrase "frozen at >=5 effective votes" and "survives a GZD-native vote-depth sensitivity check" should not appear in the same claim sentence. Together they imply that `>=5` is both adjudicated and still awaiting validation. The replacement above resolves that conflict.

## Plain Answer For Duho

Safe to assert after the one sentence repair:

> Accepted-yield feasibility is no longer the blocker. At the adjudicated GZD-5 floor of `has-spiral-arms_total-votes >= 5`, the restricted spiral fraction is `18.23%`, above the `13.06%` break-even. The Longo-amplitude route appears feasible if enough additional DR10.1 South keyspace is counted.

Still not safe to assert:

> The accepted-yield requirement is already closed, or a sky run is authorized.

No sky run, preregistration freeze, publication, commit, or acceptance follows from this gate.
