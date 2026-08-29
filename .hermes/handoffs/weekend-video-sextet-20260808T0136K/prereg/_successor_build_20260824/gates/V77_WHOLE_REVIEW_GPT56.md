# V77 whole-document adversarial referee — GPT56

## Verdict

**NOT CLEAR.** I verified the subject at sha256 `d2d61a274c8c0739b4cd1b597265f7d7a1580d19a150b420235af9ca7901cfee` before reading it. V77 repairs the literal V76 bounds and adds real bootstrap fields, but the new fields evade the registry that is supposed to make omissions blocking; the bootstrap does not bind the native code actually loaded; two claimed canonical bodies are still undefined; and several lifecycle/string controls remain promises whose counterexamples pass the specified predicates. The green lint therefore does not establish the advertised guarantees.

## Findings

### F1 — HIGH — the new BS-7p bootstrap sub-schema is invisible to the exhaustive string registry

V77 §11 lines 1326–1330 adds `interpreter_path`, `interpreter_sha256`, and `dependency_roots` as ordered `(path, digest)` pairs. None appears in `ref/STRING_FIELD_REGISTRY.md`; registry line 67 instead continues to classify the entire `BS-7p.environment` value as a scalar `closed-vocab`. The path leaves have no closed set, byte bound, or canonical path encoding.

This is a generator hole, not merely a stale generated file. An in-memory import of `ref/gen_string_field_registry.py` returned `False` for all three names from `extract(V77)`. Its extractor at lines 170–184 does not parse this nested sub-schema. The promised default-forbidden rule therefore cannot see the very fields V77 added.

Required repair: enumerate and constrain every nested field and every root-pair component, and make the generator derive them from the sub-schema rather than retaining the obsolete scalar classification.

### F2 — HIGH — receipt-listed dependency roots do not bind the transitive native code that computes verdict cells

V77 §11 lines 1326–1339 requires hashing the interpreter and receipt-listed dependency roots, then says configuration rebinding has been removed. It defines no canonical directory/tree digest, symlink policy, load-completeness predicate, or rejection of mapped objects outside the listed roots. A receipt can therefore truthfully hash every object it lists while omitting an answer-producing native dependency.

That path is real, not hypothetical. `ref/gain_gradient_estimator.py` uses `np.linalg`; read-only `otool -L` inspection showed NumPy's `_multiarray_umath` loading `@loader_path/../.dylibs/libopenblas64_.0.dylib`, while the Python executable itself loads a separate `@executable_path/../Python3`. Whether a sufficiently broad root happens to include one observed dylib is irrelevant: V77 neither requires such a root nor verifies dyld's transitive view. An omitted mutable third-party dylib is not the interpreter binary and is not necessarily an OS object covered by the declared trust boundary.

Required repair: define canonical tree hashing and symlink handling, trace the transitive import/dynamic-load closure, and refuse every mapped non-OS object outside pinned roots or an explicit frozen allowlist.

### F3 — HIGH — at least two canonical digest-ref rows have no canonical preimage schema

V77 §6.1 line 669 says six canonical bodies joined the registry. Registry lines 95–100 classify all six as `digest-ref` under a canonical field-order encoding. But no ordered provenance-record field set, encoding, or verifier exists in V77; the only operative change is that `BS-1b.provenance` points to such a record. The explanation body is also not fully canonical: §6.1 line 610 names `cause`, unspecified “bounded numeric parameters (durations, counts),” and a join, but gives no exact parameter field list or field order.

The generator cannot detect either absence. `ref/gen_string_field_registry.py` lines 195–197 force-add the six names through the hard-coded `CANONICAL` set. In-memory reproduction found `canonical.provenance_record` in `CANONICAL` while `provenance_record` was absent from `extract(V77)`. A canonical name hard-coded beside a missing body is `SCHEMA-PENDING` wearing `digest-ref`.

Required repair: give every canonical body an exact ordered field schema, encoding, and verifier, and derive registry rows from those definitions. Until then, classify the undefined bodies honestly as pending.

### F4 — HIGH — the access-log `timestamp` has no bound despite being labelled bounded

V77 §6.1 line 589 declares `timestamp` in the access-log event schema and nowhere defines its type, format, character set, or byte limit. Nevertheless `ref/gen_string_field_registry.py` line 147 manually classifies it as `bounded-encoding`, and `ref/STRING_FIELD_REGISTRY.md` line 158 repeats that classification with an empty note.

Arbitrary text can therefore occupy `timestamp` while the registry generator remains green. This is the same contradiction V77 repaired for `python`, `platform`, and `machine`: “bounded-encoding” with no declared or enforceable bound.

Required repair: freeze a canonical timestamp representation and byte/range bound with verifier enforcement, or mark the field pending until BS-2k defines it.

### F5 — HIGH — G2's refusal-reason truth has no evidence binding or verifier

