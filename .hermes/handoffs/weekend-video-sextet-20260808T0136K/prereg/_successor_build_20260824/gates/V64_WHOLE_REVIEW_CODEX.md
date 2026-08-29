# V64 whole-document referee — CODEX

## Verdict

**NOT CLEAR.** The draft hash matched the brief, but the new request lifecycle is not crash-safe, the availability codes directly violate the vocabulary's own non-object principle, and the catch-all guard has no enforceable freeze artifact. The BS-3g specification also admits a favourable perturbation manifest and does not actually supply the frozen draw values or closed identifier sets its verifier is supposed to enforce. Two referenced-file checks independently fail: the authoritative raise ledger contradicts V64 on L986, and the refusal-checker digest stated in V64 is stale.

## Findings

### F1 — HIGH — the request lifecycle cannot log a request after the process that alone knows it has died

V64 §6.1 lines 606–608 says a request is in exactly one state, places the durable log boundary only when a permission verdict is reached, and then promises that a request which dies earlier in `RECEIVED`, `PENDING-AUTHORISATION`, or `PENDING-SURFACE-CHECK` "is logged" as `REFUSED-UNCLASSIFIED`. No durable request record, recovery actor, watchdog, transaction, or replay rule exists before the verdict boundary. A crash in `PENDING-AUTHORISATION` can therefore erase the only process able to append the promised refusal. The write path is worse: line 607 requires payload decode before the verdict/log append, so a crash during decode has already touched the payload but leaves no event. The assertion that "no request can end undecided or unlogged" is not implemented by the state list.

There is a second atomicity hole at the boundary itself. Computing a verdict and appending an event are distinct effects; "at the instant" does not make them atomic. A crash after the verdict is computed but before the append produces a decided, unlogged request. Conversely, the sole event is appended before transfer, yet line 608 later says a transfer death is "completed as FAILED under the availability codes" without authorising a second event or an update to the append-only first event. Repair requires a durable pre-verdict request identity plus a recovery/transaction protocol that settles exactly one terminal event, including the write-decode and verdict→append crash windows.

### F2 — HIGH — four new refusal codes describe the object, contradicting the governing principle and creating a new per-object leak

Section 6.1 line 590 says a refusal reason may describe the request and authorisation state but "may never describe the OBJECT" and claims the reason adds no per-object information beside the logged object identity. Lines 593–594 then admit `REFUSED-OBJECT-ABSENT`, `REFUSED-OBJECT-UNREADABLE`, `REFUSED-OBJECT-INCOMPLETE`, and `REFUSED-INTEGRITY-MISMATCH`. Each is explicitly a property of the identified object. An access-log reader learns, for object X, that X is absent, unreadable, incomplete, or digest-mismatched. This is distinct from the parked `REFUSED-OUTSIDE-STATED-SURFACE` membership leak: it publishes availability/integrity state for an otherwise permitted request. The claimed principle therefore does not bind the eleven-code set it is said to justify.

### F3 — HIGH — the catch-all guard is a wish, and a routine timeout passes it

Section 6.1 line 596 says every `REFUSED-UNCLASSIFIED` emission is enumerated at freeze, its count reviewed, and each emission named or explained. But an emission caused by a run-time verifier timeout at line 608 does not exist at freeze. No class-P slot, schema field, producer, verifier, zero-count requirement, or dependency edge records freeze-time catch-all fixtures or blocks freeze on them. A verifier that times out on every request can therefore route every request to the same catch-all, while the prose still says that class was "enumerated"; line 609 even concedes that this foreseeable routine class is being routed into the defect category.

`tools/refusal_vocabulary_check.py` does not enforce the guard. Its R05 implementation (lines 131–133) only searches the whole document for the phrases `enumerated at freeze` and `REFUSED-UNCLASSIFIED`; it does not parse an emission inventory, require a count, require zero, bind a freeze artifact, or test a blocking edge. R01 similarly collects backticked codes globally (lines 102–109), not from the normative vocabulary list. Thus the checker exits 0 on the present prose while proving none of the operational claims that are load-bearing after taking the catch-all.

### F4 — HIGH — a singleton favourable perturbation manifest passes BS-3g while omitting the allowed range

The BS-3g schema binds only `perturbation_manifest_sha256` and `n_perturbations` (lines 1043–1046). Lines 1071–1073 define the manifest merely as the ordered list of γ values evaluated. Verifier clause (a0), lines 1125–1129, recomputes that digest and checks only that the reported count equals the manifest length. It never binds the manifest to a preregistered grid rule, requires coverage of `gamma_bound`, requires both endpoints or both signs, or even requires a nonzero perturbation.

A manifest containing only γ = 0 therefore has a valid digest and length 1, and every draw×perturbation cell equals `baseline_verdict`; clause (e) then reports `HELD` under lines 1133–1137. This is a receipt that passes all manifest/count/draw checks while reporting the worst of the chosen list rather than the worst over the allowed perturbations. Hashing a favourable subset authenticates the subset; it does not establish coverage.

### F5 — HIGH — the frozen draw comparison and closed identifier sets have no values to compare against

