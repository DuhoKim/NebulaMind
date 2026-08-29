# V67 whole-document adversarial review — CODEX

**VERDICT: NOT CLEAR.** The subject digest matched the brief exactly. Mechanical inventories reproduce, but the central V67 repairs remain breakable: resolve–append–release cannot atomically guarantee a truthful sole event, the off-log request ID does not make recovery idempotent, the refusal-enumeration mechanism has neither an authenticated object nor a stable recurrence identity, a conforming `FAILED` BS-3g receipt is not prevented from discharging the gate, the stated grid rules are not enforced by the verifier, and Row F has neither a legal producer nor a typed separation for its new χ-bearing input.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — resolve–append–release cannot preserve truthful outcome, no under-reporting, and one event

V67 §6.1 lines 619–622 makes resolution precede the event append: a read is performed or a write is staged, then the sole event is appended, then bytes are released or the write is committed. This does not establish the claimed atomic boundary.

For a read, Row B's table at line 654 defines touching sealed-store bytes as the logged act. Step (1) has already read those bytes. A crash before step (2) therefore leaves a real sealed-store touch with no event, contrary to line 621's claim that the touch “did not happen” and that the log can never under-report. For a write staged outside the destination, staging success does not establish that the later destination commit succeeds: append `COMPLETED`, then let commit fail, and the event is false. If staging writes into a non-transactional destination, durable bytes can precede the append. Line 626 then says a request dying in `TRANSFER` is completed as `FAILED`, but the append-only one-event contract supplies no event in which to record that post-append change.

A concrete atomic transaction/recovery construction must bind source read or destination commit to the event append. Ordering prose alone cannot simultaneously guarantee a true terminal outcome, no unlogged store touch, and exactly one event.

### F2 — HIGH / REPAIR-REQUIRED — the off-log request ID is not atomically bound to the event

Lines 623–625 assign an internal request identifier, keep it in recovery state, and expressly omit it from the access log. No atomic binding is specified between that state and the append.

Counterexample: request R's event becomes durable, then Row B crashes before its separate recovery state records that R owns that chain position. On restart, `(actor,row,operation,object)` is non-unique because repeated touches and legal retries are expected. Reprocessing R appends a second event for one request; treating a matching tuple as R can instead suppress a later legal request. Serialization and lease loss prevent concurrent writers, not this crash boundary. The authenticated event must carry the request identity, or a durable idempotency index must be atomically committed and bound to the event digest/chain position.

### F3 — HIGH / REPAIR-REQUIRED — the named enumeration verifier has no authenticated enumeration object or implementation obligation

Lines 599 and 604 require one enumeration entry per catch-all emission and say every event carries one, but the closed access-log schema at lines 586–590 has no enumeration-entry field or reference. The draft defines no separate entry schema, canonical serialization, producer, identity/join key, signature, or authenticated chain-entry type. The phrase “named and separately pinned” at line 604 names no symbol, file, or digest, and §11 contains no code-side item requiring the verifier, its schema, fixtures, or its two gate invocations.

The on-disk search found no enumeration-verifier implementation. `tools/refusal_vocabulary_check.py` does not establish one: R08 at checker lines 155–161 only regex-matches the phrase `enumeration verifier` and evidence that it is “consulted twice.” Its clean result therefore accepts prose with no verifiable bytes. A nominal verifier can accept an unauthenticated side table, a blank explanation, or a producer summary. Until the enumeration object, custody, join, producer, verifier, and both invocations are specified and required in §11, the P6/P7 block is not executable.

### F4 — HIGH / REPAIR-REQUIRED — recurrence can be defeated by relabelling because “same class” has no frozen identity

Line 600 says explanation ceases to discharge “the same class” when it recurs, but no equivalence rule or machine-computed class key defines sameness. Line 599 permits a person to name or explain each entry.

The same verifier timeout can recur every run while being labelled `timeout/request-17`, `timeout/request-18`, or with slightly different prose. Every event remains individually enumerated, no formally identical class recurs, and the vocabulary is never re-derived. The checker is weaker still: R09 at line 162 only searches the entire draft for `recur`, so unrelated historical prose can satisfy it. The rule needs a preregistered, verifier-enforced equivalence key independent of object, request, run, and human wording, plus the history over which recurrence is tested.

