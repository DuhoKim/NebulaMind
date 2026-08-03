# Cycle 4 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_04`
Audit UTC: 2026-07-09T13:44:25Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=261808 sha256=0e99b11c117e71319702087242169ba6d3d5d23c999837aecbb63ba0a9916ec4 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=550630 sha256=80a4c273eea9335774f4db2b1235dab44a9d2dfa73f945fb58ec41d08141ab6f bad_markers=[]

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
