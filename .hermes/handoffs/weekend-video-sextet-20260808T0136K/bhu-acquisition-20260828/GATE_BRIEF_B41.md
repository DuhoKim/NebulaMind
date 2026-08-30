# Gate brief — B41, the census coverage proof

**What is being claimed.** Duho ordered (2026-08-30, via Blanc): "read the unflagged remainder"
of the obstruction census. `b41_census_coverage.py` claims this directive is ALREADY DISCHARGED
by the existing batch artifacts, and proves it by set arithmetic: screen flags {6,22,25} +
the 11-paper preregistered sample (re-drawn from the committed seed) + 25 batch-read papers
= all 39 readable BHU papers, empty difference both directions. It further reports the final
numbers Duho asked for: remainder read = 25, paper-level obstructions in the readable corpus =
{22, 5} (parsed from Testability lines), screen miss rate 1 of 2 (missed entry 5), precision
1 of 3 flags.

**Your task: refute it.** This is the census CLOSER — if it survives, the lane reports the
census done. Attack the load-bearing joints:

1. **Binding-by-substring.** The batch sets are re-declared by hand and bound to their committed
   artifacts by exact substrings (e.g. "entries 8, 43, 55" in b33). Does any binding
   under-specify — could a batch artifact have actually adjudicated more or fewer papers than
   its bound fragment names? Read the batch artifacts (b33, b34, b36, b37, b38, b39 and their
   AGATE/CGATE verdicts) and check the sets against what was actually adjudicated.
2. **The flags' provenance.** {6,22,25} is frozen in b28 as "b1's flags, hand-checked". Where
   are the READS of entries 6 and 25 recorded? Trace each of the three to an artifact (a
   bibliography block note, a gate verdict, b25's convention dispute on 25). If any flag's
   adjudication is testimony with no artifact, say so — that is a hole in "all 39 adjudicated".
3. **Map-parse misattribution.** The live flag recomputation uses b25's stem→entry parse of
   ENTRY_SOURCE_MAP. Could a wrong mapping hide a flagged corpus paper as a receipt, or
   misnumber a flag? The check only asserts FROZEN ⊆ live.
4. **The miss-rate denominator.** Ground truth = paper-level THEORETICAL-OBSTRUCTION entries
   parsed from Testability lines: {22, 5}. Entries 37, 51, 52/53, 57, 38§4 carry CLAIM-level
   exclusions recorded in prose per the CGATE_B30 §5 convention and are excluded from the
   denominator. Is "miss rate 1 of 2" honest, or does the claim-level exclusion undercount
   what the screen was FOR? State what number you would print instead if you disagree.
5. **The discharge claim.** Is it honest to count b32's gate-reads (38, 57) as census reads,
   and to say Duho's "read the unflagged pile" is discharged by work that predates the order?
   The alternative reading is that he ordered a FRESH read. Rule on which reading the record
   supports (his ratified precedent is question 3's "then look harder with more entries").
6. **Predicate audit of `b41_census_coverage.py`** as usual: which checks compute the claim
   and which merely detect phrase presence.

**Verdict file:** write `<A|C>GATE_B41_VERDICT.md` in this directory. First line: a single
token verdict (e.g. `COVERAGE_CONFIRMED` / `COVERAGE_REFUTED_<REASON>`), then your reasoning.
Read the script and run it if you wish: `python3 b41_census_coverage.py` from this directory.
