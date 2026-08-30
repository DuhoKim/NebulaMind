# GPT56 — V88 whole-document adversarial referee report

## Verdict: NOT CLEAR

The V88 sweep repaired G4 but did not re-derive the event partition around the new ARRIVAL class. ARRIVAL is forbidden by G3 as an event that is neither a touch nor a refusal, and it also falls outside §6.1's exhaustive non-χ schema. The surrounding recovery text still asserts the retired no-arrival regime. The promised arrival→terminal total join is only injective in prose and is absent from the verifier's build contract. Independent attacks also found a circular BS-L checkpoint cut, a false count-correction statement, and two raise sites that violate the classification file's own caller/numerical boundary.

## Identity and reproduced checks

- Subject SHA-256, verified before reading: `1a7810442b6d774301c840487ec271b095512b85311745d93c2fdc0fd3cc235a` — exact match.
- Companion/spec SHA-256: `5005290afd34c720e5dc24e838f674f9d1e6690d5ed1df8afcd87939c76d6c3b`; the draft's lifecycle pin matches.
- `ref/RAISE_SITE_CLASSIFICATION.md`: `e5f4832df3d19075153361b19bb1613c679eb5b5f8eaefd53e3662c456f290e7`.
- `tools/refusal_vocabulary_check.py`: `58344f0b89a2c91eaf1bf15266d5ae5e15ea0df4af6547c0d00fa60ff0487291`, matching the draft's abbreviated pin.
- `prereg_counts.py`: 16 class P / 9 class E; the live count sentence matches the current table.
- `prereg_trace.py --check`: 87 transitions, 0 problems.
- `prereg_lint.py`: exit 0; 97 advisory legacy citations, 0 blocking.
- `refusal_vocabulary_check.py`: 0 problems; self-test 34 controls, 0 failures.
- `lifecycle_derivation_check.py`: 0 problems; self-test 9 controls, 0 failures. Its declared unlabelled-prose blind spot is material to F3.
- `void_registry.py --self-test`: 57 antecedents; 6 controls, 0 failures.
- Independent AST/table reconciliation: frozen v9 has exactly 112 `Raise` nodes, and their line set equals the classification table's 112 rows. Table counts reproduce as CALLER 26, INTEGRITY 59, NUMERICAL 20, PLANNING-INTERNAL 3, TYPED-OUTCOME 1, WRAPPER 3.
- Read-only simulation of `gen_string_field_registry.py` over V88 found 203 fields, no missing or stale classifications, and no declaration cross-check failure. That green result does not cure F2 or F5.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — ARRIVAL violates G3's exhaustive event partition

`LIFECYCLE_GUARANTEE_SPEC.md` line 36 says every touch event is exactly one touch's event or a refusal's event and that no event is neither. Lines 53–63 then introduce ARRIVAL as a second event class, and line 62 expressly says it is not a touch and satisfies no touch invariant. G4 at line 37 was reworded to count DECISION events, but G3 was not: every ARRIVAL is now precisely the event that G3 says cannot exist. The draft reproduces the same full G3 body at §6.1 line 631 and requires ARRIVAL at lines 632 and 702. This is a spec-level contradiction hidden by a byte-exact derivation checker: the checked quote is faithfully wrong.

Required repair: partition all event classes explicitly—ARRIVAL versus DECISION, with DECISION partitioned into touch/refusal—and re-derive G2/G3 and every consumer from that partition.

### F2 — HIGH — REPAIR-REQUIRED — ARRIVAL is outside §6.1's exhaustive non-χ schema

Section 6.1 lines 589–592 declares the non-χ-bearing schemas exhaustively. Item (ii)'s access-log event has `timestamp, actor, table row, operation, object identity, success/refusal, refusal reason, running chain digest`. Row B at line 702 defines ARRIVAL with a different closed body: `kind=ARRIVAL, timestamp, row, operation, object identity, request_key, running chain digest`. It adds `kind` and `request_key`, omits decision fields, and is neither item (i)'s slot receipt nor item (ii)'s stated event. Line 691 makes everything off the list χ-bearing by default. Therefore the pre-unblinding ARRIVAL records needed by recovery and gate readers are χ-bearing by the document's own bytes.

The generator's manually declared `arrival.*` rows (`gen_string_field_registry.py` lines 140–151, 279–280) do not widen §6.1's normative exhaustive list. The generated registry even labels those rows as `v9 SLOT_SCHEMA`, although frozen v9 contains no ARRIVAL schema.

Required repair: add ARRIVAL as an explicit authenticated non-slot event schema in the exhaustive list, with accurate provenance and value-domain enforcement.

### F3 — HIGH — REPAIR-REQUIRED — the supersession sweep leaves the retired no-arrival regime live

The supposedly swept lifecycle block still contains mutually exclusive regimes:

