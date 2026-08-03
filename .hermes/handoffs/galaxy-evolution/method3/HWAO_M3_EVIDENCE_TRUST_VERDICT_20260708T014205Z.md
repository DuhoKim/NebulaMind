# Hwao-m3 method verdict — evidence links + trust leveling (Method3)

Order marker: `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z`
Continuation marker: `GE_AUTOPILOT_IDLE_CONTINUATION_V1`
Role: Method3 Hwao — autonomous method controller. Method verdict after authoring + verifying the docs-only evidence/trust candidate. **NO-APPLY, no product binding.**

## VERDICT: READY_FOR_USER_APPROVAL (Method3)

M3's page had 0 hrefs and 0 trust wording. This lane adds a **docs-only, static-safe evidence + trust layer** — honest to M3's P2 scope — as additive working-repo candidates. No product claim/citation binding was created (that stays a separate CLOSED P3 gate) and nothing was mirrored to the live root (that stays a separate approval gate).

## What was added (working-repo candidates, `debate-map-to-wiki-rebuild/evidence-trust-rebuild/`)

1. `page-content-evidence-trust-20260708T014205Z.md` (17,173 B) — the verified 9-H2 narrative + a **page-level trust summary** + **per-section trust chips** + **per-section evidence-basis links**.
2. `evidence-basis-20260708T014205Z.md` (8,091 B) — the **local provenance & trust ledger** the section links point to: real axis statuses, per-section source/claim IDs, atlas trust-level counts, and explicit unmatched items.
3. `wiki-format-preview-evidence-trust-20260708T014205Z.html` — self-contained **static preview** rendering the trust summary panel, per-section trust chips, and clickable evidence-basis panels.

## Trust leveling (plain-English, visible, non-invented)

Trust = the **real debate-map status** of each section's axes (from `status_debate_map.json`), rendered as chips:
- `widely_supported` → "widely supported" (mechanism, alternatives)
- `emerging_sample_limited` → "emerging / sample-limited" (outflow prevalence)
- `actively_debated` → "actively debated" (dominance, reservoir response)
- `contradicted_or_model_dependent` → "model-dependent" (maintenance heating, simulation scope)
- gap sections → "scoped coverage-extension" (halos, morphology, chemical enrichment, reionization)

A page-level summary panel states plainly: this is a docs-only P2 narrative; trust = debate-map status (not a product trust score); **0 product claim/cite markers by design**; product binding is a CLOSED P3 gate; baseline caveat = debate map `PENDING_RECHECK`.

## Evidence links (useful, static-safe, local)

Each section has an "Evidence basis →" link to the corresponding anchor in the local provenance ledger (`evidence-basis-…md#s1…#s9`), which lists the **real** source/claim IDs already present in `evidence_source_inventory.json` / `debate_map_data.json` (verified by Kun's P2 repro). 11 clickable local links + 9 sidecar anchors. **No live API/fetch/scripts/external URLs** (all static-safety counts 0). Known unmatched items are shown as explicit **unbound/unmatched** labels, not hidden:
- `2915 / 2921 / 2913` — v1709-body-only, re-resolve at P3.
- `2133 → 2605.22497` — true source missing from the listed set (add or restrict at P3).
- `2374` — garbled `claim_text`, does not support the EoR-seeding clause (repair/drop at P3).

## Conformance + safety (Goru PASS, Tori PASS)

9 article `<h2>` (exact order), TOC `<h3>Contents</h3>`, trust-summary heading `<h3>` (raw `<h2>` count == 9, no chrome leak), 0 product claim/cite markers, 0 scripts/fetch/API/DB/external-URL. Old `wiki-page.html` + `same-format-rebuild/` preview preserved. Nothing invented; no product binding. Evidence: `autopilot/GORU_M3_EVIDENCE_TRUST_CHECK_20260708T014205Z.md` (PASS) + `receipts/TORI_M3_EVIDENCE_TRUST_RECEIPT_20260708T014205Z.md` (PASS).

## Honest limits (what M3 does NOT claim)

- No product claim chips / cite chips were added — M3 stays docs-only P2. Turning the local provenance into product `<!--claim:-->`/`<!--cite:-->` bindings is the **P3 gate** (fresh snapshot + Goru re-check + user approval + resolve the 3 unmatched items + PENDING_RECHECK).
- The candidates are **working-repo only** → they 404 on :3000 (which serves the live root). Making them visible requires the separate live-root mirror gate.

## User approval gate (Method3 portion)

> "Approve mirroring the 3 Method3 evidence+trust candidate files (`evidence-trust-rebuild/`) from the working repo into the live-served repo so the trust chips + evidence-basis links become visible on :3000. Static copy, no build/deploy/restart/git/DB/`/api/pages`/`page_versions`/product-wiki publish; reversible. Product claim/citation (P3) binding remains a separate gate."

## Report to Hwao-director

Method3 evidence+trust candidate COMPLETE and READY_FOR_USER_APPROVAL. Provides the M3 inputs (paths, checks, PASS) for the director's cross-method final no-apply packet. Method-local separation preserved; live root untouched; no shared-parent write by this lane.

## Safety ledger

Read-only inspection of local ledgers + additive candidate authoring under the order-named working-repo subdir + method-local `.hermes` writes (progress, Goru check, Tori receipt, this verdict). Zero live-root writes; zero product DB/SQL, `/api/pages`, `page_versions`, live-wiki publish, deploy/restart, git, cockpit/global/shared-parent, cloud/GCP/OAuth/secrets, browser, cron; zero Method3 P3 binding; zero invented evidence/cite/claim/source IDs/DOI/ADS links/trust levels.

## Stop state

Method3 method verdict issued: READY_FOR_USER_APPROVAL, docs-only evidence+trust candidate authored + verified (Goru/Tori PASS), honest to P2 scope, static-safe, no product binding, live root untouched. Hwao-m3 stopping after this method verdict; the cross-method final no-apply packet is the director's aggregation step.
