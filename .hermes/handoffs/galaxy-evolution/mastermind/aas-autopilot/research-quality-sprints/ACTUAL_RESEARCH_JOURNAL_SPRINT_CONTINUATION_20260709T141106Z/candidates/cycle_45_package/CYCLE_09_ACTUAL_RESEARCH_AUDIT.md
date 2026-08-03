# Cycle 9 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_09`
Audit UTC: 2026-07-09T15:25:25Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=264222 sha256=b5c6bc6f6d2fba55456124fa1b207e4524126104c0db7abb228af8a1e1bdf095 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=552451 sha256=b71d22f0703515c7adbd44996a1658873cda677cbf9c19a2bddc9ed1ba7de705 bad_markers=[]

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
