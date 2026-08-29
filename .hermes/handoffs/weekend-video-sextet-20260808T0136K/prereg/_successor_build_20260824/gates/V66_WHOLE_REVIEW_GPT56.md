# V66 whole-document adversarial review — GPT56

**VERDICT: NOT CLEAR.** The pinned subject digest matches, and several mechanical checks hold, but the new lifecycle and catch-all repairs are not executable as written. I found two distinct request-state counterexamples, a post-BS-L path around the purported continuous catch-all block, a finite-manifest evasion of the gradient invariance question, and a live prose/ledger contradiction.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — a pre-verdict crash still leaves a received request undecided and unlogged

Section §6.1 says every request occupies exactly one lifecycle state (line 611), that a request dying in `RECEIVED`, `PENDING-AUTHORISATION`, or `PENDING-SURFACE-CHECK` "is logged as a refusal" (line 617), and therefore "no request can end undecided or unlogged." But lines 614–616 also say that there is no durable pre-verdict state, that a request with no appended event "never happened," and that such a request is merely eligible to be reprocessed.

Counterexample: Row B receives request R and enters `RECEIVED`; before appending any event, Row B and the requester both crash, so nobody retries R. The real request did arrive, but the only durable record is indistinguishable from no request. No recovery rule can discover R, append `REFUSED-UNCLASSIFIED`, or force reprocessing. R therefore ends in exactly the state the universal claim excludes: received in reality, undecided and unlogged. Calling it "never happened" changes the definition after the failure; it does not supply the terminal treatment promised at line 617.

This is worse than the narrowly stated residue at line 616. The residue is not only epistemic indistinguishability between decide-and-append and non-arrival; it defeats the broader exact-one-terminal-treatment claim. Repair requires either a durable receipt/in-flight event before `RECEIVED` is claimed, or narrowing the universal lifecycle claim so such requests are expressly outside its accounted universe.

### F2 — HIGH / REPAIR-REQUIRED — the one-event, append-before-release schema cannot record the terminal result of transfer

Row B's normative table cell says it appends "exactly one event per touch, success or refusal" (line 645). The lifecycle says an authorised request moves through `TRANSFER` to `COMPLETED` or `FAILED` (line 611), while append-before-release requires the sole event before any read byte is released or any write byte is committed (line 614). Recovery then forbids re-decision after an event exists (line 615).

Counterexample: an authorised read appends its sole success/refusal event, begins releasing a multi-byte payload, releases a prefix, and then the transport dies. At append time Row B cannot know whether the terminal state will be `COMPLETED` or `FAILED`. If the event says success, it is false after the partial failure; if it records only authorisation, it violates the declared success/refusal schema and does not record the terminal treatment; if Row B appends an availability-coded failure afterward, it violates exactly one event and the no-redecision rule. The same problem occurs when a write's durable store commit fails after the pre-commit append.

Line 614 openly permits over-reporting a touch, but line 617 separately claims the failed transfer is "completed as `FAILED` under the availability codes." No event remains in which to record that code. Atomic permission logging and exact terminal-transfer logging are two different state transitions; one pre-transfer event cannot truthfully represent both.

### F3 — HIGH / REPAIR-REQUIRED — the continuous catch-all block has no post-BS-L enforcement path, and the checker cannot detect that absence

Lines 598–600 correctly notice the P6→P7 gap and assert that both BS-L and opening the lock are blocked by any outstanding unenumerated `REFUSED-UNCLASSIFIED`. The surrounding executable contract does not bind the second block:

- `verify_lock()` verifies the pre-unblinding checkpoint used to canonicalise BS-L (line 674); it cannot cover later events.
- The opening-authorisation verifier binds BS-L, store identities, destination, ceremony ID, phase, signer, and schema (line 682), but no fresh log checkpoint or catch-all enumeration.
- Row O requires a passing `verify_lock()` and opening authorisation (line 659), again with no post-BS-L catch-all check.

Counterexample: BS-L is issued from a clean checkpoint; afterward Row B emits `REFUSED-UNCLASSIFIED`; Duho supplies a valid opening authorisation; Row O verifies the already-valid BS-L and authorisation and opens. Every named executable prerequisite passes while the line-600 invariant is outstanding.

The referenced checker gives false comfort. `tools/refusal_vocabulary_check.py` has the correct live sha256 `90a2d74e5eeca79e1c2417aef08a69302a263d85c18c8e511aaf8e8b04369143`, but R07 only regex-checks the phrase `MAY NOT BE ISSUED while any REFUSED-UNCLASSIFIED` (lines 146–147). It does not check the claimed block on opening, a fresh checkpoint, one-entry-per-emission closure, or any gate/verifier dependency. Accordingly it exits 0 on V66 despite the path above. Line 607 and line 617 also still say "freeze-time enumeration," contradicting lines 597–600's explicit finding that freeze-time enumeration is impossible.

### F4 — HIGH / REPAIR-REQUIRED — endpoints plus three values do not test invariance throughout the bound

The BS-3g manifest repair requires both endpoints and at least three distinct γ values (lines 1094–1101), then defines `HELD` iff every evaluated cell equals the baseline verdict (lines 1154–1158). A conforming manifest `[-gamma_bound, 0, +gamma_bound]` still leaves every interior γ unevaluated.

