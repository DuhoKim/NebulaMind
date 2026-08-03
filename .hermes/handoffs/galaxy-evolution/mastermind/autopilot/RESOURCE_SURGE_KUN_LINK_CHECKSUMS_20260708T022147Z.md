# Kun link graph + checksum manifest

Marker: RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z

Status: WARN

## Scope

Inspected all 10 candidate files under:

`frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/evidence-trust-rebuild/`

Method: local shell/Python only. Computed byte counts and SHA-256, extracted HTML/Markdown `href` links, verified local relative targets exist, and listed external hosts separately. No network fetch was performed.

## Results Summary

- Candidate files inspected: 10
- Local relative href targets checked: 54
- Missing local relative href targets: 0
- Anchor-only hrefs: 14
- External hrefs found: 43
- Exact surge marker occurrences in candidate artifact bodies: 0
- Evidence-trust marker/string occurrences: 9 of 10 files
- WARN: `source-first-paper-adjudication/evidence-trust-rebuild/page-content-20260708T014205Z.md` has no `RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z` or evidence-trust marker string in its body.

## File Manifest

| Status | Path | Bytes | SHA-256 | hrefs | Local missing | Marker scan |
|---|---|---:|---|---:|---:|---|
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md` | 8091 | `45d1cc932083c91d903e799815ca77772789099cdc7eb57262ec0b5846e59947` | 0 | 0 | evidence-trust |
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md` | 17173 | `d908af489202ee08872352284f06fe6ae0235138fc09e4fd12e997364990542d` | 10 | 0 | evidence-trust |
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html` | 14920 | `5e9236f56226b7252299adcb0e270964d5e19ac30859a25b2d254645a2c9150f` | 22 | 0 | evidence-trust |
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-bindings-20260708T014205Z.md.json` | 17491 | `ea08877e9348f93bf8fe7671bf0fd634bc2a08448bd03b3399e52ec92865a024` | 0 | 0 | evidence-trust |
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html` | 37763 | `70564e0ba8144ef5f28328745ec56a6928a4431bea3ddb964f867cd426fdf19e` | 49 | 0 | evidence-trust |
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/manifest-20260708T014205Z.json` | 468 | `fc5238bcef58f34ed353bcf5b7af249da88e4a9f3b770ab985be25e95e5a90e7` | 0 | 0 | evidence-trust |
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json` | 7499 | `c9848105c1a279a1a888cb003844f9d5b16d39bbd534793b95218a4f6003f7df` | 0 | 0 | evidence-trust |
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/manifest.json` | 978 | `7cf79edc6d21eb81ac57125b9518babe8883e57ee4ca9a448f1d1b3a95bde36c` | 0 | 0 | evidence-trust |
| WARN | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/page-content-20260708T014205Z.md` | 14073 | `52cf8bfb422df8096da866a9144bcfa2d546fb42003e02e5630d22f6da255407` | 7 | 0 | missing marker string |
| PASS | `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/wiki-format-preview-20260708T014205Z.html` | 13531 | `6b106e5eb67798f5460a4a233eda933d0a7924883993ded8cc8ce5bc387fce92` | 23 | 0 | evidence-trust |

## Local Link Verification

PASS: all 54 local relative href targets exist. Repeated links resolved to:

- `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`
- `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.json`
- `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.html`
- `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.html`

## External Hosts

External href host list, not fetched:

- `arxiv.org` — 43 href occurrences, 26 distinct URLs:
  - `https://arxiv.org/abs/1108.0110`
  - `https://arxiv.org/abs/1203.2926`
  - `https://arxiv.org/abs/1301.3092`
  - `https://arxiv.org/abs/1301.3130`
  - `https://arxiv.org/abs/1308.5224`
  - `https://arxiv.org/abs/1507.06366`
  - `https://arxiv.org/abs/1606.03086`
  - `https://arxiv.org/abs/2008.00005`
  - `https://arxiv.org/abs/2009.11175`
  - `https://arxiv.org/abs/2112.07672`
  - `https://arxiv.org/abs/2401.12953`
  - `https://arxiv.org/abs/2403.17145`
  - `https://arxiv.org/abs/2501.00986`
  - `https://arxiv.org/abs/2508.06707`
  - `https://arxiv.org/abs/2511.02964`
  - `https://arxiv.org/abs/2512.05584`
  - `https://arxiv.org/abs/2512.21927v1`
  - `https://arxiv.org/abs/2603.18292`
  - `https://arxiv.org/abs/2604.15438`
  - `https://arxiv.org/abs/2605.03008`
  - `https://arxiv.org/abs/2605.25075`
  - `https://arxiv.org/abs/2605.31052`
  - `https://arxiv.org/abs/2606.03652`
  - `https://arxiv.org/abs/2606.25367`
  - `https://arxiv.org/abs/arXiv:0901.1880`
  - `https://arxiv.org/abs/arXiv:1712.04452`

## Safety Ledger

- Read-only/static verification only: yes
- Report writes only under `.hermes`: yes
- Product DB/SQL/page_versions/live wiki/API calls: 0
- Git/deploy/restart/browser/cloud/OAuth/secrets/cron/live publication actions: 0
- Writes into `NebulaMind-origin-main-live`: 0
