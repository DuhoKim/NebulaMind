# Lana — C2 Scientific / Representation Red-Team Brief (read-only)

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_REDTEAM_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_REDTEAM_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at Deepening Gate 1. Dispatched by: Tori (do not self-start).
- Lane: **direct Claude subscription only** — no API-key, no PAYG, no third-party route, no Nous purchased-balance.
- This brief is standalone. **READ-ONLY review — you make NO edits to the C2 candidate or any other file.**

## Your role
Adversarially red-team the C2 candidate (`gated-e2e-demo` MZR) for **scientific honesty and representation**: does it overclaim, over-represent, or mis-frame relative to what the source artifacts actually support? Are the caveats sufficient and honest? Are the AI-draft / forced-demo / TENSION / unresolved-calibration disclosures visibly rendered? You produce findings + recommended (NOT applied) changes. Kun runs a separate mechanical contract audit in parallel; yours is the scientific/representation lens.

## Allowed READ roots (read-only)
1. C2 candidate: `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/candidate.tex`, `candidate.pdf`, `COMPILE_NOTE.md`.
2. Source (for comparison): `/Users/duhokim/…/lab-runs/gated-e2e-demo/draft.tex`, `gated-e2e-demo.json`, `gated-e2e-demo/result.png`.
3. Baseline; `reviews/hwao/HWAO_PACKET_A_CANONICAL_DECISION.md`, `HWAO_PACKET_B_FINAL_DECISION.md`, `HWAO_ABCD_FIRSTPASS_ROLLUP.md`; your own `reviews/lana/LANA_PACKET_C_RECEIPT.md`; `reviews/tori/TORI_CD_FIRSTPASS_VALIDATION.md`; this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverable ONLY under `…/packets/C-candidate-build/lana-c2-redteam/`
- Receipt ONLY at `…/reviews/lana/LANA_C2_REDTEAM_RECEIPT.md`
- Temp ONLY as `…/packets/C-candidate-build/lana-c2-redteam/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Forbidden (stop and report if any is required)
Edit or rewrite `candidate.tex`/`candidate.pdf` or ANY other file (this is a read-only review); run the live runner; recompile or replace the candidate; introduce any new source/citation/claim; any public/static-root, DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance; Anthropic third-party PAYG routing. **No publication.** **Lane: direct Claude subscription only.**

## Tasks (produce findings; recommend, do not apply)
1. **Representation review.** Does the candidate anywhere state or imply it is a validated measurement, an accepted/peer-reviewed paper, or human-authored? Check title, author/affiliation, abstract, body, caveats, and the rendered PDF. Flag any over-representation. (Note the abstract says "bounded, reproducible, descriptive study"; author = "NebulaMind Lab (autonomous pipeline)" — judge whether the honest-labelling is sufficient and consistent.)
2. **Claim-surface / overclaim review.** Enumerate every scientific claim in the body (Abstract, Data-and-method, Result). For each, mark whether it is supported by the source artifacts (the summary "median relations for TNG100 23,722 + SDSS 120,000; TNG SF-weighted O/H solar-scaled" + the figure) or an overreach. Flag phrases such as "provides insights into the relationship…" if they assert more than a descriptive median-relation comparison. Any claim beyond source = finding.
3. **Caveat sufficiency & honesty.** Confirm the O/H-scale, TENSION, and provenance caveats are present, honest, and non-weakening. Verify the O/H caveat avoids asserting the difference is physical OR definitively systematic (bounded "confounded … cannot be interpreted as physical until a common calibration is established"). Verify TENSION is carried, not upgraded. Flag any caveat that is too weak, too strong, or missing.
4. **PDF disclosure visibility.** By reading the rendered `candidate.pdf` text, confirm the AI-draft (`AI_DRAFT_NOT_HUMAN_GOLD`), forced/demo-lineage, TENSION, and unresolved-calibration disclosures are **visibly rendered** (not only in non-rendered `%` comments). Flag any disclosure that exists only as a comment.
5. **Anchor/frontier honesty.** Judge whether the framing as an anchor / systematics-reconciliation note (not a frontier or novel-physical claim) is honest per the owner's publishable bar. Flag if the candidate reads as a stronger result than the source supports.

## Deliverable
`packets/C-candidate-build/lana-c2-redteam/SCIENCE_REDTEAM_REVIEW.md` — a findings table (`issue`, `location` [file+section], `severity` = `BLOCKER`/`MAJOR`/`MINOR`/`OK`, `supported_by_source?`, `recommended_change` [explicitly NOT applied]), plus an overall representation verdict: is the candidate honestly labelled as an AI research-note draft, and is it free of scientific overclaim? Headed `AI_DRAFT_NOT_HUMAN_GOLD`.

## Stop conditions
Any temptation to edit the candidate; source drift vs `INPUT_SHA256.txt`; any need for the runner/recompile; a payment/overage/top-up/Nous/PAYG prompt; any need to write outside your write root.

## Completion contract
`reviews/lana/LANA_C2_REDTEAM_RECEIPT.md` must list the deliverable's SHA-256, a finding count by severity, the overall representation verdict, an explicit "no candidate edits made" attestation, any STOP notes, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success). End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_REDTEAM_COMPLETE_V1`
