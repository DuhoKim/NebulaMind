# V137 BS-3g range record — 2026-09-03

V137 copies signed V136 and changes only the preamble amendment paragraph, the §7 BS-3g row, the §10 predecessor-coverage row, the §11 BS-3g range/build language, the two generated sidecars, and the blank signature lines. V134, V135, V136, `ref/DRAW_MECHANICS_COMMIT_20260830.md`, and every P0-manifest member remain byte-unchanged. No pixel was opened.

## Ruling applied

Duho ruled option (a) via Blanc at 2026-09-03 16:52 KST, human direction #66: Γ is re-ratified at 0.01, `n_steps = 50`, and everything else is unchanged. Under Amendment 2 of `ref/DRAW_MECHANICS_COMMIT_20260830.md`, Δγ is derived as `2Γ/n_steps = 0.0004`; the amendment requires a new commitment only for asymmetric endpoints, so the symmetric re-ratification does not trigger that stop.

The historical `GAMMA_RATIFICATION_20260830.md` citation remains. V137 adds: “Γ re-ratified at 0.01 by the principal's ruling (a) of 2026-09-03 16:52 KST on the FAILED BS-3g receipt a8277a19…, evidence that ±0.25 was never compatible with the 0.85 floor on the frozen fixtures”.

## Receipt and tooling status

- True blocking record: `run/classp_candidates/BS-3g.json`, sha256 `a8277a193caffa826ac3a1c2884545f0112b64e7cd3f6a6556dcc996041e49ba`, verifier-valid `FAILED` under the historical Γ = 0.25.
- Producer: `gates/bs3g_producer.py`, sha256 `618767cd41e5283bdf736e30249ce2f0bdb180b4f0257e58e690bea58d3a18e6`.
- Independent verifier: `gates/verify_bs3g_receipt.py`, sha256 `09b0acaadca1d95c756ad974ed48de28a4a1bbbf5f5fb765e7d7f042ea87dd64`.
- V137 status: **FILL-PENDING-RECEIPT**. A new verifier-valid receipt under Γ = 0.01 must be produced; only `invariance_outcome = HELD` fills BS-3g and discharges BS-6.

## Sidecars

- `gates/FINDINGS_MAP.md`: V136 → V137 entry added for ruling (a), direction #66; sha256 `8dd0975f81687dc18e43841fa0bbb7870cac001186ca1827d37e0bcc013bfdd6`.
- `ref/STRING_FIELD_REGISTRY.md`: regenerated from V137; 315 fields found, 315 classified, 0 forbidden-by-default, 0 stale; sha256 `90733d899a124ea347aa12149d544b152a11c45b3cf5d9bc948599e581f3d7f2`.

Both sidecars are outside `P0_PACKAGE_MANIFEST_20260831.txt`.

## Generated predecessor coverage row

```text
| V135 → V136 | `a55fb433697bb3d9` | `90ee001ae3b08288` | §11 (+11/−10), (preamble) (+2/−2), §7 (+2/−2), §10 (+1/−0) | no row-count change | the BS-2a DESIGN fill under amendment discipline — `PRINCIPAL-20260903-1B2B`, human direction #58, verbatim "1b 2b"; quality gate `dfbd63d1…`, evidence-schema digest `9f3aca28…`, verifier digest `6e70a8ef…`, receipt_strict sha `27e88520…`, schema `BS2A-V1`, candidate receipt sha `f0d9bcce…`; design identities only, no catalogue rows evaluated. |
```

## Verification

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V137_20260903.md
  136 computed transition(s); 0 problem(s)

prereg lint — PREREG_SUCCESSOR_DRAFT_V137_20260903.md
  §7 data rows: 25 (16 class P, 9 class E) — 23 carry a BS- identifier
  97 finding(s), 0 blocking (97 advisory)

prereg counts — PREREG_SUCCESSOR_DRAFT_V137_20260903.md
  computed from the table: 16 class P, 9 class E (23 rows carry a BS- identifier)
  prose says filled: BS-2m  (not computed — a claim about receipts, not rows)
  prose already matches the table

P0 manifest: 30/30 OK
```

## Diff hunk headers V136 → V137

```text
@@ -1 +1 @@
@@ -3 +3 @@
@@ -939 +939 @@
@@ -1161,0 +1162 @@
@@ -1248,0 +1250 @@
@@ -1280 +1282 @@
@@ -1337 +1339 @@
@@ -1347 +1349 @@
@@ -1371 +1373 @@
@@ -1373 +1375 @@
@@ -1615,2 +1617,2 @@
```

Digest below is SHA-256 of `PREREG_SUCCESSOR_DRAFT_V137_20260903.md` with both signature lines blank, as committed in the draft bytes.

SEAT: CODEX
VERSION: SUCCESSOR-DRAFT-V137
HUNKS: preamble, §7, §10, §11, signature lines; sidecars FINDINGS_MAP and STRING_FIELD_REGISTRY
TRACE_CHECK: PASS
DIGEST: 9f2b48939ef3753c6c4925c4c1d3bdc878a0f516253518ebabe1a9a2d2f76a17
