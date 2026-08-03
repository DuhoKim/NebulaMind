# Cycle 2 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_02`
Audit UTC: 2026-07-09T13:30:22Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=261361 sha256=2bf6eaec69bc40a6ae64c93e78686cb26624735af54c40834ba64049c21a6e7a bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=548889 sha256=07c7b92eaea3c34ecb3542b676f3806d0afac6e68b983ddb79025259da2b8070 bad_markers=[]

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
