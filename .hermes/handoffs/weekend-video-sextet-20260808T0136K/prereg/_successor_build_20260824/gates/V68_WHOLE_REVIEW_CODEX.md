# V68 whole-document adversarial review — CODEX

**VERDICT: NOT CLEAR.** The subject digest matched the brief exactly before the draft was read. Several V68 repairs do hold mechanically, but the central new contracts remain breakable. The atomic-touch contract omits the requester-delivery edge and contradicts its own transfer-failure treatment; the recurrence key depends on a field absent from the closed event schema; the draft falsely claims two §11 implementation items that do not exist; the Row-F recomputation predicate can be satisfied by a χ-conditioned strict subset; `gamma_bound` is self-declared rather than bound to the measured gradient; two pre-run planning failures remain typed run outcomes; and the BS-3g verifier permits `NOT-EVALUATED` to hide a decisive flip.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the atomic commit does not include delivery to the requester

V68 §6.1 lines 622–624 puts the sealed stores, access-log event, and request-identifier binding in one transactional commit domain. Row B at line 657, however, must convey the bytes to another row. That requester-facing delivery is not one of the three committed effects.

The omitted edge recreates the ordering problem one boundary later. If Row B commits before delivering, a crash can leave a committed `COMPLETED` event and binding while the requester received nothing; line 624 then suppresses re-decision because the binding exists. If Row B delivers first, a crash can expose bytes without a committed event. A transactional outbox could distinguish store-read commit from requester delivery, but the document defines neither an outbox nor an acknowledgement/recovery state and instead claims that “bytes leaving the store” is itself the atomic effect. The contract therefore does not establish its universal claims for a read whose consumer lies outside the store/log transaction.

### F2 — HIGH / REPAIR-REQUIRED — a request can change terminal outcome after its sole event is durable

Lines 622–624 require one truthful event committed with the touch. Line 629 then says a request that dies in `TRANSFER` “has a verdict already durably logged” and is subsequently completed as `FAILED` under an availability code.

Those statements cannot all hold under the append-only one-event schema at line 589. If the durable event records success/authorization, the later `FAILED` treatment makes it false. If it does not yet record a terminal outcome, the event is not the one truthful terminal event the atomic-touch contract claims. The log cannot mutate the old event and the covenant forbids a second event. This is a concrete request lifecycle ending with a terminal fact that its only durable event cannot carry.

### F3 — HIGH / REPAIR-REQUIRED — two `_plan` failures violate the draft's own planning/non-outcome boundary

Section §5 line 503 states that a failure before a run exists “cannot be a run outcome of any kind.” Yet `ref/RAISE_SITE_CLASSIFICATION.md` lines 101–102 classifies source lines 1331 and 1341 as `TYPED-OUTCOME`. The pinned `successor_ref_v9.py` shows both are `InconclusiveByPower` raises inside `_plan`: no ledger prefix passes Stage P, or the final selected set fails the Stage-P re-pass. `_plan` is reached from `build_plan`, the production planning entry point, before `run_production_verdict` or a study run exists.

The ruling moved only `local_pass` lines 963/973/986. It missed these two explicit planning raises, so the referenced classification still assigns run outcomes during the phase the draft says admits none.

### F4 — HIGH / REPAIR-REQUIRED — `class_key` cannot be recomputed from the closed event schema

Line 601 defines `class_key = (table row, operation, lifecycle state at failure)` and says all three fields are already carried by the event, allowing the verifier to recompute the key. The exhaustive event schema at line 589 carries timestamp, actor, table row, operation, object identity, success/refusal, refusal reason, and running chain digest. It carries no lifecycle state.

A verifier reading only the chain therefore lacks one third of the key. It must either trust a lifecycle value supplied by the enumeration entry—restoring the relabelling freedom V68 claims to remove—or invent it from information the event does not authenticate. `tools/refusal_vocabulary_check.py` does not catch this: R08/R09 merely search for an entry, `class_key`, recurrence language, and two consultations.

### F5 — HIGH / REPAIR-REQUIRED — both new executable mechanisms claim §11 build items that are absent

Line 607 says §11 carries a separately pinned build item for `gates/enumeration_verifier.py`; line 625 says §11 carries the atomic-touch implementation item. Section §11 lines 1098–1127 contains neither. Its Row-B item at line 1103 implements the C2 precondition block and general mediation checks, not transactional store/log/binding atomicity. Repository search found no `gates/enumeration_verifier.py` or other `*enumeration_verifier*` file.

