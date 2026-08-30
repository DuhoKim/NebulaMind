# CODEX adversarial whole-document review — V112

## Verdict: NOT CLEAR

The subject digest matched the brief before the draft was read:
`22cf104327282adc4367b2f98b589ab4d2c89a3c3145a694743e46bbb671e1c7`.

V112 is not clear. The identity-envelope repair did not propagate into the generated string registry; the newly introduced ATTEMPT-CLOSE kind is neither closed-vocabulary nor domain-registered; and the generator advertised as preventing another non-χ integration lag is blind to deletion or field drift of VERIFICATION-BOUNDARY. The admission hold has no executable liveness consequence, the review object still has no representable authenticated envelope or evidence/roster contract, and the BS-3g text both omits a still-missing mapping from its blocker inventory and carries the superseded measurement-derived interpretation of the ratified a-priori range.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the generated registry restores the payload-digest oracle V112 says it killed

The companion spec at `LIFECYCLE_GUARANTEE_SPEC.md:73` and the draft at §6.1 Row B (`PREREG_SUCCESSOR_DRAFT_V112_20260830.md:713`) define `request_digest` as SHA-256 of only the domain-tagged identity envelope `(origin_row, frame_sequence, operation, object_identity)`. They explicitly exclude payload bytes and retire the wire-frame preimage.

The generated value-domain source says the opposite. `ref/gen_string_field_registry.py:224-227` still defines `arrival.request_digest` as SHA-256 of the “complete framed wire unit, domain-tagged wire-frame”; generated `ref/STRING_FIELD_REGISTRY.md:101` repeats that live rule. This is not harmless commentary: §6.1 lines 679-700 makes that registry the value-domain contract consumed by `receipt_strict()` and the successor verifiers, while §6.1 line 702 classes an opaque digest of χ-bearing bytes as χ-bearing by default.

Concrete break: two writes use the same envelope and different payloads. The spec/draft give them one request identity, but the generated registry gives them two identities and exports a confirmation oracle over each payload. Conversely, an implementation following the generated registry violates the claimed non-χ arrival schema while every current generator/check remains green.

Required repair: re-derive the registry source and output from the identity-envelope rule, delete the wire-frame semantics, and add a semantic control that flips the preimage class—not merely a field-name equality check.

### F2 — HIGH / REPAIR-REQUIRED — ATTEMPT-CLOSE is not a closed, domain-separated record kind

The pair-law repair in companion §3c T2 (`LIFECYCLE_GUARANTEE_SPEC.md:132`) and draft §6.1 lines 641 and 674 introduces the exact record `(kind, member_position, close_class, boot_epoch, monotonic_reading)` and says all four V112 checkpoint-family kinds are domain-tagged.

The referenced registries do not implement that statement:

- `ref/gen_string_field_registry.py:246-249` makes `vread.kind`, `vbound.kind`, and `attstart.kind` closed-vocabulary, but omits `attclose.kind`.
- `ref/gen_string_field_registry.py:258-265` instead classifies `attclose.kind` together with its clock integers as merely `bounded-encoding`.
- `ref/gen_domain_kinds.py:25-43` and generated `ref/DOMAIN_KINDS.md:5-29` register `attempt-start` but no `attempt-close` kind.

Thus an ATTEMPT-CLOSE body has no declared `NMPR1:<kind>` preimage domain and its `kind` field is not constrained to the ATTEMPT-CLOSE literal. The pair count can be fed a bounded arbitrary kind token, and the corpus-wide cross-kind-preimage claim is false for the record added by this revision.

Required repair: give ATTEMPT-CLOSE its own closed literal and domain kind, map its canonical body, regenerate both registries, and add deletion/stranger controls for this exact kind.

### F3 — HIGH / REPAIR-REQUIRED — the generated non-χ surface is mechanically blind to the V112 boundary record

V112 claims the hand-maintained integration lag is over: §6.1 line 674 says `ref/gen_nonchi_surface.py` makes a fifth omission impossible. The generator itself says FIELD ECHO covers restated rows (`ref/gen_nonchi_surface.py:18-22`). But its SURFACE row for `vbound` uses the generic probe `"(ii-g)"` and `restate=False` (`ref/gen_nonchi_surface.py:60-65`). Unlike the T1-T3 tuples, VERIFICATION-BOUNDARY is not a label-bound quotation from the companion spec; its only exact tuple is hand-written in the draft.

