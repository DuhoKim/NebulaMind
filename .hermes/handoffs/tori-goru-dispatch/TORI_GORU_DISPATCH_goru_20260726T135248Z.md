# Tori -> Goru dispatch

Target: goru
Timestamp: 20260726T135248Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260726T135248Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# Goru — Packet A Brief: MZR Mechanical Field/Provenance Matrix

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_A_GORU_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_A_GORU_MECHMATRIX_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable (coordinator) at T0 = 2026-07-26 22:32 KST / 2026-07-26T13:32:16Z
- Dispatched by: Tori (do not self-start before Tori dispatch)
- Lane: **existing Antigravity / agy Gemini subscription only** — no API-key, no GCP, no PAYG, no third-party route (cross-model independence from the Codex lane is intentional).
- This brief is standalone. You do not need to open any other file to know your scope, roots, or stop rules.

## Your role (mechanical only)
Extract fields verbatim and lay them side by side. **Do not infer, do not conclude, do not draft science, do not apply any correction or reconciliation.** The canonical MZR reconciliation decision is Hwao's, made only after BOTH your receipt and Kun's independent reproducibility/duplication receipt exist. Your job is to make the raw facts and their agreements/disagreements visible; Kun independently analyses reproducibility and duplication; Hwao adjudicates.

## Allowed READ roots (read-only — never write here)
1. Immutable source lab-runs (read-only): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/`
   Only these four MZR-family runs and their run subdirectories, histories, figures, tex/pdf, manifests:
   - `2958462772b2` / `2958462772b2.json`
   - `d8de519cb9c9` / `d8de519cb9c9.json`
   - `e2f3b038f8dd` / `e2f3b038f8dd.json`
   - `gated-e2e-demo` / `gated-e2e-demo.json`
2. Baseline (read-only): `…/overnight-paper-board-research-20260726/baseline/` — `BOARD_SNAPSHOT.json`, `INPUT_SHA256.txt`, `INPUT_MANIFEST.json`.
3. This brief and the `EXECUTION_BRIEF.md` at the output-root top.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverables ONLY under: `…/overnight-paper-board-research-20260726/packets/A-mzr-reconciliation/goru/`
- Your receipt ONLY at: `…/overnight-paper-board-research-20260726/reviews/goru/GORU_PACKET_A_RECEIPT.md`
- Temp/intermediate files ONLY as `…/packets/A-mzr-reconciliation/goru/_tmp_*` (NEVER TMPDIR, /tmp, or a scratchpad — scoped-lane rule).
- Do not write anywhere else, including Kun's subfolder or the packet root.

## Forbidden (stop and report if any is required)
Write/rewrite any current Lab run JSON; alter any Lab run directory; run the live runner; replace any existing PDF; modify the public cockpit or any public/static root; any DB/SQL/API/wiki/page-version write; deploy/restart; git add/commit/push/merge; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance usage; Anthropic third-party PAYG routing. No publication. **Lane: existing Antigravity / agy Gemini subscription only — no API-key / GCP / PAYG / third-party route.**

## Task — the field/provenance matrix
For EACH of the four runs, extract the following cells **verbatim from the source JSON** (quote the value). If a field is not present, write the literal token `ABSENT`. **Never infer a missing value.**

- `run_id`, `status`, `created_utc`
- `spec.method`, `spec.data_sources`, `spec.topic`, `spec.topic_source`, `spec.outputs`, `spec.force`
- `result.method`, `result.data_sources`, `result.summary` (full verbatim string)
- N galaxies per data source, exactly as stated in the summary/result (e.g. "SDSS 120,000", "TNG 23,722")
- Metallicity indicator / calibration / O/H scale — verbatim if stated; `ABSENT` if the JSON does not state a calibration or scale. Record verbatim any phrasing such as "SF-weighted gas metallicity → O/H (solar-scaled)".
- Mass definition — verbatim if stated; else `ABSENT`
- Redshift — verbatim if stated; else `ABSENT`
- Explicit numeric O/H anchors where present (e.g. `oh_at_logM9`, `oh_at_logM10p5`) — value + key
- Artifacts declared (`artifacts[]`) AND which exist on disk (draft.pdf? draft.tex? figure png? review/review_loop?) — confirm presence from disk + `INPUT_MANIFEST.json`
- Gates present and their verdicts (`novelty`, `expected_value`, `citation_entailment`) — verbatim verdict tokens; `ABSENT` if the run has no gates block
- `result.provenance` / any provenance or caveat string — verbatim; else `ABSENT`
- SHA256 of each of that run's files, copied from `INPUT_SHA256.txt`

### Deliverables (all under your write root)
1. `MZR_FIELD_MATRIX.csv` — machine-readable (one row per run × field, or a wide table; your choice, but header row required).
2. `MZR_FIELD_MATRIX.md` — human-readable matrix, PLUS a "Cross-run consistency" section that states **mechanically** which fields agree / differ / are ABSENT across runs (e.g. "SDSS N = 120,000 in three runs vs 80,000 in e2f3b038f8dd", "O/H calibration scale = ABSENT in all four", "d8de519cb9c9 and gated-e2e-demo carry an identical summary string"). State only same/different/absent — **draw no scientific conclusion** about which is correct.
3. `PROVENANCE_NOTES.md` — the verbatim provenance/caveat strings per run.

Every science-touching artifact you write must carry the literal token `AI_DRAFT_NOT_HUMAN_GOLD`.

## Known cross-run signals to make VISIBLE (do not resolve — that is Kun's / Hwao's job)
- `d8de519cb9c9` and `gated-e2e-demo` share an identical TNG(23,722)+SDSS(120,000) summary string. Record as "duplicate summary string across two runs"; leave duplication analysis to Kun.
- `e2f3b038f8dd` is labeled `method=scaling-relation-evolution`, `topic=main-sequence-quenching`, yet reports an MZR (mzr.png, 12+log(O/H) vs logM★, `oh_at_logM9=8.572`, `oh_at_logM10p5=9.05`). Record the label↔content mismatch verbatim; do NOT relabel it.
- SDSS metallicity calibration scale is not stated in these run JSONs. If `ABSENT`, write `ABSENT`. Do NOT apply any dex offset or scale correction — Hwao is aware SDSS-Tremonti vs Te/PP04 O/H scales can differ by ~0.24 dex, but reconciling that is a downstream decision, not yours.
- `d8de519cb9c9` has no draft.pdf/draft.tex (draft was queued, not built). Confirm from disk + manifest and record as `ABSENT` for those artifacts. This run is the "d8 candidate" whose candidate build is gated by Packet A — flag it clearly.

## Stop conditions (halt, write STOP in receipt, do not continue)
- Any source file's live hash differs from `INPUT_SHA256.txt` (source drift).
- A required run JSON is missing or unreadable.
- Any prompt requests payment, overage, top-up, or Nous purchased-balance.
- Any step would require writing outside your write root or mutating a source file.
- You are asked to infer a value the source does not state.

## Completion contract
When all three deliverables plus the receipt exist and every cell is either a verbatim source value or the literal `ABSENT`, write `…/reviews/goru/GORU_PACKET_A_RECEIPT.md` containing: files produced (with their SHA256), field/consistency summary, any STOP notes, and a final completion state — one of `DONE` / `PARTIAL` / `BLOCKED`. Never relabel `PARTIAL` or `BLOCKED` as success. End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_A_GORU_MECHMATRIX_COMPLETE_V1`

Done marker: TORI_GORU_DISPATCH_DONE_20260726T135248Z

```
