# V68 whole-document adversarial review — GPT56

**VERDICT: NOT CLEAR.** The pinned subject digest matches and the mechanical inventories reproduce, but the two central V68 mechanisms still fail adversarial construction. The atomic-touch promise cannot atomically include delivery to an external requester, and its own TRANSFER terminal rule assumes an event that the atomic contract says cannot yet exist. The enumeration repair also computes its class key from a lifecycle field absent from the closed event schema, has no machine-verifiable binding from `NAMED-AS-DEFECT` to an actually re-derived vocabulary (or from `EXPLAINED` to an authenticated explanation), and cannot enforce its expressly cross-run recurrence rule because both verifier consultations see only the current chain.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the atomic domain cannot include successful delivery of read bytes to an external requester

Section §6.1 lines 622–624 makes a read's “bytes leaving the store,” its event, and its request binding one atomic commit and concludes that a committed touch carries its true outcome. Row B at line 657 is not merely a database reader: it “conveys bytes” to the requesting row. Delivery to that requester is an external effect and cannot be rolled back with the store/log transaction.

Counterexample: Row B commits the store read, event and binding, then the IPC/socket/interface delivery to Row D or Row G fails or Row B crashes before the requester receives the last byte. The chain now contains a committed success and recovery will never re-decide the request, but the requester received no complete object. If delivery occurs before commit instead, the requester can receive bytes and the transaction can later abort, leaving exactly the unlogged read the repair claims impossible. Calling “bytes copied into Row B's private buffer” the store effect does not close the request lifecycle: it merely restores V67's admitted over-report window under a narrower definition of touch.

The contract needs an explicit external-delivery/acknowledgement protocol and a truthful event meaning (for example, committed-to-mediator versus acknowledged-to-requester); a local transaction cannot make remote observation atomic.

### F2 — HIGH / REPAIR-REQUIRED — the TRANSFER death rule contradicts the atomic commit boundary

Lines 618 and 629 say a request reaches `TRANSFER`, then ends `COMPLETED` or `FAILED`, and that a request dying in `TRANSFER` “has a verdict already durably logged” and is completed as `FAILED`. But lines 620–623 say the event is the verdict and is committed atomically with the store effect. Before the store effect commits, the sole event cannot already be durable; after it commits, the touch is no longer an in-flight transfer under the stated atomic model.

Concrete write counterexample: authorization succeeds, the request enters `TRANSFER`, and the writer dies while producing/staging the payload but before the atomic store/log/binding commit. The atomic contract requires no effect, no event and no binding. Line 629 requires an already logged verdict and a `FAILED` treatment. Emitting a pre-transfer event to satisfy line 629 recreates V66's false-outcome defect; emitting a second failure event violates exactly one event per touch. The same contradiction applies to a read interrupted before the atomic effect.

This is not the parked invisible pre-verdict residue alone: the live lifecycle expressly assigns a terminal logged treatment at a boundary where the new atomic contract forbids the asserted log state.

### F3 — HIGH / REPAIR-REQUIRED — `class_key` cannot be recomputed from the access-log event schema

Section §6.1 line 601 defines `class_key = (table row, operation, lifecycle state at failure)` and asserts all three are fields the event already carries. The closed BS-2k event schema at line 589 contains timestamp, actor, table row, operation, object identity, success/refusal, refusal reason and running chain digest. It does **not** contain lifecycle state at failure.

The enumeration verifier at lines 605–607 is required to recompute every key from the chain itself and never trust a producer summary. That is impossible from these bytes: two events identical in every logged field but failing in `PENDING-AUTHORISATION` versus `PENDING-SURFACE-CHECK` have different normative keys and indistinguishable chain records. Adding lifecycle state only to the off-chain enumeration entry does not help because the verifier must reject, rather than trust, its stored key.

The event schema must authenticate the lifecycle state (with a closed state vocabulary), or the class key must be redefined entirely over fields the chain actually carries.

### F4 — HIGH / REPAIR-REQUIRED — both enumeration dispositions can discharge without establishing what their names claim

The exact enumeration-entry fields at line 607 are `chain_position`, `event_digest`, `class_key`, `disposition`, `explanation_ref`, and enumerator signature. For a recurrence, line 601 says a second `EXPLAINED` is refused and demands `NAMED-AS-DEFECT` **and vocabulary re-derivation**. But the entry carries no new refusal code, vocabulary version/digest, or binding showing that the re-derived vocabulary names this class; the verifier's stated duties recompute emissions and keys, not the vocabulary change. A human can therefore set `disposition = NAMED-AS-DEFECT`, sign the entry, leave all eleven refusal codes unchanged, and pass the specified machine checks. The catch-all remains routine while wearing the required token.

The first-occurrence route is similarly underbound: `explanation_ref` is only an identifier. No canonical explanation schema, explanation-body digest, signer identity/authorization rule, existence check, signature verification duty, or minimum assertion is defined. An `EXPLAINED` entry can point to a nonexistent or irrelevant signed object and still satisfy every verifier behavior stated in lines 605–607.

A disposition is a claim, not evidence. `NAMED-AS-DEFECT` must bind to and verify the new vocabulary bytes/code that name the computed class; `EXPLAINED` must bind to an authenticated explanation body under a specified schema and verifier.

