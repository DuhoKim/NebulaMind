# Tori -> Goru dispatch

Target: goru
Timestamp: 20260726T145946Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260726T145946Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# Goru — Packet D Brief: `fesc002` Acceptance-Readiness / Citation-Gate Coverage Checklist

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_D_GORU_FESC_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_D_GORU_FESC_READINESS_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at the C/D dispatch gate. Dispatched by: Tori (do not self-start).
- Lane: **existing Antigravity / agy Gemini subscription only** — no API-key, no GCP, no PAYG, no third-party route.
- This brief is standalone.

## Your role
Build an **acceptance-readiness / citation-gate coverage checklist** for `fesc002` (reionization ionizing-photon-budget). Mechanical checklist only — **no publication, no source edit, no prose patch**. You produce an isolated worksheet, not a modified draft.

## Allowed READ roots (read-only)
1. Immutable source lab-runs: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/` — `fesc002.json`, `fesc002/draft.tex`, `fesc002/draft.pdf`, `fesc002/review_loop.md`, `fesc002/result.png`. Nothing outside this run.
2. Baseline: `…/baseline/`.
3. Hwao decisions and this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverables ONLY under `…/packets/D-gap-closure/goru/`
- Receipt ONLY at `…/reviews/goru/GORU_PACKET_D_RECEIPT.md`
- Temp ONLY as `…/packets/D-gap-closure/goru/_tmp_*` (never TMPDIR, /tmp, scratchpad — the earlier /tmp incident must not recur).

## Forbidden (stop and report if any is required)
Run the live runner or re-pull data; edit or replace any source file or PDF; write any prose fix to the draft; write outside your write root; any public/DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance; Anthropic third-party PAYG routing. **No publication.** **Lane: existing Antigravity / agy Gemini subscription only — no API-key / GCP / PAYG / third-party route.**

## Tasks
1. **Acceptance-readiness checklist (verbatim from source).** Record: review verdict (`MINOR`, converged in 1 cycle) with the referee's stated minor concerns; gate verdicts verbatim — `novelty = NOVEL` (top-sim 0.784), `expected_value = TENSION` (`n_values=21`, `kill=false`), `citation_entailment` (`checked=0`, `n_unsupported=0`, `adversarial=true`); lit-grounding ("grounded on 6 papers, 5 passages"); the provenance string (literature-anchored budget; NO survey catalog data).
2. **Citation-gate COVERAGE check (the key gap).** Mechanically list every inline citation key used in the `draft.tex` body versus the formal reference list (`\section*{References}` / `lit_reflist`). Flag every cited-but-unlisted key. Known signal to VERIFY (do not assume): the body cites `[Chisholm+22, Flury+22; Simmonds+24]` and `[Muñoz2024, Davies2021]`; the reference list is `Muoz2024, Davies2021, Park2022, Duncan2015, Madau2017`. Determine which inline keys have no reference-list entry (expected: `Chisholm+22`, `Flury+22`, `Simmonds+24`). Also record explicitly that `citation_entailment.checked = 0` means the citation gate provided **zero positive entailment coverage** — "0 unsupported" is NOT "verified supported."
3. **Caveats presence.** Confirm mechanically that `draft.tex` has a Caveats section acknowledging proxy-calibration systematics and the absence of new survey data (present).
4. **Readiness verdict.** Enumerate what remains for acceptance readiness: resolve the cited-but-unlisted reference-coverage gap; note the citation gate ran zero checks (no positive coverage); note `TENSION` is carried as a systematic, not a contradiction. **Do NOT patch the draft** — checklist/worksheet only. **No publication.**

Deliverables under `…/goru/`: `FESC_READINESS_CHECKLIST.md` and `CITATION_COVERAGE.md` (+ optional `.csv`), each headed `AI_DRAFT_NOT_HUMAN_GOLD`.

## Stop conditions
Any temptation to patch the draft; source drift vs `INPUT_SHA256.txt`; any need for the runner or a data re-pull; a payment/overage/top-up/Nous/PAYG prompt; any need to write outside your write root or edit a source file.

## Completion contract
The honest readiness status of `fesc002` is **`PARTIAL`** (compiled, `MINOR`, lit-grounded — but an open cited-but-unlisted citation-coverage gap and a citation gate with zero positive coverage). Record it as `PARTIAL`, never relabeled as clean/ready. `reviews/goru/GORU_PACKET_D_RECEIPT.md` must list the deliverables' SHA-256, the readiness checklist summary, the citation-coverage findings, any STOP notes, and the completion state. End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_D_GORU_FESC_READINESS_COMPLETE_V1`

Done marker: TORI_GORU_DISPATCH_DONE_20260726T145946Z

```
