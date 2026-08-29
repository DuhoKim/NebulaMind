# V66 whole-document adversarial review — CODEX

**VERDICT: NOT CLEAR.** The pinned subject digest matches and the mechanical inventories reproduce, but the V66 repairs do not close the request lifecycle or the catch-all gate. The sole pre-transfer event cannot represent a later transfer failure; recovery has no stable request identity with which to enforce no-redecision; a post-BS-L catch-all event reaches opening without any named verifier consulting it; and even an enumerated catch-all can become routine without violating the stated rule. Separately, the BS-3g endpoint-spanning manifest still does not establish invariance over its claimed bound, and §5 retains a false planning-site classification.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — one pre-transfer event cannot truthfully carry the terminal transfer outcome

Row B appends exactly one event per touch, classified as success or refusal (§6.1 line 645). The lifecycle nevertheless has an authorised request enter `TRANSFER` and finish `COMPLETED` or `FAILED` (line 611), while the only event must be durably appended before any read byte is released or any write byte is committed (line 614). Line 617 then says a transfer that dies is completed as `FAILED` under an availability code.

Counterexample: Row B authorises a read, appends its sole event, releases a prefix of a multi-byte payload, and the transport fails. At append time the terminal result is unknowable. If the event says success, it is false; if it records only the permission verdict, it does not conform to the stated success/refusal terminal schema; if Row B appends the later availability-coded failure, it violates the one-event rule. A write whose store commit fails after the pre-commit append has the same shape.

The admitted possibility of over-reporting a touch (line 614) does not repair the distinct promise that every state has one logged terminal treatment. Permission decision and transfer completion are two state transitions. The contract needs two authenticated event classes or must narrow what its sole event claims.

### F2 — HIGH / REPAIR-REQUIRED — recovery cannot enforce “never re-decided” because the log schema has no stable request identity

The access-log schema is closed at timestamp, actor, row, operation, object identity, success/refusal, refusal reason, and chain digest (§6.1 lines 589 and 645). It carries no request ID, traversal-position ID, attempt number, lease epoch, or idempotency key. Yet recovery must distinguish a request whose event was appended from one with no event and must never re-decide the former (line 615). The access schedule expressly permits repeated appearances and fixed retries (lines 623–624), so `(actor,row,operation,object)` cannot be used as a unique surrogate.

Counterexample: worker A appends the verdict for request R, loses its lease before receiving the append acknowledgement, and worker B recovers R. With no stable request identity in the durable event, B cannot determine whether the matching tuple is R, an earlier legal re-presentation of the same object, or a retry. Re-deciding R can produce two events for one request; deduplicating by tuple suppresses a later legal touch. A single serialised writer prevents simultaneous appends but does not solve idempotency across lease handover.

The “one decision per request” claim therefore lacks the field that would make it checkable. Add a canonical request/traversal-position identity and lease epoch to the authenticated event schema, and define recovery against them.

### F3 — HIGH / REPAIR-REQUIRED — a post-BS-L catch-all event does not block opening through any named verifier

Lines 598–600 correctly identify the P6→P7 gap and state that both BS-L issuance and lock opening are blocked while a `REFUSED-UNCLASSIFIED` event remains unenumerated. The executable prerequisites do not implement the second block:

- `verify_lock()` checks the checkpoint canonicalised into BS-L (line 674), which necessarily predates a later event.
- Row O requires only a passing `verify_lock()` and the canonical opening authorization (line 659).
- The opening-authorization body/verifier binds BS-L, store identities, destination, ceremony ID, phase, signer, and schema, but no fresh access-log checkpoint or catch-all enumeration state (line 682).

Counterexample: issue BS-L from a clean checkpoint; then emit an unenumerated catch-all event; then present a valid opening authorization. Every named Row-O prerequisite passes and opening proceeds.

The cited checker does not detect this. `tools/refusal_vocabulary_check.py` has the correctly quoted live digest `90a2d74e5eeca79e1c2417aef08a69302a263d85c18c8e511aaf8e8b04369143`, but R07 merely regex-matches `MAY NOT BE ISSUED while any REFUSED-UNCLASSIFIED` (checker lines 135–147). It never requires an opening-time checkpoint, enumeration verifier, or Row-O dependency. A fresh checkpoint plus a verifier consulted atomically by opening is required.