### F5 — HIGH / REPAIR-REQUIRED — a valid `FAILED` BS-3g receipt is not prevented from filling the slot and opening BS-6

The BS-3g row at line 846 says the slot binds an acceptance rule and failure consequence and blocks BS-6. Lines 1142 and 1195–1199 define a detected verdict flip as the valid token `FAILED`; lines 1216–1222 require the verifier to accept that classification when any matrix cell differs from `baseline_verdict`. But lines 1227–1229 block BS-6 only when the verifier refuses and no receipt is emitted. They do not say that a conforming receipt whose authenticated `invariance_outcome` is `FAILED` leaves BS-3g unfilled or keeps the edge shut.

Thus the worst possible scientific result can produce a schema-valid, verifier-valid receipt and discharge a class-P slot whose existence is supposed to gate that result. The acceptance rule must state and enforce that only the designated passing outcome can fill BS-3g; `FAILED` must have an explicit terminal consequence and must not discharge BS-6.

### F6 — HIGH / REPAIR-REQUIRED — the BS-3g verifier does not enforce the manifest's endpoint, distinctness, or Δγ rules

Lines 1136–1143 normatively require both endpoints, at least three distinct values, and maximum spacing `Δγ`. The concrete checks at lines 1138–1139 require only `max|γ| >= gamma_bound` and rejection of singleton `{0}`. A manifest `[0, +gamma_bound, +gamma_bound]` has length three, reaches the bound, and is not `{0}`, yet lacks the negative endpoint and has only two distinct values. The independent-verifier checklist at lines 1210–1226 recomputes the manifest digest and length but never adds exact endpoint, uniqueness, or adjacent-gap checks.

`Δγ` is also absent from the exact seventeen-field schema at lines 1100–1104, and no verifier clause binds the manifest to the frozen value. After the currently honest blockers are filled, a nonconforming grid can therefore pass the specified machine checks and report `HELD` at a resolution it did not evaluate. Bind the frozen spacing unambiguously and require the verifier to validate finite sorted unique points, both exact endpoints, at least three distinct values, and every adjacent gap.

### F7 — HIGH / REPAIR-REQUIRED — Row F's new χ-bearing stratum input has no authorised producer and no enforced bin/allocation separation

Row F at line 659 now consumes a per-object HC stratum index for allocation, and §6.3 lines 725–741 says that index is machine-committee state × |χ| tertile. No covenant row produces that object. Row D emits only the primary instrument's χ/sign/amplitude/confidence receipts (line 657); no authorised row runs the additional classifiers needed for machine-committee state or writes a canonical stratum-assignment artifact. `successor_ref_v9.py` confirms the missing path: `allocate_handcheck(cell_counts, budget)` accepts an already-built 3×9 matrix, but no production function computes the HC strata. Because the table is exhaustive, an unnamed producer falls to Row R and is forbidden.

The promised separation is also not enforced. Row F possesses both position values and the χ-bearing numeric index, while `calibration_bins(c)` accepts an untyped numeric array. Executing the pinned function on repeated stratum indices `0..8` succeeds and returns boundaries `[3.0, 6.0]`; there is no type or capability barrier proving which numeric array reached bin construction. The repair needs an authorised producer plus authenticated schema and typed/capability-separated interfaces that make the allocation input impossible to pass to `calibration_bins()`.

### F8 — LOW / REPAIR-REQUIRED — two live clauses still invoke the freeze-time enumeration mechanism V67 declares impossible

Lines 597–605 correctly say freeze-time enumeration cannot police run-time emissions and move checks to BS-L and opening. Yet line 612 says “the freeze-time enumeration surfaces it,” and line 626 says “the freeze-time enumeration required above” keeps undecided permission visible. These are live maintenance and terminal-treatment clauses, not clearly quarantined history, and there is no such requirement “above.” Replace both with the continuous run-time enumeration/verifier mechanism. The checker's narrow R06 regex misses this direct contradiction.

## Failed attacks and verified holdings

