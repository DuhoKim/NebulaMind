# BRIEF — one question, adversarially: does any Row B refusal escape BOTH axes?

**Subject:** `PROPOSAL_REFUSAL_VOCABULARY_REDERIVED.md`
**sha256 `b7096cb4f2524640f9192fe89161fcfa569b613d9c16089e1d74452ff1a4b2a6`**
**Scope: §3 primarily, §4's change list and §5's flagged overlap secondarily. Nothing else.**

**This is a narrow round and it is deliberately not a review of the vocabulary.** Do not tell me
whether the codes are well named, whether nine is the right number, or whether the set is good. **The
question is whether the exhaustiveness CONSTRUCTION holds.**

## Why this round exists, in one line

**The previous derivation was ruled on, and both seats broke its closure argument within the hour** —
it enumerated one branch and forgot the other existed. **The principal has ordered that this argument
be attacked before he decides anything against it.** Do to this construction what you did to the first.

## The construction you are attacking

§3 claims a Row B refusal occurs when a requested access does not complete, and that **exactly one** of
two things holds: **(A) the access was not permitted**, or **(B) the access was permitted and could not
be completed.** The claimed reason this is exhaustive: *"'permitted' is binary and evaluated before the
attempt."*

**Find a refusal that escapes both axes, or one that belongs to both.** Either breaks it.

### Attack 1 — the load-bearing step is the ordering, not the binariness

**"Permitted is binary AND evaluated BEFORE the attempt" is what makes the axes disjoint.** If a
permission decision can depend on something **only learned during the attempt**, the ordering fails
and the two axes overlap. Construct such a case against Row B's actual conduct table, or show that
none can exist. **A general argument that permission checks usually precede access is not an answer**
— the question is whether the covenant as written forbids the dependency.

### Attack 2 — the χ-blind dependency, which I surfaced and did not test

The proposal admits the availability axis on the ground that its refusals are **non-leaking only while
the set of objects read is fixed χ-blind**. I flagged that as the price of admitting the axis. **Test
whether the price is actually paid: does it hold under EVERY access pattern Row B permits, not just
the intended one?** An availability refusal on a set whose membership depends on anything χ-derived
publishes a fact about χ by which object it refuses on. **If some permitted pattern breaks it, say so
— that is a defect in the axis, not in the wording.**

### Attack 3 — `REFUSED-INTEGRITY-MISMATCH`, both readings, adjudicated not assumed

§5 leaves this flagged rather than resolved. **Both readings go to you and I want the overlap
adjudicated:** a digest mismatch on a sealed object may be an ordinary **storage fault** (a refusal),
or it may be **tampering** (and §5 already voids on digest deviation). **Say which, and on what
distinguishing evidence — or say that the two cannot be distinguished at the point the code is
emitted, which is itself the answer.** Do not assume the safe direction: getting this wrong toward
VOID is exactly how the earlier over-strict concern arose.

## The three structural changes — defended, not offered as tidying

**I would defend these hardest, so push on them rather than around them.**

1. **`REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` is GONE, not reworded**, because *"outside the permitted
   set"* already **is** *"outside the stated surface"*. It was redundant **and** leaking, and
   rewording would have kept a code that publishes a membership answer.
2. **Lock and ceremony merge** because splitting them named **which** state — finer than the refusal
   needs. **Finer than needed is the same defect as free text, in smaller units.**
3. **`REFUSED-SCHEMA-NONCONFORMING` leaves this vocabulary entirely** because it is a
   **receipt-construction** refusal, not an access refusal. Keeping it put one fact in two places, and
   V59 already assigns it to `receipt_strict()`.

**If you think any of the three is wrong, the argument to beat is the one stated beside it.**

## What does not move, whatever you find

**The suspended eight-code set stands. Nothing goes into the draft from this proposal. The catch-all
question stays open with the principal** — it is his, it is not being decided here, and I am not
re-recommending on it because my last recommendation rested on the argument that failed.

## Boundaries

**Read-only outside your own report.** A separate whole-document round is in flight on
`PREREG_SUCCESSOR_DRAFT_V63_20260829.md`; **do not modify that draft, `ref/successor_ref_v9.py`, or
any file other than your report.** v9 is FROZEN at
`6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.

## Report

Write to `gates/VOCAB_EXHAUSTIVENESS_<SEAT>.md`, `<SEAT>` being `GPT56` or `CODEX`. End with exactly
this block, marker at column 0:

    <!-- FINDINGS-BLOCK v1 -->
    SEAT: GPT56
    VERSION: VOCAB-R1
    VERDICT: CLEAR | NOT CLEAR
    COUNT: <n>
    F1 | HIGH|MEDIUM|LOW | REPAIR-REQUIRED|ADVISORY | <location> | <one-line summary>
    <!-- END FINDINGS-BLOCK -->

**`CLEAR` here means only one thing: you tried to break §3's construction and could not.** If you
found nothing, say what you tried — an unattacked argument that returns CLEAR is worth nothing to the
principal, and he is holding a decision on this.
