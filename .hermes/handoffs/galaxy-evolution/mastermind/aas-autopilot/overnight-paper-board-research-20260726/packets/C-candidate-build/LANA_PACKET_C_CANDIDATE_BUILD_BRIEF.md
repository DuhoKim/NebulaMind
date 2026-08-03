# Lana — Packet C Brief: Isolated Candidate Build (two approved targets)

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_C_LANA_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_C_LANA_CANDIDATE_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at the C/D dispatch gate. Dispatched by: Tori (do not self-start).
- Lane: **direct Claude subscription only** — no API-key, no PAYG, no third-party route, no Nous purchased-balance.
- This brief is standalone. It implements Hwao's `HWAO_PACKET_A_CANONICAL_DECISION_V1` and `HWAO_PACKET_B_FINAL_DECISION_V1`.

## Your role
Build TWO isolated Packet C deliverables, nothing published:
- **C1 — `2ab3c92eea8a`: STRUCTURAL OUTLINE ONLY, with NO synthetic results.**
- **C2 — canonical `gated-e2e-demo`: isolated AASTeX candidate** from source artifacts + Lana's verified split + mandatory caveats.

## Allowed READ roots (read-only)
1. Immutable source lab-runs: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/` —
   - `gated-e2e-demo/draft.tex`, `gated-e2e-demo/result.png`, `gated-e2e-demo.json`
   - `2ab3c92eea8a.json`, `2ab3c92eea8a/result.png`, `2ab3c92eea8a/history.json`
2. Baseline: `…/baseline/`.
3. Your own split candidate `packets/B-citation-integrity/lana/candidates-lana/gated-e2e-demo.split.md`; Kun's map + Goru's cross-check for context; `reviews/hwao/HWAO_PACKET_A_CANONICAL_DECISION.md` and `reviews/hwao/HWAO_PACKET_B_FINAL_DECISION.md`; this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverables ONLY under `…/packets/C-candidate-build/lana/` — use subfolders `c1-sfms-2ab-outline/` and `c2-mzr-gated-e2e-candidate/`.
- Receipt ONLY at `…/reviews/lana/LANA_PACKET_C_RECEIPT.md`.
- Temp ONLY as `…/packets/C-candidate-build/lana/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Forbidden (stop and report if any is required)
Run the live runner or re-pull any TNG/SDSS/obs data; edit or replace any source file or existing PDF; write outside your write root; introduce any new scientific number, relation, or claim beyond what the source states; any public/static-root, DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance; Anthropic third-party PAYG routing. **No publication.** **Lane: direct Claude subscription only.** Compile (C2) ONLY inside your candidate root.

## C1 — `2ab3c92eea8a` structural outline (NO synthetic results)
Source facts (the ONLY things the source provides): `method = star-forming main sequence (scaling-relation-evolution, median relations)`, `data = TNG100`, `N = 23,060 galaxies`, one figure `result.png`, `spec.outputs = []` (no draft was ever produced), summary = "Star-forming main sequence — median relations for TNG100 (23,060 gals)."
- Produce a **structural outline** (section skeleton: Title placeholder, Abstract placeholder, Introduction, Data & Method, Result, Caveats) that scaffolds an SFMS paper.
- **NO synthetic results.** Every quantitative slot (slope, normalization, scatter, turnover mass, any SFR/M⋆/O/H value) must read literally `TO BE COMPUTED — NOT IN SOURCE`. You may state only the three source facts above and reference the existing `result.png`. Invent no relation, number, slope, or finding.
- Deliverable: `c1-sfms-2ab-outline/OUTLINE.md`, headed `AI_DRAFT_NOT_HUMAN_GOLD` and `STRUCTURAL OUTLINE — NOT A CANDIDATE PAPER; NO SYNTHETIC RESULTS`.

## C2 — `gated-e2e-demo` canonical isolated AASTeX candidate
- **Base text:** the source `gated-e2e-demo/draft.tex`, with the Introduction citation form REPLACED by your VERIFIED split (four single-citation sentences; all 5 reference entries retained, incl. `LaraLopez2013`). Use ONLY source artifacts + the split. Introduce no new number/claim.
- **Mandatory caveats** (place in the Caveats section; do not weaken existing caveats):
  - **O/H-scale:** SDSS O/H calibration/scale is ABSENT in source; no common TNG-vs-SDSS O/H scale is established; scales may differ; **no dex offset may be invented or applied**; TNG-vs-SDSS metallicity comparability is **unresolved**; any TNG−SDSS difference is scale-limited/systematic, not physical. (State no specific external offset value — none exists in source.)
  - **TENSION:** carry the source `expected_value = TENSION` honestly; frame as a systematics/anchor reconciliation, not a novel physical MZR claim (a z~0 TNG-vs-SDSS MZR is an anchor relation).
  - **Forced/demo provenance:** disclose that the candidate's lineage is the forced (`spec.force=true`) `gated-e2e-demo` end-to-end build and that `d8de519cb9c9`'s independent draft was queued but never compiled; the candidate is assembled from existing artifacts, not a fresh production run.
- **Figure:** copy the source `result.png` into `c2-mzr-gated-e2e-candidate/` (read source → write a copy to your root) and `\includegraphics` the local copy; never modify the source figure.
- **Compile (optional, root-local only):** a TeX engine is available locally — `tectonic` is present (`pdflatex`/`latexmk` are not). Attempt a PDF compile with `tectonic` INSIDE `c2-mzr-gated-e2e-candidate/` only. If it succeeds, include `candidate.pdf`. If `tectonic` cannot fetch `aastex631`/packages or otherwise fails, deliver `candidate.tex` + `COMPILE_NOTE.md` recording the exact outcome — **this is NOT a failure state**. Never invoke the Lab runner; never write outside the candidate root.
- Deliverables: `c2-mzr-gated-e2e-candidate/candidate.tex`, the copied `result.png`, `candidate.pdf` (if compiled), `COMPILE_NOTE.md`. All science artifacts headed `AI_DRAFT_NOT_HUMAN_GOLD`. Candidate is isolated; **no publication**.

## Stop conditions
Any need to invent a number/relation/claim (especially C1); source drift vs `INPUT_SHA256.txt`; any need for the runner or a data re-pull; a compile that would write outside the candidate root; a payment/overage/top-up/Nous/PAYG prompt; any public or source mutation.

## Completion contract
When C1 outline and the C2 candidate (`.tex` + figure copy + optional PDF + compile note) exist under your write root and `reviews/lana/LANA_PACKET_C_RECEIPT.md` lists their SHA-256, per-target status (C1: DONE/PARTIAL; C2: DONE with-or-without compiled PDF / PARTIAL), a caveats-applied confirmation, the compile outcome, any STOP notes, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success), end the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_C_LANA_CANDIDATE_COMPLETE_V1`
