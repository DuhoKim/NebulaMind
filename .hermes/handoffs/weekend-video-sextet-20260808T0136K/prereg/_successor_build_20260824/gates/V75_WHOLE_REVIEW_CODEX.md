# V75 whole-document adversarial review — CODEX

## Verdict: NOT CLEAR

The pinned draft digest matches, and the three advertised text checkers I ran are green, but the V75 repairs do not close the two highest-value mechanisms the brief asks this seat to break. The 138-field registry is not an enumeration of the nine non-slot schemas and does not enumerate the runtime environment record it calls a closed vocabulary. The isolated replay also leaves interpreter selection under an unpinned parent-side configuration vector. Separately, the render rules do not make render-commit ↔ view-session ownership injective, and the live raise-site classification contradicts the draft's own caller-error boundary at `require_complete_sample`.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — §6.1 lines 586–588, 663–684; §11 line 1157; `ref/gen_string_field_registry.py` lines 85–91, 139–167; `ref/STRING_FIELD_REGISTRY.md` lines 101–109

**The 138-field registry does not enumerate the nine non-slot artifact schemas; it substitutes nine class-name pseudo-fields and labels each one `digest-ref`, including classes whose schemas do not exist.**

The draft's claim is strong: the non-χ list is “defined by schema” and exhaustive (§6.1 lines 586–588), and the generator supposedly extracts “every field token from the declared field lists” (lines 668–677). The code does something else. `NONSLOT` is a hand-written set of nine strings (`nonslot.access_log_chain`, `nonslot.unblinding_receipt`, etc.; generator lines 164–167), inserted wholesale into `v9f` (line 172). The extractor never opens or parses a per-class schema for them. `V9_CONSTRAINTS` then pre-classifies each class-name pseudo-field as a `digest-ref` (lines 85–91). My read-only reproduction selected V75 and reported `37` extracted draft fields + `101` v9/pseudo-fields = `138`, with the nine hard-coded `nonslot.*` names accounting for nine of the total.

That is not a harmless representation choice. The closed-list claim is about what fields each artifact can carry, but a digest reference to an artifact class does not constrain the fields inside an instance of that class. The counterexample is in the draft itself: §11 line 1157 says the canonical unblinding-receipt schema is only required work, gives fields “at minimum,” and says implementation is `UNRESOLVED`. Nonetheless the registry counts `nonslot.unblinding_receipt` as one fully classified `digest-ref` row and contributes it to “138 fields.” Similar rows for the cutout-completion receipt, stage-completion artifact, label-set receipt, adequacy receipt and lock checkpoint are not their schemas either. A conforming generator run therefore says `missing []`, `stale []`, exit-worthy defects absent, while having inspected none of those class bodies.

**Required repair:** enumerate the exact authenticated fields and value domains of every non-slot class from canonical per-class schema bytes; fail if a class schema is absent; pin those schema digests; do not count a class-name pointer as the class's field inventory. The unblinding schema must remain a blocker until those bytes exist, not a row that makes the count look closed.

### F2 — HIGH — REPAIR-REQUIRED — §6.1 lines 663–684; `ref/successor_ref_v9.py` lines 49–65, 208–224; `ref/STRING_FIELD_REGISTRY.md` lines 95–100

**`envelope.environment` is falsely classified as one closed-vocabulary field; the runtime record is a nested six-field mapping, and half of its values are not in the frozen vocabulary.**

Frozen v9 composes `environment_record()` at runtime with six keys: `python`, `python_major_minor`, `numpy`, `platform`, `machine`, and `byteorder` (v9 lines 53–57). `FROZEN_ENV` and `require_environment()` constrain only `python_major_minor`, `numpy`, and `byteorder` (lines 49–65). The receipt serializes the entire six-key dictionary into `envelope.environment` and returns it as a mapping (lines 220–224). The registry does not enumerate those six nested fields; it has one row, `envelope.environment | closed-vocab | ... | environment_record keys x pinned values` (registry line 98). That note is byte-false for `python`, `platform`, and `machine`: no declared member set or bounded encoding is enforced for them.

This is exactly the brief's “field the environment record composes at runtime” attack. The generator's `envelope_fields()` extracts only outer `field(...)` names and adds digest names; it never parses `environment_record()`. Thus the registry can report all 138 classified while a runtime-produced string-bearing subrecord escapes the no-third-kind rule.

**Required repair:** mechanically extract and enumerate every nested environment key; either close/bound each value and make `require_environment()` enforce it, or digest-reference a canonical, pinned environment body. If interpreter/OS values are trusted by declaration, that does not make their serialized strings members of a closed vocabulary.

