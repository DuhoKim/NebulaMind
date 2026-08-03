# HWAO B3 PLAN + COCKPIT DIRECTIVE

From: Hwao/Fable (coordinator) · To: Tori (relay/executor), Lana, Goru, Kun · Status: PLAN/DIRECTIVE ONLY — no queue edits yet; no SQL/DB/apply/prose/runtime/git. Standing: 10/36 decided, 26 pending, cron `fd0987371f65` paused (stays paused until B3 receipts complete), phrase `NO ACTIVE EXECUTION PHRASE`, SQL locked until 36/36 + new operator-approved packet.

## 1. B3 plan and lane order (same proven pattern)

**Rows (6, one paper — arXiv 2403.17145, galaxy groups as AGN-feedback probe):** 28123 (opts 2946/2942) · 28127 (2946/2945/2947) · 28139 (2946/2947) · 28143 (2946/2943) · 28151 (2946) · 28158 (2946/2947). All dependency counts zero (verified in the brief; Lana re-confirms from the snapshot).

**Lane order:** cockpit checkpoint (§2) → **Lana proposal** (§3) ∥ **Kun checker config update** (§4) → **Goru validation** (checker + mechanical checks; block→recheck) → **Hwao gate** (PASS/BLOCKED; any `retire_reject` reviewed row-by-row) → **Tori bounded apply** (fresh pre-edit snapshot first; four formats; receipts) → count line ("16/36").

