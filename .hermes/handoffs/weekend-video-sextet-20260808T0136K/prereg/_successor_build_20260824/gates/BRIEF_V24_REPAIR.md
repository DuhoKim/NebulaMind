# REPAIR BRIEF — V24. Two blockers, and stop writing two things that can be computed.

Base: `../PREREG_SUCCESSOR_DRAFT_V23_20260827.md`, sha256
`134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7`. **Verify before starting.**
Read `V23_WHOLE_REVIEW_GPT56.md` and `V23_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V24_20260827.md`.** Do not edit V23. **Do not touch V15–V22.**

## Credited — do not disturb

Both seats independently recounted §7, bounding the Class-E table before `### §7.1`, and confirm the
count repair is correct: **15 class P, 8 class E.** Both historical trace rows are repaired. CODEX
recomputed the whole V16→V23 predecessor banner chain — **every successor pin matches.** V23 remains
honest about being an unfinished programme.

## Blocker 1 — the coverage test is still self-referential (both seats, third round)

§7.1's registry exists, but the operative equality still compares the converter against a set the
converter effectively supplies. GPT56: *the antecedent registry is not independent of the converter.*
CODEX: *the operative coverage test remains self-referential.*

**Repair — make the independence structural, not asserted.** The normative registry in §7.1 must be
**pinned by digest in the preregistration itself**, and the gate must compare the converter's emitted
IDs and the exercised fixture IDs **against that pinned digest's contents**, which the converter does
not author and cannot alter. State the digest field, where it is bound, and what the gate does on
mismatch. If the registry cannot be pinned before the converter exists, **say that and mark the gate
unresolved** — a third round of rewording will not make a self-comparison independent.

## Blocker 2 — BS-2v is listed but has no authenticated receipt schema (both seats)

§6.1 names BS-2v in the closed non-χ-bearing list, but §11 supplies **no canonical authenticated
receipt schema**, so nothing can produce a conforming receipt and no gate can reject a
non-conforming one.

**Repair:** specify the schema in §11 — registry digest, converter implementation digest, ordered
normative IDs, exercised IDs, uniqueness and count closure, per-ID source/phase/failure-effect, and
result classification — and state which are authenticated.

## Blocker 3 — the V22→V23 trace claims a completion that did not happen (GPT56 3)

It records the BS-2v repairs as done. Blockers 1 and 2 show they are not. **Correct it.**

## Change 4 — §10's trace is now GENERATED. Replace it.

**`gates/GENERATED_TRACE.md` contains a trace table computed from the draft bytes** — digests by
sha256, sections and line counts by diff, §7 row counts by parsing the table. **Replace §10's
hand-written transition rows with that table verbatim.**

Keep the finding→change mapping §6.3 requires, but express it as **finding IDs referenced from the
referee reports**, not as prose characterising whether each change succeeded. The reason, which
belongs in §10 in your own words: *a characterisation of a change can be falsified by a later edit
without the sentence changing, as happened when the V16→V17 row went from accurate to inaccurate
untouched. An observation of what the bytes did cannot.*

## Change 5 — §7's counts are now EMITTED. Say so.

§7 currently claims a "Lint assertion" that both seats note is not a passing independent check.
`tools/prereg_counts.py` now **writes** the count sentence from the parsed table rather than checking
a typed number.

**Repair:** state in §7 that the class counts are **emitted from the table by
`tools/prereg_counts.py`** and are not to be hand-edited, and remove the unbacked lint-assertion
claim. Then leave the numbers alone — 15 and 8 are already what the tool emits.

## Why 4 and 5 exist, for §10's record

The class-E count read 8, 8, 8, 8, then 7, then 8 across V18–V23: a closed invariant reopened because
a human typed a number a table already knew. §10 grew every round — the most-edited section in every
recent transition — because each row was a fresh assertion about history that a later edit could
falsify. **Both surfaces are now computed, so neither can drift.**

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**, including on unfilled `BS-2v`.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V24_20260827.md`, complete, single write, titled **V24**.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.