### F5 — HIGH / REPAIR-REQUIRED — the verifier has no cross-run history with which to enforce the recurrence rule it states

Line 600 defines the motivating failure explicitly across runs: “A class that fires every run can be explained every run,” and says recurrence stops explanation from discharging it. Lines 605–607 consult the verifier at BS-L and opening over “the chain as it stands at that moment”; entries live in this run's lock-checkpoint materials. No prior-chain digest, prior enumeration registry, vocabulary-maintenance ledger, or historical class-key set is an input to either consultation.

Counterexample: one catch-all class occurs exactly once in each study run. Each run's chain contains one instance, so its sole entry may be `EXPLAINED`; the verifier sees no second key in that chain. At the next run the chain and checkpoint materials are new, so the same class is again a first occurrence. The class fires every run and is explained every run — the exact evasion line 600 says is forbidden — while every specified current-chain check passes.

If “recurrence” is intended only within one chain, line 600's cross-run closure claim is false. If it is intended across runs, the verifier needs an authenticated, freeze-bound history input and a rule for continuity across preregistrations.

## Failed attacks / checks that held

- Subject identity held: sha256 recomputed before reading as `010f5ece044e67a1928f2182f8df29dc1c68cb1b96f085cac332b7f376cec9a7`.
- The §0 reference pin held: `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- The checker digest quoted at §6.1 line 615 held: `tools/refusal_vocabulary_check.py` recomputed to `9586e207f20141fde3d0f87f86d23cd2c84913934c7493161cfed0efb759d2e3`.
- `tools/refusal_vocabulary_check.py` exited 0 on V68; its self-test reported 17 controls, 0 failures, every code controlled. F3–F5 attack semantics its regex controls do not establish, consistent with the tool's own lines 30–33 limit.
- The eleven formatted refusal codes match the checker's exact set. I found no different leak beyond the parked availability/object-identity issues.
- The V68 BS-3g field count is 18 and the prose now states both endpoints, at least three distinct values, adjacent spacing bounded by frozen Δγ, field equality, and discharge only for `HELD`. The slot remains honestly blocked by unset `n_draws`, unset `draw_master_seed`, unset Δγ and an empty generator set; I found no current emission path through those blockers.
- The Row F producer gap is now explicitly filed and blocking. The recomputation predicate correctly protects the actual boundary values against a harmful alternative input: a stratum-contaminated transformation that happens to reproduce exactly the full-set boundaries has no downstream boundary effect, while changed boundaries are refused.
- `ref/RAISE_SITE_CLASSIFICATION.md` parses to 112 rows with 25 CALLER, 60 INTEGRITY, 20 NUMERICAL, 1 PLANNING-INTERNAL, 3 TYPED-OUTCOME and 3 WRAPPER. The draft no longer assigns `UNREACHABLE-BY-CONSTRUCTION` to any site.
- Mechanical checks held: `prereg_counts.py` reported 16 class P / 8 class E and prose match; `prereg_trace.py --check` reported 67 transitions and 0 problems; `prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; `void_registry.py` found 54 antecedents and its self-test reported 6 controls, 0 failures.
- The V43 in-run rerun allowance remains deleted. The numerical VOID antecedents remain post-unblinding, while forbidden-act, protocol-deviation and digest-deviation remain `Any`.

## Evidence ledger and scope

Content read:

- `gates/BRIEF_V68_REVIEW.md`
- `PREREG_SUCCESSOR_DRAFT_V68_20260829.md` (all 1,276 lines)
- `gates/V67_WHOLE_REVIEW_GPT56.md`
- `ref/RAISE_SITE_CLASSIFICATION.md`
- targeted regions of `ref/successor_ref_v9.py`
- `/Users/duhokim/NebulaMind/NebulaMind/tools/refusal_vocabulary_check.py`

Commands/checks executed:

- `shasum -a 256` on the subject, pinned reference, raise-site classification and refusal checker.
- `git diff --no-index` for V67→V68.
- refusal-vocabulary live check and self-test.
- prereg counts, lint and trace check; VOID-registry live check and self-test.
- programmatic recount of the raise-site classification table.
- targeted searches for atomic delivery/commit boundaries, event-schema fields, recurrence history, enumeration disposition bindings, BS-3g verifier constraints and Row-F recomputation language.

I did not modify the draft, reference code, tools, or any file other than this report. Parked findings named by the brief were not re-derived.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V68
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 622–624, 657 | A local store/log transaction cannot atomically include delivery to an external requester, so either a committed success can deliver nothing or bytes can escape before an aborted commit.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 618, 620–623, 629 | A request dying in TRANSFER cannot both have the already-durable verdict line 629 requires and obey the new rule that the sole event commits only with the store effect.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 589, 601, 605–607 | The class key requires lifecycle state at failure, but the closed event schema does not carry that field, so the verifier cannot recompute the key from the chain.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 600–601, 605–607 | `NAMED-AS-DEFECT` is not bound to an actually re-derived vocabulary, and `EXPLAINED` is not bound to a verifiable explanation, so either token can discharge an unsupported claim.
F5 | HIGH | REPAIR-REQUIRED | §6.1 lines 600, 605–607 | The rule forbids a class explained once per run, but both verifier passes inspect only the current chain and bind no prior class-key history, so cross-run recurrence is invisible.
<!-- END FINDINGS-BLOCK -->