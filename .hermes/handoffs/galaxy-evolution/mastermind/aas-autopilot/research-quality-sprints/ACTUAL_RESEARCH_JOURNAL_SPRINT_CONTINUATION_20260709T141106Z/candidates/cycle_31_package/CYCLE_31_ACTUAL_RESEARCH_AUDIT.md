# Cycle 31 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_31`
Audit UTC: 2026-07-09T18:16:23Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=269404 sha256=f8b6ac6926c57ba4c2c8e84d6614d893f72274e3ec18b8256630d402e33855d0 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=555994 sha256=4561055edc94310ed67eb7a685b09fb89300e15daeb2a3676c408d84c34cf253 bad_markers=[]

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
