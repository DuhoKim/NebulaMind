# Hwao role-split packet — Method1 / PGR — bounded draft assembly (9-H2 confirmed)

GO marker: HWAO_DIRECTOR_GO_M1_DRAFT_ASSEMBLY_20260707T004129Z
User-confirm marker: USER_CONFIRM_9H2_CONTINUE_METHODS_20260707T003920Z
Packet marker: HWAO_PGR_DRAFT_ASSEMBLY_ROLE_SPLIT_20260707T005045Z
Method markers: GALAXY_EVOLUTION_METHOD1_ULTRA_FORMAT_ROLE_SPLIT_20260707 · GALAXY_EVOLUTION_METHOD1_P0_START_20260706T140842Z
Issued by: Hwao-m1 (coordinator). Safety: NO ACTIVE EXECUTION PHRASE — docs/static only, method-local only. Publication to the live wiki is NOT authorized (separate future user gate).

## Source constants (binding, from director sequencing HWAO_DIRECTOR_9H2_CONFIRMED_SEQUENCING_20260707T004129Z)
- Base body: `docs/baseline_step9_exact_diff_packet_20260703T1306Z/current_snapshots/https_nebulamind_net_api_pages_galaxy_evolution.body` (v1709 JSON; article markdown in its `content` field). Do not cite v1710 content.
- Skeleton: `# Galaxy Evolution` + opening provenance blockquote + exact 9-H2 list in order (Overview: Galaxy Evolution as a Regulated Baryon Cycle · Dark Matter Halos & Structure Formation · Gas Supply, Star Formation & Feedback · AGN Feedback & Quenching · Environment, Morphology & Structural Growth · Chemical Enrichment & Cosmic Timing · High-Redshift & Reionization Frontier · Observational Evidence & Surveys · Synthesis & Open Tensions). The v1709 body already matches this skeleton; assembly PRESERVES structure, adds no sections.
- Chips ≤30 total; grammar `<!--claim:ID-->…<!--/claim:ID-->`; rulings binding: GO 2943/2947 (permitted, not mandated) · conditional 2942/2944/2945/2946 (explicit debated/reported framing only) · NO-GO 2298/2299/2924/2948 · zero `"0.5"`-bucket chips. Cites `<!--cite:NUMERIC-->` only, pool 30754–30760, optional. No debate-group dependence. `hero_facts` untouched. Contract: `docs/wiki_content_contract_v1.md` (no HTML tags/entities, math only in `$…$`/`$$…$$`, no `[n]` refs or bibliography sections).

## Assembly decision (Hwao, coordination-level)
The v1709 body contains exactly one NO-GO inline chip: 2924 (`parent_replaced`, displayed consensus 0.8). The single authorized reconciliation edit for A1 is: strip chip 2924 and recast its sentence to reported-framed scoped wording chip-bound to successor 2946 (T3's designated scoped correction), keeping total chips at 30. All other 29 baseline chips (2905–2923, 2925, 2926, 2929–2936) are preserved unchanged: none is on a NO-GO list, none is in the `"0.5"` bucket, and the method rule preserves already-reader-facing prose moves. No cites added (0 → 0). No other prose changes.

## Role assignments
- A1 — Lana (assemble + caution review): produce the draft at `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md` (markdown content only, extracted from the v1709 `content` field with exactly the §Assembly edit). Then write `LANA_PGR_DRAFT_CAUTION_REVIEW_20260707T005045Z.md` (method root): verb-discipline check on the edited sentence and the debated/reported baseline chips, confirmation no NO-GO chip remains, chip total, and any caution notes for Goru/Kun.
- A2 — Goru (mechanical conformance receipt): `GORU_PGR_FORMAT_CONFORMANCE_RECEIPT_<UTC>.md` with every parent-packet field: title check; blockquote check; H2 count + exact list vs binding order; claim marker count + full ID list (opens=closes, IDs match); cite marker count + numeric IDs; source/fact-source compatibility note; contract scans (entities/span/sub/sup, TeX outside math, `[n]` refs); the five safety negatives. Counts only, no prose judgment.
- A3 — Kun (rebuild check): `KUN_PGR_DRAFT_REBUILD_CHECK_<UTC>.md` — verify another agent rebuilds the identical draft from the v1709 body + this packet alone (deterministic edit), no hidden state; re-verify renderer parsing facts on the actual draft.
- A4 — Tori (receipts-last): `receipts/TORI_PGR_DRAFT_RECEIPTS_LEDGER_<UTC>.md` after A1–A3 exist; may update Method1 cockpit surfaces (manifest.json/index.html in the Method1 workspace ONLY) to status `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`.
- A5 — Hwao: final method verdict `HWAO_PGR_METHOD_VERDICT_<UTC>.md` after A1–A4.

Ordering: A1 now (this pane hosts Lana); A2/A3 next in their panes (A3 after A2 exists is preferred but not required — the rebuild is deterministic); A4 receipts-last; A5 final. Any lane hitting a missing input or forbidden action writes ROLE_TABLE_BLOCKER and stops.

## Hard rails (unchanged)
Method1 handoff root + Method1 public workspace writes only. No live wiki/page_versions, DB/SQL, trust recompute, deploy/restart, git, cloud/API/GCP/billing/account/payment/credits/OAuth/token, browser, cron, route/config, cross-method/shared-parent, or Ultra/Gemini/Antigravity action. ULTRA_NOT_NEEDED standing.
