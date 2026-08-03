# Method2 / SFA role-split packet — Ultra usage scrutiny + same-format wiki output gate

Marker: GALAXY_EVOLUTION_METHOD2_ULTRA_FORMAT_ROLE_SPLIT_20260707
Parent marker: ULTRA_USAGE_AND_WIKI_FORMAT_ROLE_TABLE_PACKET_20260707
Issued by: Hwao (Hwao-SFA, coordinator/planner) — as required by parent packet ("Hwao must issue a role-split packet before any method continues").

Method: Method2 / SFA / source-first paper adjudication
Handoff root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2
Public workspace: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication

## User direction being executed
1. Scrutinize Ultra usage — Ultra/Antigravity/Gemini is supervised second-opinion capacity only, never autonomous rewriting, never used just because quota exists.
2. The final Method2 Galaxy Evolution wiki output must match the current live NebulaMind page format (Markdown article, page 57 / `galaxy-evolution`, version 1710 contract), not a custom method-card layout.
3. No solo execution — every step below is role-split per the role table.

## Ultra usage position for Method2 (scrutiny result)
- Default: NO Ultra/Antigravity/Gemini use in Method2.
- Ultra may be used only if Lana or Hwao names one exact contested question on a specific Method2 artifact (e.g., a disputed source-position adjudication), and only via a separate Hwao role packet authorizing exactly one bounded, marker-bearing supervised review — then stop.
- If ever authorized: Goru records visible non-secret quota before/after; Kun reconciles the output against local repo/source facts; Tori records the receipt and rejects anything not traceable to local artifacts.
- `/usage (quota)` read-only is safe; `/credits` must never be opened without explicit user approval.
- Hard stops (all lanes): no API key/GCP/Vertex/billing/payment/credits/account/OAuth handling, no browser automation, no cron, no DB/SQL, no publish/deploy/restart, no git, no route/config mutation.

## Format contract (all lanes verify against this)
- Final Method2 output core = Markdown article: title `# Galaxy Evolution`; opening blockquote explaining sparse provenance claim chips; the exact 9-H2 skeleton from the parent packet (Overview: Regulated Baryon Cycle → Dark Matter Halos → Gas Supply/SF/Feedback → AGN Feedback & Quenching → Environment/Morphology → Chemical Enrichment → High-Redshift/Reionization → Observational Evidence & Surveys → Synthesis & Open Tensions) unless Hwao records a written method-level exception.
- Claim chips `<!--claim:ID-->…<!--/claim:ID-->` sparse and meaningful; citations `<!--cite:EVIDENCE_ID-->`; no `hero_facts`; renderer-compatible with `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`.
- Existing `wiki-page.html` in our public workspace is a static workspace only, NOT the final output.

## Role assignments and deliverables (sequence S1 → S5)
- S1 — Hwao (this lane): source-position ledger skeleton + target-paper list + sequencing, at `hwao/SOURCE_POSITION_LEDGER_PLAN_20260707.md` under the handoff root. Method rule holds: papers first; no claims/prose until source roles are accepted or accepted-limited.
- S2 — Lana: adjudicate each proposed source position (accepted / accepted-limited / rejected) with science-caution review; flag overclaim/prose-drift risk; name any single contested question that would genuinely need an Ultra second opinion. Deliverable: `lana/LANA_SFA_SOURCE_ADJUDICATION_20260707.md`.
- S3 — Goru: mechanical validation — count papers, positions, adjudication verdicts, and (once a same-format draft exists) title/blockquote/H2 list, claim-marker count+IDs, cite-marker count+evidence IDs vs the contract. Deliverable: `goru/GORU_SFA_FORMAT_COUNTS_20260707.md`.
- S4 — Kun: reproducibility — verify another agent can rebuild the ledger and the same-format draft from packet + artifacts alone, no hidden web/app state. Deliverable: `kun/KUN_SFA_REBUILD_CHECK_20260707.md`.
- S5 — Tori: record lane receipts under `receipts/`, verify files exist and carry markers, relay blockers; no live wiki writes. Deliverable: `receipts/TORI_SFA_S5_RECEIPT_20260707.md` plus per-lane receipt verification lines.
- Same-format Markdown draft conversion happens only AFTER S2 acceptance, as a subsequent Hwao-sequenced packet, and must ship with the format-conformance receipt required by the parent packet.

## Stop conditions
- Each lane stops after its own deliverable + receipt; no lane advances another lane's step.
- Any missing partner or missing evidence → write `ROLE_TABLE_BLOCKER` in a receipt under `receipts/` and stop.
- No commit/push/merge, deploy/publish, live wiki/page_versions, DB/SQL, trust recompute, restart, cloud/API/billing mutation, or cross-method/shared-parent edits.

Safety state: NO ACTIVE EXECUTION PHRASE — relay, analysis, and docs/static receipts only.
