# Distributed expert panel design

Status: concrete Option 4 design for ratification. This is an explicit replacement of HC-1H's quoted “one human checker (Duho)” architecture, not an interpretation of it. It preserves the frozen real-sample floors, the 200 blind synthetic objects, the 150 mirrored re-presentations, `R_max=2`, blindness/integrity rules, and the downstream calibration gates. No image bytes or χ-bearing values were inspected.

## 1. Load-bearing arithmetic and minimum headcount

The panel reference is a three-person majority call. Consequently every real object, every synthetic control, and every mirrored repeat must be independently decided by **three distinct panelists**. Anything less changes the aggregate rule by category and does not calibrate on synthetics “assigned the same way.” `R_max=2` means exactly two committed render events per assigned presentation; it doubles render commits, not decisions.

The frozen real-label floor is

`9 strata × max(30 per stratum, 3 live cells × 10 per cell) = 270 aggregate real-object calls`.

For a real-object budget `N`, the lower-bound workload is therefore

`D = 3 × (N real + 200 synthetic + 150 mirrored repeat)`,

and committed renders are `2D`. The 150 repeats are controls, not additional independent real objects. The figures exclude flagged-item replacements, abstention replacements, training, dropouts, and Duho's optional diagnostic audit; hence they are optimistic lower bounds.

| aggregate real calls | real decisions | synthetic decisions | repeat decisions | total decisions | committed renders | people @ 50 | people @ 40 | people @ 30 | people @ 20 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 270 (floor) | 810 | 600 | 450 | **1,860** | 3,720 | **38** | 47 | 62 | 93 |
| 500 (inherited) | 1,500 | 600 | 450 | **2,550** | 5,100 | **51** | 64 | 85 | 128 |

All headcounts are `ceil(total decisions / cap)`. Thus 37 people at cap 50 supply only 1,850 decisions and cannot execute even the 270-real floor design.

The control burden must be spread across the whole panel. Balanced assignment gives each panelist the same category proportions, up to integer rounding:

| real budget | real share of each person's queue | synthetic share (calibrates that panelist's error) | mirrored-repeat share | average decisions/person at the minimum 50-cap headcount |
|---:|---:|---:|---:|---:|
| 270 | 270/620 = 43.55% | **200/620 = 32.26%** | 150/620 = 24.19% | 1,860/38 = 48.95 |
| 500 | 500/850 = 58.82% | **200/850 = 23.53%** | 150/850 = 17.65% | 2,550/51 = 50.00 |

Those fractions preserve the mandatory control composition at the presentation-object level. At the 50-cap minima they yield only about 15.8 synthetics per person in the 270 design and 11.8 in the 500 design. That identifies person-specific error but estimates it very noisily. No larger per-person synthetic minimum is frozen, so inventing one would not be “arithmetic from frozen constants”; any scientifically desired minimum would increase headcount or force fewer real decisions per person. The aggregate rule's error is estimated from 200 three-vote synthetic calls, not by pretending the roughly 12–16 controls make every individual's error precise.

Duho may take at most 30–50 separately sealed diagnostic decisions, but because Row G bars a member holding another role, those decisions cannot make him a panel voter and do not reduce the counts above. They do not enter `a`, `epsilon`, adjudication, or replacement.

## 2. Fixed overlap graph

Use a preregistered balanced incomplete **3-uniform block design**:

- Panelists are vertices. Each presentation object is one block containing exactly three distinct vertices; those three panelists see it and no one else does.
- Every first real object, blind synthetic, and mirrored repeat is a three-vertex block. A mirrored repeat uses the same trio as its selected real first presentation, while its later queue positions and within-view parity remain independently sealed.
- Blocks are assigned to make each panelist's total degree differ by at most one, each category-specific degree differ by at most one, and each unordered pair's co-rating count differ by at most one subject to the repeat-pair constraint. Within real objects, the same balance is imposed inside every calibration-bin × inherited-stratum cell.
- The incidence matrix and category-blind opaque queue tokens are frozen before Row G. Checkers never see another checker's label, machine/instrument sign, category, stratum, identity, running tally, or aggregate.

This is the minimum-cost overlap compatible with a strict majority call: all objects already need three votes, so the three votes simultaneously supply the overlap. There is no additional overlap row hidden outside the arithmetic. At 270 real calls there are 620 presentation blocks and 1,860 pair-incidences; at 500 there are 850 blocks and 2,550 pair-incidences. Recurrent, balanced pairs distinguish a checker main effect from object difficulty and expose pair dependence. A design in which most objects receive one vote plus a small overlap sample would be cheaper, but its “panel call” would usually be one person's call and its synthetic calibration would not describe a three-vote aggregate; it is rejected.

The allocator must fail before image access if it cannot meet all degrees, category balance, real-cell floors, trio distinctness, and pair-balance constraints. Panelists may not be substituted after labels are known. Recruitment and qualification close before the incidence graph is sealed.

## 3. Aggregate call, estimand, and covariance

Each panelist returns `LEFT`, `RIGHT`, or frozen `ABSTAIN`. After sealed-key de-mirroring:

- two or three matching non-abstaining votes produce that sign;
- a 2–1 split produces the majority sign;
- zero or one non-abstaining vote, or one vote each way with a third abstention, produces `NO_CALL`;
- there is no adjudicator, confidence weight, post hoc expert weight, or discussion.

The allocation target is 270 or 500 **usable aggregate real calls**, including every required cell/stratum floor. A `NO_CALL` or a timely `suspected-identifiable` flag invokes only the frozen same-stratum-and-category replacement path before key opening. Because replacements consume three more decisions and up to six render commits, the table is a mathematical minimum, not a safe recruitment plan. If the personnel caps leave no spare capacity, the run fails closed at the first required replacement.

