# Kun — Packet A Brief: Independent Reproducibility / Duplication Analysis + Canonical Recommendation

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_A_KUN_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_A_KUN_DUPLICATION_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at the A/B repair gate. Dispatched by: Tori (do not self-start).
- Lane: **standalone ChatGPT Codex subscription (gpt-5.5) only** — no API-key, no PAYG, no third-party route (cross-model independence from Goru's Antigravity/Gemini matrix lane is the point of this assignment).
- This brief is standalone.

## Your role
Independently analyse the four MZR-family runs for **reproducibility (traceability)** and **duplication**, and give a **canonical recommendation**. "Independent" means you derive your own findings from the immutable source runs. You MAY read Goru's field matrix (v1 now, `*.v2.*` when it lands) as a cross-reference, but you must NOT merely echo it — a disagreement with Goru is a valuable signal, not an error. Hwao makes the canonical decision only after BOTH Goru's v2 matrix receipt AND your receipt. **Your recommendation gates the Packet C `d8de519cb9c9` candidate build.**

## Critical method boundary
This is a **documentary / traceability** audit, NOT live recomputation. Do NOT run the live runner and do NOT re-pull SDSS or TNG catalog data (both forbidden). "Reproducibility" here = whether each stated result is traceable to that run's own spec/summary/provenance/history and internally consistent — not a fresh numerical rerun.

## Allowed READ roots (read-only)
1. Immutable source lab-runs: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/` — the four MZR-family runs: `2958462772b2`, `d8de519cb9c9`, `e2f3b038f8dd`, `gated-e2e-demo` (+ subdirs/histories/figures/manifests).
2. Baseline: `…/baseline/`.
3. Goru's field matrix `packets/A-mzr-reconciliation/goru/MZR_FIELD_MATRIX.md`/`.csv` (v1 and `*.v2.*`) for cross-reference; the Hwao preservation record; the Tori validation; this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverables ONLY under `…/packets/A-mzr-reconciliation/kun/`
- Receipt ONLY at `…/reviews/kun/KUN_PACKET_A_RECEIPT.md` (distinct from your existing `KUN_PACKET_B_RECEIPT.md` — do not overwrite that).
- Temp ONLY as `…/packets/A-mzr-reconciliation/kun/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Forbidden (stop and report if any is required)
Run the live runner or re-pull SDSS/TNG data; write/rewrite any current Lab run JSON; alter any Lab run directory; replace any existing PDF; overwrite any v1 output or Goru's files; modify the public cockpit or any public/static root; any DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance usage; Anthropic third-party PAYG routing. No publication. **Lane: standalone ChatGPT Codex subscription (gpt-5.5) only — no API-key / PAYG / third-party route.**

## Tasks
1. **Reproducibility (traceability) audit** — `REPRODUCIBILITY_AUDIT.md`. Per run, check whether every stated numeric result and N-count is traceable to that run's own fields and internally consistent (e.g. `e2f3b038f8dd`: `oh_at_logM9=8.572`, `oh_at_logM10p5=9.05`, N=80,000; the `120,000` SDSS and `23,722` TNG counts elsewhere). Flag any number lacking provenance or contradicting another field. Do not recompute from raw catalogs; do not invent a value.
2. **Metallicity O/H-scale gap** — explicitly record whether each run states an O/H calibration/scale. SDSS calibration is `ABSENT` across these runs; TNG states "SF-weighted gas metallicity → O/H (solar-scaled)." Note that any TNG-vs-SDSS MZR reconciliation requires a common O/H scale; where the scale is `ABSENT`, record it as a reproducibility/reconciliation **gap**. Do NOT invent or apply any dex offset — flag the gap, don't close it.
3. **Duplication analysis** — `DUPLICATION_ANALYSIS.md` (+ optional `.csv`). Classify each run pair as `exact-duplicate` / `superset-subset` / `near-duplicate-different-sample` / `distinct`, grounded in fields (summary strings, N, method, data_sources, artifacts, gates). Verify these known signals:
   - `d8de519cb9c9` and `gated-e2e-demo` carry an identical summary string (same TNG 23,722 + SDSS 120,000, same `mass-metallicity` method). Determine the relationship — e.g. `d8de519cb9c9` is figure/summary-only (no draft), `gated-e2e-demo` is the drafted + gated build of the same analysis.
   - the SDSS-only pair `2958462772b2` (120,000) vs `e2f3b038f8dd` (80,000) — same topic family, different sample/label.
4. **Canonical recommendation** — `CANONICAL_RECOMMENDATION.md`. Recommend which run should be the canonical MZR representative, and specifically whether the Packet C `d8de519cb9c9` candidate should be built from `d8de519cb9c9` or from `gated-e2e-demo`; list which runs are redundant; state your assumptions and the open reconciliation gaps (esp. the O/H-scale gap). This is a RECOMMENDATION only — Hwao decides.

Every artifact must carry the literal token `AI_DRAFT_NOT_HUMAN_GOLD`.

## Stop conditions
A number you cannot trace and would have to invent; source drift vs `INPUT_SHA256.txt`; any `expected_value` verdict of `CONTRADICTS`; a prompt requesting payment/overage/top-up/Nous purchased-balance; any need to run the runner, re-pull data, or write outside your write root.

## Completion contract
When `REPRODUCIBILITY_AUDIT.md`, `DUPLICATION_ANALYSIS.md`, and `CANONICAL_RECOMMENDATION.md` exist under your write root and `KUN_PACKET_A_RECEIPT.md` lists their SHA-256, the traceability findings, the duplication classifications, the canonical recommendation, any STOP notes, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success), end the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_A_KUN_DUPLICATION_COMPLETE_V1`
