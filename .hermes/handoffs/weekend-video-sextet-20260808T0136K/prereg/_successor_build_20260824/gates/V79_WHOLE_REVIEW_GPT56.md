# GPT56 V79 whole-document adversarial referee report

**VERDICT: NOT CLEAR.** The pinned V79 bytes are not a coherent preregistration even as an honestly unfinished programme. Four new defects survive attack: the replay-end closure rests on an AST claim contradicted by the pinned reference and on a current-state enumeration that cannot detect transient loads; the canonical opening-authorization body has two incompatible field sets; the new `OBJECT-ABSENT` audit rule treats past presence as proof of present presence; and the string registry hides the opening body's leaves behind one digest-ref row.

## Findings

### F1 — HIGH — replay-end enforcement is neither the claimed AST-closed program nor a load-history check

V79 §11 lines 1338–1346 says replay-end enforcement enumerates `sys.modules` and the loader image list and then makes the load surface safe because the frozen reference and counterfactual path contain **“no dynamic-load constructs — no `ctypes`, no `dlopen`, no `importlib` dynamic use — auditable once by AST.”** The pinned reference disproves that literal premise: `ref/successor_ref_v9.py` lines 266–277 imports `importlib.util`, calls `spec_from_file_location`, creates a module, inserts it into `sys.modules`, and executes it through `spec.loader.exec_module`. The draft's own §0 makes these bytes normative and says code beats prose.

The proposed end check is also a snapshot, not an enumeration of what was *actually loaded over time*. A Python module can affect state and then be deleted from `sys.modules`; a native image can affect state and be unloaded before the final loader-image query. Neither is in the enumerated end state. Auditing only v9 and the wrapper also does not establish that pinned dependencies never perform a lazy load. Therefore the mechanism does not support “a late load is a violation, never a need,” and it does not defeat the brief's load-then-unload attack.

**Required repair:** replace the false AST absence claim with a real import/load inventory over every reachable pinned dependency and require a monotone load-event trace or an execution boundary that prevents unmanifested loads at load time. A final-state comparison alone cannot prove historical closure.

### F2 — HIGH — the canonical opening-authorization body has contradictory preimages

V79 §6.1 line 610 declares the opening authorization's canonical field order as exactly `(authorizer_identity, lock_digest, timestamp)`. But §6.1 Clause 6, line 735, says the canonical opening-authorization body binds exactly the BS-L digest, **both store identities**, declared post-unblinding destination, unique one-use ceremony identifier, phase P7, Duho's signer identity bound to the BS-2k key, and schema/version. Those are not the same ordered body: line 610 omits both store identities, destination, ceremony identifier, phase, and schema/version, while adding a timestamp Clause 6 does not name.

The one-encoding repair therefore does not close the digest-without-preimage defect. An implementer can obey either field list and reject the other's bytes; worse, the three-field interpretation drops the replay identity and destination that Clause 6 makes security-critical.

**Required repair:** define one ordered opening-authorization field list containing every Clause-6 field, state the representation of composite fields such as the two store identities, and make Clause 6 and the canonical-body paragraph byte-identical in content and order.

### F3 — HIGH — `OBJECT-ABSENT` is not falsifiable merely because the object existed earlier

V79 §6.1 line 626 classifies `REFUSED-OBJECT-ABSENT` as “falsifiable-from-history” and says **a prior committed touch of the same object contradicts it**; the §11 audit pass must enforce that at five gates. This confuses past existence with present existence. A truthful sequence is: Row B commits a read/render touch while the object exists; the object later becomes absent because of a storage fault or forbidden deletion; a later request is truthfully refused as `REFUSED-OBJECT-ABSENT`. The prior touch proves only that the object existed at the earlier event. It does not contradict absence at the later timestamp.

“Append-only” and “mutation is forbidden” do not rescue the inference: an integrity/storage fault or forbidden act can still make bytes disappear, and availability refusals exist precisely because store state can fail. The proposed audit would reject a truthful G2 event and force an incorrect code or testimony solely to satisfy history.

