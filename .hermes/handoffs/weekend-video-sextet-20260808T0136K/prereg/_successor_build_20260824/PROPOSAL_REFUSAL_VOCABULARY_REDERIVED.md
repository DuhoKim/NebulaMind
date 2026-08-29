**STATUS: RULED — 2026-08-29 22:18 KST. NON-CLOSURE IS ESTABLISHED AND THE CATCH-ALL IS TAKEN. The
no-catch-all decision of 19:52 is FORMALLY REVERSED, not merely suspended.** §3's exhaustiveness
argument below is **REFUTED and kept as the record of the second failure** — read it as the evidence
for the ruling, never as a live claim. **Three defects the ruling does NOT close are listed at the end
and must not be absorbed by the catch-all.**

# The refusal vocabulary, rederived — and the principle that failed had to be rebuilt first

**The first derivation missed a class, not a member.** It enumerated from *authorisation* structure
and forgot that a mediator also fails for reasons that are nobody's fault. Patching in a ninth code
would have repaired the instance and left the method that produced it. So this starts from the
principle.

## 1. The old principle was too strong AND too weak, and both showed up in one round

**Old:** *a reason may describe the request and the authorisation state, never the object.*

**Too weak** — CODEX-V56 F4: request-shaped codes can still reveal object membership.
`REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` is phrased as authorisation and **is** an object fact; the
refusal itself announces that a named identity sits outside a set.

**Too strong** — GPT56-V56 F2: an unreadable cutout is a refusal the mediator must log, and
*"unreadable"* is unavoidably about an object. A principle forbidding all object description makes the
availability axis unloggable, which is exactly the hole that voided a run.

**The two failures are one failure.** "Object" was the wrong axis. The thing that must never leak is
not *the object* but **anything derived from its content**.

## 2. The rebuilt principle, stated as a test that can be applied to a candidate code

> **A refusal reason may describe the request, the authorisation state, and the object's STORAGE
> STATE. It may never describe anything derived from the object's CONTENT.**
>
> **The operational test: can this code be emitted without the instrument ever having read the
> object's bytes as data?** If yes, it is admissible. If emitting it requires knowing something the
> instrument computed *from* the object, it is not.

`REFUSED-OBJECT-UNREADABLE` passes: storage failed, nothing was computed.
A hypothetical `REFUSED-LOW-CONFIDENCE` fails: emitting it requires the classifier's output.
**`REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` fails** — deciding it requires testing this identity
against a set, and the refusal publishes the answer.

**Safety condition, stated because the storage-state allowance depends on it:** availability refusals
are non-leaking **only while the set of objects read is fixed χ-blind**. §2.7(3) already requires every
exclusion predicate to be sign-blind by construction; **this vocabulary inherits that requirement, and
if it ever fails, the availability codes become a χ-derived channel.** That dependency is the price of
admitting the axis at all, and it should be visible rather than buried.

## 3. The exhaustiveness argument — REFUTED 2026-08-29 22:14, and this is why the catch-all was taken

**Both seats broke this within five minutes of being asked to, with different countercases, both
against the actual conduct table rather than against a general theory.**

- **CODEX — an ESCAPE.** *"Permitted"* is not binary because it can be **undecided**. Row B must
  verify Row D's authenticated stage-completion artefact before proceeding, and that verifier can time
  out, deadlock or lose its process **before returning a verdict**. The access has not completed and it
  was adjudicated neither permitted nor refused — Axis A needs the former, Axis B the latter, and the
  case escapes both. In its words: *"Calling permission binary does not make an unevaluated predicate
  true or false."*
- **GPT56 — an OVERLAP.** Field-constrained writes need permission facts learned **during** the
  transfer, so the pre-attempt split is not a split.
- **And the miss was self-inflicted.** The draft's line 588 — the instruction this derivation was
  written against — lists the mediator failures to cover and names **"timed out"** explicitly. **The
  word does not appear once in what I wrote.** I omitted a class the requirement named.

