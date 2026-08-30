# V80 whole-document adversarial referee — CODEX

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V80_REVIEW.md` first and verified the subject at sha256 `a9d5d0a2214fe4b16d15a4821d2463209b2105424eb2ce9b84933769e2656edc` before reading it. V80 closes some literal V79 statements, but six repair-required defects survive. Most seriously, the composition proof ignores caller-controlled Python dispatch that the frozen production path accepts: a conforming `SealedMask` subclass can execute and unload code, change the signs seen by the verdict machinery, retain the original mask digest, and disappear from the replay-end module census. The isolated bootstrap also leaves `-O` unbound even though frozen v9 uses a load-bearing `assert`. Separately, the supposedly withdrawn second opening-authorization body still differs from Clause 6 and has propagated into the generated registry; the monotone-presence audit cannot establish sameness because the event schema omits store identity; the request lifecycle gives a live indefinitely-stuck request no terminal transition; and the refusal checker still accepts both a suffixed non-member and ordinary retired-token reactivation.

## Findings

### F1 — HIGH — caller-controlled mask dispatch defeats the composition proof and the replay-end census

V80 §11 lines 1347–1355 says frozen v9 has exactly one dynamic-load site, that only pinned code runs before the end snapshot, and that “an unload requires an unloader, and there is nowhere for one to live.” The frozen bytes contradict that composition claim even without reaching `_frozen_planner`.

`ref/successor_ref_v9.py` lines 1097–1110 accepts subclasses through `isinstance(m, SealedMask)`. The verdict path then repeatedly dispatches through attributes on that caller-supplied object (`m.s`, `m.c`, `m.digest`, `m.n`) in `perm_record()` and its callees. Python attribute dispatch is executable caller code and is invisible to the name-only call graph.

I constructed a `SealedMask` subclass whose `__getattribute__('s')` imported the pure-Python `colorsys` module, removed it from `sys.modules`, and returned the negated sign vector. Executing the pinned `perm_record()` on eight rows produced:

```text
{'accepted_subclass': True,
 'digest_unchanged': True,
 'beta_base': 1.6666666666666667,
 'beta_seen': -1.6666666666666667,
 'transient_module_absent': True}
```

Thus the accepted object retained the digest computed over the original signs while the statistic consumed their negation; the transient module was absent at the final census. The same shape exists one guard earlier: `run_production_verdict()` requires only `isinstance(stage_c_receipt, dict)` and invokes attacker-controlled `.get()` at lines 1600–1605. My bounded probe reached an overridden `get()` immediately. The lower-bound call graph therefore cannot support “only pinned code runs,” and current-state `sys.modules`/loader-image enumeration cannot detect the executed-and-removed code.

Required repair: reject subclasses and other dynamic-dispatch carriers at every production boundary (or canonicalize into exact immutable base objects before any verdict use), bind recomputed values to their digests at consumption, and enforce a monotone load/import event policy rather than an end-state census.

### F2 — HIGH — `-I -S` leaves optimization mode free while v9 relies on a load-bearing `assert`

V80 §11 lines 1324–1363 claims the isolated bootstrap removes every configuration rebinding vector short of owning the interpreter or OS. The BS-7p environment sub-schema binds the interpreter path/digest and dependency roots, but it does not bind interpreter flags or require `sys.flags.optimize == 0`.

`python -O -I -S` is valid and reports all three isolation properties while setting `optimize = 1`. Under that mode Python removes assertions. Frozen v9 uses an assertion at `ref/successor_ref_v9.py` line 1622 to enforce that the calibration path selected before the statistic is unchanged after `_decide_from()` recomputes it:

```python
assert out["path"] == path, "calibration path changed after the statistic — FAIL"
```

Bytecode inspection reproduced the difference: the check is present at optimization level 0 and absent at level 1. This is not a cosmetic assertion: `cal` is a caller-supplied `dict`, exact type and immutability are not enforced, and `_decide_from()` calls `adjudicate_path(cal)` again. A stateful mapping can therefore present one path before the statistic and another afterwards; ordinary mode refuses the mismatch, while `-O` accepts it. The configuration vector survives `-I -S` and is not part of the declared trust boundary.

Required repair: pin and verify the complete interpreter invocation and relevant `sys.flags` (at minimum optimization level), and replace every load-bearing `assert` with an unconditional checked refusal. Exact-type/canonicalization repair from F1 must also cover `cal`.

### F3 — HIGH — the “withdrawn” second opening-authorization body still exists, and the registry follows the wrong one

V80 §6.1 line 610 says the opening authorization is Clause 6’s body and then gives this alleged Clause-6 order:

```text
(bsl_digest, store_identity_main, store_identity_committee,
 destination, ceremony_id, phase, signer_identity, timestamp)
