# GATE BRIEF — B36, census batch 4 (entries 39, 21, 11)

Fresh context, adversarial. `b36_census_batch4.py` (4/4). Re-read all three against the
preregistered rule (b28); default to disagreeing — my solo miss rate measured 2-of-11 in B29.

> Does the paper PROVE that no member of a specified class of models can satisfy a specified
> conjunction of conditions — refutable by counterexample in that domain, not by measurement?

Sources: 39 → `../bhu-reading-20260823/sources/1105.6127_clean.txt`;
21 → `.../2203.13295_clean.txt`;
11 → `../reviews/bhu-citation-custody-evidence-20260811/arxiv-1410.3881v2.txt`.

## MY VERDICTS — all three NOT-OBSTRUCTION
39: constructive torsion-bounce family (as 10/40/12). 21: strongest hit is an internal stability
theorem ("radial perturbations cannot develop unstable radial modes"); operative contribution is
the detectable-universe construction. 11: constructive family, closes with "may create".

## ATTACK
1. **The draw, this time.** `b35_draw_batch4.py` was committed at a038e197b BEFORE the reads.
   Re-run it. Does it reproduce {39, 21, 11}? Is the pool ordering stated and honoured? Anything
   still unverifiable?
2. **Entry 21's stability theorem.** Is "cannot develop unstable radial modes" really internal, or
   does it exclude a class? Check the derivation around Eqs. 105–108 and its stated domain.
3. **Entry 39 vs its family.** Its claim that a classical bounce pre-empts a quantum bounce —
   mechanism comparison, or a no-go against quantum-bounce models?
4. Predicate audit.

## VERDICT
One token: `BATCH4_CONFIRMED` / `BATCH4_REFUTED_<what>` / `BATCH4_NARROWED_<what>`.
Write to `<C or A>GATE_B36_VERDICT.md` here. State which papers you read in full.
