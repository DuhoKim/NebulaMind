# Cycle 8 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_08`
Audit UTC: 2026-07-09T15:13:19Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=263721 sha256=1797ca09b955e3e503c0a9be8f6820351a2ca5b2414aea947a2aeebd1223e4bf bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=553093 sha256=fe8b9f84978ad03bad6d70c70151a5bbd2c51fee63ef9390cf4f7a7eee187fb2 bad_markers=[]

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