**Two B3-specific coordination rules (the batch's real content):**

- **R1 — same-paper stacking cap, now intra-batch.** All six rows come from ONE paper, and 2946 appears in every row's options — six same-paper rows must not all become supports of one claim. Default expectation: the **strongest one or two spans per target claim** proceed as `accepted_limited` (or role-distinct caution), and the rest go `leave_archival` with `redundant_same_paper` reasoning — unless a span is genuinely role-distinct (support vs caution vs limitation), which is the B2-28108 precedent. Lana judges; I gate.
- **R2 — the observational-heating gap flag.** 2946 (maintenance/heating) is `model_bounded` because its 9E evidence set is simulation-heavy, and the campaign carries a standing gap card: *no observational maintenance-heating evidence*. Galaxy groups are exactly the regime where observational heating evidence lives (X-ray cavities, bubbles, jet-inflated lobes). **If any B3 span is observational group-scale heating evidence (not simulation, not review-of-simulations), Lana must flag it `gap_card_relevant: observational_maintenance_heating`** in the row note. It still enters as `accepted_limited` under this batch (no cap change now) — but the flag feeds the later ledger decision on whether 2946's model-bounded framing can eventually be revisited through proper Step 5/6 machinery. Finding one of these would be the batch's most valuable outcome; inventing one would be the worst — zone honesty decides.

**Zone caution:** 2403.17145 reads like a review/probe-style paper; review sentences are secondary synthesis, not primary measurement — they support background/qualifier roles more often than measurement supports.

## 2. Cockpit checkpoint — YES, publish before dispatching lanes (content-only patch)

- **Marker:** `GALAXY_2929_B3_RUNNING_HWAO_20260705T044944Z` · **Phrase state:** `NO ACTIVE EXECUTION PHRASE` (unchanged)
- **Card text (verbatim):**

> **Claim-evidence cleanup — batch B3 running (Hwao coordinating)**
> Re-filing retired claim 2929's evidence under its replacement claims, documents-only. **10 of 36 rows decided; batch B3 covers 6 more**, all from one paper (galaxy groups as a probe of AGN feedback — arXiv 2403.17145). Because all six come from the same paper, at most a couple of the strongest spans will attach per claim; the rest stay archival to avoid over-weighting one source.
> Lane order: Hwao plan → Lana source reading → Kun checker → Goru validation → Hwao gate → Tori applies.
> **No database writes are possible in this phase:** SQL stays locked until all 36 decisions are complete and you approve a new packet. Nothing needs your action — this card is for visibility.

- **Status JSON:** `b3_state: "RUNNING"`, `queue_progress: "10/36 decided, 6 in flight (B3), 20 pending"`, marker/phrase as above, other fields unchanged.
- **Tori verification after patch:** protected anchors intact, guard PASS, public URLs return the marker, no phrase strings. Milestone updates: only the card's one progress line.

## 3. Lana brief outline (Tori relays verbatim; dispatch immediately after the cockpit patch)

- **Task:** propose source-position + adjudication for the six B3 rows using the queue's field template (four blocks, as batches 1–2).
- **Source material:** arXiv 2403.17145 — abstract first; **fetch full text if publicly accessible** (a review paper's zone judgments usually need body context; six rows amortize the read). Label per row honestly: `abstract_only_verified` vs full-text-verified with locators.
- **Candidate handling:** options are hints, not orders (2946-heavy; 2947 on three rows; 2942/2943/2945 scattered). Apply **R1** (stacking cap: strongest 1–2 spans per target, rest archival with `redundant_same_paper`) and **R2** (flag observational group-scale heating spans `gap_card_relevant`). For any 2947 route, the dedup set = live 26681–26685 + routed 28095/28111 + caution 28108 (record in the row). For 2946, record the queue's successor-evidence reference set if present, else `db_dedup_deferred_to_sql_time` (the standing C2 pattern).
- **Tiered rule (binding):** full `accepted` only with full-text span pinning; otherwise cap `accepted_limited`. Model-bounded discipline for 2946: simulation/review-of-simulation spans must say so; no measured-prevalence language.
- **Park/archival conditions:** park (don't decide) on paper-identity doubt, non-zero dependency counts, or any outcome needing a **new claim** (→ backlog note instead). `leave_archival` is the *default* for redundant same-paper spans and for topic-match-only spans (the 28133 precedent: measuring-methods sentences are not suppression evidence).
- **Outputs:** `LANA_B3_PROPOSAL.md` + `lana_b3_proposal.jsonl` (6 rows) in this handoff dir. Marker: `LANA_B3_SOURCE_POSITION_PROPOSAL_20260705T044944Z`. Read-only otherwise; two files only.

## 4. Kun checker: reuse with a config update (no logic changes)

The B2 checker's defaults point at B2 paths/rows. Kun updates it to accept run-config (queue dir, pre-edit snapshot dir, expected-edited-row-id set, output path) via args or a small JSON config — **no validation-logic changes** — and saves the B3 config in this handoff dir. If the checker already supports args, this is config-only. Output: updated `kun_queue_checker.py` (or config file) + one-line usage note here. Marker: `KUN_B3_CHECKER_CONFIG_READY_20260705T044944Z`. Checker remains read-only (writes only its results JSON).

## 5. Stop conditions and hard locks

Locks (verbatim from the brief, governing every lane): no DB queries/connections, no SQL files, no apply/rollback files, no DB writes, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge; cockpit only as directed in §2; `product_publication_gate` + `write_lock` untouched on all 36 rows; **SQL locked until 36/36 + new operator-approved packet.**
Stop conditions (pause + report, never improvise): (1) any B3 row showing non-zero dependencies at proposal time; (2) paper identity mismatch/unfetchable; (3) any outcome requiring a new claim → backlog + park; (4) pre-edit snapshot drift at apply → stop, re-snapshot, re-gate; (5) cross-format inconsistency post-apply → revert, re-apply once, else stop; (6) cron fires despite pause → stop, verify queue integrity; (7) any shortcut pressure toward SQL/DB/phrases → tripwire.

**After B3 receipts:** cockpit line updates to "16/36 … next: B4 (two four-row papers, 8 rows)"; cron may resume; I dispatch B4 on the same pattern per the standing go-ahead, unless the user redirects.

HWAO_B3_USER_GO_20260705T044944Z