**Two independent derivations have now been broken within an hour of being written. That is the
finding, and it is what the principal ruled on: if closure cannot be shown, the escape hatch stops
being a concession and becomes the honest answer — and a routine verifier timeout stops voiding the
study.**

**The sequence is why the ruling holds, and it belongs in the record.** The catch-all was decided
**after** this argument was attacked, not against it. Had it been decided against an argument that had
only been written, it would have collapsed exactly as the first one did and we would have found out in
the next round. **Gating the ruling on the round is the whole reason the answer is durable.**

## 3a. The construction as written — REFUTED, retained verbatim below as the record

A Row B refusal occurs when a requested access **does not complete**. Exactly one of:

- **(A) the access was not permitted** — the authorisation axis;
- **(B) the access was permitted and could not be completed** — the availability axis.

**These are exhaustive because "permitted" is binary and evaluated before the attempt.** There is no
third state: an access is either refused by the permission check or attempted, and an attempt either
completes or fails. **This is the argument to attack** — the previous one failed by enumerating one
branch and forgetting the other existed, so the shape to test is whether some refusal escapes *both*.

**Axis A decomposes by what the permission check consults**, and it consults exactly: who is asking,
what they are asking to do, what must already exist, when it is, and whether the lock/ceremony state
allows it.

**Axis B decomposes by how an attempted transfer fails**: the bytes are not there, cannot be read, are
incomplete, or do not match their pinned digest.

## 4. The proposed set — nine codes, two axes

**Axis A — authorisation (5):**
`REFUSED-ROW-NOT-AUTHORISED` · `REFUSED-OUTSIDE-STATED-SURFACE` · `REFUSED-PRECONDITION-UNVERIFIED` ·
`REFUSED-PHASE-NOT-REACHED` · `REFUSED-LOCK-OR-CEREMONY-STATE`

**Axis B — availability and mediator behaviour (4):**
`REFUSED-OBJECT-ABSENT` · `REFUSED-OBJECT-UNREADABLE` · `REFUSED-OBJECT-INCOMPLETE` ·
`REFUSED-INTEGRITY-MISMATCH`

**Changes from the suspended set, each with its reason:**

- **`REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` is GONE**, not reworded. An identity outside the
  permitted set **is** outside the row's stated surface, so `REFUSED-OUTSIDE-STATED-SURFACE` already
  covers it **without publishing the membership answer**. The code was not merely badly phrased; it
  was redundant *and* leaking.
- **`REFUSED-LOCK-NOT-OPEN` and `REFUSED-CEREMONY-CONSUMED` merge** into
  `REFUSED-LOCK-OR-CEREMONY-STATE`. Both are one thing — the ceremony state does not permit this —
  and splitting them let the code name *which* state, which is finer than the refusal needs.
- **`REFUSED-SCHEMA-NONCONFORMING` is GONE from this vocabulary.** It is not an access refusal; it is
  a receipt-construction refusal, and V59 assigns that to `receipt_strict()`. **Keeping it here put one
  fact in two places.**
- **Four availability codes are new** — the class the first derivation missed entirely.

**Every one of the nine passes the §2 test:** none can be emitted only by knowing something computed
from the object's content.

## 5. What I am NOT deciding

**The catch-all question returns to the principal**, as ruled — it was suspended, not carried
forward. **I have no recommendation to repeat here:** my last one rested on a closure argument that
failed, and the argument above has not yet survived a round. **Ask the seats to break §3 first**, then
decide the catch-all against a derivation that has been attacked rather than one that has only been
written.

**Also not decided:** whether `REFUSED-INTEGRITY-MISMATCH` should instead be a VOID antecedent. A
digest mismatch on a sealed object may be tampering rather than a storage fault, and §5 already voids
on digest deviation. **I have left it as a refusal and flagged the overlap rather than resolving it**,
because getting that wrong in the VOID direction is how the option-C concern arose.


