# GPT56 — V70 whole-document adversarial review

**VERDICT: NOT CLEAR.** The pinned subject digest matches, and the mechanical lint/count/trace/registry checks are green, but the new lifecycle specification is internally inconsistent for refusal commits; the continuation-enumeration design has an impossible disposition binding and incomplete downstream wiring; and the BS-3g stochastic baseline rule does not test invariance at the draw grain it defines. The refusal checker also does not enforce the textual properties the draft credits it with.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — Refusal commits fall outside G2 and directly contradict G3

`LIFECYCLE_GUARANTEE_SPEC.md` defines a refusal commit as `{event, binding}` with **no store effect** (§0, lines 15–17). But G2 says only that an event is true “of the store effect it records,” and G3 says both “one event per touch” **and** “one touch per event” (§1, lines 30–33). A refusal event has no store effect and no touch by definition. Therefore:

1. G3 is false for every refusal commit: the refusal has one event and zero touches.
2. G2 supplies no truth condition for the refusal outcome/reason, because there is no store effect of which it can be true.

Concrete counterexample: Row B commits one event saying `REFUSED-SCHEMA-NONCONFORMING` for a conforming write and binds the request, with no store effect. G1 holds (no touch), G4 holds (one event), N1 and N2 do not apply, while G2 is undefined/vacuous and G3’s reciprocal direction is violated. This is exactly a failure that lands in no G/N cell. The draft repeats the same construction at §6.1 lines 630–642 and claims every request gets one terminal treatment, so the defect is not confined to explanatory prose. Repair requires a refusal-specific truth invariant and either limiting G3’s reciprocal to touch events or defining a refusal as a distinct event class outside the touch bijection.

### F2 — HIGH — REPAIR-REQUIRED — Post-BS-L `EXPLAINED` entries cannot satisfy their own binding

The draft correctly says post-`BS-L` enumeration entries live in an authenticated continuation segment **outside** the sealed checkpoint materials (§6.1 line 608). But the entry schema requires every `EXPLAINED` entry’s `explanation_ref` to resolve to a signed explanation artifact **in the lock-checkpoint materials** (§6.1 lines 601 and 610). Those materials were already sealed by `BS-L` and cannot gain a postdating explanation.

Counterexample: the first catch-all emission occurs after `BS-L` and is a non-recurring, explainable one-off. Its continuation entry cannot point to a newly written explanation inside the already sealed checkpoint materials. A dangling external explanation must be refused by the stated verifier; placing it inside the checkpoint would require changing signed checkpoint bytes after `BS-L`. The only surviving disposition is to misclassify the emission as `NAMED-AS-DEFECT` and re-derive the vocabulary, even though the schema explicitly permits `EXPLAINED`. The continuation segment therefore does not carry both promised dispositions. Specify an independently authenticated post-`BS-L` explanation/re-derivation object and a verifier rule that resolves it without mutating or pretending to extend the checkpoint.

### F3 — HIGH — REPAIR-REQUIRED — The build inventory wires only two verifier consultations, so P8/P9 catch-alls can pass

The normative prose says fresh enumeration-verifier passes are required at the opening, `BS-7f`, `BS-V`, and disclosure (§6.1 line 609). The sole §11 implementation item says the verifier is consulted only at `BS-L` issuance and at opening (§11 lines 1329–1336). It does not require the fresh `BS-7f`, `BS-V`, or disclosure consultations, nor does it specify continuation-segment authentication.

This is an executable gap in the design inventory: append `REFUSED-UNCLASSIFIED` during unsealing immediately after the opening pass. The implemented item described by §11 can still issue `BS-7f`, `BS-V`, and disclose because none of those gates is wired to a fresh pass. The prose sentence at line 609 is therefore a wish not carried into the atomic build contract. The same omission is invisible to `tools/refusal_vocabulary_check.py`: R08 explicitly accepts a draft when it finds only the two consultations at `BS-L` and opening (checker lines 160–167). Add all three later gate hooks and continuation verification to §11 and to controls that delete each hook independently.

### F4 — MEDIUM — REPAIR-REQUIRED — The refusal checker can be defeated by formatting or by a contradictory clause

The draft says `tools/refusal_vocabulary_check.py` “enforces the eleven-code set and the catch-all guard” (§6.1 line 618). It does not. R01 extracts only backtick-delimited tokens with ``re.findall(r"`(REFUSED-[A-Z-]+)`", text)`` (checker line 115), while the principle checks are positive phrase searches (lines 139–143). I imported the checker against the exact V70 bytes and tested two in-memory mutations, writing no file:

