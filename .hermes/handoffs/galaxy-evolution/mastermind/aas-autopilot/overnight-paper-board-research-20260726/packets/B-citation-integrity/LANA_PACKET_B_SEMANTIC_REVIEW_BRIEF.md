# Lana — Packet B Brief: Semantic / No-Overclaim Review — Gate Defect vs Removal/Splitting

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_B_LANA_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_B_LANA_SEMANTIC_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at the A/B repair gate. Dispatched by: Tori (do not self-start).
- Lane: **direct Claude Code subscription only** — no API-key, no PAYG, no third-party route.
- This brief is standalone.

## Your role
Run the semantic / no-overclaim review of Kun's Packet B unsupported-citation flags and corrected candidates. For each flagged citation, decide exactly one:
- **(a) Gate defect (compound-sentence / key-assignment artifact):** the citation IS supported by its own clause, and the gate faulted it only for not covering the OTHER citation's content in the same compound sentence → recommend **sentence-splitting / re-grounding** to preserve the valid anchor, NOT deletion.
- **(b) Genuine unsupported / bare citation:** the citation has no specific support in the passage → **removal** (Kun's fix) is correct, OR **re-attribution** to a source already in that run's reference list that the passage actually supports.

Hard constraints: **no new sources, no new citations beyond the run's existing reference list, no new scientific claims, no weakened or deleted caveats.** You run AFTER Kun's candidate text exists (it does). You provide the semantic verdict; Goru's independent one-to-one mechanical cross-check (Packet B, later) and Hwao's adjudication follow — you do not make the final decision.

## The specific defect to adjudicate (from the baseline gate output)
- `gated-e2e-demo` sentence 1: "For instance, [Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50, while [Torrey2019] investigated the evolution of the mass-metallicity relation in IllustrisTNG…" Gate: `Qi2025` SUPPORTED, `Torrey2019` UNSUPPORTED — but the stored Torrey2019 reason confirms Torrey's own content IS present and faults it only for "not mentioning Qi2025." That is the compound-sentence / key-assignment pattern.
- `gated-e2e-demo` sentence 2: "Additionally, [Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG, and [Guo2016] studied the stellar mass-gas-phase metallicity relation…" Gate: `Garcia2023` SUPPORTED, `Guo2016` UNSUPPORTED — reason faults Guo2016 only for "not mentioning Garcia's analysis." Same pattern.
- `gated-halt-demo`: "Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS…" Gate: `Renzini2015` SUPPORTED, `Pearson2023` UNSUPPORTED — reason: the passage does not mention either author's specific content. This is a **grouped / bare citation** (no per-author content), likely a DIFFERENT case from the compound-sentence artifact. Assess whether `Pearson2023` has ANY specific support in the passage; if none and no supported source exists in the reference list, removal may be correct.

Kun's first pass **removed** `Torrey2019`, `Guo2016`, and `Pearson2023` (all "removal", no re-attributions). Your job is to test whether that removal discards valid anchors. Where it does (case a), the better fix keeps each citation on its own clause using ONLY the existing passage wording and the run's reference list (e.g. split the two-citation sentence into two single-citation sentences).

## Allowed READ roots (read-only)
1. Immutable source lab-runs: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/` — `gated-e2e-demo`, `gated-halt-demo` (and `fesc002` for completeness); read their `draft.tex`, `review`/`review_loop`, and `lit_reflist`/`lit_refs`.
2. Baseline: `…/baseline/`.
3. Kun's Packet B outputs (read-only): `packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.md`/`.csv`, `METHOD.md`, and `candidates/gated-e2e-demo.corrected.md`, `candidates/gated-halt-demo.corrected.md`; the Hwao preservation record; the Tori validation; this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverables ONLY under `…/packets/B-citation-integrity/lana/`
- Receipt ONLY at `…/reviews/lana/LANA_PACKET_B_RECEIPT.md`
- Temp ONLY as `…/packets/B-citation-integrity/lana/_tmp_*` (never TMPDIR, /tmp, scratchpad).
- Do NOT edit any source `draft.tex`, any Kun file, or any v1 output — produce NEW isolated files only.

## Forbidden (stop and report if any is required)
Introduce any new citation not already in that run's reference list; add any new scientific claim; weaken or delete any caveat; edit a source `draft.tex` or any Kun/Goru/v1 file; write/rewrite any current Lab run JSON; alter any Lab run directory; run the live runner; replace any existing PDF; modify the public cockpit or any public/static root; any DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance usage; Anthropic third-party PAYG routing. No publication. **Lane: direct Claude Code subscription only — no API-key / PAYG / third-party route.**

## Tasks / Deliverables
1. `SEMANTIC_REVIEW.md` — one entry per flagged citation (`Torrey2019`, `Guo2016`, `Pearson2023`, and confirm the SUPPORTED ones `Qi2025`, `Garcia2023`, `Renzini2015` are genuinely supported): verdict = `gate-defect (compound-sentence)` or `genuine`; recommended action = `split/re-ground` or `remove` or `re-attribute (to <ref-list key>)`; one-line justification grounded verbatim in the passage; explicit no-overclaim / no-new-source confirmation.
2. Where you recommend splitting/re-grounding, an isolated candidate file under `…/lana/candidates-lana/` (e.g. `gated-e2e-demo.split.md`) that keeps each citation on its own clause using ONLY existing passage wording + the run's reference list. Each candidate carries `AI_DRAFT_NOT_HUMAN_GOLD`.
3. A short comparison note stating, per run, whether you concur with Kun's removal or recommend split/re-ground/re-attribute instead — so Goru's later one-to-one cross-check and Hwao's adjudication have a clear decision surface.

## Stop conditions
A fix would need a new source/citation not in the reference list, a new scientific claim, or a weakened caveat; any `expected_value` verdict of `CONTRADICTS`; source drift vs `INPUT_SHA256.txt`; a prompt requesting payment/overage/top-up/Nous purchased-balance; any need to edit a source draft or write outside your write root.

## Completion contract
When `SEMANTIC_REVIEW.md`, any split candidate files, and the comparison note exist under your write root and `LANA_PACKET_B_RECEIPT.md` lists their SHA-256, the per-citation verdicts, any STOP notes, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success), end the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_B_LANA_SEMANTIC_COMPLETE_V1`
