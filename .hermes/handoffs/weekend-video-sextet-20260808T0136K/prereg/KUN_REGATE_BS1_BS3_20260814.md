# KUN_REGATE_BS1_BS3_20260814

Timestamp: 2026-08-14 KST

Target brief: `prereg/_tmp_KUN_REGATE_BRIEF_20260814T1600K.md`

Primary receipt inspected: `prereg/TORI_FOOTPRINT_VARIANCE_RECEIPT.md`

Boundary: read-only re-gate. I did not query NOIRLab, export rows, inspect images, compute chirality, run a sky statistic, freeze a preregistration, publish, commit, push, or accept anything for Duho.

## Verdict

**PASS WITH REPAIRS.**

BS-1's footprint-variance item is satisfied on the bounded Tier-3 route. The delivered value is not the literal per-object trigonometric aggregate named in the first BS-1 wording, but it is the exact substitute I authorized in `KUN_VARIANCE_APPROACH_AUDIT.md`: exact post-Cut-6 counts per brick, frozen brick centres, local Longo-axis geometry, and a conservative intra-brick error bracket with fail-closed semantics.

BS-3 is not disturbed by the Tier-3 route. The instrument evidence is substantively complete against my 11-item blocker list, including the later R4/R5 receipts and the corrected 85.72% retention lower bound. One assembly repair is required before a freeze candidate may claim BS-3 cleanly: the preregistration slot table must not say `identity 1,000/1,000` unless the final production witness is actually a 1,000-probe production receipt, or it must rewrite that line to cite the landed production evidence exactly.

The preregistration is **not ready to freeze** as-is. BS-1/variance and BS-3 no longer appear to be the blockers, but the assembled preregistration still needs named open slots and wording repairs cleared before a freeze gate.

## 1. BS-1 Tier-3 Substitution

**PASS.**

The delivered statistic is:

- frozen dered Cut-6 population: `832,393`;
- nonempty selected bricks: `270,577`;
- count-weighted brick-centre `mean(cos theta)`: `-0.109116141652194`;
- count-weighted brick-centre `mean(cos^2 theta)`: `0.457107680481017`;
- count-weighted brick-centre `var(cos theta)`: `0.445201348111956`;
- conservative object-variance interval: `[0.432801348111956, 0.457601348111956]`;
- threshold: `0.15`.

This closes the scientific purpose of BS-1: object-weighted angular spread around Longo's fixed axis is far above the minimum needed for a meaningful fixed-axis amplitude test.

It must be described accurately. Safe wording:

> BS-1 footprint adequacy passes on the bounded Tier-3 brick-centre route, not on an exact per-object server-side trigonometric aggregate.

Unsafe wording:

> We measured exact per-object `var(cos theta)` from object coordinates.

That latter sentence would be false.

## 2. Error Bracket

**PASS.**

The bracket is conservative in the right direction. For unit sky vectors, `cos(theta) = a dot r` is 1-Lipschitz under angular displacement because `|a dot r_1 - a dot r_2| <= |r_1-r_2| <= angular_distance(r_1,r_2)` for the small angles here.

With half-diagonal `0.177 deg = 0.00309 rad`, every object's centre-substitution error is bounded by `epsilon <= 0.00309` in `x = cos(theta)`.

For `x in [-1,1]` and `y = x + e`, `|e| <= epsilon`:

- the mean error is at most `epsilon`;
- the second-moment error is at most `2epsilon + epsilon^2`;
- the variance error is safely below `4epsilon`.

Using `4 * 0.00309 = 0.01236`, rounded up to `0.0124`, is honest. The receipt applies it conservatively:

- lower pass-side bound: `0.445201348111956 - 0.0124 = 0.432801348111956`;
- margin above threshold after the bound: `0.282801348111956`;
- binding pass test: `V_center - 0.15 >= 0.0248`, which is satisfied because `0.295201348111956 >= 0.0248`.

The bracket was not used to make a marginal value pass. The lower bound is nearly three times the threshold.

## 3. Sanity Check On `var(cos theta) = 0.445`

**PASS, with the caveat that the high value must be explained in the freeze text.**

The value is high relative to a full-sphere uniform `1/3`, but it is physically plausible for this footprint and axis. The receipt's own range shows selected brick centres reaching almost both ends of the axis:

- minimum centre `cos(theta)`: `-0.9999988623867118`;
- maximum centre `cos(theta)`: `0.9999988623867118`.

My read-only local sanity check reproduced Tori's intended-axis moments from the combined per-brick counts and static brick centres:

- intended axis `(RA,Dec)=(216.984434, 32.060611)`: mean `-0.109116141652194`, second moment `0.457107680481017`, variance `0.445201348111956`;
- unweighted nonempty-brick quantiles of `cos(theta)` were approximately `[-1.000, -0.901, -0.745, -0.307, 0.548, 0.838, 1.000]`, i.e. a broad two-lobe footprint, not a compact cap.

The adversarial failure modes do not fit the observed pattern:

- using the antipode flips the mean sign but leaves variance unchanged, so the variance pass does not depend on axis sign;
- swapping RA/Dec gives variance about `0.328`, distinguishable from the receipt;
- incorrectly treating Longo Galactic `(l,b)=(52,68.5)` as equatorial `(RA,Dec)` gives variance about `0.195`, still passing but not the landed value;
- a radians/degrees mistake would not naturally produce the exact receipt axis unit vector and the symmetric near-`+/-1` extrema from valid brick centres.