### F4 — HIGH / REPAIR-REQUIRED — the catch-all may become routine while every emission is formally “enumerated”

The guard says each catch-all emission is a defect, never routine (line 596), but its completion rule is only one entry per emission, naming row, operation and lifecycle state, with each “named or explained by a person” (line 599). It requires neither a new named refusal code, a root-cause repair, a recurrence cap, nor a refusal to open after the same explanation repeats. Line 617 routes every pre-verdict timeout, deadlock, lost verifier or crash to the catch-all, and line 618 acknowledges verifier timeout is foreseeable.

Conforming counterexample: the same verifier times out on every request; each event receives an enumeration entry saying “verifier timeout”; a person explains each entry; no event remains technically unenumerated; BS-L and opening may proceed. `REFUSED-UNCLASSIFIED` has become the routine timeout code while satisfying the letter of the enumeration rule.

This is worse than the parked “tension”: the draft contains an executable path through the claimed safeguard, not merely awkward vocabulary. Enumeration must have a closure consequence—for example, repeated known classes require a frozen named code and re-derived vocabulary, or block until the cause is repaired—not merely human acknowledgement. Lines 607 and 617 also still call this “freeze-time enumeration,” directly contradicting lines 597–600’s correction that freeze-time enumeration is impossible.

### F5 — HIGH / REPAIR-REQUIRED — a three-point endpoint-spanning manifest can miss an interior verdict change

The BS-3g rule requires both endpoints and at least three distinct γ values (§11 lines 1094–1101), while `invariance_outcome` is `HELD` iff every evaluated draw×perturbation cell equals the baseline verdict (lines 1149–1158). The conforming manifest `[-gamma_bound, 0, +gamma_bound]` leaves every other permitted γ unevaluated.

Construct a decision response equal to the baseline at those three values but different in a narrow interval around `gamma_bound/2`; two threshold crossings create exactly this shape. The manifest passes endpoint, cardinality, ordering, digest, replay and all-cells-equal checks and reports `HELD`, although invariance fails inside the stated bound. No monotonicity, convexity, mesh-width, exhaustive finite-domain, or interval-certification rule excludes the construction.

The digest binds the sampled list to the receipt, not the sampled list to the universal invariance question. Either define the admissible γ domain as exactly a frozen finite manifest and narrow the claim accordingly, or require a justified coverage/certification rule over the full interval.

### F6 — MEDIUM / REPAIR-REQUIRED — §5 still falsely classifies all three planning sites as CALLER

Section §5 line 528 says the former `NUMERICAL-PLANNING` class’s “three sites are `CALLER`.” The same draft correctly says L963 and L973 are caller errors while L986 is `PLANNING-INTERNAL` (line 503). The referenced `ref/RAISE_SITE_CLASSIFICATION.md` independently reports CALLER 25 and PLANNING-INTERNAL 1 (lines 11–16) and classifies L963/L973 as CALLER and L986 as PLANNING-INTERNAL (lines 80–82).

The sentence remains false even though the paragraph says the table wins on disagreement. Delete the duplicated disposition or correct it; a preregistration cannot carry two classifications for the same site in the same section.

## Failed attacks / checks that held

