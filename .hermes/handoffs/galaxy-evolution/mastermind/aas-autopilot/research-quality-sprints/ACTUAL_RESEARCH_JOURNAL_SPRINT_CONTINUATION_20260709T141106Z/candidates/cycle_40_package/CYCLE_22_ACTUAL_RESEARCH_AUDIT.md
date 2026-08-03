# Cycle 22 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_22`
Audit UTC: 2026-07-09T17:07:21Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=267097 sha256=2acbb6a9f55d8b03be1742be5839be088a0e9010f9ca2727ae3ecd50da2ed71a bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=555566 sha256=2554aac247dd50dbf68e4e8b170fd7c2b0f462c9cd207727878bce2ac38a5c47 bad_markers=[]

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
