# GATE BRIEF — B25, the screen's real precision

Fresh context, adversarial. `b25_screen_precision.py` (4/4). This is **evidence for Duho's one
remaining open question**, so an error here misleads a live decision. Question 1 asks whether the
THEORETICAL-OBSTRUCTION tier should be re-sorted by an automatic screen or only by hand.

Files: `b1_theoretical_obstruction_tier.py` (the screen), `b25_screen_precision.py`,
`../bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md`, sources in
`../bhu-reading-20260823/sources/`.

## THE CLAIMS

1. **b1's reported figure is stale.** It says "flags 4 of 29 sources and only 1 is correct". The
   pool is now **41**, and b1's own flagged list already prints **six** items while its check still
   says four — the code and its summary disagree.
2. **It is measured over the wrong population.** 14 of the 41 pinned files map to no corpus entry —
   they are measurement papers held as receipts (Planck, DESI, Carr). Three of the six flagged are
   receipts. Scoring a tier screen against papers it would never be run on counts them as its
   mistakes.
3. **Corrected: 1-in-3 over corpus entries**, versus 1-in-6 over everything. b1's "1-in-4" is
   neither.
4. **It does not rescue the screen.** 0.33 is still wrong more often than right; it flags entry 25
   (a BHU construction paper) and entry 6 (the CNS founding paper) alongside the one real no-go.

## ATTACK

1. **Is the flagged list right?** B25 hardcodes the six identifiers from b1's printed output rather
   than re-running b1's criterion. **If b1's criterion would flag a different set on the current
   41-source pool, every number here is wrong.** Re-run the criterion itself and report what it
   flags now.
2. **Is "corpus entries only" the right denominator?** 27 of 41 map to an entry via
   `ENTRY_SOURCE_MAP.md`, but that map has 32 rows and the bibliography has 51 BHU papers — so the
   mapped set is neither all sources nor all entries. **Is 1-in-3 measured over a coherent
   population, or a third arbitrary one?**
3. **Is the direction claim safe?** B25 says restricting the population *improves* precision. That
   is favourable to the screen and therefore to one side of Duho's decision. Check it is not an
   artefact of which files happen to be pinned.
4. **Does entry 6 or entry 25 have any case for being a no-go?** If either is arguably correct,
   precision rises again and the verdict shifts.
5. **Predicate audit**, and: is it honest for this file to say it "decides nothing" while producing
   the number the decision will turn on?

## VERDICT

First line one token: `PRECISION_CONFIRMED` / `PRECISION_REFUTED_<what>` / `PRECISION_NARROWED_<what>`.
Write to `<C or A>GATE_B25_VERDICT.md` here.
