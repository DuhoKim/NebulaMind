# Hwao-m3 autopilot progress — evidence links + trust leveling (Method3)

Order marker: `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z`
Continuation marker: `GE_AUTOPILOT_IDLE_CONTINUATION_V1`
Role: Method3 Hwao — autonomous method controller (bounded docs/static, NO-APPLY, no product binding).

## STATUS: COMPLETE

User feedback: pages read better now but are **missing evidence links + trust leveling**. M3 baseline (Tori 01:42Z): `wiki-page.html` 9 `<h2>`, **0 hrefs, 0 trust-word hits**. → Now addressed with a docs-only static evidence+trust candidate.

### Completion outputs (this run)
- `evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md` — narrative + trust chips + evidence links
- `evidence-trust-rebuild/evidence-basis-20260708T014205Z.md` — local provenance & trust ledger (link target)
- `evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html` — static preview (raw `<h2>`=9, static-safe)
- `autopilot/GORU_M3_EVIDENCE_TRUST_CHECK_20260708T014205Z.md` — PASS
- `receipts/TORI_M3_EVIDENCE_TRUST_RECEIPT_20260708T014205Z.md` — PASS
- `HWAO_M3_EVIDENCE_TRUST_VERDICT_20260708T014205Z.md` — READY_FOR_USER_APPROVAL

### Result
Trust leveling = real debate-map axis statuses (per-section chips + page summary); evidence links = 11 clickable links to the local provenance ledger; 4 unmatched items honestly flagged; 0 product claim/cite binding (P3 stays CLOSED); static-safe (0 scripts/fetch/API/external URLs); old pages preserved. NO-APPLY — candidates are working-repo only (404 on :3000 until the separate live-root mirror gate). Method verdict issued.

## Honest M3 framing (per order §Quality + §Method3)

M3 is **docs-only P2, 0 claim / 0 cite markers by design** — it has NO product claim/citation binding, and I will NOT fake one (P3 binding stays a separate CLOSED gate). What M3 *does* have locally and can surface honestly:
- **Debate-map axis statuses** (real, from `status_debate_map.json` / `debate_map_data.json`): widely_supported / emerging_sample_limited / actively_debated / contradicted_or_model_dependent → per-section **trust leveling** (plain English).
- **Per-section local provenance** (real source/claim IDs from Lana's P2 author report §6, verified against `evidence_source_inventory.json`) → per-section **evidence-basis panels**, clearly labeled "local provenance (P2 docs-only, unbound to product cite IDs)."
- **Known unmatched items** (Kun PROV-1: claim 2133 source 2605.22497; PROV-2: claim 2374 garbled) → shown as **unbound/unmatched**, not hidden.

## Plan (author → build → Goru → Tori → Hwao verdict; NO-APPLY, additive candidate)

New order-named subdir: `debate-map-to-wiki-rebuild/evidence-trust-rebuild/`
1. Lana-role candidate: `page-content-evidence-trust-20260708T014205Z.md` (same 9-H2 content + per-section trust chips + evidence-basis references + page-level trust summary; docs-only, non-invented) and `wiki-format-preview-evidence-trust-20260708T014205Z.html` (static preview: trust summary panel + per-section trust chips + evidence-basis panels linking to local artifacts; NO scripts/fetch/API).
2. Goru-role mechanical check: hrefs, evidence-ish links, trust chips, unmatched labels, no-script/API/DB scan, files-exist/non-empty, old pages preserved → `autopilot/GORU_M3_EVIDENCE_TRUST_CHECK_20260708T014205Z.md`.
3. Tori-role receipt → `receipts/TORI_M3_EVIDENCE_TRUST_RECEIPT_20260708T014205Z.md`.
4. Hwao method verdict (READY_FOR_USER_APPROVAL / HARD_BLOCKED) → `HWAO_M3_EVIDENCE_TRUST_VERDICT_20260708T014205Z.md`.
5. Update this progress → COMPLETE.

Old wrong-format + same-format-rebuild artifacts preserved (additive only). Live root untouched. No product binding.

## Hard gates (closed)

No product DB/SQL, `/api/pages`, `page_versions`/publish, live-root writes, deploy/restart, git, cockpit/global/shared-parent, cloud/GCP/OAuth/secrets, browser, cron, Method3 P3 binding, invented evidence/cite/claim/source IDs. Read-only inspection + additive method-local static candidate + `.hermes` receipts only.