I exercised the actual checker in memory against the exact V112 bytes. Each of these mutations returned zero problems:

1. delete the whole phrase `the VERIFICATION-BOUNDARY record (kind, boot_epoch, monotonic_reading)`;
2. replace that tuple with `(kind, timestamp)`.

The `(ii-g)` label remains, so ADMISSION passes; `restate=False` suppresses FIELD ECHO; CLOSURE sees the registry prefix and passes. The checked-in `ref/NONCHI_SURFACE.md:22` even labels the row “quote-bound/no,” which is false of this draft-owned schema. The generator’s own four controls do not exercise this row.

Required repair: make `vbound` an exact unique admission probe with `restate=True`, or move the tuple to a genuinely label-bound single source and cross-check it there. Add deletion, rewording, and field-drift controls for all non-T `restate=False` rows. The brief’s “surface registry 19 rows” should also be reconciled with the generated file’s actual 18 rows (`ref/NONCHI_SURFACE.md:28`).

### F4 — HIGH / REPAIR-REQUIRED — the admission hold has no executable bound or failure consequence

The V112 §11 verifier contract (`PREREG_SUCCESSOR_DRAFT_V112_20260830.md:1564`) makes a pass boundary Row B’s last ordinary append until the gate action, moving all new requests into W0 wire residue. It says the hold is “bounded by the BS-2k GATE-PASS BUDGET, a stated design obligation with its fixture.” That is the entire liveness mechanism: there is no authenticated budget field, supervisor, timeout transition, abort rule, or named consequence if the verifier does not finish. The companion lifecycle spec contains no VERIFICATION-BOUNDARY, gate-pass-budget, or admission-hold rule at all.

Concrete break: the verifier appends its boundary and then deadlocks. No ordinary ARRIVAL may commit, so the waiting frames remain pre-arrival wire residue and their request deadlines never start. No later sequence event forces expiry, the pass never reaches its gate action, and the asserted bounded hold is infinite. Repeated termination aborts can produce the same starvation because “re-boundary after it” has no attempt cap.

A fixture can show one implementation usually returns; it cannot make the universal bound true. Required repair: put the hold budget and its enforcement in the normative lifecycle/BS-2k schema, name the watchdog authority and atomic release/abort transition, specify the failure outcome, and give a total bound across retries and consecutive gates.

### F5 — HIGH / REPAIR-REQUIRED — the signed REVIEW RECORD has no representable authenticated envelope on the closed surface

Draft §6.1 line 614 calls the review record’s schema exactly nine fields:
`(kind, reviewer_identity, review_timestamp, review_disposition, evidence_ref, reviewed_chain_position, reviewed_event_digest, reviewed_class_key, first_opening_digest)`.
It then says “the whole” is under a reviewer’s 64-byte detached deterministic signature. The exhaustive admission at line 676 repeats the same nine fields while claiming the artifact carries a roster-bound HUMAN signature.

No signature exists in the actual registry or surface. `ref/gen_string_field_registry.py:228-245` / `ref/STRING_FIELD_REGISTRY.md:221-229` enumerate the nine body fields only. The generic signature set at `ref/gen_string_field_registry.py:463` covers freeze, BS-L, opening, explanation, and checkpoint signatures—not review. `ref/NONCHI_SURFACE.md:25` likewise has no signature field/envelope row. This differs from terminated-family records, whose detached signatures are explicitly registered at `ref/gen_string_field_registry.py:286-288`.

Therefore the exact closed artifact is either unsigned, contradicting the verifier contract, or gains an undeclared tenth leaf/envelope, making it χ-bearing by §6.1’s default. Required repair: specify the detached review-signature envelope as an exact authenticated schema, admit it to the non-χ surface, value-domain it, and make the verifier consume those exact bytes.

### F6 — MEDIUM / REPAIR-REQUIRED — evidence_ref and the reviewer roster do not bind an evidentiary adjudication

