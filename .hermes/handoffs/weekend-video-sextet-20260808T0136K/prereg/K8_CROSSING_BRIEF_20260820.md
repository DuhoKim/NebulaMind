# RETIRED (settled) — The K-8 crossing — what it is, and what it costs. For Duho's decision.

**RETIRED from the decision list 2026-08-25 (Blanc, on Duho's review): The decision this brief asked for was given the same evening: Duho authorized the crossing at 22:20 on 2026-08-20 and the first real measurement followed 52 minutes later, as the custody record documents. Decided and executed; kept as the briefing that preceded it.**


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

---

# ADDENDUM 2026-08-20 22:xx — the rehearsal ran, and it changes the recommendation

The synthetic end-to-end rehearsal completed (`_rehearsal_20260820/REHEARSAL_REPORT_20260820.md`).
It worked — and it found **eight interface faults plus two items that must be frozen BEFORE the
K-8 crossing, not after.** My earlier lean ("authorize now") is withdrawn until those two are
settled, because both are parameters, and a parameter chosen after the first real χ voids the run
under F-9.

## What worked

- χ recovers synthetic chirality at **94.8%** direct-sign accuracy, zero exact-zero χ.
- **Observed sign convention: χ > 0 ↔ BS-3 truth_sign +1 (direct).** This is a fact that must be
  written down and frozen now; a convention discovered later is a convention that can be flipped
  to taste, and the dipole's sign is the whole result.
- End-to-end cost **216 s per 1,000 objects** ⇒ the full 208,407 ≈ **12.5 hours** of compute.
- The HC-1H harness accepted a real-shaped 850-item campaign and produced a blinded session with
  a sealed key; zero labels were submitted (correctly — no human labelled anything).

## The two that must be frozen before crossing

1. **The Neyman prior estimator / smoothing rule (report finding 6).** The frozen allocator
   *refuses* when empirical per-stratum priors are exactly 0 or 1, because every information
   weight becomes zero. The rehearsal only proceeded by choosing Jeffreys smoothing
   `(correct+0.5)/(N_s+1)`. That choice is a parameter of the allocation. The report's own
   real-run implication, verbatim: *"Freeze the prior estimator/smoothing rule before production
   rather than selecting it after seeing synthetic outcomes."* Choosing it after real χ exists =
   voided run.
2. **The sparse-cell rule (report finding 1).** The floor of 30 per stratum was only satisfiable
   in rehearsal because the synthetic sample could be *engineered* (12,000 candidates screened
   down to 2,000 with ≥35 per cell). Verbatim: *"The real accepted population cannot be
   engineered this way; if any real cell has N_s<30, HC-1H is infeasible and must hold or receive
   a preregistered sparse-cell rule before any labels."* My projection from the natural draw says
   the smallest real cell should be ~834, so this is unlikely to bite — but "unlikely" is not a
   rule, and the rule cannot be written after we see the real populations.

## The six that are just engineering (fix, then re-gate; none touch K-8)

Environment split (torch venv lacks Pillow/astropy); inference CLI takes one `--inputs` argument
per tensor and will hit the argument-length ceiling at scale (needs a manifest/stdin mode);
committee has no batch entry point and does not load its own member-B weights; HC-1H needs
Pillow-readable images while inference consumes raw tensors (a rendering step must be specified,
not improvised); committee emits `AGREE_CONFIDENT` while HC-1H accepts `agree-confident` (a
bijection that should be frozen, not re-derived); HC-1H calls its 500-row input `real_population`
even for synthetic data (naming, but it invites exactly the wrong mistake).

## Revised recommendation

**Do not cross K-8 yet.** Sequence instead: (a) freeze the sign convention, the prior-smoothing
rule, and the sparse-cell rule as a small preregistration amendment, gated like every other;
(b) fix the six plumbing faults and re-gate; (c) then authorize real χ, incrementally, with the
partial-tertile prohibition from the original brief. That order costs a day and removes the two
ways this run could have been voided after the irreversible step.
