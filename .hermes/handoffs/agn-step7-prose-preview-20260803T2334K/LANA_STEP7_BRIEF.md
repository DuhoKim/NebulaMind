# LANA BRIEF — AGN Step 7: wording contract → prose-preview packet (campaign lane L-B)

Lane: `agn-step7-prose-preview-20260803T2334K` (write ONLY here; temps `_tmp_*`).
Campaign gate: Duho 2026-08-03 23:31 KST — "APPROVE PAPERS OVERNIGHT — LANES PER PLAN; ARTIFACTS
ONLY; HARD STOP 09:00 KST." You are Lana, the no-overclaim lane. The P0 apply gate on the board
remains HELD — you produce the PACKET the gate would act on; you land nothing anywhere.

## Inputs (read-only)

- The patched AGN map + condensation report: `.hermes/handoffs/agn-step6-map-pilot-20260803T1330Z/`
  (`AGN_STATUS_DEBATE_MAP_V1.md` post-patch, `PATCH_LOG.md` for what changed).
- Ledger ground truth + wording machinery: `docs/claim_ledger_contract_v1_agn_20260703T0830Z/`
  — `artifacts/claim_status_ledger.jsonl`, `artifacts/wording_contract_check.json`,
  `artifacts/prose_sentence_bindings_template.jsonl`, `artifacts/prose_sentence_bindings.jsonl`
  (existing bindings — study and extend, do not contradict), `CLAIM_LEDGER_CONTRACT_V1.md`.
- Roadmap § "Step 7 — Apply the wording contract" (`.hermes/plans/2026-07-01_205807-…roadmap.md`).

## Task

Produce the AGN **prose-preview packet**: reader-facing prose paragraphs for each of the 5 map
axes, where EVERY sentence carries a binding row (sentence → ledger entry IDs → modality ceiling →
wording-contract template used). Rules, absolute:
- Prose modality never exceeds ledger certainty (your law); `pending` verification status must be
  visibly disclosed in the preview exactly as the map header does.
- Every countercase the map names appears in prose (the countercase quota survives translation).
- No content beyond ledger + map; contested numbers keep their do-not-average guards.

## Deliverables (lane dir)

1. `AGN_PROSE_PREVIEW.md` — the prose, axis by axis, with inline sentence IDs.
2. `PROSE_SENTENCE_BINDINGS_STEP7.jsonl` — one row per sentence (template-conformant).
3. `WORDING_CONTRACT_CHECK_STEP7.json` — self-check results against the contract templates.
4. `LANA_STEP7_REPORT.md` — process, ambiguities (report-don't-fix), runtime; marker:
   `LANA_AGN_STEP7_COMPLETE_20260804`.

Constraints: no network, no DB, no git, lane-only writes; do not read the C41 lane, the f_esc
dirs, or the campaign ledger. Kun red-teams your packet afterward.
