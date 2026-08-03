# Lana — 2913/2921 science & source-position verdict (docs-first, read-only)

Marker: `2913_2921_DOCS_FIRST_LANE_VERDICT_20260705T143217Z`
Task: `2913_2921_DOCS_FIRST_DISPOSITION_20260705T143217Z`
Scope honored: read-only. No SQL/apply/DB/prose/git/restart/deploy/rollback. No new SQL/apply artifacts created.

## Top-line verdict

- **Dispositions are already complete and epistemically SOUND.** Both were decided 2026-07-04 and executed/verified via `galaxy_2913_2921_exact_write_preflight_20260704T134546Z`; the fresh read-only snapshot confirms the executed state still holds (2948 exists; 2913 & 2921 `parent_replaced`; 26678/26679→2948; 26694→2546; dependency rows 0).
- **No remaining docs-only disposition gap.** The next safe docs-first workstream is therefore **full-text pinning / read-only source-hardening** (the brief's named alternate), not a new disposition.

## Source-position review (are the outcomes faithful to the sources?)

### Claim 2948 (scoped successor of 2913) — SOUND
Successor text scopes AGN-driven rapid quenching to "selected massive galaxies at cosmic noon (z≈1.5–3)… implicated in some observations and simulations… sample- and model-dependent pathway rather than a universal z∼2 rule."
- **26678 / 2605.31052v1 (COLIBRE II, simulation):** abstract identifies AGN feedback as the *primary* quenching mechanism, but "the two models behave differently" (thermal efficient at z>3; hybrid weaker; jet acts on *longer timescales*) → explicitly **model-dependent**. 2948's "simulations… model-dependent" hedge is faithful (and if anything slightly more conservative than the source, which is epistemically safe).
- **26679 / 2210.03747v2 (Park et al., observation + TNG100 analog):** 12 young QGs at z∼1.5; rapid-quench fraction ~4% (z=1.5) → 23% (z=2.2); AGN "most likely," "driven by AGNs" for the sample, mergers for half, authors "speculate." → **selected / sample-dependent, AGN implicated**. Matches 2948's wording.
- **Old 2913** ("quenching … by AGN feedback at z∼2 **is a rapid process**") was a universal overclaim the sources do **not** license. Retiring it and substituting the scoped 2948 is the sounder reading. ✔

### Claim 2921 → 2546 consolidation — SOUND
- 2921 was a near-duplicate of 2546 ("growth of central stellar mass density is linked to mass quenching").
- **26694 / 1308.5224v1 (Fang et al.):** "quenching is linked with an increase in Σ1"; Σ1 threshold grows with mass (∝M^0.64). Directly supports the central-density↔quenching link. ✔
- Structural/central-density evidence, **not** AGN-feedback evidence → correctly relocated out of the "Retrieval-Complete Evidence Claims"/AGN bucket onto 2546 in "Star Formation, Quenching & Color Bimodality." ✔
- **Preserved caveat is load-bearing:** source states a dense bulge is "necessary but not sufficient," quenching depends on inner-structure ↔ halo interplay, and "halo quenching does not require the presence of an AGN." 2546 must not be read as monocausal.

## Full-text pinning gaps (all closeable docs-only; full PDF text is already local)

Strength first: all three sources have full extracted text locally (2605.31052v1 23pp/114KB, 2210.03747v2 20pp/104KB, 1308.5224v1 22pp/106KB via `fitz`) — pinning needs **no re-fetch**.

1. **No per-evidence canonical pin.** Snippets are query-keyed retrieval spans, not a fixed `evidence_id → {verbatim_quote, page, char_offset}` anchor. Gap: designate one authoritative anchor quote per link (26678, 26679, 26694).
2. **No source-text immutability fingerprint.** Byte counts are recorded but no `sha256` per `*_pdf_text.txt` / `*.pdf`. Gap: record content hashes so pinned quotes are anchored to a frozen snapshot (this is exactly what a no-SQL pin checker would re-verify: `quote ∈ text` AND `hash(text)==pinned_hash`).
3. **Modality tag missing on the pin.** 26678 = simulation (COLIBRE); 26679 = observation + sim-analog (Park); 2948's "observations and simulations / model-dependent / sample-dependent" hedge should be traceable to *which* source supplies which modality. Gap: add `modality: sim|obs` to each pin.
4. **Caveat span not pinned for 2546/26694.** The "necessary-but-not-sufficient / halo interplay / no-AGN-required" caveat from 1308.5224v1 should be pinned as an explicit caveat quote so downstream prose can't drift to a monocausal reading.
5. **A few source pages un-snippeted.** snippet_pages < pdf_pages for 2605.31052v1 (19/23) and 2210.03747v2 (18/20). If a chosen anchor lands on an unindexed page, re-snippet from the already-local full text (no re-fetch).
6. **Retired-parent pin hygiene (already satisfied — verify in pinning pass).** 2913/2921 retain old text as `parent_replaced` with their evidence moved and dependency rows = 0, so no live evidence is pinned to the retired parents. Pinning pass should assert this stays true (0 active evidence on 2913/2921).

## Handable to next lane
A docs-only full-text pinning packet would emit a `claim ↔ evidence ↔ {quote,page,offset,modality,source_sha256}` table for {2948:[26678,26679], 2546:[26694]} plus the 2546 caveat quote — read-only, verifiable by a no-SQL checker (Kun), no DB/prose writes. No fresh disposition needed; any future DB/prose/git action still requires a new explicit packet.

Verdict: **PASS — dispositions complete & source-faithful; proceed to full-text pinning; gaps above are docs-only.**
