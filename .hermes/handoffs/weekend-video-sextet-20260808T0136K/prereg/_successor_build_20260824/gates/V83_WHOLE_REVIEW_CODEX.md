# V83 whole-document adversarial referee — CODEX

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V83_REVIEW.md` first and verified the dispatched subject at SHA-256 `7bc71ce4787f1d81aa06b3537260969aad3084aa9a7a4c94d733dfed690f1d30` before reading it. The green mechanical checks hold at their stated scopes, but the advertised V83 repairs do not survive the document's own bytes: the replay harness still has no actual independent expected pin, ordinary imports still consume mutable dependency files, and the continuation partition leaves the BS-L issuance interval without a legal enumeration surface. The new cross-run rule has no closed authenticated history domain; the lifecycle's bounded-commit claim assumes away the very stalled commit it must terminate; and the registry's new lock-body row points to an enumeration that does not exist while its generator still cannot detect same-format schema additions on several manually declared surfaces.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §11 lines 1183–1191, 1231, 1449–1461

**`replay_harness_sha256` still has no independent expected value to compare against.** Line 1231 now says the verifier compares the receipt to “the value FROZEN IN THIS PREREGISTRATION,” and clause (a) now includes the harness among five recomputed digests. But the draft supplies no harness path, module identity, or 64-hex expected harness digest anywhere. A content search found only four draft occurrences: the field list, the assertion that a value is frozen, and two verifier-list mentions. A file-name search found no production replay harness in the build—only historical review/attack harnesses and logs.

This is the same self-report one level later: recomputing the digest of whichever harness the producer presents does not establish equality to independently frozen bytes when no expected bytes or digest are named. The freeze signature cannot cover a value absent from the preregistration. The repair requires a named harness artifact and its literal expected digest (or an exact freeze-body field populated independently before execution), plus equality to those bytes.

### F2 — HIGH / REPAIR-REQUIRED — §11 lines 1336–1390; `ref/successor_ref_v9.py` lines 39–47; `ref/gain_counterfactual_path.py` lines 43–50

**PRE-BINDING closes only the second v9 read; imported dependencies retain the verified/consumed swap window.** Executing the verified v9 buffer imports standard-library modules and NumPy through ordinary import machinery. Executing the path buffer does the same, and line 49 additionally inserts its on-disk source directory into `sys.path`. V83 explicitly leaves those dependencies on the import path and offers only an end-of-computation root recheck plus a loaded-object census.

Counterexample: after the initial root verification, replace an allowed dependency file at its already-manifested path; let the buffer import and execute those transient bytes; restore the pinned file before the final root recheck. The final disk digest matches, and the loaded-object census sees an allowed module/path, while the live module object and its side effects came from bytes that were never the bytes finally rehashed. A path/digest manifest of current disk state does not hash the consumed in-memory Python code object. PRE-BINDING correctly makes `import successor_ref_v9` bind the verified v9 module, but it does not cover the imports executed while constructing that module or the path module. The contract needs execution from verified dependency bytes, immutable file descriptors/content-addressed roots, or an equivalent consumed-code attestation; hash-before/import/hash-after is not sufficient against swap-and-restore.

### F3 — HIGH / REPAIR-REQUIRED — §6.1 lines 598–609, 724–731; §11 lines 1495–1507

**The temporal partition orphans catch-all events appended during BS-L issuance itself.** Pre-BS-L emissions must be in the sealed checkpoint materials; continuation entries are allowed only for events appended **after BS-L issuance**. Yet Clause 4 says the checkpoint is taken immediately before canonicalizing BS-L and the chain continues through issuance. A Row-B refusal can therefore be appended after the checkpoint has been sealed but before issuance has completed—for example, while the lock ceremony reads/canonicalizes a required object, or in the same transaction that records issuance.

That event is too late for the immutable checkpoint and not “after BS-L issuance,” so a continuation entry for it is refused by V83's new rule. If issuance waits for its enumeration, the checkpoint bytes and signed lock body are already stale; if issuance completes first, the event was outstanding at the gate that line 599 says “MAY NOT BE ISSUED.” The text needs an exact chain-position/epoch cut defining which transaction owns the boundary, with issuance atomic relative to that cut, rather than the undefined interval between “checkpoint sealed” and “issuance complete.”

### F4 — HIGH / REPAIR-REQUIRED — §6.1 lines 600–610 (especially the cross-run paragraph embedded in line 601); `LIFECYCLE_GUARANTEE_SPEC.md` lines 158–164

**“ANY prior run” is not a closed or authenticated recurrence domain.** V83 says a successor freeze review reads “this run's enumeration” and treats a class explained in any prior run as recurring. It does not define which run identities form the predecessor set, how the successor proves that set complete, or what happens to a run aborted before BS-L, a voided run, or a run whose failure was the enumeration mechanism itself. Those runs can contain the once-per-run catch-all emission while producing no final enumeration for the successor to read.

Nor is a prior-run registry/digest an input to the successor freeze checker. An operator can therefore present only the prior enumerations that reached their gates and classify a once-per-run defect in an omitted failed run as first occurrence. “Any” is an absence claim and needs an independently closed run-history manifest including terminal/aborted/voided runs and explicit treatment of missing/corrupt enumerations; an obligation to read whatever enumeration exists does not establish that history.

### F5 — MEDIUM / REPAIR-REQUIRED — `LIFECYCLE_GUARANTEE_SPEC.md` lines 81–95; draft §6.1 lines 634–646 and §11 lines 1508–1512

**The bounded-commit repair assumes abort availability instead of specifying it.** The spec says a commit exceeding its BS-2k bound is aborted and asserts that “transactional semantics make abort always available.” Atomicity says what states may become durable; it does not guarantee that the process/domain can execute an abort while blocked in an uninterruptible store `fsync`, kernel I/O, or a wedged single-writer transaction. Killing the writer is not by itself a proven abort: recovery may discover that the original commit became durable, so appending the promised deadline refusal can create the two-terminal-treatment state G4 forbids.

This is exactly the request the deadline clause says cannot exist: past deadline, nonterminal, and unable to append its refusal. The BS-2k requirement needs a fault model and a separately live fencing/recovery arbiter that decides the timeout/commit race from durable transaction state and proves the losing branch can never later commit. Without that, “abort always available” is the universal negative under attack, not a transactional consequence.

### F6 — HIGH / REPAIR-REQUIRED — §6.1 Clause 3 lines 724–727; `ref/gen_string_field_registry.py` lines 92–101; `ref/STRING_FIELD_REGISTRY.md` line 124

**`lockbody.bound_digests` points to a nonexistent Clause 3(a) enumeration.** The new registry row says its leaves are “the digest set clause 3(a) enumerates.” Clause 3(a) does not enumerate the lock-body digest leaves; it states only that BS-L is class E and has the freeze and BS-5f as preconditions. The actual canonical-body field list is in Clause 3(b), and it includes materially more objects: roster, accepted mask, calibration, Stage-C, decision inputs, class-P/gate/freeze manifest, checkpoint/chain segment, archive receipt, environment, and signer identity.

The one-row container therefore does not point to the claimed field-order enumeration, and the registry still has no field-by-field lock-body leaves. Worse, the generated row labels this manually injected pseudo-field as declared under “v9 SLOT_SCHEMA,” although frozen v9 has no such `lockbody.bound_digests` field. The V82 container-hides-leaves defect has been redirected to the wrong clause rather than closed. Point to Clause 3(b) and define how its heterogeneous leaves map into one canonical ordered structure, or enumerate the leaves explicitly.

### F7 — MEDIUM / REPAIR-REQUIRED — §6.1 lines 664–678; `ref/gen_string_field_registry.py` lines 225–284; `ref/STRING_FIELD_REGISTRY.md` lines 1–3

**The registry still claims omission resistance that its manual inventories do not provide.** The generated header now admits two provenances, but it still says “Extraction cannot silently omit,” and the draft says the generator “extracts every field token from the declared field lists.” In code, `extract()` recognizes only three regex-shaped draft blocks. Opening authorization, freeze, canonical bodies, non-slot classes, BS-7p environment, signatures, lock body, and explanation parameters are hard-coded sets unioned after extraction.

An in-memory no-write probe supplied a same-format opening-authorization declaration containing `newly_added_field`; `extract()` returned an empty set and the hard-coded `OPENAUTH` set did not contain it. Thus a future Clause-6 addition is silently absent unless a human edits the generator in the same revision—the exact drift that produced the earlier `timestamp`/`schema_version` error. Declared surfaces need structural extraction and byte-equality checks against their prose declarations, or the document must drop the claim that the generator prevents omissions and treat those inventories as manually reviewed lists.

## Failed attacks / confirmations (not findings)

- Subject SHA-256 matched before reading and again during the battery. The companion spec hashes to `65561de67208f8c135e3c98ba0c8c505084fdd43e144ac74d651a030d1ab8184`, matching the draft's pin.
- Frozen code hashes matched disk: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`; `tools/refusal_vocabulary_check.py` = `c448646b955bd2200d5f3062a397791530300a29a32b353a62d7f13919ae8dee`.
- `tools/prereg_lint.py` exited 0 with 97 advisory legacy citations and 0 blocking findings. Per the brief, I do not report those option-D advisories as unresolved.
- `tools/prereg_counts.py` returned 16 class-P / 8 class-E and prose/table agreement. `tools/prereg_trace.py ... --check` returned 82 transitions / 0 problems; its scope self-test returned 0 failures. `tools/void_registry.py` returned 54 antecedents / 20 named rows.
- `tools/refusal_vocabulary_check.py` returned 0 problems; its 32-control self-test returned 0 failures. The V83 negated-form R08 repair held for its stated patterns.
- `tools/lifecycle_derivation_check.py` returned 0 problems: the labelled G/N quotations match the spec bytes. F3–F5 concern semantics outside what byte-copy checking proves.
- The frozen v9 AST has 112 `Raise` nodes, and `ref/RAISE_SITE_CLASSIFICATION.md` has 112 rows with exact closure `26 CALLER / 59 INTEGRITY / 20 NUMERICAL / 3 PLANNING-INTERNAL / 1 TYPED-OUTCOME / 3 WRAPPER`. No site is marked `UNREACHABLE-BY-CONSTRUCTION`. I did not re-derive the parked per-raise/per-call-site defect.
- The opening-authorization tuple at line 610 matches Clause 6's eight names and ends in `schema_version`; I found no third stale field-name body.
- The V83 canonical-JSON additions close V82's lowercase-escape and post-NFC-collision examples. I did not promote a new JSON ambiguity without a counterexample that survived the stated minimal-escape rule.
- I did not re-derive the brief's parked availability-code, durable-pre-verdict-state, strata/producer, VOID partition, logged-object membership, BS-3g lifecycle cycle, freeze-exemption, BS-2v, `require_authorization`, draw-discipline, or Row-L phase issues.