### F3 — MEDIUM — REPAIR-REQUIRED — §6.1 lines 663–677; `ref/STRING_FIELD_REGISTRY.md` line 3; `tools/prereg_lint.py` lines 537–575

**The registry gate is not wired into the advertised blocking battery, and the checked registry still declares V74 as its source.**

`ref/STRING_FIELD_REGISTRY.md` line 3 says it was generated from `PREREG_SUCCESSOR_DRAFT_V74_20260830.md`, while the subject is V75. The generator would select V75 today, but it has not been run to produce the checked artifact: a read-only import selected V75, whereas the on-disk registry header remains V74. More importantly, `prereg_lint.py`'s blocking integration runs the lifecycle check, recomputes the refusal-checker digest, and then runs slot/count/citation checks (lines 537–575); it never invokes `gen_string_field_registry.py` or compares the on-disk registry to a generated V75 representation. I ran that lint on V75 and it exited 0 with 97 legacy citation advisories, exactly while F1/F2 remained invisible.

The generator's nonzero return on `missing` or `stale` rows is useful only when someone runs it. The current battery permits a stale registry artifact, a changed extractor, or an omitted schema class to coexist with a green lint.

**Required repair:** add a no-write check mode that generates the canonical registry in memory from the exact draft and schema pins, byte-compares it to the reviewed registry, and wire that mode into the blocking lint with a negative control. Bind the registry and generator digests to V75.

### F4 — HIGH — REPAIR-REQUIRED — §11 lines 1310–1328

**`python -I -S` plus a cleared child environment does not pin which interpreter executes; bare `python` is resolved through parent-side configuration before the child can clear anything.**

The draft says the replay is launched as `python -I -S`, with a cleared environment and pinned cwd, and declares “the interpreter binary and the OS” trusted (lines 1317–1324). The binary identity is never named or pinned. Resolving the bare executable name `python` happens in the launcher, using its PATH/executable-search state before the new process begins and before the child's environment is cleared. A PATH-prepended shim can accept `-I -S`, fake the hash/import/replay protocol, and emit a passing result. This is a configuration rebinding vector, not ownership of the declared trusted interpreter: the defect is that the declaration does not identify which interpreter is trusted.

`-I -S` correctly defeats Python's own `site`, `sitecustomize`, user-site, `PYTHONSTARTUP`, and normal cwd-path injection after a genuine interpreter starts; it does not authenticate process image selection.

**Required repair:** freeze an absolute interpreter path plus executable digest (and, if applicable, loader/runtime identity), have a trusted launcher open/verify that exact executable before spawning it, clear environment explicitly in the spawn payload, and receipt the executable identity used. “Trust the interpreter” must bind a byte identity, not a command name.

### F5 — HIGH — REPAIR-REQUIRED — `LIFECYCLE_GUARANTEE_SPEC.md` lines 30–35, 99–125; §6.1 lines 620–645

**The session-bounded buffer rule is not injective: one render commit/buffer can serve two simultaneous view sessions while every stated lifetime and occlusion fixture still passes.**

G6 defines a view as “the display session of one render commit” (spec line 34), which maps each view to a commit but never requires one commit to own exactly one session/surface. The buffer rule says it lives until “its VIEW SESSION ends” and forbids a redisplayable surface beyond “the live session” (spec lines 116–125), both singular assumptions rather than a cardinality/ownership invariant.

Counterexample: attach one committed render buffer concurrently to two sealed-interface windows, mirrored outputs, or two committee display sessions before either is interrupted. Each session is continuous and is a display session of that same commit. The buffer remains alive while at least one session is live, and an occlude-and-restore fixture on either surface can still produce “second event or no image.” Yet two renders/views have been delivered under one touch event, violating G3/G5's one-event-per-touch and fresh-commit-per-render claims. If session A ends first, “destroy at its session end” conflicts with continuing session B; if destruction waits for B, the buffer outlives A's session and is a redisplayable cache relative to A. The interface cannot resolve this from the present rule because the commit carries no unique session/surface binding.

**Required repair:** make render commit ↔ view session/surface a one-to-one binding; prohibit a buffer from attachment to more than one display session, window, display, compositor surface, or consumer; specify which trusted component observes every end condition; and add simultaneous-two-session/mirrored-output fixtures, not only sequential occlude-and-restore.

### F6 — MEDIUM — REPAIR-REQUIRED — §5 lines 504, 569–576; `ref/RAISE_SITE_CLASSIFICATION.md` line 129; `ref/successor_ref_v9.py` lines 1591–1599, 1647–1649

