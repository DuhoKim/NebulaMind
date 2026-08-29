# V56 whole-document referee — CODEX

## Verdict

**NOT CLEAR.** The V56 subject hash matches the brief, and several requested repairs hold, but the access-log repair fails its own load-bearing claims. The fingerprint advertised as binding the vocabulary to every gate-bearing surface ignores the entire surface column; the new BS-3g receipt is still not schema-conformable or independently verifiable; a normal mediator refusal exists outside the eight-code set; and the stated request/authorisation principle does not prevent an ostensibly request-shaped code from revealing an object property. The raise-site inventory also violates §5's caller boundary at a concrete site and retains contradictory post-V55 totals.

## Findings

### F1 — HIGH — the refusal-vocabulary fingerprint ignores every row's stated surface

**At issue:** §6.1 lines 581–582; `tools/refusal_vocabulary_check.py` lines 70–85.

V56 says the set stops being closed when §6.1 gains or changes “a row, a surface or a precondition,” and says the adjacent fingerprint makes that dependency a check. The checker does not fingerprint the `may touch (read → write)` surface column. After splitting a row, line 83 keeps columns 1, 4, 5 and 7: row ID, phase, authorization, and void condition. Column 3—the entire surface—is omitted.

I replaced Row B's surface in memory with `MAY READ AND EXPORT EVERY SEALED BYTE WITHOUT LIMIT` while leaving its ID, phase, authorization and void column untouched. The fingerprint remained byte-for-byte identical:

- original: `1d0b3e48ac5a435441662d3a9137fbf6b07e603e8b78205931fad386b72682bd`
- surface-mutated: `1d0b3e48ac5a435441662d3a9137fbf6b07e603e8b78205931fad386b72682bd`
- equality: `True`

That is not a hypothetical parser edge: the derivation at line 581 explicitly rests on whether the requesting row's surface covers the act. The checker therefore passes after changing the very premise from which `REFUSED-OUTSIDE-STATED-SURFACE` is supposedly derived. Its exit 0 on V56 does not establish the claimed closure. The repair must fingerprint the surface column as well, with a control that mutates only that column and demands a changed digest.

### F2 — HIGH — BS-3g remains non-receiptable, and absent slot schemas accept arbitrary outcome fields

**At issue:** §6.1 lines 574–587; §7 lines 747, 762; §11 line 976; `ref/successor_ref_v9.py` lines 185–224.

The §6.1 closed non-χ list names BS-3g as a slot receipt “under the pinned `SLOT_SCHEMA`,” but the pinned schema has no BS-3g entry. It also lacks BS-2a, BS-2k and BS-L. Section 11 merely says to add a schema entry, producer and independent verifier later and expressly admits that without them the BS-3g edge is not receiptable. It does not specify the exact BS-3g receipt fields or verification contract now.

The code makes this worse than a documentation omission. `receipt()` checks exact fields only when `slot in SLOT_SCHEMA`; an unknown slot falls through and receives a canonical-looking envelope over arbitrary fields. Executing the pinned bytes with the synthetic field `{'per_object_chi': b'+1'}` produced accepted receipts for all four absent slots:

- `BS-3g ACCEPTED e905f1b8…`
- `BS-2a ACCEPTED e905f1b8…`
- `BS-2k ACCEPTED e905f1b8…`
- `BS-L ACCEPTED e905f1b8…`

Thus the V41 addition did not make the `blocks BS-6` edge receiptable, and a consumer that equates a `receipt()` envelope with schema conformance can export exactly the per-object outcome field §6.1 says no listed schema can carry. Before BS-3g can appear on the non-χ list, the draft must pin its exact fields, producer, verifier and failure behavior, and the receipt machinery must reject unknown slots rather than canonically enveloping them.

### F3 — MEDIUM — the eight-code refusal set omits ordinary mediator execution refusals

**At issue:** §6.1 lines 577–582 and Row B at line 598.

Row B must append one event for every attempted touch, “success or refusal.” Consider an otherwise authorized, in-phase, in-surface read whose sealed-store read fails because the store/object bytes are unavailable or the mediator's I/O operation fails. Row B must refuse delivery. None of the eight codes applies:

- the requester and identity are permitted;
- the act is within the stated surface;
- all prior artifacts verify;
- the phase and lock are correct;
- the request schema conforms;
- no ceremony has been consumed.

`REFUSED-OBJECT-BYTES-UNAVAILABLE` would describe the object and violate the new principle; `REFUSED-REQUEST-COULD-NOT-BE-SATISFIED` would fit the principle's grammar but is not in the set. Treating the event as an unlogged refusal merely triggers the accepted VOID cost; it does not make line 581's universal statement (“Every refusal is therefore one of”) true, nor does it preserve the required complete refusal log. The derivation enumerates policy/authorization denials but silently omits execution failures of the mediator itself. This category must be decided explicitly and the vocabulary regenerated from the actual refusal state machine, not asserted from the actor table alone.

### F4 — MEDIUM — the request/authorisation wording test still permits object leakage

**At issue:** §6.1 lines 578–581.

The principle is syntactic, not information-flow safe. An event already records the requested object identity. The existing code `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` can be described as an authorization-state statement about the request, yet in combination with that identity it reveals a property of the object/reference: whether the named identity belongs to the permitted set. That is new per-object membership information, contrary to line 578's claim that the reason “adds no per-object information.”

