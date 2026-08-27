# DRAFTING BRIEF — write §6, the blinding covenant. You are the author this time.

You have refereed this document four times. This asks you to write one section of it instead.

## Why the roles are inverted

§6 has been rewritten four times by me and every rewrite introduced a contradiction with a
clause elsewhere in a 650-line document. Blocker counts by round: **6, 4, 3, 12.** The last
round's newest defects were all mine, made while repairing the round before. Two were found
independently by all three seats. My defect-introduction rate in this prose now exceeds my
repair rate, so another attempt by me is the least promising option available.

**You draft. GPT56 and CODEX referee your draft. I review it before it enters the document.**
You will not referee your own text — that separation is the point, and if you find yourself
wanting to argue a choice rather than state it, that is the signal to write the alternative
down instead.

## What §6 must do

The study measures the spin handedness of 65,060 galaxies to test whether a claimed four-percent
directional lean exists. Its entire licence rests on nobody knowing the outcome while decisions
that could shape the outcome remain open. §6 is the clause that makes that true and checkable.

## The requirements, drawn from your own findings across four rounds

1. **Ban access, not merely disclosure** (unanimous, round 1). "Not published" is an embargo. A
   person must not be able to comply while opening, querying, rendering or computing inside the
   sealed store.
2. **The ban must not be role-scoped** (KIMI-V12 F3). V12 banned four powerful roles and granted
   read access to named key holders, so a holder outside those roles could read pre-lock,
   authorised and merely logged.
3. **The exceptions must exist and must not be voided by the ban** (KIMI-V14 F1, GPT56-V14 4,
   CODEX-V14 3 — all three of you, and the reason this brief exists). Some pre-lock access is
   mandatory: the instrument that writes χ, the cutout producer, the Stage-C runner, the
   acceptance-ledger recompute, **the calibration computation** (CODEX-V14 4 says I omitted it),
   and the hand-check committee, which must view χ-bearing cutouts to produce BS-8f's labels. My
   V14 authorised these and then voided the run on "any pre-lock access, authorised or not", so
   the committee voided the run it exists to enable.
4. **The lock must be executable and receiptable** (GPT56-V14 2/3, CODEX-V14 1/2). BS-L was
   defined as the moment every class-P slot holds a receipt — and then made a class-P slot, so it
   certifies a set containing itself. The verdict receipt BS-V must not double as the lock, and
   the sequence BS-5f → lock → unblinding must be recordable through a named producer.
5. **The automation set must be complete and each member identified** by the pinned code symbol
   that implements it (CODEX-V14 4).
6. **Every actor is enumerated**, including the hand-check committee, its sealed store, its
   isolation from other roles, and where its χ-derived labels live.
7. **Violation must be detectable, not merely forbidden.** An append-only log, receipted, whose
   absence is itself a failure.

## How to write it so it can be checked

Prose defeated me because clauses have to be mutually consistent and nothing verifies that.
**Write §6 as a lifecycle**: a table or state machine over (actor or process) × (what it may
touch) × (when, relative to BS-5f / lock / unblinding) × (under which receipt) × (what voids the
run). Anything not in the table is forbidden by default, so completeness is checkable by reading
one column rather than by cross-referencing paragraphs.

Prose may surround the table. **The table is the normative object.**

## Deliverable

Write `SECTION6_DRAFT_KIMI.md` in this directory containing:

- the complete replacement §6, ready to drop into the document, self-contained;
- a short statement of every choice you made where the requirements did not force one, and what
  the alternative was;
- **the residual risks your own draft carries** — the things it does not close, named as plainly
  as you have named mine.

Do not modify the preregistration itself. `../PREREG_SUCCESSOR_DRAFT_V14_20260827.md` is the
current text; §7's slot table tells you which receipts exist and what blocks what. Your four
reports and the other seats' are on disk.

Do not read `/Users/duhokim/NebulaMindData/`.

One instruction I want to be explicit about: **if a requirement above is wrong, say so and do
not implement it.** Four rounds of your findings are the input to this brief, but I assembled
them, and assembling them is exactly the operation I keep getting wrong.
