# Cycle 39 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_39`
Audit UTC: 2026-07-09T19:19:10Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=270696 sha256=037ccd19c69f6776eb108b4eb6d252495ff90dbf822a23285b77453a5b04fbce bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=558558 sha256=8038ed3075bc7abf8b518230cda0106934bafbdcfec8a37b15269b5ccf9e66ea bad_markers=[]

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
