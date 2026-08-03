# Cycle 3 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_03`
Audit UTC: 2026-07-09T13:37:27Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=261370 sha256=63fbacf1af7b993d4bc66bdb8f58f83740006ef3391907fd55c1f57981726e08 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=550261 sha256=f480aaaeeaaa5942399271fc11cd46c822245519bebd1af747432254591c3019 bad_markers=[]

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
