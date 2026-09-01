# Low-human hand-check calibration options

## Finding

The load-bearing constraint can be met without changing the frozen estimator, but not by eliminating human judgements altogether. The leading admissible design is: **one independent checker completes the inherited 850-presentation HC-1H stream; Duho makes at most 30–50 independently sampled audit decisions that do not enter `a`.** Stage two must explicitly replace “one human checker (Duho)” with “one named independent human checker,” define Duho's small audit as a protocol-quality check only, and preserve every sampling, blinding, synthetic correction, repeat, floor, and estimator rule.

This is a real amendment, not an interpretation of stage one. It transfers the volume; it does not make it disappear.

## What `a` actually requires

The v9 bytes define, for each of three calibration bins,

`raw_b = agree_b/n_b`, `a_b = (raw_b - epsilon)/(1 - 2 epsilon)`,

and globally the same transformation of pooled agreement. Here `agree` means agreement between the instrument sign and a **human handedness label on a sampled real object**. The global `epsilon` is the human's error rate on blind ground-truth synthetic injections. `accuracy_from_handcheck()` propagates two uncertainties:

`Var(a_b) = raw_b(1-raw_b) / [n_b(1-2epsilon)^2] + [(2a_b-1)/(1-2epsilon)]^2 sigma_epsilon^2`.

The shared `epsilon` creates nonzero covariance between bins. The scalar uncertainty is the analogous expression at pooled `N`. The estimator therefore needs:

- random human labels on real objects, with known inclusion/allocation weights;
- enough labels in each of three calibration bins and each of nine inherited HC strata to satisfy the frozen allocation floors;
- blind synthetic human judgements to estimate the checker's `epsilon`; and
- a human repeat stream if HC-1H's self-consistency and identity-exposure checks are retained.

It does **not** statistically require that the human be Duho. It does require that the human reference whose real labels define agreement be calibrated by the synthetics under the same blinded task. A small Duho audit cannot substitute for the volume checker's calibration unless Duho, rather than that checker, supplies the real reference labels.

### Scale of sampling uncertainty

For orientation, the ideal uncorrected binomial standard error at accuracy `a=0.90` is `sqrt(.9*.1/N)`:

| labels N | ideal sigma |
|---:|---:|
| 850 | 0.0103 |
| 500 | 0.0134 |
| 200 | 0.0212 |
| 100 | 0.0300 |
| 50 | 0.0424 |

Those figures are optimistic: v9 has three bins and a shared synthetic-error term. As a concrete, nonbinding arithmetic point using only the v9 formula, take corrected `a=0.90`, `epsilon=0.05`, and 200 synthetics, so `raw=0.86` and binomial `sigma_epsilon=0.0154`. With real labels divided equally among three bins:

| real N | pooled sigma_a | per-bin sigma_ab | corrected point `a_b` needed approximately for `a_LB_b >= .85` at the displayed sigma |
|---:|---:|---:|---:|
| 850 | 0.0190 | 0.0267 | 0.894 |
| 500 | 0.0220 | 0.0329 | 0.904 |
| 270 | 0.0272 | 0.0429 | 0.921 |
| 200 | 0.0305 | 0.0492 | 0.931 |
| 100 | 0.0409 | 0.0682 | 0.962 |
| 50 | 0.0562 | 0.0954 | >1.00 |

The last column is `0.85 + 1.645 sigma_ab` evaluated at the stated `a=.90` operating point; it illustrates power loss, not an exact prospective threshold because sigma itself changes with realized agreement and allocation. Perfect agreement can mathematically clear the bound even at small N because its raw binomial term collapses. Thus there is no sample size at which the `.85` bound becomes algebraically impossible for every dataset. There is, however, a hard **design** cutoff.

`HC_MIN_PER_CELL=10` over three calibration bins and `HC_MIN_PER_STRATUM=30` over nine live strata imply, exactly as `allocate_handcheck()` computes,

`sum_j max(30, 10 * live_cells_j)`.

If all three cells are live in all nine strata, this is `9 * max(30,30) = 270` real labels. Therefore real budgets of 200, 100, or 50 are **inadmissible under the frozen floors**; they fail before labels are allocated. A 270-real-label budget is the smallest generally admissible total when all nine strata and all three bins are live. Sparse configurations can still fail for lack of objects, and fewer live cells do not reduce a live stratum below 30. The inherited 500-real budget is comfortably feasible but materially more precise.

The prompt's N=850 is a presentation budget, not v9's real calibration N: HC-1H contains only 500 real first presentations; 200 synthetics estimate `epsilon`, and 150 mirrored repeats measure consistency rather than add independent real objects. Treating all 850 as independent trials for `a` would be wrong.

## Admissible options under the constraint

