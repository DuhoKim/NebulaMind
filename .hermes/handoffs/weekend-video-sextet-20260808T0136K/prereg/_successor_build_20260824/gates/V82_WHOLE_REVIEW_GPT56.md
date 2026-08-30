# V82 whole-document adversarial referee — GPT56

## Verdict

**NOT CLEAR.** The subject digest matched the brief, and the generated checks are green at their stated syntactic scopes, but three substantive defects survive them. The highest-severity defect breaks V82's central compile-from-verified-buffer repair against the actual bytes of `gain_counterfactual_path.py`. A second leaves the supposedly bounded explanation surface with unbounded chosen-value fields. A third makes the recurring-catch-all guard run-local while claiming to stop a class that recurs once per run.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — compile-from-buffer does not remove the path module's import of v9

V82 §11 lines 1339–1348 claims that the two pinned modules are each compiled from their verified in-memory buffers into fresh namespaces, with “no import machinery” and no second read. The referenced path bytes contradict that construction:

- `ref/gain_counterfactual_path.py` lines 49–50 mutate `sys.path` and execute `import successor_ref_v9 as v9` at module top level.
- Executing verified v9 bytes into a separate fresh dictionary does not bind that dictionary to the name imported by the path module.
- I reproduced the exact semantic gap by `compile(..., optimize=0)`/`exec`-ing both verified buffers. During execution of the path buffer, `__import__('successor_ref_v9')` fired, and the resulting `pns['v9']` module was not the namespace produced by the verified v9-buffer exec (`pns['v9'].__dict__ is vns` was `False`).

Therefore the path buffer still reaches import machinery and resolves v9 by name unless the harness performs an additional, presently unstated binding (for example, installing the exact verified module object under `sys.modules['successor_ref_v9']` before executing the path and proving that identity). As written, the repair reopens the very disk/bytecode/name-resolution path it says it removes. “Fresh namespaces” is not enough; the dependency binding between the two namespaces is the missing operation.

### F2 — HIGH — REPAIR-REQUIRED — explanation parameters are labelled bounded but have no value or encoding bounds

V82 §6.1 line 610 permits the closed `cause` token “plus bounded numeric parameters (durations, counts)” and relies on that surface to exclude free prose and bound the pre-unblinding channel. `ref/STRING_FIELD_REGISTRY.md` lines 142–146 classifies five leaves as `bounded-encoding`:

- `param.duration_ms`
- `param.attempt_count`
- `param.signal_number`
- `param.lease_id_digest`
- `param.store_errno`

But neither those rows nor their source declarations in `ref/gen_string_field_registry.py` lines 109–115 specify a byte width, numeric interval, digit cap, signedness, or (for `lease_id_digest`) a fixed digest grammar. They specify only which parameter names and arities accompany each cause. A mechanical scan of the five generated rows found zero explicit range/byte/bit/hex bounds. The registry generator nevertheless exits 0 (`fields found 183 classified 183`), because it checks that a classification label exists, not that `bounded-encoding` has a bound.

This defeats both the string rule and the named residual analysis. An arbitrarily long decimal integer can carry an arbitrarily long chosen bit string while remaining an integer under line 610's decimal-ASCII canonical encoding; `lease_id_digest` is even misclassified as generic `bounded-encoding` rather than a fixed 64-hex digest-ref. Names and arity close the shape, not the capacity. The five leaves need exact enforceable domains/encodings, and the generator must reject a `bounded-encoding` row whose bound is absent.

### F3 — MEDIUM — REPAIR-REQUIRED — the recurrence guard cannot detect one recurring emission per run

V82 §6.1 line 600 states the motivating attack exactly: “A class that fires every run can be explained every run,” then claims that recurrence forces vocabulary re-derivation. The executable specification later narrows the state the verifier actually consults:

- line 601 refuses a second `EXPLAINED` disposition for the same key **within the run**;
- §11 lines 1492–1495 require `per-key EXPLAINED count (≤ 1 within the run)`;
- `LIFECYCLE_GUARANTEE_SPEC.md` line 158 explicitly leaves **cross-run recurrence** as a successor-preregistration duty.

Construct a foreseeable pre-χ failure class that emits once in each study run—for example, one verifier timeout on the same `(row, operation)` key. Each run has count one, so each entry may be `EXPLAINED`; no verifier sees a second occurrence, and no state is carried to the successor preregistration. The class becomes routine across runs by the exact route line 600 says is blocked.

This is distinct from the parked post-χ vocabulary-rederivation/VOID collision: the counterexample can occur pre-χ and requires no post-χ re-derivation. The repair must either narrow line 600's claim to within-run recurrence and state that once-per-run routine use remains open, or define authenticated cross-run recurrence state and its consuming gate.

## Adversarial checks that held or were correctly disclosed

- Subject sha256 rechecked as `12d54356b4fde6b0dec0919a13f7af65f34a1927a9c1984e427e3401a93ed5ad` before reading and again before report assembly.
- `LIFECYCLE_GUARANTEE_SPEC.md` hashes to the draft's pin `2520c904b0e5fef5d4f136e6c2b7a05c2e290252ae2bf9d223bd66973cc2f880`; `tools/lifecycle_derivation_check.py` reports 0 problems and its nine-control self-test reports 0 failures.
- `tools/refusal_vocabulary_check.py` hashes to the draft's cited `a8c17f9361127f7f…`; it reports 0 problems on V82 and its 31-control self-test reports 0 failures.
- I defeated that checker's finite activation-word heuristic with `REFUSED-LOCK-NOT-OPEN was retired; it must control P7.` (the checker returned no problem), but did not count this separately because the checker itself explicitly says the activation list is finite and known incomplete and assigns prose semantics beyond it to the referee round.
- `tools/prereg_lint.py` reports 16 class P / 8 class E and 97 advisory legacy citations, 0 blocking, consistent with the brief. I did not re-report the option-D legacy advisories.
- `tools/prereg_counts.py` independently reports 16/8 and prose/table agreement.
- `tools/void_registry.py` reports 54 antecedents and 20 defined §6.1 rows; its six-control self-test reports 0 failures while correctly disclaiming semantic coverage.
- `ref/RAISE_SITE_CLASSIFICATION.md` was read against `ref/successor_ref_v9.py`; I did not re-find the already-referred per-raise versus per-call-site unit defect.
- The canonical opening-authorization field order at §6.1 line 610 ends in `schema_version` and matches Clause 6 line 735.
- The refusal checker digest and lifecycle-spec digest cited by V82 match the files on disk.

## Evidence and scope

Read in full: the 1,510-line V82 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `tools/refusal_vocabulary_check.py`; relevant portions of `ref/successor_ref_v9.py`, `ref/gain_counterfactual_path.py`, `ref/STRING_FIELD_REGISTRY.md`, and `ref/gen_string_field_registry.py`. Executed the lint/count/lifecycle/refusal/VOID/registry checks and the compile/exec reproduction described above. No draft, reference, tool, registry, or other artifact was modified; this report is the sole write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V82
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1339–1348; ref/gain_counterfactual_path.py lines 49–50 | The verified path buffer still imports successor_ref_v9 by name, so fresh-namespace exec does not eliminate import machinery or bind the verified v9 namespace.
F2 | HIGH | REPAIR-REQUIRED | §6.1 line 610; ref/STRING_FIELD_REGISTRY.md lines 142–146 | Five explanation parameters are labelled bounded-encoding but have no ranges or byte grammar, leaving an unbounded chosen-value channel.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 600–601; §11 lines 1492–1495 | Recurrence is enforced only within one run, so a class emitted once per run can be explained forever despite the claimed guard.
<!-- END FINDINGS-BLOCK -->