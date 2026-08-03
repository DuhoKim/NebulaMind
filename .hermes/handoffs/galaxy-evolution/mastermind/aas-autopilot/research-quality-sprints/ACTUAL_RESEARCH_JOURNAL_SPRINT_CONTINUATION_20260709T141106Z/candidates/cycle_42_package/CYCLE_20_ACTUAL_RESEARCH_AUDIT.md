# Cycle 20 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_20`
Audit UTC: 2026-07-09T16:53:29Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=266076 sha256=7f1a74ff96764dfab2bd7dd65b6cb49b12892bb0ee95f5df28cac063e40c6015 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=555422 sha256=8ff8465f2b118711383b67d3945e0cf7098a9f6d6e41325842d6a33e8bf9cd0b bad_markers=[]

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
