# Kun — Packet D Brief: `7cb504ea7ad3` Evidence-Closure / Reproducibility Worksheet

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_D_KUN_7CB_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_D_KUN_7CB_GAP_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at the C/D dispatch gate. Dispatched by: Tori (do not self-start).
- Lane: **standalone ChatGPT Codex gpt-5.5 Pro subscription only** — no API-key, no PAYG, no third-party route.
- This brief is standalone.

## Your role
Build an **evidence-closure / reproducibility worksheet** for `7cb504ea7ad3` (IllustrisTNG z=0 stellar mass function). Mechanically recover the actual verdict language — **do NOT infer a missing single-token verdict**. Document the acceptance-gap ledger. **Write NO prose patch for any gap whose source evidence is missing.** This is a documentary worksheet, not a draft rewrite.

## Allowed READ roots (read-only)
1. Immutable source lab-runs: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/` — `7cb504ea7ad3.json`, `7cb504ea7ad3/draft.tex`, `7cb504ea7ad3/draft.pdf`, `7cb504ea7ad3/review.md`, `7cb504ea7ad3/history.json`, `7cb504ea7ad3/result.png`. Nothing outside this run.
2. Baseline: `…/baseline/`.
3. Hwao decisions and this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverables ONLY under `…/packets/D-gap-closure/kun/`
- Receipt ONLY at `…/reviews/kun/KUN_PACKET_D_RECEIPT.md`
- Temp ONLY as `…/packets/D-gap-closure/kun/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Forbidden (stop and report if any is required)
Run the live runner or re-pull TNG/observational data; edit or replace any source file or PDF; **write any prose fix that fabricates missing evidence** (obs comparison, error model, bias analysis); write outside your write root; any public/DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance; Anthropic third-party PAYG routing. No publication. **Lane: standalone ChatGPT Codex gpt-5.5 Pro subscription only — no API-key / PAYG / third-party route.**

## Tasks
1. **Verdict-language recovery (verbatim).** Quote the source review verdict EXACTLY from `review.md` / `result.review`. Note explicitly that `7cb504ea7ad3` uses a **prose** verdict ("…requires substantial improvement before publication"), NOT a single-token verdict (`MINOR`/`MAJOR`/`CONTRADICTS`). Do NOT infer, assign, or normalize a token the source does not contain.
2. **Evidence inventory (documentary; no recompute).** List the numeric/figure evidence the source actually contains and whether each is internally traceable: the single SMF number `n(>10^10.5 M⊙) = 1.49e-3 Mpc^-3`, `N = 203,524` galaxies, box `(111 Mpc)^3`, figure `result.png`. Confirm each traces to the summary/title/abstract. Do not recompute from catalogs.
3. **Acceptance-gap ledger.** For each referee-identified gap, mark source-evidence `PRESENT` / `ABSENT`:
   - comparison to observational data (SDSS/GAMA/COSMOS) — expected `ABSENT`
   - error analysis / uncertainty quantification — expected `ABSENT`
   - selection / stellar-mass bias discussion — expected `ABSENT` (the draft's Caveats mentions default selections / no completeness modelling, but performs no bias analysis)
   Verify each against `draft.tex` + `review.md` rather than assuming.
4. **Closure assessment.** State, per gap, whether it can be closed WITHOUT new source evidence. Closing them requires obs catalogs / an error model / bias modelling that are NOT in the immutable source and cannot be produced without the runner or a data pull (both forbidden). Record each such gap as `OPEN — uncloseable tonight without new source evidence`. Per the mandate, produce **no prose patch** for these.
5. **Reproducibility note.** The single stated number is documentarily traceable; the study is a bounded descriptive first-pass (its own Caveats say "a starting point, not a validated measurement").

Deliverables under `…/kun/`: `EVIDENCE_CLOSURE_WORKSHEET.md` and `ACCEPTANCE_GAP_LEDGER.md` (or one combined file), each headed `AI_DRAFT_NOT_HUMAN_GOLD`.

## Stop conditions
Any temptation to write a prose patch for a missing-evidence gap; source drift vs `INPUT_SHA256.txt`; any need for the runner or a data re-pull; a payment/overage/top-up/Nous/PAYG prompt; any need to write outside your write root or edit a source file.

## Completion contract
Because the referee gaps are uncloseable tonight without new source evidence (forbidden to generate), the honest acceptance status of `7cb504ea7ad3` is **`BLOCKED`** (needs new evidence via a future gated runner/data step, out of scope tonight) — record it as `BLOCKED`, never relabeled as success. `reviews/kun/KUN_PACKET_D_RECEIPT.md` must list the deliverables' SHA-256, the verbatim recovered verdict, the gap ledger, the closure assessment, any STOP notes, and the completion state. End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_D_KUN_7CB_GAP_COMPLETE_V1`