`LIFECYCLE_GUARANTEE_SPEC.md` line 31 and V77 §6.1 line 625 require a specific refusal code to assert a condition actually established; an undecided permission check may carry only `REFUSED-UNCLASSIFIED`. But the event schema at V77 line 589 carries only the selected reason token, not the completed permission verdict or evidence that established it. The enumeration verifier at lines 606–610 and 1437–1449 selects events already labelled `REFUSED-UNCLASSIFIED`; it does not recompute whether a specific token was true.

Counterexample: the permission verifier times out, but Row B emits the schema-valid `REFUSED-PRECONDITION-UNVERIFIED`. The event, signature, chain, atomic commit, and all five enumeration passes can succeed because no catch-all event exists. G2 is false and every specified checker is green.

Required repair: bind authenticated permission-decision evidence (including undecided state) into the event/binding domain and require an independent verifier to recompute reason-token truth before each consuming gate.

### F6 — HIGH — a committed render can open no session and leave its buffer with no destruction trigger

`LIFECYCLE_GUARANTEE_SPEC.md` line 34 calls commit↔session ownership “one-to-one” but only requires that each render commit open **at most** one session. N1 and W3 (lines 53–66) permit a committed render whose frame is never delivered. Yet render-buffer destruction at lines 116–125 is tied to the view session ending; the “delivery completion or request end” fallback at lines 126–130 is stated for conveyance buffers, not render buffers. V77 lines 633 and 652–653 reproduce that split.

Counterexample: Row B commits `{render buffer, event, binding}`, then the interface crashes before the first frame. No session opens, which “at most one” and N1 permit. No session can therefore end, so no specified trigger destroys the render buffer. The claimed bijection is false and a redisplayable surface can survive with no live session.

Required repair: define commit-without-session as a terminal branch with bounded lifetime and mandatory destruction, and bind commit/session identifiers so zero-, one-, and duplicate-session cases are mechanically checked.

### F7 — HIGH — `NAMED-AS-DEFECT` can discharge without naming any defect

V77 §6.1 lines 601–602 claim that a recurrence forces re-derivation which names every distinct failure found under the coarse `(row, operation)` key. But line 610 and §11 lines 1437–1449 require only that the re-derived revision exist and contain the entry's `class_key`. The access-log event at line 589 carries no failure cause, while a `NAMED-AS-DEFECT` entry may not carry `explanation_ref`.

Counterexample: two `(D, READ)` catch-alls arise from different causes. Submit a signed revision saying only `class_key=(D,READ): unresolved; no code added`. Its digest resolves and its text contains the key, so the stated predicate accepts the second entry as `NAMED-AS-DEFECT`, although no defect or new vocabulary member was named. The guard can therefore become routine through a vacuous re-derivation.

Required repair: define a canonical re-derivation body containing the joined emissions and an explicit nonempty defect inventory, and make discharge depend on machine-checkable linkage to named replacement code(s), not substring presence of the coarse key.

### F8 — MEDIUM — the closed explanation vocabulary remains a mechanically valid χ channel

V77 lines 586–587 and 660 classify enumeration explanations as non-χ-bearing by constraint. Line 610, however, admits that whether the selected `cause` actually happened is unverifiable testimony. Closing `cause` to five tokens narrows capacity but does not make token selection non-χ by construction.

Counterexample: for a real timeout, emit `VERIFIER-TIMEOUT` when the joined object's χ bit is 0 and `DEADLOCK` when it is 1. Both values are in the closed set; joins, bounds, canonical body, and signature pass; `(row, operation)` cannot detect the false cause. The explanation channel therefore leaks at least `log2(5)` chosen bits per entry while every mechanical constraint holds.

Required repair: derive the cause token from authenticated operational evidence under a pinned verifier, or classify the explanation surface as testimony with residual χ capacity rather than non-χ by construction.

### F9 — MEDIUM — retired/active vocabulary semantics still diverge from the checker in both directions

`tools/refusal_vocabulary_check.py` lines 121–144 closes activation semantics with a finite synonym regex. Appending `REFUSED-LOCK-NOT-OPEN was deleted but is now mandatory.` to the exact V77 bytes in memory returned `[]`: “deleted” grants the exemption and “mandatory” restores force without matching `ACTIVATION`.

The inverse also passes. Lines 134–136 add every token in `CODES` to `pinned` before retirement logic applies. If the active occurrence of `REFUSED-OBJECT-ABSENT` is removed and the only occurrence is `REFUSED-OBJECT-ABSENT was deleted.`, `check()` still returns `[]`; a tombstone is counted as the required active member. Thus neither prose nor the checker's dict reliably governs operative membership.

Required repair: accept retired tokens only in one canonical tombstone grammar and reject normative/modal material around them; separately require each current member in a canonical active vocabulary block that retirement prose cannot satisfy.

### F10 — MEDIUM — the perturbation-manifest digest has no reproducible byte encoding

V77 §11 lines 1219–1221 define `perturbation_manifest_sha256` as the digest of a “canonical, ordered list” of γ values, and lines 1390–1394 demand independent recomputation. Nowhere does V77 specify whether values are float64 bytes or decimal strings, separators/framing, signed-zero treatment, NaN rejection at serialization, or endianness. `ref/gain_counterfactual_path.py` converts the grid to NumPy float64 and checks ordering but implements no manifest serialization or digest.

