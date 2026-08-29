# V64 whole-document adversarial review — GPT56

## Verdict

**NOT CLEAR.** The dispatched draft matched the required SHA-256 before reading. V64's request lifecycle is not a state machine that can deliver its universal claims: it has no durable pre-verdict request record, atomic verdict/log operation, crash-recovery actor, or fencing against a timed-out verifier returning after a refusal. The catch-all guard is also temporally incapable of keeping run-time undecided requests from becoming routine, because it reviews emissions "at freeze," before those emissions exist, and attaches no run-time consequence. Separately, the claimed draw pre-commitment contains no actual frozen count or seed, the live raise-site classification contradicts V64's L986 disposition, and V64 misstates the live refusal checker hash.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — §6.1 lines 605–610 — the lifecycle cannot guarantee one terminal, logged treatment

The universal claim is false for ordinary crash and timeout schedules.

* Lines 606–608 say every request is in exactly one state, that Row B logs "at the instant" the permission verdict is reached, and that a request dying in `RECEIVED`, `PENDING-AUTHORISATION`, or `PENDING-SURFACE-CHECK` is logged as `REFUSED-UNCLASSIFIED`.
* But no durable request identity or pre-verdict journal entry is created at `RECEIVED`; the access-log schema at line 589 records timestamp, actor, table row, operation, object identity, success/refusal, refusal reason, and chain digest, but no request-state record or recovery ownership. If Row B crashes before the permission verdict/log append, there may be no durable evidence that the request existed and no live Row B left to append the promised refusal. Saying the dead request "is logged" does not name a mechanism that can do it.
* "Verdict reached" and "event appended" are distinct effects. No transaction, write-ahead record, compare-and-swap, or recovery rule makes them atomic. A crash after computing the verdict but before the append leaves a reached but unlogged verdict, directly falsifying line 607's claimed boundary.
* A verifier can time out, causing a refusal to be logged, and later return `AUTHORISED`. Nothing cancels or fences that stale completion. The same request can therefore acquire both `REFUSED` and `AUTHORISED` treatments and can proceed to `TRANSFER` after its refusal. Exactly-one state requires a durable request ID, monotonic transition record, terminal compare-and-swap, and generation/cancellation fencing; none is specified.
* Death after the logged `AUTHORISED` verdict but before entry into `TRANSFER` is also omitted from line 608's terminal treatments, which cover pending states and `TRANSFER` but not the intermediate `AUTHORISED` state.

Smallest sufficient repair: specify a durable request record before any check/decoding, canonical request identity, an atomic monotonic transition/log protocol, a recovery owner for abandoned pending states, and fencing that makes every late verifier/worker result after a terminal refusal incapable of transfer. Then exercise crash points at every transition and prove one terminal event per request.

### F2 — HIGH — REPAIR-REQUIRED — §6.1 lines 596, 602, 608–609 — the catch-all guard cannot stop routine run-time use

V64 itself gives a deterministic routine path: every timeout, deadlock, lost verifier, or crash in any pre-verdict state emits `REFUSED-UNCLASSIFIED` (line 608). Yet the guard says its count is reviewed "at freeze" and each emission is named or explained (line 596). Freeze precedes execution, so run-time emissions do not exist at the only named review point. A freeze-time count can therefore be zero, after which the same predictable verifier timeout can land in the catch-all on every request/run without violating any executable condition in the draft.

Even if "at freeze" were read as reviewing hypothetical classes rather than observed events, the guard still has no threshold, no required reclassification before the next request, no halt/VOID consequence, no post-run reconciliation, and no prohibition on repeatedly explaining the same emission. Line 609 already admits verifier timeout is foreseeable; that makes this worse than the parked "tension." The only checker supplied for the guard is syntactic: `tools/refusal_vocabulary_check.py` R05 passes whenever the text contains `enumerated at freeze` and `REFUSED-UNCLASSIFIED` (lines 131–133). It does not and cannot verify timing, count closure, or terminal consequence. The checker passed V64 and all self-controls, demonstrating only phrase presence.

Smallest sufficient repair: move enumeration/reconciliation to a durable execution boundary after emissions can exist, bind request IDs and counts, make repeated/unexplained catch-all use halt or block continuation, and add a control where a fixed timeout occurs on every request yet the purported guard must fail.

### F3 — HIGH — REPAIR-REQUIRED — §11 lines 1095–1121, especially 1100–1102 and 1117–1120 — the draw set is not pre-committed in V64

The repair says `n_draws` and `draw_master_seed` are "FROZEN IN THIS PREREGISTRATION" and that `draw_generator_id` and `mapping_id` come from closed enumerated sets declared in this document. Byte-level search of V64 finds no assignment/literal value for `n_draws`, no assignment/literal value for `draw_master_seed`, no enumerated generator ID at all, and only `MAPPING-NOT-PREREGISTERED` as a mapping token. The field bounds `[1, 10^6]` and `[0, 2^64-1]` are domains, not pre-committed values.

Thus an editor can choose count, seed, generator, and mapping in a later revision after exploratory counterfactual verdicts while V64's claimed repair remains textually satisfied. The future freeze signature can prove only that the final choices preceded that future freeze; it cannot prove they preceded off-record exploration already performed before the revision. V64 honestly labels BS-3g DESIGN/UNFILLED elsewhere, but lines 1095–1104 specifically claim the pre-commitment gap is closed; it is not. A receipt matching values chosen later is replayable, not result-blind.

Smallest sufficient repair: place the actual count and seed literals and the finite mapping/generator enumerations in the exact gated draft before any allowed exploratory execution, bind their bytes into the freeze body, and bar any pre-freeze execution of the draw generator/control outside synthetic fixtures whose outputs cannot reveal a candidate gate verdict.

