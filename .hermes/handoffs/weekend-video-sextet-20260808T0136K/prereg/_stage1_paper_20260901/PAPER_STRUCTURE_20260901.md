# STAGE-ONE PAPER — structure and honesty contract (Hwao's judgment; codex drafts)

**Order (Duho, direction #43):** "write up stage one as a paper."

## What this paper IS and IS NOT — settle it before a word is drafted

**IS:** a preregistered methodology and validation study. Its claim is about
*method*: that a galaxy-handedness measurement can be specified, frozen,
adversarially audited, and executed under cryptographic custody — and that the
sampling design, instrument identity, and robustness machinery pass their
prespecified tests.

**IS NOT — and the paper must say so in the abstract, not a footnote:**
- **Not a handedness detection.** No χ was measured. No galaxy image was
  analysed for science. γ̂ is unmeasured.
- **Not a cosmological result.** It makes no claim about parity violation,
  Longo's signal, or large-scale structure.
- **Not a completed pipeline.** The image-analysis half is designed but
  unexecuted, and the paper says exactly why it stopped.

The standing bar in this lab: assembling published values plus commentary is
not a study. So the paper must state clearly what is genuinely new — see §4.

## The structure

**1. Introduction.** The question (spiral handedness / parity), why it is
unusually vulnerable to analyst degrees of freedom (a sign convention error
flips the answer invisibly; a post-hoc cut can manufacture a dipole), and why
that makes it a natural test case for hard preregistration. State the paper's
actual contribution in the first paragraph.

**2. The preregistration and freeze.** The document, its adversarial
construction (author↔referee rounds to convergence), the freeze package (30
files, manifest digest, ed25519 signature, three independent verifications),
and the rule that made it binding: anything not derivable from frozen bytes
requires a new text. Include the known-debt appendix as an honest artifact —
a preregistration that lists what it could not close is more trustworthy than
one that claims completeness.

**3. Methods, in the order they were executed.**
- 3.1 Population and release choice (Branch B / DR10.1, the date-gated rule and
  its early resolution by disclosed ruling).
- 3.2 The sample: parent → quality cut → 49,211 objects, 6,104 bricks; the
  frozen traversal, plan and selection with their receipts.
- 3.3 Stage-P exact power: the design (every trial against its own
  20,000-permutation null, no shared reference null) and the frozen floor.
- 3.4 The instrument: identity pins, and the antisymmetry identity as the
  correctness criterion.
- 3.5 The robustness machinery: the gain-gradient counterfactual, the ratified
  γ grid, the mapping and its blind-committed conventions.
- 3.6 Custody: the chain, the mediator, the enumeration verifier, the
  five-gate discipline.

**4. Results — every number from a receipt, cited to its file.**
- Stage-P: prefix battery **984/1000**, final re-pass **996/1000** against the
  frozen floor 962.
- Instrument antisymmetry: **1000/1000** bit-exact identity, **1000/1000**
  byte-exact mirror involutions, max residual 0.0.
- Synthetic absolute-sign anchor: BATTERY-SIGN PASS; positive control
  REPRODUCED-LONGO.
- Machinery robustness: **5,049 evaluations** (99 draws × 51 γ), **zero verdict
  flips** against each draw's own γ=0 baseline — **with its scope stated: this
  is a machinery statement on fixture data, NOT `invariance_outcome = HELD`.**
- Custody: epoch opened, Row-A seal signed and independently verified; **two
  go-live attempts voided by post-hoc verification before anything consumed
  them** (unit error; key/shares divergence) — report these as evidence the
  discipline works, not as embarrassments to hide.
- The audit trail: N adversarial rounds, N findings, N repaired — count them
  from the gate records.

**5. The boundary — the paper's most useful section.** Why stage one stops
where it does: the frozen estimator needs a human-calibration term `a` that
requires ≥270 real labels across 9 strata × 3 bins; every route was costed and
closed (no checker available; panel 38 people minimum; Galaxy Zoo publishes
winding *tightness* not *direction*, and its one chirality release lacks
coverage, known-answer controls and an anchorable sign; loosening deletes
population coverage rather than adding noise). **State this as a finding with
its arithmetic, because it is genuinely useful to anyone attempting this
measurement.**

**6. Discussion.** What the preregistration machinery caught that ordinary
practice would not: the dependency cycle in the frozen text; the two voided
go-lives; the fixtures that passed for the wrong reason; the paraphrase-vs-quote
failures. Also the honest costs: the effort, the rigidity when a frozen
executable contradicted a ruling, and what we would do differently.

**7. Data and code availability.** The frozen package, its manifest and
signature, the pinned tools, the receipts.

## Drafting rules (non-negotiable)
- **Every number cites its receipt file.** No number from memory or from an
  earlier draft's prose — the standing lesson in this lane.
- **No claim beyond the receipts.** If a receipt says "machinery statement on
  fixture data", the paper says that, not "robustness demonstrated".
- **The halt is reported, not buried.**
- Refuse to draft any sentence you cannot source; list it as a gap instead.
