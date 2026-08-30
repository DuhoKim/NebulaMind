# V81 whole-document adversarial referee — CODEX

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V81_REVIEW.md` first, then verified the dispatched draft at SHA-256 `aa62779e73f7708f67e9cc4a45346529a7c0cc36e3c2d3901e11e7668bce6e62` before reading it. V81 repairs the literal V80 opening-body error, type-subclass surface, and `-O` launch-flag omission, but the stronger replay-composition claim still has unbound executable machinery and two independent ways to execute bytes other than the bytes checked. The lifecycle repair also lives outside the lifecycle spec it declares authoritative, and the new history audit cannot derive store identity from the event schema for multi-store rows. The canonicalization and registry mechanisms remain non-canonical and non-exhaustive in exactly the absence direction they claim to close.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §11 lines 1182–1188, 1324–1359, 1432–1454

**The replay harness that carries every V81 repair is neither named nor pinned.** V81's nineteen-field BS-3g schema pins `counterfactual_path_sha256`, and line 1333 says that field pins the wrapper. `verifier_sha256` is defined at lines 1245–1247 as the digest of `gates/verify_mu_gamma.py`. Neither field pins the new harness that is supposed to construct the mask, enforce `type(m) is SealedMask`, import the future mapping, launch the isolated interpreter, reject optimization, enumerate loaded objects, and replay every cell. Lines 1432–1454 specify an independent verifier but still provide no harness identity or digest.

This is not implementation incompleteness alone. A future producer can satisfy every named module digest while running a different harness that accepts a caller object, omits the end census, or launches with different arguments. The receipt has no field by which the independent verifier can distinguish that execution. Add a named replay-harness artifact/digest to the schema and bind execution to those exact bytes.

### F2 — HIGH / REPAIR-REQUIRED — §11 lines 1347–1374; `ref/closure_worker_v9.py` lines 138–152

**The bootstrap verifies paths and later imports paths; it does not execute the bytes it verified.** V81 requires the verifier to recompute interpreter/root/closure digests from disk, then says the replay “hashes the pinned file, imports it, computes.” That is two reads with a swap window. A dependency or mapping module can be replaced after the hash read, imported from the replacement, and restored before the end loaded-object census. The census sees the permitted path, and a final path digest sees the restored bytes, while the process retains objects and side effects produced by the transient bytes.

The repository already contains the exact forensic precedent: `closure_worker_v9.py` lines 138–152 says hash-then-import was unsound and repairs it by executing `compile(subject_bytes, ...)` from the already-verified bytes. V81 does not require immutable descriptors, execution from verified bytes, or an equivalent no-swap construction for the dependency roots and future mapping module. `-I -S` does not close a mutable-file race.

### F3 — HIGH / REPAIR-REQUIRED — §11 lines 1324–1342

**`sys.flags.optimize == 0` does not prove that the executed code was not optimized.** It reports the process default, not each code object's compilation mode. In a process where `sys.flags.optimize` is zero, `compile(source, ..., optimize=1)` produces and executes a code object with `assert` removed. I reproduced exactly that: the process reported optimize 0, the compiled code contained no assert opcode, and execution continued past an `assert False`.

This matters because V81 itself records v9's line-1622 assert as load-bearing, while the future pinned mapping module and the still-unpinned replay harness are executable import surfaces. Either can compile/execute optimized code without changing the process flag. The contract must bind the consumed v9 code object to the verified source under optimize 0 (or inspect the consumed code object / replace the load-bearing assert); checking only `sys.flags.optimize` is insufficient.

### F4 — HIGH / REPAIR-REQUIRED — §6.1 lines 621, 642, 646; `LIFECYCLE_GUARANTEE_SPEC.md` lines 77–84

**The deadline repair is outside the lifecycle's declared single home and still permits an indefinitely live pending state.** Line 621 says the state machine has one home in `LIFECYCLE_GUARANTEE_SPEC.md`, and line 642 calls the resulting lifecycle the BS-2k design requirement. The spec's complete state list at lines 77–84 has no deadline, clock, expiry transition, or timeout terminal treatment. The only deadline appears in unlabelled draft prose at line 646.

Even that prose fixes only a value: it does not bind a monotonic clock source, absolute-versus-relative semantics, persistence across worker/lease handover, or a fixture proving rollback/reset cannot postpone expiry. A wall-clock deadline moved backward, or a relative deadline restarted on worker handover while Row B remains live, leaves the request `PENDING-*` forever while satisfying the literal claim that it “carries a DEADLINE.” Put the transition and clock semantics in the authoritative spec and require BS-2k fixtures for rollback and handover.

### F5 — HIGH / REPAIR-REQUIRED — §6.1 lines 589, 626, 689, 706

**The monotone-presence audit cannot derive the store component of its own join.** Line 626 upgrades the join to `(STORE identity, brickid, objid)` but says STORE identity is derived from the event's row and stated surface. The closed event schema at line 589 carries no store identity. Derivation from row is not single-valued: Row I at line 706 reads the committee sealed label set and the corresponding main-store instrument outputs under the same row; the document's store inventory at line 689 confirms they are distinct stores. The same `(row, operation, brickid, objid)` can therefore denote two different store objects unless the still-undeclared operation vocabulary happens to encode the store.

That contingency is not the asserted join. A prior touch in one store can be paired with a later `OBJECT-ABSENT` in the other, manufacturing the contradiction the audit treats as evidence. Add a closed store-identity field or define a closed operation vocabulary whose members map bijectively to one store and make that mapping part of the audited schema.

### F6 — HIGH / REPAIR-REQUIRED — §6.1 lines 601, 611; §6.3 lines 821–824

**`NAMED-AS-DEFECT` cannot both repair the active vocabulary and avoid the document's post-χ void rule.** Line 601 lets a recurring catch-all discharge when an entry points to a changed “re-derived vocabulary revision” containing `NAMES-CLASS: <key> AS <token>` and a token definition. But it requires no activation record, effective chain position, parent revision, or proof that Row B actually adopted that revision. A changed text artifact can therefore pass the verifier while the operative mediator vocabulary remains unchanged.

If the intended repair is instead to make that changed revision operative during the run, §6.3 lines 821–824 voids any post-first-real-χ change to a binding rule or schema. Catch-all recurrence can occur after real χ exists. V81 nevertheless says at line 611 that enumeration blocks “repairably” rather than voiding. The text needs one coherent choice: either bind an effective vocabulary revision under a predeclared, non-voiding transition, or admit that a post-χ recurrence cannot be repaired inside this run.

### F7 — MEDIUM / REPAIR-REQUIRED — §6.1 line 610; `ref/successor_ref_v9.py` lines 219–224

**The declared “canonical JSON” is not a unique byte encoding.** V81 specifies sorted keys, compact separators, and UTF-8, but does not specify escape policy or Unicode normalization. Two byte strings, `{"label":"\u00e9"}` and `{"label":"é"}` encoded in UTF-8, satisfy those stated properties and decode to the same JSON value while hashing differently. NFC `é` and NFD `e` + combining acute add a second ambiguity. JSON also admits spelling differences such as escaped versus unescaped `/`.

The claimed precedent is wrong as bytes: v9 line 222 uses `json.dumps(env, sort_keys=True).encode()` with default separators, not the compact separators V81 mandates. A digest-ref must select one algorithm (for example, a pinned RFC 8785 implementation plus an explicit Unicode policy) rather than a family of valid JSON encodings.

### F8 — MEDIUM / REPAIR-REQUIRED — §6.1 lines 669–678; `ref/gen_string_field_registry.py` lines 209–227, 238–266

**The registry generator does not extract every declared schema field; several decisive inventories are hard-coded.** The draft and generated registry claim mechanical extraction from schema blocks so a field cannot be silently omitted. In code, `extract()` recognizes only a few regex-shaped blocks. Opening-authorization fields are supplied by the hard-coded `OPENAUTH` set at lines 241–242; canonical bodies, non-slot classes, BS-7p environment fields, parameters, and freeze fields are likewise hard-coded sets at lines 238–254 and unioned into the result at line 266.

This is why the V80 `timestamp`/`schema_version` repair required a manual dictionary correction: changing Clause 6 again does not make the extractor discover the new field or mark the old hard-coded member stale. A synthetic same-format schema block is ignored. The registry currently matches V81, but the claimed omission-proof mechanism is false. Parse all declared blocks structurally, or label the hard-coded inventories as manually maintained and gate their byte equality to the prose declarations.

## Failed attacks / repairs that held

- The subject digest matched before reading. The lifecycle spec digest matched V81's pin: `eeead2285f6a905cd2e92b7ab853de4f383b6000d25d3428b10e5d7bb2f3bf49`.
- V81's opening-authorization bytes now agree: Clause 6 and line 610 both end with `schema_version`, not `timestamp`; `ref/STRING_FIELD_REGISTRY.md` lines 134–141 matches that eight-field body.
- The frozen code pins matched disk: `successor_ref_v9.py` = `6a9abbbd…`; `closure_worker_v9.py` = `28f8e1f9…`; `refusal_vocabulary_check.py` = `b37fe6e3…`.
- The frozen v9 AST has exactly 112 `Raise` nodes, and `ref/RAISE_SITE_CLASSIFICATION.md` has 112 matching rows with table closure `26 CALLER / 59 INTEGRITY / 20 NUMERICAL / 3 PLANNING-INTERNAL / 1 TYPED-OUTCOME / 3 WRAPPER`. No site is assigned `UNREACHABLE-BY-CONSTRUCTION`.
- `tools/refusal_vocabulary_check.py` reports 0 problems; its 30-control self-test reports 0 failures. I did not turn its admitted finite activation vocabulary into a finding without finding an operative V81 divergence.
- `tools/lifecycle_derivation_check.py` reports 0 quoted-invariant problems. That held for the labelled G/N bodies; F4 concerns unlabelled lifecycle machinery omitted from the spec.
- `tools/prereg_lint.py` exits 0 with 97 advisory and 0 blocking findings. Per the brief, the legacy citation advisories are not reported as outstanding work.
- `tools/prereg_counts.py` independently returns 16 class-P and 8 class-E rows. `tools/void_registry.py` returns 54 antecedents and 20 named rows. The trace checker reports 80 transitions and 0 problems when invoked in check mode.
- The name-based call graph does not reach v9's `_frozen_planner` dynamic import from `run_production_verdict`; I do not re-report that site as reachable. F1–F3 concern the new replay/bootstrap contract around the frozen path.
- The `SealedMask` subclass attack is textually closed by type-exact construction. I found no remaining caller-supplied mask argument in V81's stated replay contract.
- The parked availability-code truth problem, durable pre-verdict state, VOID/numerical partition, Row-F strata/producer, BS-3g lifecycle cycle, `require_authorization`, draw discipline, and per-call-site raise classification were not re-derived.

## Evidence ledger and scope

Read in content: `gates/BRIEF_V81_REVIEW.md`; V81 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/successor_ref_v9.py`; `ref/closure_worker_v9.py`; `ref/gain_counterfactual_path.py`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `tools/refusal_vocabulary_check.py`; and the named checker sources/results. I also compared the V80 reports and the V80→V81 delta only to test the claimed repairs. No draft, spec, reference, checker, receipt, or gate file was modified. This report is the sole intended write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V81
VERDICT: NOT CLEAR
COUNT: 8
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1182–1188, 1324–1359, 1432–1454 | The replay harness carrying the no-caller/type/optimization/load-census repairs is neither named nor pinned in the receipt schema.
F2 | HIGH | REPAIR-REQUIRED | §11 lines 1347–1374 | Hashing dependency paths and later importing those paths leaves a verified-bytes/consumed-bytes swap window.
F3 | HIGH | REPAIR-REQUIRED | §11 lines 1324–1342 | sys.flags.optimize == 0 does not detect code objects compiled explicitly with optimize=1, which still strip v9's load-bearing assert.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 621, 642, 646; lifecycle spec lines 77–84 | The deadline is absent from the lifecycle's declared single-home spec and has no monotonic clock or reset semantics.
F5 | HIGH | REPAIR-REQUIRED | §6.1 lines 589, 626, 689, 706 | The event schema lacks store identity, and multi-store Row I makes the claimed presence-audit join non-derivable.
F6 | HIGH | REPAIR-REQUIRED | §6.1 lines 601, 611; §6.3 lines 821–824 | NAMED-AS-DEFECT either leaves the operative vocabulary unchanged or activates a post-χ rule revision that the document says voids the run.
F7 | MEDIUM | REPAIR-REQUIRED | §6.1 line 610 | Sorted compact UTF-8 JSON is not a unique encoding without escape, numeric, and Unicode-normalization rules.
F8 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 669–678; ref/gen_string_field_registry.py lines 209–266 | The alleged schema extractor hard-codes opening, canonical, non-slot, environment, and parameter fields instead of extracting them.
<!-- END FINDINGS-BLOCK -->