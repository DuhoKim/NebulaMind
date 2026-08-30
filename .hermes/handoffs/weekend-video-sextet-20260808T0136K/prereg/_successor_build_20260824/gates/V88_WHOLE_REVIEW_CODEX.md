# CODEX — V88 whole-document adversarial referee report

## Verdict: NOT CLEAR

The V88 supersession sweep did not close the arrival-event regime as a set. The new arrival class is absent from the draft's exhaustive non-χ-bearing access-log schema, multiple live sentences still assert the retired no-arrival regime, the claimed arrival→terminal total join is implemented in prose only as a partial/injective join, and the BS-L temporal partition requires its signed checkpoint both before and through issuance. These are contract-level contradictions, not implementation TODOs.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — §6.1 lines 589–592, 691, 702: the arrival event is outside the exhaustive non-χ-bearing schema

Section 6.1 says the non-χ-bearing receipt/log list is closed and exhaustive, and item (ii) defines the BS-2k access-log event schema as:

`timestamp, actor, table row, operation, object identity, success/refusal, refusal reason, running chain digest`.

Row B later defines ARRIVAL with a different closed body:

`kind=ARRIVAL, timestamp, row, operation, object identity, request_key, running chain digest`.

The arrival body adds `kind` and `request_key`, omits the decision-only fields, and is neither a slot receipt under item (i) nor an event conforming to item (ii) as written. Section 6.1 line 691 makes the consequence explicit: everything not on the exhaustive list is χ-bearing by default. Thus the write-ahead arrival events needed by recovery and the pre-lock verifier become χ-bearing objects that the non-χ gate readers are not allowed to consume.

The registry generator does not repair this document contract. `ref/STRING_FIELD_REGISTRY.md` has manually generated `arrival.*` rows (95–101), but labels them `v9 SLOT_SCHEMA` even though frozen v9 has no arrival slot, while `nonslot.access_log_chain` says it is inventoried by the `event.*` rows. A registry row cannot silently widen §6.1's exhaustive schema.

Required repair: make ARRIVAL an explicit second authenticated non-slot event schema in §6.1's exhaustive list, bind its exact fields and value domains to BS-2k, and make the registry's declared source accurately point to that schema.

### F2 — HIGH — REPAIR-REQUIRED — §6.1 lines 640, 647–652; lifecycle spec line 70: the supersession sweep missed multiple live no-arrival assertions

The highest-value sweep attack succeeds in both governed files:

- Draft line 640 says death before commit has “no event” and, in the same sentence, says “the arrival event shows the request existed.”
- Draft line 648 still says “a request with no binding never happened,” although an arrival-without-terminal is now the ruled, visible recovery state.
- Draft line 649 first says arrival makes the request visible, then retains the old residue: “a crash between decide-and-append is indistinguishable from a request that never arrived.” It is distinguishable by the already-committed arrival event.
- Draft line 652 says “nothing above changes what the access log records beyond the refusal-reason field,” directly contradicting the newly authorised second event class acknowledged three lines earlier.
- `LIFECYCLE_GUARANTEE_SPEC.md` line 70 retires N2 because the principal authorised the second event class, while its live “why it cannot be otherwise” cell still says the change is “not authorised, REFERRED.”

These are not harmless history labels: they sit in live construction, recovery, authority, and non-guarantee statements. The derivation checker stays green because it binds labelled G/N quote bodies and does not cover these unlabelled normative tails—the exact blind spot the brief asked this round to exploit.

Required repair: re-derive the whole request/recovery block and the complete N2 row from the arrival ruling; do not append corrective tails to predecessor sentences.

### F3 — HIGH — REPAIR-REQUIRED — §6.1 line 702; lifecycle spec lines 55–63, 80, 97–111: the claimed exactly-one terminal join is only at-most-one

Row B claims that “every arrival joins EXACTLY ONE terminal event,” but the stated bidirectional verifier proves only:

- every arrival has **at most one** terminal naming it; and
- every terminal has exactly one prior arrival.

That permits an orphan arrival with zero terminal events. The lifecycle spec explicitly produces that state after a W1 death (line 80) and relies on deadline/recovery to close it, but neither Row B's join predicate nor the five-gate enumeration rule says a gate refuses an arrival with no terminal after its deadline. A chain containing one arrival and no terminal satisfies both stated join directions vacuously on the terminal side and satisfies “at most one” on the arrival side.

This breaks the promised totality (“every request ends in exactly one state with one terminal treatment”) while preserving uniqueness. `request_key = chain_position` fixes key reuse; it does not fix missing terminals.

Required repair: at each relevant checkpoint, require every arrival either (a) to have exactly one terminal decision, or (b) to be provably still within its immutable deadline under a separately named pending-state rule that blocks any gate which requires lifecycle closure. At the final checkpoint, zero-terminal arrivals must be forbidden without exception.