- Subject identity held: sha256 was recomputed before reading as `92b589e635228be87120585dfe04ec691923ac0cd8ae970634da57d0e49ca79d`.
- The §0 pin held: `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- The refusal-checker digest held exactly. Its self-test reported 12 controls, 0 failures, every code controlled; its V66 check reported 0 problems. F3 is a missing mechanism predicate, not a stale digest or failed existing control.
- The eleven formatted refusal codes matched the checker's exact set. I found no different leak beyond the parked object-identity channel.
- The three current BS-3g emission blockers held as text: `n_draws` and `draw_master_seed` are UNSET and `draw_generator_id` has an empty admissible set. I found no present receipt-emission path surviving all three.
- The BS-3g mask digest equality and strict-constructor posture are honest about being specified but unimplemented; I did not find a current slot producer that defeats those stated blockers.
- Mechanical checks held: `prereg_counts.py` returned 16 class P / 8 class E with prose match; `prereg_trace.py --check` returned 65 transitions and 0 problems; `prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; `void_registry.py --self-test` returned 6 controls and 0 failures, and the live registry contained 54 antecedents.
- Independent AST enumeration of `successor_ref_v9.py` reproduced 112 raises: 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, and 1 bare re-raise.
- `UNREACHABLE-BY-CONSTRUCTION` is assigned to no site in `RAISE_SITE_CLASSIFICATION.md`; its draft occurrences describe the ruled empty status and falsification behavior.
- The V43 in-run rerun allowance remains deleted. Remaining rerun/re-run references are historical or future Stage-P work, not a retry after the terminal numerical outcome.
- The numerical VOID rows remain Post-unblinding, while forbidden-act, protocol-deviation, and digest-deviation remain `Any`.
- KIMI-V11 F7 was checked against `gates/PREREG_TEXT_V11_KIMI.md`: it concerns the exact Stage-P receipt's v7 subject, not the claimed Stage-P implementation defect. V66 now records that the V42 substitution was also wrong rather than relying on it.

## Evidence ledger and scope

Content read:

- `gates/BRIEF_V66_REVIEW.md`
- `PREREG_SUCCESSOR_DRAFT_V66_20260829.md`
- `ref/RAISE_SITE_CLASSIFICATION.md`
- `ref/RAISE_CALLSITE_LEDGER.md`
- `ref/successor_ref_v9.py` targeted regions
- `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`
- `gates/PREREG_TEXT_V11_KIMI.md`
- `/Users/duhokim/NebulaMind/NebulaMind/tools/refusal_vocabulary_check.py`
- `/Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py` targeted regions
- `/Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py` targeted regions
- `gates/V66_WHOLE_REVIEW_GPT56.md`, read only after the lifecycle, manifest, and ledger attacks above had been independently formed; it was used as a cross-check, not as ground truth.

Commands/checks executed:

- `shasum -a 256` on the subject, pinned reference, refusal checker, and raise-site classification.
- `tools/prereg_lint.py`, `tools/prereg_counts.py`, `tools/prereg_trace.py --check`, refusal-vocabulary check/self-test, and VOID-registry live check/self-test.
- Independent Python AST raise-node enumeration.
- Targeted searches for request identity/idempotency, catch-all gate dependencies, transfer terminal events, rerun residue, `UNREACHABLE-BY-CONSTRUCTION`, BS-3g bindings, and planning classifications.

I did not modify the draft, reference code, tools, or any file other than this report. The parked durable pre-verdict event-class gap, availability-code object semantics, Row-F strata, VOID partition, object-identity leak, integrity-mismatch collision, BS-3g lifecycle cycle, per-call-site classification-unit defect, unbounded freeze-signature residue, BS-2v status, Row-L phase residue, gain mapping, authorization guard, and V54 residue were not re-derived as findings.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V66
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 611, 614–617, 645 | One pre-transfer event cannot truthfully record a later COMPLETED/FAILED transfer result.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 589, 615, 623–624, 645 | Recovery has no stable request identity with which to prevent redecision across legal retries and repeated touches.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 598–600, 659, 674, 682; checker lines 135–147 | A post-BS-L catch-all event reaches opening because no named verifier consults a fresh enumeration checkpoint.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 596–600, 607, 617–618 | Human explanation can enumerate an endlessly recurring catch-all class, making it routine while formally passing the guard.
F5 | HIGH | REPAIR-REQUIRED | §11 lines 1094–1101, 1149–1158 | An endpoint-spanning three-value γ manifest can miss an interior verdict flip and still report HELD.
F6 | MEDIUM | REPAIR-REQUIRED | §5 lines 503, 528; RAISE_SITE_CLASSIFICATION lines 11–16, 80–82 | Draft says all three planning sites are CALLER although L986 is PLANNING-INTERNAL.
<!-- END FINDINGS-BLOCK -->