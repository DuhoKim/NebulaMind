# V63 whole-document referee — CODEX

## Verdict

**NOT CLEAR.** The dispatched bytes match the required digest, but the round's highest-value repair does not survive a literal counterexample: a value produced during this run can subsequently be sealed and verified before unblinding, so the new numerical/VOID question assigns the same post-unblinding failure to both sides. The new draw fields authenticate a replay only after the fact and do not authenticate the asserted pre-verdict choice of draw count and seed. The BS-3g field-list proof also relies on identifier and seed fields whose lexical types and widths are not specified. Independently, the draft still overstates `require_complete_sample()` even though the pinned function accepts any equal pair of caller integers without inspecting a parent or a receipt.

## Findings

### F1 — HIGH — the new numerical/VOID partition is not exclusive

**At issue:** §5 lines 495–501, especially the exclusivity claim at line 499; §6.1 phase order and BS-8f/BS-5f production at lines 598, 613–614.

The draft asks whether the failing quantity “was PINNED, SEALED OR VERIFIED before this point, or did the run COMPUTE it?” and then asserts that a pinned object is not computed by this run and that a computed quantity was not verified before unblinding. Those assertions are false for the draft's own lifecycle. Row I computes BS-8f during this run at P4, Row J computes BS-5f at P5, and both artifacts are then authenticated and bound into BS-L before P7 unblinding. At P8, each is therefore simultaneously (a) a quantity computed by this run and (b) an object sealed/verified before the failure.

Concrete counterexample: after unblinding, Row P or the required pre-verdict validator reopens the BS-L-bound BS-8f bytes and discovers that an aggregate field is non-finite or degenerate. Under line 497, the already-verified BS-8f object now contradicts its certification and is `VOID-5-NONFINITE`/`VOID-5-DEGENERATE`. Under line 498, that same aggregate is a quantity the run computed from the calibration inputs and is `INCONCLUSIVE-BY-NUMERICAL-FAILURE` (or the calibration-specific code). The draft's “mixed case” sentence covers a derivative of a pinned object; it does not cover an object that was first computed by the run and later sealed and verified. Precedence is needed to decide the case, so line 501's own falsification test says the repair has not landed.

The repair needs a time-indexed custody rule, not an origin dichotomy—for example, classify the failure by whether the currently failing bytes equal the authenticated bytes that passed the named prior verifier, regardless of who originally computed them.

### F2 — HIGH — all four draw fields can verify after adaptive choice of `n_draws` or seed

**At issue:** §11 lines 1024–1031, 1058–1068 and verifier clause (e), lines 1080–1087.

The receipt records `n_draws`, `draw_generator_id`, `draw_master_seed`, and a digest of the replayed verdict sequence. Clause (e) can therefore prove that the final receipt is internally replayable and that its reported outcome is the worst of the declared sequence. It cannot prove either chronology assertion the text makes: that `n_draws` was fixed before the first draw, or that the master seed was selected before any verdict was seen.

An operator can evaluate several candidate seeds or progressively larger prefixes off record, inspect their verdicts, then choose a favourable `(n_draws, draw_master_seed)` pair and emit one receipt. The verifier regenerates exactly that chosen sequence, sees exactly `n_draws` draws, reproduces the digest, confirms the worst member, and accepts. All four fields and clause (e) pass even though the gate was selected after seeing verdicts. “Exactly `n_draws`, all evaluated” prevents early stopping inside the declared sequence; it does not prevent selection among undeclared sequences.

Because the draft correctly says draw count is the gate's strictness, both count and seed need a pre-draw commitment external to the receipt they later help produce: a separately authenticated pre-execution artifact/digest, bound into BS-3g and checked for ordering before any draw event. A post-run self-report cannot authenticate its own pre-result timing.

### F3 — MEDIUM — the BS-3g field list does admit object-indexed payloads

**At issue:** §11 lines 1019–1023 and the universal-negative proof at lines 1091–1097.

The draft says every field is a fixed-width scalar, digest, closed token or count and that no allowed field can carry an object identifier or per-object quantity. The exact field definitions do not establish that. `mapping_id` and `draw_generator_id` are merely “stable identifiers”: no closed registry, lexical grammar, canonical encoding, or maximum length is specified. `draw_master_seed` is called a “single frozen seed,” but no integer/byte type, range, or width is stated. `n_draws` and `n_perturbations` are integers with sign constraints but no encoding or width.

A conforming serialized value in any unconstrained identifier field—or an arbitrary-precision seed/count—can encode an object ID or an object-indexed bitstring while still occupying an allowed field. Exact field-set checking rejects an extra key; it does not constrain the information capacity of an under-specified allowed key. The future verifier's requirement that an identifier “name” a preregistered mapping/generator is also not a lexical/type contract unless the registry and canonical identifier bytes are themselves pinned.

This does not show that the intended honest values leak χ. It breaks the stronger property claimed from the field list itself. Pin closed identifier registries and exact byte encodings/widths for every scalar, count and seed before treating BS-3g as non-χ-bearing.

### F4 — HIGH — `require_complete_sample()` authenticates no sample completeness

**At issue:** §5 lines 556–568; pinned `ref/successor_ref_v9.py` lines 1591–1599 and 1647–1649.