- Draft line 640 says death before any commit has “no event” and in the same sentence says the ARRIVAL event shows the request existed.
- Line 647 says the request identifier is internal and “not written to the access log,” while line 702 defines the on-chain `request_key` as that request's join identity.
- Line 648 says a request with no binding “never happened,” although arrival-without-terminal is now the ruled visible recovery state.
- Line 649 retains the old claim that decide/append death is indistinguishable from a request that never arrived; the preceding committed ARRIVAL is the distinguishing record.
- Line 652 says nothing above changes what the access log records beyond refusal reasons, directly contradicting the authorised second event class three lines earlier.
- The lifecycle spec's N2 row at line 70 calls ARRIVAL authorised in its body while its “why” cell still says the second event class is “not authorised, REFERRED,” contradicting line 176.

These are operative state, recovery, and authority rules, not harmless historical quotations. The label-bound lifecycle checker cannot see them, exactly as its lines 21–23 admit.

Required repair: replace the old request/recovery block and the complete N2 row from the new state machine; do not preserve predecessor assertions beside corrective tails.

### F4 — HIGH — REPAIR-REQUIRED — “exactly one terminal” is implemented as at-most-one

Row B line 702 claims every ARRIVAL joins exactly one terminal, then defines the verifier as: every arrival has **at most one** terminal naming it, and every terminal has exactly one prior arrival. An arrival with zero terminal events satisfies both predicates. The lifecycle spec produces exactly that state after death and delegates closure to deadline/recovery (lines 80, 97–111), but neither the join predicate nor a named gate says a post-deadline orphan arrival is rejected. `request_key = chain_position` prevents key reuse; it does not establish totality or one ARRIVAL per request.

Required repair: gates must distinguish a provably live, within-deadline pending arrival from an overdue orphan; every final/checkpoint-closed request must have exactly one terminal decision, and duplicate ARRIVALs for one request must be rejected.

### F5 — HIGH — REPAIR-REQUIRED — the ARRIVAL join verifier is absent from its own build item

Line 702 assigns the bidirectional ARRIVAL↔terminal check to the enumeration verifier. The actual required build contract at §11 lines 1529–1541 covers only `REFUSED-UNCLASSIFIED` emissions, enumeration entries, entry↔catch-all bijection, explanation/re-derivation references, and five consultations. It never mentions ARRIVAL, `request_key`, terminal bindings, duplicate arrivals, orphan arrivals, deadline closure, or the arrival→terminal relation.

This is the exact “claim without item” defect that lines 1529–1531 say the inventory exists to prevent. The registry note at `gen_string_field_registry.py` lines 147–150 asserts a verifier behavior but does not create a build obligation or fixture.

Required repair: put the complete arrival/decision bijection, deadline state, checkpoint coverage, and adversarial duplicate/orphan fixtures into the pinned verifier's §11 contract.

### F6 — HIGH — REPAIR-REQUIRED — BS-L's checkpoint cut is circular

Section 6.1 line 736 requires the pre-unblinding lock checkpoint immediately before canonicalizing BS-L; line 731 includes that checkpoint and its chain segment in BS-L's signed canonical body. But line 611 says issuance is one atomic commit whose own mediated write events are the last pre-partition events and whose checkpoint chain segment extends through issuance completion.

A checkpoint cannot both precede canonicalization and include the event caused by completing/writing the artifact whose signed body contains that checkpoint. Atomicity removes partial states; it does not solve self-reference. If issuance events are included, the signed body depends on its own issuance. If the checkpoint is truly pre-canonicalization, issuance events are post-cut and line 611's sealed-side claim is false.

Required repair: choose a non-circular cut—e.g. a signed pre-issuance checkpoint with issuance events in the authenticated continuation, or a separate post-issuance envelope binding the pre-issuance body and issuance event.

### F7 — MEDIUM — REPAIR-REQUIRED — the count-correction prose contradicts the generated history

Independent recounts of the actual drafts are V84=16/8, V85=17/8, V86=17/8, V87=16/9, V88=16/9. The generated §10 row at line 1113 correctly records V86→V87 as class-P 17→16 and class-E 8→9. Yet the live BS-SI row at line 934 says “THE COUNT MOVE IS CORRECTED: 16/8 → 16/9, not 17/8,” and the narrative in line 1113 repeats “16/9, not 17/8.” That denies the very predecessor count from which the generated row computes the move.

`prereg_counts.py` checks only the current table/count sentence, and `prereg_trace.py` compares generated trace cells, not the narrative embedded in the BS-SI row or repair prose. Their green outputs therefore do not reach this contradiction.

Required repair: state the actual move, 17/8→16/9, while separately explaining that 17/8 was the erroneous intermediate classification.

### F8 — MEDIUM — REPAIR-REQUIRED — two argument-validation raises are classified NUMERICAL against the ledger's own boundary

`ref/RAISE_SITE_CLASSIFICATION.md` line 7 defines CALLER as testing a property of an argument “as supplied” and NUMERICAL as testing a value computed from admissible data. In frozen v9, `accuracy_from_handcheck()` line 1458 converts supplied `n_counts` to `n`; line 1462 raises when that supplied array has an empty bin. Lines 1465–1468 convert supplied `epsilon_hat` to `eps` and raise when it is outside `[0, 0.5)`. The table marks both lines 1462 and 1468 NUMERICAL/soft (classification lines 113 and 115), even though each tests an input argument's admissibility before the function computes its result. By the document's own boundary they are CALLER, not numerical.

