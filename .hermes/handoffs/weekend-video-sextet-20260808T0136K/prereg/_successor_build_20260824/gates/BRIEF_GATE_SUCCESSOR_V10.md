# REFEREE BRIEF — successor preregistration V10 (round 9)

You are a referee for a preregistered astronomy study. Your task is the ordinary one for a
methods referee: read the preregistration and its reference implementation, look for places
where a stated guarantee is not actually delivered, and recommend acceptance or revision.
Recommend revision if any guarantee fails. Rounds 1–8 all recommended revision, and every
round's findings were correct and were repaired.

Scientific context: the study tests Longo (2011)'s published spiral-galaxy handedness dipole
at his published axis, on a footprint chosen for statistical leverage. Its predecessor was
declined on 2026-08-25 because its footprint could not reach the preregistered power. This
document is a DRAFT: no run, no data acquisition beyond an already-completed catalog-count
step, and no freeze is authorized. If the text assumes an authorization it does not have,
report that.

## Verify the file digests first

Compute sha256 of all three and confirm before reading further:
- `../PREREG_SUCCESSOR_DRAFT_V10_20260825.md` =
  `cca636b9444c4f5a1df47aaddf419443caa27350adfbdbfd5c3ba31065ea39c7`
- `../ref/successor_ref_v4.py` =
  `0b312c96db0b4551bcafd554b4bdd7124d3104cef4cc7f405eea3f849e08e21c`
- `../ref/FIXTURES_V4_20260825.out` =
  `6b14d8a69b606cbf5ddb6d0e82f856a08d6a5928227c3cba4956a1c02636e436`
Any mismatch: stop and report it.

## Background reading (read-only)

`GATE_GPT56_SUCCESSOR_V9.md` and `GATE_CODEX_SUCCESSOR_V9.md` (the round-8 referee reports V10 responds to — its §10 trace says
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
   document's operative definition: input regimes where a routine returns a result it should
   refuse, docstrings that disagree with their bodies, properties the prose promises that the
   code does not enforce.
2. **The four round-8 repairs, each checked AT THE PRODUCTION PATH rather than at a fixture.**
   Your round-8 reports found a repair that lived only in a fixture while the production entry
   point kept the defect; that is the failure mode to look for again.
   (a) Does `close_manifest()` itself derive plans from the frozen planner, and does it refuse
   a manifest missing either historical neighbour when called end to end?
   (b) Is the swap-then-removal phase now equivalent to frozen `local_pass()`? Try to build a
   counterexample as you did before — different seeds, tie-dense values, wider brick counts,
   targets near the crossing. The claim is 400 cases in your prior regime with zero mismatches;
   test OUTSIDE that regime.
   (c) Does Stage P's widened audit bound the risk it claims, or can an unsafe success still be
   counted? Is measuring the reference null against a sample of trials' own nulls sufficient to
   call it conservative for all 1,000?
   (d) Can the count-oracle completeness proof still be satisfied without an independent
   witness?
3. **Guarantees that must hold end to end.** For each, trace whether the property can fail while
   every named check reports success: manifest closure; sealed-input typing; the ordering of the
   calibration decision relative to the real statistic; the power gate; the release
   choice-point; receipt schemas and whether receipts can be consumed by the routines that need
   them; hand-check allocation floors and the accuracy estimator.
4. **Statistical soundness.** The permutation variance identity; whether one measured null per
   prefix legitimately serves 1,000 trials; whether the reported Stage-P result supports the
   conclusion drawn, given it was measured pre-reduction and is explicitly not restated as
   re-run.
5. **Fidelity of quotations** to the frozen predecessor and the photometric-cuts receipt,
   byte-level where an executable predicate is claimed.
6. **§10 lists four items as disclosed-not-closed.** Do not re-report those; check instead
   whether anything else is described as repaired that is not.

## Report

Write `GATE_<YOURSEAT>_SUCCESSOR_V10.md` in this directory — seat name per your dispatch line.
Include: the digests you computed; your environment; numbered findings with severity, the
quoted text or symbol at issue, why the guarantee fails, and the smallest sufficient repair;
and a final line that is exactly `**PASS**` (ready to freeze) or `**REVISE**` (with the
blocking findings named). Put any statement you cannot support with a shown command under a
heading `Testimony`.