Let `M_i` be the fixed majority call on real object `i`, and `S_i` the instrument sign. In each calibration bin `b`, `raw_b` is the allocation-weighted probability estimate `P(M_i = S_i | b)` over usable probability-sampled real objects; `raw` is its frozen population-weighted aggregate. Let `epsilon_M = P(M_j != T_j)` on the 200 blind synthetic objects with known sign `T_j`, each assigned to a trio by the same graph rule. The panel estimand is the effective accuracy of the **three-person majority rule**:

`a_b = (raw_b - epsilon_M)/(1 - 2 epsilon_M)`,

with the global `a` formed under the same frozen population/allocation weights. Accordingly `A_L = beta/(2a-1)` retains its interpretation only for this aggregate reference and only if the inherited sign-symmetric-error assumption remains declared and tested. Individual checker accuracies and repeat consistency are diagnostics; they are not averaged to manufacture `a`.

Inference uses a preregistered crossed random-effects model (checker intercepts plus object intercepts, with checker-pair covariance) fitted jointly to individual real, synthetic, and repeat decisions, and a **graph-preserving parametric bootstrap** over checker and object effects. Each replicate reconstructs majority calls, `raw_b`, `epsilon_M`, `a_b`, global `a`, lower bounds, and full `Cov_a`. A two-way checker/object cluster-robust sandwich is reported as a sensitivity check. The production covariance is the bootstrap covariance because majority voting is nonlinear and the same checker appears across bins and categories. A pooled binomial proportion is inadequate: it treats 1,860 or 2,550 correlated votes as exchangeable independent truth labels, ignores repeated panelists and mirrored objects, and estimates individual-vote rather than majority-rule uncertainty.

## 4. Stage-two build and re-gate

`accuracy_from_handcheck()` must be retired for panel receipts and replaced by `accuracy_from_panel()` with no fallback to the one-human formula path. Stage two must build:

1. `allocate_panel_graph()`: constructs and seals the three-uniform incidence graph; enforces distinct trios, decision caps, category-degree and pair balance, the 3 × 9 real allocation, `HC_MIN_PER_CELL=10`, `HC_MIN_PER_STRATUM=30`, and infeasibility refusal.
2. `ingest_panel_labels()`: accepts only the pinned Row-H schema and one sealed label set per panelist; verifies exact traversal, two render commits per assigned presentation, no cross-panel leakage, key custody, cap compliance, and no intermediate/export path.
3. `aggregate_panel_calls()`: de-mirrors only after authorized key opening, applies the fixed majority/`NO_CALL` rule, executes no adjudication, and produces the χ-bearing aggregate label-set receipt and sealed store.
4. `accuracy_from_panel()`: applies allocation weights, estimates majority-rule `epsilon_M` from the 200 identically assigned synthetics, computes global/per-bin corrected accuracy and lower bounds, fits the crossed checker/object/pair model, runs the graph-preserving bootstrap, and emits full `Cov_a` plus integrity triggers.
5. `adjudicate_panel_path()`: preserves the frozen rule `max_b |a_b-a| <= 0.03` and every `a_LB_b >= 0.85` for scalar; spread failure alone selects profile; any `a_LB_b < 0.85` halts `INCONCLUSIVE-BY-CALIBRATION` before Stage C or unblinding.

Mandatory fixtures include: exact 38- and 51-person feasible graphs; 37-person/50-cap floor refusal; every other table boundary; pair/category/cell imbalance refusal; duplicated voter in a trio; cap overflow; missing/incomplete label set; synthetic assignments differing from real assignments; repeat assigned to a different trio; parity/de-mirroring; every abstention pattern; 3–0 and 2–1 majorities; `NO_CALL` replacement accounting; known synthetic majority error; heterogeneous checker error; perfectly correlated checker pair; shared-checker cross-bin covariance; mirrored-repeat dependence; deterministic bootstrap seed/serialization; non-finite/degenerate `epsilon_M`; and BS-8f round-trip into Stage C.

The re-gate must compare the amended quotation, Row G/H access chain, sealed-key custody, HC-5/HC-6/HC-7 triggers, allocation receipt, aggregate label-set receipt, BS-8f schema, `Cov_a`, scalar/profile branch, Stage-C consumer, and BS-V consumer against executable code and byte-pinned fixtures. All prior gates that assumed one checker or `accuracy_from_handcheck()` are stale and must be rerun. No real image access is authorized until both independent gate seats pass the complete panel path.

## 5. Honest verdict

This panel is **infeasible for a small research group under the stated cap**. The smallest admissible version needs 38 qualified, independent, role-separated people completing tightly blinded queues; the inherited 500-real version needs 51. That is before recruiting reserves for withdrawal, abstention replacement, suspected-identity replacement, or a failed label set. The design therefore does not solve the recruiting bottleneck—it converts one unavailable 850-decision checker into a much larger coordination and recruitment problem.

The remaining honest paths are: obtain a genuinely independent external labeled source with defensible sampling/transport and error calibration; explicitly revise the frozen real/control floors and accept lower coverage, precision, and power; narrow the study scope so fewer live strata/cells are scientifically claimed under a newly frozen design; or declare hand-check calibration infeasible. The last choice means BS-8f cannot supply `a`, `Cov_a`, or the required lower bounds, so Stage C cannot run and no calibrated `A_L = beta/(2a-1)` confirmatory result or production verdict may be formed. It is an inconclusive/abandoned calibration, not permission to substitute machine committee output or a synthetic-only `a`.

SEAT: CODEX
VERSION: PANEL-V1
VERDICT: INFEASIBLE
COUNT: 38