- Subject SHA-256 matched exactly: `3dbf4af7fab34e1f58477fffb92fcc4af40a4ceb9ed21d61f8063469f9e7c0e8`.
- `ref/successor_ref_v9.py` matched its pin `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; AST recomputation found 112 raise nodes, and `ref/RAISE_SITE_CLASSIFICATION.md` reproduced 25 CALLER / 60 INTEGRITY / 20 NUMERICAL / 1 PLANNING-INTERNAL / 3 TYPED-OUTCOME / 3 WRAPPER.
- `tools/refusal_vocabulary_check.py` matched the draft's digest `f74040dc8c98b7c3a70c3970006772fd20961c65472d9a782338fc81acf6dcf3`; its live check returned 0 problems and its self-test returned 15 controls, 0 failures. F3/F4/F8 concern what those phrase-based controls do not establish.
- The eleven formatted refusal codes match the checker's exact set; no different leak was established beyond F3's unconstrained enumeration object. I did not re-find the parked logged-identity membership leak.
- `prereg_counts.py` reproduced 16 class P / 8 class E. `prereg_trace.py` reproduced 66 transitions / 0 problems. `prereg_lint.py` exited 0 with 97 advisory / 0 blocking findings. `void_registry.py` self-test returned 6 controls / 0 failures.
- The currently stated BS-3g emission blockers are honest: `n_draws`, `draw_master_seed`, and `Δγ` are unset and the generator set is empty. No present emission path survives those blockers. F5/F6 attack the eventual consequence and verifier after values are filled.
- V67 correctly narrows `HELD` to no flip found on the evaluated grid. I do not re-find the V66 universal-invariance overclaim.
- No genuinely new VOID/numerical-partition break was established beyond the brief's parked/referral cases. Misconduct conditions remain `Any`.
- `UNREACHABLE-BY-CONSTRUCTION` is assigned to no raise site; the V43 in-run rerun allowance remains deleted; the class counts no longer assume 15/8.
- KIMI-V11 F7 was checked against its report and does not support the Stage-P implementation claim; V67 correctly records the V42 substitution as wrong.

## Evidence ledger and scope

Read in content: the governing brief; all 1,244 lines of V67; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; targeted source regions of `ref/successor_ref_v9.py`; `tools/refusal_vocabulary_check.py`; `FINDING_ROW_F_STRATA.md`; and, only after the independent attacks above were formed, the same-order GPT56 report as non-binding corroboration.

Executed read-only checks: subject/reference/checker SHA-256; AST raise-node and classification recount; refusal-vocabulary live check and self-test; prereg counts; prereg lint; prereg trace; VOID-registry self-test; targeted source searches; and a direct `calibration_bins()` wrong-input probe. I did not modify the draft, reference code, tools, or any file outside this report. Parked findings named by the brief were not re-derived.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V67
VERDICT: NOT CLEAR
COUNT: 8
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 619–622, 626, 654 | Resolve-before-append can under-log a completed sealed-store read, while append-before-commit can falsely report a write or let bytes precede the event.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 623–625 | An internal request ID omitted from the event has no atomic event binding, so recovery can duplicate one request or suppress a legal retry.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–590, 599, 603–605; §11; checker lines 155–161 | The enumeration verifier has no authenticated entry schema, producer, join, implementation item, or executable gate wiring; the checker verifies only phrases.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 599–600; checker line 162 | “Same class recurs” has no frozen equivalence key, so routine catch-all failures can be relabelled into formally distinct classes forever.
F5 | HIGH | REPAIR-REQUIRED | §7 line 846; §11 lines 1142, 1195–1199, 1216–1229 | A verifier-valid `FAILED` BS-3g receipt is not prevented from filling the slot and discharging the BS-6 edge.
F6 | HIGH | REPAIR-REQUIRED | §11 lines 1100–1104, 1136–1143, 1210–1226 | BS-3g's verifier does not enforce both endpoints, distinct points, or maximum spacing Δγ, and Δγ is absent from the receipt binding.
F7 | HIGH | REPAIR-REQUIRED | §6.1 lines 657, 659; §6.3 lines 725–741; successor_ref_v9.py lines 1359–1378 | Row F admits a χ-bearing stratum index that no authorised producer creates, and no typed boundary keeps it out of calibration_bins().
F8 | LOW | REPAIR-REQUIRED | §6.1 lines 597–605, 612, 626 | Two live clauses still invoke impossible freeze-time enumeration after the mechanism expressly moved to run-time gates.
<!-- END FINDINGS-BLOCK -->
