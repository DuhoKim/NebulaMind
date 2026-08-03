# Method1 autopilot — research-topics specificity-pass dispatch

Order marker: AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Controller: Method1 Hwao. Class: BOUNDED DOCS/STATIC.

## Task (M1)
User: current proposal pages read too general. Revise the 6 M1 proposals so each answers, concretely: what prior studies/source rows already find · what remains unknown · what exact measurement the study makes · which surveys supply each measurement · what test decides it. Overwrite the existing `research-topics-from-wiki-20260708T090359Z/` set.

## Required 8-section card structure (§37)
Research question · What studies already show (2–4 grounded findings) · What remains unknown (specific gap) · Survey/data plan (each data family tied to a measurement) · Analysis/test (concrete comparison) · Expected result or decision point · Caveats · Provenance (claim/source IDs only here).

## Grounding (no invention, §31)
"What studies already show" phrased from what the M1 wiki actually reports: internal AGN regulation is non-committal (2929); internal-vs-environmental quenching is debated/split (2931); maintenance heating is simulation-reported not observed (2946); only 2 of 9 sections carry direct evidence; 43 records → 26 distinct studies. No invented titles/DOIs/numeric findings/source IDs.

## Output (overwrite)
`…/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/` → `.html` + `.md` + `research-topic-map-…json` + `manifest-…json`.

## Lane chain
Author → Kun generate → Goru mechanical (section counts, static-safety, product-binding=0, jargon scan, data-tied-to-measurement) → Kun validity → Hwao verdict/receipt `RESEARCH_TOPICS_SPECIFICITY_PASS_M1_20260708T105800Z.md`. Director rollup is mastermind (not this lane).

## Gates closed
live-root write · :3000 restart · DB/SQL · /api/pages · page_versions/publish · deploy · git · cockpit/global/shared-parent · cloud/OAuth/secrets · browser · cron · M3 P3.

Status: **DISPATCHED** — building M1 specificity revision.