V64 says the four draw-set gaps are "CLOSED HERE" (line 1095), and verifier clause (e) must compare `n_draws` and `draw_master_seed` against values "frozen in this preregistration" (lines 1136–1137). The document contains no concrete `n_draws` or `draw_master_seed` value. The BS-3g row itself says the count and generator "are not yet frozen" and `mapping_id` remains `MAPPING-NOT-PREREGISTERED` (line 791). Likewise, line 1117 asserts `draw_generator_id` and `mapping_id` come from closed enumerated sets declared in the document, but no such member lists are declared; the only literal mapping token is the non-discharging placeholder.

Consequently the future verifier has neither comparison constants nor an enumerated generator family. A producer can still choose gate strictness (`n_draws`), seed, and generator definition at the later implementation/freeze step while satisfying the current prose. Saying they will be frozen later does not close the precommitment gap in the bytes that claim to close it. At minimum the current text must stop claiming closure; a genuine repair must pin the values and identifier sets in an independently verifiable freeze component before any candidate seed/generator is evaluated.

### F6 — MEDIUM — L986 is repaired in prose but remains CALLER in the authoritative live classification

Section 5 line 503 correctly distinguishes L986 `MOVE_CAP` from L963/L973: it fires on an internal frozen cap after a feasible prefix and is dispositioned `PLANNING-INTERNAL`, not CALLER. The same draft later says all three sites are CALLER (line 528). `ref/RAISE_SITE_CLASSIFICATION.md` repeats the stale premise at line 9 (all three are setup errors against caller-supplied `l_plan`) and classifies L986 as CALLER at line 81. This contradicts both the source condition and V64's stated repair, while §5 calls the generated ledger authoritative. The class totals and downstream conversion inventory therefore remain based on a classification V64 itself disproves.

### F7 — MEDIUM — the refusal-checker SHA claim does not match the referenced file

Section 6.1 line 603 says `c2ccebbcb4730944…` is the SHA-256 of `tools/refusal_vocabulary_check.py` and that both named values are right. The live referenced file hashes to:

`acb38c401e00b07565fe753206644acae99c1e8d8ea5ac66f58fa63bed7047d4`

The claimed `c2ccebb…` prefix is the prior checker bytes, not the rewritten eleven-code checker reviewed here. Because the paragraph uses that digest to distinguish the row fingerprint from the tool identity, this is a false referenced-file claim, not cosmetic drift.

## Failed attacks / checks that held

- Subject SHA-256 recomputed exactly to `af171440cd2d31c6b247f784c19f3ecc0d10647dd25eb5fbd93399565c688bbe` before the draft was read.
- The frozen `successor_ref_v9.py` recomputed exactly to its §0 pin `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/prereg_lint.py` exited 0 with 16 class-P / 8 class-E rows and 97 advisory, 0 blocking findings. I did not convert the brief's permanently advisory legacy citations into findings.
- `tools/prereg_trace.py` checked 64 computed transitions with 0 problems. (The brief's stated 63 is stale, but the checker found no trace defect.)
- `tools/void_registry.py` parsed 54 antecedents and 20 §6.1 rows. I did not re-report the parked semantic-coverage limit or the parked VOID/numerical partition.
- `tools/refusal_vocabulary_check.py --self-test` reported 10 controls, 0 failures; the live V64 check reported 0 problems. Findings F2–F3 concern what those lexical controls do not prove.
- The withdrawal held in the classification table: no raise site is assigned `UNREACHABLE-BY-CONSTRUCTION`.
- I found no surviving five-step computation rerun allowance; the remaining Stage-P rerun language concerns completing the unfilled planning gate, not retrying a terminal run outcome.

## Evidence ledger

Read in full: `gates/BRIEF_V64_REVIEW.md`; the exact V64 draft bytes; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/gain_counterfactual_path.py`; `tools/refusal_vocabulary_check.py`. Mechanically searched the V64 bytes for refusal codes, lifecycle terms, draw fields, `UNREACHABLE-BY-CONSTRUCTION`, and rerun/retry language. Executed SHA-256 checks, refusal checker and self-test, prereg lint, prereg trace, VOID registry, and pre-write git status. No draft, code, ledger, or file outside this report was modified.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V64
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 606–610 | Pre-verdict death and the verdict-to-append gap leave requests undecided or unlogged despite the lifecycle's universal claim.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 590, 593–600 | Four availability codes explicitly describe the logged object and create a new per-object state leak.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 596, 608–610; refusal checker lines 102–133 | The catch-all has no freeze artifact or blocking invariant, and the checker only phrase-matches the guard.
F4 | HIGH | REPAIR-REQUIRED | §11 lines 1043–1046, 1071–1073, 1125–1137 | A γ=0 singleton manifest passes all BS-3g checks while omitting the allowed perturbation range.
F5 | HIGH | REPAIR-REQUIRED | §7 line 791; §11 lines 1095–1120, 1133–1138 | No concrete frozen draw values or closed generator/mapping sets exist for the claimed verifier comparisons.
F6 | MEDIUM | REPAIR-REQUIRED | §5 lines 503, 528; raise-site ledger lines 9, 79–81 | L986 is PLANNING-INTERNAL under the source and V64's repair but CALLER in the authoritative live classification and later prose.
F7 | MEDIUM | REPAIR-REQUIRED | §6.1 line 603 | V64's claimed refusal-checker SHA prefix c2ccebbcb4730944 disagrees with the live referenced file's acb38c401e00b075 hash.
<!-- END FINDINGS-BLOCK -->