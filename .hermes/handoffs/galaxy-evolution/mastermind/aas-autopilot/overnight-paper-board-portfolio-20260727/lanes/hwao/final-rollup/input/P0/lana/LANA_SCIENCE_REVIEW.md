# LANA science review — P0 TNG-validation served artifact

**Disposition: `MZR_STATE_CONTRADICTORY__CORRECTION_LEDGER_ONLY`**

Reviewed artifact: `galaxy-evolution-tng-validation-draft.pdf`, 4 pp, 132,831 bytes, SHA-256 `086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef` (pinned copy directly read, text-extracted, and visually inspected page by page — see `ARTIFACT_IDENTITY.md` for the full attestation).

## Answer to the brief's question

**Which SFMS and MZR claims survive consistently in the served four-page PDF?**

**The SFMS chain survives in full.** Every load-bearing star-formation claim is stated consistently in the abstract, methods, results, figures, discussion, and conclusion, and every step of its arithmetic reproduces exactly from values stated in the artifact:

1. TNG z≈0 SFMS residual −0.30 dex, removed before interpreting evolution (two-level differencing).
2. Internal growth +1.30/+1.45/+1.61 dex (= raw +0.99/+1.15/+1.30 plus the 0.30 residual, exact).
3. Over-evolution gap **+0.41/+0.49 dex at z≈4.7/5.4** (= 1.30−0.89 and 1.45−0.96, exact, under the conservative nearest-lower-snapshot pairing).
4. The gap is a **conservative lower bound**: the Hβ-flux-floor selection model (nine (σ, F_lim) configurations) only widens it — **+0.46/+0.83 dex** sample-matched, up to ~+1.1 dex, sign-robust across the grid, quoted correctly as an envelope, not a point estimate.
5. The **+0.13 dex** aperture→total mass-basis offset (redshift-stable, +0.12 at z=6) cancels to first order in the internal differencing; the residual raw-plane effect 0.61×0.13≈0.08 dex is stated and correct.
6. Headline: *TNG forms stars too vigorously at high z* — consistent everywhere, including the board card and history JSON.

Caveats that must ride with the SFMS result: (a) the observed medians blend Nakajima+2023 with a supplement whose citation **fails identity and role** (see below), so the exact values +0.89/+0.96 carry unresolved provenance even though the direction and lower-bound logic survive on Nakajima alone; (b) the de-biasing envelope and the −0.30/−0.13 dex inputs are internally consistent but not recomputable from pinned inputs (no data/code in the packet).

**The MZR consistency claim does not survive.** The abstract and conclusion assert a completed matched-Te-scale analysis: SDSS anchor recomputed via PP04 O3N2 from 2.0×10⁵ galaxies, removing ~0.24 dex; observed deficit becomes ≈−0.40 dex vs TNG internal −0.27 dex; factor ~1.5; within the 0.1–0.15 dex residual systematic; *hence not significant — chemical evolution consistent*. The rest of the artifact contradicts this:

- **Methods** contain no PP04 recomputation step of any kind.
- **Results §3** report only unmatched-scale numbers: TNG internal −0.23/−0.25/−0.25 vs observed ≈−0.50, a *factor ~2* under-evolution.
- **Figure 2 (right)** — visually inspected at 300 dpi — plots only Tremonti-scale series; its annotation still reads "obs −0.50 vs TNG internal −0.25 → factor ~2 (not 3–4×); also a calib-scale caveat". No Te-anchored series, no −0.40, no −0.27 anywhere.
- **Discussion §4** states, present tense, that the three abundance scales "*are on different scales*", that these offsets "*do not cancel*", that "*a definitive result requires re-deriving all three on a single calibration*", and labels the metallicity result "*suggestive*".
- The abstract's two matched-scale numbers are not derivable from anything in the paper: shifting the anchor by −0.24 dex moves a −0.50 deficit to ≈−0.26, not −0.40; and TNG's internal evolution is anchor-independent by construction, so the abstract's −0.27 cannot follow from any anchor recalibration of the body's −0.25.

