# BS-2a CODE GATE — CODEX, round 2

Verdict: **NOT CLEAR**. The pinned subject digest matches, the real acquisition reproduces 49,211 of 65,060, and deletion of the parent-digest, retained-count, and duplicate-key checks makes the rebuilt battery name the corresponding silent control and exit 1. However, the verifier still accepts χ inside the nested thresholds object, accepts evidence for a forged parent member while claiming the frozen parent source, and accepts non-integer count fields. More directly against the round-2 repair standard, deleting any of three closure checks leaves `--self-test` green because the parent-identity and joined-count controls match overlapping refusal text from surviving checks.

## Identity and executed comparison

- Subject: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `d7da1568dc294595640b603368135df288ac4bbc0cc54003a1fc906e237e650c`.
- Independently computed sha256 before testing: `d7da1568dc294595640b603368135df288ac4bbc0cc54003a1fc906e237e650c`.
- Independently recomputed sha256 after all probes: `d7da1568dc294595640b603368135df288ac4bbc0cc54003a1fc906e237e650c`.
- Comparison: **MATCH** — the reviewed bytes are exactly the brief-pinned subject at the sha256 identity level.
- `python3 ref/bs2a_quality_gate.py --self-test` exited 0 and printed `17 controls, 0 failure(s)`.
- `python3 ref/bs2a_quality_gate.py --acquire acquire` exited 0 and independently printed `n_parent=65060`, `n_joined=65060`, `n_retained=49211`, `n_excluded=15849`, evidence sha256 `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca`, and `retained 49,211 of 65,060 (expected 49,211) — MATCH`.

## Numbered findings

### 1. HIGH — the closed receipt schema still accepts χ in a nested receipt field

- File/lines: `../ref/bs2a_quality_gate.py:66-78, 220-241`.
- Executed attack: from `_sample_evidence()`, set `receipt["thresholds"]["chi_net"] = 0.731` and call `verify_receipt(receipt, evidence)`.
- Observed verifier output: `[]` — **ACCEPTED**.
- Why it fails: outer receipt keys are closed, but `thresholds` is not. The verifier asks only whether the three required threshold names have their expected values; it neither type-checks the nested object nor rejects extra names. A receipt can therefore carry χ while satisfying the claimed schema. None of the seventeen controls exercises a nested extra receipt field.
- Smallest sufficient repair: require `type(thresholds) is dict` and exact key equality with `{flux_ivar_r_gt, psfsize_r_lt, nobs_r_ge}` before value comparisons; add an isolated nested-extra/χ control with a distinct refusal code or exact reason.

### 2. HIGH — frozen parent cardinality is checked, but frozen parent membership is not authenticated

- File/lines: `../ref/bs2a_quality_gate.py:283-304`, especially the cardinality and duplicate-key checks at `285-300`.
- Executed attack: start from the clean 65,060-row fixture, replace the first evidence key with `brickid="FORGED_PARENT_MEMBER_NOT_IN_SOURCE"`, leave all counts unchanged, honestly recompute `evidence_sha256`, and call the verifier.
- Observed verifier output: `[]` — **ACCEPTED**.
- Why it fails: `parent_source_sha256` is only a self-asserted receipt literal checked against a constant. The verifier never consumes the authenticated parent bytes or an independently frozen digest of the parent key set. `n_parent == 65,060`, evidence length 65,060, and key uniqueness establish cardinality, not set equality. Thus evidence for one wrong object can claim the frozen parent source and pass. The seventeen controls cover duplicates and totals but miss wrong unique membership.
- Fixture consequence: the full-size fixture does use the same `verify_receipt()` path with no weakened test branch, which held. But it is synthetic, uses invented keys, and does not pass through `verified_bytes()`/`build_evidence()`. That difference matters precisely because the verifier accepts a false parent membership independently of the builder.
- Smallest sufficient repair: bind an independently frozen canonical parent-key-set digest and compare it with a canonical digest of the evidence keys, or make standalone verification consume the authenticated parent bytes and enforce exact key-set equality. Add an isolated unique-key-substitution control.

### 3. HIGH — three deleted closure checks remain invisible because controls match surviving reasons

- File/lines: controls and match logic at `../ref/bs2a_quality_gate.py:376-395, 457-499`; closure checks at `285-300`.
- Executed control-isolation audit on the unmodified subject:
  - `parent identity wrong` emitted two reasons, and its required substring `n_parent` matched both the intended parent-identity reason and the unrelated join-totality reason.
  - `joined count wrong` emitted two reasons, and its required substring `n_joined` matched both the join-totality reason and the evidence-length reason.
  - `non-boolean quality_pass` also emitted two reasons (non-boolean and retained-count mismatch), so not every control is isolated even where the expected substring remains unique.
