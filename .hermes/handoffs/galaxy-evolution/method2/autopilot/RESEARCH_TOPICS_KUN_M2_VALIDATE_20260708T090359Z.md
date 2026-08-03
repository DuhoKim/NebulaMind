# Kun M2 research-topic HTML validation receipt

Marker: `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z`

Status: WARN

## Scope

Executed only the `Kun M2 — HTML builder/validator` lane from:

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESEARCH_TOPICS_HELPER_LANE_BRIEFS_20260708T090359Z.md`

Validated existing Method2 artifacts rather than overwriting them.

## Exact source wiki file(s) inspected

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/autopilot/RESEARCH_TOPICS_GORU_M2_SEED_20260708T090359Z.md`

## Exact artifacts validated

Output directory:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/`

Files:

| File | Bytes | sha256 |
| --- | ---: | --- |
| `research-topics-from-wiki-20260708T090359Z.html` | 17387 | `b5dc1b344bf855530c37ce22e72f595a1cc661db148dbd623223452a337b7f19` |
| `research-topics-from-wiki-20260708T090359Z.md` | 10214 | `eff3e105489a51a0799376ff07da9344d5c1c35980d2ce3959a95bc2ab2822a9` |
| `research-topic-map-20260708T090359Z.json` | 9155 | `7516023547e3b53926a5430ef7828a2c0a5cc47c63e1db06babefe1419c0598a` |
| `manifest-20260708T090359Z.json` | 695 | `17b44be0a5db99cf14cf7606ffbb396ea7a1a6838efb54da1ad57d817e13513c` |

## Validation results

- Topic count: 10 in JSON, 10 topic sections in HTML.
- JSON parse: PASS for `research-topic-map-20260708T090359Z.json` and `manifest-20260708T090359Z.json`.
- Parent marker presence: PASS in HTML, JSON, and manifest; WARN in Markdown because `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z` is absent.
- Product claim/cite comment counts in created HTML: `product_claim_comments=0`, `product_cite_comments=0`.
- Product claim/cite comment counts in inspected source HTML: primary `0/0`, comparison `0/0`.
- Relative link check: PASS, 4 local relative links resolved, 10 same-page anchors, 0 missing, 0 external links.
- Active HTML safety result: PASS, no `script`, `iframe`, `form`, `fetch(`, `XMLHttpRequest`, `WebSocket`, inline event handlers, or external assets.
- Manifest consistency: PASS for listed filenames, topic count, source wiki, static-safe declaration, and hard-gates declaration.

## WARN basis

The Markdown artifact is otherwise present and consistent with the topic packet, but it does not include the required parent marker. I did not edit the existing artifact because this lane instructed Kun to validate rather than overwrite if Hwao had already created the files.

## Safety ledger

- Hard-excluded surface touched: 0.
- Live-root writes/copies: 0.
- Restart/deploy/service mutation: 0.
- Product DB/SQL, `/api/pages`, page-version records, live publish: 0.
- Git actions: 0.
- Cloud/GCP/API/billing/OAuth/token/secret/cookie access: 0.
- Browser automation: 0.
- Cron: 0.