The strongest explanation is geometric, not erroneous: DR10 South spans a large high-latitude footprint, and Longo's axis lies close enough to a pole-like direction that the selected footprint contains weight near both the axis and its antipode. A two-lobe footprint can have variance above `1/3`.

Required freeze-text repair: state this as a footprint-adequacy statistic and mention that values above `1/3` are possible for a non-uniform/two-lobe footprint. Do not let a reader infer that `0.445` is a handedness amplitude or sky-result statistic.

## 4. BS-3 Re-Gate

**PASS WITH ASSEMBLY REPAIR.**

The 11 blockers from my earlier BS-3 gate are now substantively accounted for:

1. full generator-code hash present: `89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75`;
2. master seed present: `LONGO-AMPLITUDE-FREEZE-M1`;
3. materialized training manifest present: `train-20000`, hash `498a505c84bb6d70058299e05c78d3ac1f025042ec173c405b404743d2742872`;
4. reproducibility object declared as frozen weights plus generator, not retrainability;
5. weights file and canonical flat-parameter hashes present;
6. tau present: `4.4006456017494235`, null manifest `null-8000` hash present;
7. operative retention present and corrected to `86.24%` central / `85.72%` one-sided lower 95%;
8. production mirror/antisymmetry receipts present;
9. signed-zero receipt present with value comparisons, not sign-bit comparisons;
10. R4 interpolating-mirror canary present and passing;
11. R5 paired raw-output / flip-imbalance receipt present, with `dA_raw = +0.015` on 200 synthetic probes and no production antisymmetry failure.

The Tier-3 variance route does not touch BS-3. It uses exact aggregate counts and static brick-centre geometry over the frozen parent population. It does not read survey images, run the estimator, change tau, change retention, change weights, or compute handedness.

Required assembly repair: the preregistration slot table currently says BS-3 requires `identity 1,000/1,000 bit-exact`. The landed production receipts include `200/200` R1/R2 production probes, `2,727/2,727` high-inclination nonzero identity probes, and `256/256` exact-edge probes. The old appendix also cites the spike's `1000/1000`, but the spike is not the final production receipt. Before freeze, either:

- run and receipt the exact 1,000-probe production identity test named by the slot table; or
- amend the slot table to cite the actual landed production identity witnesses and have that amendment re-gated.

This is an assembly/custody repair, not a reason to reopen estimator design.

## 5. Freeze Readiness

**Not ready to freeze.**

Closed by this re-gate:

- BS-1 footprint variance / spread check: **CLOSED on bounded Tier-3 route**.
- BS-3 production estimator: **SUBSTANTIVELY CLOSED, with the identity-count wording repair above required before freeze assembly**.

Remaining blockers I can name from the files inspected:

1. **BS-1 derived-catalogue publication licence**: still open in `TORI_SURVEY_ROUTE_BINDING_20260812.md` and `TORI_BS1_CLOSURE_PACKET.md`; image CC BY language must not be silently extended to derived catalogue publication.
2. **BS-2 covariate products**: no final exact product/coverage receipt found here closing the `>=8/10` covariate survival rule, photo-z decision, and deblend-flag decision.
3. **BS-4 secondary instrument spec**: not re-gated here as filled.
4. **BS-5 Longo sign dictionary**: the draft still lists this as `[VERIFY]`; it needs verbatim source quotation and mapping.
5. **BS-6 photometric cut constants**: final freeze needs the bound constants cited to survey documentation and no chirality/morphology-label dependence.
6. **BS-7 distortion branch**: final declared branch and receipt are not re-gated here as filled.
7. **BS-8 power receipt**: must be rerun/evaluated at bound `N` and measured attenuation/accuracy, not inherited from an earlier indicative curve.
8. **BS-9 evaluated constants table**: must be printed at bound `N` and measured `a`, including `sigma_ours <= 0.008` and detection floor `<=0.025`.
9. **BS-10 Shamir amplitude class**: draft still marks it `[VERIFY]`; informational only, but the slot must be filled or explicitly dropped by a gated prereg revision.
10. **Assembled freeze candidate absent**: the current `PREREG_LONGO_AMPLITUDE_TEST_20260812.md` is still a draft with open-slot language. A clean assembled preregistration must remove `[VERIFY]`, `[UNKNOWN]`, ellipsized hashes, and stale "drafting in parallel" language, then return as exact bytes for gate.

## Plain Answer For Duho

The variance blocker that caused the 14-hour stall is cleared by a cheaper and scientifically valid route. The number is high, but not suspicious after checking the footprint geometry and bad-axis alternatives. The safest statement is:

> The frozen Cut-6 footprint has enough object-weighted angular spread around Longo's axis; BS-1's variance/spread requirement passes on the bounded Tier-3 brick-centre route.

BS-3 is substantively ready, but the freeze document must not overstate the identity witness as `1,000/1,000` unless that exact production receipt exists.

No sky run, preregistration freeze, publication, commit, push, or acceptance is authorized by this gate. Duho owns acceptance.
