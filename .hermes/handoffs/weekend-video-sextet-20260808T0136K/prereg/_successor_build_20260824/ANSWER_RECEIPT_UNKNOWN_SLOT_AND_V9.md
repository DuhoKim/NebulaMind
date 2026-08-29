**FOR BLANC → THE PRINCIPAL.** Does closing CODEX-V56 F2 half two require unfreezing v9? **No — but
the wrapper alone does not close it, and that distinction is the answer.**

# `receipt()` accepts unknown slots — what it takes to close, and whether v9 must move

## CODEX's finding reproduces exactly, and is wider than reported

`receipt()` enforces exact fields **only** when `slot in SLOT_SCHEMA`. An unknown slot falls through
and receives a canonical-looking envelope over arbitrary fields. Executing the pinned bytes with
`{'per_object_chi': b'+1'}`:

    BS-3g  ACCEPTED  envelope 1a60e5c6  body e905f1b8
    BS-2a  ACCEPTED  envelope b35c41fa  body e905f1b8
    BS-2k  ACCEPTED  envelope a94f35dd  body e905f1b8
    BS-L   ACCEPTED  envelope b4e5aec8  body e905f1b8

**SLOT_SCHEMA holds 18 entries. Five slots are absent, not four** — BS-3g, BS-2a, BS-2k, BS-L **and
BS-2v.** So a consumer treating an envelope as schema conformance can export the per-object outcome
field §6.1 swears no listed schema can carry, on five slots.

## The v9 question, answered

**A successor-layer wrapper closes the mechanism without touching v9.** Verified:

    def receipt_strict(slot, fields):
        if slot not in v9.SLOT_SCHEMA:
            raise RuntimeError(f"receipt {slot}: slot is not in the pinned SLOT_SCHEMA — FAIL")
        return v9.receipt(slot, fields)

`BS-3g` is refused; `BS-6`'s existing field enforcement is untouched and still refuses a wrong field
set. **v9 verified unchanged at `6a9abbbd`.**

## But the wrapper alone is not sufficient, and this is the part to put to him

**`v9.receipt()` remains permissive.** The wrapper protects only callers who use it, so the hole
closes only if **every producer is bound to the strict constructor** — and that binding is a
**document** obligation, not a code change:

- **§11** must name the strict constructor as the **only** permitted receipt path;
- **a verifier** must check that every emitted receipt's slot is in the pinned schema, so a receipt
  built by the permissive path is detectable after the fact rather than merely discouraged;
- and the five missing slots need entries, or they remain unconstrained even under the wrapper.

**The unfreeze question returns only if the document cannot bind all producers.** If some producer
cannot be routed through the wrapper, the permissive path stays reachable and only v9 itself can close
it. **My reading: bind and verify, do not unfreeze.** The principal has kept v9 frozen all day and
deprioritised `require_authorization` specifically to avoid this, and nothing here forces his hand.

**What I have NOT done:** written the wrapper into the successor layer, added the five SLOT_SCHEMA
entries, or specified BS-3g's schema. **He asked for the schema and producer; that is half one and is
document content, and I did not start it at 20:47 against a 21:00 bound** — a half-specified schema is
exactly the defect CODEX just found, and the fields have to be written so someone who did not write
them can implement the verifier.

**Also true, and it is the reason to do half one carefully rather than quickly:** BS-3g's receipt must
be shown incapable of carrying a per-object field, because §6.1's non-χ-bearing claim rests on it.
That is the same test CODEX applied to the refusal codes, and it is a property to be demonstrated,
not asserted.
