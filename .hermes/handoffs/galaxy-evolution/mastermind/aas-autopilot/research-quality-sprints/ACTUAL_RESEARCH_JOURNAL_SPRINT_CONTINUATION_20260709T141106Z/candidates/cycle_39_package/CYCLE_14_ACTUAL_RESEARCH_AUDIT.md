# Cycle 14 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_14`
Audit UTC: 2026-07-09T16:04:55Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=265316 sha256=25d39fab3fa5a9a9447ee95dbd8afb46f23318cd432d6460241f580d3923168c bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=552914 sha256=6c320a5c31d8aaa82c387d74ac4a2c0f991fe834cda38701b752393573c415d1 bad_markers=[]

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
