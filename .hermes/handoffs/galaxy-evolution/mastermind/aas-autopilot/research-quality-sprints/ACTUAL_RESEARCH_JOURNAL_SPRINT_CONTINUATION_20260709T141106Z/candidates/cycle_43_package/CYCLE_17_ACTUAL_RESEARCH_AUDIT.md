# Cycle 17 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_17`
Audit UTC: 2026-07-09T16:31:08Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=265463 sha256=fe7471b214ecb1911190da9337ecec5dd513506dd73d92bf3f60ab31849dde9e bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=554277 sha256=55e8a1107eef4c32d4d45d4fc6922bbfb81b6e4d2923190359660ea3f0a7e172 bad_markers=[]

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
