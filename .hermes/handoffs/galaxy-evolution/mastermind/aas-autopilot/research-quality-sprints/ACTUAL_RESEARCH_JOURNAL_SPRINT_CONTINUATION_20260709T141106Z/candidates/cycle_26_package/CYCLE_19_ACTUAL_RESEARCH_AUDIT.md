# Cycle 19 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_19`
Audit UTC: 2026-07-09T16:45:42Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=265875 sha256=494041b57722f106e7f8d8d2d689156b935dc2297011215f9305e474cc17fbb7 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=555178 sha256=606c813d1703b05e972bd6737ba3ccb877b248f6806ea636dcc94e05dbc8304f bad_markers=[]

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
