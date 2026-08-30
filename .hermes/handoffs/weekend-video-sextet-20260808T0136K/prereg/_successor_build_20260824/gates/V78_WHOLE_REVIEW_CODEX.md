# V78 whole-document adversarial referee — CODEX

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V78_REVIEW.md` first and verified the subject at sha256 `b4a9c69d9389e66202bdfa3fe41468dc7af14ca993ce3f3fcbb64f92cc70cb5d` before reading it. V78 closes several literal V77 defects, but six repair-required defects survive. The native-load closure is a snapshot rather than a run-closed set; nested manifest paths still evade the string rule; ordering explanation causes does not stop χ-correlated applicability; the recurrence repair still accepts a vacuous changed revision; G2's new auditability split names no gate or verifier that enforces reason truth; and several canonical digest-ref bodies still lack reproducible byte encodings.

## Findings

### F1 — HIGH — the dynamic-load manifest closes what was loaded at freeze, not what can load during replay

V78 §11 lines 1330–1348 adds `dynamic_load_manifest`, defined as the linker-resolved transitive closure of shared objects “the interpreter and roots load,” recorded at freeze, and says only the linker and kernel remain above it. That is not a closed runtime boundary. It records the objects mapped while the freeze probe runs; it does not forbid or detect a later `dlopen`, a lazy extension import, a NumPy plugin/backend, or locale/codec data first opened after the verifier has recomputed the manifest.

The pinned reference makes the timing defect concrete. `successor_ref_v9.py` imports NumPy at line 47, constructs generators lazily through `np.random.default_rng` at lines 160–161, and dynamically imports the frozen planner with `importlib.util` at lines 269–276. A freeze probe can therefore record a truthful manifest and a replay can subsequently map or open an answer-affecting object absent from it. The verifier described at line 1337 only recomputes the recorded closure from disk; it does not trace the replay, reject a new mapping/open, or compare the final mapped-object set after every verdict cell. An omitted third-party object is neither the linker nor the kernel, so the declared stopping boundary does not cover it.

Required repair: make the manifest a runtime allowlist, trace mappings and verdict-relevant data opens through the complete replay, refuse any object first loaded outside the frozen set, and compare the final runtime set to the receipt. If verdict-relevant locale/codec/plugin data is intentionally trusted rather than pinned, name that additional trust boundary instead of saying the boundary stops at linker and kernel.

### F2 — HIGH — nested root/manifest path strings remain outside the string rule

V78 repairs `interpreter_path` itself with an absolute-POSIX/printable-ASCII/256-byte bound, but it gives no corresponding value-domain or byte bound to each `path` component in `dependency_roots` or `dynamic_load_manifest` (§11 lines 1330–1337). Both are ordered `(path, digest)` lists and therefore contain string-bearing leaves.

The supposedly exhaustive registry collapses each whole structured field to `digest-ref` (`ref/STRING_FIELD_REGISTRY.md` lines 95–98). The generator hard-codes the four BS-7p names in `BS7P_ENV` and assigns the two pair lists `digest-ref` at `ref/gen_string_field_registry.py` lines 84–87 and 206–210; it does not extract or classify their nested `path` leaves. A digest of a structure authenticates whatever path string was chosen; it does not bound that string or turn it into a digest. Thus an arbitrarily long or prose-bearing path can inhabit a conforming non-χ artifact while the generator exits zero, contrary to §6.1 lines 664–687.

Required repair: specify and registry-enumerate the path and digest components separately, including canonical path syntax, normalization/symlink policy, character set and byte bound; make the generator derive those leaves from the declared nested schema rather than force-adding container names.

### F3 — HIGH — precedence removes cause selection but not the χ-correlated applicability channel

V78 §6.1 line 610 answers GPT56-V77 F8 by ordering the five explanation causes and requiring the highest applicable cause. That removes discretion only after the applicable set is fixed. It does not make applicability χ-blind.

A worker or verifier that has legitimately touched a χ-bearing cutout can stall until `VERIFIER-TIMEOUT` applies for one outcome-dependent condition and crash (or lose its lease) for another. The mandatory precedence then deterministically publishes which operational condition became true. The explanation still passes the closed vocabulary, canonical body, join, signature, and precedence checks. The draft expressly says the cause's truth is testimony, not mechanically checked, and classifies explanations as non-χ-bearing by constraint (§6.1 lines 586–610 and 660–685). Ordering a testimony channel does not remove its capacity; it moves the channel from choosing among applicable causes to controlling which causes apply.

This is distinct from the parked object-identity leak. The new leak is in the explanation cause itself and survives even with a fixed object identity and a mandatory highest-cause rule.

Required repair: derive cause applicability from authenticated operational evidence under a pinned verifier whose inputs are χ-blind, or classify the explanation surface as testimony with residual χ capacity and keep it inside the sealed boundary. A precedence rule alone is insufficient.

### F4 — HIGH — a different digest plus the coarse key is still a vacuous re-derivation

V78 §6.1 lines 601–602 repairs GPT56-V77 F7 by refusing a `NAMED-AS-DEFECT` revision whose digest equals the prior vocabulary revision. The remaining predicate still requires only (a) a different digest and (b) text containing the entry's coarse `(row, operation)` key. It does not require a nonempty defect inventory, a replacement refusal code, or a machine-checkable mapping from every joined emission to what was named.

Counterexample: copy the prior vocabulary revision, add `class_key=(D,READ): unresolved` (or any other harmless textual delta), and sign it. Its digest differs; its text contains the key; every existing predicate passes; yet no failure under the merged key is named and no vocabulary member changes. This is exactly the vacuous re-derivation V78 says it prevents, with one byte changed instead of zero. §11 lines 1446–1458 gives the enumeration verifier no stronger discharge test.

Required repair: define a canonical re-derivation artifact with a nonempty defect inventory, joins to all emissions under the triggering key, and explicit named replacement code(s) or a blocking unresolved disposition. Verify semantic linkage, not digest inequality plus substring presence.

### F5 — HIGH — the G2 reason-truth split adds prose, not a consuming verifier

`LIFECYCLE_GUARANTEE_SPEC.md` line 31 and V78 §6.1 line 625 require every specific refusal code to be true. V78 line 626 now says recomputable conditions are audit-checkable and “the auditor recomputes them,” while availability conditions are testimony. But the access-log schema at line 589 still carries only the selected reason token, not the completed permission verdict or evidence that established it, and §11 contains no reason-truth verifier or gate consultation. The enumeration verifier consumes only `REFUSED-UNCLASSIFIED` events.

Counterexample: at a phase already reached, Row B emits the schema-valid specific code `REFUSED-PHASE-NOT-REACHED`. The chain itself disproves it, but because it is not `REFUSED-UNCLASSIFIED`, all five enumeration passes ignore it. Nothing in the required build inventory blocks BS-L, opening, BS-7f, BS-V, or disclosure on that false code. Saying a post-hoc auditor could notice it does not make G2 hold and does not prevent a false specific token from bypassing the catch-all guard.

The availability/testimony boundary is also not as absolute as stated: custody-consistent successful touches to the same immutable sealed object before and after an `OBJECT-ABSENT` refusal, with no intervening write or VOID event, can contradict the refusal under the draft's own store invariants. At minimum, the verifier must attempt every chain-recomputable contradiction before falling back to testimony.

Required repair: bind permission-decision evidence to the refusal commit, implement a separately pinned reason-truth verifier, and require a fresh pass at every gate that currently consumes the enumeration verifier. Define testimony as the residual after all chain-recomputable conditions and contradictions, not as a blanket category by code family.

### F6 — HIGH — registry `digest-ref` labels still name canonical bodies whose bytes are not reproducible

The registry says `canonical.freeze_signature_body`, `canonical.lock_body`, `canonical.opening_authorization`, `canonical.entry_body`, and `canonical.explanation_body` all have a written “field-order encoding” (`ref/STRING_FIELD_REGISTRY.md` lines 99–104). The draft does not provide one common byte encoding.

- BS-L's body (§6.1 line 726) names fields in canonical order but gives no scalar encoding, field framing, separator, length prefix, or nested-list encoding.
- The opening-authorization body (line 735) lists fields but does not even state their order.
- The freeze-signature body (§11 line 1174) delegates to “the same canonical field encoding BS-L's lock body uses,” but that encoding is not defined; the reference `field()` length-prefix function cannot supply it because BS-L is absent from frozen v9 and the successor implementation is unresolved.
- The entry and explanation bodies state field order, but not the encoding of values, optional fields, parameter names/values, or signatures into bytes.

Two independent implementers can therefore bind the same logical fields and produce different body digests, while the generator remains green because `CANONICAL` is a hard-coded set (`ref/gen_string_field_registry.py` lines 72–79 and 208–210), not extracted proof that an encoding exists. V78 correctly leaves `canonical.provenance_record` as `SCHEMA-PENDING`; the other bodies need the same honesty until their byte contracts exist.

Required repair: define one explicit canonical field serializer (types, framing, ordering, optional-field rules, nested collection rules, Unicode/ASCII policy) and apply it to every body, with independent serializer/verifier fixtures. Make the registry generator derive each canonical row from that actual definition rather than force-adding its name.

## Attacks that held

- The required subject digest matched before reading. The lifecycle spec matched its pin `eeead2285f6a905cd2e92b7ab853de4f383b6000d25d3428b10e5d7bb2f3bf49`; frozen v9 and its worker matched `6a9abbbd…` and `28f8e1f9…`.
- `tools/prereg_lint.py` exited 0 with 16 class-P / 8 class-E and 97 advisory, 0 blocking findings. I did not re-report the principal-parked legacy citation advisories.
- `tools/prereg_trace.py` reproduced 77 transitions with 0 problems; its three scope controls passed.
- `tools/refusal_vocabulary_check.py` passed V78 and its 27-control self-test. The live checker digest is `bd317939d6866aaebbfd17f57f671486dba19f4ce8510145c02b8e464c63ff48`, matching the draft's prefix.
- `tools/lifecycle_derivation_check.py` passed the draft/spec pair and its 9-control self-test. This establishes byte derivation, not semantic completeness; F5 attacks a guarantee both files share.
- `tools/void_registry.py` found 54 antecedents and 20 §6.1 rows; all six controls passed. The phase-Any entries for forbidden acts, protocol deviation and digest deviation remain present.
- Independent AST enumeration found 112 `Raise` nodes; the classification ledger has 112 unique rows with exactly the same line set. I found no new per-statement omission and did not re-report the parked per-call-site-unit defect.
- The 24-byte UTC timestamp repair is a real capacity bound. Leap-second syntax does not change its byte count, and `Z` blocks timezone-offset smuggling.
- `canonical.provenance_record` is now honestly `SCHEMA-PENDING`; the perturbation manifest now has a reproducible decimal-ASCII serialization; and a render commit that opens no session now destroys its buffer at request end.
- The three ≤64-byte interpreter strings provide a real encoding bound. If the adversary owns the interpreter, those chosen values add no capability beyond the explicit interpreter trust declaration.
- I did not attack the draw discipline or re-derive any issue parked or referred by the brief.

## Evidence ledger and scope

Read before the subject: `gates/BRIEF_V78_REVIEW.md`. Read in full or by targeted line windows: exact V78 bytes; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/successor_ref_v9.py`; `ref/closure_worker_v9.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/_registry_counts.txt`; `tools/refusal_vocabulary_check.py`; and both V77 whole-review reports only to distinguish old findings from failed repairs, with every retained claim checked against V78/current files.