- Executed deletion probes on temporary copies only:
  1. Delete only `if receipt["n_parent"] != PARENT_ROWS`: self-test still exited 0 with `17 controls, 0 failure(s)`; `parent identity wrong` was reported OK from `n_joined 65060 != n_parent 65059`.
  2. Delete only `n_joined != n_parent`: self-test still exited 0 with `17 controls, 0 failure(s)`; `joined count wrong` was reported OK from `n_joined 65061 but evidence holds 65060`.
  3. Delete only `n_joined != len(evidence)`: self-test still exited 0 with `17 controls, 0 failure(s)`; `joined count wrong` was reported OK from the surviving totality branch.
- Why it fails: the battery now checks a substring, but broad field-name substrings are not check identities. Surviving guards still mask deleted guards, reproducing the round-1 defect for three newly added closure checks.
- Smallest sufficient repair: give every refusal branch a unique stable code and have each control require that code; construct each mutator so it triggers exactly one refusal. At minimum split parent-identity, join-totality, and evidence-length controls rather than using `n_parent`/`n_joined` as shared substrings, and assert `len(out) == 1` for isolated controls.

### 4. MEDIUM — receipt count fields accept non-integer numeric types

- File/lines: `../ref/bs2a_quality_gate.py:285-302`.
- Executed attack: convert all four count fields (`n_parent`, `n_joined`, `n_retained`, `n_excluded`) from integers to equal-valued floats and verify the otherwise clean fixture.
- Observed verifier output: `[]` — **ACCEPTED**.
- Why it fails: equality and arithmetic validate numerical equality but not count type. An authenticated count contract should not accept `65060.0` as an exact row-count field merely because Python compares it equal to `65060`; the current schema has no scalar type enforcement, and none of the seventeen controls tests it.
- Smallest sufficient repair: require `type(value) is int` and `value >= 0` for every count field before arithmetic; add one isolated wrong-type control (including a boolean case, because `bool` subclasses `int`).

## Deletion-probe calibration that held

All mutations below were made only to auto-removed temporary copies under the assigned `gates` directory; the pinned subject was never edited.

- Deleting the parent-source digest comparison produced `FAIL parent digest wrong: ACCEPTED, control is silent`, `17 controls, 1 failure(s)`, exit 1. This confirms the rebuilt battery names that specific silent control exactly as required.
- Deleting the retained-count recomputation produced `FAIL retained count inflated: ACCEPTED, control is silent`, `17 controls, 1 failure(s)`, exit 1. The earlier partition-sum masking defect is repaired for this control.
- Deleting duplicate-key rejection produced `FAIL duplicate evidence key: ACCEPTED, control is silent`, `17 controls, 1 failure(s)`, exit 1.
- These successful calibrations do not cure finding 3: parent identity, join totality, and evidence length still mask one another.

## Other failed attacks and claim-boundary review

- The clean full-size fixture takes the production `verify_receipt()` function directly; there is no self-test flag or weakened verifier branch.
- Threshold mutation, schema version, both source digests, join-key declaration, retained recomputation, partition sum, evidence digest, outer receipt extra/missing fields, late-row off-schema evidence, per-row predicate disagreement, non-boolean predicate value, non-finite quality value, and duplicate evidence key all produced their named expected refusal on the intact subject.
- The source consistently limits its claim to outcome-blindness with respect to this study's unobserved χ and explicitly disclaims statistical independence from handedness and conditional independence given position (`lines 21-32`). I found no executable path or comment making the stronger claim.
- `successor_ref_v9.py` was neither imported nor opened by the subject; its only subject reference is explanatory text at line 6. Its independently checked sha256 before and after review was `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, and scoped `git status` showed no change to it.

## Testimony and constraints

None. Every verdict-bearing assertion above was executed or directly grounded in the pinned source lines. I did not read `/Users/duhokim/NebulaMindData/`, did not fetch an image byte, did not emit an acquisition artifact, and did not modify either reviewed source file. This review does not fill BS-2a, authorise a fetch, or resolve conditional independence. BS-2a remains UNFILLED; one of fifteen class-P slots is filled; BS-6 and the first image byte remain blocked.

**NOT CLEAR**