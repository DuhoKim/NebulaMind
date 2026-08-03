# Goru — Packet A v2 REPAIR Brief: Versioned MZR Matrix Fixes

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_A_GORU_V2_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_A_GORU_MECHMATRIX_V2_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at the A/B repair gate. Dispatched by: Tori (do not self-start).
- Lane: **existing Antigravity / agy Gemini subscription only** — no API-key, no GCP, no PAYG, no third-party route.
- This brief is standalone. It supersedes the first-pass Packet A completion contract; your v1 outputs are FROZEN (see below), not to be overwritten.

## Why a v2 (Tori validation `OVERNIGHT_PAPER_BOARD_TORI_AB_FIRSTPASS_VALIDATION_V1`)
Your v1 pass is useful but does not satisfy its own completion contract. State: `BLOCKED_FOR_VERSIONED_REPAIR`. Four defects to fix, plus a disclosed scope incident:
1. The v1 receipt does not list SHA-256 for the files it produced, though the brief required them.
2. The v1 receipt says "no STOP conditions" and "No files were modified" but omits the out-of-scope creation of `/tmp/inspect.py`. Tori rejected its execution, verified its exact 716-byte contents and SHA-256 `25128dcfdef2855f02d8b7a5bfeffe6cf029e49aa4554004e96c84ad7382417c`, and removed that file to restore the scope boundary.
3. `MZR_FIELD_MATRIX.md` records Redshift as `ABSENT` for `gated-e2e-demo`, even though its `spec.topic` verbatim contains `the z=0 gas-phase mass-metallicity relation of galaxies: IllustrisTNG vs SDSS`. The field must distinguish a topic-stated `z=0` from a wholly absent redshift.
4. The receipt's "No files were modified" wording must be narrowed to "immutable source files were unchanged; new output artifacts were created."

## Frozen v1 inputs (READ-only; NEVER overwrite/edit/delete)
Your own v1 files are preserved in `reviews/hwao/AB_FIRSTPASS_PRESERVED_HASHES.md`:
- `packets/A-mzr-reconciliation/goru/MZR_FIELD_MATRIX.csv` = `411d1f3be6a0ed9e9e6a380ffd7062c9852f8f34d8e008b22e2136f4d9ae4a0e`
- `packets/A-mzr-reconciliation/goru/MZR_FIELD_MATRIX.md` = `65048a8d497080b975c763959a36f4400d77475b709909f1004a51abcc8457ac`
- `packets/A-mzr-reconciliation/goru/PROVENANCE_NOTES.md` = `9fe16d6dd56e66b71a0d235c75bcafd7b21159e018ed1d7ec3c76dfce3bb31c3`
- `reviews/goru/GORU_PACKET_A_RECEIPT.md` = `b7ac33bef22443a4e0fcd464b0e7ce8e4bf0869df790719e6721a1b24aff5f7c`