The classification header admits exactly this possibility—if the two soft sites are CALLER, NUMERICAL drops from 20 to 18—but §5 line 530 still presents 20 as the live classification. Honest uncertainty is not a classification.

Required repair: classify the two sites under the stated boundary and propagate the resulting totals/routing; if context can change their meaning, classify per call site rather than leaving one soft raise-level label.

## Failed attacks / verified survivals

- The exact subject, lifecycle spec, frozen v9, raise-table, registry, generator, and refusal-checker digests were recomputed; the named pins checked above held.
- The current §7 table and live count sentence genuinely close at 16 P / 9 E. F7 is the predecessor-transition narrative, not the current total.
- The refusal vocabulary's operative eleven-token set matches the checker; its rebuilt three-prong R03 fixture and all 34 controls pass. I found no second active retired token in the V88 bytes.
- The AST raise-line set closes exactly at 112 and matches every classification-table line. F8 concerns semantic class assignment, not missing rows.
- The frozen v9 dynamic-load construct remains at `_frozen_planner()` and is not name-call-graph reachable from `run_production_verdict`; I did not promote the known lower-bound limitation into a finding without a concrete verdict-path edge.
- The generator's current declared/extracted union has no missing or stale row and the generated registry reflects the ruled seed, generator, `n_draws`, and a-priori bound state. I did not re-report V87's repaired registry drift.
- The endpoint-ratification blocker and absent replay harness still prevent BS-3g discharge; per the brief's later explicit instruction, I did not re-derive the parked draw discipline.
- I did not re-report the parked logged-object leak, fault/tampering indistinguishability, durable pre-verdict-state history except where the newly authorised ARRIVAL directly contradicts live text, strata/producer question, VOID/numerical partition, per-call-site classification-unit defect, freeze-signature residue, `require_authorization`, or BS-3g lifecycle cycle.

## Evidence and custody

Content-read included the complete V88 draft, complete lifecycle spec, `ref/RAISE_SITE_CLASSIFICATION.md`, frozen `ref/successor_ref_v9.py` at the attacked raise sites and dynamic-load site, `tools/refusal_vocabulary_check.py`, `tools/lifecycle_derivation_check.py`, `tools/prereg_counts.py`, `tools/prereg_trace.py`, `tools/prereg_lint.py`, `tools/void_registry.py`, `ref/gen_string_field_registry.py`, `ref/STRING_FIELD_REGISTRY.md`, and the V87 referee reports. Executions were read-only; the registry generator was simulated in memory rather than run in its writing mode. The only intended file write is this report.

The brief's required block literally specifies `VERSION: V87` although the assigned subject and report path are V88. I preserve that mandatory control-plane token exactly rather than silently correcting it.


**CONTROL-PLANE CORRECTION (Hwao, 2026-08-30, V89 build).** The block below declared `VERSION: V87` because my brief's REQUIRED REPORT FORMAT carried that literal — the seat flagged the discrepancy in its own report and preserved the token rather than silently correcting my template. The token is corrected to `V88` here because two blocks declaring one (seat, version) key made citations resolve against the wrong report (prereg_lint caught it as two false FABRICATED verdicts). Findings, prose and verdict are untouched; the template itself is fixed in BRIEF_V89.
<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V88
VERDICT: NOT CLEAR
COUNT: 8
F1 | HIGH | REPAIR-REQUIRED | lifecycle spec §1 lines 36-37 and §1c lines 53-63; draft §6.1 lines 631-632, 702 | ARRIVAL is an event that is neither a touch nor refusal, violating G3's exhaustive event partition.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 589-592, 691, 702; gen_string_field_registry.py lines 140-151, 279-280 | ARRIVAL does not conform to the exhaustive non-chi access-log schema and therefore defaults chi-bearing.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 640, 647-652; lifecycle spec lines 70, 176 | The supersession sweep leaves live no-arrival assertions contradicting the authorised second event class.
F4 | HIGH | REPAIR-REQUIRED | §6.1 line 702; lifecycle spec lines 80, 97-111 | The stated join enforces at-most-one terminal, not the claimed exactly-one total treatment.
F5 | HIGH | REPAIR-REQUIRED | §6.1 line 702; §11 lines 1529-1541; gen_string_field_registry.py lines 147-150 | The claimed ARRIVAL-terminal verifier behavior is absent from the verifier's build contract.
F6 | HIGH | REPAIR-REQUIRED | §6.1 lines 611, 731, 736 | BS-L's signed checkpoint is required both before and through issuance, creating a circular cut.
F7 | MEDIUM | REPAIR-REQUIRED | §7 line 934; §10 line 1113 | Count prose says 16/8 to 16/9 although the actual and generated predecessor move is 17/8 to 16/9.
F8 | MEDIUM | REPAIR-REQUIRED | RAISE_SITE_CLASSIFICATION.md lines 7, 18, 113, 115; successor_ref_v9.py lines 1457-1468; §5 line 530 | Two supplied-argument validation raises are labelled NUMERICAL despite the ledger's own CALLER boundary.
<!-- END FINDINGS-BLOCK -->