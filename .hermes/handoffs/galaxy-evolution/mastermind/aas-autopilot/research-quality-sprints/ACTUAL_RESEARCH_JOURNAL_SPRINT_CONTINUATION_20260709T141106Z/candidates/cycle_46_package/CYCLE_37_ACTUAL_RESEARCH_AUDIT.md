# Cycle 37 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_37`
Audit UTC: 2026-07-09T19:04:51Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=270339 sha256=604054ca145b3c4ecc6d87323185d80d1b8f82f489cd7278bf61e09c802d2132 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=558275 sha256=77db6da0ff49ad347336c92dbde97d579adf230add51cf36477106cbec348d2c bad_markers=[]

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
