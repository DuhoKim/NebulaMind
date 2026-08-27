# DRAFTING BRIEF — BS-2a, the acceptance design. It must exist before any image byte.

## What this decides

A study will measure the spin handedness of 65,060 galaxies. Some measurements will fail: a
cutout missing, an instrument returning nothing, a confidence too low. **Which measurements
count** decides the sample, the geometry, and therefore the answer.

Two referees found independently that the preregistration closes the *vocabulary* of exclusion
reasons without binding the *truth* of one. As CODEX put it: a conforming operator can mark an
unwanted object `EXCLUDED / confidence below threshold`, mark a wanted one `ACCEPTED`, and
satisfy the partition, the closed reason list and both digests. That choice is exercised **after**
image inference exists, so it moves both the signs and the geometry.

BS-2a is the slot that closes it. It is a DESIGN slot: text **and** code, gated **before the
first image byte**. Nothing about it may be settled once measurements exist, because by then
every choice is outcome-adjacent.

## Read first

- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` §2.7 — the current rule, and §7's BS-2a row.
- `PREREG_TEXT_V11_CODEX.md` finding 3 and `PREREG_TEXT_V11_GPT56.md` F3 — the original finding,
  in full, with their prescribed repairs.
- `../ref/successor_ref_v9.py` — the frozen code. `run_production_verdict()` currently accepts
  caller-supplied accept flags; `require_complete_sample()` currently compares two integers.
  **Neither implements this.** That gap is the work.

Read the reports yourself. My summary above is a summary, and summarising findings is the
operation that keeps going wrong in this lane.

## What BS-2a must specify

1. **The partition.** All 65,060 parent object IDs end in exactly one terminal status, ACCEPTED
   or EXCLUDED, no remainder, no duplicates, accounted once each.
2. **The evidence.** For each object: expected cutout checksum and tensor shape, actual checksum
   and shape, the instrument execution receipt, a finite-output flag, and the confidence value.
   Name the fields and their types.
3. **The predicates.** Each exclusion reason as a function of that evidence alone. The current
   closed list is: cutout missing or failing byte-integrity; incomplete at the frozen tensor
   shape; non-finite or absent instrument output; confidence below threshold. Say whether that
   list is right.
4. **Recomputation, not labels.** The contract by which production recomputes every predicate
   from the evidence and refuses any status, reason or evidence that disagrees. Name the function,
   its inputs, and what it raises.
5. **The confidence quantity** — defined, not merely thresholded. Which field, produced by what,
   on what scale. **And the threshold's single home**: referees found it in two places at once
   (BS-3 and BS-2a). Pick one and say which.
6. **Sign-blindness by construction.** Show that no predicate can read handedness, its sign, its
   amplitude, or the object's position relative to the tested axis. "Shown", not "asserted" —
   and note that one referee has already found a related contradiction elsewhere, where a
   recompute was declared sign-blind while authorised to read receipts carrying signs.
7. **Fixtures.** What tests would demonstrate each of the above on synthetic evidence.

## The rule about verdicts

For each requirement, **REPAIR or REFUSE, never a bare "Accepted"**. REPAIR means naming the
artifact, its fields, its producer, its verifier and what fails if it is absent. REFUSE means the
requirement is wrong or cannot be satisfied yet, with what would have to exist first.

A drafter on the §6 work refused a requirement of mine — every automation row carrying a pinned
code symbol that does not yet exist — and was right to; I would have fabricated the pin. Another
accepted all nine findings and three of the acceptances turned out to be renamings. **A refusal
with a reason is worth more than an acceptance without a mechanism.**

## Deliverable

`BS2A_DESIGN_DRAFT_GPT.md`, with: the replacement §2.7 text ready to drop in; the code contract
in enough detail to implement without further decisions; the conforming edits required elsewhere
in the document; every choice the requirements did not force with its rejected alternative; and
the residual risks your own design carries.

Do not modify the preregistration or the frozen code. Do not read `/Users/duhokim/NebulaMindData/`.
Other seats will referee this; you will not referee it yourself.
