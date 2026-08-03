# Cycle 30 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_30`
Audit UTC: 2026-07-09T18:08:00Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=269240 sha256=b462ad5f8d609a68f101524f8c371357903b1b624444f8f8e8916848a819a8fc bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=555968 sha256=34f8ae7abd9cc7f7d446ed4f2c1030276abea1ffbf7e6685310123b5fca639ec bad_markers=[]

## Guards
- flagship missing required phrases: ['non-random']
- supplement missing required phrases: []
- flagship missing numeric invariants: []
- forbidden mock/synthetic data-use hits flagship: []
- forbidden mock/synthetic data-use hits supplement: []

Fatal failures: 1

## Real-data policy
- Never use mock, synthetic, fake, placeholder, or toy data.
- Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.
- New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.
- If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.
- Literature-only sources may motivate future work; they do not become measured NebulaMind results.
- The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied.
