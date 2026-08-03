# P0 Render and Representation Acceptance Plan

Status: `PREPARED_NOT_RENDERED`

No TeX compile, source-level test, PDF render, or build was executed under the packet-preparation-only approval.

## Frozen current representation

- Served PDF: 4 pages, 132,831 bytes.
- SHA-256: `086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef`.
- Figure 1 source asset SHA-256: `90bb9742228ff74dcf8ebf45cf4ca4a249ac628ede5254ba635563fd3b537e70`.
- Figure 2 source asset SHA-256: `5ef7a5ba52e565cc73b16afc28cae5c8f1de03a0565277e2cc3d7614c482b0a0`.
- Current Figure 2 visually shows unmatched-scale series and a factor-of-two annotation with a calibration-scale caveat.

## Figure disposition

Both figure assets are intentionally unchanged. The selected repair retracts the unsupported matched-scale abstract/conclusion state and aligns text to the existing figure state. The TeX caption is narrowed to say explicitly that the factor-two MZR comparison is face-value, on unmatched scales, and subject to the calibration caveat.

## Required post-apply compile gate

1. Copy the applied TeX and both pinned figure assets into a clean temporary build directory.
2. Run `tectonic after.tex` there; do not compile into the tracked source directory.
3. Require exit code 0 and no unresolved citation/reference warnings.
4. Require 4–5 pages; any larger pagination change needs review rather than automatic acceptance.
5. Run `pdfinfo` and `pdftotext -layout` on the candidate PDF.
6. Render every page at 300 dpi with `pdftoppm`.
7. Visually inspect title, abstract, both columns, both figures, captions, Results, Discussion, Conclusion, and bibliography.

## Structural acceptance checks

- Abstract and Conclusion contain no PP04 performed-analysis claim, −0.40, −0.27, factor 1.5, or chemistry-consistency verdict.
- Results, Figure 2 caption, Discussion, and Conclusion all call the MZR state unmatched-scale and suggestive.
- Figure 2 image pixels remain byte-identical to the pinned source asset and retain the calibration caveat.
- +0.41/+0.49, +0.46/+0.83, up-to-~1.1, and +0.13 remain visible and correctly scoped to the SFMS result.
- Kennicutt 1998 appears in text and bibliography; Lisiecki and PP04 performed-analysis language do not.
- No line, citation, legend, annotation, or bibliography row is clipped, overlapping, missing, or off-page.
- Extracted text and rendered pixels agree for all changed sentences.
- Page title and descriptive/non-human-validated status remain visible.

## Board representation checks after a future source apply

- P0 card retains the same supported SFMS summary.
- P0 has no dead review metadata and no fabricated verdict.
- All five merit scores remain numerically unchanged.
- DR/Tori/Kun/Goru notes carry the corrected MZR/provenance scope.

Final representation status cannot advance beyond `PREPARED_NOT_RENDERED` until the separate apply/test gate is opened.
