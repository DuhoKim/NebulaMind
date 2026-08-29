**FOR BLANC — READ BEFORE TAKING ANYTHING TO THE PRINCIPAL.** V59's STOP condition fired. **It does
NOT return the unfreeze question.** It fired on my own overbroad wording, and the repair is scoping.

# The STOP triggered, and it is mine rather than v9's

**Both seats fired it** (CODEX-V59 F2 HIGH, GPT56-V59 F1 HIGH): the universal `receipt_strict()`
binding *"cannot be satisfied by named producers of non-`SLOT_SCHEMA` receipts."*

**They are right, and the cause is a sentence I wrote too broadly.** V59 says *every producer named in
§6.1 and §7 must construct receipts through `receipt_strict()`*. But §6.1's rows emit artifacts that
are **not slot receipts at all**:

    Row B   the access-log chain
    Row C   the χ-bearing cutout-completion receipt
    Row C2  the acceptance-evidence projections, one per parent object
    Row H   the χ-bearing label-set receipt
    Row O   the unblinding receipt
    Row P   the post-unblinding adequacy receipt
    Row Q   the archive seal-state receipt

`receipt_strict()` **refuses any slot absent from `SLOT_SCHEMA` by design**. Routing a non-slot
artifact through it would refuse it by construction. **So the rule as written is unsatisfiable for
seven rows — not because those producers are unbindable, but because I applied a slot-receipt rule to
artifacts that are not slot receipts.**

## Why this is not the unfreeze path

My STOP was written for *"a producer that cannot be routed through the strict constructor"*, meaning
**a slot-receipt producer that must use the permissive `receipt()` and cannot be redirected.** That
would leave the permissive path reachable by a route the document cannot bind, and only v9 could close
it.

**No such producer has been found.** What was found is a rule broader than its subject. **The repair
is to scope the binding to producers of SLOT receipts**, and to say what governs the other seven
artifact classes — which is document work, not a change to frozen v9.

**One genuine gap sits inside it, and it is also not an unfreeze:** GPT56-V59 F1 notes **BS-7p still
names the permissive `receipt()`** — and BS-7p *is* in `SLOT_SCHEMA`. That is a slot producer pointed
at the wrong constructor, and it is fixed by pointing it at the right one.

**v9 stays frozen at `6a9abbbd`. Nothing here asks him to reconsider that.**

## Second item, so it is not read as a wrong value

Both seats flagged that the digest `fd6d6d7e…` in §6.1 does not match the refusal checker's on-disk
SHA-256 `c2ccebbc…`. **Both numbers are correct and I labelled one wrong.**

    fd6d6d7e99dcb5ca   the corrected ROW FINGERPRINT of §6.1's gate-bearing columns
    c2ccebbcb4730944   the sha256 of tools/refusal_vocabulary_check.py itself

V59 says *"the tool is fixed (`fd6d6d7e…` is the corrected digest)"*, which reads as the tool's digest.
**It is not a wrong value; it is a wrong label**, and two independent readers took it the way it was
written rather than the way it was meant. Fixing the sentence, not the number.

## Not yet repaired, and not blocked on him

GPT56-V59 F4 / CODEX-V59 F1 — the suspended eight-code set is still the operative schema language and
the checker still enforces it, so the prose suspends what the machinery asserts. GPT56-V59 F3 /
CODEX-V59 F3 — BS-3g binds neither its input sample nor a perturbation manifest, so a valid-looking
receipt could certify a favourable subset; that is a real hole in the schema I wrote this evening.
GPT56-V59 F6 — the evidence bar's "vary every argument" is vacuous for zero-argument guards that read
global or filesystem state. GPT56-V59 F7 / CODEX-V59 F5 — the count drifted again, 21 against a live
table at 20.
