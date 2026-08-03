# Cycle 43 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_43`
Audit UTC: 2026-07-09T19:50:08Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=271928 sha256=296ea0205be490f24aecfc639933a2d8500bb1097599cdc463d92b6284859d44 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=558728 sha256=32af0732b9ed2567a31a3795b6af722478859ba021c79a7b05b7a42de6c422c9 bad_markers=[]

## Guards
- flagship missing required phrases: ['not a causal']
- supplement missing required phrases: []
- flagship missing numeric invariants: []
- forbidden mock/synthetic data-use hits flagship: []
- forbidden mock/synthetic data-use hits supplement: []

Fatal failures: 1

## Real-data policy
- Never use mock, synthetic, fake, placeholder, or toy data.
- Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.
- New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.
- If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.
- Literature-only sources may motivate future work; they do not become measured NebulaMind results.
- The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied.
