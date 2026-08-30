# V83 whole-document adversarial referee — GPT56

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V83_REVIEW.md` first and verified the dispatched subject at SHA-256 `7bc71ce4787f1d81aa06b3537260969aad3084aa9a7a4c94d733dfed690f1d30` before reading it. The green mechanical checks hold at their stated scopes, but seven substantive defects survive. PRE-BINDING closes the second v9 import while leaving mutable dependency imports exposed; the claimed independently frozen replay-harness value does not exist in the preregistration; the continuation partition has no legal side for events committed during BS-L issuance; “ANY prior run” has no closed history domain; the bounded-commit repair assumes abort availability; the new lock-body registry row cites an enumeration absent from the clause it names; and manually declared registry surfaces remain outside the claimed omission-resistant extraction.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — §11 lines 1183–1191, 1231, 1449–1461

**`replay_harness_sha256` still has no independently frozen expected value.** Line 1231 now says the verifier compares a receipt against “the value FROZEN IN THIS PREREGISTRATION,” and clause (a) now includes the harness among five recomputed digests. But the document gives no harness path or module identity and no literal 64-hex expected harness digest. An exact search found only three occurrences of `replay_harness_sha256`, none followed by a literal expected digest; a filename search found no replay-harness artifact in the successor build.

Recomputing the digest of whichever harness the producer presents remains self-report. The freeze signature cannot cover a value absent from the bytes it signs. This needs a named harness artifact and an expected digest independently present in the preregistration (or an exact freeze-body field populated before execution), followed by equality to those bytes.

### F2 — HIGH — REPAIR-REQUIRED — §11 lines 1336–1390; `ref/successor_ref_v9.py` lines 39–47; `ref/gain_counterfactual_path.py` lines 43–50

**PRE-BINDING protects the pinned pair, not the bytes consumed by their imports.** Executing the verified v9 buffer still imports standard-library modules and NumPy through ordinary import machinery; the path buffer also imports NumPy and mutates `sys.path`. V83 expressly leaves dependency roots on the real import path and covers them with a post-computation disk recheck plus a loaded-object census.

Counterexample: after the initial root verification, replace an allowed dependency file at its already-manifested path; let execution import and run those transient bytes; restore the pinned bytes before the end recheck. The final disk hash matches and the census sees an allowed module at an allowed path, while the live module object and its side effects came from bytes never attested as consumed. A path/digest census hashes current disk state, not the executing Python code object or mapped image bytes. The document’s claim that “a mid-run swap shows at the end recheck” is therefore false for swap-and-restore. Dependency consumption needs verified buffers/immutable file descriptors, content-addressed immutable roots, or equivalent in-memory-code attestation.

### F3 — HIGH — REPAIR-REQUIRED — §6.1 lines 598–609, Clauses 3–4 lines 724–731; §11 lines 1495–1507

**The temporal partition orphans an event appended during BS-L issuance.** V83 requires every pre-BS-L emission to live in the sealed checkpoint and allows a continuation entry only for an event appended **after BS-L issuance**. Clause 4 says the checkpoint is taken immediately before canonicalizing BS-L and that the chain continues through issuance. A Row-B refusal can therefore commit after checkpoint sealing but before issuance completes—for example while the ceremony resolves a required object, or in the transaction recording issuance.

That event is too late for the immutable checkpoint and not after issuance, so the continuation rule refuses it. Rebuilding the checkpoint makes the signed body stale; completing issuance first violates the invariant that BS-L “MAY NOT BE ISSUED” with an outstanding event. Define and sign an exact chain-position/epoch cut and serialize issuance atomically relative to it; “before/after issuance” is not a complete partition of transactions crossing the boundary.

### F4 — HIGH — REPAIR-REQUIRED — §6.1 lines 600–610 (cross-run paragraph in line 601); `LIFECYCLE_GUARANTEE_SPEC.md` lines 158–164

**“ANY prior run” has no complete authenticated domain.** The successor obligation says its freeze review reads “this run’s enumeration” while treating a class explained in any prior run as recurring. It does not define the set of prior run identities, bind a complete run-history manifest, or say how to include a run aborted before BS-L, a voided run, or a run whose enumeration mechanism was itself the failure. Such a run can contain the paced catch-all emission yet produce no final enumeration for the successor to read.

An operator can therefore present only enumerations from runs that reached their gates and call a class from an omitted failed run a first occurrence. “Any prior run” is an absence claim: it needs independently closed run-history custody, including terminal/aborted/voided runs and explicit treatment of missing or corrupt enumerations. Reading whatever enumeration exists does not prove the history complete.

### F5 — MEDIUM — REPAIR-REQUIRED — `LIFECYCLE_GUARANTEE_SPEC.md` lines 19–21, 81–95; draft §6.1 lines 634–646 and §11 lines 1508–1512

**The bounded-commit repair assumes the abort it needs.** The spec says a commit exceeding its BS-2k bound aborts because “transactional semantics make abort always available,” then the request receives a refusal commit. Atomicity constrains durable outcomes; it does not guarantee that a single-writer domain blocked in an uninterruptible store `fsync`, kernel I/O, or wedged transaction can execute abort. Killing the writer also does not prove abort: recovery may later find the original commit durable, and appending the promised refusal would create two terminal treatments.

The refusal commit is itself a commit and can encounter the same stall, so “abort-then-refusal” is not a terminal construction merely by repetition. The design needs a fault model and independently live fencing/recovery arbiter that resolves the timeout/commit race from durable transaction state and proves the losing branch cannot later commit.

### F6 — HIGH — REPAIR-REQUIRED — §6.1 Clause 3 lines 724–727; `ref/STRING_FIELD_REGISTRY.md` line 124; `ref/gen_string_field_registry.py` lines 254–267

**`lockbody.bound_digests` points to an enumeration Clause 3(a) does not contain.** The new registry row says its leaves are “the digest set clause 3(a) enumerates.” Clause 3(a) states only BS-L’s class and two preconditions. The canonical lock-body list is in Clause 3(b), and it contains roster, mask, calibration, Stage-C, decision inputs, the class-P/gate/freeze manifest, checkpoint and chain segment, archive receipt, environment, and signer identity.

The repair therefore replaces missing lock-body leaves with one manually injected pseudo-field whose cited source has no field-order enumeration. It is also labelled as declared under “v9 SLOT_SCHEMA” although frozen v9 has no `lockbody.bound_digests` field. Point to the actual Clause 3(b) body and define its ordered heterogeneous leaves, or enumerate those leaves directly.

### F7 — MEDIUM — REPAIR-REQUIRED — §6.1 lines 664–678; `ref/gen_string_field_registry.py` lines 225–309; `ref/STRING_FIELD_REGISTRY.md` lines 1–3

**The registry still overclaims omission resistance for manually declared surfaces.** The header now honestly admits two provenances, but the draft still says the generator extracts every field token from declared field lists and therefore cannot silently omit one. In code, `extract()` recognizes only a few regex-shaped blocks. Opening authorization, freeze body, canonical bodies, non-slot classes, BS-7p environment, signatures, lock body, and explanation parameters are hard-coded sets unioned after extraction.

A new field added to one of those prose schemas is invisible unless a human also edits the corresponding Python set in the same revision—the exact same-format drift this generator is claimed to prevent. “Auditable in one screen” is manual review, not omission detection. Those surfaces need structural extraction/byte-equality checks against their source declarations, or the omission-resistance claim must be narrowed to the blocks actually extracted.

## Adversarial checks that held or were correctly disclosed

- The subject digest matched before content review. The companion lifecycle spec hashes to `65561de67208f8c135e3c98ba0c8c505084fdd43e144ac74d651a030d1ab8184`, matching the draft pin.
- Frozen code hashes matched disk: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`; `tools/refusal_vocabulary_check.py` = `c448646b955bd2200d5f3062a397791530300a29a32b353a62d7f13919ae8dee`.
- `tools/prereg_lint.py` exited 0 with 97 advisory legacy citations and 0 blocking findings. Per the brief, I did not report those option-D advisories.
- `tools/prereg_counts.py` independently returned 16 class P / 8 class E and prose/table agreement.
- `tools/refusal_vocabulary_check.py` returned 0 problems; its 32-control self-test returned 0 failures. The V83 negated-form repair held for its stated patterns.
- `tools/lifecycle_derivation_check.py` returned 0 problems and its nine-control self-test returned 0 failures. F3–F5 are semantic failures outside its byte-copy scope.
- `tools/void_registry.py` returned a clean six-control self-test and correctly disclaims semantic coverage.
- Independent AST enumeration reproduced 112 raises: 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, and 1 bare re-raise. I did not re-derive the parked per-raise/per-call-site defect.
- The V83 lowercase-escape and post-NFC-collision repairs defeat V82’s two concrete unique-JSON counterexamples. The opening-authorization field-name tuple ends in `schema_version` and matches Clause 6; I did not count another stale-name finding.
- I did not re-derive the brief’s parked availability-code, durable-pre-verdict-state, strata/producer, VOID partition, logged-object membership, BS-3g lifecycle cycle, freeze-exemption, BS-2v, `require_authorization`, draw-discipline, or Row-L phase issues.

