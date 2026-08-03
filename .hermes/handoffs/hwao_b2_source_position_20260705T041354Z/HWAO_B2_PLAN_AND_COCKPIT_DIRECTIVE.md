# HWAO B2 PLAN + COCKPIT DIRECTIVE

From: Hwao/Fable (coordinator) · To: Tori (relay/executor), Lana, Goru, Kun · Status: PLAN/DIRECTIVE ONLY — no queue edits yet; no SQL/DB/apply/prose/runtime/git. User authorization: B2 go + cockpit visibility (Hwao-directed patch only). Tori's cron pause (`fd0987371f65`) acknowledged — **cron stays paused until B2 receipts are complete**; resumption is a Tori action after my gate note.

## 1. B2 plan and lane assignments

**Rows (4):** `28087` (2009.11175, candidate 2942) · `28108` (2009.11175, kinetic/radio check — candidates 2942/2946, option **2947**) · `28133` (2009.11175, candidate 2943) · `28074` (SWAN 2604.15438, candidate 2942).
**Paper context already established in batch 1:** 2009.11175's own finding is jet-mode feedback (ionised outflows tracking radio extents); SWAN's own finding is the two-stage jet-ISM mechanism. Batch-1 rows from both papers were introduction/background zone — expect the same and keep zone honesty.

**Lane order:** Hwao (this plan) → **Kun checker** (before any edit — see §3) → **Lana proposal** (§4; dispatch immediately, parallel with Kun) → **Goru validation** (using Kun's checker plus the batch-1 mechanical checks; block→recheck applies) → **Hwao edit gate** → **Tori bounded apply** (four queue formats + receipts; fresh pre-edit snapshot first) → count line to cockpit ("10/36").

**One coordination catch Lana must handle (written into her brief):** if `28108` routes to 2947, the duplicate/redundancy check set is **both** 2947's live evidence (26681–26685) **and** the two batch-1 rows already routed there pending SQL (28095, 28111) — three rows from the *same paper* landing on the *same claim* would stack one source's weight. Lana judges whether 28108 adds a genuinely distinct span or should be `leave_archival` to avoid same-paper stacking.

## 2. Exact cockpit patch for Tori to publish NOW (content-only; rich layout and protected anchors preserved)

- **Marker:** `GALAXY_2929_B2_RUNNING_HWAO_20260705T041354Z`
- **Phrase state (unchanged):** `NO ACTIVE EXECUTION PHRASE`
- **Status card text (verbatim):**

> **Claim-evidence cleanup — batch B2 running (Hwao coordinating)**
> We are re-filing the evidence of retired claim 2929 under its replacement claims, one decision at a time, documents-only. **6 of 36 rows are decided; batch B2 covers 4 more** (evidence 28087, 28108, 28133 from the radio-jet outflows paper; 28074 from the SWAN M51 paper).
> Lane order: Hwao plan → Lana source reading → Kun checker → Goru validation → Hwao gate → Tori applies to the queue files.
> **No database writes are possible in this phase:** SQL stays locked until all 36 decisions are complete and you approve a new packet. Nothing needs your action right now — this card is for visibility.

- **Status JSON fields:** `b2_state: "RUNNING"`, `queue_progress: "6/36 decided, 4 in flight (B2), 26 pending"`, `coordination: "Hwao plans/assembles; Tori relays/executes"`, `sql_lock: "until 36/36 + new operator-approved packet"`, marker + phrase as above.
- **Tori verification after patch:** protected anchors intact (`RICH_BASELINE_STABLE_COCKPIT_V1`, `id="baseline"`, `id="baseline-steps"`, `id="lane-board"`, `id="safety-ledger"`); guard PASS; public URLs return the new marker; no execution-phrase strings anywhere. On each later B2 milestone (proposal in, validation PASS, gate PASS, applied), Tori may update **only** the card's one progress line — no other cockpit change without a new directive.

## 3. Kun checker: YES — build before the B2 edit step (not before Lana starts)

Kun writes the read-only queue-edit checker now, in parallel with Lana: parse all four queue formats; assert 36 rows each; byte-diff untouched rows vs pre-edit snapshot; per-row enum/field/non-null checks against each row's own options lists; quote+locator presence; no-SQL-string scan; cross-format consistency for edited rows. Output: `kun_queue_checker.py` + a short usage note in this handoff dir; **the checker itself must be read-only** (reads queue files + snapshot, writes only a results JSON into this dir). Goru and Tori both run it from B2 onward. Marker: `KUN_B2_QUEUE_CHECKER_READY_20260705T041354Z`.

## 4. Lana brief — dispatch immediately (Tori relays this outline verbatim)

- **Task:** propose source-position + adjudication values for B2 rows 28087, 28108, 28133 (arXiv 2009.11175) and 28074 (arXiv 2604.15438), using the queue's own `required_source_position_fields` template — the same four blocks as batch 1 (source-position; adjudication; decision; checks).
- **Inputs:** the four queue rows; her batch-1 report (both papers already verified/zone-mapped); the tiered source rule from the 30-row plan.
- **Rules that bind:** zone honesty (introduction/background spans marked and capped at `accepted_limited`); **full `accepted` requires full-text span pinning** — otherwise cap at `accepted_limited`; abstract-only decisions acceptable for archival/route/limited outcomes with `abstract_only_verified` labeling; the 28108 same-paper-stacking judgment from §1; candidate targets are hints, not orders — she may propose differently with reasons; expected zero vote/comment/link dependencies on these rows — **if any `dependency_counts` is non-zero, stop that row and report** (batch-1 vote-honoring pattern, my gate required).
- **Outputs (two files, in this handoff dir):** `LANA_B2_PROPOSAL.md` (method, per-row reasoning, the stacking judgment) + `lana_b2_proposal.jsonl` (4 rows, full field template). Marker: `LANA_B2_SOURCE_POSITION_PROPOSAL_20260705T041354Z`.
- **Locks:** read-only; no queue edits; no SQL/DB; two output files only.

## 5. Stop conditions (any lane, any time — pause and report, never improvise)

1. Any B2 row with non-zero `dependency_counts` (votes/comments/element links) → row parked for the dependency pattern + my gate.
2. Paper identity mismatch or unfetchable source → row parked with a written question.
3. Any proposed decision that would require creating a **new claim** → out of scope; write to backlog, park the row.
4. Queue-file drift: pre-edit snapshot mismatch at apply time → stop, re-snapshot, re-gate.
5. Cross-format inconsistency after apply → revert to snapshot, re-apply once, else stop.
6. Cron `fd0987371f65` must remain paused through apply + validation; if it fires anyway, stop and verify queue integrity before proceeding.
7. Any pressure to touch SQL/DB/phrases "to save time" → tripwire; the 36/36 lock is the user's own instruction.

Milestone flow after this directive: Tori publishes the cockpit patch (§2), dispatches Lana (§4) and Kun (§3) in parallel, then the lane order runs. I gate before any queue edit, as always.

HWAO_B2_USER_GO_20260705T041354Z
