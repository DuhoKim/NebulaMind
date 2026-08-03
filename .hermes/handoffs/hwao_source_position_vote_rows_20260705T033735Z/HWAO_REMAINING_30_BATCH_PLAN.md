# HWAO PLAN — remaining 30 source-position rows, batched by paper

From: Hwao/Fable (coordinator) · To: Tori, Lana, Goru, Kun · Status: PLAN ONLY — no queue edits, no SQL, no DB, no apply files, no prose/runtime/git/public-cockpit mutation. User hard lock restated and governing: **no SQL until all 36 rows carry completed human/source decisions.** Current standing: 6/36 done (validated PASS), 30 remain.

## 1. Source-paper batches (12 papers → 5 batches; grouping verified against the live queue)

| Batch | Papers | Evidence rows | Count | Character (from triage hints) |
|---|---|---|---|---|
| **B2 — already-verified papers** | arXiv 2009.11175 (×3), arXiv 2604.15438 SWAN (×1) | 28087, 28108, 28133, 28074 | 4 | kinetic/radio routing checks; both papers already abstract-verified and zone-mapped in batch 1 |
| **B3 — the big single paper** | arXiv 2403.17145 (galaxy groups as AGN-feedback probe) | 28123, 28127, 28139, 28143, 28151, 28158 | 6 | one read amortized over six rows; alternative/qualifier-heavy → likely 2944/2945 or archival |
| **B4 — the two four-row papers** | arXiv 2512.05584 (×4), arXiv 2512.21927 Perseus superbubble (×4) | 28066, 28069, 28070, 28073 · 28076, 28080, 28083, 28084 | 8 | superbubble rows are SN-feedback context → expect qualifier/reject-out-of-AGN-scope outcomes |
| **B5 — the two three-row papers** | arXiv 2508.06707 (×3), arXiv 0901.1880 ΛCDM sim (×3) | 28062, 28089, 28144 · 28075, 28110, 28131 | 6 | sim paper rows are model-bounded-role candidates; measured-prevalence language forbidden |
| **B6 — remainder** | arXiv 1203.2926 (×2) + singletons 1507.06366, 2605.03008, 2111.01801, 2604.22922 | 28114, 28118 · 28082, 28088, 28140, 28148 | 6 | mixed; 2605.03008 and 2604.22922 were already read in earlier campaign passes — reuse those notes |

Total: 4+6+8+6+6 = **30** ✓. One batch in flight at a time; the queue has a single editor (Tori) per batch, no parallel edits.

## 2. Lane order per batch — the proven sequence, plus one Kun task once

Per batch: **Lana proposes** (report + per-row JSONL, same field template as batch 1) → **Goru validates** (mechanical checks; block→recheck on any failure) → **Hwao gates** (I review; all `retire_reject` rows get individual review — rejection removes rows from future consideration and deserves per-row eyes) → **Tori edits** the four queue formats + receipts → count line updates.
**Kun, once, before B2's edit step:** write a small local, read-only **queue-edit checker script** (parse all four formats; assert row count 36; diff untouched rows byte-level; per-row enum/field/non-null checks; no-SQL-string scan) saved in this handoff dir. Five more validation rounds by hand is where mistakes creep in; Goru and Tori both run the checker from B2 onward. Docs/handoff script only — it touches nothing outside its own output.

## 3. Abstract-only vs full-text — a tiered rule, not a blanket answer

- **Abstract-only remains acceptable** (labeled `abstract_only_verified`, caveat carried into the row) for: `leave_archival`, `retire_reject`, `route_kinetic_radio`, and `relink` at **`accepted_limited`** — these are disposition/metadata decisions where the abstract + snippet suffice to judge zone, topic, and vote-consistency.
- **Full-text pinning is required** before any row is marked full **`accepted`** for a relink to a visible successor — accepted rows are tomorrow's citation candidates, and the campaign's standard for citation-grade positions is a located span. If full text is unavailable, the row caps at `accepted_limited`.
- **Escalation rule:** any ambiguity (unclear zone, stance-vs-hint tension, paper identity doubt) → full-text before deciding, or park the row with a written question rather than guessing.
- **Batch-1 retro-note (standing):** 28095 and 28141 were marked `accepted` on abstract-only under the earlier rule; they stay flagged for the full-text pinning pass already recorded in their rows — that pass can run alongside any later batch.

## 4. Hard locks and stop conditions

Locks (every batch): no `psql`/DB/SQL/apply/rollback files; no execution phrases; edits confined to the four queue files + handoff reports/receipts; no prose/wiki/runtime/git/public-cockpit mutation beyond the pre-authorized count line; `product_publication_gate` and `write_lock` untouched on all rows; **SQL stays locked until 36/36, then only via a new operator-approved packet.**
Stop conditions (pause the row or batch, report, await my direction): a remaining row turns out to carry vote/comment/element-link dependencies (`dependency_counts` non-zero → handle per the batch-1 vote-honoring pattern, my gate required); pre-edit snapshot drift on the queue files; paper identity cannot be verified (title/ID mismatch class); a proposed decision would require creating a *new* claim (out of scope — write it to the backlog instead, park the row); cross-format inconsistency after edit (revert to snapshot, re-apply).

## 5. First next batch: **B2 — the four rows from already-verified papers.**

Reasons: both papers were fetched, verified, and zone-mapped in batch 1 (2009.11175's own finding is jet-mode feedback; SWAN's is the two-stage jet-ISM mechanism), so per-row marginal cost is the lowest of any batch; three of the four rows are kinetic-routing candidates onto 2947 — the exact decision pattern just exercised and gated; and a fast, clean B2 proves the batch machinery (including Kun's checker) before the six-row B3 read. Expected outcome shape: routes to 2947 and/or `accepted_limited` relinks, with the same zone-honesty discipline.

Cockpit: unchanged except the pre-authorized count line after each validated batch ("10/36 … 16/36 … 24/36 … 30/36 … 36/36 adjudicated — SQL locked until 36/36"). When 36/36 is reached, I will assemble the completion review and only then plan the SQL packet request for the operator.

HWAO_REMAINING_30_SOURCE_POSITION_BATCH_PLAN_20260705T033735Z