**The live raise-site ledger misclassifies `require_complete_sample` L1649 as `INTEGRITY` under the draft's own boundary; it is a supplied-argument mismatch and therefore `CALLER`.**

The boundary at §5 line 504 says a raise is `CALLER` when it tests an argument as supplied, and asks whether it can fire while every argument satisfies the contract. The draft later admits this exact guard compares “two caller-supplied integers,” that any equal pair passes, and that it is only a count check (lines 569–576). Frozen v9 passes `n_receipts` and `n_parent` straight from `run_production_verdict`'s caller (v9 lines 1591–1599); `require_complete_sample` merely casts and compares them (lines 1647–1649). The live classification nevertheless marks L1649 `INTEGRITY` (`RAISE_SITE_CLASSIFICATION.md` line 129).

This is not the parked per-raise-versus-per-call-site issue: this site has the production call shown above, and its current classification is wrong even at that site. Under the stated rule, mismatch means the caller supplied inconsistent count arguments. If a future validator binds both values to authenticated artifacts, that future path may acquire integrity semantics; frozen v9 does not.

**Required repair:** classify the existing L1649 path as `CALLER`, or change the documented calling contract and implementation so the values are independently authenticated and then classify that new path. Re-run the AST/table count and call-site ledger after the correction.

## Failed attacks / controls that held

- Draft identity held: SHA-256 recomputed as `781b7f3f065ff20dc2cbee1ec4bf5bde944cfe3a85ffe75f5df2a83fe0e69054` before the draft was read.
- Companion and frozen-source pins held: lifecycle spec `c6d266129689e05ea3f78c11ac266a4bcea6a95489f85eb6fe64d5244e15d8f5`; v9 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; refusal checker `35fd85487c5d71b0f25f583d08894ccabf99c1cfbd17324803be15d00f280ba7`.
- `tools/refusal_vocabulary_check.py` on V75: 0 problems, exit 0. Its self-test: 23 controls (1 negative), 0 failures. The only non-member token in the actual draft is the explicitly deleted `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` at line 614; I found no second active token in that fragment.
- `tools/lifecycle_derivation_check.py` on V75/spec: 0 problems, exit 0. Its self-test: 9 controls, 0 failures. The labelled G/N bodies and pin are byte-consistent; F5 is an uncovered cardinality hole, not a quote mismatch.
- `tools/prereg_lint.py` on V75: 16 class P / 8 class E; exit 0; 97 advisories and 0 blocking. Per the brief, the legacy citation advisories are not findings here.
- The generator's current extraction, reproduced without calling its write-producing `main()`, selects V75 and has no `missing` or `stale` keys under its own model. That failed attack is also the evidence for F1: the model itself substitutes pseudo-fields.
- `-I -S` does remove the named in-interpreter hooks once the intended binary is running; F4 is limited to authenticating which executable gets to that point.
- I did not attack the draw discipline, the parked availability-code/object-identity leak, the durable pre-verdict state, the VOID/numerical partition, the stratum producer, `require_authorization`, or the already-referred per-raise/per-call-site unit defect.

## Evidence ledger and custody

Content read: `gates/BRIEF_V75_REVIEW.md` first; then, only after the matching digest, V75; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/successor_ref_v9.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; repository `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; and `tools/prereg_lint.py`.

Read-only executions: SHA-256 recomputation; the three checkers and their relevant self-tests; in-memory import/extraction of the registry generator without `main()`; AST/source and token inventories. I did not execute the registry generator's write path. The repository was already broadly dirty before this report; I made no attempt to alter or clean pre-existing state. My sole intended write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V75
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | §6.1 586–588, 663–684; §11 1157 | 138-field registry substitutes nine non-slot class-name pseudo-fields for the absent per-class schema inventories
F2 | HIGH | REPAIR-REQUIRED | §6.1 663–684; v9 49–65, 208–224 | runtime environment's six nested string fields collapse into one falsely closed-vocab registry row
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 663–677; registry 3; prereg_lint 537–575 | string registry is V74-stale and its generator is not wired into the blocking lint
F4 | HIGH | REPAIR-REQUIRED | §11 1310–1328 | bare python executable selection remains PATH-rebindable before the cleared isolated child starts
F5 | HIGH | REPAIR-REQUIRED | lifecycle spec 30–35, 99–125; §6.1 620–645 | one render commit/buffer can serve two simultaneous view sessions because ownership is not one-to-one
F6 | MEDIUM | REPAIR-REQUIRED | §5 504, 569–576; raise ledger 129 | require_complete_sample is misclassified INTEGRITY although it only compares caller-supplied arguments
<!-- END FINDINGS-BLOCK -->