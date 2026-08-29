# GPT56 — V72 whole-document adversarial review

## Verdict

**NOT CLEAR.** The dispatched draft matched the required SHA-256 before I read it. The V72 bytes do quote the current lifecycle spec, and the advertised lint/count/trace/VOID/refusal checks are green. The new derivation predicate nevertheless is not in that lint path and is structurally unable to enforce label-to-invariant identity or even the continued presence of the quotation block. Separately, the global string rule leaves `explanation_ref` unbounded, the enumeration verifier is one-way rather than exact-set, and the production-equal BS-3g replay does not bind the actual `successor_ref_v9` module object used by `gain_counterfactual_path.py`.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the derivation predicate is not wired into the advertised lint/battery

Draft §6.1 line 622 says the derivation is now a **CHECK**, and the review brief says this check is the mechanism that makes a stale spec pin break the draft. The check exists at `tools/lifecycle_derivation_check.py`, but `tools/prereg_lint.py` contains no lifecycle/derivation invocation at all. I searched that file for `lifecycle`, `derivation_check`, and `LIFECYCLE`; there were zero matches. The standard V72 lint exited 0 without running or reporting this predicate. I had to invoke it separately to obtain `lifecycle derivation: 0 problem(s)`.

Therefore a normal green lint does not establish the new derivation claim. A later spec edit can leave the draft stale while the advertised battery stays green unless an operator remembers an extra command that neither the lint nor a named gate dependency executes. This is exactly the brief's requested “stale pin the battery never runs” attack.

Repair: make the lifecycle check a blocking, controlled subcheck of `prereg_lint.py` (or a comparably mandatory named gate), add a self-test proving a stale spec pin makes the integrated battery nonzero, and report its result in the lint summary.

### F2 — HIGH / REPAIR-REQUIRED — the derivation checker does not bind invariant labels and accepts deletion of the quoted guarantee

`tools/lifecycle_derivation_check.py` lines 17–19 says the draft may quote fewer invariants, and lines 38 plus 55–59 extract only the body after `G… —`/`N… —` and test whether that body occurs anywhere in the normalized spec. It never checks that a body belongs to the same label, and it has no required-label inventory.

I attacked the function in memory, without changing disk bytes:

- Baseline V72: 0 problems.
- Swapped the complete G1 and G2 bodies while retaining the opposing labels (`G1 — No false event…`, `G2 — No unlogged touch…`): **0 problems**.
- Deleting all quoted G/N lines likewise returns 0 problems (the loop is vacuous).

The current V72 quotation happens to be correct, but line 622's claim that divergence now fails and makes this class “impossible” is false. The predicate permits a future draft to assign the no-false-event guarantee to G1, assign no-unlogged-touch to G2, or remove the duplicated guarantee block entirely while staying green.

Repair: parse `(label, full normalized body)` pairs from the spec, require the draft's complete declared label set G1–G5/N1–N3 exactly once, compare each body to the body for that same label, and add swap/delete/duplicate controls.

### F3 — HIGH / REPAIR-REQUIRED — `explanation_ref` violates the global string rule and is a pre-unblinding payload channel

Draft §6.1 lines 662–672 makes the rule universal: every string field in every non-χ artifact must be closed-vocabulary or a bounded encoding, with identifiers coming from a declared set. But line 610 defines `explanation_ref` only as “the identifier of the signed human explanation.” It declares no vocabulary, byte grammar, length/range, canonical derivation, or finite identifier set. The verifier only resolves the reference and checks the signed explanation's joined event/cause fields. Line 659 then exempts these entries and explanations as non-χ-bearing.

A signer can mint a resolvable explanation artifact whose identifier itself encodes arbitrary prose or an object-indexed bit string. Resolution, signature, event join, closed `cause`, and bounded numerics can all remain valid; the payload lives in the reference string, not the explanation body. `tools/refusal_vocabulary_check.py` does not test the global string rule and remained green after a synthetic mutation explicitly allowing free prose in `explanation_ref`.

Repair: define `explanation_ref` as a fixed-width digest of a canonical explanation body (or another genuinely bounded encoding with an explicit grammar and maximum), have the verifier recompute it, and add a control for oversized/free-form/object-indexed identifiers.

### F4 — HIGH / REPAIR-REQUIRED — the enumeration verifier is one-way and accepts orphan entries for non-catch-all events

The mechanism is supposed to enumerate `REFUSED-UNCLASSIFIED` emissions. Draft §11 lines 1388–1395 requires the verifier to recompute that event set and refuse an **unenumerated** emission, dangling reference, or second `EXPLAINED`. It never requires the reverse inclusion: every enumeration entry must join an event whose reason is `REFUSED-UNCLASSIFIED`. Line 610's entry schema binds `(chain_position, event_digest)` but likewise does not state that the joined event must be a catch-all refusal.

Counterexample: the chain contains an ordinary `REFUSED-OBJECT-UNREADABLE` event and no catch-all events. Add a correctly signed `EXPLAINED` enumeration entry joined to that ordinary event, with a resolvable explanation. The recomputed catch-all set is empty; there is no unenumerated catch-all, no dangling reference, and no second `EXPLAINED`. All stated refusal predicates pass. The extra entry and its five-way `cause` token are nevertheless admitted to the pre-unblinding non-χ continuation surface, creating an unauthorized side channel and defeating the claimed closed artifact class.