**Required repair:** treat present absence as testimony unless a contemporaneous or later authenticated observation proves the object present for the same request, or redefine the code to mean “object never existed in committed history.” Do not use an earlier touch as a contradiction of a later state.

### F4 — HIGH — the registry generator misses the opening body's string-bearing leaves

The generated `ref/STRING_FIELD_REGISTRY.md` claims mechanical enumeration cannot silently omit a declared field, but it contains only the aggregate row `canonical.opening_authorization` as `digest-ref` (line 103). It has no rows for the opening body's `authorizer_identity`, store identities, destination, ceremony identifier, phase, or schema/version. `ref/gen_string_field_registry.py` lines 72–79 and 228–230 hard-code the canonical body as one container row; its extraction at lines 194–212 does not descend into canonical-body field lists. The access-log `timestamp` row does not fix this—it is explicitly scoped to the §6.1 event schema, not the opening authorization.

This repeats the exact container/leaf failure V79 says it repaired for `dependency_roots` and `dynamic_load_manifest`: a fixed-size digest wrapper does not constrain the strings in its preimage. Under Clause 6, arbitrary destination, identity, ceremony, and schema/version text can enter the canonical non-χ body while the registry stays green. The registry's “no unclassified string field” claim is therefore false.

**Required repair:** extract and register every leaf of every canonical body, including composite-entry leaves, with closed vocabularies or explicit bounded encodings. Add deletion/format-drift controls proving each canonical leaf is found rather than hard-coding only the body container.

## Failed attacks / checks that held

- Subject identity held: sha256 independently recomputed as `01d3877a2973fff901b16d0668bb0438e7cc42ca6ae0ea35429f65c474972561` before the draft was read.
- Referenced pins held: lifecycle spec `eeead228…`, refusal checker `412a086…`, and frozen v9 `6a9abbbd…` matched the draft.
- `tools/prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; I did not re-report the permanent option-D legacy citations.
- `tools/prereg_counts.py` independently returned 16 class P / 8 class E and prose match.
- `tools/prereg_trace.py <build> --check <V79>` returned 78 transitions and 0 problems.
- `tools/void_registry.py` returned 54 antecedents, 20 §6.1 rows, and no failure.
- `tools/lifecycle_derivation_check.py` returned 0 problems; its self-test returned 9 controls, 0 failures.
- `tools/refusal_vocabulary_check.py` returned 0 problems; its self-test returned 28 controls (1 negative), 0 failures, every code controlled.
- The five-cause applicability token's per-emission alphabet bound `log₂5` is arithmetically correct. The defect found this round is not that bound.
- The `NAMES-CLASS: <class_key> AS <token>` repair is parseable and checks token membership; I do not count its explicitly acknowledged semantic adequacy testimony as a new defect here.

## Evidence and scope

Read in full: the V79 draft, `LIFECYCLE_GUARANTEE_SPEC.md`, `ref/RAISE_SITE_CLASSIFICATION.md`, `tools/refusal_vocabulary_check.py`, `ref/gen_string_field_registry.py`, generated registry/counts, and the relevant pinned-reference regions. Executed the checkers listed above. I did not modify the subject, spec, reference, checker, registry, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V79
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1338–1346; ref/successor_ref_v9.py lines 266–277 | Replay-end closure relies on a false no-importlib claim and cannot see a load removed before the final snapshot.
F2 | HIGH | REPAIR-REQUIRED | §6.1 line 610 and Clause 6 line 735 | Opening authorization has incompatible three-field and Clause-6 canonical bodies.
F3 | HIGH | REPAIR-REQUIRED | §6.1 line 626 | A prior touch proves past presence, not that a later OBJECT-ABSENT refusal is false.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 664–685; ref/gen_string_field_registry.py lines 72–79, 194–212, 228–230 | Registry hides canonical opening-authorization leaves behind one digest-ref container.
<!-- END FINDINGS-BLOCK -->
