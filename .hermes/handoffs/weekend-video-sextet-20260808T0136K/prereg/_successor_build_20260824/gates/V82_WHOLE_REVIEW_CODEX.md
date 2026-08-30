# V82 whole-document adversarial referee — CODEX

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V82_REVIEW.md` first and then verified the dispatched draft at SHA-256 `12d54356b4fde6b0dec0919a13f7af65f34a1927a9c1984e427e3401a93ed5ad` before reading it. The advertised compile-from-verified-buffer repair is contradicted by the pinned counterfactual module's own bytes; the newly added harness digest has no independent expected pin or complete verifier obligation; continuation entries can retroactively heal a lock-time enumeration failure; the claimed unique JSON still admits multiple bytes for one value; and the string/authorization closure remains incomplete one level below its named containers. The lifecycle deadline also does not terminate a live-but-stalled atomic commit, and the refusal checker accepts explicit negations of the mechanisms it claims to test.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §11 lines 1335–1348; `ref/gain_counterfactual_path.py` lines 43–50

**COMPILE-FROM-VERIFIED-BUFFER does not eliminate import machinery or the second read it was introduced to eliminate.** The draft says the harness reads both pinned modules once, compiles those buffers into fresh namespaces, and thereby has “no import machinery” and “no second read.” But the exact pinned counterfactual-path bytes execute:

- `sys.path.insert(0, str(Path(__file__).resolve().parent))` at line 49; and
- `import successor_ref_v9 as v9` at line 50.

Executing the verified counterfactual buffer therefore invokes ordinary import machinery. A `python3 -B` probe that compiled and executed those exact bytes with `optimize=0` recorded `ordinary_import_called True` and bound `v9.__file__` to the on-disk `ref/successor_ref_v9.py`. Unless the harness pre-populates `sys.modules['successor_ref_v9']`, the verified v9 buffer is ignored and v9 is read/imported from disk again, restoring the verified/consumed swap and bytecode paths. If the harness does pre-populate it, that binding and its module metadata become load-bearing harness behavior not stated here, while the claim “no import machinery” remains false. A genuinely buffer-only design must either provide pinned bytes whose import line is absent or explicitly define, pin, and verify the module-namespace/sys.modules bootstrap that makes the import resolve only to the already-compiled object.

### F2 — HIGH / REPAIR-REQUIRED — §11 lines 1182–1190, 1230, 1442–1448

**`replay_harness_sha256` is a self-reported digest with no independent expected pin and is omitted from the detailed verifier recomputation.** V82 adds the field and says the verifier refuses a harness digest that differs from “the pinned one,” but the draft contains no expected harness digest, no harness path/module identity, and no separate freeze field naming that expected digest. A content search found no replay-harness implementation in the build; the only occurrences of `replay_harness_sha256` in the draft are the schema field and that assertion. The detailed independent-verifier contract later says it recomputes “all four” module digests—kernel, estimator, verifier, and counterfactual path—and does not include the replay harness. Thus a producer can report the digest of whichever harness it executed, while the verifier has no independently fixed value to compare to and no enumerated obligation to recompute it. Pin the harness as a freeze-time input outside the receipt, identify its bytes/path, add it to the detailed recomputation list, and bind that expected pin through the signed preregistration/slot schema.

### F3 — HIGH / REPAIR-REQUIRED — §6.1 lines 599, 603–610; §11 lines 1489–1501

**The continuation segment can retroactively launder a `BS-L`-time enumeration failure.** Pre-`BS-L` catch-all emissions must be enumerated before `BS-L` issues, while post-`BS-L` entries live in a continuation segment. But the exact enumeration-entry body carries only `(chain_position, event_digest)`, `class_key`, disposition/reference fields, and signature; it carries no segment provenance, bound `BS-L`/checkpoint identity, or issuance epoch. The opening verifier reads checkpoint entries plus continuation entries as one set and the inventory requires a bijection, but neither passage requires a continuation entry's chain position to be strictly after the checkpoint bound by `BS-L`.

Counterexample: a pre-`BS-L` `REFUSED-UNCLASSIFIED` event is left unenumerated and `BS-L` is incorrectly issued; after issuance, mint a validly signed continuation entry joining that old event; the opening union is now bijective and complete even though the lock-time blocking invariant was false. The later entry has healed a gate that was required to have passed earlier. Bind every continuation segment to one `BS-L` identity and require every continuation entry to join a chain position strictly after that signed checkpoint; independently recompute the checkpoint-only enumeration when verifying `BS-L`.

### F4 — HIGH / REPAIR-REQUIRED — §6.1 line 610 (canonical payload encoding)

**The “unique” canonical JSON rules still admit two byte strings for the same logical value and do not define NFC-key collisions.** The rule requires minimal JSON-mandatory escapes but does not fix hexadecimal case. Both `{"x":"\\u001f"}` and `{"x":"\\u001F"}` use the mandatory six-byte control-character escape, satisfy the stated minimality, decode to the same value, and have different SHA-256 digests. NFC creates a second unresolved case: an object containing keys `"é"` and `"e\u0301"` has two distinct source keys that normalize to the same key; the rule says strings are normalized but neither rejects the post-normalization duplicate nor defines which value survives. These are digest/signature ambiguities inside the claimed one-value/one-byte contract. Specify lowercase (or uppercase) escape hex, normalize before sorting, and reject duplicate keys after normalization at every nesting level.

### F5 — HIGH / REPAIR-REQUIRED — §6.1 lines 664–685, 726, 735; `ref/gen_string_field_registry.py` lines 72–94, 247–255; `ref/STRING_FIELD_REGISTRY.md` lines 102, 134–141

**The string/authorization registry closes container names while leaving their load-bearing leaves unenumerated or unbound.** The generator declares `canonical.lock_body` as one digest-ref and comments that the lock body's components are “already enumerated elsewhere,” but the registry has no `lockbody.*` rows for the Clause 3(b) fields (roster, accepted-mask/calibration/Stage-C/decision-input bindings, class-P manifest, checkpoint, archive receipt, environment, signer identity). This repeats the already-recognized container-hides-leaves defect.

The eight opening-authorization field names now match Clause 6, but the value domains still do not close: the registry labels destination and both store identities `closed-vocab` without declaring members or requiring equality to the exact BS-2k-provisioned identity bytes, and labels `schema_version` “the literal” although Clause 6 supplies no literal version token. “Authenticates these fields” verifies a signed author choice; it does not establish that the chosen stores/destination/version are the preregistered ones. Enumerate the lock-body leaves, declare exact opening-authorization member sets/version, and make the verifier compare store identities and destination to independently pinned BS-2k values.

### F6 — MEDIUM / REPAIR-REQUIRED — `tools/refusal_vocabulary_check.py` lines 194–224

**The refusal-vocabulary mechanism checks are polarity-blind.** R08/R09 test only for the presence of phrases such as `enumeration verifier`, `consulted twice`, `chain_position`, `recur`, and `class_key`. They do not test whether the prose affirms or negates those mechanisms. Two in-memory, no-write probes against the full V82 bytes both returned an empty problem list:

1. replacing `explanation stops discharging it` with `explanation alone continues discharging it forever`; and
2. appending `No enumeration verifier exists. It is not consulted twice. Enumeration entries do not carry chain_position. Recurrence needs no class_key.`

The current V82 prose is affirmative, so this is not a claim that those exact bytes negate the mechanism. It is a defect in the referenced checker and in the evidentiary weight assigned to its green result: the checker can certify the literal opposite of the rule it says it checks. Add negative/polarity controls tied to the operative clauses or parse a structured mechanism block instead of searching document-wide substrings.

### F7 — MEDIUM / REPAIR-REQUIRED — `LIFECYCLE_GUARANTEE_SPEC.md` lines 63–70, 81–90; draft §6.1 lines 643–646

**The deadline does not terminate a request stalled inside the single-writer atomic commit.** The spec says a live request past its monotonic deadline receives a refusal commit and that no request may be neither terminal nor within deadline. It also calls W2 “empty by atomicity,” while the draft makes Row B a single serialized writer with at most one decision in flight. Atomicity excludes partially *committed* state; it does not make commit execution instantaneous or guarantee that a stalled transaction/chain append releases the writer.

Counterexample: Row B remains alive but blocks after entering the transaction/chain-append path and before the atomic commit returns. The deadline expires. The same serialized writer cannot append a refusal commit, and a second watchdog writer would create a concurrent second decision unless a specified cancellation/abort arbiter first proves the original commit cannot later complete. This is not parked N2—the writer is alive—and the request is exactly the forbidden state: past deadline, nonterminal, and unable to receive its promised refusal. Specify a deadline arbiter and cancellable commit protocol, including which outcome wins at the timeout/commit race and a fixture that proves the losing path cannot later commit.

## Failed attacks / confirmations (not findings)

- The dispatched draft digest matched exactly before content review; the lifecycle spec digest recomputed to `2520c904b0e5fef5d4f136e6c2b7a05c2e290252ae2bf9d223bd66973cc2f880`, matching line 623.
- `tools/prereg_lint.py` reproduced 16 class-P / 8 class-E rows, 97 advisory legacy citations, and 0 blocking findings. I did not re-report the 97 option-D legacy advisories.
- `tools/refusal_vocabulary_check.py` returned 0 problems on the unmodified V82 bytes and its self-test returned 31 controls, 0 failures. F6 attacks what that green result can prove, not the current eleven-token inventory.
- `tools/lifecycle_derivation_check.py` returned 0 problems. The quoted G/N bodies match the spec; F3 and F7 are semantic failures that byte-copy checking cannot detect.
- `ref/RAISE_SITE_CLASSIFICATION.md` carries 112 rows and the stated 26/59/20/3/1/3 class totals. I did not re-derive the parked per-raise-versus-per-call-site defect.
- The opening-authorization field-name tuple at draft line 610 now matches Clause 6's eight names and ends in `schema_version`; F5 is about value-domain and leaf closure, not another stale-name finding.
- The V43 rerun allowance is absent from the live outcome machinery; I found no surviving retry schedule to report.
- The numerical VOID misconduct antecedents remain `Any` at §7.1 lines 951–953, as required.

## Evidence ledger and scope

Read in content: the review brief; V82 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; and `tools/refusal_vocabulary_check.py`. I also inspected the V81 review/delta only to distinguish new repairs from parked findings. Read-only probes used `python3 -B` or in-memory `compile`/`exec`; they wrote no review artifacts. I did not attack the draw-discipline design choices excluded by the brief and did not re-derive the parked availability-code, durable-pre-verdict-state, strata, VOID-partition, access-membership, BS-3g-cycle, per-call-site, freeze-exemption, BS-2v, or Row-L phase issues.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V82
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1335–1348; ref/gain_counterfactual_path.py lines 43–50 | The verified counterfactual buffer still executes an ordinary import of v9, restoring import machinery and a second disk consumption path.
F2 | HIGH | REPAIR-REQUIRED | §11 lines 1182–1190, 1230, 1442–1448 | replay_harness_sha256 has no independent expected pin and is omitted from the detailed verifier digest recomputation.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 599, 603–610; §11 lines 1489–1501 | A post-BS-L continuation entry can join a pre-BS-L event and retroactively heal a lock-time enumeration failure.
F4 | HIGH | REPAIR-REQUIRED | §6.1 line 610 | Canonical JSON leaves escape-hex case and post-NFC duplicate keys undefined, so one logical value can have multiple canonical bytes.
F5 | HIGH | REPAIR-REQUIRED | §6.1 lines 664–685, 726, 735; STRING_FIELD_REGISTRY lines 102, 134–141 | Lock-body leaves are absent from the registry and opening-authorization value domains are not independently closed.
F6 | MEDIUM | REPAIR-REQUIRED | tools/refusal_vocabulary_check.py lines 194–224 | R08/R09 are polarity-blind and accept explicit negations of the mechanisms they claim to verify.
F7 | MEDIUM | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC lines 63–70, 81–90; §6.1 lines 643–646 | A live Row B stalled inside the atomic commit cannot append the promised deadline refusal, leaving a past-deadline nonterminal request.
<!-- END FINDINGS-BLOCK -->