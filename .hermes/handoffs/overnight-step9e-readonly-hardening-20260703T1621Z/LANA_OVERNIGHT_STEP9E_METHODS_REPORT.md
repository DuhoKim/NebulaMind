# Lana — overnight Step 9E read-only hardening review

Task: Overnight Step 9E hardening review · Lane: Lana (methods / risk reviewer) · Read-only.
Written: 2026-07-04, repo `/Users/duhokim/NebulaMind/NebulaMind`. **No DB writes, no SQL executed, no apply/rollback run, no API/migration/deploy/git.**

## Verdict: **PASS_WITH_PATCHES**

All five critical schema-safety patches are verified, they do **not** weaken provenance/stance semantics (the shortened `debate_stance` nuance is preserved in `debate_stance_basis_long`), and the runbooks are strong on execution-time safety — exact-phrase gate, no method fallback without countersign, the 2924 visible-intermediate-state reconfirmation (my Step 9E Patch 2), and mandatory evidence_votes/jury_scorecards drift checks. One small documentation patch remains: explicitly record the deferred trust-recompute requirement (my Step 9E Patch 3) so it is not lost. **No blocker before the operator sees the wake-up handoff.**

## Critical patches — all verified

1. **`debate_stance` ≤20 + long basis preserved.** New values: `mixed_debated` (13), `reported_scoped` (15), `mixed_debated`, `mixed_debated`, `model_bounded` — all ≤20 (column is String(20); the old `mixed_debated_or_reported_after_vote_review` was 43 = overflow). `debate_stance_basis_long` present on all 5 (43/36/13/13/49 chars) carrying the full nuance. Schema audit `payload_lengths.claims.debate_stance: 15`. ✓
2. **`match_method` = `step9e_source_registry_key` (26 ≤32).** All 35 citation links use it; audit `payload_lengths.page_citation_links.match_method: 26`. ✓
3. **Rollback tightened.** Claim count and DELETE are now scoped by `page_id=57 AND order_idx BETWEEN 732 AND 736 AND text = ANY(...)` (triple-scoped), and the state guard allows only all-zero or all-full packet states. Evidence/links remain `packet_id`-scoped; Peng 6651 and existing rows are never touched. ✓
4. **Validator + schema/SQL contract audit both PASS.** `status: PASS`, `validator_status: PASS`, `apply_required_tokens_present: True`, `rollback_required_tokens_present: True`, no payload exceeds its column. ✓
5. **Runbooks forbid execution without the exact phrase.** Pre-execution checklist hard gate ("Stop unless the latest user message exactly equals `APPROVE EXECUTE …`; 'continue/keep going/do it/approved' is not enough"); execution runbook "Do not run … unless the latest user message is exactly `APPROVE EXECUTE …`." ✓

## Task 1 — patches preserve doctrine and do not weaken provenance/stance

Confirmed. The patches are pure schema-safety (column-length + rollback-scope). The `debate_stance` shortening loses **no** meaning — the full basis lives in `debate_stance_basis_long`. The JSONB provenance that carries the anti-laundering semantics (`stance_design`, `human_gold_status: not_human_gold`, `metrics_null_rationale`, differentiated `quality_design_basis`) is untouched (2628-char payload intact). Stance mapping, Peng restriction (P9S008/P9S009 only), and non-destructive reuse are all preserved. No weakening.

## Task 2 — runbook execution-time safety

- **Exact phrase:** ✓✓ strong hard gate in both the pre-execution checklist and the (locked) execution runbook.
- **No method fallback without countersign:** ✓✓ pre-exec item 7 and execution runbook ("if psql unavailable or a Python/raw-cursor fallback is proposed, stop and obtain a fresh Goru/Kun mechanical method check").
- **Visible intermediate state + 2924 sequencing (my Patch 2):** ✓ pre-exec item 6 — "Reconfirm with the operator that the visible intermediate state is acceptable: five new claims and 35 citation links may appear before prose content is applied; old claim 2924 remains until the later visible/desurface/nuance gate."
- **evidence_votes / jury_scorecards drift surface:** ✓✓ post-exec runbook makes packet-specific checks against both mandatory (baseline counts 2603 / 210 recorded), plus Celery/worker-task inspection, and "if background workers created votes/scorecards outside the direct apply SQL, do not silently accept it."
- **Trust recompute (my Patch 3):** ⚠️ **partial.** The *immediate* risk is covered — post-exec item 2 (row-level payload verification) would catch any trust-level drift on the new claims, and items 4–5 surface the vote/jury automation that could drive a recompute. But the **forward requirement** — that when trust is eventually recomputed over the 35 all-`supports` rows, it must honor the `debated`/`reported` design and provenance `stance_design` (qualifier-supports ≠ full support), or the debated claims inflate — is not explicitly written down.
- **No Step 10 creep:** ✓ post-exec item 6 forbids publishing prose / updating `wiki_pages` / unlocking Step 10 as part of Step 9E verification.

## Task 3 — blockers before the wake-up handoff

**No blocker.** The packet is unexecuted, checksum-pinned (apply `bf6e60b2…`, rollback `11624d35…`), locked behind the exact phrase, schema-safe, and the runbooks cover execution/containment well. One small documentation patch (not a blocker):

**Patch (documentation): record the deferred trust-recompute requirement.** Add to the post-execution runbook (or the deferred-gate handoff) one line: *"When trust is later recomputed over the Step 9E claims, it must honor the inserted `debated`/`reported` levels and provenance `stance_design` — the 35 `supports` rows are supports of scoped caution/qualifier/debate claims, not full support for AGN dominance; a naive recompute would inflate the debated claims (trust-scalar-laundering tripwire)."* This closes my Step 9E Patch 3 in writing so the future gate cannot lose it.

Optional nicety: the pre-execution checklist could add an explicit post-apply trust-level check ("confirm the 5 new claims still read `debated`/`reported` after apply") to make the auto-recompute-trigger verification (my Step 9E Patch 1) a named step rather than an implicit consequence of the payload check.

## Safety ledger

- DB writes: 0 · SQL executed: 0 · apply/rollback run: 0 · API mutations: 0 · migrations: 0 · deploy/restart: 0 · product publish: 0 · git: 0 · execution_authorized: False
- Reads: 5 claim rows, apply + rollback SQL, schema/SQL contract audit, runbooks validation, pre-execution / execution / post-execution runbooks (read-only). Files written by Lana: 1 (this report).

LANA_OVERNIGHT_STEP9E_METHODS_DONE
