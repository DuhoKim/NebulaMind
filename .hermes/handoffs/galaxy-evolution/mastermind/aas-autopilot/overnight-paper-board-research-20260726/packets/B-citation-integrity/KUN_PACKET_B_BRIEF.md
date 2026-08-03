# Kun — Packet B Brief: Citation-Integrity Unsupported-Claim Map + Isolated Corrected Candidates

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_B_KUN_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_B_KUN_CITATIONMAP_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable (coordinator) at T0 = 2026-07-26 22:32 KST / 2026-07-26T13:32:16Z
- Dispatched by: Tori (do not self-start before Tori dispatch)
- Lane: **standalone ChatGPT Codex subscription (gpt-5.5) only** — no API-key, no PAYG, no third-party route (cross-model independence from Goru's Antigravity/Gemini lane is intentional).
- This brief is standalone. You do not need to open any other file to know your scope, roots, or stop rules.

## Your role
Produce the exact, one-to-one **unsupported-claim / citation map** across the board's runs, and **isolated corrected candidate text** (NEW files only — never edit a source draft). Goru will independently repeat the one-to-one citation check against your map; Lana runs the no-overclaim review only AFTER your candidate text exists. **Do not weaken any caveat to make a candidate pass — if a fix would require that, STOP.**

## Allowed READ roots (read-only — never write here)
1. Immutable source lab-runs (read-only): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/`
   Runs that carry citation gates or reference lists — read their JSON, `draft.tex`, and `review`/`review_loop`:
   - `gated-e2e-demo` / `gated-e2e-demo.json` (citation_entailment: 2 unsupported of 4 at baseline)
   - `gated-halt-demo` / `gated-halt-demo.json` (citation_entailment: 1 unsupported of 2 at baseline)
   - `fesc002` / `fesc002.json` (citation_entailment: 0 unsupported of 0, adversarial=true at baseline)
   - Any other run only if it carries `lit_reflist`/`lit_refs`/a `citation_entailment` block; otherwise out of scope.
2. Baseline (read-only): `…/overnight-paper-board-research-20260726/baseline/` — `BOARD_SNAPSHOT.json`, `INPUT_SHA256.txt`, `INPUT_MANIFEST.json`.
3. This brief and the `EXECUTION_BRIEF.md` at the output-root top.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverables ONLY under: `…/overnight-paper-board-research-20260726/packets/B-citation-integrity/kun/`
- Your receipt ONLY at: `…/overnight-paper-board-research-20260726/reviews/kun/KUN_PACKET_B_RECEIPT.md`
- Temp/intermediate files ONLY as `…/packets/B-citation-integrity/kun/_tmp_*` (NEVER TMPDIR, /tmp, or a scratchpad — scoped-lane rule).
- Do not write anywhere else, including Goru's / Lana's subfolders or the packet root.

## Forbidden (stop and report if any is required)
Write/rewrite any current Lab run JSON; **edit any source `draft.tex`** (corrected candidates are NEW isolated files under your write root); alter any Lab run directory; run the live runner; replace any existing PDF; modify the public cockpit or any public/static root; any DB/SQL/API/wiki/page-version write; deploy/restart; git add/commit/push/merge; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance usage; Anthropic third-party PAYG routing. No publication. **Lane: standalone ChatGPT Codex subscription (gpt-5.5) only — no API-key / PAYG / third-party route.**

## Task
### 1. Unsupported-claim / citation map
`UNSUPPORTED_CLAIM_MAP.md` + `UNSUPPORTED_CLAIM_MAP.csv` — one row per checked citation, columns: `run_id`, `citation_key`, `sentence` (verbatim), `gate_verdict` (supported / unsupported), `gate_reason` (verbatim from the run's `citation_entailment` block), `kun_adjudication` (agree / disagree + one-line mechanical reason). Ground every row in the gate output actually present in the run JSON; **do not invent citations not present in the source.**

Baseline signals to **verify, not assume**:
- `gated-e2e-demo`: `Torrey2019` UNSUPPORTED (passage supports Qi2025, not Torrey2019 — swapped attribution); `Guo2016` UNSUPPORTED (passage supports Garcia2023, not Guo2016 — swapped attribution). 2 of 4 checked; `Qi2025` and `Garcia2023` marked SUPPORTED.
- `gated-halt-demo`: `Pearson2023` UNSUPPORTED (passage does not mention it); `Renzini2015` SUPPORTED. 1 of 2 checked.
- `fesc002`: 0 unsupported of 0 checked, `adversarial=true`. Confirm explicitly that no citation is silently *unchecked* (i.e. distinguish "checked and supported" from "not checked at all"); record which.

### 2. Isolated corrected candidates
For each UNSUPPORTED citation, produce a corrected candidate in a NEW file under your write root (e.g. `candidates/gated-e2e-demo.corrected.md`, `candidates/gated-halt-demo.corrected.md`). For each fix, choose and label exactly one of:
- (a) re-attribute the citation to the reference the passage actually supports, or
- (b) remove the unsupported citation entirely.
Base every fix only on the existing passage text + the run's `lit_reflist`/`lit_refs`. **Introduce no new scientific claim and no new citation that is not already in that run's reference list.** Mark every candidate file `AI_DRAFT_NOT_HUMAN_GOLD`.

### 3. Method note
`METHOD.md` — describe exactly how you matched each claim to each citation (what text you compared, what counts as "supported"), precisely enough that Goru can reproduce your one-to-one check independently.

## Stop conditions (halt, write STOP in receipt, do not continue)
- A corrected candidate would require a NEW unsupported number or a NEW citation not in the source reference list.
- A fix would require weakening or deleting a caveat.
- Any run shows an `expected_value` verdict of `CONTRADICTS`.
- Any source file's live hash differs from `INPUT_SHA256.txt` (source drift).
- Any prompt requests payment, overage, top-up, or Nous purchased-balance.
- Any step would require editing a source `draft.tex` or writing outside your write root.

## Completion contract
When the map (md+csv), the corrected candidate files, and `METHOD.md` exist under your write root, write `…/reviews/kun/KUN_PACKET_B_RECEIPT.md` containing: files produced (with their SHA256), a count of checked vs unsupported per run, which fixes are re-attributions vs removals, any STOP notes, and a final completion state — one of `DONE` / `PARTIAL` / `BLOCKED`. Never relabel `PARTIAL` or `BLOCKED` as success. End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_B_KUN_CITATIONMAP_COMPLETE_V1`
