# Tori Independent Browser and Source-Identity Check

Observed 2026-07-27 22:15–22:22 KST. This is custody/representation verification, not a packet science verdict.

## P0 served representation

- Browser-opened `https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf` with a cache-busting query.
- The public viewer reported 4 pages.
- Page 1 rendered at fit-to-page with title, author/byline area, abstract, keywords, and two-column opening text visible. No obvious clipping, overlapping blocks, or missing glyphs were visible at that scale.
- This visual check does not validate scientific content or the remaining pages.

### P0 Figure 2 independent rendered-crop check

- Opened Lana's preserved 300-dpi crop from the exact pinned served PDF.
- The right panel is titled `Metallicity offset`; the visible series are `JWST observed (vs SDSS)`, `TNG (vs SDSS anchor)`, and `TNG internal (vs TNG z = 0)`.
- Its in-panel annotation visibly reads `obs −0.50 vs TNG internal −0.25 → factor ~2 (not 3–4×); also a calib-scale caveat`.
- The panel does not display a matched-Te/PP04 series or the abstract's −0.40, −0.27, or factor-1.5 quantities.
- Plot axes, legends, points, and annotation are visible without obvious overlap or missing glyphs. The stored crop clips unrelated surrounding page prose at its right edge, not the figure itself.
- This independently confirms the representation-state mismatch; it does not validate either numerical model.

### P1 page 3 independent rendered-page check

- Rendered the exact pinned served P1 PDF page 3 at 300 dpi; PNG SHA-256 is `68373de4c4c53d54a84e81b326bda79c11e330157f0d78f5e1215fdd6b11c5a7`.
- Figure 1's green-arrow annotation visibly says `erased by 0.28 dex M⋆`.
- The caption directly below says the z≈5 excess on the total-mass footing `is erased by a 0.20 dex downward stellar-mass shift`.
- This is a real same-page representation contradiction, not a text-extraction artifact.
- Figure 1 axes, points, legend, and arrow remain legible. Separately, Table 1's rightmost `grounding` column visibly overruns/clips at the page's right edge, truncating several citation strings; preserve this additional layout defect for Lana/Hwao adjudication.
- No scientific validity is inferred from the visual check.

## P2 exact identities

The frontier PDF itself resolves the shorthand bibliography:

| Shorthand | Exact frontier bibliography identity | Independent public identity check | Finding against Goru primary |
|---|---|---|---|
| Chisholm et al. 2022 | MNRAS 517, 5104; ADS `2022MNRAS.517.5104C`; arXiv 2207.05771 | Title: “The Far-Ultraviolet Continuum Slope as a Lyman Continuum Escape Estimator at High-redshift” | Goru recorded `2022MNRAS.515.4265C`. That ADS path is 404 and the volume/page corresponds to a different paper context. Goru's `VERIFIED` status is false and must be patched. |
| Flury et al. 2022 | ApJ 930, 126; ADS Part II identity | The independently opened `2022ApJS..260....1F` is LzLCS Part I, DOI `10.3847/1538-4365/ac5331`, and is a real related source, but it is not the exact bibliography entry printed in the frontier PDF. | Goru verified a related Part I paper rather than the exact cited Part II paper. Exact citation identity was not verified. |
| Simmonds et al. 2024 | MNRAS 527, 6139; ADS `2024MNRAS.527.6139S`; DOI `10.1093/mnras/stad3605` | Title: “Low-mass bursty galaxies in JADES efficiently produce ionizing photons and could represent the main drivers of reionization” | The frontier bibliography is not ambiguous: it prints 527, 6139. `2024MNRAS.535.2998S` is a separate later Simmonds JADES paper (DOI `10.1093/mnras/stae2537`). The `fesc002` novelty gate lists both, so the pipeline shorthand is cross-wired, but the frontier citation is resolved. |

Independent public pages checked:

- `https://ui.adsabs.harvard.edu/abs/2022ApJS..260....1F/abstract`
- `https://ui.adsabs.harvard.edu/abs/2024MNRAS.527.6139S/abstract`
- `https://ui.adsabs.harvard.edu/abs/2024MNRAS.535.2998S/abstract`
- `https://ui.adsabs.harvard.edu/abs/2022MNRAS.515.4265C/abstract` returned the ADS not-found page.
- Public search resolved Chisholm's exact frontier citation to `2022MNRAS.517.5104C` / arXiv 2207.05771.

## P2 citation and representation boundary

- The frontier PDF prints all three exact references and describes Chisholm/Flury as LzLCS proxy calibrations and Simmonds as the adopted `xi_ion` source.
- The `fesc002` PDF cites `[Chisholm+22, Flury+22; Simmonds+24]` in prose but omits all three from its printed reference list.
- The `fesc002` stored `citation_entailment` gate checked zero claims. “6 papers, 5 passages” is not a citation-entailment pass.
- The `fesc002` novelty gate contains both Simmonds JADES papers, while the manuscript shorthand does not specify which one. The pipeline identity remains cross-wired/unresolved even though the frontier identity is explicit.
- The pipeline abstract says “Generated autonomously from public data (jwst)” while its body says it uses existing literature and no new survey data or catalogs. Preserve this as a reader-facing provenance contradiction; do not silently normalize it.
- Goru's `CANONICAL_PLUS_SUPPORTING` relationship is a hypothesis consistent with the one-point-versus-landscape content, but the primary artifact does not supply a derivation/lineage receipt. It cannot be treated as proven until a reviewer distinguishes content similarity from lineage.

## Disposition

`P2_GORU_PRIMARY_REQUIRES_PATCHES`

Required cross-review outcome: correct the Chisholm and Flury identities, resolve the frontier Simmonds identity separately from the pipeline cross-wire, downgrade false `VERIFIED` claims, and keep the lineage relationship provisional unless a direct derivation record is found.

Marker: `TORI_INDEPENDENT_SOURCE_IDENTITY_CHECK_20260727`