Construct a permitted mapping/decision response whose verdict equals baseline at those three points but flips in a narrow interval around `gamma_bound/2` (a threshold crossing followed by a crossing back is enough). The manifest passes every stated span, cardinality, digest, replay, and all-cells-equal check and reports `HELD`, although invariance fails inside the claimed bound. Nothing states monotonicity, convexity, a mesh width, an exhaustive finite allowed set, or an adaptive interval-certification rule that would exclude this construction.

The repair binds the sampled list to the receipt, but still does not bind that list to the universal invariance question. Either define the admissible γ set as exactly a frozen finite manifest and narrow the claim to that set, or require a coverage/certification rule justified for the response function.

### F5 — MEDIUM / REPAIR-REQUIRED — §5 still falsely says all three planning sites are CALLER

Section §5 line 528 says the former `NUMERICAL-PLANNING` class's "three sites are `CALLER`." The referenced live ledger says otherwise: `ref/RAISE_SITE_CLASSIFICATION.md` reports CALLER 25 and PLANNING-INTERNAL 1 (lines 11–16), classifies L963 and L973 as CALLER, and classifies L986 as PLANNING-INTERNAL (lines 80–82). Its explanatory line 9 says the same. The draft itself correctly describes L986 as PLANNING-INTERNAL at line 503, so line 528 contradicts both the authoritative file and the nearby prose.

This is not cured by line 528's "the table is right" escape: the preregistration makes a false disposition claim in the same paragraph that says copied counts/dispositions drift and must not be restated. Delete or correct the sentence; do not leave two operative classifications for L986.

## Failed attacks / checks that held

- Subject identity held: sha256 recomputed as `92b589e635228be87120585dfe04ec691923ac0cd8ae970634da57d0e49ca79d` before reading.
- The §0 reference pin held: `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- The refusal checker digest quoted in V66 held exactly, and its own self-test reported 12 controls, 0 failures, every code controlled. The finding above is about missing mechanism coverage, not a stale digest or a failing self-test.
- The checker accepted exactly the eleven formatted refusal codes; I did not find a twelfth formatted code or revival of either retired code.
- The frozen draw blockers held as text: `n_draws` and `draw_master_seed` are explicitly UNSET, `draw_generator_id`'s admissible set is empty, and V66 forbids BS-3g receipt emission while these remain unresolved. I found no current emission path through all three blockers.
- The mask binding and strict-constructor posture are honest about being unimplemented: V66 does not falsely claim the successor-layer BS-3g schema or producer/verifier already exists.
- Mechanical inventory held: `tools/prereg_counts.py` reported 16 class P / 8 class E and prose match; `tools/prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; `tools/void_registry.py --self-test` reported 6 controls and 0 failures.
- `UNREACHABLE-BY-CONSTRUCTION` does not occur in `ref/RAISE_SITE_CLASSIFICATION.md`; no site currently holds it. The draft's occurrences describe the ruled status and falsification rule rather than assigning a site.
- The V43 in-run rerun allowance remains deleted. Historical uses of rerun/re-run describe prior measurements, future Stage-P work, or the deletion record; I found no new retry-after-`INCONCLUSIVE-BY-NUMERICAL-FAILURE` path.
- The numerical `VOID` antecedents remain Post-unblinding, while forbidden-act, protocol-deviation, and digest-deviation remain `Any` in §7.1.

## Evidence ledger and scope

Content read:

- `gates/BRIEF_V66_REVIEW.md`
- `PREREG_SUCCESSOR_DRAFT_V66_20260829.md`
- `ref/RAISE_SITE_CLASSIFICATION.md`
- `ref/RAISE_CALLSITE_LEDGER.md`
- `/Users/duhokim/NebulaMind/NebulaMind/tools/refusal_vocabulary_check.py`

Commands/checks executed:

- `shasum -a 256` on the subject, pinned reference, raise-site ledger, call-site ledger, and refusal checker.
- `git diff --no-index` for V65→V66.
- refusal-vocabulary check and self-test.
- prereg lint, counts, trace invocation, and VOID-registry self-test. (`prereg_trace.py` was invoked on one draft and correctly returned "no consecutive draft pairs found"; no trace claim is based on that invocation.)
- targeted searches for rerun residue, `UNREACHABLE-BY-CONSTRUCTION`, catch-all gates, BS-3g bindings, and planning classifications.

I modified no draft, reference, tool, or other artifact. My sole write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V66
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 610–617 | Without durable pre-verdict state, a received request can crash and remain forever undecided and unlogged.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 611, 614–617, 645 | One pre-transfer success/refusal event cannot also truthfully record a later COMPLETED/FAILED transfer outcome.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 598–600, 659, 674, 682; checker lines 146–147 | Post-BS-L catch-all events do not block opening through any named verifier, and R07 checks only a BS-L phrase.
F4 | HIGH | REPAIR-REQUIRED | §11 lines 1094–1101, 1154–1158 | A three-point endpoint-spanning γ manifest can miss an interior verdict flip and still report HELD.
F5 | MEDIUM | REPAIR-REQUIRED | §5 line 528; RAISE_SITE_CLASSIFICATION lines 9, 11–16, 80–82 | Draft says all three planning sites are CALLER while L986 is authoritatively PLANNING-INTERNAL.
<!-- END FINDINGS-BLOCK -->