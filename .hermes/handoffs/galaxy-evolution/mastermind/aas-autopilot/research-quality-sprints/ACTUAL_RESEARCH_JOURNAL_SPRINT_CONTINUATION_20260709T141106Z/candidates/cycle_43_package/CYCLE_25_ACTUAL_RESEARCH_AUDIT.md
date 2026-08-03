# Cycle 25 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_25`
Audit UTC: 2026-07-09T17:27:01Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=267399 sha256=632a1cb8d8fad1718c9df304707b2b23ef647fc425b9169257ae1d34660e382f bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=555713 sha256=83afb37716d54e6a3dcddf559e76aa28d4508d34591eeec55ecd00aa98059f03 bad_markers=[]

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