Repair: require exact set equality between enumeration-entry joins and `REFUSED-UNCLASSIFIED` chain events; reject orphan, duplicate, extra, wrong-reason, wrong-position, and wrong-digest entries in checkpoint and continuation segments. Add each as a named control.

### F5 — HIGH / REPAIR-REQUIRED — production-equal replay pins the wrapper file but not the production module object it executes

Draft §11 lines 1283–1292 says `counterfactual_path_sha256` binds the verdict-producing computation and every cell replays under the frozen production contract. Clause (a), lines 1347–1349, recomputes four file digests: kernel, estimator, verifier, and counterfactual path. It does **not** recompute the §0-pinned `successor_ref_v9.py` digest as part of this verifier contract.

The actual referenced code makes the surviving degree of freedom concrete. `ref/gain_counterfactual_path.py` lines 49–50 inserts its parent directory and executes an ordinary `import successor_ref_v9 as v9`; lines 137 and 141 call `v9.perm_record` and `v9._decide_from`. Python first consults `sys.modules`, so these exact wrapper bytes can bind to a preloaded object that is not the on-disk pinned module. I demonstrated this in a fresh in-memory probe: the counterfactual-path SHA remained `92cbbdf8…`, the real disk v9 SHA remained `6a9abbbd…`, `import_bound_to_fake` was `True`, and a production-address-looking call returned the fake module's `FAKE-PATH` result.

Thus the path digest plus address parameters do not prove that the cells were produced by the §0 code bytes. A later verifier implementation that imports the same way can replay the same substituted object and agree with a false receipt.

Repair: load v9 from the exact pinned path under a private module name only after hashing those bytes, reject a pre-existing/module-cache substitution, include/recompute the v9 digest in the BS-3g verifier contract, and add a malicious-`sys.modules` control.

## Failed attacks / credited repairs

- Subject identity held: `66fcc42c6de59cfd8b19397f5bc482f80391fc04f75926cf04b41281ea928979`.
- Companion spec identity held: `1c499dbcb9be30f959722dc76b84379da25c6842e640321ca9e1e1adf2a8df3c`; V72's pin matches it and the literal G1–G5/N1–N3 bodies currently match.
- `tools/refusal_vocabulary_check.py` identity held at `a3f64aef6e7b9d2e2e9f70449e320b1430579529f928a13ac67446724d24a422`; draft check and 20-control self-test were green.
- V72 lint reproduced 16 class P / 8 class E and 97 advisory / 0 blocking findings. I did not re-report the 96/97 legacy citation class parked by option D.
- `prereg_trace` reproduced 71 transitions / 0 problems; `void_registry` self-test reproduced 6 adversarial controls / 0 failures.
- The `BS-3g` field list now includes the four advertised module digests and the within-draw equality rule is internally coherent under common random variates. I did not count “statistics move but categorical verdict does not” as a defect because the text narrowly claims verdict invariance.
- The gamma manifest now requires zero, both endpoints, no out-of-range point, at least three distinct values, and a frozen maximum gap. The stated finite-grid limitation is honest.
- `ref/RAISE_SITE_CLASSIFICATION.md` was read against the pinned v9 bytes; its 112-row closure and the parked per-call-site-unit problem were not re-derived as new findings.
- The known availability-code/object-identity leak, durable pre-verdict-state gap, VOID partition, BS-3g lifecycle cycle, strata/producer pair, authorization weakness, and other expressly parked items were not recycled.

## Evidence ledger and scope

Read in content: the V72 brief; exact V72 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `tools/lifecycle_derivation_check.py`; `tools/refusal_vocabulary_check.py`; `tools/prereg_lint.py`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/successor_ref_v9.py`; and `ref/gain_counterfactual_path.py`. Ran SHA-256 checks, the V72 lint, lifecycle/refusal checks and self-tests, count/trace/VOID checks, AST/table inspection, and in-memory adversarial mutations/import probes. No draft, spec, reference, tool, gate, or repository file was modified; the only write made by this seat is this report. Pre-existing repository dirt was present and left untouched.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V72
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 line 622; tools/prereg_lint.py | The lifecycle derivation predicate is not wired into the blocking lint/battery, so a stale pin can leave the advertised battery green.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 622-632; tools/lifecycle_derivation_check.py lines 17-19, 38, 55-59 | The derivation checker accepts swapped invariant labels and deletion of the entire quoted guarantee block.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 610, 659, 662-672 | Unbounded explanation_ref violates the global string rule and can carry arbitrary pre-unblinding payload.
F4 | HIGH | REPAIR-REQUIRED | §6.1 line 610; §11 lines 1388-1395 | The enumeration verifier lacks reverse set inclusion and accepts orphan entries joined to non-catch-all events.
F5 | HIGH | REPAIR-REQUIRED | §11 lines 1283-1292, 1343-1356; ref/gain_counterfactual_path.py lines 49-50, 137-141 | Production-equal replay pins the wrapper but not the actual successor_ref_v9 module object it executes.
<!-- END FINDINGS-BLOCK -->