Under the revision-consistency rule (the strongest uncaveated claim controls; a caveat plus an unchanged strong conclusion is an unresolved contradiction), the served artifact's own body supports at most: *on unmatched scales TNG under-evolves the metallicity deficit by ~2×, and this result is suggestive pending a single-scale re-derivation.* The "consistent once abundance scales are matched" headline — which is also the claim the board's merit panel repeatedly credits (paperScores notes cite "unmasks the chemical failure as an abundance-scale artifact" and "showed the apparent metallicity discrepancy dissolves") — is unsupported by the artifact.

Version comparison shows the contradiction is **inherited, not introduced**: the July 17 3-page source carries the identical abstract claim with the identical unsupported body. The July 23 revision landed the SFMS upgrades the history JSON describes but never landed the MZR analysis it also describes.

## Defect separation (brief item 5)

- **Capture-caused:** none material. `pdftotext` reading-order interleaving on page 3 and minor glyph artifacts only; verified harmless against rendered pages. The contradiction is not an extraction artifact — it is visible in the rendered pages themselves.
- **Manuscript/model-caused:** the Z4 abstract/conclusion vs body contradiction (core defect); the underived −0.27/−0.40 values; the Lisiecki mis-citation; missing PP04 and Kennicutt bibliography entries; "~3×10⁴" TNG count vs the plan-corrected 23,722 invariant (flagged, not provable from pinned inputs).
- **Validator/review-link-caused:** the configured review URL 404s (baseline and live re-check) while the board card links it — an artifact-integrity defect. No referee artifact exists that could have caught the contradiction; no verdict is inferred from the human-direction history JSON.
- **Unresolved:** whether a PP04 recompute exists anywhere outside this packet; true provenance of the z=3–6 supplement medians; exact TNG selection count.

## Why this disposition and not the others

- Not `CONSISTENT_CLAIMS__ISOLATED_REVISION_PACKET_ALLOWED`: the artifact's headline MZR claim is contradicted by its own results, discussion, and figure — the manuscript state is not internally stable enough to revise from.
- Not `SOURCE_OR_ESTIMAND_BLOCKED__NO_REVISION`: the estimands are well-defined and commensurable, the SFMS chain is reproducible, and the primary high-z source (Nakajima+2023) passes identity and role. The defects are correctable manuscript-state defects (contradictory MZR text, one cross-wired citation, two missing references, a dead review link) — exactly what a correction ledger records.
- `MZR_STATE_CONTRADICTORY__CORRECTION_LEDGER_ONLY` fits precisely: SFMS claims survive; the MZR state is contradictory; no corrected manuscript is written tonight; any revision is a separate next-day gate.

## Correction-ledger items (for Hwao's disposition; NOT applied tonight)

1. Abstract + conclusion: either supply the actual PP04/Te-anchored analysis (methods + results + figure series) with a derivation of the matched-scale deficit and internal evolution, or retract the matched-scale sentences and align the abstract/conclusion with the body's "factor ~2, suggestive, single-scale re-derivation required" state.
2. Reconcile −0.27 (abstract) vs −0.23/−0.25/−0.25 (results/figure).
3. Replace or remove the Lisiecki 2025 A&A 708 A235 citation (resolves to a 2026 quiescent-galaxy selection paper; wrong identity and role); re-provenance the blended z≈4.7/5.4 observed medians.
4. Add PP04 (Pettini & Pagel 2004) and Kennicutt bibliography entries — or remove the dependent claims.
5. Repair or remove the dead review link on the board card; do not present a review pointer for a review that does not exist.
6. Correct or substantiate the "~3×10⁴" TNG sample count against the frozen invariant (TNG=23,722) if the selection is the same.
7. Update Figure 2 right panel (series + annotation) to whatever the corrected MZR state is.

No manuscript, source file, Lab record, public artifact, DB/wiki row, service, or Git state was modified by this lane. All intermediates live in `packets/P0-tng-validation/lana/_tmp_audit/` (preserved as evidence of the visual inspection).

Marker: `P0_LANA_PRIMARY_COMPLETE_20260727`