## Evidence ledger and scope

Read in content: the V83 brief; the full 1,516-line V83 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; and `tools/refusal_vocabulary_check.py`, plus the V81/V82 reports only to distinguish new repairs from parked or already-known findings. Executed read-only hash, lint, count, trace, lifecycle, refusal, VOID, AST-closure, content-search, and in-memory extractor probes. The repository already contains extensive unrelated dirty/untracked state; I did not alter it. I modified no draft, spec, reference, checker, registry, receipt, or gate artifact other than this assigned report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V83
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1183–1191, 1231, 1449–1461 | replay_harness_sha256 still has no named harness artifact or literal independently frozen expected digest.
F2 | HIGH | REPAIR-REQUIRED | §11 lines 1336–1390; pinned module import blocks | PRE-BINDING protects v9 only; mutable dependency imports can consume swapped bytes restored before the end recheck.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 598–609, 724–731 | Events appended after checkpoint sealing but during BS-L issuance fit neither the sealed checkpoint nor the post-issuance continuation.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 600–610; lifecycle spec lines 158–164 | ANY-prior-run recurrence has no authenticated complete run-history domain and loses aborted/voided/enumeration-failed runs.
F5 | MEDIUM | REPAIR-REQUIRED | lifecycle spec lines 81–95; §11 lines 1508–1512 | Atomicity does not make abort always available for a commit wedged inside storage, leaving the deadline lifecycle non-total.
F6 | HIGH | REPAIR-REQUIRED | §6.1 Clause 3 lines 724–727; STRING_FIELD_REGISTRY line 124 | lockbody.bound_digests points to Clause 3(a), which contains no lock-body field enumeration.
F7 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 664–678; gen_string_field_registry.py lines 225–284 | Manually hard-coded schema inventories still permit silent omission despite the generator's extraction claim.
<!-- END FINDINGS-BLOCK -->