---

# THE RULING APPLIED — 2026-08-29 22:18 KST

## The catch-all, and the guard that has to come with it

**`REFUSED-UNCLASSIFIED` is added, and it carries A CODE AND NOTHING ELSE** — no free text, no
appended detail, no incident pointer inside the field. The whole reason a closed vocabulary was wanted
is that a refusal must not describe the object, and a catch-all with room for explanation is free text
with extra steps.

**Its use is a DEFECT TO BE ENUMERATED AT FREEZE, NOT A ROUTINE OUTCOME.** I warned when proposing a
catch-all that it will attract every refusal nobody wants to classify, and that warning is now the
guard: **the count of `REFUSED-UNCLASSIFIED` emissions is reviewed at freeze, and each one is a defect
to be named or explained.** A catch-all whose count is never reviewed **becomes** the vocabulary — that
is the failure mode, stated so it can be checked rather than hoped against.

## The set as it now stands — eleven codes

**Axis A — authorisation (5):** `REFUSED-ROW-NOT-AUTHORISED` · `REFUSED-OUTSIDE-STATED-SURFACE` ·
`REFUSED-PRECONDITION-UNVERIFIED` · `REFUSED-PHASE-NOT-REACHED` · `REFUSED-LOCK-OR-CEREMONY-STATE`

**Axis B — availability (4):** `REFUSED-OBJECT-ABSENT` · `REFUSED-OBJECT-UNREADABLE` ·
`REFUSED-OBJECT-INCOMPLETE` · `REFUSED-INTEGRITY-MISMATCH` *(flagged — see below)*

**Returned (1):** **`REFUSED-SCHEMA-NONCONFORMING` COMES BACK.** Structural change 3 is defeated:
Rows C2 and H write **non-slot, field-constrained objects through Row B**, and V62 scoped
`receipt_strict()` to producers of **slot** receipts only — so moving the code there does not classify
the mediator's refusal of those writes. **My own scoping repair removed the basis for the deletion**,
and the code has to come back rather than leave a real class of writes with no home.

**Catch-all (1):** `REFUSED-UNCLASSIFIED`, under the guard above.

## What the ruling does NOT close — three live defects

1. **Permission is not made total and durable before fallible processing** (CODEX F1). The repair is a
   **covenant** fix, not a vocabulary fix: an explicit request state machine with a fixed terminal
   treatment for **timeout and crash in each state**, and a durable log boundary. **The catch-all makes
   the failure loggable; it does not make the permission decided.**
2. **"Permitted before the attempt" is false for writes** (GPT56 F1). On Rows C2 and H, whether a write
   is within the stated surface **cannot be known until Row B decodes the payload**.
3. **`REFUSED-INTEGRITY-MISMATCH` stays flagged and UNRESOLVED.** Both seats: a digest mismatch cannot
   be adjudicated at emission — storage fault and tampering are indistinguishable there — and CODEX
   adds that the same observable event is already claimed by the **phase-Any digest-deviation VOID
   antecedent**. **A third open item, not a settled one.**

## One tension I am flagging rather than deciding

**A routine verifier timeout is foreseeable, and the guard above defines the catch-all as a defect.**
Routing a foreseeable class into a category whose count is reviewed as defects is in tension with
itself. **The clean answer is probably a named pre-decision state rather than a catch-all entry** — but
adding a code is close to the "not a ninth code" instruction and it is not mine to decide, so it is
recorded here and goes with the covenant repair when that is designed.

## Not part of the vocabulary, and not waiting on it

**The χ-adaptive access leak** — both seats found Rows D and G permit χ-adaptive access patterns, so
the χ-blind condition the availability axis depends on **is not paid under the current draft**, and
availability refusals become a χ-derived channel **whichever vocabulary is adopted**. **That is a leak,
not a taxonomy problem.** It has its own file: `OPEN_QUESTION_CHI_ADAPTIVE_ACCESS_LEAK.md`.
