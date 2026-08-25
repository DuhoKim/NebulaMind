# REFEREE BRIEF — successor preregistration V9 (round 8)

You are a referee for a preregistered astronomy study. Your task is the ordinary one for a
methods referee: read the preregistration and its reference implementation, look for places
where a stated guarantee is not actually delivered, and recommend acceptance or revision.
Recommend revision if any guarantee fails. Rounds 1–7 all recommended revision, and every
round's findings were correct and were repaired.

Scientific context: the study tests Longo (2011)'s published spiral-galaxy handedness dipole
at his published axis, on a footprint chosen for statistical leverage. Its predecessor was
declined on 2026-08-25 because its footprint could not reach the preregistered power. This
document is a DRAFT: no run, no data acquisition beyond an already-completed catalog-count
step, and no freeze is authorized. If the text assumes an authorization it does not have,
report that.

## Verify the file digests first

Compute sha256 of all three and confirm before reading further:
- `../PREREG_SUCCESSOR_DRAFT_V9_20260825.md` =
  `b97ba35c8d1eeb66cc44e6915d2ae752fd19c374ff4906c9d15b8518056919b6`
- `../ref/successor_ref_v4.py` =
  `ffea5b6c58956c1f6c2e44939113f5170e459e566d132e8e3f69d117344e657b`
- `../ref/FIXTURES_V4_20260825.out` =
  `c5a4b95b554e16a7aea99213b06f21b18868e701c5a9682e8d3b325a18b10e72`
Any mismatch: stop and report it.

## Background reading (read-only)

`GATE_CODEX_SUCCESSOR_V8.md` (the round-7 referee report V9 responds to — its §10 trace says
which findings are repaired and which are explicitly left open);
`../real/REAL_GEOMETRY_RESULT_20260825.md` and the scripts in `../real/`;
`../../SUCCESSOR_SCOPE_20260821.md` including Amendment 1;
`../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`;
`../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`;
`../../VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md`.
Do not read `/Users/duhokim/NebulaMindData/`.

## Review dimensions

1. **Run the reference implementation.** `python3 ../ref/successor_ref_v4.py --fixtures` and
   compare with the pinned transcript; record your environment. Then judge the code as the
   document's operative definition: are there input regimes where a routine returns a result
   it should refuse, where a docstring and its body disagree, or where the prose promises a
   property the code does not enforce?
2. **The two round-7 repairs, checked directly.**
   (a) The cutout planner: V9 retires a reimplementation and binds to the frozen planner in
   the lane. Confirm the frozen planner returns the two historical neighbour bricks on the
   real survey-bricks table, that the retired routine can no longer produce a plan, and that
   the closure check would refuse a manifest missing either brick.
   (b) The selection: V9 reports 6,445 bricks after the frozen reduction. Reproduce it if you
   can, and judge whether the fast implementations used at production scale are adequately
   evidenced as equivalent to the frozen ones (40 and 30 random cases respectively).
3. **Guarantees that must hold end to end.** For each, trace whether the stated property can
   fail while every named check still reports success: manifest closure; sealed-input typing
   for Stage C and the production record; the ordering of the calibration decision relative to
   the real statistic; the power gate's self-confirmation; the count-oracle completeness
   proof; the release choice-point; the receipt schemas and whether receipts can be consumed
   by the routines that need them; the hand-check allocation floors and accuracy estimator.
4. **Statistical soundness.** The permutation variance identity; whether one measured null per
   prefix legitimately serves 1,000 trials; whether the 10× confirmation band can miss unsafe
   trials outside it; whether the reported Stage-P result supports the conclusion drawn.
5. **Fidelity of quotations** to the frozen predecessor and the photometric-cuts receipt,
   byte-level where an executable predicate is claimed.
6. **§10 lists six findings as still open and four as disclosed-not-closed.** Do not re-report
   those; check instead whether anything else is described as repaired that is not.

## Report

Write `GATE_<YOURSEAT>_SUCCESSOR_V9.md` in this directory — seat name per your dispatch line.
Include: the digests you computed; your environment; numbered findings with severity, the
quoted text or symbol at issue, why the guarantee fails, and the smallest sufficient repair;
and a final line that is exactly `**PASS**` (ready to freeze) or `**REVISE**` (with the
blocking findings named). Put any statement you cannot support with a shown command under a
heading `Testimony`.
