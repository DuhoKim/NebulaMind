# Hwao-director progress — research-topics specificity pass supervision

Marker: AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z
Role: Hwao-director — supervisor + final rollup (method teams revise; NOT director solo-author). Snapshot 2026-07-08T10:59Z (19:59 KST).

## Goal
Revise the three existing `research-topics-from-wiki-20260708T090359Z` pages (currently general proposal agendas) into **specific, evidence-aware** agendas — each proposal card concrete enough to answer: what prior studies/source basis already find, what remains unknown, what exact measurement the study makes, which named data supply each measurement, and what test decides the result. Overwrite in place. Keep **5–8 cards** per method.

## Required per-card sections (verify each card has, or close equivalent)
1. `Research question` (one specific question) · 2. `What studies already show` (2–4 concrete findings from the method source basis, plain words, IDs out) · 3. `What remains unknown` (a direct gap: variable/scale/denominator/causal-link/population/redshift/gas-phase/selection) · 4. `Survey/data plan` (each data family **tied to a measurement** — e.g. SDSS/MaNGA/MUSE→resolved SF histories; ALMA→molecular gas/depletion; Chandra/XMM/eROSITA→cavities/cooling; VLA/LOFAR→jet power; DESI/COSMOS/Euclid/Rubin→matched denominators; JWST/MOSDEF→high-z outflows; TNG/HORIZON-AGN→forward-modeled counterfactuals labeled as sims) · 5. `Analysis/test` (the actual comparison) · 6. `Expected result/decision point` · 7. `Caveats` · 8. `Provenance` (IDs/labels only here).

## Hard constraints (verify)
- **No-invent:** no fabricated paper titles, DOI/ADS records, numeric findings, source IDs, or results. Weak/simulation-only support said so explicitly. "What studies already show" only for what the method page/source basis supports.
- Surveys labeled **proposed data to use**, not already-accepted evidence (unless the source says so).
- No internal jargon in headings (claim IDs, cite-unmatched, P3, bound/unbound-local, packet, lane, audit).
- Static-safe (no script/fetch/XHR/WS/handlers/forms/external links/hosts); product claim/cite comment counts **0/0**.

## Plan
Method teams revise + write `method<N>/autopilot/RESEARCH_TOPICS_SPECIFICITY_PASS_M<N>_20260708T105800Z.md` (PASS/WARN/FAIL, files, proposal count, section counts, ≥2 specificity before/after examples, static-safety, 0/0 markers). Director independently verifies + writes final rollup (status, per-method proposal+section counts, plain specificity summary, static validation, live-root-mirror=0, and the exact next action for Tori if public M1/M2/M3 mirrors should be refreshed post-verification).

## Boundaries (CLOSED)
Overwrite ONLY within the 3 `research-topics-from-wiki-20260708T090359Z/` dirs + `.hermes` receipts. NO live-root/mirror by autopilots (Tori only on the current instruction's narrow static refresh), restart/deploy, DB/SQL/API/`/api/pages`/page_versions/publish/trust-recompute, git, cockpit/global/shared-parent, cloud/OAuth/secrets, browser, cron, M3 P3. No director keystrokes; no solo authoring.

AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z
