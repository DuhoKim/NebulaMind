# Task 27 — the verdict estimator LAPSES unbuilt, by decision

Hwao, 2026-08-22 23:38 KST. Duho, verbatim: *"let #27 lapse with the note."*

## What lapses

`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` called for F-3..F-7 — the dipole estimator at Longo's
axis, the 100,000-permutation null, the sigma chain, the four decision regions — to be built,
validated on synthetic skies, adversarially gated, and hash-frozen **before the sample completes**,
so the analysis could be shown to predate its data. The transfer completes ~Wednesday afternoon;
after that the provably-data-blind property is unobtainable forever. Nothing was built. The window
is being released, not missed.

## Why lapsing is the right call, not a failure to execute

The spec was written on the morning of 2026-08-21, hours **before** the footprint finding. What
two adversarial gates then established (`GATE_FOOTPRINT_GEOMETRY_20260821.md`,
`GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`, HOLD twice, refuted never):

- F-1's frozen `A_hat = 3 * D_hat` is exact only when `E[cos^2 theta] = 1/3`; on this footprint
  that moment is `0.475857`, so the frozen normalisation over-responds by 42.76%;
- no accepted subset of this parent reaches the preregistered 95% power at Longo's amplitude
  (SSE bound 4.4888 against a required 4.7351, at perfect labelling).

The spec mandates implementing the frozen protocol as frozen — building it now would freeze a
**known-mis-normalised instrument** for a run whose decline is the standing recommendation
(`DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`, Revision 6, awaiting signature). A frozen
artifact whose defect is already on the record protects nothing and would exist only to have
existed.

## What the successor takes instead

Not this code — the **requirements the spec got right**, which carry into the successor's own
preregistration (`SUCCESSOR_SCOPE_20260821.md` items 3-7): refuse-without-authorization gating on
the inference-runner pattern; refuse-unless-complete sample checks; the synthetic validation
battery (null must never yield REPRODUCED; the sign test at A = -0.0408; the below-floor test;
the N-1 power refusal). The successor's estimator is footprint-aware by design — normalisation as
a procedure over accepted positions, monopole projected out, sigma from the permutation variance —
and none of that is buildable honestly until the successor's selection exists.

## Effect

- Task 27 closes as **lapsed by decision**, this note is the record.
- No forward claim about any estimator exists anywhere: the decision memo already states "the
  verdict estimator does not exist" and makes none.
- The completion sequence is unchanged: `_dustin_list_20260822/completion_check.py` verifies
  custody and **stops before strata**, which remain Duho's open decision.
