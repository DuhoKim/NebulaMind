# CODEX — V70 whole-document adversarial review

**VERDICT: NOT CLEAR.** The required subject SHA-256 matched before the draft was read. The mechanical checks are green, but the new lifecycle specification is internally false for refusal events and still leaves the Row-G re-view fork open. The catch-all enumeration introduces pre-unblinding artifacts outside the document's exhaustive non-χ surface, makes one post-BS-L disposition impossible, and is not fully wired at the later gates. Its recurrence key remains caller/implementation-splittable. The BS-3g contract also leaves the actual verdict-producing permutation path unbound and permits a manifest to refute the control only outside the claimed bound.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — Refusal events falsify G3 and have no G2 truth condition

`LIFECYCLE_GUARANTEE_SPEC.md` §0 lines 15–17 defines a refusal commit as `{event, binding}` with **no store effect**. The same spec's G2 says every event is true of the store effect it records, and G3 says both one event per touch and “one touch per event” (§1 lines 30–33). A refusal event has neither a store effect nor a touch. Therefore every refusal commit violates G3's converse, while G2 says nothing checkable about whether its refusal outcome/reason is true.

Concrete counterexample: Row B commits `REFUSED-SCHEMA-NONCONFORMING` for a conforming write, with no store effect. There is one event and zero touches. G1 and G4 hold; N1/N2 do not classify the false refusal; G2 is inapplicable because there is no store effect. This failure lands in no valid G/N cell. The draft repeats the refusal construction at §6.1 lines 630 and 642. A refusal-specific truth invariant is required, and G3's converse must be limited to touch events or refusals must be explicitly outside it.

### F2 — HIGH — REPAIR-REQUIRED — Cached-frame magnification preserves the Row-G unlogged-view fork

The spec defines RENDER as display to a human and G5 says every render has its own committed event (`LIFECYCLE_GUARANTEE_SPEC.md` lines 12–14, 34). It then says dwell and magnification of an already-rendered frame are not touches (lines 87–90; draft §6.1 line 649), while Row G still voids **any unlogged view** (draft line 676).

Counterexample: render frame R1 under event E1; retain the interface framebuffer; then magnify/crop it locally without fetching store bytes. The human receives a materially new view through the sealed interface, but the draft classifies the operation as no touch and therefore gives it no fresh event. Calling this “magnification” rather than “render” does not satisfy Row G's view-level rule. G5 dissolves the fork only for re-renders that re-convey store bytes; it does not dissolve it for cached-frame transformations the text affirmatively exempts.

### F3 — HIGH — REPAIR-REQUIRED — Enumeration evidence is outside the exhaustive non-χ artifact surface

Draft §6.1 lines 586–589 and 655–661 say the non-χ artifact list is exhaustive, everything else is χ-bearing by default, and gates/referees may read only that closed list. Lines 608–610 then introduce enumeration entries, a continuation segment, signed explanation artifacts, and re-derived vocabulary revisions. None is a listed non-χ schema or permitted aggregate.

The enumeration verifier must read and resolve those objects before BS-L/opening and at later gates (lines 606–610), but under the draft's own default they are χ-bearing and unavailable to an external pre-unblinding verifier. This is not cured by calling an entry “authenticated”: authentication does not supply the absent field restrictions that make an artifact non-χ. It also leaves `explanation_ref` as an unbounded identifier and the explanation as signed free text, so the mechanism the brief asked me to smuggle through is admitted directly. Add exact authenticated non-χ schemas, bounded encodings, and a verifier-readable custody surface, or the guard cannot execute without violating the covenant.

### F4 — HIGH — REPAIR-REQUIRED — A post-BS-L `EXPLAINED` entry cannot bind its explanation

The draft correctly places post-BS-L entries in a continuation segment because BS-L has already digested and signed the checkpoint materials (§6.1 line 608). But `EXPLAINED` requires `explanation_ref` to resolve to a signed explanation artifact **in the lock-checkpoint materials** (lines 601 and 610).

