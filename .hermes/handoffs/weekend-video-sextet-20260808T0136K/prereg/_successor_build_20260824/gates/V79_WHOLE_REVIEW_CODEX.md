# V79 whole-document adversarial referee — CODEX

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V79_REVIEW.md` first and verified the subject at sha256 `01d3877a2973fff901b16d0668bb0438e7cc42ca6ae0ea35429f65c474972561` before reading it. V79 repairs several literal V78 findings, but seven repair-required defects survive. The replay-end manifest check is a current-state snapshot resting on an AST claim contradicted by the pinned reference; the opening authorization has two incompatible canonical bodies; the new `OBJECT-ABSENT` rule mistakes past presence for present presence; the supposedly exhaustive string registry hides canonical-body leaves; the `NAMES-CLASS` template accepts a wrong or vacuous member; `field()` frames already-encoded bytes but does not canonicalize logical payloads; and the expanded retirement guard still accepts direct semantic reactivation.

## Findings

### F1 — HIGH — replay-end enforcement cannot see transient loads, and its no-importlib premise is false

V79 §11 lines 1338–1346 says that after verdict computation the process enumerates `sys.modules` and the native loader image list, rejects objects outside the manifest, and relies on the frozen reference and counterfactual path containing “no dynamic-load constructs — no `ctypes`, no `dlopen`, no `importlib` dynamic use.” Both parts fail.

First, the pinned reference directly contradicts the AST premise. `ref/successor_ref_v9.py` lines 266–277 imports `importlib.util`, calls `spec_from_file_location`, creates a module, inserts it into `sys.modules`, and executes it with `spec.loader.exec_module`. These are the exact dynamic-import constructs the draft says are absent, and §0 says the pinned code beats prose.

Second, an end-state enumeration is not an enumeration of what was actually loaded during replay. A Python module can execute and then be removed from `sys.modules`; a native image can execute and be unloaded before the final image-list query. Either can alter process state or a verdict and be absent from both final snapshots. Auditing only the reference and wrapper also says nothing about lazy loads performed by their pinned dependencies. Thus the repair does not defeat the brief’s load-then-unload attack and does not justify “a late load is a violation, never a need.”

Required repair: enforce the allowlist at each import/load event or retain a monotone authenticated load-event history through result acceptance; inventory every reachable pinned dependency; and replace the false AST-absence claim with a check that matches the actual pinned bytes.

### F2 — HIGH — the opening authorization has two incompatible canonical preimages

V79 §6.1 line 610 declares the opening authorization’s order as `(authorizer_identity, lock_digest, timestamp)`. Clause 6 at line 735 says the canonical opening-authorization body binds exactly the BS-L digest, both store identities, the declared post-unblinding destination, a unique one-use ceremony identifier, phase P7, Duho’s signer identity bound to the BS-2k key, and schema/version.

Those are not two descriptions of one body. The three-field body omits the store identities, destination, ceremony identifier, phase, and schema/version, and adds a timestamp absent from Clause 6. An implementer following line 610 produces different bytes from one following Clause 6; worse, the three-field interpretation drops the replay and destination bindings Clause 6 makes security-critical.

Required repair: define one ordered field list containing every Clause-6 field, specify the representation of composite fields such as both store identities, and make the canonical-body paragraph and Clause 6 byte-identical in content and order.

### F3 — HIGH — a prior touch does not falsify a later truthful `OBJECT-ABSENT` refusal

V79 §6.1 line 626 classifies `REFUSED-OBJECT-ABSENT` as “falsifiable-from-history,” with a prior committed touch of the same object declared to contradict the refusal. The new §11 audit pass must enforce that rule at all five gates.

A truthful counterexample is straightforward: Row B commits a touch while object X exists; X later becomes unavailable because of storage loss, corruption, failed mounting, or an unauthorised deletion; a later request is truthfully refused as `REFUSED-OBJECT-ABSENT`. The earlier event proves existence only at its own time. It does not prove presence at the later request. Append-only logging and a prohibition on mutation do not make physical disappearance impossible; the availability vocabulary exists precisely because present store state can fail. If the disappearance is also a protocol or VOID event, that does not make the later absence token false.

The proposed audit therefore rejects a true G2 event and pressures the mediator to emit an incorrect code merely because the object once existed.

Required repair: treat present absence as testimony unless contemporaneous authenticated evidence or a later same-request observation proves presence, or redefine the token to mean “no committed history of this object.” Past presence alone is not present-state falsification.

### F4 — HIGH — canonical-body string leaves remain invisible behind digest-ref containers

The generated `ref/STRING_FIELD_REGISTRY.md` claims every string-bearing field in every non-χ artifact is mechanically enumerated, but line 103 contains only the aggregate `canonical.opening_authorization` row. It has no rows for `authorizer_identity`, store identities, destination, ceremony identifier, phase, schema/version, or the newly added timestamp.

The omission is structural. `ref/gen_string_field_registry.py` lines 72–79 and 228–230 hard-code canonical body names as container rows; `extract()` at lines 194–212 does not descend into canonical-body field lists. This is the same container/leaf defect V79 repaired for `dependency_roots` and `dynamic_load_manifest`: hashing a body authenticates whatever leaf strings were chosen but does not close or bound them. An arbitrary destination, identity, ceremony, or schema/version string can therefore inhabit a conforming non-χ artifact while the generator exits zero.

Required repair: generate rows for every leaf of every canonical body, including composite-entry leaves, assign each a closed vocabulary or explicit bounded encoding, and add deletion/format-drift controls proving the leaves are extracted rather than force-added by body name.

### F5 — HIGH — `NAMES-CLASS` verifies syntax and membership, not that the recurring defect was named

V79 §6.1 lines 601–602 replaces the vacuous changed-revision test with `NAMES-CLASS: <class_key> AS <token>` and checks only template parse, key equality, and membership of the token in the revised set. That still accepts naming without naming.

Concrete counterexample: a recurring verifier-timeout defect under `(D, READ)` is discharged by a changed revision containing `NAMES-CLASS: (D, READ) AS REFUSED-OBJECT-ABSENT`. The key parses, the token is a vocabulary member, and the revision digest differs, but the named code is false of the joined emissions. `REFUSED-UNCLASSIFIED` itself or any unrelated pre-existing member creates the same vacuity. The adjacent sentence explicitly relegates adequacy to testimony, so the verifier has no stronger predicate. This defeats the rule’s purpose: a recurring catch-all class can remain routine after a syntactically conforming but semantically unrelated “re-derivation.”

Required repair: bind a canonical defect inventory to the joined emissions under the triggering key and require an explicit mapping from each distinct observed failure to a newly defined or demonstrably applicable code; an unresolved mapping must remain blocking. Existing-member membership alone is not semantic naming.

### F6 — HIGH — `field()` supplies framing, not a canonical encoding for logical payloads

V79 §6.1 line 610 says every canonical body now uses v9’s `field(name, payload)` records. The pinned function at `ref/successor_ref_v9.py` lines 180–182 only frames an already-created `bytes` payload with name and length prefixes. It does not define how a logical integer, timestamp, digest, identifier, parameter map, ordered manifest, signer identity, or pair of store identities becomes those payload bytes.

The gap is immediately concrete in the same paragraph: `chain_position` and explanation parameters are numeric, `parameters…` is a named collection, and the opening authorization contains identifiers and composite fields. Decimal ASCII versus little-endian integers, raw 32-byte digest versus 64-byte hex, and alternative nested-list encodings all produce different canonical-body digests while using `field()` exactly as instructed. Clause 3(b)’s ordered manifest and chain segment have the same unresolved nested-payload problem.

This is distinct from F2: even after reconciling the opening field list, two implementers still cannot reproduce its bytes from the logical values.

Required repair: define canonical payload encoders for every scalar and collection type, including optional-field rules and nested sequence/map framing, then apply those types to every canonical-body field and fixture independent serializer/verifier agreement.

### F7 — MEDIUM — the expanded retired-token guard still accepts direct reactivation prose

`tools/refusal_vocabulary_check.py` lines 121–160 exempts a known retired token when a retirement word shares its fragment unless a finite activation regex matches nearby text. V79 expands that regex and its self-test, but ordinary operative language still passes. Executing the actual checker in memory produced no finding for each of these fragments:

- `REFUSED-LOCK-NOT-OPEN was deleted, but remains operative for future openings.`
- `REFUSED-CEREMONY-CONSUMED was retired, but operators are expected to apply it henceforth.`
- `REFUSED-LOCK-NOT-OPEN was deleted, but should control all future lock attempts.`

Each sentence directly reactivates a retired code while `check()` returns `[]`. The 28-control self-test remains green because it exercises only enumerated activation phrases. The checker comments admit the vocabulary is finite, but the draft simultaneously relies on the guard as blocking/deletion-detecting and the brief specifically requires future-tense reactivation to be attacked.

Required repair: permit retired tokens only in a narrowly canonical tombstone grammar with no adversarial free continuation, or generate operative semantics from a machine-readable active/retired source of truth. Enumerating more English activation verbs cannot establish a semantic negative.

## Failed attacks / repairs that held

- The subject digest matched before reading. The pinned companion and code digests also matched: lifecycle spec `eeead2285f6a905cd2e92b7ab853de4f383b6000d25d3428b10e5d7bb2f3bf49`, refusal checker `412a08673ebcdd0b6e49257aa763df3ed2040cf1f2685304b72a4833ddd98d01`, frozen v9 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, and closure worker `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- `tools/prereg_lint.py` exited 0 with 16 class P / 8 class E and 97 advisory, 0 blocking findings. I did not re-report the principal-parked legacy citation advisories.
- `tools/prereg_counts.py` independently reproduced 16 class-P and 8 class-E rows; prose matched.
- `tools/prereg_trace.py` reproduced 78 transitions with 0 problems.
- `tools/lifecycle_derivation_check.py` reported 0 problems and its nine controls passed. This proves quoted-byte derivation, not semantic completeness.
- `tools/refusal_vocabulary_check.py` reported 0 problems on V79 and its 28-control self-test passed. F7 attacks the untested semantic boundary; it does not misstate the green result.
- `tools/void_registry.py` parsed 54 antecedents and 20 §6.1 rows. I treated that as name coverage only, as the draft requires.
- `ref/RAISE_SITE_CLASSIFICATION.md` carries 112 sites and openly preserves the referred per-call-site-unit limitation. I did not re-derive that parked defect.
- The dependency-root and dynamic-manifest path leaves now have explicit 256-byte POSIX bounds. The explanation parameter-name/arity repair is a genuine closed per-cause schema. The per-emission cause alphabet bound of `log₂5` is arithmetically valid; F5 concerns a different surface.
- I did not attack the draw discipline or re-derive the parked VOID partition, durable pre-verdict state, strata/producer pair, integrity-mismatch collision, BS-3g lifecycle cycle, authorization, call-site unit, Row-L phase, or other principal-referred issues.

