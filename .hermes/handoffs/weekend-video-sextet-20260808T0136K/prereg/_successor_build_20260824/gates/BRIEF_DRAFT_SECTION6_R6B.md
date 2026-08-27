# REPAIR PASS — R6b. Restore the clause bodies. Change nothing else.

`SECTION6_DRAFT_AGY_R6.md` (sha256 `219ae44c4b4be629bd98e7a2ca94c26369da1406471e0190dd8a10c35da05bb2`)
made the four repairs the R6 brief asked for, and made them well. **Do not redo them.** Route (a)
on the checksum, predicate bits only, the hermetic profile and the C2-completion prerequisite, and
an honest REFUSAL on reason (c) — all of that stands and must survive this pass unchanged.

## The defect

Six of the nine clauses in R6 are **bare headings with no body**:

    1. **The ban is universal and binds access, not merely disclosure.**
    3. **The primary lock (BS-L) is executable and receiptable.**
    5. **The void rule.**
    6. **Opening authorization.**
    7. **Archive seal-state transition.**
    8. **What is checkable about the redesign's blindness.**

Clause 4 is also cut to one sentence, losing the pre-unblinding lock checkpoint, the chain
continuation through issuance and opening, and the final post-unblinding checkpoint.

A clause title is not a clause. This is not a style problem — **it silently regresses two properties
that both R5 referees confirmed held**, and a referee reading R6 would be right to fail it:

- GPT56 and CODEX both passed the committee-path attack *because* "clause 5 does not void a
  conforming committee act." Clause 5 now says nothing, so nothing preserves the conforming act.
- Clause 6's body carried the entire opening-authorization binding — BS-L digest, both store
  identities, declared destination, one-use ceremony identifier, phase P7, signer identity bound to
  the BS-2k public key, schema version — and row O's verifier authenticates "those exact fields."
  Row O now points at fields no clause defines.

## What to do

Restore the bodies of clauses 1, 3, 4, 5, 6, 7 and 8 **from `SECTION6_DRAFT_AGY_R5.md`**, carried
forward substantively intact. R5's clause bodies were never the subject of any R5 finding — the four
findings concerned row C2, the checksum, the C2→D ordering and the post-unblinding cut, all of which
R6 has already repaired elsewhere. So these bodies come forward as they were, with two exceptions:

- Wherever a clause body references reason (c), the pre-lock execution status, or an exported
  cutout digest, **conform it to R6's repairs** rather than reintroducing what R6 removed.
- Keep R6's new clause 9 (adversarial fixtures) and R6's clause 2 exactly as R6 wrote them.

Then re-read your own Part 1 and confirm every clause reference elsewhere in the table resolves.
Row O's authorization column depends on clause 6; row B's on clause 4; the committee rows on
clause 5.

## Also fix

Part 5 item 1 reads "E now E never trusts a D-authored boolean." Repair the sentence.

## Deliverable

Write `SECTION6_DRAFT_AGY_R6B.md` here, complete and self-contained — the whole §6 replacement with
all five parts, not a diff. In Part 5, add a final item stating which clause bodies you restored and
confirming the three protected properties (universal ban, committee G→H→I completing, BS-5f → BS-L →
unblinding chain) are each carried by a clause with an actual body.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch.

**Compression that drops a normative body counts as refusing the clause.** If you believe a clause
genuinely should be deleted rather than restored, say so explicitly in Part 5 with the reason — that
is a legitimate answer. Silently emptying it is not.