### Option 1 — one independent volume checker; Duho audits 30–50 items (leading)

The independent checker makes all **850 decisions** (500 real, 200 blind synthetics, 150 mirrored re-presentations), with up to 1,700 committed renders under `R_max=2`. This is plainly hundreds of decisions, but they are not Duho's. Duho makes a preregistered random 30–50-item audit on non-overlapping or separately sealed presentations. His audit tests instruction clarity, interface parity, and gross reproducibility; it does not enter `a`, alter labels, adjudicate disagreements, or expose running results.

Stage two must explicitly replace the inherited checker identity, name or prospectively qualify the independent checker, bar that person from all other roles, and bind that checker's real labels and synthetic `epsilon` together in BS-8f. It must also state the audit sampling frame, blindness, permitted outputs, and a prospective consequence for audit failure. The one-checker estimator and v9 code remain unchanged.

Cost: recruitment and 850 decisions remain; only Duho's burden is reduced. The scientific cost is a change of human reference population: `a` becomes the named independent checker's synthetic-error-corrected accuracy, not Duho's. The benefit is stronger role separation and operational blindness. This is the narrowest defensible amendment.

### Option 2 — multiple independent/crowd checkers split the allocated stream; Duho audits at most 50

Several qualified checkers divide the 500 real allocations, 200 synthetics, and 150 repeats, so no one necessarily performs hundreds. Duho makes 30–50 audit decisions. Each checker must receive enough blinded synthetics and repeats to estimate or bound checker-specific error and consistency; assignments must be randomized within every calibration-bin × inherited-stratum cell.

