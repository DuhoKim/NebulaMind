# KUN FEASIBILITY GATE -- ACCEPTED-YIELD RECEIPT

Timestamp: 2026-08-12 KST

Target:

- `prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`

Supporting artifacts inspected:

- `prereg/TORI_PARENT_ROW_COUNT_20260812.md`
- `prereg/TORI_CUT6_INCLINATION_COUNT_20260812.md`
- `prereg/YUI_INCLINATION_RETENTION_REMEASURE_20260812.md`
- `prereg/LANA_SPIRAL_FRACTION_SOURCED_20260812.md`
- local GZ DECaLS schema copy at `isotropy-parity-scope-v2-20260810T2300K/evidence_gz_2.md`
- local Walmsley et al. GZ DECaLS paper copy at `isotropy-parity-scope-20260810T2245K/evidence_gz_decals_paper_full.md`

Boundary: read-only gate. I did not run a sky statistic, inspect images, assign handedness, compute chirality, publish, accept, or mutate any out-of-scope surface.

## Verdict

PASS WITH REPAIRS.

The feasibility direction is credible: Goru was right to reject both the original `total-votes >= 20` Willett-clean death verdict and the lenient/strict conditional-fraction counts. But the current receipt overstates closure. It may support "likely feasible if more keyspace is counted"; it does not yet support a freeze-clean statement that the 100,000 accepted-galaxy requirement is met.

The blocking weakness is the same one that made the receipt flip twice: the surviving fraction, `Willett-clean without total-votes >= 20`, has not been stress-tested under any GZD-5-native vote-depth floor. Dropping a non-native GZ2 floor is justified. Dropping every vote-depth guard is not automatically justified.

## 1. Vote Floor

The `total-votes >= 20` floor should not be used as the primary feasibility gate for GZD-5. The local Walmsley paper copy says GZD-5 moved to variable retirement and that after June 2019 the non-prioritized galaxies received at least about 5 classifications, unlike the 40-classification GZD-1/2 regime. Goru's own decomposition also reports median total votes 5.0 and 76.10% below 20.

So the original pessimistic `5.5% - 10.0%` verdict is not trustworthy. It mostly measured classification depth, not spiral morphology.

But `Willett-clean minus the vote floor` is also not freeze-clean as written. The receipt says the valid count is 42,550, giving `f_s ~= 16.8%` unrestricted or `30.4%` restricted. That may be right as a no-floor diagnostic, but it permits low-effective-evidence branch outcomes. A galaxy with only one downstream spiral-arm voter can still pass a fraction threshold if that one vote is "yes"; Goru correctly identified that as invalid for lenient/strict, but the same low-denominator risk remains unless the Willett-clean count records per-node denominators.

Defensible repair:

- remove the imported `total-votes >= 20` floor;
- add a GZD-5-native vote-depth sensitivity table for the same upstream predicate:
  - no vote floor;
  - `smooth-or-featured_total >= 5`;
  - `smooth-or-featured_total >= 5 AND disk-edge-on_total >= 2 AND has-spiral-arms_total >= 2`;
  - `smooth-or-featured_total >= 5 AND disk-edge-on_total >= 3 AND has-spiral-arms_total >= 3`.

The freeze should use the least favourable defensible row that still reflects the GZD-5 decision tree. I cannot state what `f_s` becomes at those floors from the current receipt, because it does not provide the counts. That missing table is load-bearing.

## 2. Conditional Fractions

Goru's conditional-fraction diagnosis holds.

The GZ DECaLS schema describes `{question}_{answer}_fraction` as a fraction over volunteers who answered that question, and the same schema says downstream question relevance is represented by the product of preceding answers for the automated catalogue. The local paper copy also shows GZD-5 has an improved decision tree and different branching from GZD-1/2. Therefore `has-spiral-arms_yes_fraction` must not be thresholded as a standalone galaxy-level spiral predicate without enforcing the upstream featured and not-edge-on path.

That invalidates the Lenient and Strict variants in the receipt as decision evidence. They can remain as diagnostics only if explicitly labelled structurally invalid.

## 3. Inclination Denominator

The restricted denominator is not automatically a double count, but the receipt needs to rewrite the algebra.

There are two clean formulations:

1. Use the unrestricted joint fraction `P(featured AND not-edge-on AND spiral)` against the pre-Cut-6 parent, then multiply by Yui retention only.
2. Use the restricted conditional fraction `P(featured AND spiral | not-edge-on)` against the post-Cut-6 parent, then multiply by Yui retention.

The current single multiplier, `0.8240 * 0.8572 * f_s`, is correct for formulation 2, not for formulation 1. Applying it to the unrestricted `16.8%` joint fraction double-counts the not-edge-on condition. This is conservative numerically, but it is still bad custody because it makes two differently conditioned fractions look interchangeable.

Numerically, using the current no-floor values:

- counted keyspace with restricted-chain `16.8%`: about 23,619 accepted, not enough now;
- full-keyspace extrapolation with restricted-chain `16.8%`: about 129,258 accepted;
- full-keyspace extrapolation with unrestricted-chain `16.8%` and no separate inclination multiplier: about 156,858 accepted;
- restricted `30.4%` with the post-Cut-6 chain: about 233,895 accepted.

So the denominator correction does not by itself kill feasibility. It does require a repaired receipt before freeze.

Also, "perfectly matches our non-edge-on parent" is too strong. Tori's Cut-6 is a catalogue ellipticity cut, `b/a > 0.4`, while GZD-5 `disk-edge-on_no_fraction >= 0.715` is a volunteer morphology branch. They are aligned conditioning concepts, not the same measured variable.

## 4. Least Favourable Defensible Forks

Using only values already in the receipt, the no-floor `16.8%` clears the full-keyspace break-even even under the conservative, double-counting formula: about 129k accepted against a 100k requirement.

But that is not the least favourable defensible choice. The least favourable defensible choice must include a GZD-5-native effective-vote floor, and the current artifact does not report that count. Because the decisive threshold is only `13.06%`, the missing sensitivity is not cosmetic; a modest reduction from `16.8%` could flip the answer.

A second caveat remains: the full-keyspace parent is still an extrapolation over BRICKID keyspace, not a counted sky-area bound. Tori's parent receipt explicitly warns that partition density is not uniform enough to scale as a result. Goru's verdict is therefore an acquisition feasibility statement, not a closed accepted-yield count.

## Required Repairs

Before this can be used in a preregistration freeze:

1. Replace `Closed` and `securely satisfies` language with `provisionally feasible pending vote-depth sensitivity and counted keyspace extension`.
2. Add the GZD-5-native vote-depth sensitivity table above, with exact counts and `f_s` for each row.
3. Pick one canonical denominator formula:
   - unrestricted joint fraction with no separate inclination multiplier, or
   - restricted conditional fraction applied after Tori's Cut-6 multiplier.
4. Label the unrestricted/restricted values by probability meaning, not just as lower/upper bracket.
5. Preserve the no-extrapolation boundary: current counted keyspace does not meet 100,000; full-keyspace feasibility remains to be established by further aggregate counts or a preregistered stop rule.

## Plain Answer For Duho

The current evidence does not justify the old "dead" verdict. It also does not justify a clean "yield closed" pass.

It is safe to say:

> The DESI DR10.1 South route appears feasible for a Longo-amplitude test if the no-floor GZD-5 spiral fraction survives a GZD-native vote-depth sensitivity check and if additional keyspace is counted.

It is not yet safe to say:

> The 100,000 accepted-galaxy requirement is closed.

No empirical sky run or preregistration freeze should proceed from this receipt until the repairs above land and are re-gated.