Executed read-only: SHA-256 recomputation; V77→V78 byte diff; prereg lint; trace check and self-test; refusal checker and self-test; lifecycle derivation check and self-test; VOID registry check and self-test; AST raise/ledger reconciliation; registry/source searches. I did not run `ref/gen_string_field_registry.py` because it writes generated files. No draft, reference, checker, registry, or other project file was modified; this report is the sole intended write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V78
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1330–1348 | freeze-time dynamic-load snapshot does not forbid lazy verdict-affecting loads during replay
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 664–687; §11 lines 1330–1337 | dependency-root and dynamic-manifest path leaves remain unbounded and invisible behind digest-ref containers
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–610 and 660–685 | cause precedence moves the χ channel into applicability rather than removing it
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 601–602 and 610; §11 lines 1446–1458 | a changed revision containing only the coarse key still vacuously discharges NAMED-AS-DEFECT
F5 | HIGH | REPAIR-REQUIRED | lifecycle spec line 31; §6.1 lines 589 and 625–626; §11 | G2 reason truth has no evidence binding or consuming verifier, so false specific codes bypass catch-all gates
F6 | HIGH | REPAIR-REQUIRED | §6.1 lines 610, 726 and 735; §11 line 1174 | canonical digest-ref bodies still lack a reproducible common byte encoding
<!-- END FINDINGS-BLOCK -->