The draft accurately limits `require_authorization()` but immediately retains the stronger claim that `require_complete_sample()` “refuses unless every parent object has a measurement receipt.” The pinned function receives only two caller-supplied integers and returns normally when `int(n_receipts) == int(n_parent)`. It reads no parent manifest, receipt set, object IDs, uniqueness relation, receipt digest, or parent digest; the runner passes those same caller arguments directly to it.

Direct execution against the pinned `6a9abbbd…` bytes returned normally for `require_complete_sample(1, 1)`. Thus a partial or empty receipt set can be represented by any equal pair and pass the named guard. Calling the guard by name is not evidence that its stated property was checked. The draft already gives the authorization guard this exact describe-versus-compute treatment; the adjacent completeness guard needs the same disclosure and must be replaced by an exact parent-to-receipt set check before the prose may claim completeness.

## Failed attacks / repairs that held

- The subject SHA-256 was recomputed before reading and exactly matched `8b224c684ea4cdf067883b4d478e3cdef083118ebf7bc9c205c6ae44979ae376`.
- The frozen reference pin recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; the refusal checker recomputed to `c2ccebbcb4730944ce1ff15ca27984feef17b39529f89656c9432b2e83c80b4c`.
- `prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings. Per the brief, I did not report the legacy citation advisories.
- `prereg_counts.py` independently returned 16 Class-P / 8 Class-E rows; `prereg_trace.py --check` returned 62 transitions / 0 problems; `void_registry.py --self-test` returned 6 controls / 0 failures.
- Independent AST enumeration found 112 raises. Parsing the live classification table gave CALLER 26, INTEGRITY 60, NUMERICAL 20, TYPED-OUTCOME 3 and WRAPPER 3, with zero `UNREACHABLE-BY-CONSTRUCTION` rows. No measurement-only promotion remains operative.
- The three `local_pass` sites L963/L973/L986 are reached by `_plan`, and the in-module source exposes `_plan` through `build_plan` and fixtures, not through `run_production_verdict`. The call-site ledger correctly labels its graph a lower bound; I found no concrete run-time path and do not upgrade absence to proof.
- The V43 same-run rerun allowance remains deleted. Remaining uses of “rerun” concern a future Stage-P measurement, historical explanation, or explicit no-retry language.
- `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION` remain phase `Any`; only the numerical non-finite/degenerate antecedents are narrowed to post-unblinding.
- The refusal-vocabulary suspension behaves as described: direct execution of `tools/refusal_vocabulary_check.py` on V63 exits 1 with only R05 because no derivation fingerprint is pinned. I did not report that intended refusal as a defect.
- The Stage-P citation is now honest. Reading `PREREG_TEXT_V11_KIMI.md` confirms F7 is about the v7-subject disclosure and does not support dual-valued Stage P; V63 now says exactly that and records KIMI F13 as the opposite claim.
- For an honestly implemented full-mask verifier, `mask_sha256 == BS-2f.mask_digest` plus independent recomputation defeats the simple favourable-subset attack. F2 concerns adaptive draw-set choice before that replay, not a hash collision or omitted-mask claim.
- The V62 wording correctly scopes `receipt_strict()` to slot-receipt producers and separately lists seven non-slot artifact classes. I found no textual reintroduction of V59's impossible universal binding. BS-3g's schema/producer/verifier remain openly unimplemented, so I do not renumber that disclosed unfinished state.

## Evidence and custody

Read in content: `BRIEF_V63_REVIEW.md` first; the exact V63 draft only after its digest matched; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; the relevant `SLOT_SCHEMA`, `receipt()`, `local_pass()`, mask, verdict-runner and guard regions of pinned `ref/successor_ref_v9.py`; `tools/refusal_vocabulary_check.py`; `tools/prereg_lint.py`; `tools/prereg_counts.py`; `tools/prereg_trace.py`; `tools/void_registry.py`; `gates/PREREG_TEXT_V11_KIMI.md`; and prior V54/V56/V59 CODEX reports as inputs to attack rather than authority.

Executed read-only checks: subject and referenced-file SHA-256; lint; counts; trace; VOID self-test; refusal checker; independent AST and ledger recount; direct `require_complete_sample(1,1)` execution; and a canonical BS-5f `receipt()` probe. The latter confirmed that `receipt()` returns only envelope metadata and not decoded `passed`/`mask_digest` fields; I treated that as evidence for the existing unfinished receipt work rather than adding a fifth finding. No draft, reference, checker, ledger or source file was intentionally modified. The only deliverable write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V63
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §5 lines 495–501 | Run-produced BS-8f/BS-5f artifacts are later sealed and verified, so one post-unblinding failure belongs to both sides of the alleged exclusive partition.
F2 | HIGH | REPAIR-REQUIRED | §11 lines 1024–1031, 1058–1068, 1080–1087 | A replayable receipt cannot prove n_draws and seed were fixed before verdicts; adaptive off-record selection passes all four fields and verifier clause (e).
F3 | MEDIUM | REPAIR-REQUIRED | §11 lines 1019–1023, 1091–1097 | Unbounded identifier, seed and count encodings defeat the claim that no allowed BS-3g field can carry an object-indexed payload.
F4 | HIGH | REPAIR-REQUIRED | §5 lines 556–568; successor_ref_v9.py lines 1591–1599, 1647–1649 | require_complete_sample accepts any equal caller integers and does not verify a parent-to-receipt partition.
<!-- END FINDINGS-BLOCK -->