```

Clause 6 at line 735 instead binds exactly the BS-L digest, both store identities, destination, ceremony identifier, phase P7, Duho’s signer identity, and **schema/version**. It does not bind a timestamp. V80 therefore did not withdraw the second body; it changed its first fields but retained the incompatible `timestamp`/`schema-version` substitution.

The mismatch has propagated into the mechanism advertised as exhaustive. `ref/gen_string_field_registry.py` lines 82–86 and 239–240 hard-code `openauth.timestamp` and omit any schema/version leaf; `ref/STRING_FIELD_REGISTRY.md` lines 134–141 does the same. A direct set comparison gives:

```text
expected_minus_generator ['openauth.schema_version']
generator_minus_expected ['openauth.timestamp']
```

Two implementers following the two normative passages still hash different bodies, and the registry classifies the field Clause 6 does not contain while failing to classify the one it does.

Required repair: choose one eight-field body, make line 610 and Clause 6 byte-identical in field identity and order, and mechanically extract those leaves into the registry rather than hard-coding a competing list.

### F4 — HIGH — the monotone-presence disjunction cannot prove it is about the same stored object

V80 §6.1 line 626 now says a prior committed touch plus a later `REFUSED-OBJECT-ABSENT` proves either a false refusal or a forbidden removal, relying on append-only stores and monotone presence. That inference requires the two events to identify the same object in the same store.

The event schema at line 589 contains `object identity` but no store identity. The registry makes the limitation concrete at `ref/STRING_FIELD_REGISTRY.md` line 174: object identity is only “brickid/objid keys.” Clause 4 at line 731 says one access log covers all three sealed stores. The same `(brickid, objid)` can therefore be touched in the main store and truthfully absent in the committee store or predecessor archive. Nothing in the committed event identity establishes the store component needed for the join. `table row` and the as-yet-uninstantiated closed `operation` set do not repair this: rows can touch more than one store (notably unsealing), and the schema never requires operation tokens to encode store identity.

So history plus later absence need not imply either disjunct; it can simply describe different stored objects sharing the coarsened identity. The named §11 audit consumer would surface a false contradiction.

Required repair: bind an immutable store/object namespace into every event identity and into the audit join, or narrow the history rule to event classes whose row and closed operation token provably determine one store and specify that proof in the schema.

### F5 — HIGH — a live indefinitely-stuck request has no terminal treatment

The lifecycle claims every request reaches exactly one commit/treatment. `LIFECYCLE_GUARANTEE_SPEC.md` lines 77–80 gives only:

```text
RECEIVED → PENDING-AUTHORISATION → (writes: PENDING-SURFACE-CHECK) → one commit
```

N2 at line 54 covers a request whose processing dies before commit. Draft line 646 covers a worker timeout, deadlock, or lost verifier only after “processing fails while Row B survives,” at which point Row B emits `REFUSED-UNCLASSIFIED`. Neither file defines the deadline, watchdog, lease expiry, failure detector, or transition that turns a live but permanently stuck worker/verifier into that failure.

Counterexample: Row B remains alive, a worker remains alive but blocks forever in `PENDING-AUTHORISATION` (or a write blocks forever in `PENDING-SURFACE-CHECK`), and no timeout is configured. The request neither dies (so N2 does not apply) nor fails in a detectable way, and no commit occurs. It remains undecided and unlogged indefinitely, contradicting the draft’s “every state has one terminal treatment” and Clause 10’s branch-termination rule. This is distinct from the parked durable pre-verdict/N2 issue: no crash or missing durable event is needed.

Required repair: make liveness part of the BS-2k design contract—pin bounded per-state deadlines and the authority that observes expiry, require expiry to produce one refusal commit while Row B survives, and fixture a permanently non-returning worker/verifier.

### F6 — MEDIUM — the blocking refusal checker still accepts non-members and direct retired-token reactivation

`tools/refusal_vocabulary_check.py` line 137 uses:

```python
(?<![A-Z0-9-])REFUSED-[A-Z][A-Z-]+
```

There is no right token boundary and digits are excluded from the captured suffix. Consequently the operative token `REFUSED-UNCLASSIFIED2` is parsed only as the legal prefix `REFUSED-UNCLASSIFIED`; running the actual `check()` returned `[]`. A non-member can therefore occupy prose while the eleven-code check remains green.

The retired-token rule at lines 121–160 also remains a finite English activation heuristic. The V80 additions catch the prior examples, but the actual checker still returned `[]` for both:

```text
REFUSED-LOCK-NOT-OPEN was retired, but is required for every P7 opening.
REFUSED-CEREMONY-CONSUMED was superseded, but remains the required rule for replay.
```

The checker comments admit the activation list is incomplete, but the lint uses this result as the blocking active/retired corpus check. An admitted semantic limit does not make an accepted active non-member safe.

Required repair: add a proper right boundary and include the full allowed identifier alphabet in tokenization; more importantly, permit retired-code mentions only through a canonical machine-readable tombstone grammar or derive active/retired membership from one structured source of truth rather than attempting to enumerate activation prose.

## Failed attacks / repairs that held

- Subject sha256 matched before reading. Companion and pinned bytes also matched: lifecycle spec `eeead2285f6a905cd2e92b7ab853de4f383b6000d25d3428b10e5d7bb2f3bf49`; refusal checker `0b9e1f0d9d66e28120ba1e94bb6862efc83651cbb6fcfabecca52d1437dae341`; frozen v9 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; closure worker `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- `tools/prereg_lint.py` exited 0 with 16 class P / 8 class E and 97 advisory, 0 blocking findings. I did not re-report the principal-parked legacy citation advisories.
- `tools/prereg_counts.py` independently reproduced 16 class-P and 8 class-E rows; prose matched.
- `tools/prereg_trace.py` reproduced 79 transitions with 0 problems after invocation against the build directory.
- `tools/lifecycle_derivation_check.py` reported 0 problems and its nine controls passed. The exact G/N quote bytes and lifecycle pin hold; F5 attacks an uncovered liveness branch rather than a quote mismatch.
- `tools/refusal_vocabulary_check.py` reported 0 problems on V80 and its 29-control self-test passed. F6 records inputs those controls do not detect; it does not misstate the green result.
- `tools/void_registry.py` parsed 54 antecedents and 20 §6.1 rows. I treated this as name coverage only, as the draft requires.
- Independent AST/table reconciliation reproduced all 112 raise nodes and the ledger classes exactly: 26 CALLER, 59 INTEGRITY, 20 NUMERICAL, 3 PLANNING-INTERNAL, 1 TYPED-OUTCOME, 3 WRAPPER. I did not re-derive the parked per-raise versus per-call-site defect.
- The canonical payload framing and declared raw/UTF-8/decimal/hex/canonical-JSON encodings now exist. F3 is a field-identity conflict, not a repeat of V79’s missing-payload-encoding finding.
- The NAMES-CLASS definition now binds the member token’s own definition to the coarse key. I did not re-report V79 F5.
- I did not attack the draw discipline or re-derive the parked VOID partition, durable pre-verdict state, strata/producer pair, known logged-identity leak, integrity-mismatch collision, BS-3g lifecycle cycle, authorization limitation, call-site unit, Row-L phase, or other principal-referred issues.

