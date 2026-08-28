# REPAIR BRIEF — V28. The document is sound. My checker was not, and §10 repeated its claim.

Base: `../PREREG_SUCCESSOR_DRAFT_V27_20260827.md`, sha256
`e801a18bb7c489f0e4924695a13ba2f97f65a1b768c6dcc54a515cd5b31fb064`. **Verify before starting.**
Read `V27_WHOLE_REVIEW_GPT56.md` and `V27_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V28_20260827.md`.** Do not edit V27. **Do not touch V15–V26.**

## What both seats confirmed held — change none of it

- **Stage P superseded**: `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK` at §2.6 line 292 and §4
  lines 448–450, with BS-5p unfillable until a rerun. Held.
- **Orphan `VOID-6.1C2-ATTESTATION-FAIL` removed**, not given a fabricated antecedent. Held.
- **Catalogue quality in the closed pre-lock vocabulary.** Held.
- **§2.7 line 378 byte-for-byte unchanged.** Keep it that way.

## The only blocker — and it is mine, not yours

§10 claims the findings mapping is enforced. **I gave you that claim on the strength of a checker
that could not fail.** Both seats tested it and it broke three ways:

1. **The current transition was skipped entirely** instead of checked against the sidecar that owns
   it — the row most needing verification was the one guaranteed never to be examined.
2. **The presence test searched the whole document**, so §6.3's prose sentence *"The V24→V25 mapping
   must…"* satisfied it and masked a missing table row.
3. **The endpoint test ORed both digests document-wide**, and a predecessor's result digest already
   appears in the preceding row.

All three are fixed in `tools/prereg_trace.py`. Under the corrected checker, **V27's §10 table is
missing two rows: `V24 → V25` and `V25 → V26`.** V26 was missing one and I had reported it clean.

## Repair

1. **Replace §10's transition table with `gates/GENERATED_TRACE.md` verbatim.** It is regenerated and
   carries every transition through `V26 → V27`, each with both endpoint digests, computed section
   and line counts, §7 row-count changes, and the human-supplied findings column.

2. **Rewrite §10's enforcement sentence to say what the checker actually does**, in three parts:
   - in-band coverage is the §10 table, scoped to **the table itself**, stopping at the subject's
     predecessor;
   - the **current transition** is mapped in the sidecar `gates/FINDINGS_MAP.md` and **is checked
     there**;
   - **V1→V15 are exempt by a named rule in the checker**, not by silence.
   Each written row must carry **its own result digest** — not any digest found elsewhere.

3. **Do not assert that the checker returns zero.** State the contract; let the referees run it.
   The previous claim was true of a checker too weak to fail, and asserting a passing result is what
   made a tooling defect into a document defect.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V28_20260827.md`, complete, single write, titled **V28**.

Do not read `/Users/duhokim/NebulaMindData/`. No image byte is authorised.

**Where the document describes a check, describe what it checks — never that it passed.**
