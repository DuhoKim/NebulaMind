# Cycle 32 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_32`
Audit UTC: 2026-07-09T18:22:40Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=269416 sha256=333e48d5c33445244e7d2cdf7f1b79ae9d3089d7ad1174002991ad47cb88376c bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=556143 sha256=745a89ecd6b8e5a6c22eb23ffcc1a8c9ad3ec1eb94599b88c166c8c62a78cd82 bad_markers=[]

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
