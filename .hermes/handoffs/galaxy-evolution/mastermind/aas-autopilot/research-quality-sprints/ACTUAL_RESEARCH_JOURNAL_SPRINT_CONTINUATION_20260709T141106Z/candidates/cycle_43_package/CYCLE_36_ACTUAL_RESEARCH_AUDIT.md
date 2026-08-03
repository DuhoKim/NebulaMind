# Cycle 36 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_36`
Audit UTC: 2026-07-09T18:56:27Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=270060 sha256=964baa8cfb85b067524e61cc507eb946938904bae5858b4f71adc109011752d2 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=557859 sha256=6ba70393c601d1f8cdcaaa6e81ddb939b68bc41f2c21a0da8505447a4fe040eb bad_markers=[]

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
