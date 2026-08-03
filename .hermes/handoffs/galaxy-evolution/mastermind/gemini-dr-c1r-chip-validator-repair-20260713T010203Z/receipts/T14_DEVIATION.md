# T14 deviation — coordinator adjudication required

The first GREEN integration attempt reached the real sealed HTML and matched every T14 pin except two C6 details. Per the binding stop condition, Tori stopped instead of editing the test or pin.

## Deviation 1 — pinned FLAMINGO comparison not detected

Pinned residue requires five S1 emergent-cell `UNLABELED_COMPARISON` findings plus GAP1. The implementation produced four S1 findings plus GAP1.

The missed pinned cell is FLAMINGO emergent (`table_row_10`, role `emergent`):

> The calibrated simulations successfully reproduce a variety of complex cluster scaling relations and thermodynamic density and temperature profiles that were strictly excluded from the initial machine-learning-driven Gaussian process emulation and calibration methodology.

It has a simulation reference and result verb (`reproduce`) but does not contain Lana §4.2's literal observation-reference words (`observed|observation|observational|survey|empirical|data`). Lana nevertheless states this rule yields the five-cell pin, so the prose rule and pin are internally inconsistent on this unit.

Proposed bounded resolution: for typed S1 `emergent` cells only, treat `cluster scaling relations` / `thermodynamic ... profiles` as an observational-comparison reference when paired with a simulation reference and result verb. This preserves per-cell typing and adds only the pinned FLAMINGO unit.

## Deviation 2 — unexpected numeric-fraction finding on a model parameter

The numeric gate correctly removed the three known bare-word false positives, but it also found a separate `MISSING_QUALIFIER` in SIMBA `feedback_params` (`table_row_6`, cell 2):

> The simulation explicitly tuned the fraction of material entering the accretion disc that actually accretes onto the central black hole to a value of ∼10% ...

This is a tuned model-parameter fraction, not a reported population fraction/incidence observable. The T14 pin requires zero `MISSING_QUALIFIER` findings and Lana §7.2 lists none, but Lana §4.3's numeric regex would match this text. That is a second prose-rule/pin inconsistency.

Proposed bounded resolution: scope the four-qualifier fraction/incidence gate away from typed `feedback_params` and `calibration_target` roles. Keep it active for result/emergent/observable prose where tracer/selection/denominator/redshift semantics apply.

## Current result

- Expected and observed: C2 sentinel 1; C4 S2 Result-cell 8; C7 integrity 1; all artifact regressions absent.
- Expected C6: six unlabeled comparisons, zero missing qualifiers.
- Observed C6: five unlabeled comparisons, one missing qualifier.

No sealed file changed, no test assertion changed, and no live/network/browser/git/DB/deploy/dashboard action occurred.

Request Hwao adjudication and Lana countersign for the two bounded rule clarifications. If approved, Tori will patch only the C6 role-aware detector and rerun the unchanged tests.

TORI_C1R_T14_DEVIATION_STOP_20260713T010203Z