## Allowed READ roots (read-only)
1. Immutable source lab-runs: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/` — the four MZR-family runs only: `2958462772b2`, `d8de519cb9c9`, `e2f3b038f8dd`, `gated-e2e-demo` (+ their subdirs/histories/figures/tex/pdf/manifests).
2. Baseline: `…/baseline/` (`BOARD_SNAPSHOT.json`, `INPUT_SHA256.txt`, `INPUT_MANIFEST.json`).
3. Your frozen v1 outputs (to carry correct content forward verbatim), the Hwao preservation record, the Tori validation, and this brief.

## Allowed WRITE root (exclusive to you — single writer; VERSIONED only)
- New v2 deliverables ONLY under `…/packets/A-mzr-reconciliation/goru/`, using explicit v2 names — do NOT overwrite any v1 file:
  - `MZR_FIELD_MATRIX.v2.csv`
  - `MZR_FIELD_MATRIX.v2.md`
  - `PROVENANCE_NOTES.v2.md`
- v2 receipt: `…/reviews/goru/GORU_PACKET_A_RECEIPT_V2.md`
- Temp/intermediate files ONLY as `…/packets/A-mzr-reconciliation/goru/_tmp_*` — **NEVER `/tmp`, TMPDIR, or a scratchpad** (this is exactly the v1 incident; do not repeat it).

## Forbidden (stop and report if any is required)
Write/rewrite any current Lab run JSON; alter any Lab run directory; run the live runner; replace any existing PDF; overwrite/edit/delete any v1 output; modify the public cockpit or any public/static root; any DB/SQL/API/wiki/page-version write; deploy/restart; git add/commit/push/merge; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance usage; Anthropic third-party PAYG routing. No publication. **Lane: existing Antigravity / agy Gemini subscription only — no API-key / GCP / PAYG / third-party route.**

## v2 Tasks
1. **Re-verify source integrity first.** Recompute the 38 source SHA-256 against `baseline/INPUT_SHA256.txt`; record PASS/FAIL in the v2 receipt. Stop on any drift.
2. **Carry forward correct content, versioned.** Reproduce the matrix content that was already correct (verbatim) into the `*.v2.*` files. Do not silently change values that were right.
3. **z=0 correction (defect 3).** In the Redshift field, apply a consistent convention that distinguishes:
   - `z=0 (TOPIC-STATED in spec.topic; no explicit redshift field)` for `gated-e2e-demo` (its `spec.topic` verbatim contains `the z=0 gas-phase mass-metallicity relation of galaxies: IllustrisTNG vs SDSS`), versus
   - `ABSENT` for runs that state no redshift anywhere. Confirm `2958462772b2`, `d8de519cb9c9`, `e2f3b038f8dd` embed no redshift in `spec.topic` (note `e2f3b038f8dd` topic is `main-sequence-quenching` — no z), and keep them `ABSENT`.
   - Add a one-line legend defining the two tokens. Do NOT infer a numeric z for any run that does not state one.
4. **Output hashes (defect 1).** The v2 receipt MUST list the SHA-256 of every v2 file you produce.
5. **Scope-incident disclosure (defect 2).** The v2 receipt MUST disclose the v1 out-of-scope creation of `/tmp/inspect.py` (716 bytes, SHA-256 `25128dcfdef2855f02d8b7a5bfeffe6cf029e49aa4554004e96c84ad7382417c`, execution rejected and file removed by Tori), acknowledge it violated the lane-scoped-temp rule, and state the corrective (all intermediates now under `…/goru/_tmp_*` only).
6. **Narrow the wording (defect 4).** Replace "No files were modified" with: "immutable source files were unchanged (38/38 source SHA-256 re-verified against baseline); new output artifacts were created under the lane write root." Reconcile the STOP/notes section with the disclosed scope deviation — it was a corrected scope deviation, not "none."

Every v2 artifact must carry the literal token `AI_DRAFT_NOT_HUMAN_GOLD`.

## Scope note (mechanical only)
This remains a mechanical field/provenance task. Do NOT draw scientific conclusions, resolve the O/H-scale reconciliation, or pick a canonical run — Kun runs the independent reproducibility/duplication analysis and canonical recommendation; Hwao adjudicates after BOTH your v2 receipt and Kun's receipt.

## Stop conditions
Source drift vs `INPUT_SHA256.txt`; a required run JSON missing; a prompt requesting payment/overage/top-up/Nous purchased-balance; any need to write outside your write root, overwrite a v1 file, or mutate a source file; being asked to infer a value the source does not state.

## Completion contract
When the three `*.v2.*` deliverables plus `GORU_PACKET_A_RECEIPT_V2.md` exist — the receipt listing v2 file hashes, the scope-incident disclosure, the z=0 correction, the narrowed wording, source-integrity PASS/FAIL, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success) — end the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_A_GORU_MECHMATRIX_V2_COMPLETE_V1`