The V112 body now names the exact mismatch emission, which closes V111’s reuse defect. It does not define what `evidence_ref` must resolve to or how the evidence must relate to that emission. The generated domain map explicitly classifies `revrec.evidence_ref` as raw arbitrary “evidence artifact bytes” (`ref/gen_domain_kinds.py:58`; `ref/DOMAIN_KINDS.md:81`), and its registry row has an empty semantic note (`ref/STRING_FIELD_REGISTRY.md:221`). One empty or unrelated artifact can therefore serve every review while all position/digest/class/chain checks pass.

The same paragraph introduces a “REVIEWER ROSTER — a BS-2k-committed artifact” but gives it no closed schema, signer/authority, canonical digest preimage, producer, or §11 build item. A machine-domain commitment to a list of alleged humans does not establish who authorized the list or whether the roster signer is entitled to add itself.

Required repair: either state that the human disposition is pure testimony and remove the evidentiary overclaim, or define a closed evidence artifact that names the emission and is checked in both directions. Separately define and authenticate the reviewer-roster body and its authority chain, and wire both into the §11 verifier item.

### F7 — HIGH / REPAIR-REQUIRED — BS-3g still lacks the executable mapping that its blocker inventory says is no longer open

The §7 BS-3g row at line 922 says the draw set is derived and “what remains open is the harness pin,” but the same row keeps `mapping_id = MAPPING-NOT-PREREGISTERED` and says “a mapping family is not a preregistered mapping.” §11 lines 1295-1298 and 1475-1479 state that this literal cannot discharge BS-6. The replay contract at lines 1379-1387 invokes no mapping callback and says a future mapping must enter as a pinned module; no such module exists.

The ratification record compounds the false inventory: `GAMMA_RATIFICATION_20260830.md:19-21` says the only remaining emission preconditions are the replay-harness digest and BS-SI schema. But without a pinned executable mapping, `gain_counterfactual_path.py` refuses at its `mapping is None` guard, and the prescribed harness cannot produce any conforming draw matrix.

This is not an objection that the draft is unfinished; it is a contradiction about which unfinished work blocks the slot. Required repair: restore “pinned executable mapping + identity/digest + harness integration” to every blocker inventory and §11 build list, or provide the mapping artifact and its exact verifier contract.

### F8 — HIGH / REPAIR-REQUIRED — the a-priori γ ruling still inherits the superseded measurement-derived guarantee

V112 correctly says at lines 1236 and 1299-1303 that Γ = 0.25 is an A-PRIORI FROZEN RANGE, not the old `|γ̂| + kσ` measurement-derived bound, and marks the old formula as history at lines 1308-1325. But the live composition immediately after that history reactivates its conclusion:

- lines 1326-1333 say “The bound statement places the TRUE gradient inside” the range “with stated confidence, under its three named conditions”;
- line 1330 says HELD asserts that “the systematic which actually exists cannot have flipped” the verdicts;
- line 1306 still says the bound’s origin is “the measurement itself plus a frozen constant.”

Those are the old estimator-bound semantics. Ratifying a threat-model endpoint does not itself place the unknown true gradient inside it with confidence. The proposal’s actual argument is different and conditional (`PROPOSAL_GAMMA_RANGE.md:29-33`): if |γ| exceeds 0.25 and calibration fails to catch it, the sweep does not cover it.

Concrete break: true |γ| = 0.30, the calibration gate misses it, and every evaluated point in [-0.25,+0.25] preserves the categorical verdict. The receipt conformingly reports HELD, while the actual systematic outside the grid flips the verdict. The current live sentence calls that impossible; the proposal expressly names it as residual.

Required repair: state HELD only conditionally—no evaluated-grid flip given |γ_true| ≤ 0.25 and the calibration/threat-model assumptions—and replace the stale “three conditions” with the a-priori range’s actual calibration conditions. Do not claim a confidence bound unless its confidence construction is specified.

## Attacks that held