This is not HC-1H. Stage two must replace the single-checker structure and preregister the estimand and combination rule: for example, a fixed checker-weighted Horvitz–Thompson agreement estimator with checker-specific synthetic-error terms and cluster-robust/bootstrap covariance. A simple pooled proportion pretending labels are exchangeable is not adequate. Agreement statistics (pairwise overlap, Fleiss' kappa or Krippendorff alpha, plus raw confusion tables) are diagnostics; they do not create truth. A small fixed overlap sample is required to identify checker effects, but majority vote is permissible only if its accuracy and covariance model are frozen prospectively.

Cost: greater code and covariance complexity, heterogeneous skill, platform-quality risk, and loss of the clean one-reference interpretation. The frozen `A_L=beta/(2a-1)` still works only if the revised `a` is explicitly the effective accuracy of the final preregistered aggregate human labeling rule. Existing `accuracy_from_handcheck()` would need revision and re-gating.

### Option 3 — one independent checker, smaller but floor-respecting budget

Set **270 real first presentations**, the hard all-live-strata minimum, rather than 500. Retain enough blind synthetics to estimate the checker's shared `epsilon`; keeping 200 preserves the inherited synthetic-error precision. Retain a preregistered repeat subset, for example 50–81, sufficient only for a coarse consistency diagnostic. Total independent-checker work would then be roughly 520–551 decisions, still hundreds, while Duho performs at most 30–50 audit decisions.

Stage two must explicitly revise `HC_REAL_LABELS=500`, the 850 composition, repeat count, allocation receipt, expected precision, and any fixed category counts, while retaining the 10-per-cell and 30-per-stratum floors. At the illustrative `.90/.05` point, pooled sigma rises from about .0220 at 500 real labels to .0272 at 270, and balanced per-bin sigma from .0329 to .0429. A corrected bin near .90 is then unlikely to clear `a_LB_b>=.85`; approximately .921 is needed at that displayed uncertainty. The v9 estimator remains valid, but calibration halts and Stage-C power failures become substantially more likely.

Budgets of 200, 100, or 50 real labels are not options while the frozen floors remain. Revising those floors would be a deeper scientific amendment and would leave some of the nine-stratum/cell coverage guarantee behind.

### Option 4 — distributed expert panel with a fixed aggregate label per object

Use three or more independent experts, each seeing a randomized subset, with a prospectively fixed overlap graph and a fixed aggregation rule. No expert, including Duho, need exceed 50 decisions if enough experts are recruited; total human work remains at least the floor-respecting volume plus controls. Each aggregate real-object call is compared with the instrument, and aggregate-rule accuracy is calibrated on synthetics constructed and assigned in the same way.

This differs from Option 2 in making the panel's aggregate call—not a pooled individual call—the reference. Stage two must define missing-vote handling, abstentions, ties, overlap, dependence, synthetic calibration of the aggregate rule, and covariance. Existing HC-1H code is not sufficient. `A_L=beta/(2a-1)` remains conceptually valid for the aggregate rule if sign-symmetric error is retained and tested, but a new `accuracy_from_handcheck()` implementation and full re-gate are necessary.

Cost: many people, coordination, and model risk. Agreement statistics quantify reproducibility, not correctness on real images. This option is useful only if recruiting one sustained independent checker is harder than recruiting a panel.

### Option 5 — synthetic-only/machine-only calibration (not admissible for the frozen estimand)

The 200 blind synthetic injections have known signs, but their HC-1H role is to estimate **human reference error `epsilon`**. They do not estimate the instrument-versus-human agreement on real objects. Running the instrument alone on known synthetic truth estimates synthetic-domain machine accuracy, not the real accepted-sample accuracy required to deattenuate `beta`. The frozen text also says the machine committee is stratifier/allocator/diagnostic only, never inside `a`.

A machine-only route would therefore require redefining `a` as synthetic-domain instrument accuracy and adding an unverified synthetic-to-real transport assumption exactly where real morphology may differ. That does not preserve what the frozen estimator requires and is not an admissible calibration path from the present bytes. It could be preregistered only as a separate sensitivity analysis or a conservative no-correction/inconclusive path, never as a replacement BS-8f value.

### Option 6 — external pre-existing truth labels, if a genuinely independent blinded source exists

Stage two could use a preregistered external human-labeled reference set or catalogue, with Duho making at most 30–50 audit decisions, **only** if its labels cover a probability sample of the accepted real population or support a valid transport/weighting design, its parity/sign convention is independently anchored, and it was not selected using this instrument's outputs. Synthetic controls would still be needed to calibrate the external labeling process or bound its error.

No such source is established by the inspected bytes, so this is conditional, not execution-ready. It would revise sampling, custody, checker identity, and error modeling and likely require a new estimator implementation. Convenience labels without coverage and provenance do not supply `a`.

## Exact stage-two amendment for the leading option

Stage two should say, in substance:

> **Explicit supersession of inherited HC-1H identity only.** Stage one's carried quotation “one human checker (Duho)” is superseded. The sole volume checker is one prospectively named or qualification-selected independent human holding no other study role. That checker completes the sealed 850-presentation stream: 500 probability-sampled real first presentations, 200 blind ground-truth synthetic injections, and 150 randomized mirrored re-presentations, under the inherited parity, sealed-key, replacement, replay, stratum, and integrity rules. The checker's real agreement counts and that same checker's global synthetic error estimate are the sole human inputs to `accuracy_from_handcheck()` and BS-8f. Duho completes at most 50 separately sealed, preregistered audit presentations; those labels are diagnostic only and never enter `a`, `epsilon`, allocation, adjudication, replacement, or a verdict. Audit failure has a prospectively fixed fail-closed consequence and cannot trigger relabeling after values are known.

It must also preserve and quote: the three calibration bins; nine inherited strata; random within-cell allocation; `HC_MIN_PER_CELL=10`; `HC_MIN_PER_STRATUM=30`; `HC_REAL_LABELS=500`; the 200/150 controls; shared-`epsilon` covariance; per-bin `a_LB_b>=.85`; scalar/profile branch rule; blind categories and parity; identity-exposure and key-compromise triggers; and no machine result inside `a`.

The honest cost is that the reported calibration describes one independent checker's reference behavior rather than Duho's, and stable checker-specific real-image mistakes remain identifiable only to the extent the synthetic realism and repeat diagnostics expose them. It preserves precision and code semantics, not the identity-specific validity claim.

## What cannot be preserved

- The literal “one human checker (Duho)” rule cannot coexist with fewer than roughly 50 Duho decisions while retaining 500 real labels and 350 controls. It must be superseded.
- The original evidence about **Duho's** own 500-real-object accuracy cannot be obtained from another checker's labels. What is preserved is the estimator's need for a calibrated human reference, not that person's identity.
- No machine-only analysis of the 200 synthetics can establish real accepted-sample accuracy without a new, strong synthetic-to-real transport assumption. The frozen machine-committee exclusion cannot be preserved if machines are put inside `a`.
- With all nine strata and all three calibration cells live, fewer than 270 real labels cannot preserve both frozen allocation floors. A 50-, 100-, or 200-real-label design must either fail or explicitly abandon those coverage protections.
- Reducing 500 real labels to 270 cannot preserve the original per-bin precision or verdict power. Near-boundary runs will more often halt `INCONCLUSIVE-BY-CALIBRATION` or fail Stage C.
- Splitting work among checkers cannot preserve HC-1H's single-reference semantics without a new aggregation/error model and re-gating. Agreement alone is not ground truth.
- The 150 repeats and 200 synthetics are mandatory under literal inherited HC-1H. Shrinking them forfeits, respectively, repeat-consistency sensitivity and precision in the shared human-error correction. They may be revised in stage two, but not silently described as preserved.

SEAT: CODEX
VERSION: LOWHUMAN-V1
VERDICT: OPTIONS-READY
COUNT: 6
