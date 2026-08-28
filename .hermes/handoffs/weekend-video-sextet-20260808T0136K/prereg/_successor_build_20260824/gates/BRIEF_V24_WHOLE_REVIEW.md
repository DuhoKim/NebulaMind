# REFEREE BRIEF — V24, whole document. Ninth assembled round.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V24_20260827.md`**, sha256
`6d722dc51316a2dbc3f3cf07a7dec8c8c5776df16388b43177681899cb32f977`. **Verify; state what you
compared.** 125 lines changed from V23 — most of it §10 being replaced by a generated table.

## Two surfaces are no longer written. They are computed.

Both of you have now spent rounds on defects that were never about the study. The principal's
diagnosis: **the §7 count and the §10 trace are prose asserting facts that a program can derive, so
both have expiry dates.** The evidence he gave:

- §7's class-E count read **8, 8, 8, 8, then 7 at V22, then 8 at V23** — a closed invariant reopened,
  because a human types a number a table already knows.
- GPT56 recorded the V16→V17 trace row as ACCURATE in V20, ACCURATE in V21, **NOT ACCURATE in V22** —
  **nobody edited that row.** Later edits made a true statement false.

So:

1. **§10's transition rows are now generated** by `tools/prereg_trace.py` from the draft bytes —
   digests by sha256, sections and line counts by diff, §7 row counts by parsing the table. The table
   states **what changed**, never **what the change accomplished**, because a characterisation can be
   falsified by a later edit without the sentence changing, and an observation cannot.
2. **§7's counts are emitted** by `tools/prereg_counts.py` from the parsed table, not typed.

**Judge these as you would any other mechanism.** A generator can be wrong. Check the table against
the drafts yourself — the files are all present and immutable at their reviewed digests.

## The two blockers you both raised

3. **BS-2v coverage independence** — third round on this. V24 was told to make it structural: pin the
   §7.1 registry **by digest in the preregistration**, and have the gate compare emitted and fixture
   IDs against that pinned content, which the converter cannot author. **Check whether that is what
   happened, or whether it is a fourth rewording of a self-comparison.** The brief also authorised
   marking the gate unresolved if the registry cannot be pinned before the converter exists — if that
   is the honest state, confirm the document says so.
4. **BS-2v's authenticated receipt schema** in §11 — registry digest, converter implementation digest,
   ordered normative IDs, exercised IDs, uniqueness and count closure, per-ID
   source/phase/failure-effect, result classification. **Can a gate now reject a non-conforming
   receipt using only what is written?**

5. The V22→V23 trace's false completion claim about the BS-2v repairs.

## What you credited in V23 — do not disturb

The §7 count repair (both of you recounted, bounding before `### §7.1`: 15 class P, 8 class E), both
historical trace rows, and the V16→V23 predecessor banner chain, which CODEX recomputed pin by pin.

## Also

**Clause 10 across §§0–11, both directions**, still expected unresolved at `VOID`. **Every threshold:
value, phase, failure effect.** **Read the neighbours** of every change. And say whether replacing
§10 with a computed table has broken anything that depended on its prose.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**, including on unfilled `BS-2v`.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`V24_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.**