Counterexample: the first one-off catch-all occurs after BS-L. Its explanation cannot be inserted into already-signed checkpoint bytes. An external explanation is dangling under the stated rule; mutating the checkpoint breaks BS-L. Thus the continuation segment does not support both declared dispositions: the only available route is to label even a one-off as `NAMED-AS-DEFECT`. Post-BS-L explanations need their own independently authenticated continuation object and trust/identity binding.

### F5 — HIGH — REPAIR-REQUIRED — The atomic build inventory omits the P8/P9 enumeration gates

Normative prose requires fresh enumeration passes at BS-7f, BS-V, and disclosure (§6.1 line 609). The sole §11 build item for `gates/enumeration_verifier.py` wires only BS-L issuance and opening (§11 lines 1329–1336); the file does not exist on disk, as the draft openly states.

An implementation satisfying §11 can append `REFUSED-UNCLASSIFIED` during/after opening and still advance through BS-7f, BS-V, and disclosure, because those hooks are absent from the implementation inventory. The current `tools/refusal_vocabulary_check.py` also accepts only the two early consultations: R08's predicate at lines 160–167 checks BS-L plus opening, not the three later gates. Each later hook and continuation-segment authentication must be explicit in §11 and independently deletion-tested.

### F6 — MEDIUM — REPAIR-REQUIRED — `(row, operation)` is splittable because `operation` has no canonical vocabulary

The recurrence mechanism says relabelling cannot split a class because labels are not in the key, but `operation` is in the key (§6.1 lines 599–602). The access-log schema supplies no closed operation vocabulary, canonicalization, or mapping from request forms to one operation token.

A caller or mediator can express the same routine read defect as `read`, `read-cutout`, and `fetch-cutout`. The computed keys `(D, read)`, `(D, read-cutout)`, and `(D, fetch-cutout)` are distinct, so each receives one `EXPLAINED` disposition and none recurs. This is a real evasion, not honest data grain, when the underlying authorized act and failure are identical. The operation field must be a bounded canonical enum derived by Row B, with semantically equivalent request forms normalized before recurrence.

### F7 — HIGH — REPAIR-REQUIRED — BS-3g does not bind the verdict-producing permutation contract

The 18-field BS-3g schema (§11 lines 1143–1147) binds the gain kernel, estimator, and verifier, but not `ref/gain_counterfactual_path.py`, nor the `stage`, `prefix`, `trial`, or `n_perm` used to produce each verdict cell. The actual referenced path exposes all four as caller inputs and defaults `n_perm` to 2,000 (`ref/gain_counterfactual_path.py` lines 120–152), then passes them directly to `v9.perm_record()`.

The draft elsewhere defines the production record at 100,000 permutations and says the production path exposes no permutation-count or stage/trial override (§3 lines 394–397; §5 lines 480–484). A BS-3g producer can therefore keep every one of the 18 receipt fields fixed while choosing a different permutation resolution or randomness address and changing the categorical verdict matrix. `draw_verdict_digest` authenticates the chosen output; it does not bind the computation that chose it. Pin the counterfactual path and exact production permutation/address contract in the schema and independently replay those exact parameters.

### F8 — HIGH — REPAIR-REQUIRED — A conforming manifest may refute only outside `gamma_bound`

The manifest rules require both endpoints, zero, at least three distinct values, maximum spacing, and `max|γ| >= gamma_bound` (§11 lines 1175–1185, 1234–1241). They never require every evaluated γ to lie inside `[-gamma_bound, +gamma_bound]`. Yet any cell differing from baseline forces `FAILED` (lines 1273–1277), and the prose says a found flip proves non-invariance under an **allowed** gradient (lines 1187–1188).

Counterexample with `gamma_bound = 1` and frozen `Δγ = 1`: the sorted manifest `[-2, -1, 0, 1, 2]` contains both required endpoints, zero, five distinct values, has maximum adjacent gap 1, and satisfies every stated coverage check. If verdicts are constant on `[-1,1]` but flip at ±2, the receipt must say `FAILED`, falsely attributing an out-of-bound perturbation to the allowed family. Require `min(γ) = -gamma_bound`, `max(γ) = +gamma_bound`, and reject every point outside that interval.

