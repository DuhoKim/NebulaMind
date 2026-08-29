# GATE BRIEF — B29, the miss-rate audit result

Fresh context, adversarial. **You are being asked to be the blinded reader I cannot be.**

`b28_missrate_draw.py` drew a sample and was committed (932250d2c) **before any paper was opened**,
seeded from a git sha already public. `b29_missrate_result.py` reports the result: **zero misses in
eleven**, giving a 95% upper bound of 6 of 31 unflagged papers, i.e. a miss rate under 19%.

## THE JUDGING RULE, fixed before reading

> Does the paper PROVE that no member of a specified class of models can satisfy a specified
> conjunction of conditions — refutable by exhibiting a counterexample, and NOT by any measurement?
> A paper that merely fails to predict is silent about what cannot happen and is not a no-go.

## THE ELEVEN, and my verdict on each — ALL "not an obstruction"

5, 7, 10, 24, 27, 36, 37, 40, 46, 49, 56. My one-line reasons are in `b29`'s docstring.

## ATTACK — this is the important part

1. **RE-JUDGE THE ELEVEN YOURSELF, against the rule above.** I knew every sampled paper was
   unflagged, so I am not blinded and may have unconsciously graded toward "no". **Read them and
   tell me if any one is an obstruction.** A single miss changes the result qualitatively.
   Pay closest attention to:
   - **entry 49** (Blau, Guendelman & Guth 1987) — this literature contains a well-known result
     that a universe cannot be created in the lab without an initial singularity. **Is that result
     in THIS paper?** I judged it a dynamical taxonomy and may have missed a theorem.
   - **entry 40** — "gravitational repulsion of torsion PREVENTS a singularity". Is preventing a
     singularity for a class of collapsing fluids a no-go, or a constructive existence result?
     I ruled constructive.
   - **entry 56** — argues infinite-extent ΛCDM needs dark energy. Is that a class-wide
     impossibility argument or a motivating critique? I ruled the latter.
2. **Is the frame right?** 31 unflagged readable papers, from a list that was itself refuted twice
   and rebuilt. If the frame is wrong the bound is wrong.
3. **Is the hypergeometric bound correctly computed and correctly stated?** Check the arithmetic and
   whether "at most 6 of 31 at 95%" is the right reading of it.
4. **Does b29 overclaim or underclaim?** It says the result excludes a gross failure and leaves a
   moderate one open, and that a clean sample must not be read as "recall is fine". Is that the
   right weight, or is it hedging away a real finding?
5. **The free observation.** b29 notes that ten of eleven random papers are constructive and none
   proves anything impossible, and suggests the tier has one member because the literature has
   about one such paper. Is that supported, or a story?
6. Predicate audit.

## VERDICT

First line one token: `MISSRATE_CONFIRMED` / `MISSRATE_REFUTED_<what>` / `MISSRATE_NARROWED_<what>`.
Write to `<C or A>GATE_B29_VERDICT.md` here. **State explicitly whether you re-read the eleven.**
