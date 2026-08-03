# HWAO COORDINATOR BRIEF — V4 paper-video correction: introductions and evidence plots

Timestamp: 2026-07-23T12:00:45Z
User direction: "the front page of the paper is not helping. and introduction and plots would be very helpful"

## Context

Five male-presenter V3 paper explainers were locally QA'd and then published public under the receipt:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z/final_publication_handoff.json`

The user has now identified a comprehension/design failure: showing the manuscript front page does not teach the paper. They prefer an actual introduction and useful plots.

## Hwao role

Coordinate and plan the correction first. Tori relays, records, verifies, and performs only later bounded actions that Hwao or the user explicitly directs.

## Read-only scope

Inspect only what is needed from:

- the V3 final/local/publication receipts and QA sheets;
- the V2/V3 video specs and renderers under `.hermes/handoffs/paper-videos-v2-*` and `.hermes/handoffs/paper-videos-v3-*`;
- the five frozen manuscript PDFs and any already-exported figure/data assets they reference;
- canonical repository source/data needed to verify a plotted quantity.

## Required decision packet

Write exactly one report:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v4-intro-plots-20260723T120045Z/HWAO_V4_INTRO_PLOTS_DIRECTION.md`

The report must:

1. Translate the user correction into an acceptance contract:
   - no manuscript cover-page-as-explanation;
   - opening establishes the scientific question in plain language;
   - plots are evidence-bearing and readable, not decorative;
   - each plotted visual is tied to a frozen figure/data source and one allowed claim;
   - presenter C + Michael voice + exact-audio lip-sync remain unless the user changes them;
   - descriptive/not-validated boundaries remain prominent.
2. Propose a reusable V4 scene grammar, preferably:
   - brief title hook;
   - problem/introduction;
   - method/sample;
   - two or three evidence plots with plain-English annotation;
   - interpretation/cross-check;
   - limitation/status recap.
3. Produce a paper-by-paper plot candidate map for all five papers with:
   - manuscript path;
   - figure/page or verified data asset;
   - what the axes mean in plain English;
   - exact claim supported;
   - any risk (tiny labels, absent raw data, calibration mismatch, visual inference beyond source).
4. Decide whether to crop manuscript figures or deterministically redraw them from verified data. Default to redraw only when the source values/series are fully recoverable; never invent geometry or synthetic points.
5. Recommend one highest-risk local canary and exact QA criteria before any batch rebuild.
6. State the ordered next gate and who should do each lane: Hwao coordinates, Lana reviews scientific/visual semantics, Goru mechanically inventories figures/pages/data assets, Kun checks reproducibility, Tori verifies receipts and executes only bounded directed work.

## Hard exclusions

- No video rendering or media generation.
- No YouTube upload, privacy update, deletion, or metadata mutation.
- No V1/V2/V3 visibility changes.
- No website/embed/cockpit mutation.
- No DB write, deploy, restart, cron, Git write, branch/worktree change, or public publication.
- Do not overwrite or alter any V3 artifact/checkpoint/receipt.

## Done marker

End the report with a standalone line:
`HWAO_V4_INTRO_PLOTS_DIRECTION_COMPLETE`