## Failed attacks / checks that held

- Subject SHA-256 held exactly at `a1deae2e44b51a7305f7eb7b3b18ab4d6ff180cfc7379c69e6fafe0304b3e89a`, verified before reading.
- `successor_ref_v9.py` held its §0 pin: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/refusal_vocabulary_check.py` held its cited digest `9586e207f20141fde3d0f87f86d23cd2c84913934c7493161cfed0efb759d2e3`; exact V70 returned 0 problems and its self-test returned 17 controls, 0 failures.
- `prereg_lint.py` returned 97 advisory legacy citations and 0 blocking findings; I did not report those advisories, per the brief.
- `prereg_counts.py` independently returned 16 class-P / 8 class-E and prose agreement.
- `prereg_trace.py --check` returned 69 transitions, 0 problems.
- `void_registry.py --self-test` returned 6 controls, 0 failures.
- The AST exception inventory closed to 112 raise nodes with the stated exception-type totals. I did not re-find the parked per-raise-versus-call-site unit defect.
- The continuation join itself held against a simple forged `(chain_position,event_digest)`: the text requires recomputation against the chain.
- The disposition schema now conditionally requires exactly one of `rederivation_digest` and `explanation_ref`; the defects above are custody/binding defects, not a missing-field re-finding.
- The gamma-bound prose now honestly names the linear-model, unbiased-estimator, and honest-σ conditions. I did not report violation of a named condition as an unpartitioned non-guarantee.
- No `TRANSFER` state remains in the live state declaration; historical mentions are explanations of its deletion.
- I did not count the parked availability-code/object-identity leak, durable pre-verdict state, VOID partition, strata/producer question, BS-3g lifecycle cycle, per-raise classification unit, Row-L signature phase, or `require_authorization` limit as new findings.

## Evidence and write scope

Content read: `gates/BRIEF_V70_REVIEW.md`; the exact V70 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/successor_ref_v9.py` at relevant paths; `ref/gain_counterfactual_path.py`; and `tools/refusal_vocabulary_check.py` plus the invoked preregistration checkers. Commands were read-only. Only this CODEX report was written; the draft and all referenced artifacts were left unchanged.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V70
VERDICT: NOT CLEAR
COUNT: 8
F1 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §0–§1 lines 15–17, 30–33; draft §6.1 lines 630, 642 | Refusal events have no touch/store effect, so G3 contradicts them and G2 does not guarantee their truth.
F2 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §0, §1 G5, §5 lines 87–90; draft §6.1 lines 649, 676 | Cached-frame magnification creates a new Row-G view while the text exempts it from a fresh touch event.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–610, 655–661 | Enumeration/continuation/explanation artifacts are absent from the exhaustive non-χ list their pre-unblinding verifier may read.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 601, 608, 610 | A post-BS-L EXPLAINED entry cannot place its signed explanation inside already sealed checkpoint materials.
F5 | HIGH | REPAIR-REQUIRED | §6.1 line 609; §11 lines 1329–1336; tools/refusal_vocabulary_check.py lines 160–167 | The build inventory and checker omit fresh BS-7f, BS-V, and disclosure enumeration hooks.
F6 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 599–602 | The recurrence key is splittable because its operation component has no canonical bounded vocabulary.
F7 | HIGH | REPAIR-REQUIRED | §3 lines 394–397; §5 lines 480–484; §11 lines 1143–1147; ref/gain_counterfactual_path.py lines 120–152 | BS-3g leaves the verdict path and its stage/trial/permutation parameters unbound.
F8 | HIGH | REPAIR-REQUIRED | §11 lines 1175–1188, 1234–1241, 1273–1277 | A conforming manifest may include out-of-bound gamma points and report a false allowed-range failure.
<!-- END FINDINGS-BLOCK -->