This is not cosmetic: two independently conforming encoders can represent the same evaluated grid with different bytes and digests. V77 itself shows the needed standard at lines 1371–1375, where the verdict matrix serialization is defined exactly.

Required repair: freeze the manifest's scalar encoding, framing, order, and normalization byte-for-byte, and pin a serializer/verifier fixture.

### F11 — LOW — V77 still carries the hand-copied counts it says it removed

V77 §6.1 line 669 says “the nine non-slot artifact classes” and “145 fields,” then later on the same physical line says the counts are generated and that the generator reports ten classes and seven pending. `ref/_registry_counts.txt` says `total=151 nonslot=10 pending=7`; the registry contains 151 rows.

The same paragraph therefore asserts both old and new inventories while claiming hand-copy drift has been eliminated.

Required repair: delete the stale nine/145 assertions and render the one generated count quotation as the sole inventory statement.

## Attacks that held

- The subject digest matched before reading and again after the attack pass. The companion lifecycle digest matched V77's pin (`22c65dcfe4272b8e2e69d30746275c05b75c06a855157b2db0e5b2c8498c2c27`), and frozen v9 matched `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings. I did not re-report the 96/97 legacy citation advisories parked by the brief.
- `tools/refusal_vocabulary_check.py` passed V77 and its 25-control self-test. F9 is a semantic counterexample outside that battery, not a claim that the shipped controls fail.
- The three printable-ASCII ≤64-byte environment bounds are real capacity bounds. If the adversary already owns the interpreter, the chosen 64-byte values buy no capability beyond the draft's explicit interpreter trust declaration; I do not score that channel separately.
- BS-3g remains explicitly DESIGN/UNFILLED with unset draw parameters. I did not re-attack the draw discipline or re-derive the parked BS-3g lifecycle cycle.
- The `Any` phases for forbidden acts, protocol deviation, and digest deviation remain present in §7.1. Class counts reproduce as 16 class-P / 8 class-E.

## Evidence ledger and scope

Read in full or by targeted line windows: `gates/BRIEF_V77_REVIEW.md` first; exact V77 bytes; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/_registry_counts.txt`; frozen `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `ref/gain_gradient_estimator.py`; `tools/refusal_vocabulary_check.py`; and the concurrent CODEX report only as a lead, with every retained claim independently reproduced.

Executed read-only: SHA-256 recomputation; prereg lint; refusal checker and self-test; in-memory generator extraction probes; in-memory retirement/activation mutations; registry-row/count reconciliation; targeted AST/source inspection; and Mach-O dependency inspection. I created or modified no project artifact other than this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V77
VERDICT: NOT CLEAR
COUNT: 11
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1326–1330; registry line 67; generator lines 170–184 | BS-7p's nested interpreter/root fields bypass the exhaustive string registry and have no declared path bounds
F2 | HIGH | REPAIR-REQUIRED | §11 lines 1326–1339 | listed-root hashing has no transitive dynamic-load closure, so omitted native dependencies can alter verdict computation
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 610, 669; registry lines 95–100; generator lines 195–197 | canonical provenance and explanation digest-refs lack exact canonical preimage schemas
F4 | HIGH | REPAIR-REQUIRED | §6.1 line 589; registry line 158; generator line 147 | timestamp is labelled bounded-encoding without any format or byte/range bound
F5 | HIGH | REPAIR-REQUIRED | lifecycle spec line 31; §6.1 lines 589, 606–610, 625; §11 lines 1437–1449 | specific refusal-reason truth is normative but no evidence binding or verifier can detect a false specific code
F6 | HIGH | REPAIR-REQUIRED | lifecycle spec lines 34, 53–66, 116–130; §6.1 lines 633, 652–653 | a render commit may open no session and its buffer then has no specified destruction trigger
F7 | HIGH | REPAIR-REQUIRED | §6.1 lines 589, 601–602, 610; §11 lines 1437–1449 | NAMED-AS-DEFECT accepts a revision containing only the coarse key, so a vacuous re-derivation can discharge recurrence
F8 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 586–587, 610, 660, 682–684 | unconstrained truthful selection among five cause tokens remains a mechanically valid χ channel
F9 | MEDIUM | REPAIR-REQUIRED | §6.1 line 618; tools/refusal_vocabulary_check.py lines 121–144 | unlisted activation wording and active-code tombstones both make prose semantics diverge while the checker stays green
F10 | MEDIUM | REPAIR-REQUIRED | §11 lines 1219–1221, 1371–1375, 1390–1394 | perturbation_manifest_sha256 has no reproducible byte serialization contract
F11 | LOW | REPAIR-REQUIRED | §6.1 line 669; ref/_registry_counts.txt line 1 | stale nine/145 inventory prose contradicts generated 10/7/151 counts
<!-- END FINDINGS-BLOCK -->
