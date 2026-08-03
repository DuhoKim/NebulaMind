# Public verification — research-topic PDF link

Marker: `RT_PDF_LINK_PUBLIC_VERIFY_20260708T124436Z`

## User request

Add the link to the PDF on the research topic page.

## PDF linked

AAS-style pilot manuscript:

`A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts`

Source PDF:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.pdf`

PDF bytes: `234,931`

PDF SHA256:

`7f2832413b354023be6375e3a8c2bf4a9658c0791f9167a5056a9c5fc19d8e75`

## Pages updated

Working and live static roots were updated for all three Galaxy Evolution research-topic pages:

- Method 1: `packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- Method 2: `source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- Method 3: `debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`

Each page now has a visible `AAS pilot PDF` callout near the top.

## Implementation note

The PDF was copied into each current research-topic directory as `sdss_agn_sfr_pilot_aas.pdf` in both working and live roots.

Direct public static PDF URLs returned 404 from the already-running Next static server even though the files existed in the live root. To avoid a frontend restart, the visible HTML link uses an embedded `data:application/pdf;base64,...` download link, with `download='sdss_agn_sfr_pilot_aas.pdf'` and `data-static-href='sdss_agn_sfr_pilot_aas.pdf'` preserved for the normal static file path after any future static refresh.

## Public URLs verified

- `https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- `https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- `https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`

## Verification results

Source/static verification:

- Working root: 3/3 pages have embedded PDF download links.
- Live root: 3/3 pages have embedded PDF download links.
- Working root: 3/3 copied PDFs exist and match SHA256.
- Live root: 3/3 copied PDFs exist and match SHA256.
- Source HTML active-content safety: 0 scripts, 0 forms, 0 fetch/XHR/WebSocket/javascript URLs.

Public verification:

- Public page HTTP 200: 3/3.
- Visible `AAS pilot PDF` text: 3/3.
- Embedded download link found: 3/3.
- Decoded embedded PDF bytes: 234,931 on each page.
- Decoded PDF starts with `%PDF`: 3/3.
- Decoded PDF SHA256 matches expected: 3/3.

Public response note: the fetched public HTML responses included 2 `<script>` tags from the hosting/response layer; source files in working and live roots have 0 `<script>` tags.

## Backups

Live backup root:

`/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/`

Per-file local backups were also written in each working/live research-topic directory before the PDF-link edits.

## Safety boundary

No NebulaMind DB writes. No product SQL. No `/api/pages`. No page_versions/live wiki publish. No trust recompute. No deploy/restart. No git commit/push/merge. No cron. No billing/cloud/OAuth/API-key changes.

RT_PDF_LINK_PUBLIC_VERIFY_20260708T124436Z
