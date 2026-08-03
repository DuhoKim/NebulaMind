# Cycle 6 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_06`
Audit UTC: 2026-07-09T14:57:35Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=263787 sha256=c408d5bfcef40be0242e7b09853427de60bc2b9d1ae316aa308e5773ddc832a9 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=551326 sha256=ed23ee080f5e4303c0e6451ccd73eee12211bb98ec9bf9737dd12472115c8153 bad_markers=[]

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
