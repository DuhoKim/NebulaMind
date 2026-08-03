# Method1 autopilot — EVIDENCE/TRUST LINKING dispatch status

Order marker: AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Controller: Method1 Hwao (autonomous). Class: BOUNDED DOCS/STATIC, additive candidate under `evidence-trust-rebuild/`.

## Problem (Method1)
M1 same-format page has 30 claim chips but 0 evidence links and no visible trust leveling.

## Real local evidence available (no invention)
Source of record: `…/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.json` (`watch_claim_evidence_raw`).
- **3 of 30 on-page chips have full local evidence + trust:** 2931 (debated, 20 evidence rows), 2929 (unverified, 14 rows), 2946 (reported, 9 rows) — each row has title/arxiv_id/url/stance/votes/quality, all on-topic and claim-associated.
- **27 of 30 chips have NO local per-claim evidence** — their trust/evidence lives in the product claim/evidence layer (closed gate). These will be labeled **unbound-local**, not invented.
- Product **cite IDs** are not locally resolvable → I will NOT inject `<!--cite:-->` markers into page.content (inventing IDs is forbidden). Evidence/trust is delivered as a static rendering overlay + an auditable bindings sidecar linking to the local ledger and the real arxiv URLs.

## Lanes dispatched
- Lana/Kun (content+shell): build the enriched static candidate under `evidence-trust-rebuild/` — trust badges on the 3 bound chips, per-claim evidence panels, page/section trust summary, honest unbound labels, links to the local ledger + real arxiv URLs. Static-safe (no script/fetch/API/DB).
- Goru: mechanical checks (href counts, evidence-ish hrefs, trust chips, unbound labels, no-script/API/fetch scan, files exist/non-empty, old pages preserved).
- Tori receipt → Hwao verdict → contribute to final no-apply packet.

## Hard gates closed
DB/SQL · /api/pages · page_versions/publish · live-root write · deploy/restart · git · cockpit/shared-parent · cloud/OAuth/secrets · browser · cron · M3 P3. Only additive `.hermes` + working-repo `evidence-trust-rebuild/` static candidates.

Status: **DISPATCHED** — building M1 evidence/trust static candidate.
