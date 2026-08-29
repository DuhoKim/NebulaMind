**STATUS: PROPOSAL — for the principal.** The refusal vocabulary rederived from scratch on his 20:30
ruling. **Nothing here is applied to the draft**; V59 is under review and the suspended set stands
until this is accepted.

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

## 3. The exhaustiveness argument — as a construction, since the last one failed

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
