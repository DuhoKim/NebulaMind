# KUN FEASIBILITY RE-GATE -- ACCEPTED-YIELD REPAIRS

Timestamp: 2026-08-12 KST

Target:

- `prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`, especially sections `Repair 1` and `Repair 2`

Prior gate:

- `prereg/KUN_FEASIBILITY_GATE_20260812.md`

Boundary: read-only re-gate. I did not run a sky statistic, inspect images, assign handedness, compute chirality, freeze a preregistration, publish, commit, accept, or authorize a sky run.

## Verdict

PASS WITH REPAIRS.

Substantively, the feasibility verdict now clears as an acquisition-feasibility statement: the 100,000 accepted-galaxy requirement is reachable if more DR10.1 South keyspace is counted, provided the preregistration uses a GZD-5-native floor no stricter than the least favourable defensible floor, `has-spiral-arms_total-votes >= 5`.

The reason this is not a clean `PASS` is textual custody, not arithmetic: the top half of the receipt still contains the superseded mixed-conditioning verdicts and "Closed"/"securely satisfies" language. The appended repair section fixes the logic, but the artifact should not carry contradictory old and new verdicts without explicitly marking the old ones superseded.

## Repair 1: Algebra

PASS.

Goru adopted the correct conditional formulation:

> Parent Cut-5 count x Tori Cut-6 survival x Yui retention x restricted conditional `f_s`

That means `f_s` is read as `P(featured AND spiral | not-edge-on)` using the restricted denominator `139,758`, and the separate Cut-6 multiplier supplies the parent-to-not-edge-on transition. This is the formulation I approved in the first gate. The mixed use of unrestricted joint `f_s` with a separate inclination multiplier is no longer the operative calculation in the repair section.

One textual repair remains: the earlier sections still present unrestricted and restricted fractions under a single multiplier. If the file is used as a receipt, the old sections must be labelled "superseded diagnostic" or rewritten so only the repaired formulation is authoritative.

## Repair 2: Vote-Depth Floor

PASS on the table; ruling on floor: `>=5` is the least favourable defensible primary floor currently supported by the record.

The new restricted-denominator table is the load-bearing repair:

| `has-spiral-arms_total-votes` floor | Count | `f_s` | Verdict against 13.06% |
|---:|---:|---:|---|
| none / `>=1` | 42,550 | 30.45% | clears |
| `>=2` | 42,175 | 30.18% | clears |
| `>=3` | 40,844 | 29.22% | clears |
| `>=5` | 25,482 | 18.23% | clears |
| `>=10` | 15,249 | 10.91% | fails |

I do not accept `>=10` as a defensible morphology-purity floor for GZD-5 on the current evidence. It is too likely to reselect the high-classification retirement regime rather than cleaner spirals. The local GZ DECaLS paper says GZD-5 deliberately mixed galaxies with roughly 40 classifications and galaxies with at least about 5 after active learning. A downstream `has-spiral-arms_total-votes >= 10` therefore selects objects from a different classification-depth regime. That is the same family of defect as the rejected GZ2 `total-votes >= 20` floor: it measures how much volunteer effort a subject received, not just whether it is a usable spiral.

I do accept `>=5` as the conservative native floor for feasibility. It is tied to GZD-5's low-retirement regime, and because it is a downstream node it also implies at least five volunteers traversed the upstream featured/not-edge-on path. It is strict enough to remove the one-voter conditional-fraction failure, but not so strict that it turns active-learning allocation into the sample definition.

The steep `>=3` to `>=5` drop is real enough to preserve, not smooth over. It probably reflects the discrete retirement structure and the branching nature of the tree. The preregistration must not interpolate across the ladder; it should freeze one floor. My recommendation is:

> Primary feasibility floor: `has-spiral-arms_total-votes >= 5`; report `>=2`, `>=3`, and `>=10` only as sensitivity diagnostics.

Under that primary floor, the restricted conditional fraction is `18.23%`, comfortably above the `13.06%` break-even.

## Repair 3: Claim Boundary

PASS WITH TEXTUAL CLEANUP.

The repaired claim is correctly bounded:

> The DR10.1 South route appears feasible for a Longo-amplitude test if additional keyspace is counted.

It also retains the two necessary caveats:

- this is acquisition feasibility, not a closed accepted-yield count;
- the full-keyspace parent is an extrapolation over BRICKID keyspace, not a counted sky-area bound.

But the earlier body still says "Closed" in the title and contains superseded verdict language including "securely satisfies." That is not fatal to the feasibility conclusion, but it is not acceptable for a frozen preregistration evidence packet unless explicitly marked superseded.

## Least-Favourable Defensible Choice

Taking the least favourable defensible choices simultaneously:

- use the repaired restricted conditional formulation;
- use Tori's measured Cut-6 survival, `82.404622%`;
- use Yui's one-sided lower retention, `85.72%`;
- use the conservative GZD-native primary floor, `has-spiral-arms_total-votes >= 5`;
- keep the full-keyspace parent as an acquisition target, not a counted result.

The decisive fraction is `18.23%`, above the `13.06%` break-even. Therefore the program is not dead on accepted-yield grounds.

Using `>=10` would kill the route, but I do not treat that as a fair least-favourable morphology criterion without a separate argument that ten downstream votes is a morphology-quality threshold rather than a classification-depth selector. The present record gives the opposite indication.

## Required Repairs Before Citation Or Freeze Assembly

1. Mark sections 2-4 of the receipt as superseded diagnostics, or rewrite them so the repaired formulation is the only authoritative calculation.
2. Replace the title phrase `Closed` with a bounded status such as `Acquisition Feasibility Repaired; Yield Not Yet Closed`.
3. Freeze `has-spiral-arms_total-votes >= 5` as the primary feasibility floor if this path proceeds; leave `>=10` as a depth-regime sensitivity, not as the primary kill switch.
4. Preserve the warning that the current keyspace count does not itself meet 100,000 and that no sky run is authorized.

## Plain Answer For Duho

The repaired feasibility finding is good enough to proceed to preregistration assembly work, but not to freeze or run.

Safe to assert:

> Accepted-yield feasibility is no longer the blocker. Under a defensible GZD-5-native downstream vote floor of `>=5`, the restricted spiral fraction is `18.23%`, above the `13.06%` break-even, so the Longo-amplitude route appears feasible if additional DR10.1 South keyspace is counted.

Not safe to assert:

> The accepted-yield requirement is closed, or the study may now run on sky data.

No sky run, preregistration freeze, publication, commit, or acceptance follows from this gate.
