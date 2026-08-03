# Hwao-PGR lane plan — Method1 / packet-gated paper-to-wiki reconciliation

Marker: GALAXY_EVOLUTION_METHOD1_P0_START_20260706T140842Z
Plan id: HWAO_PGR_LANE_PLAN_20260706T140842Z
Author lane: Hwao — Coordinator/planner (Hwao-PGR), mesh-ge-m1-packet:Mesh-m1
Safety: NO ACTIVE EXECUTION PHRASE. Docs-only planning artifact. No DB write, SQL apply/rollback, migration, trust recompute, live wiki/page_versions publish, backend/API/service restart, git operation, deploy, or cloud/API mutation is authorized by this plan.

## 1. P0 receipt status (coordinator check)

| Lane | Receipt | Status |
|---|---|---|
| Hwao | receipts/HWAO_P0_ACK_20260706T140842Z.md | present |
| Goru | receipts/GORU_P0_ACK_20260706T140842Z.md | present |
| Kun | receipts/KUN_P0_ACK_20260706T140842Z.md | present |
| Tori | receipts/TORI_P0_ACK_20260706T140842Z.md | present |
| Lana | receipts/LANA_P0_ACK_20260706T140842Z.md | **missing** — Lana acked method2/method3 only |

Visible coordination note (P0 stop condition): Method1 P0 is complete only when Lana's receipt or an explicit Lana blocker exists in this method root. This plan records the gap as the current visible blocker for closing P0. Tori (relay/verifier) should surface the Lana-PGR packet path to the Lana pane; no other lane may write Lana's receipt on her behalf.

## 2. Inputs this plan is gated on (already captured, read-only)

- Current page inventory `pgr-current-page-inventory-20260706T130610Z.{md,json,html}` (marker `GALAXY_EVOLUTION_PGR_CURRENT_PAGE_INVENTORY_20260706T130610Z`): page id 57, version 1710, health 74.6; 730 visible claim chips across 14 sections; trust counts include 526 chips in a literal `"0.5"` bucket; 30 citation traces; 3 fact-source records; watch-claim table for P1–P5 blockers.
- P1 legacy overclaim disposition spec `p1-legacy-overclaim-disposition-spec.html` (marker `GALAXY_EVOLUTION_PGR_P1_DISPOSITION_SPEC_20260706T101547Z`): targets claims 2298, 2299, 2924; status prepared_static_docs_only_no_execution.
- Method board `index.html`, `wiki-page.html`, `quintet.html`, `manifest.json` (marker `GALAXY_EVOLUTION_METHOD_DIRECTORIES_QUINTET_20260706T0928Z`).
- Manifest `next_safe_step`: "P2 2929 archival-row route-confirmation inventory/spec unless Hwao chooses another blocker."
- Inventory gate result: prose-delta remains **closed** because P1/P2 blockers are not executed/confirmed.

## 3. Lane goal

Produce a reviewed, packet-gated reconciliation package for the Galaxy Evolution page that (a) keeps the current baseline page shape, (b) marks exactly which prose moves are already safe for a reader-facing page under the existing claim/evidence/trust packets, and (c) records every unsafe or unconfirmed move as a visible caution/no-go row — all as static docs in this method workspace, with zero live-surface mutation. Final publish/execution stays behind explicit user approval (none exists; NO ACTIVE EXECUTION PHRASE).

## 4. Lane order and per-lane assignments

Sequence S1→S5; a lane starts when its input rows exist. All outputs are docs-only, written under this handoff root (working notes) or the Method1 public workspace (reader-facing artifacts, Tori-relayed).

- S1 — Tori (relay/verifier): close P0 — relay the Lana-PGR brief/packet path to the Lana pane; verify all five receipts (or an explicit Lana blocker) and record a receipt ledger `TORI_PGR_RECEIPT_LEDGER_<ts>.md` in this root. Do not steer method substance.
- S2 — Goru (mechanical validator): validate the captured inventory against the workspace artifacts — recount markers/paths/bytes, verify claim-chip and trust-count tallies, and build the no-go row list. Must explicitly disposition the off-topic citation traces seq 1–5 (gravitational-wave/mirror-star/PDS 70 titles on a galaxy-evolution page), the `"0.5"` literal trust bucket (526 chips; watch claim 2546 / P4 bug), and `debate groups returned: 0`. Output: `GORU_PGR_MECH_VALIDATION_<ts>.md`.
- S3 — Lana (science/prose reviewer): from the P1 disposition spec and watch-claim table, classify prose moves for targets 2298, 2299, 2924 (and successor claims 2942–2948) as safe-now / caution-note / no-go under the method rule "preserve only prose moves already safe for a reader-facing wiki page." Flag overclaim risk where displayed trust (e.g. 2924 consensus 0.800 with parent_replaced hazard) outruns packet evidence. Output: `LANA_PGR_PROSE_SAFETY_REVIEW_<ts>.md`. Blocked on her P0 receipt.
- S4 — Kun (reproducibility reviewer): confirm another agent could reproduce the method from briefs + workspace files alone: check that every marker, path, count, and gate decision in S2/S3 outputs traces to a file in this method's territory; list any missing links. Output: `KUN_PGR_REPRO_CHECK_<ts>.md`.
- S5 — Hwao (this lane): author the P2 blocker spec for claim 2929 archival-row route confirmation (13 retire-with-audit rows plus voted row 28060 move/merge candidate to 2942 per manifest p2_note) as the next static docs-only step, then issue the final method verdict (section 6).

Parallelism: S2 and S1 may run concurrently; S3 requires S1 (Lana receipt) and uses S2's no-go rows if available; S4 requires S2+S3; S5 requires S1–S4.

## 5. Stop conditions and hard stops

- Prose-delta to the wiki draft stays closed until P1 (2298/2299/2924) and P2 (2929) blockers are executed/confirmed — execution itself is out of scope for this plan and requires explicit user approval with an active execution phrase.
- Any lane that would need a DB/API write, trust recompute, live wiki/page_versions update, git operation, restart, or cloud mutation must stop and record a blocker file in this root instead.
- No writes outside the Method1 handoff root or Method1 public workspace; no edits to shared parent/alias files (`galaxy-evolution/index.html`, `packet-gated-paper-to-wiki-reconciliation.html`, sibling method aliases) without explicit Hwao/user coordination.
- Each lane stops after writing its assigned artifact and awaits the next packet; no lane self-extends scope.

## 6. Final method verdict criteria (Hwao, S5)

Method1 verdict is GO-for-approval-request when all hold, else HOLD with named gaps:
1. Five receipts (or explicit blockers) on file — P0 closed.
2. Goru's mechanical validation reports zero unexplained count/marker/path mismatches, and every no-go row (incl. citation seq 1–5, `"0.5"` bucket, debate-group zero) has a disposition.
3. Lana's review marks each P1-target prose move safe-now / caution / no-go with packet citations, no unresolved overclaim.
4. Kun confirms reproducibility from files+briefs alone.
5. P2 spec for 2929 exists as static docs with routes named but not executed.
The verdict artifact (`HWAO_PGR_METHOD_VERDICT_<ts>.md`) will state plainly that execution/publish remains blocked pending explicit user approval.

## 7. Current blockers

- B1 (open): Lana-PGR P0 receipt missing in this method root — owner: Lana pane via Tori relay (S1).
- No other blockers; S2 (Goru) is immediately actionable.
