# P0 Kun Cross-Review

Marker: `P0_KUN_CROSSREVIEW_COMPLETE_20260727`

## Disposition

`ISSUES`

I independently cross-checked Lana's primary review against the immutable packet inputs and the pinned served PDF. Lana's custody claims, SFMS claim survival, review-link defect, and MZR contradiction are supported. The served four-page artifact is not representation-stable enough to accept as a clean paper-board item because the abstract/conclusion claim a completed matched-Te-scale MZR result that the methods, results, figures, and discussion do not contain and visibly contradict.

## Inputs And Custody

- Read `input/BRIEF.md` and all files under immutable `input/`.
- Verified every file hash listed in `input/INPUT_MANIFEST.json`; all listed hashes match.
- Parsed all JSON inputs successfully: both manifests, Lana receipt, `PUBLIC_ARTIFACT_IDENTITY.json`, `served-history.json`, `NUMERIC_INVARIANTS.json`, and `REPRESENTATION_MATRIX.json`.
- Confirmed served PDF identity: `input/source/served-p0.pdf`, 132,831 bytes, SHA-256 `086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef`, 4 pages, CreationDate `Thu Jul 23 20:28:34 2026 KST`.
- Confirmed secondary PDF identity: `input/source/secondary-3page-source.pdf`, 120,426 bytes, SHA-256 `f037d89d210130d464e3ddbc2390b020aa3ffeebabab272357102691190f75d6`, 3 pages, CreationDate `Fri Jul 17 00:57:00 2026 KST`.
- The 4-page served artifact and 3-page source copy are not interchangeable. The July 23 version adds the SFMS lower-bound/debiasing/mass-basis material; the MZR contradiction is already present in the July 17 text and remains unresolved in the July 23 served PDF.

## Section State Cross-Check

SFMS state labels: `PASS_WITH_CAVEATS`.

The SFMS chain is consistently represented across abstract, method, results, Figure 2/caption, discussion, conclusion, history, and board-card summary. The arithmetic reproduces from the paper text:

- `1.30 - 0.89 = 0.41`
- `1.45 - 0.96 = 0.49`
- `0.61 * 0.13 = 0.0793`, matching the stated about 0.08 dex raw-plane effect.

The selection-debiasing envelope `+0.46/+0.83` and up to about `+1.1 dex` is consistently stated as an envelope and lower-bound direction, not a plotted point estimate. It is internally coherent but not recomputable from pinned data/code. The exact observed medians remain provenance-caveated because the Lisiecki supplement citation fails identity and role.

MZR state labels: `ISSUES`.

The served abstract states that all three datasets were put on a single Te-anchored scale via PP04 O3N2, removing about `0.24 dex`; it then claims the observed deficit is about `-0.40 dex`, TNG internal evolution is `-0.27 dex`, the shortfall is about `1.5x`, and the chemical evolution is consistent within residual systematics. The rendered and extracted body do not support this:

- Methods contain no PP04/O3N2 recomputation procedure.
- Results report unmatched-scale MZR values only: TNG internal `-0.23/-0.25/-0.25 dex` versus observed about `-0.50 dex`, a factor about 2.
- Rendered Figure 2 right panel shows only the unmatched-scale series and annotates a factor about 2, with a calibration-scale caveat.
- Discussion says the three oxygen abundances are on different scales, the offsets do not cancel, a definitive result requires re-deriving all three on one calibration, and the metallicity result is suggestive.
- Conclusion reasserts matched-scale consistency despite the body state.

Arithmetic also challenges the matched-scale claim: `-0.50 + 0.24 = -0.26`, not `-0.40`, if the high-z Te/low-scale values are unchanged; TNG internal evolution should not change under an SDSS anchor recalibration, yet the abstract's `-0.27` is not derived from the body's `-0.23/-0.25/-0.25`.

## Citation And Review Link

Lisiecki identity failure is upheld. Public search resolves `A&A 708, A235` to Lisiecki et al. 2026, "Impact of stochastic star formation histories and dust information on selecting quiescent galaxies with JWST photometry", not a 2025 z=3-6 star-forming SFMS/MZR supplement. VizieR/CDS reports bibcode `2026A&A...708A.235L` and describes a CEERS/MIRI photometric quiescent-galaxy catalogue, so the cited source cannot carry the manuscript role. Nakajima 2023 ApJS 269, 33 does match the high-z JWST MZR/SFR-MZ role.

The missing PP04 and Kennicutt bibliography entries are real load-bearing reference gaps. Pettini & Pagel 2004 is the named O3N2 calibration basis for the abstract's MZR claim, and Kennicutt is named for the H-alpha/H-beta SFR conversion in the selection model; neither appears in the PDF references.

Review-link handling is correct. `input/source/PUBLIC_ARTIFACT_IDENTITY.json` records the P0 review URL as HTTP 404 at `2026-07-27T13:02:48Z`; `input/source/FrontierDrafts.tsx` still exposes that review path. `served-history.json` is explicitly human-directed and must not be treated as an automated review verdict. Lana did not infer a verdict from history, and neither do I.

Public identity sources used for citation challenge:

- VizieR/CDS `J/A+A/708/A235`: https://cdsarc.cds.unistra.fr/viz-bin/cat/J/A%2BA/708/A235
- IPAC/NASA ADS-style record for Nakajima 2023 ApJS 269, 33: https://www.ipac.caltech.edu/publication/2023ApJS..269...33N

## Capture Versus Manuscript

No capture-caused false defect found. `pdftotext -layout` interleaves some two-column text and figure text, but rendered page inspection confirms the load-bearing MZR mismatch appears in the visible PDF itself. Figure 2 right visibly preserves the factor-about-2 unmatched-scale state, while page 4 visibly reasserts matched-scale consistency in the conclusion.

## Boundary Check

No input files, source files, public artifacts, project files, services, database/wiki records, or Git state were modified. Writes were limited to this lane directory: `CROSSREVIEW.md`, `VALIDATION.json`, and `RECEIPT.json`. Temporary extraction/render files were written under `/tmp`.

Final disposition: `ISSUES`. The correct next state is correction-ledger/adjudication, not publication or revision acceptance from the current served artifact.
