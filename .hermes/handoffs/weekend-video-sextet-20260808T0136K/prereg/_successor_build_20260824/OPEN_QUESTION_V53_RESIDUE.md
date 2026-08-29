**STATUS: OPEN** — with the principal. Two V53 findings whose repair is normative.

# OPEN QUESTION — the freeze-signature exemption's scope, and BS-2v's stale UNRESOLVED

**Raised 2026-08-29 19:4x KST by Hwao. V54 repaired the rest. These two change what the study
claims.**

## 1. "The freeze signature" is not defined, so the exemption is unbounded (CODEX-V53 F4)

V52 exempted **the freeze signature** and **the canonical opening authorization** from Row L's
wrong-signature VOID condition, and I wrote at the time that the exemption is *"by named object rather
than by category"* because *"an exemption for 'signatures generally' would be broad enough to be the
hole it closes."*

**CODEX's finding is that naming the object is not enough when the object has no canonical form.**
There is no freeze-signature body, no field set and no verifier that says which signed bytes qualify.
So *"the freeze signature"* exempts whatever the signer chooses to call by that name — which is the
breadth the exemption was written to avoid, arriving through the definition rather than the category.

**The repair is a build, not an edit:** define the canonical freeze-signature body and its verifier,
the way BS-L's detached signature is defined over the canonical lock-body digest. **That is new
normative machinery** and it is the principal's.

**Worth noting what it does not undo.** The self-voiding contradiction is genuinely closed — the row
no longer punishes the acts it mandates. What is open is that one of the two exempted acts is
under-specified.

## 2. BS-2v is still UNRESOLVED for a self-reference its own checker disproves (GPT56-V53 F2)

The BS-2v row and the preamble both carry the claim that the registry cannot be pinned before the
converter exists. **`tools/void_registry.py` disproves it and both seats cleared the mechanism back at
the VOID gate round:** §7.1's content comes from the document's own normative clauses, and digesting
the canonical rows while storing the digest in the BS-2v row creates no fixed point.

**Moving BS-2v off UNRESOLVED changes a slot's status**, which is a claim about what the study has
settled, so it is not mine. **And pinning remains necessary-not-sufficient** — CODEX established at
that round that the converter, receipt schema, verifier and fixtures must still be delivered and
gated. Clearing the stale *reason* does not unblock the slot.

## Repaired in V54

**All five `UNREACHABLE-BY-CONSTRUCTION` promotions are WITHDRAWN** (GPT56-V53 F1, CODEX-V53 F1, both
HIGH; CODEX-V53 F2). Both seats showed **L1401 is directly reachable**: `allocate_handcheck` takes
`budget` as an argument and my harness froze it at `HC_REAL_LABELS = 500`. **At `budget = 200` it
fires immediately.** A harness that freezes an argument cannot observe the guards that argument
controls.

Re-run with `budget` varied over 80,000 executions: **L1401 fires**; L1411/L1435/L1437/L1439 still do
not. Their measurement survives — **they are withdrawn anyway**, because a generic appeal to
*"feasibility is decided before allocating"* is not the per-site predecessor condition the rule
demands. Surviving a better harness is not meeting the bar.

**No site now holds the status.** The bar is restated in §5 so a third attempt is not a third failure:
a harness varying **every argument in the callable's documented surface**; a **named per-site**
subsuming condition for any structural claim; and a positive control.

**This is the second consecutive round the promotion failed**, which is why V54 withdraws rather than
re-argues. Also fixed: §11's stale 48-unread status, and §5/ledger agreement — both now at
**NUMERICAL 22**.

**V54** = `b0ccbecc46e21677`. Checkers: 16/8 prose-matched, trace 53 transitions 0 problems,
`void_registry` 6/0, lint exits 0. **BS-6 and the first image byte remain blocked.**
