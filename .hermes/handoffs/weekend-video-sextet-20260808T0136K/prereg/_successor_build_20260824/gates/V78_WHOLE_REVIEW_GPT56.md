# V78 whole-document adversarial referee — GPT56

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V78_REVIEW.md` first and then verified the subject at sha256 `b4a9c69d9389e66202bdfa3fe41468dc7af14ca993ce3f3fcbb64f92cc70cb5d` before reading it. V78 makes several literal V77 repairs, but the new native-load closure still stops at a time snapshot rather than a closed future-load policy; the pre-unblinding explanation schema retains an unregistered string channel; one canonical digest-ref still has no byte preimage; the claimed testimony/audit split is too coarse; and the retired-token activation guard is bypassable by ordinary activation prose it knowingly does not recognize.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §11 lines 1321–1348; `ref/gain_counterfactual_path.py` lines 43–50, 120–152

**`dynamic_load_manifest` does not close dynamic loading after the manifest is recorded.** V78 defines it as the linker-resolved transitive closure of shared objects that the interpreter and roots load, recorded at freeze, and says only the linker and kernel remain above it. That does not specify either (a) a complete trace of every verdict path through process exit or (b) a run-time deny rule for later `dlopen`/extension loads. A file can therefore be absent from the freeze snapshot and be loaded after replay starts by a lazy Python extension, NumPy submodule/plugin, or future preregistered mapping implementation. Such a file sits **below** the declared linker/kernel trust boundary and can alter a verdict while the recorded manifest still recomputes exactly.

The actual wrapper makes this a live boundary, not an abstract OS concern: it imports NumPy and `successor_ref_v9` and then executes a caller-supplied mapping before `v9.perm_record()` and `v9._decide_from()`. Nothing in the manifest clause says that a library first loaded by that mapping or by a lazy native path must already occur in the frozen list, nor does it require the verifier to compare the loaded-image set again after every verdict cell. The repair must define the manifest over the full permitted future-load set or enforce “no new executable/native image after manifest verification,” with a final loaded-image-set comparison. Declaring the linker trusted does not trust arbitrary objects the linker is asked to load later.

### F2 — HIGH / REPAIR-REQUIRED — §6.1 line 610; §6.1 lines 661–685; `ref/gen_string_field_registry.py` lines 181–195, 224–244; `ref/STRING_FIELD_REGISTRY.md` lines 99–104, 132–143

**The canonical explanation body admits unregistered, unbounded parameter names.** Line 610 permits a `cause` plus “bounded numeric parameters (durations, counts)” and defines the digest preimage as `(chain_position, event_digest, cause, parameters…)`, with parameters “sorted by name.” The names and arity are not a closed vocabulary or bounded encoding. A signer can therefore encode arbitrary pre-unblinding text/bits in chosen parameter names while keeping every value numeric and every named cause legal. This defeats both the no-free-prose claim and the statement that the enumeration continuation is non-χ-bearing.

The registry generator demonstrably cannot see this field surface: its `extract()` adds `cause` when that phrase exists but has no extraction for `parameters` or their names. Importing the generator read-only against V78 returned `cause_found=True` and `parameters_found=False`; the emitted registry consequently has a `cause` row but no parameter-name row. “Parameters sorted by name” gives a deterministic order, not a closed domain or a byte encoding. Repair requires a cause-specific closed parameter-name schema, fixed arity, bounds and canonical name/value serialization, or removal of parameters from pre-unblinding explanations.

### F3 — HIGH / REPAIR-REQUIRED — §6.1 clause 3(b), line 726; clause 6, line 735; §11 lines 1172–1175; `ref/STRING_FIELD_REGISTRY.md` lines 99–104

**`canonical.opening_authorization` is classified as a digest-ref with a written field-order encoding, but the draft never writes that encoding.** Clause 6 enumerates semantic fields the authorization “binds exactly”; unlike the explanation body, it does not state their order, field tags, scalar encodings, length framing, or byte serialization. The registry nevertheless marks `canonical.opening_authorization` as `digest-ref` and says its “field-order encoding [is] WRITTEN in this draft.”

The attempted cross-reference does not supply the missing bytes. The freeze-signature clause says it uses “the same canonical field encoding BS-L's lock body uses,” but clause 3(b) merely lists lock-body components “in canonical order”; it likewise gives no byte framing or field encoding, and frozen v9 has no BS-L/opening schema to inherit. Two independent implementers can encode the same decoded fields differently and obtain different digests while each follows the prose. This is the SCHEMA-PENDING defect wearing a digest-ref label. Write the exact ordered field names and canonical byte encoding (including collections and integers) or classify the body honestly as pending.

### F4 — MEDIUM / REPAIR-REQUIRED — §6.1 lines 593 and 625–626; `LIFECYCLE_GUARANTEE_SPEC.md` lines 30–35

**The availability/testimony split is drawn too broadly: some false availability codes are provable from the chain.** V78 says all four availability codes assert store states “no later reader can replay” and are therefore testimony only. Counterexample: the chain contains a prior successful touch of sealed object X; there is no intervening authorized write, delete, truncate, identity change, or integrity/VOID event; a later request for the same fixed identity is refused as `REFUSED-OBJECT-ABSENT`. The earlier committed touch proves X existed, the sealed-object rules forbid its disappearance, and the later token is incompatible with the chain unless a separately logged protocol/digest deviation occurred. This is audit-detectable from the chain plus the pinned immutable-object rules, not merely attributable testimony.

The correct split is per emission/condition: recompute any availability assertion whose truth is entailed or contradicted by chain history and pinned immutability facts; use signed testimony only where contemporaneous store state genuinely cannot be reconstructed. Otherwise G2 understates what its auditor must reject and permits a chain-provably false specific token to bypass `REFUSED-UNCLASSIFIED` enumeration.

### F5 — MEDIUM / REPAIR-REQUIRED — `tools/refusal_vocabulary_check.py` lines 121–127, 129–163 and controls 269–304; §6.1 line 618

**The retired-token activation guard accepts a direct semantic reactivation.** The checker admits its activation vocabulary is finite, then treats a known retired token as legal whenever the fragment contains a retirement word and none of its listed activation stems. Executed against the actual checker, this fragment returned `[]` (clean):

`REFUSED-LOCK-NOT-OPEN was deleted, but will be used for all future openings.`

“will be used” plainly reactivates the code but matches none of `reinstat|restored|reactivat|is active|in force|hereby|applies again|governs|mandatory|shall apply|takes effect|is live`. The 27 self-controls pass because they test only named phrasings, not semantic equivalence. The draft is honest that the list is incomplete, but it simultaneously describes this lint as blocking/deletion-detecting; the demonstrated sentence is exactly the prose/checker divergence the guard exists to prevent. Repair with an operative source of truth generated from the declared member/retired sets, rather than trying to enumerate English activation verbs, or conservatively reject any operative mention of a retired token outside a narrowly canonical tombstone sentence.

## Failed attacks / repairs that held

- The subject digest matched before review; the lifecycle companion digest recomputed to `eeead2285f6a905cd2e92b7ab853de4f383b6000d25d3428b10e5d7bb2f3bf49`, matching V78's pin.
- `tools/prereg_lint.py` exited 0 with 97 advisory legacy citations and 0 blocking findings. I did not re-report those option-D legacy citations.
- `tools/prereg_counts.py` independently parsed 16 class-P and 8 class-E rows; the prose matches.
- `tools/prereg_trace.py` checked 77 transitions with 0 problems.
- `tools/void_registry.py` parsed 54 antecedents and 20 §6.1 rows; its self-test passed all six controls. I treated that as name coverage only, exactly as V78 instructs.
- `tools/refusal_vocabulary_check.py` reports 0 problems on V78, and its 27-control self-test passes. F5 attacks the untested semantic boundary; it does not misreport those green results.
- `tools/lifecycle_derivation_check.py` reports 0 problems and its nine controls pass; the quoted G/N invariant bodies match the pinned spec.
- AST recount of `successor_ref_v9.py` matches `ref/RAISE_SITE_CLASSIFICATION.md`: 112 raise nodes and 112 unique ledger rows, with class counts 26 CALLER / 59 INTEGRITY / 20 NUMERICAL / 3 PLANNING-INTERNAL / 1 TYPED-OUTCOME / 3 WRAPPER.
- The V42/KIMI Stage-P citation is now represented honestly as a prior miscitation: the KIMI report predates FINDINGS-BLOCK, and the draft itself states F7 does not support the dual-valued claim. I found no new repair claim resting on F7.
- I did not re-derive the parked draw-discipline, VOID partition, durable pre-verdict state, strata/producer, integrity-mismatch, BS-3g lifecycle-cycle, call-site-unit, Row-L-phase, authorization, or other principal-referred questions.

## Evidence and custody

Read in content: the exact V78 draft; `gates/BRIEF_V78_REVIEW.md`; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `tools/refusal_vocabulary_check.py`; and the named checker sources needed to interpret their outputs. Executed only read-only hashes, parsers, self-tests, AST comparisons, and in-memory synthetic mutations. I did not modify the draft, spec, reference files, tools, or registries. My sole write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V78
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1321–1348 | The freeze-time dynamic-load manifest neither closes nor forbids verdict-affecting native loads first requested after replay starts.
F2 | HIGH | REPAIR-REQUIRED | §6.1 line 610 | Explanation parameter names and arity are unregistered free strings, restoring a pre-unblinding channel the string rule claims to remove.
F3 | HIGH | REPAIR-REQUIRED | §6.1 clauses 3(b), 6; §11 lines 1172–1175 | canonical.opening_authorization is labelled digest-ref although no exact field-order byte encoding defines its digest preimage.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 593, 625–626 | Availability truth is not uniformly testimony: immutable-chain history can make a false OBJECT-ABSENT token audit-provable.
F5 | MEDIUM | REPAIR-REQUIRED | tools/refusal_vocabulary_check.py lines 121–163 | A retired code stated as “will be used” is semantically reactivated while the blocking checker returns clean.
<!-- END FINDINGS-BLOCK -->