## Evidence and scope

Read in content: `gates/BRIEF_V80_REVIEW.md` first; exact V80 bytes; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; and V79 CODEX report only to distinguish old findings from V80 repairs, with every retained claim independently checked against current bytes.

Executed read-only: SHA-256 recomputation; prereg lint; counts and trace checks; lifecycle derivation check and self-test; VOID registry parse; refusal checker and self-test; AST/table raise reconciliation; bytecode comparison under optimization levels 0/1; a bounded caller-dispatch/load-unload/sign-mutation probe; a bounded overridden-`dict.get` reachability probe; and synthetic retired/non-member vocabulary probes. I did not modify the draft, companion, references, tools, registries, or any file outside this report. This report is the sole intended write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V80
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1347–1355; ref/successor_ref_v9.py lines 1097–1110 | Accepted SealedMask subclass dispatch can execute and unload code, alter consumed signs under the original digest, and evade the end snapshot.
F2 | HIGH | REPAIR-REQUIRED | §11 lines 1324–1363; ref/successor_ref_v9.py line 1622 | Unbound `-O` survives `-I -S` and removes the load-bearing calibration-path assertion.
F3 | HIGH | REPAIR-REQUIRED | §6.1 line 610; Clause 6 line 735; ref/gen_string_field_registry.py lines 82–86, 239–240 | The supposedly withdrawn second opening body substitutes timestamp for schema/version, and the generated registry follows it.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 589, 626 and Clause 4 line 731 | The monotone-presence audit lacks store identity and can join different stored objects sharing brickid/objid.
F5 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md lines 54, 77–80; §6.1 line 646 | A live indefinitely-stuck pending request has no deadline, failure transition, commit, or terminal treatment.
F6 | MEDIUM | REPAIR-REQUIRED | tools/refusal_vocabulary_check.py lines 121–160 | Missing right token boundary and finite activation prose let a suffixed non-member and direct retired-code reactivation pass.
<!-- END FINDINGS-BLOCK -->