A still clearer code-shaped counterexample is `REFUSED-REQUESTED-RANGE-OUTSIDE-OBJECT-BOUNDS`: grammatically it describes the request and its authorization/admissibility state, but, given the logged range and object identity, it leaks a bound on the object's length. The stated TEST cannot exclude it. The checker only regex-checks that the prose contains “never ... OBJECT”; it performs no semantic or noninterference check on the codes. Closure therefore needs a field-by-field information-flow rule (what an observer can infer from identity + code), not a rule about which noun the reason describes.

### F5 — MEDIUM — a supplied-mask admissibility check is classified as integrity/VOID, violating §5's caller boundary

**At issue:** §5 line 496; `ref/RAISE_SITE_CLASSIFICATION.md` line 82; `ref/successor_ref_v9.py` lines 1012–1022.

`_BaseMask.__init__` receives `c` as an argument, converts that supplied argument, and raises at source line 1020 if it is non-finite or outside `[-1,1]`. The same constructor classifies supplied length, duplicate-ID, bin-label, acceptance and sign-label checks as CALLER errors. There is no independent digest or recomputation at line 1020 that turns bad supplied `c` into a protocol-integrity fact. Nevertheless the ledger alone marks line 1020 `INTEGRITY`, which §5's precedence assigns to VOID rather than to the caller boundary.

This is precisely the “too wide and it swallows input validation” failure §5 tells the referee to seek. Either the production contract must independently derive/authenticate `c` before construction (making a mismatch an integrity condition), or this site is CALLER under the draft's present checkable test. The current classification cannot stand as written.

### F6 — LOW — the V55 count repair remains internally contradictory in both the draft and ledger

**At issue:** §5 line 524; `ref/RAISE_SITE_CLASSIFICATION.md` lines 9–16.

The ledger summary says CALLER 21 and NUMERICAL 21, but its next paragraph says the numerical class “drops from 22 to 18.” V56 line 524 first reports `CALLER 20 · ... · NUMERICAL 22`, immediately says “The numerical class is 21,” and then discusses 18 if the three soft sites move. The table's stated class totals are 21/21. V55 was supposed to move L1464 from numerical to caller and reconcile 22→21; the stale 20/22 and “from 22” text means that repair did not reach all count claims. Replace every derived total from the table, not by hand.

## Failed attacks / repairs that held

- The subject SHA-256 recomputed exactly to `c0743b40698e75b69451fd317adafae94d4f80d011b988dcb2e992496040d122` before the draft was read.
- `tools/prereg_counts.py` recomputed 16 Class-P and 8 Class-E rows and exited 0; I found no live 15/8 assumption outside the historical V36→V37 trace.
- `UNREACHABLE-BY-CONSTRUCTION` is retained only as a status definition/history in the draft: V56 says no site holds it, all five promotions are withdrawn, and the raise-site ledger assigns none.
- The falsification clause names `INCONCLUSIVE-BY-NUMERICAL-FAILURE` as the outcome if a future unreachable classification fires; I found no route-less falsification branch in that clause.
- Row L's two named exemptions are wide enough for the required freeze and opening-authorization acts; the BS-L detached signature is over the canonical lock digest and therefore does not need a third exemption. I did not re-derive the parked question about canonical freeze-signature bytes.
- The misconduct antecedents remain `Any` for forbidden acts, protocol deviation and digest deviation in §7.1. The post-unblinding narrowing applies only to numerical non-finite/degenerate antecedents.
- The V43 five-step numerical rerun allowance is absent. Remaining “rerun/retry” text concerns future Stage-P measurement, BS-2a design semantics, historical explanation, or an explicit prohibition on Row-P retry—not a discretionary retry after numerical failure.
- The Stage-P attribution now cites GPT56-V11 F4 and CODEX-V11 4, and those reports do support the dual-valued claim. KIMI-V11 F7 instead concerns the v7 subject/disclosure and does not support it; V56 now says so.
- `tools/refusal_vocabulary_check.py` exits 0 and its self-test reports seven controls, zero failures; F1 explains why those passing results do not test surface changes.
- `tools/void_registry.py` reports 54 antecedents, 20 defined rows and exits 0. This confirms name coverage only, consistent with V56's limitation statement.
- The lint exits 0 and the count checker matches 16/8. Passing tools do not reach F1–F5.

## Evidence and scope

Read in content: the exact V56 draft; `BRIEF_V56_REVIEW.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/successor_ref_v9.py` at the referenced schema, mask and calibration regions; `tools/refusal_vocabulary_check.py`; and the V11 KIMI/GPT56/CODEX reports needed to verify the repaired Stage-P attribution. Executed: subject SHA-256; refusal checker and self-test; an in-memory Row-B surface mutation against `row_fingerprint`; synthetic unknown-slot `receipt()` probes; AST raise count; prereg count checker; VOID registry checker; and lint. No draft or referenced file was modified. The only written deliverable is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V56
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 581–582; refusal_vocabulary_check.py lines 70–85 | Fingerprint omits the row-surface column, so a closure-breaking surface change passes unchanged.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 574–587; §7 line 762; §11 line 976 | BS-3g has no pinned schema/producer/verifier, and unknown-slot receipts accept arbitrary outcome fields.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 577–582; Row B line 598 | Ordinary mediator I/O or object-unavailability refusal is outside the alleged exhaustive eight-code set.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 578–581 | Request/authorisation-shaped codes can still reveal object membership or bounds.
F5 | MEDIUM | REPAIR-REQUIRED | §5 line 496; raise ledger line 82 | Supplied mask-c admissibility is misclassified as integrity/VOID rather than caller error.
F6 | LOW | REPAIR-REQUIRED | §5 line 524; raise ledger lines 9–16 | Post-V55 caller/numerical totals still contradict the table and each other.
<!-- END FINDINGS-BLOCK -->