- append `Active refusal member: REFUSED-EVADE.` without backticks;
- append `A refusal reason may describe the OBJECT.` while retaining the earlier prohibition.

`check()` returned `[]` for both. Thus a twelfth active code can evade R01 by Markdown formatting, and an explicit contradiction of the governing principle can coexist with the phrase that makes R03 pass. This is not hypothetical formatting independence: the draft deliberately leaves the retired `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` unformatted so the checker will not count it (§6.1 line 614). Scope the parser to the normative vocabulary block and parse semantic members independently of Markdown decoration; add negative controls for a bare twelfth member and a later contradiction.

### F5 — HIGH — REPAIR-REQUIRED — A scalar `baseline_verdict` confounds draw noise with gradient sensitivity

The BS-3g mapping redraws signs for each draw, making the evaluation a draw × perturbation matrix (§11 lines 1268–1272). Yet the receipt carries one scalar `baseline_verdict`, recomputed from the entire γ=0 column (§11 lines 1232–1237), and declares `HELD` iff **every matrix cell** equals that scalar (§11 lines 1273–1277).

A γ=0 column has `n_draws` stochastic verdicts, not necessarily one verdict. Construct two draws over a three-point manifest:

- draw 1: `[A, A, A]`;
- draw 2: `[B, B, B]`, with `A != B`.

Each draw is perfectly invariant across γ: the perturbation changes no verdict. Nevertheless no scalar `baseline_verdict` makes every cell equal, so the specified rule returns `FAILED` (or leaves scalar baseline recomputation undefined). It is testing equality across exchangeable draws as well as invariance across perturbations. The natural grain is row-wise: recompute the γ=0 verdict for each draw and compare that draw’s nonzero-γ cells against its own baseline, then reduce across draws. If the intended baseline is instead the single observed production verdict, the text must stop claiming it is recomputed from a stochastic γ=0 column.

## Failed attacks / checks that held

- Subject identity held: SHA-256 recomputed as `a1deae2e44b51a7305f7eb7b3b18ab4d6ff180cfc7379c69e6fafe0304b3e89a` before the draft was read.
- `successor_ref_v9.py` held its §0 pin: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/refusal_vocabulary_check.py` held its cited digest: `9586e207f20141fde3d0f87f86d23cd2c84913934c7493161cfed0efb759d2e3`.
- The unmodified V70 refusal check returned 0 problems; its self-test returned 17 controls, 0 failures.
- `prereg_lint.py` returned 97 advisory legacy citations and 0 blocking findings, as the brief states.
- `prereg_counts.py` independently parsed 16 class-P and 8 class-E rows; the prose matches.
- `prereg_trace.py --check` recomputed 69 transitions with 0 problems.
- `void_registry.py` parsed 54 antecedents and 20 §6.1 rows and emitted registry digest `d111d95d023ebd3b639f3efd9f0ec6c33ad33f1cee551b5428292e24f9848403`.
- The raised-site ledger’s body closes to 112 nodes and its current header counts close to 112 (25 CALLER + 60 INTEGRITY + 20 NUMERICAL + 3 PLANNING-INTERNAL + 1 TYPED-OUTCOME + 3 WRAPPER). I did not re-find the parked per-raise-versus-call-site unit defect.
- I did not count the parked availability-code/object-identity leak, durable pre-verdict state, VOID partition, strata producer, BS-3g lifecycle cycle, or `require_authorization` weakness as new findings.

## Evidence and scope

Files read as content: `gates/BRIEF_V70_REVIEW.md`; the exact V70 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `tools/refusal_vocabulary_check.py`; and the relevant checker entry points. Commands were read-only except for writing this report. No draft, spec, reference implementation, checker, ledger, or other gate file was modified.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V70
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §0–§1 lines 15–17, 30–33; draft §6.1 lines 630–642 | Refusal events have no touch/store effect, so G3 contradicts them and G2 does not guarantee their truth.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 601, 608, 610 | A post-BS-L EXPLAINED entry cannot place its signed explanation inside already sealed checkpoint materials.
F3 | HIGH | REPAIR-REQUIRED | §6.1 line 609; §11 lines 1329–1336 | The implementation inventory omits fresh BS-7f, BS-V, and disclosure enumeration passes.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 line 618; tools/refusal_vocabulary_check.py lines 115–143 | The claimed eleven-code/principle enforcement is evadable by formatting and survives an explicit contradiction.
F5 | HIGH | REPAIR-REQUIRED | §11 lines 1232–1237, 1268–1277 | One scalar gamma-zero baseline confounds stochastic draw variation with perturbation sensitivity.
<!-- END FINDINGS-BLOCK -->