The enumeration entry is consequently also under-specified at the exact point the prose says existence is established: no §11 item pins canonical encodings, the signed bytes and verification key, authentication of the signed object named by `explanation_ref`, fixtures, or both gate invocations. A syntactically valid entry can point `explanation_ref` at a nonexistent or content-free object unless a verifier authenticates that target; the stated verifier checklist never says it does. These are not merely unbuilt honest TODOs—the draft expressly claims the TODOs are present and uses that claim to call both mechanisms executable.

### F6 — HIGH / REPAIR-REQUIRED — Row F's equality predicate does not prove χ-free bin construction

Section §6.3 lines 766–774 claims that boundaries constructed from any stratum-filtered, stratum-augmented, or truncated input differ from full-set recomputation and are therefore refused. That universal claim is false for the pinned `calibration_bins()`.

Direct execution against the pinned `successor_ref_v9.py` produced:

```
full range(12)             -> [4.0, 8.0]
strict subset [0,4,8,9]    -> [4.0, 8.0]
```

A second independent probe similarly produced `[3.0, 6.0]` from both full `[0,1,2,3,4,5,6,7,8]` and a χ-conditioned strict subset `[0,1,3,4,6,8]`. Row F can therefore feed a χ-conditioned subset to bin construction while sealing boundaries equal to the full recomputation. The verifier passes although the act violates Row F's void clause (“any χ-bearing input to bin construction”). Equality of outputs cannot establish absence of forbidden input; this is exactly the brief's absence-clause failure mode.

### F7 — HIGH / REPAIR-REQUIRED — `gamma_bound` is self-declared, allowing an arbitrarily favourable manifest

Lines 1160–1164 require the perturbation manifest to span `±gamma_bound`, but lines 1174–1176 define `gamma_bound` only as the bound the invariance test was evaluated against. The verifier at lines 1244–1253 recomputes `gamma_hat` and `sigma_gamma`, yet never derives `gamma_bound` from them and never compares it with a separately frozen class-P bound.

A conforming producer can report the authentic measured `gamma_hat` and `sigma_gamma`, choose an arbitrarily small positive `gamma_bound = ε`, evaluate `[-ε, 0, +ε]` at a compliant spacing, and report `HELD`. Endpoint, distinctness, spacing, digest, field-equality, and draw checks all pass while the allowed gradient interval has been chosen favourably. Binding the grid to its own self-declared endpoint does not bind it to the scientific bound.

### F8 — MEDIUM / REPAIR-REQUIRED — `NOT-EVALUATED` can conceal a decisive BS-3g failure

Lines 1225–1229 define the categorical truth rule: `HELD` iff every matrix cell equals `baseline_verdict`, and `FAILED` otherwise. Verifier clause (e), lines 1247–1251, enforces only the `HELD` biconditional. When any cell differs, both `FAILED` and `NOT-EVALUATED` satisfy “not HELD.” Clause (f), lines 1253–1255, then explicitly calls `NOT-EVALUATED` a valid record, although lines 1255–1258 require exactly all draws to be evaluated.

A producer can therefore evaluate the full matrix, observe a flip, report `NOT-EVALUATED`, pass the literal clause-(e) truth check, and obtain a verifier-valid blocking record that hides the decisive `FAILED` evidence from the principal. Enforcing the earlier categorical rule would instead make `NOT-EVALUATED` unreachable for an emitted receipt. The outcome vocabulary and verifier contract are not single-valued.

## Failed attacks and verified holdings

