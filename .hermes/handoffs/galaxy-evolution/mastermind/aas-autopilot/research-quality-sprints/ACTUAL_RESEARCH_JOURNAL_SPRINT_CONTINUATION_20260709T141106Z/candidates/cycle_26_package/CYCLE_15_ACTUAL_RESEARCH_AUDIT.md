# Cycle 15 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_15`
Audit UTC: 2026-07-09T16:12:13Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=265368 sha256=342d284567bb8988462ef45e824a746f7d028f09cbd851ed5291ca3d90b0da59 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=553568 sha256=494802fe878c7ba49547e04eb83b890564f18541090b551c35b426676606928f bad_markers=[]

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