### F4 — HIGH — REPAIR-REQUIRED — §6.1 lines 611, 731, 736: the BS-L checkpoint is required both before and through issuance

Clause 4 says the pre-unblinding lock checkpoint is taken “immediately before canonicalizing BS-L” (line 736), and Clause 3(b) puts that checkpoint inside BS-L's signed canonical body (line 731). But the temporal-partition paragraph says BS-L issuance is one atomic commit whose **own mediated write events are the last pre-partition events**, and that “the checkpoint's chain segment extends through issuance completion” (line 611).

Both orderings cannot hold. If the signed body contains a checkpoint through issuance completion, canonicalizing/signing BS-L requires the event caused by issuing/writing that same BS-L: a circular object. If the checkpoint is taken before canonicalization as Clause 4 says, issuance's own events are not in the signed checkpoint and cannot be the sealed-side events line 611 claims.

Atomicity removes partial commit states; it does not solve this serialization/self-reference problem.

Required repair: choose a non-circular cut. For example, bind BS-L to a checkpoint immediately before issuance and put issuance events in the authenticated continuation, or define a separately signed post-issuance envelope that authenticates both the pre-issuance body and the issuance event. The current text may not claim both.

## Failed attacks / checks that held

- Subject identity held: live SHA-256 was exactly `1a7810442b6d774301c840487ec271b095512b85311745d93c2fdc0fd3cc235a` before reading.
- `tools/prereg_counts.py` independently returned 16 class P / 9 class E and said prose matched the table. The V86→V87 generated row contains the 17→16 / 8→9 move.
- `tools/prereg_lint.py` exited 0: 97 advisory legacy citations, 0 blocking. I did not re-report those option-D legacy advisories.
- `tools/refusal_vocabulary_check.py` exited 0 on V88; its self-test reported 34 controls, 0 failures, every code controlled. Its live SHA-256 matches the draft's `58344f0b89a2c91e…` pin.
- `tools/lifecycle_derivation_check.py` reported 0 problems; the spec SHA-256 matches the draft's full pin `5005290afd34c720e5dc24e838f674f9d1e6690d5ed1df8afcd87939c76d6c3b`.
- `tools/void_registry.py --self-test` reported 57 antecedents and 6 controls with 0 failures.
- Independent AST enumeration of `successor_ref_v9.py` found exactly 112 `Raise` nodes. Their line set exactly equals all 112 rows in `ref/RAISE_SITE_CLASSIFICATION.md`; recomputed classes are CALLER 26, INTEGRITY 59, NUMERICAL 20, PLANNING-INTERNAL 3, TYPED-OUTCOME 1, WRAPPER 3. The source SHA-256 also matches its frozen pin.
- The draw discipline was not re-derived because the brief's later explicit instruction says not to attack it while pending the principal's sitting.

## Evidence ledger and scope

Content-read: `BRIEF_V88_REVIEW.md`; the complete V88 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `tools/refusal_vocabulary_check.py`; targeted arrival rows in `ref/STRING_FIELD_REGISTRY.md` and `ref/gen_string_field_registry.py`; frozen `ref/successor_ref_v9.py` by AST.

Executed: SHA-256 recomputation; V87→V88 byte diff; prereg counts; prereg lint; refusal-vocabulary checker and self-test; lifecycle derivation checker; VOID-registry self-test; independent AST/table reconciliation; scoped git-status checks. No draft, spec, reference, tool, or gate file other than this report was modified.

Uncertainty: the brief's required block literally specifies `VERSION: V87` although the subject and requested report filename are V88. I preserve the mandatory block exactly as instructed rather than silently correcting the control-plane token.


**CONTROL-PLANE CORRECTION (Hwao, 2026-08-30, V89 build).** The block below declared `VERSION: V87` because my brief's REQUIRED REPORT FORMAT carried that literal — the seat flagged the discrepancy in its own report and preserved the token rather than silently correcting my template. The token is corrected to `V88` here because two blocks declaring one (seat, version) key made citations resolve against the wrong report (prereg_lint caught it as two false FABRICATED verdicts). Findings, prose and verdict are untouched; the template itself is fixed in BRIEF_V89.
<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V88
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 589–592, 691, 702 | ARRIVAL is outside the exhaustive non-χ-bearing access-log schema and defaults χ-bearing.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 640, 647–652; lifecycle spec line 70 | The supersession sweep leaves live no-arrival assertions contradicting the authorised arrival class.
F3 | HIGH | REPAIR-REQUIRED | §6.1 line 702; lifecycle spec lines 55–63, 80, 97–111 | The verifier enforces at-most-one terminal per arrival, not the claimed exactly-one total join.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 611, 731, 736 | BS-L's signed checkpoint is required both before and through issuance, creating a circular cut.
<!-- END FINDINGS-BLOCK -->