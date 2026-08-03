# Hwao-director progress — research-topics proposal-style rewrite supervision

Marker: AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z
Role: Hwao-director — supervisor + final rollup (method teams rewrite; NOT director solo-author). Snapshot 2026-07-08T09:33Z (18:33 KST). Concurrent with the low-usage continuation (time-gated 10:31Z).

## Goal
The three topic autopilots rewrite their existing `research-topics-from-wiki-20260708T090359Z` pages (currently 8/10/9 jargonic topics) into **academic research-proposal style** — **5–8 polished proposal cards** each, plain language for an astronomy reader, overwriting the existing HTML/MD/JSON/manifest in place.

## Per-card requirements (verify)
Each proposal card: proposal title · research aim/central question · background+significance · a section titled **exactly `Survey/data plan`** (naming surveys/instruments/archives/sims the study would use — e.g. DESI, MOSDEF, JWST, ALMA, SDSS/MaNGA, Chandra/XMM/eROSITA, VLA/LOFAR, IllustrisTNG/HORIZON-AGN — **labeled proposed data, not existing evidence**) · study design · expected contribution · feasibility+caveats · a small end-of-card provenance line (claim/source IDs only there).
- Title `Galaxy Evolution — Research proposal agenda (Method X)`; plain-language note (proposed studies, not accepted claims / not product-bound).
- **Demote jargon** out of headings: claim IDs / cite-unmatched / P3 / bound-unbound / packet / lane / audit → plain phrasing.
- Static-safe (no script/fetch/XHR/WS/handlers/forms/external); product claim/cite comment counts **0/0**; no-invent.

## Method focus (per order)
- M1: internal AGN feedback vs environment/halo; observational tests for maintenance heating vs simulation-only; evidence-prioritization; metadata repair only as a methods appendix.
- M2: robustness of AGN-outflow claims to observations; out-of-model-dependence for maintenance heating; kinetic/radio-mode; M51 vs general; stellar vs AGN boundaries; gas removal vs recycling.
- M3: when AGN dominates vs halo/environment/stellar; comparable-denominator outflow prevalence; reservoir response; maintenance heating as an observational program; sim-to-obs validation; non-AGN alternatives completeness.

## Plan
Method teams rewrite + write `method<N>/autopilot/RESEARCH_TOPICS_PROPOSAL_STYLE_M<N>_20260708T093140Z.md` receipts (PASS/WARN/FAIL, files, proposal count, Survey/data-plan confirmation, 0/0 markers, static-safety, jargon before/after). Director independently verifies + writes the final rollup (status, per-method proposal counts, public-readability summary, static validation, live-root-mirror=0, and the exact next action if Tori should mirror M1 to public).

## Boundaries (CLOSED)
Overwrite allowed ONLY within the 3 `research-topics-from-wiki-20260708T090359Z/` dirs + `.hermes` receipts. NO live-root/mirror (method autopilots must not; Tori only on separate user approval), `:3000` restart/deploy, product DB/SQL/API, `/api/pages`, page_versions, publish, trust recompute, git, cockpit/global/shared-parent, cloud/OAuth/secrets, browser, cron, M3 P3. No director keystrokes; no solo authoring.

AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z