## Evidence and scope

Read in content: `gates/BRIEF_V79_REVIEW.md` first; exact V79 bytes; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/successor_ref_v9.py`; `tools/refusal_vocabulary_check.py`; V78 referee reports to distinguish old findings from attempted repairs; and the already-present current sibling report only as a cross-check, with every overlapping claim independently verified against V79/current files.

Executed read-only: SHA-256 recomputation; V78→V79 byte diff; prereg lint; counts and trace checks; lifecycle derivation check and self-test; VOID registry parse; refusal checker and self-test; and in-memory synthetic retirement mutations. I did not modify the draft, companion, reference files, tools, registries, or any file outside this report. This report is the sole intended write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V79
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1338–1346; ref/successor_ref_v9.py lines 266–277 | Replay-end closure relies on a false no-importlib premise and cannot detect a load removed before the final snapshot.
F2 | HIGH | REPAIR-REQUIRED | §6.1 line 610 and Clause 6 line 735 | The opening authorization has incompatible three-field and Clause-6 canonical bodies.
F3 | HIGH | REPAIR-REQUIRED | §6.1 line 626 | A prior touch proves past presence, not that a later OBJECT-ABSENT refusal is false.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 664–685; ref/gen_string_field_registry.py lines 72–79, 194–212, 228–230 | The registry hides canonical-body string leaves behind digest-ref containers.
F5 | HIGH | REPAIR-REQUIRED | §6.1 lines 601–602 | NAMES-CLASS accepts an unrelated existing member and does not prove the recurring failure was named.
F6 | HIGH | REPAIR-REQUIRED | §6.1 line 610; ref/successor_ref_v9.py lines 180–182 | field() frames bytes but leaves logical payload and nested-collection encodings undefined.
F7 | MEDIUM | REPAIR-REQUIRED | tools/refusal_vocabulary_check.py lines 121–160 | Direct reactivation via “remains operative,” “expected to apply,” or “should control” passes the blocking retired-token checker.
<!-- END FINDINGS-BLOCK -->