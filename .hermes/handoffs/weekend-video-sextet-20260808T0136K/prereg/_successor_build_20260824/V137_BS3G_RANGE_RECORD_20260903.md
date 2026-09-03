# V137-H BS-3g range record — 2026-09-03

V137-H re-drafts the existing V137 draft in place from signed, read-only V136.
It changes the preamble, §1 status, §7 BS-3g row, §11 BS-3g range/build text,
generated sidecars, and blank signature lines. §10 contains only the generated
V135 → V136 predecessor row. No pixel or network was used; no signed or pinned
input was edited.

## Ruling and design parameter

Duho ruled option (a) via Blanc at 16:52 KST (direction #66), then re-ratified
option (ii) via Blanc, verbatim "as their recs", at 19:37 KST (direction #69):
BS-3g DESIGN accuracy a₀ = 0.95 and Γ = 0.10, with nothing else changed.
At `n_steps = 50`, Δγ is derived as `2Γ/n_steps = 0.004`; seed 20260830,
99 draws, CRN, mapping A worst case, and option (b) remain fixed.

`gates/bs3g_headroom_experiment/HEADROOM_RESULTS_20260903.md` records the
0.95 fixture's measured calibration-admissible edge as 0.12 (analytic
0.121181392), ratio 2.505127, and σ_γ 0.047901763.
`BS3G_HEADROOM_MEMO_20260903.md` recommends Γ = 0.10 within that edge. The
unpinned producer applies the experiment's disclosed +0.07 accuracy-location
shift while the P0-signed `ref/gain_counterfactual_path.py::_fixture` remains
byte-untouched at `92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7`.

## Receipts and truthful outcome

- Retained 0.88 record: `run/classp_candidates/BS-3g.FAILED-0p88-20260903.json`,
  sha256 `a8277a193caffa826ac3a1c2884545f0112b64e7cd3f6a6556dcc996041e49ba`.
- Fresh producer run 1: `19ffcbab574a8663e248b4d837be9734e48843e8c9ab8ea59489ef2558cf5818`.
- Fresh producer run 2: `19ffcbab574a8663e248b4d837be9734e48843e8c9ab8ea59489ef2558cf5818`.
- `cmp`: byte-identical; deterministic yes.
- Fresh candidate: `run/classp_candidates/BS-3g.json`, same sha256.
- Result: `invariance_outcome = FAILED`; 0/5,049 calibration-inconclusive
  cells; minimum `a_lb_b = 0.8639832635983262`; γ̂ =
  `-1.3752885039820904e-18`; σ_γ = `0.04790176316993866`.
- Counterexample: draw 94 (zero-based), γ = −0.10 is `REPRODUCED-LONGO`
  while that draw's γ = 0 baseline is `INCONCLUSIVE`.

The memo correctly forecast floor headroom but did not forecast the worst-case
decision result. Under the pre-stated §7 acceptance rule, only `HELD` fills
BS-3g. Therefore the verifier-valid `FAILED` result is a true blocking record,
and the slot remains UNFILLED. The control tests decision invariance to a
sensitivity tilt up to about 2σ_γ on a synthetic sky of accuracy 0.95; the real
instrument's floor headroom is what the retained FAILED receipt documents.

## Tooling and schema pins

```text
48b2cc6607b91b1e746c2ee7cb21c9b624fb247be5aee3922fb3572351848e82  gates/bs3g_producer.py
ca6e2ea35b38bebb020b053839477306cbce97a7791de4ad76d9f524afe21454  gates/verify_bs3g_receipt.py
```

Pin sheet: `BS3G_TOOLING_PIN_V2_20260903.md`. The twenty-field BS3G-V1 entry
is unchanged at `eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102`;
a₀ is recorded in the build record and V137-H text, not added to the receipt.

## Generated predecessor coverage row

```text
| V135 → V136 | `a55fb433697bb3d9` | `90ee001ae3b08288` | §11 (+11/−10), (preamble) (+2/−2), §7 (+2/−2), §10 (+1/−0) | no row-count change | the BS-2a DESIGN fill under amendment discipline — `PRINCIPAL-20260903-1B2B`, human direction #58, verbatim "1b 2b"; quality gate `dfbd63d1…`, evidence-schema digest `9f3aca28…`, verifier digest `6e70a8ef…`, receipt_strict sha `27e88520…`, schema `BS2A-V1`, candidate receipt sha `f0d9bcce…`; design identities only, no catalogue rows evaluated. |
```

## Verification and sidecars

```text
BS-3g receipt verifier: 20/20 fields PASS; outcome FAILED
prereg trace check: 136 computed transitions; 0 problems
prereg lint: 97 findings; 0 blocking (97 advisory)
prereg counts: 16 class P, 9 class E; 23 rows carry a BS- identifier
string-field registry: 315 found, 315 classified, 0 forbidden, 0 stale
receipt_strict fixtures: 10/10 PASS
BS-3g V137-H parameter tests: 12/12 PASS
```

Sidecars: `gates/FINDINGS_MAP.md` sha256
`8c8f682f3a6885962804f93dc4b9885901f97ebb308b49c4b984aa5dd1a60825`;
`ref/STRING_FIELD_REGISTRY.md` sha256
`90733d899a124ea347aa12149d544b152a11c45b3cf5d9bc948599e581f3d7f2`.

V136 → V137 hunk headers:

```text
@@ -1 +1 @@
@@ -3 +3,3 @@
@@ -122 +124 @@
@@ -939 +941 @@
@@ -1161,0 +1164 @@
@@ -1248,0 +1252 @@
@@ -1280 +1284 @@
@@ -1337 +1341 @@
@@ -1347 +1351 @@
@@ -1371 +1375 @@
@@ -1373 +1377 @@
@@ -1615,2 +1619,2 @@
```

The digest below is SHA-256 of V137-H with both signature lines blank, as the
draft bytes stand.

SEAT: CODEX
VERSION: SUCCESSOR-DRAFT-V137-H + BS3G-BUILD-V3
RECEIPT: 19ffcbab574a8663 DETERMINISTIC: yes
INVARIANCE_OUTCOME: FAILED INCONCLUSIVE_CELLS: 0/5049 MIN_A_LB: 0.8639832635983262 SIGMA_GAMMA: 0.04790176316993866
TRACE_CHECK: PASS
DIGEST: 76e15005585d84ebab98ba792892e48152e7ff21233da449d5c69c9a25dd097f