## Evidence and scope

Read in content: the governing V83 brief; the full 1,516-line draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `tools/refusal_vocabulary_check.py`; the prior V82 seat reports; and, only after independently deriving the candidate failures, the already-present V83 CODEX report as a convergence cross-check. Executed read-only hash, lint, count, lifecycle, refusal, VOID, AST-closure, and content-search probes. The repository had extensive unrelated pre-existing dirty/untracked state. I changed no draft, spec, reference, checker, registry, receipt, or gate artifact other than this assigned report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V83
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1183–1191, 1231, 1449–1461 | replay_harness_sha256 has no named harness artifact or literal independently frozen expected digest.
F2 | HIGH | REPAIR-REQUIRED | §11 lines 1336–1390; pinned module import blocks | PRE-BINDING protects v9 only; mutable dependency imports can consume transient swapped bytes restored before the end recheck.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 598–609, 724–731 | Events appended after checkpoint sealing but during BS-L issuance fit neither the sealed checkpoint nor the post-issuance continuation.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 600–610; lifecycle spec lines 158–164 | ANY-prior-run recurrence has no authenticated complete history domain and loses aborted, voided, or enumeration-failed runs.
F5 | MEDIUM | REPAIR-REQUIRED | lifecycle spec lines 19–21, 81–95; §11 lines 1508–1512 | Atomicity does not make abort always available for a commit wedged inside storage, leaving the deadline lifecycle non-total.
F6 | HIGH | REPAIR-REQUIRED | §6.1 Clause 3 lines 724–727; STRING_FIELD_REGISTRY line 124 | lockbody.bound_digests points to Clause 3(a), which contains no lock-body field enumeration.
F7 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 664–678; gen_string_field_registry.py lines 225–309 | Manually hard-coded schema inventories still permit silent omission despite the generator’s extraction claim.
<!-- END FINDINGS-BLOCK -->