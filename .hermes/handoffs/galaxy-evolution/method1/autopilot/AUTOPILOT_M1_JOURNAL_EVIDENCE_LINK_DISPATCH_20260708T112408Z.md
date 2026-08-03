# Method1 autopilot — journal-prospectus evidence-link dispatch

Order marker: AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z
Lane: Hwao-m1. Class: BOUNDED DOCS/STATIC.

## Task (M1)
User correction: prior-studies sections still too casual/general and lack visible evidence links; must be journal-prospectus quality. Revise the M1 research-topic page in place so every proposal has a formal **Prior evidence** section with visible links INSIDE it (not just a trailing provenance line).

## Linkable evidence (from the local M1 ledger only — no invention)
`pgr-current-page-inventory-20260706T130610Z.json` attaches real arXiv records to the three evidenced claims:
- claim 2929 (internal AGN feedback): 8 distinct papers, all recorded non-committal (several arXiv-identifier only).
- claim 2931 (internal vs environmental quenching): 13 distinct papers, 4 supporting + 9 non-committal.
- claim 2946 (maintenance heating): 8 distinct papers, all supporting, predominantly simulation.
Malformed double-prefix arXiv URLs normalized (`/abs/arXiv:XXXX`→`/abs/XXXX`). For proposals whose prior-evidence is absent (narrative-only sections), mark as an unlinked limitation and link the local coverage-map artifact instead — do not fabricate support.

## Output (overwrite in place)
`…/research-topics-from-wiki-20260708T090359Z/` → `.html` + `.md` + `research-topic-map-…json` + `manifest-…json`.

## Verification
proposal count · prior-evidence link count per card · link resolution (arXiv well-formed + local artifact exists) · static safety (no script/fetch/handlers/forms/remote assets) · product claim/cite markers 0/0 · formal-tone scan.

## Receipt
`method1/autopilot/RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_M1_20260708T112408Z.md` (name per order).

## Gates closed
live-root write · DB/SQL · /api/pages · page_versions/publish · trust recompute · restart · deploy · git · cockpit/global · cloud/OAuth/secrets · browser · cron · M3 P3.

Status: **DISPATCHED** — building M1 journal-prospectus evidence-linked page.