- Subject SHA-256 held exactly: `010f5ece044e67a1928f2182f8df29dc1c68cb1b96f085cac332b7f376cec9a7`.
- The pinned reference held: `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/refusal_vocabulary_check.py` held its cited digest `9586e207f20141fde3d0f87f86d23cd2c84913934c7493161cfed0efb759d2e3`; the live check returned 0 problems and the self-test returned 17 controls, 0 failures. F4/F5 concern facts those text-pattern controls do not establish.
- The eleven formatted refusal codes match the checker exactly. I found no different object-membership leak beyond the parked logged-identity channel and did not re-find it.
- `prereg_counts.py` reproduced 16 class P / 8 class E. `prereg_trace.py` reproduced 67 transitions / 0 problems. `prereg_lint.py` exited 0 with 97 advisory / 0 blocking findings; its self-test returned 8 controls / 0 failures. `void_registry.py` found 54 antecedents and its self-test returned 6 controls / 0 failures.
- AST recount reproduced 112 raises: 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, and 1 bare re-raise. The classification table arithmetic also closes at 25 CALLER / 60 INTEGRITY / 20 NUMERICAL / 1 PLANNING-INTERNAL / 3 TYPED-OUTCOME / 3 WRAPPER. F3 attacks the semantics of two table rows, not those totals.
- No site in `RAISE_SITE_CLASSIFICATION.md` is assigned `UNREACHABLE-BY-CONSTRUCTION`; the withdrawal held.
- The V68 manifest verifier now expressly states both endpoints, at least three distinct values, adjacent spacing, and `delta_gamma_max` equality. A conforming grid can still evade through F7's unbound interval, not through the repaired coverage checks.
- Only `HELD` discharges BS-3g; verifier-valid `FAILED` and `NOT-EVALUATED` records block BS-6. The discharge split itself held. F8 concerns truthful classification of the blocking record.
- The currently stated BS-3g emission blockers are honest: `n_draws`, `draw_master_seed`, and `Δγ` are unset and the admissible generator set is empty. I found no present emission path through all blockers.
- V68 correctly narrows `HELD` to no flip found on the evaluated grid and does not call it proof of continuous invariance.
- KIMI-V11 F7 was checked against its report and does not support the Stage-P implementation claim; V68 correctly records the V42 substitution as wrong.
- I did not re-derive the parked VOID/numerical partition, availability-code identity leak, pre-verdict residue, strata/producer decision, BS-3g lifecycle cycle, signature exemption, or other principal-held items.

## Evidence ledger and scope

Read in content: the governing brief; all 1,276 lines of V68; `ref/RAISE_SITE_CLASSIFICATION.md`; targeted source regions of `ref/successor_ref_v9.py`; `tools/refusal_vocabulary_check.py`; `tools/prereg_lint.py`; V67's CODEX and GPT56 whole-document reports; `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`; and the KIMI V11 finding regions.

Executed read-only checks: subject/reference/checker SHA-256; AST raise-node and classification recount; refusal-vocabulary live check and self-test; prereg counts, lint and lint self-test; prereg trace; VOID-registry live check and self-test; repository searches for the asserted enumeration and atomic-touch implementation items; and direct `calibration_bins()` counterexamples. I did not modify the draft, reference code, tools, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V68
VERDICT: NOT CLEAR
COUNT: 8
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 622–624, 626, 657 | The atomic commit omits requester delivery, so commit-before-delivery suppresses recovery while delivery-before-commit leaks bytes unlogged.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 589, 622–624, 629 | A request may acquire a durable verdict and then become FAILED, but the append-only one-event contract has nowhere to record the changed terminal fact.
F3 | HIGH | REPAIR-REQUIRED | §5 line 503; RAISE_SITE_CLASSIFICATION.md lines 101–102; successor_ref_v9.py lines 1291–1342 | Two `_plan` failures remain typed run outcomes despite the rule that pre-run planning failures cannot be outcomes.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 589, 601; refusal_vocabulary_check.py lines 160–172 | The recurrence key requires lifecycle state, but the exhaustive access-log event schema does not carry that field.
F5 | HIGH | REPAIR-REQUIRED | §6.1 lines 607, 625; §11 lines 1098–1127 | The draft claims §11 build items for the enumeration verifier and atomic-touch implementation, but neither item nor the verifier file exists.
F6 | HIGH | REPAIR-REQUIRED | §6.1 Row F line 662; §6.3 lines 766–774; successor_ref_v9.py calibration_bins | A χ-conditioned strict subset can yield exactly the full-set boundaries, so equality does not enforce χ-free bin construction.
F7 | HIGH | REPAIR-REQUIRED | §11 lines 1160–1176, 1240–1253 | `gamma_bound` is not derived from measured fields or compared with a frozen bound, allowing an arbitrarily favourable tested interval.
F8 | MEDIUM | REPAIR-REQUIRED | §11 lines 1225–1229, 1247–1258 | The verifier's HELD-only biconditional lets a fully evaluated flip be recorded as valid NOT-EVALUATED instead of the required FAILED.
<!-- END FINDINGS-BLOCK -->