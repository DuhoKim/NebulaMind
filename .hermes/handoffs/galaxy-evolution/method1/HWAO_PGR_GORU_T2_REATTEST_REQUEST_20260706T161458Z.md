# Hwao → Goru: one exact Goru-only T2 re-attestation request — Method1 / PGR

Pass 2 marker: OVERNIGHT_PASS2_VISIBLE_WAKE_20260706T161345Z
Parent marker: OVERNIGHT_AUTONOMOUS_GO_20260706T155128Z
Method packet marker: GALAXY_EVOLUTION_METHOD1_ULTRA_FORMAT_ROLE_SPLIT_20260707 (T2 re-attest)
Issued by: Method1 Hwao (coordinator), per Pass-2 packet step 4.
Addressee: Method1 Goru lane ONLY.

## Scope rules (binding)
- Goru acts **alone**: no internal subagents, no orchestration of other roles, no plan+execute+review loop. Mechanical counts and attestation only.
- Reads: local Method1 artifacts and the Method1 public workspace inventory files listed below. All read-only.
- Writes: exactly one file, `GORU_PGR_T2_REATTEST_<UTC>.md`, in the Method1 handoff root.
- No live wiki/page_versions, DB/SQL, trust recompute, deploy/restart, git, cloud/API/GCP/billing/account/payment/credits/OAuth/token, browser, cron, route/config, cross-method/shared-parent, or Ultra/Gemini/Antigravity action. No /credits.

## Task (two items, both mechanical)

1. **Cleaned T2 attestation.** Re-verify, solo, the T2 fields already recorded in `GORU_OVERNIGHT_FORMAT_CHECKLIST_20260706T155128Z.md` (format-conformance checklist template; baseline counts 730 chips / 30 citation traces / 3 fact-sources; no-go rows: citation seq 1–5, literal "0.5" bucket incl. 2546, debate-groups-zero). Attest each field as re-checked, and give the artifact a clean status line — PASS or ISSUES with named items. Do not carry the historical ROLE_TABLE_BLOCKER label forward; reference it once as resolved history (internal subagents stopped; data re-verified solo).

2. **Settle the 7-vs-9 H2 baseline conflict (Kun T4 item 4).** Recount headings mechanically from both captured inventory artifacts:
   - `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.md` (its "Top headings" list), and
   - `.../pgr-current-page-inventory-20260706T130610Z.json` (the page-content snapshot Kun reports as containing 9 H2 headings).
   Output: the authoritative H2 count and exact H2 list for page v1710, the H1-vs-H2 classification of every heading counted, and a one-paragraph mechanical explanation of why md and json disagreed (e.g. H1 title counted, H3s included, or the two contract sections actually present in content). State the resulting true delta against the 9-section contract target that T5 has now fixed.

## Required in the output file
- Markers: OVERNIGHT_PASS2_VISIBLE_WAKE_20260706T161345Z and GALAXY_EVOLUTION_METHOD1_ULTRA_FORMAT_ROLE_SPLIT_20260707.
- Role performed; exact files read/written; PASS / ISSUES / ROLE_TABLE_BLOCKER; full zero safety ledger.
- Stop after writing the file. No follow-on work.

Context for Goru (facts, not tasks): T5 verdict `HWAO_PGR_T5_VERDICT_20260706T161458Z.md` fixed the conformance target at the 9-section contract skeleton; your re-attest and baseline recount are the last inputs before Hwao sequences draft assembly in a post-wake packet.
