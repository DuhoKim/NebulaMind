# Kun Static Safety Check — Evidence/Trust Candidates

Marker: `RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z`
Report: `RESOURCE_SURGE_KUN_STATIC_SAFETY_20260708T022147Z`
Status: `WARN`

## Scope

Static/read-only inspection of all files under:

`frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/evidence-trust-rebuild/`

No live/API/DB/browser/git/deploy/cloud actions were performed.

## Inspected paths

1. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`
2. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md`
3. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html`
4. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-bindings-20260708T014205Z.md.json`
5. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html`
6. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/manifest-20260708T014205Z.json`
7. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json`
8. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/manifest.json`
9. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/page-content-20260708T014205Z.md`
10. `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/wiki-format-preview-20260708T014205Z.html`

Total files inspected: `10`; total bytes: `131987`.

## Static scan results

PASS:

- `<script>` tags: `0`
- `fetch(` calls: `0`
- `XMLHttpRequest`: `0`
- Actual `WebSocket` usage: `0`
- Inline `onclick` / `onload` / `on*=` handlers: `0`
- `/api/pages`: `0`
- `page_versions`: `0`
- SQL mutation strings with executable context: `0`
- External HTML anchors missing `rel="noopener"`: `0`

WARN:

- External links exist in Method1 evidence/trust candidate files.
- Domains found: `arxiv.org` only.
- Counts:
  - `evidence-trust-bindings-20260708T014205Z.md.json`: `43` stored `https://arxiv.org/...` URL fields.
  - `evidence-trust-preview-20260708T014205Z.html`: `43` external arXiv anchors, all with `rel="noopener noreferrer nofollow"`.

No non-arXiv external domains were found.

## False positives / non-issues

- `WebSocket` appears once in `evidence-trust-preview-20260708T014205Z.html` line 131 only inside a safety legend: `no &lt;script&gt;, no fetch/XHR/WebSocket, no /api or DB routes`. This is text, not code.
- SQL keyword regex matched ordinary prose:
  - `alter` in “alter the boundary conditions” / related prose.
  - `drop` in “drop the clause”.
  These are not SQL mutation statements.
- Escaped `&lt;script&gt;` appears only as safety-legend text, not an executable tag.

## Commands run

- `find frontend/public/agent-reports/wiki-method-results/galaxy-evolution -path '*/evidence-trust-rebuild/*' -type f | sort`
- `rg -n -i '<script\\b|fetch\\s*\\(|XMLHttpRequest|WebSocket|\\son[a-z]+\\s*=|/api/pages|page_versions|\\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|MERGE|UPSERT)\\b|https?://|href=["'\\'' ]https?://' frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/evidence-trust-rebuild`
- `find ... -exec wc -c {} +`
- `python3` read-only summary scripts for per-file counts and external-anchor rel checks.

## Verdict

`WARN`, not `FAIL`.

The candidates are static-safe for the requested indicators. The only warning is intentional external arXiv evidence links in Method1 candidate artifacts. No executable script, browser-network code, live page/API reference, page_versions reference, inline handler, or SQL mutation statement was found.

## Safety ledger

- NebulaMind-origin-main-live writes/copies: `0`
- `/api/pages` calls: `0`
- `page_versions`: `0`
- Product DB / SQL: `0`
- git: `0`
- deploy / restart: `0`
- browser automation: `0`
- cloud / OAuth / secrets: `0`
- cron: `0`
- live publication: `0`
- Writes: `1` report under `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/`
