# Cycle 48 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_48`
Audit UTC: 2026-07-09T20:26:52Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=273478 sha256=8763ae69cf5ca43ece50ee741ccc728a2caa7a6b4f96ec1973da56bc0c9e1d01 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=559720 sha256=302c969f47f6dd5a2052c859683d54060f88732b0d74afe775a1f7a89eb54c8b bad_markers=[]

## Guards
- flagship missing required phrases: []
- supplement missing required phrases: []
- flagship missing numeric invariants: []
- forbidden mock/synthetic data-use hits flagship: []
- forbidden mock/synthetic data-use hits supplement: []

Fatal failures: 0

## Real-data policy
- Never use mock, synthetic, fake, placeholder, or toy data.
- Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.
- New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.
- If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.
- Literature-only sources may motivate future work; they do not become measured NebulaMind results.
- The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied.
