# Lana — Step 9E guarded SQL packet methods / claim-compatibility review

Task: Step 9E Quintet review · Lane: Lana (methods / claim-compatibility reviewer) · Read-only.
Written: 2026-07-04, repo `/Users/duhokim/NebulaMind/NebulaMind`. **No SQL executed, no DB/API mutation, no apply, no git write. Never ran apply_guarded or rollback.**

## Verdict: **PASS_WITH_PATCHES**

This is the best-guarded packet of the campaign: transactional apply with comprehensive pre- and post-guards, a precisely packet-scoped reversible rollback, no evidence laundering, and every prior Lana/Quintet patch honored (per-source quality, Peng stance-restriction, non-destructive reuse). It is structurally **execution-ready**. Three managed-consequence patches must be resolved before the operator pastes `APPROVE EXECUTE` — chiefly a pre-execution check that no auto-trust-recompute trigger fires on evidence insert, and an explicit plan for the transient 2924 contradiction created by the (correct) insert-only design.

## Task answers

**1. Five inserted claim texts vs reusing old rows — the new claims are methodologically safer.** The 5 new claims carry scoped, non-universal wording with **honest trust designs** (synthesis `debated`/0.45, outflows `reported`/0.2, dominance `debated`/0.45, reservoir `debated`/0.45, heating `reported`/0.2). Reusing the old rows would carry their defects forward: 2924 is a flat `consensus` "AGN heats gas reservoirs" (an overclaim — heating is simulation-only), 2929 bundles five axes in one chip, and 2915/2917/2921/2557/2572 are duplicate-prone or scope-blurring. Fresh scoped claims avoid all of these. Safer.

**2. Insert-only (0 existing updates), 2929 preserved until a later gate — correct and non-destructive.** `existing_claim_updates_planned: 0`; the packet is purely additive (5 claims + 35 evidence + 35 links) and touches no existing claim, deferring desurface/retire/nuance and any trust recompute to a later gate. This is the safest, most reversible path. **Consequence to manage (patch):** while insert-only, the page will transiently surface the old flat 2924 ("AGN feedback heats the gas reservoirs," `consensus`) **alongside** the new "maintenance/heating remains model-dependent/simulation-bounded" claim — a visible contradiction until the deferred gate resolves 2924. The deferred visible-desurface/nuance gate must run close behind (or 2924 be desurfaced in the same visible change), or readers see contradictory heating claims.

**3. Design-stance → production-supports mapping — legitimate, not laundering.** Verified in the SQL: every counter/qualifier paper (retention: Koss/Spilker/Zhang; SF-driven: Sarzi; central: Bluck; halo: Wetzel; mass+env: Peng 2010) maps as `stance='supports'` **only to the CAUTION and DOMINANCE scoped claims — which they genuinely support — never to the mechanism/outflow claim.** The caveat is preserved three ways: (a) the target claim text is itself the caution/qualifier; (b) provenance records the original `stance_design` (`qualifies`, `supports_with_scope_qualifier`); (c) provenance carries `production_stance_basis: "supports a caution/qualifier claim; qualifier semantics preserved"`. Provenance is gold-standard throughout: `human_gold_status: not_human_gold`, `metrics_null_rationale` (relevance/entailment/rigor/confidence left NULL — not fabricated), and **differentiated `quality_design_basis`** (0.78 obs-with-span / 0.74 obs / 0.70 sim or single-case / 0.62 no-ledger-span) — my Step 9D per-source-quality patch, honored.

**4. Peng 2015 `6651` reuse — honored verbatim and non-destructive.** `core_sentence_ids_accepted: [P9S008, P9S009]`; `loose_sentence_ids_excluded_from_execution_binding: [P9S001, P9S002, P9S016]` — my Step 9D Patch 3 exactly. Decision: `REUSE_EXISTING_EVIDENCE_AND_EXISTING_PAGE57_LINK_NO_INSERT_NO_UPDATE`, and `production_stance_reuse_decision: "reuse as page-level citation…do not modify evidence.stance or claim_id"` — 6651 stays on its home claim 1240; Peng appears only via the existing page-57 link. The apply SQL enforces the precondition (exactly 1 Peng page-57 link, RAISE otherwise) and inserts no duplicate Peng row (anti-row-17). Correct and non-destructive.

**5. Execution-readiness — structurally ready; three patches before execute.** The apply SQL is `\set ON_ERROR_STOP on; BEGIN` → **pre-guards** (page-57 content sha256 `39200e8a…`, latest version 1709 + hash, claim count 729 / max order 731, a **normalization-tolerant anti-duplicate check across bibcode/arXiv/url/title expecting 0 existing matches**, packet-idempotency, Peng-link precondition — all `RAISE EXCEPTION`) → inserts (5 claims, 35 evidence, 35 links via CTEs + temp key-maps) → **post-guards** (exactly 5 / 35 / 35, `RAISE` otherwise) → `COMMIT`. The rollback is `BEGIN` → count-guards (0-or-35 / 0-or-5) → `DELETE` scoped **only** by `provenance->>'packet_id'` and the 5 exact claim texts → post-check `remaining=0` → `COMMIT`; it never touches Peng 6651 or any existing row. Both files are sha256-pinned in the summary/validation. This is exemplary guarded-SQL.

## Patches (resolve before `APPROVE EXECUTE`)

1. **Pre-execution: verify no automatic trust-recompute trigger fires on evidence/claim insert.** The 35 rows are `stance='supports'`, and the debated/reported claims are inserted with explicit `trust_level`/`trust_score`. If a DB trigger recomputes trust on evidence insert, the debated claims could inflate at apply time. Confirm (read-only) that no such trigger exists, or that the inserted trust levels are authoritative. (Campaign recomputes were always explicit `recalculate_trust_v2` calls, so this is likely clean — but confirm before execute.)
2. **Sequence the 2924 resolution with the visible change (Task 2 consequence).** Document that insert-only leaves the flat `consensus` 2924 surfaced next to the new model-bounded heating claim; the deferred desurface/nuance-+-trust-recompute gate must resolve 2924 in or immediately after the visible change to avoid a live contradiction.
3. **Forward requirement for the deferred trust-recompute gate.** When trust is eventually recomputed over these rows, it must honor the debated-claim semantics and provenance `stance_design` (qualifier-supports are not full support) — not naively read 35 `supports` as high trust, or the `debated`/`reported` claims will inflate (the trust-scalar-laundering tripwire).

None are defects in the SQL itself; they are consequences of the correct, non-destructive, insert-only staging that must be managed. With patch 1 verified, the packet is execution-ready.

## Safety ledger

- SQL executed: 0 · DB writes: 0 · API mutations: 0 · apply/rollback run: 0 · git: 0 · deploy/restart: 0 · product publish: 0 · execution_authorized: False
- Reads: summary, validation, 5 claim rows, evidence-insert rows (incl. full apply SQL lines 1-52 + tail guards), rollback SQL, Peng decision, DB snapshot (read-only). Files written by Lana: 1 (this report).

LANA_STEP9E_METHODS_DONE
