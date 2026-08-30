# GPT56 V80 whole-document adversarial referee report

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V80_REVIEW.md` first and verified the subject SHA-256 as `a9d5d0a2214fe4b16d15a4821d2463209b2105424eb2ce9b84933769e2656edc` before reading the draft. Five repair-required defects survive. The largest are byte-level contradictions in the opening-authorization body, an unpinned executable callback that defeats the load/unload composition proof, and an interpreter-mode degree of freedom that removes a verdict-path guard while every declared environment pin still matches.

## Findings

### F1 — HIGH — the withdrawn second opening-authorization body is still present and contradicts Clause 6

V80 says Clause 6 is the one canonical body, then immediately gives a different body. Clause 6 at line 735 binds: BS-L digest, two store identities, destination, ceremony identifier, P7, signer identity, and **schema/version**. The purported Clause-6 tuple embedded at line 610 instead ends in **`timestamp`** and omits schema/version:

`(bsl_digest, store_identity_main, store_identity_committee, destination, ceremony_id, phase, signer_identity, timestamp)`.

This is not a naming difference. One signed body authenticates a schema/version and the other does not; one authenticates a timestamp and the other does not. `ref/STRING_FIELD_REGISTRY.md:134-141` and `ref/gen_string_field_registry.py:239-240` adopt the line-610 version, including `openauth.timestamp` and no `openauth.schema_version`. Thus the V80 repair claim that V79's second body was withdrawn is false in the document's own bytes, and the generated registry entrenches the wrong body. A mechanical set comparison gives `missing_from_tuple = ['schema_version']`, `extra_in_tuple = ['timestamp']`.

This also defeats the registry's completeness claim: the opening-authority leaves are hand-injected by the generator rather than extracted from Clause 6, so the generator exits clean on the contradiction it created.

### F2 — HIGH — `REFUSED-SCHEMA-NONCONFORMING` is called recomputable although the evidence is neither logged nor assigned a §11 consumer

The access-log schema at line 589 carries timestamp, actor, row, operation, object identity, success/refusal, refusal reason, and chain digest — explicitly “never payload bytes.” Line 594 nevertheless retains the specific code `REFUSED-SCHEMA-NONCONFORMING`, and line 626 classifies that code as **RECOMPUTABLE from the chain and pinned artifacts**. That cannot be done for a refused write: schema conformance is a predicate of the proposed payload, the refusal commit has no store effect, and the chain contains neither the payload nor a payload digest/evidence object. The lifecycle spec's write-validation corner (`LIFECYCLE_GUARANTEE_SPEC.md:116-132`) places the payload in pre-commit staging, not in an authenticated audit artifact.

Line 626 then names “the §11 audit pass — the enumeration verifier's sibling clause” as the consuming verifier at five gates. No such audit-pass item exists in the complete §11 inventory at lines 1156-1485. The only related item is the catch-all enumeration verifier at lines 1464-1476, whose declared input and job concern `REFUSED-UNCLASSIFIED`, enumeration entries, and their joins—not replaying rejected payload schema checks for every specific refusal.

Therefore a false `REFUSED-SCHEMA-NONCONFORMING` remains attributable testimony at best, not recomputable evidence. Because it is a specific code, it bypasses the catch-all enumeration machinery that line 625 relies on to keep false specific reasons from becoming silent.

### F3 — HIGH — the render lifecycle commits a “render” before any render exists

The lifecycle spec defines a RENDER as display to a human (`LIFECYCLE_GUARANTEE_SPEC.md:12-19`) and requires every render to be its own touch with a true event (G2/G5, lines 30-35). But the same spec explicitly allows a “render buffer” to exist after its touch commit when no session ever opens because the process crashes between commit and first frame (lines 117-120). V80 line 634 likewise says delivery occurs after the touch commit from Row B's committed buffer.

That corner cannot satisfy the definitions in both directions. If the pre-frame event says a render occurred, it is false: no frame was displayed and no view session opened. If it records only the actual store-to-buffer conveyance, the later first displayed frame is the RENDER and needs G5's fresh render event. N1 permits the log to over-report delivery; it does not permit an event to claim a touch kind that never happened, because G2 says the event is true of the store effect it records. The special “no session ever opens” destruction rule acknowledges the counterexample instead of assigning it a coherent event type.

The state machine must distinguish a committed conveyance-to-render-buffer from the render/display event, or move the render touch boundary to first display. As written, the crash-before-first-frame cell is not covered by G1-G5 with truthful event semantics.

### F4 — HIGH — an unpinned mapping callback gives the verdict path an executable load-and-unload site

V80 lines 1344-1355 claims exactly one dynamic-load site exists, that it is unreachable, and that under the isolated replay “the only code running” is pinned code covered by the AST audit, leaving nowhere for an unloader. The actual counterfactual path disproves that composition claim. `ref/gain_counterfactual_path.py:120-143` directly calls the supplied `mapping(gamma, mask, cal)` before calling the pinned v9 functions. The wrapper checks only the callback's returned values. V80's nineteen-field BS-3g schema (`:1181-1186`) has a `mapping_id` but no mapping implementation digest; `counterfactual_path_sha256` pins the caller, not the callable it dispatches to.

A mapping callable can therefore import a module, use it, remove its entries from `sys.modules`, and return a valid sign vector/calibration. I exercised that shape under `env -i`, `-I -S`: the callback transiently loaded `_decimal`, `decimal`, and `fractions`, removed them, returned a valid counterfactual result, and the end snapshot reported none of those modules and no new modules. This is the precise load-then-unload path V80 says cannot exist. It is also an attribute/callback edge the name-based graph cannot close; `ref/RAISE_CALLSITE_LEDGER.md:7` correctly admits that graph is only a lower bound.

Pinning `mapping_id` text does not pin executable callback bytes. Either the mapping implementation and its imports must be included in the receipted code/manifest closure, or arbitrary callback dispatch must be replaced by a pinned implementation. Until then, the final-state `sys.modules`/loader snapshot cannot close transient loads.

### F5 — HIGH — optimization mode survives `-I -S` and removes a verdict-path integrity guard

The replay bootstrap at V80 lines 1327-1338 pins interpreter path/hash and dependency roots and requires `-I -S`, but it does not pin the interpreter's optimization mode or full argument vector. `-O` composes legally with `-I -S` and does not change the interpreter binary hash. `require_environment()` checks only Python major/minor, NumPy version, and byte order (`ref/successor_ref_v9.py:50-64`); the recorded environment likewise has no `sys.flags.optimize` field.

This matters to the verdict, not merely to diagnostics. `run_production_verdict()` computes the calibration path before the statistic and then enforces stability only with:

`assert out["path"] == path, "calibration path changed after the statistic — FAIL"`

at `ref/successor_ref_v9.py:1622`. Python strips that guard under `-O`. A live probe with the pinned v9 bytes and matching frozen environment produced `AssertionError: calibration path changed after the statistic — FAIL` at optimization 0, but returned an accepted `INCONCLUSIVE` / `PROFILE` result at optimization 1 on the same adversarial calibration object. The interpreter path, v9 digest, Python 3.9, NumPy 1.26.4, and byte order all remained unchanged.

Thus `-I -S` does not remove every configuration rebinding vector, and the production-equal replay claim is false unless optimization is pinned/refused (preferably by replacing the safety-critical `assert` with an unconditional check as well).

## Failed attacks / checks that held

- Subject identity held before and after review.
- `tools/prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; I did not report the 97 legacy citations, per the brief.
- `tools/prereg_counts.py` reproduced 16 class P / 8 class E.
- `tools/prereg_trace.py --check` reproduced 79 transitions / 0 problems.
- `tools/void_registry.py` reproduced 54 antecedents and its six-control self-test passed; I did not treat name coverage as semantic coverage.
- `tools/lifecycle_derivation_check.py` reported 0 problems and its nine controls passed. The render finding above is a defect inside the pinned spec/draft construction, not a byte-divergence that this checker claims to detect.
- `tools/refusal_vocabulary_check.py` reported 0 problems and all 29 controls passed. F2 is outside its stated phrase/mechanism checks.
- The claimed digests for `LIFECYCLE_GUARANTEE_SPEC.md`, `ref/successor_ref_v9.py`, and `tools/refusal_vocabulary_check.py` match current disk bytes.
- I did not re-derive the parked VOID partition, durable pre-verdict state, χ-adaptive identity leak, BS-3g lifecycle cycle, strata/producer issue, draw discipline, `require_authorization`, or the per-raise/per-call-site referral.

## Scope and custody

I modified no draft, checker, reference, registry, spec, or other artifact. The only written file is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V80
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 L610; Clause 6 L735; ref/STRING_FIELD_REGISTRY.md L134-L141 | The supposedly withdrawn second opening-authorization body still substitutes timestamp for Clause 6's schema/version.
F2 | HIGH | REPAIR-REQUIRED | §6.1 L589, L594, L626; §11 L1156-L1485 | SCHEMA-NONCONFORMING is not recomputable from a payload-free chain, and its named §11 audit consumer does not exist.
F3 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md L12-L19, L30-L35, L117-L120; §6.1 L634 | A crash before first frame leaves a committed “render” event although no render or view session occurred.
F4 | HIGH | REPAIR-REQUIRED | §11 L1181-L1186, L1344-L1355; ref/gain_counterfactual_path.py L120-L143 | The unpinned mapping callback can load and unload modules before the end snapshot, defeating the composition proof.
F5 | HIGH | REPAIR-REQUIRED | §11 L1327-L1338; ref/successor_ref_v9.py L50-L64, L1591-L1624 | Unpinned -O survives isolation and strips the verdict path's calibration-stability assert.
<!-- END FINDINGS-BLOCK -->