### F4 — MEDIUM — REPAIR-REQUIRED — §5 lines 503 and 528; `ref/RAISE_SITE_CLASSIFICATION.md` lines 9, 11–17, 79–81 — L986 has two incompatible dispositions

V64 line 503 correctly distinguishes L963/L973 (`CALLER`) from L986 (`PLANNING-INTERNAL`), because L986 tests the frozen internal `MOVE_CAP` after a feasible prefix exists, not a caller-supplied `l_plan`. The pinned source confirms this at `ref/successor_ref_v9.py` lines 975–986: `moves` is internally incremented and compared to module constant `MOVE_CAP`.

But V64 line 528 says all three sites are `CALLER`, and the referenced live classification does the same. `RAISE_SITE_CLASSIFICATION.md` line 9 falsely says each of L963/L973/L986 is a setup error against caller-supplied `l_plan`; line 81 classifies L986 `CALLER`; its total is consequently `CALLER 26`. The draft also declares that ledger authoritative when prose disagrees, so its own repair is defeated by the authority rule. `RAISE_CALLSITE_LEDGER.md` does not cure the classification: it explicitly leaves L986 `UNJUDGED` and inherits the per-site class.

Smallest sufficient repair: regenerate the authoritative classification with L986 as `PLANNING-INTERNAL`, adjust totals and every prose quotation, and define the non-outcome terminal operator treatment rather than leaving an internal algorithm failure with "no terminal consequence."

### F5 — MEDIUM — REPAIR-REQUIRED — §6.1 line 603 — the checker fingerprint claim is false against the live file

V64 says `c2ccebbcb4730944…` is the SHA-256 of `tools/refusal_vocabulary_check.py` and that "both values were right." The live referenced file hashes to:

`acb38c401e00b07565fe753206644acae99c1e8d8ea5ac66f58fa63bed7047d4`

The claimed prefix and live digest disagree. This matters because V64 relies on the rewritten checker's inverted semantics and expressly identifies its bytes. The tool may have changed after the recorded digest, but then V64 is not bound to the checker actually run; if the live tool is intended, the factual hash claim is stale.

Smallest sufficient repair: either restore the exact tool bytes V64 identifies or update the draft to the independently recomputed full digest and gate that exact checker. Do not retain a truncated stale fingerprint while asserting it is right.

## Failed attacks / held points

* **Subject identity held:** SHA-256 recomputed before reading was exactly `af171440cd2d31c6b247f784c19f3ecc0d10647dd25eb5fbd93399565c688bbe`.
* **Eleven-token syntactic vocabulary held:** the live checker reported `0 problem(s)`; its self-test reported 10 controls, 0 failures, every code controlled. I did not re-report the parked object-membership leak or the unresolved integrity-mismatch/VOID collision.
* **Counts held:** live lint/count parsing returned 16 class P and 8 class E, prose-matched.
* **Withdrawal held:** neither V64 nor the live raise-site classification assigns any site `UNREACHABLE-BY-CONSTRUCTION`; the current defect is the separate L986 disposition conflict.
* **Misconduct phase held:** `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION` remain `Any` in §7.1 and the prose keeps forbidden acts/protocol-digest deviation at any phase.
* **V43 rerun deletion held:** remaining rerun references are historical, fixtures/new design execution, or explicit no-rerun clauses; I found no same-run retry after a terminal numerical outcome.
* **KIMI citation correction is no longer falsely credited:** §2.6 now says KIMI-V11 F7 does not support the Stage-P dual-valued claim and limits that claim to GPT56/CODEX.
* **BS-3g mask equality is stated in the right direction:** `mask_sha256` must equal BS-2f's pinned mask digest, and the verifier is required to recompute the comparison. I found no new subset bypass beyond the slot's openly unimplemented state.

## Evidence ledger and scope

Read in content: `gates/BRIEF_V64_REVIEW.md`; the complete V64 draft; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; relevant pinned-source region of `ref/successor_ref_v9.py`; and `/Users/duhokim/NebulaMind/NebulaMind/tools/refusal_vocabulary_check.py`.

Executed read-only checks: subject SHA-256; checker SHA-256; refusal checker and self-test; prereg lint; prereg count parser; exact searches for draw/seed assignments and enumerated IDs; searches for lifecycle, catch-all, rerun, withdrawal, classification, and receipt-binding claims. The lint returned 97 advisory legacy citations and 0 blocking findings; per the principal's option-D ruling I did not report those advisories as unresolved.

I did not modify the draft, reference files, checker, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V64
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 605–610 | The request lifecycle lacks durable pre-verdict state, atomic logging, recovery ownership, and stale-worker fencing, so requests can end unlogged or in two terminal treatments.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 596, 602, 608–609 | Freeze-time review cannot police run-time catch-all emissions, and no executable consequence prevents REFUSED-UNCLASSIFIED from becoming routine.
F3 | HIGH | REPAIR-REQUIRED | §11 lines 1095–1121 | V64 claims draw pre-commitment but contains no frozen n_draws or master-seed value and no declared generator-ID enumeration.
F4 | MEDIUM | REPAIR-REQUIRED | §5 lines 503, 528; raise-site ledger lines 9, 79–81 | L986 is PLANNING-INTERNAL under the source and V64's repair but CALLER in the authoritative live classification and later prose.
F5 | MEDIUM | REPAIR-REQUIRED | §6.1 line 603 | V64's claimed refusal-checker SHA prefix c2ccebbcb4730944 disagrees with the live referenced file's acb38c401e00b075 hash.
<!-- END FINDINGS-BLOCK -->