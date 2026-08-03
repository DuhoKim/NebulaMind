# Goru — Packet B Brief: Independent One-to-One Mechanical Citation Cross-Check

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_B_GORU_CROSSCHECK_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_B_GORU_CROSSCHECK_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at A/B Gate 2. Dispatched by: Tori (do not self-start).
- Lane: **existing Antigravity / agy Gemini subscription only** — no API-key, no GCP, no PAYG, no third-party route.
- This brief is standalone.

## Your role
Be the **independent mechanical arbiter** between Kun's removal map and Lana's semantic split. Mechanical = string/topic correspondence between each citation key, its OWN clause in the source `draft.tex`, and its OWN reference-list entry. Do NOT perform deep semantic judgement or pick the final publication fix — establish the one-to-one correspondence facts and consistency, and report which of Kun/Lana the mechanical evidence supports. Hwao adjudicates after your receipt; the Packet C candidate's citation fix is provisionally set to Lana's split pending your confirmation.

## Allowed READ roots (read-only)
1. Immutable source lab-runs: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/` — `gated-e2e-demo`, `gated-halt-demo` (and `fesc002` for completeness): read each `draft.tex`, the JSON `gates.citation_entailment.all` rows, and `lit_reflist`/`lit_refs`.
2. Baseline: `…/baseline/`.
3. Kun's Packet B outputs: `packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.md`/`.csv`, `METHOD.md`, `candidates/gated-e2e-demo.corrected.md`, `candidates/gated-halt-demo.corrected.md`.
4. Lana's Packet B outputs: `packets/B-citation-integrity/lana/SEMANTIC_REVIEW.md`, `COMPARISON_NOTE.md`, `candidates-lana/gated-e2e-demo.split.md`.
5. Hwao's `reviews/hwao/HWAO_PACKET_A_CANONICAL_DECISION.md` (for why this cross-check gates Packet C), the Tori validation, this brief.

## Allowed WRITE root (exclusive to you — single writer; NEW root)
- Deliverables ONLY under `…/packets/B-citation-integrity/goru-b/`
- Receipt ONLY at `…/reviews/goru/GORU_PACKET_B_RECEIPT.md` (new file; do NOT touch `GORU_PACKET_A_RECEIPT.md`, its captures, or `..._V2.md`).
- Temp ONLY as `…/packets/B-citation-integrity/goru-b/_tmp_*` (never TMPDIR, /tmp, scratchpad — the /tmp incident must not recur).
- Preserve ALL prior files: do NOT edit or overwrite any source, any Kun file, any Lana file, or any v1/v2 output. New isolated files only.

## Forbidden (stop and report if any is required)
Edit any source `draft.tex`; edit any Kun/Lana/v1/v2 file; introduce any new citation, source, number, or scientific claim; write/rewrite any current Lab run JSON; alter any Lab run directory; run the live runner; replace any existing PDF; modify the public cockpit or any public/static root; any DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance usage; Anthropic third-party PAYG routing. No publication. **Lane: existing Antigravity / agy Gemini subscription only — no API-key / GCP / PAYG / third-party route.**

## Tasks
### 1. One-to-one concordance table — `CITATION_CROSSCHECK.md` (+ `.csv`)
One row per checked citation (`gated-e2e-demo`: Torrey2019, Qi2025, Guo2016, Garcia2023; `gated-halt-demo`: Renzini2015, Pearson2023), columns:
- `citation_key`
- `own_clause` — verbatim, the sub-clause that names ONLY that key
- `own_reference_entry` — verbatim from the run's `lit_reflist`
- `own_clause_vs_own_reference` — `MATCH` / `PARTIAL` / `NO` (title/keyword correspondence of the clause to its own reference, ignoring any co-cited key)
- `gate_supported_bool` — from `gates.citation_entailment.all[].supported`
- `gate_consistent_with_one_to_one` — `YES` / `NO`; if the own-clause matches its own reference but the gate marked it unsupported for failing to entail a CO-CITED key, mark `NO — COMPOUND-SENTENCE-CROSS-ASSIGNMENT`
- `kun_action` (remove/retain) · `lana_verdict` (gate-defect/genuine; split/remove/retain)
- `goru_one_to_one_finding` — which of Kun/Lana the mechanical evidence supports, or `neither`

### 2. Candidate diff verification — `CANDIDATE_DIFF_VERIFICATION.md`
- **Lana split candidate** (`gated-e2e-demo.split.md`): mechanically verify the ONLY changes vs the source introduction are the two connective replacements (`, while ` → `. ` and `, and ` → `. `); that all four citations appear, each alone on its own sentence; and that all 5 reference entries are retained unchanged. Report `VERIFIED` or `DISCREPANCY` with specifics.
- **Kun removal candidates**: verify `gated-e2e-demo.corrected.md` removed exactly the Torrey2019 and Guo2016 clauses (and `gated-halt-demo.corrected.md` removed Pearson2023), with no other content changed; and state per citation whether the removed citation's own-clause content DID match its own reference entry (i.e. whether the removal discarded a valid anchor).

### 3. Pearson2023 mechanical facts (no verdict)
Record only the mechanical facts: does Pearson2023 have its OWN distinct per-author clause, or is it a bare grouped citation sharing one predicate with Renzini2015? Is its `lit_reflist` entry topically about the main sequence? Do NOT decide retain-vs-remove — that is Hwao's judgment call.

### 4. Per-run concordance verdict
For each run, state whether the mechanical one-to-one evidence supports Lana's split (e2e) / Kun's removal / neither, and flag any place Kun's or Lana's stated verdict disagrees with your mechanical finding.

Every deliverable carries the literal token `AI_DRAFT_NOT_HUMAN_GOLD`.

## Stop conditions
Source drift vs `INPUT_SHA256.txt`; a candidate that changed content beyond the stated connective/removal edits (report as `DISCREPANCY`, do NOT fix it); any need for a new citation/source/number/claim; a prompt requesting payment/overage/top-up/Nous purchased-balance; any need to write outside your write root or edit a prior file.

## Completion contract
When `CITATION_CROSSCHECK.md` (+ `.csv`) and `CANDIDATE_DIFF_VERIFICATION.md` exist under `…/goru-b/` and `reviews/goru/GORU_PACKET_B_RECEIPT.md` lists their SHA-256, the per-run concordance verdict, the split/removal verification results, the Pearson2023 mechanical facts, any DISCREPANCY, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success), end the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_B_GORU_CROSSCHECK_COMPLETE_V1`
