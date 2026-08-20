# The K-8 crossing — what it is, and what it costs. For Duho's decision.

Hwao, 2026-08-20 evening. Nothing in this brief crosses anything; the inference runner being
built tonight is synthetics-only and REFUSES real tensors without an authorization file.

## What K-8 currently says (frozen text, V3 §preamble, verbatim)

> "no real-sky statistic has been computed anywhere in this program — no chirality label, no sky
> estimand, no unblinding of any kind, and no science cutout has been fetched."

Two of those four clauses are already spent, by your authorization and on the record: science
cutouts have been fetched (the transfer) and cut (2,047 tensors tonight). **The chirality-label
clause is still intact.** Running the frozen estimator over even one real cutout ends it.

## Why that matters: F-9

> "**F-9 One run.** Any parameter change after any real-sky statistic voids the run (K-8)."

So the crossing is a one-way door. After the first real χ, every parameter is locked forever:
the instrument, the input contract and its slots, the committee, the strata definition, the
hand-check design, the decision regions. Not "locked unless we find a good reason" — locked, or
the run is void and unpublishable.

## What is already frozen and gated (i.e. what we are betting is right)

| Piece | State |
|---|---|
| Estimator weights | frozen, `83008c1c…`, synthetic-only training |
| Input contract IC-1…IC-7 + slots | pinned by the R1–R5 rerun; identity witness 1000/1000 bit-identical |
| Cutout pipeline | gated end-to-end; 2,047 real tensors verified |
| Machine committee | gated; both members mirror-antisymmetric |
| HC-1H harness + strata definition | gated |
| Pilot size (150) | your decision, recorded |

I can find nothing still open that a later measurement would want to adjust. That is exactly why
the door is safe to walk through — but it is also exactly what everyone believes right before
they learn otherwise, so the question deserves your explicit yes rather than my inference.

## The one genuine subtlety: partial-sample stratification

The strata are committee-state × **|χ| tertile**. Tertile boundaries computed on a partial sample
(2,047 galaxies) would differ from the full 208,407. Recomputing them later is a parameter change
after a real-sky quantity — i.e. it would void the run.

**Therefore, if you authorize, the safe shape is:** compute per-object χ incrementally as cutouts
accumulate (measurement only, receipted, never aggregated), and compute the tertile boundaries
**once, on the complete sample**, after the last galaxy is cut. I will not let a partial tertile
be computed even as a diagnostic — because once it exists, someone can see it.

## Options

1. **Authorize now, with the partial-tertile prohibition above.** Inference runs behind the
   cutter; by the time the transfer finishes (~Tuesday) every χ exists, strata compute once, and
   your pilot can start immediately. Fastest path, door closes tonight.
2. **Wait until the sample is complete**, then run inference in one pass. Costs a day or two of
   wall-clock, buys nothing except a later door — the design is equally locked either way, since
   nothing is scheduled to change between now and Tuesday.
3. **Authorize a bounded rehearsal instead**: run the full chain on a small set of SYNTHETIC
   galaxies injected as if real, to prove the plumbing end-to-end without touching a real
   chirality label. This is free of K-8 and I would do it regardless — it is not really an
   alternative, it is a prerequisite I recommend either way.

**My recommendation: do option 3 tonight regardless, and choose between 1 and 2 when it passes.**
Between those, I lean to 1: waiting does not de-risk anything, and the pilot is the long pole.

Nothing proceeds on real χ without your word.
