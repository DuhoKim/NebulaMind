# Public verification — all Galaxy Evolution topic AAS PDF links

Marker: `ALL_TOPICS_AAS_PDF_LINK_PUBLIC_VERIFY_20260708T130505Z`

## User request

Continue the actual-data AAS pilot manuscript workflow to all the other research topics and add the PDF links to the research-topic pages.

## Scope executed

- Kept the work in public/read-only survey data and local/static artifacts.
- Reused the public SDSS DR17 emission-line sample from the first AGN/sSFR pilot as the actual-data backbone.
- Generated 8 additional AAS-style pilot manuscripts for the remaining proposal cards.
- Linked all 9 proposal-card PDFs across the 3 public research-topic pages.
- Mirrored the working static changes to the live public root with backups.

Interpretation guard: several proposal cards require data not present in SDSS alone, such as radio jets, X-ray cavities, CO gas, resolved multiphase outflow velocities, or simulation mocks. Those manuscripts are explicitly bounded SDSS denominator/proxy pilots, not completed tests of the full physical claim.

## Public pages updated and verified

M1:
`https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`

M2:
`https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`

M3:
`https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`

Each page now has a visible `AAS pilot PDFs` callout with 3 proposal-specific manuscript links.

## PDF set

- `packet-gated-paper-to-wiki-reconciliation` RP-1: `sdss_agn_sfr_pilot_aas.pdf` — 234,931 bytes — `7f2832413b354023be6375e3a8c2bf4a9658c0791f9167a5056a9c5fc19d8e75`
- `packet-gated-paper-to-wiki-reconciliation` RP-2: `m1_rp2_environment_quenching_aas.pdf` — 59,070 bytes — `8eb4ae352e8b626829931d07587e7e38bc13a7bd3127d68d3aacacc38d44a339`
- `packet-gated-paper-to-wiki-reconciliation` RP-3: `m1_rp3_maintenance_heating_aas.pdf` — 59,204 bytes — `8a28f6a793de28384731209761d8c312ada7795ee44bd647510835e0fbdef86d`
- `source-first-paper-adjudication` P1: `m2_p1_outflow_escape_recycling_aas.pdf` — 288,385 bytes — `9314edd75a413aca99c2939f678b3f9341f1c326ccab8a6cef0af5d4850bd756`
- `source-first-paper-adjudication` P2: `m2_p2_radio_jet_environment_aas.pdf` — 58,906 bytes — `f5c19b612a5120832618c4c37cd6b9d35cdf4046f982730ce4d2ece1bc8ddd89`
- `source-first-paper-adjudication` P3: `m2_p3_feedback_transition_mass_aas.pdf` — 58,387 bytes — `e7969f69e82bc1c52bb4bf7ccb7675d449d815b1db9cab2d37d8f2e2952e1103`
- `debate-map-to-wiki-rebuild` P1: `m3_p1_multiphase_census_aas.pdf` — 59,116 bytes — `9ea6ab6c74bf655d3fbc7c016e7a34bedccb7038bde80b2acbfa8b375a6c24ba`
- `debate-map-to-wiki-rebuild` P2: `m3_p2_gas_depletion_efficiency_aas.pdf` — 182,955 bytes — `c0fb9f91ef31a771d70e36973c88b7cfb368755a859e2aad3d78fdad54938b20`
- `debate-map-to-wiki-rebuild` P3: `m3_p3_simulation_validation_aas.pdf` — 59,768 bytes — `9a9752cfd0eb4545e977c656dde56b001ed7b3bae30a78f2195255cf446bb266`

## Generated manuscript artifacts

Batch generator:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/run_remaining_topic_pilots.py`

Batch run root:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/`

Manifest:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json`

Page-link apply receipt:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/ALL_TOPICS_PDF_LINK_APPLY_20260708T130505Z.json`

## Verification results

PDF/manuscript verification:

- 8 new PDFs compiled successfully with Tectonic/AASTeX.
- 9 total PDFs now linked, including the earlier RP-1 PDF.
- Every compiled PDF exists, starts with `%PDF`, has nonzero size, and matches the recorded SHA256.
- Compile logs had no fatal errors; only small AASTeX line-breaking warnings.

Source/live static verification:

- Working root: 3/3 pages have 3 embedded PDF links.
- Live root: 3/3 pages have 3 embedded PDF links.
- Working root: all 9 copied static PDFs exist and match SHA256.
- Live root: all 9 copied static PDFs exist and match SHA256.
- Markdown links: 3/3 per page.
- Source HTML active-content safety: 0 scripts, 0 forms, 0 fetch/XHR/WebSocket/javascript URLs.

Public verification:

- Public page HTTP 200: 3/3.
- Visible `AAS pilot PDFs` text: 3/3.
- Embedded PDF download links: 3 per page, 9 total.
- Public decoded embedded PDFs: 9/9 start with `%PDF` and match the expected SHA256.
- Public response note: the fetched public HTML responses include 2 hosting-layer `<script>` tags; the working/live source HTML files contain 0 `<script>` tags.

Static PDF URL caveat:

Direct standalone public PDF URLs still return 404 from the already-running Next static server even though the PDF files exist in the live public root. To avoid a frontend restart, the visible page links use embedded `data:application/pdf;base64,...` downloads and preserve `data-static-href` for the normal static filename after any future static refresh.

## Backups

Working backup root:

`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/`

Live backup root:

`/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/`

## Safety boundary

No NebulaMind DB writes. No product SQL. No `/api/pages`. No page_versions/live wiki publish. No trust recompute. No deploy/restart. No git commit/push/merge. No cron. No billing/cloud/OAuth/API-key changes.

ALL_TOPICS_AAS_PDF_LINK_PUBLIC_VERIFY_20260708T130505Z
