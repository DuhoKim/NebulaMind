# EDIT BRIEF — close GPT56's blocker in V16. One item. Nothing else.

Target: `../PREREG_SUCCESSOR_DRAFT_V16_20260827.md`, sha256
`dc9774f1c6ef05b579493e8189aa68f5bbe0c5d76721384302394723d758a722`. **Verify before you start.**

**Edit V16 in place.** Do not create a new version. **Do not touch
`../PREREG_SUCCESSOR_DRAFT_V15_20260827.md`** — immutable at
`efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28`, checked before and after.

## The one blocker to close

GPT56, R15, HIGH/BLOCKING: **the canonical unblinding-receipt schema is absent from the
asserted-complete code-side list.**

Its evidence: Row O emits the unblinding receipt; Row P requires it; Clause 3(e) requires canonical
receipts to carry and authenticate decoded fields; Clause 4 requires the genuinely final
post-unblinding access-log checkpoint to be carried in it. The list requires §5 and the pinned
production symbol to *verify* the one-use receipt, names it as an artifact, and requires
`verify_unblinding_receipt` — **but no item says to add or freeze the canonical schema, or enumerates
the fields that verifier must authenticate.** The code-side schema bullet names BS-L, BS-2k, deferred
BS-2a, and the BS-2f/BS-L checkpoint and archive fields only.

Why it blocks, in GPT56's words: **"A verifier name does not define its accepted bytes."** Without a
frozen canonical schema, later code keeps freedom over what the receipt actually binds.

## The repair — add one item to §11, the code-side inventory

Require the **canonical unblinding-receipt schema and its exact authenticated fields**, including at
minimum:

- the **BS-L identity and checkpoint**;
- the **complete extending chain segment**;
- the **terminal unsealing events**;
- the **final post-unblinding checkpoint**;
- the **declared destination**;
- the **one-use ceremony identity and replay state**.

Bind those schema bytes into the **pinned implementation/schema digest** §11 already requires, and
state that **`verify_unblinding_receipt()` must authenticate exactly those fields**.

**Keep implementation marked UNRESOLVED until delivered.** Naming the required schema is the repair;
writing the code is not in scope and must not be claimed.

## Update the fold-record banner

The banner currently records this GPT56 blocker as **OPEN**. Change that entry to state that the
blocker is **closed at document-contract level by this edit** — the schema and its authenticated
fields are now required work in §11 — while the **implementation remains UNRESOLVED** with findings
1, 2, 2b and 3 pending the refused BS-2a design.

**Do not** claim §6 is now settled. BS-2a stays REFUSED, rows C2 and E cannot run, BS-6 and the first
image byte stay blocked.

## Also record, accurately

The banner should note that the earlier `prereg_lint.py` BS-2f finding was a **false positive in the
linter, not a defect in this document**: the flagged sentence is the fold record quoting what V15
said, and BS-2f correctly sits in Class E. The linter has been corrected and V16 now lints clean.

## What must not happen

Do not alter §6's body, the lifecycle table, any clause, any threshold, or §7's slot rows. Do not
reopen route (b) or the calibration repair. Do not touch V15.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V16_20260827.md`, edited in place, single write. Report the new sha256.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch.
