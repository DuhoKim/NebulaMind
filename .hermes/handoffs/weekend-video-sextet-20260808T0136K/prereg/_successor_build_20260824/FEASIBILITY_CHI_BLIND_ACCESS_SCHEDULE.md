**STATUS: FEASIBILITY REPORT — for the principal, via Blanc. Not a choice between A and B.** Asked at
22:24 KST: is a totally precommitted χ-blind access schedule **compatible with how Rows D and G are
actually meant to operate?** **Short answer: yes for both — and for Row G the accepted hand-check
protocol ALREADY REQUIRES ONE.**

# Is a precommitted χ-blind access schedule workable for the rows that read χ?

## First, which rows this is actually about

Four rows can reach χ-bearing bytes. **Two are already schedule-constrained and are not at issue:**
**Row C2** reads cutouts *"via row B and **fixed parent lists**"*, and **Row I** reads the sealed label
set and the instrument outputs *corresponding to it* — its read set is the **sealed allocation**, fixed
at BS-2f from χ-free inputs. **Both are already determined by an object fixed before any χ is read.**

**The live subjects are Row D and Row G**, exactly as the seats found.

## Row D — the instrument runner. Compatible, and nothing in its purpose wants adaptivity

- **The universe is already fixed and χ-blind.** Row D reads the cutouts of the accepted sample. The
  acceptance ledger is computed by Row E from **predicate bits and catalogue-quality fields only**,
  and §2.7's predicates were fixed before any image byte.
- **Order is irrelevant to the result.** Inference is per-object and independent; no quantity the study
  computes depends on the sequence. A frozen permutation — canonical `(brickid, objid)` order, or a
  seeded shuffle pinned at freeze — is available at no cost.
- **Multiplicity is already one per object**, and `require_complete_sample()` refuses a partial run
  outright: *"a partial run is not a smaller run, it is a different experiment."*
- **Retries are the only real specification work**, and they are not χ-conditioned: a transient read
  failure is a fact about storage, so *"attempt each object exactly k times in place; the k-th failure
  is terminal and recorded"* is both fixable in advance and honest.
- **Stopping is the manifest being exhausted.** There is no early-stop condition to preregister.

**Cost of A for Row D: essentially none, and the timing is favourable — the runner is not built.**
BS-3 is not yet delivered, so the constraint is something to build *to* rather than to retrofit.

## Row G — the hand check. Compatible, and this is the part that changes the question

**HC-1H — the accepted protocol, `HC1H_ACCEPTANCE_20260815.md`, authorised 2026-08-15 — replaced
HC-1…HC-6 with: one human checker, 850 blinded labels — 500 real, 200 blind synthetic ground-truth
injections, 150 mirrored re-presentations.**

**A design with injected synthetics and mirrored re-presentations cannot work unless the presentation
sequence is fixed by the design rather than by the subject.** If the checker chooses what to view next:
the 200 synthetic injections stop being blind, because a subject who controls the sequence can notice
what is being slipped in; and the 150 mirrored re-presentations stop measuring self-consistency,
because the subject selects which items get re-shown. **The blinding and the self-consistency
measurement both depend on the schedule being precommitted.**

**So option A does not impose a new constraint on Row G. It writes down a constraint HC-1H's design
already presumes.** It is unenforced in this text only because *"V3-pred's HC-1H measurement and
validity rules (committee, sealed keys, HC-5, HC-6) are carried **by quotation at freeze**"* — they are
inherited, not yet quoted, and therefore not yet in force where Row B could enforce them.

### The workable shape for a human, stated precisely

**Fixed next item; free dwell.** The checker may look at the current cutout for as long as they like
and re-display it as often as they like; **they may not choose which object comes next.** This
preserves everything a careful human review needs — time, re-examination, second looks — and removes
exactly the channel, because **the leak is in which object is requested next, not in how long one is
viewed.**

### The one thing A genuinely costs, and it should not be glossed

**Selective revisiting.** *"Come back to the hard ones at the end"* is adaptive by construction: the
decision to revisit object X after seeing Y and Z depends on their content. **A full second pass in a
fixed order is compatible; a chosen revisit is not.** If HC-1H's own rules require selective revisit,
that is a genuine conflict — **and I cannot rule it out from this text**, because HC-1H's full rules
are carried by quotation and have not been quoted yet. **Reading them is the one open piece of this
answer.**

## A discrepancy I found while checking, flagged and NOT resolved

**Row G is written as a committee; HC-1H is one human checker, and that checker is Duho.**

Row G's cells say *"Hand-check committee"*, *"the member co-signatures carried by the label-set
receipt"*, and void the run on *"a member holding any other role"*. **HC-1H — the protocol that
replaced HC-1…HC-6 — specifies one human checker (Duho).** If Row G's checker is Duho, **he also holds
Row L** (signs the freeze at P0, signs BS-L at P6, opens the lock at P7), and **Row G's own
other-role clause fires against him.**

**Either Row G was written against the superseded committee design, or the exclusivity clause cannot
mean what it says.** This is independent of the χ channel and it has to be answered before Row G can
be conducted either way. **I am not resolving it — it changes what the conduct table permits.**

## What I am not doing

**I am not choosing between A and B.** This reports feasibility only. What the report does establish is
that **the "A is unworkable for Row G" branch does not appear to be live**: the accepted hand-check
protocol already needs a precommitted presentation sequence, so A is closer to enforcing HC-1H than to
overriding it. **Whether that makes A preferable to B is not mine.**

**CODEX's sentence belongs in the repair whichever way it goes:** *a sign-blind exclusion rule is not a
substitute for a sign-blind access schedule.* **The inheritance §2.7(3) was carrying — χ-blindness of
the exclusion predicates — never reached the access schedule, and that gap is the defect.**
