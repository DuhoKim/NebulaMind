**STATUS: RULED, THEN SUPERSEDED — not pending on the principal.** He ruled **option A** on it (eight
codes, closed, **no catch-all**), and then ruled that the derivation be **redone from scratch — "not a
ninth code"**, which **suspended option A without reaffirming or reversing it**. The live document is
**`PROPOSAL_REFUSAL_VOCABULARY_REDERIVED.md`**; this file is the superseded first derivation and is
kept because the rederivation is only checkable against what it replaced. **The suspended eight-code
set is still the operative language in the draft and the checker still enforces it** (GPT56-V59 F4,
CODEX-V59 F1) — that is a live finding against the draft, not an open question on him.

# The access log's refusal vocabulary, drafted

**GPT56-V49 F1 (HIGH):** §6.1 declares the non-χ-bearing classes a *closed list defined by schema* and
admits the BS-2k access log on its event schema — *"identities and flags, never payload bytes."* But
the **refusal-reason field is unconstrained** and is written per object, so a descriptive reason can
carry χ-derived information inside a class the document asserts is not χ-bearing.

Blanc withheld this from the principal deliberately: authorising *"constrain the vocabulary"* without
the vocabulary would repeat this morning's pattern, where option D was ruled and the real decision
turned out to be which sentences count as load-bearing.

## The principle the set has to satisfy

> **A refusal reason may describe the REQUEST and the AUTHORISATION STATE. It may never describe the
> OBJECT.**

That is what makes closure safe rather than merely tidy. Object identity is already its own field, so
the reason adds no per-object information; and no code below can encode a measured property, because
none of them refers to one. A reason like *"instrument confidence below threshold"* would be
χ-derived and is excluded by construction, not by discipline.

## The proposed closed set — eight codes, no free text

| code | fires when |
|---|---|
| `REFUSED-ROW-NOT-AUTHORISED` | the requesting row has no stated surface covering this operation at all |
| `REFUSED-OUTSIDE-STATED-SURFACE` | the row is authorised, but this read or write is not within its declared surface |
| `REFUSED-PRECONDITION-UNVERIFIED` | a required prior artifact is absent or fails its verifier — e.g. Row B refusing a Row D touch until the authenticated C2 exact-parent stage-completion artifact verifies |
| `REFUSED-PHASE-NOT-REACHED` | the operation is permitted only at a later phase (pre-unblinding access to a χ-bearing object) |
| `REFUSED-LOCK-NOT-OPEN` | no verified BS-L artifact, or no canonical opening authorization |
| `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` | the object identity is outside the set this row may touch |
| `REFUSED-SCHEMA-NONCONFORMING` | the requested write does not conform to the declared schema for its receipt class |
| `REFUSED-CEREMONY-CONSUMED` | the one-use unblinding ceremony identifier has already been consumed |

**The field carries exactly one code and nothing else.** No free text, no appended detail, no
formatted values.

## Why this set can be closed — and the condition under which it stops being closed

The same argument that let the raise-site enumeration carry a negative applies here. **Row B is the
only path to sealed bytes, and §6.1's row table is closed by Row R's default-forbidden clause.** A
refusal is therefore always one of: the requester is not a row with a surface here; the surface does
not cover this act; a stated precondition is unmet; the phase has not been reached; the lock is not
open; the identity is out of set; the write does not conform; the ceremony is spent. **The vocabulary
is closed because the row table is closed.**

**It stops being closed the moment the row table gains a row, a surface or a precondition.** So the
set is not a constant — it is *derived*, and any amendment to §6.1 requires regenerating it. That
should be stated wherever the set is pinned, or it will drift the way every other derived list here
has.

## The tension drafting revealed, which the principal should hear

**A closed set with no catch-all means an unanticipated refusal cannot be logged — and §6.1 makes an
unlogged refusal void the run.** An operator meeting a genuinely novel refusal would face mislabelling
or voiding. Three ways out, none free:

- **A. No catch-all.** Cleanest and most honest: if the set is genuinely derived from a closed table, a
  novel refusal means the table changed and the run's premises changed with it. *Cost:* unforgiving in
  exactly the situation where judgement is least reliable.
- **B. `REFUSED-UNCLASSIFIED`, code only, no text.** The fact is logged, the diagnosis is lost, and the
  hole does not reopen because the code carries nothing. *Cost:* it will attract every refusal nobody
  wants to classify — the third-category failure mode, again.
- **C. Catch-all plus an out-of-band incident record** outside the log, so the diagnosis survives
  without entering a class asserted to be non-χ-bearing. *Cost:* a second custody surface to govern,
  which is new normative machinery.

**My reading: A, with B available only if the principal judges a live run needs the escape hatch.**
The derivation argument is what makes A defensible; if it does not hold, then B and C are both
admissions that the set was never closed.

**Not my decision** — and the eight codes above are a draft for the principal to accept, amend or
reject, not a proposal I have applied anywhere. **No draft has been edited for this finding.**