- Target SHA-256, lifecycle-spec pin, refusal-checker pin, and frozen-v9 pin all matched their stated bytes.
- `tools/prereg_lint.py` exited 0 with 97 legacy advisories and 0 blocking findings; counts were 16 class P / 9 class E.
- `ref/gen_nonchi_surface.py --check` was byte-equal with 0 reported problems; its self-test was 4/4. Those green results are evidence for the narrow tested shapes, not answers to F2/F3.
- `tools/refusal_vocabulary_check.py` reported 0 problems and its 43-control self-test passed. Its documented semantic-reactivation limit remains real; I found no additional live refusal code to score beyond the parked leaks.
- The pair-law crash attacks held under the text as written: an `ABORTED` close ends that attempt; a committed decision closes a successful attempt; and a dangling start is closed `ABORTED-BY-RESTART` before the next start. I do not re-score the explicitly named testimony-plus-fixture residue.
- The 51-point grid [-0.25,+0.25], Δγ = 0.01, j0 = 25, n_draws = 99, zero-based addressing, and common-random rule agree across the draft, ratification, and draw-mechanics commitment. F7/F8 concern executable completeness and claim semantics, not this arithmetic.
- The raise-site ledger’s table counts close at 112 Raise nodes plus one production assert; the already parked per-call-site limitation was not re-derived.
- The oldest-quiet §2.2 cut list held against the hash-verified predecessor blobs: all eight predicates and the absence of a surface-brightness cut agree.

## Evidence and scope

Read in full: the brief, exact V112 draft, `LIFECYCLE_GUARANTEE_SPEC.md`, `ref/RAISE_SITE_CLASSIFICATION.md`, `tools/refusal_vocabulary_check.py`, `ref/gen_nonchi_surface.py`, `ref/NONCHI_SURFACE.md`, relevant regions of `ref/gen_string_field_registry.py`, `ref/STRING_FIELD_REGISTRY.md`, `ref/gen_domain_kinds.py`, `ref/DOMAIN_KINDS.md`, the γ proposal/ratification/draw commitment, and the terminal-signature ruling. I also checked the frozen v9 digest and relevant source regions, ran the lint and the two requested checker batteries read-only, and exercised the surface checker with in-memory adversarial mutations. I did not modify the draft, companion, tools, registries, or any artifact outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V112
VERDICT: NOT CLEAR
COUNT: 8
F1 | HIGH | REPAIR-REQUIRED | §6.1 L713 / spec §1c L73 / registry L101 | Generated registry still defines request_digest over the χ-bearing complete wire frame, contradicting the identity-envelope-only repair.
F2 | HIGH | REPAIR-REQUIRED | §6.1 L641,L674 / gen_string_field_registry L246-L265 / DOMAIN_KINDS L5-L29 | ATTEMPT-CLOSE has neither a closed kind literal nor a registered domain-separated canonical-body kind.
F3 | HIGH | REPAIR-REQUIRED | §6.1 L674 / gen_nonchi_surface L37-L68,L83-L121 | Surface generator accepts deletion or field drift of VERIFICATION-BOUNDARY because its generic probe is restate=False.
F4 | HIGH | REPAIR-REQUIRED | §11 L1564 / companion spec | Admission hold can persist forever because the gate-pass budget has no normative enforcement actor, timeout transition, or failure consequence.
F5 | HIGH | REPAIR-REQUIRED | §6.1 L614,L676 / registry L221-L229 | REVIEW RECORD requires a detached signature that is absent from its exact schema, exhaustive surface, and value-domain registry.
F6 | MEDIUM | REPAIR-REQUIRED | §6.1 L614 / §11 L1552-L1564 / DOMAIN_KINDS L81 | evidence_ref is unrelated raw bytes and the reviewer roster has no authenticated schema or authority chain.
F7 | HIGH | REPAIR-REQUIRED | §7 L922 / §11 L1295-L1298,L1379-L1387,L1475-L1479 | BS-3g blocker inventory omits the still-missing executable preregistered mapping required to produce a conforming receipt.
F8 | HIGH | REPAIR-REQUIRED | §11 L1299-L1333 | A-priori gamma range is still used as if it confidence-bounded the true gradient, so HELD overclaims actual-systematic robustness.
<!-- END FINDINGS-BLOCK -->