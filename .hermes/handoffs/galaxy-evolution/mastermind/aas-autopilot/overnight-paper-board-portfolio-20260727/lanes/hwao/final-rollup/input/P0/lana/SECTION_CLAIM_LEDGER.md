# P0 Section Claim Ledger — served 4-page PDF (SHA-256 0866…62ef)

Legend: ✅ stated · — absent · ⛔ contradicted. Sections: A = Abstract, M = §2 Method, R = §3 Results, F = Figures (rendered, visually inspected), D = §4 Discussion, C = §5 Conclusion.

## SFMS claims

| # | Claim | A | M | R | F | D | C | Verdict |
|---|---|---|---|---|---|---|---|---|
| S1 | TNG z≈0 SFMS residual −0.30 dex (must be removed first) | ✅ | ✅ | ✅ | ✅ (Fig.1 left, Fig.2 annotation) | ✅ | ✅ | **CONSISTENT** |
| S2 | Raw offsets +0.99/+1.15/+1.30 (z=4/5/6) vs observed +0.89/+0.96 (z≈4.7/5.4); raw "agreement" is an artefact | ✅ (summarized) | ✅ | ✅ | ✅ (Fig.2 left, point-by-point match) | ✅ | ✅ (implied) | **CONSISTENT** |
| S3 | Internal growth +1.30/+1.45/+1.61 dex; over-evolution gap **+0.41/+0.49 dex** at z≈4.7/5.4 | ✅ | ✅ | ✅ | ✅ (caption) | ✅ | ✅ | **CONSISTENT** — arithmetic reproduces (see NUMERIC_INVARIANTS) |
| S4 | Gap is a **conservative lower bound**; de-biasing selection widens it to **+0.46/+0.83**, up to ~+1.1 dex; sign robust across all 9 configs; quoted as envelope, not point estimate | ✅ | ✅ (model params) | ✅ | caption states direction; envelope **not plotted** | ✅ | ✅ | **CONSISTENT** (text); internally coherent, not externally recomputable from pinned inputs |
| S5 | **+0.13 dex** aperture→total mass offset (z=5; +0.12 z=6); cancels in internal differencing; removes ≈0.08 dex of raw offset | ✅ | ✅ | ✅ | — (not plotted; consistent with "cancels") | ✅ | ✅ | **CONSISTENT** |
| S6 | Headline: TNG forms stars too vigorously at high z — the one reproducible, calibration- and selection-independent failing | ✅ | supported | ✅ | ✅ | ✅ | ✅ | **CONSISTENT** |

## MZR claims

| # | Claim | A | M | R | F | D | C | Verdict |
|---|---|---|---|---|---|---|---|---|
| Z1 | TNG z≈0 MZR residual +0.12 dex (high) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (implied) | **CONSISTENT** |
| Z2 | Unmatched-scale result: TNG internal −0.23/−0.25/−0.25 vs obs ≈−0.50; **factor ~2** under-evolution; ~0.25 dex too metal-rich | — | ✅ | ✅ | ✅ (Fig.2 right + annotation "factor ~2") | ✅ | — | **BODY-ONLY** — displaced in A/C by Z4 |
| Z3 | Naive cross-survey comparison would inflate to factor 3–4 (abundance-scale artifact) | ✅ | — | ✅ | — | ✅ | ✅ | **CONSISTENT** (arithmetic reproduces) |
| Z4 | **Matched Te-anchored scale claim**: SDSS anchor recomputed via PP04 O3N2 (2.0×10⁵ gal), removing ~0.24 dex; deficit → ≈−0.40; TNG internal −0.27; factor ~1.5; within 0.1–0.15 dex residual systematic; **"not significant" / "consistent"** | ✅ | **—** (no PP04 procedure) | **—** (only Z2 numbers) | **⛔** (no matched-scale series; annotation still "factor ~2") | **⛔** ("on *different scales*"; "definitive result **requires** re-deriving"; "**suggestive**") | ✅ | **CONTRADICTED** |
| Z5 | Metallicity result is "suggestive"; single-scale re-derivation is future work | — | — | — | ✅ (annotation caveat) | ✅ | ⛔ ("consistent … once abundance scales are matched") | **CONFLICTS WITH Z4** |

## The controlling contradiction (Z4 vs Z2/Z5)

The abstract and conclusion assert that the matched-scale analysis **was performed** and that TNG's chemical evolution is **consistent** with observations. The methods contain no PP04 recomputation; the results report only the unmatched-scale numbers (−0.50 vs −0.23/−0.25/−0.25, factor ~2); Figure 2 plots only unmatched-scale series with an annotation that still reads "factor ~2 … also a calib-scale caveat"; and the discussion states in the present tense that the three abundance scales *are* different, that a definitive result *requires* re-deriving all three on a single calibration, and labels the metallicity result *suggestive*. Under the revision-consistency rule ("the strongest uncaveated claim controls the verdict; a new caveat followed by an unchanged strong conclusion is an unresolved contradiction"), the MZR consistency claim **cannot be accepted from this artifact**.

Supporting numeric evidence the abstract's matched-scale numbers are not derivable from the manuscript itself:

1. Anchor-shift arithmetic does not reproduce −0.40: removing a ~0.24 dex Tremonti offset from the anchor moves an observed deficit of −0.50 to ≈−0.26 if JWST values (already Te/low-scale) are unchanged. No stated ingredient yields −0.40.
2. TNG internal evolution is measured relative to TNG's own z≈0 relation and is therefore invariant under any recalibration of the SDSS anchor — yet the abstract quotes −0.27 while the results quote −0.23/−0.25/−0.25. The −0.27 value has no derivation anywhere in the manuscript.
3. Both the −0.40 and −0.27 values appear **only** in the abstract and (as "~1.5×, ≲0.15 dex") the conclusion.

## Version comparison (served 4-page, Jul 23 vs secondary 3-page, Jul 17)

- SFMS: the July 23 revision genuinely added S3–S5 (gap numbers, de-biasing envelope, +0.13 dex measured offset) and the lower-bound framing. The history JSON's SFMS change claims **landed**.
- MZR: §3, §4, and Figure 2 metallicity content are carried over essentially verbatim from July 17. The history JSON's claim that the revision "showed the apparent metallicity discrepancy dissolves on a matched Te-anchored scale" did **not** land as body evidence in either revision — the matched-scale claim exists only in abstract/conclusion of both copies. The contradiction is inherited, not introduced by the revision.

## What survives consistently (answer to the brief's question)

**Survive:** S1–S6 (the entire SFMS chain: −0.30 dex z≈0 residual; two-level differencing; +0.41/+0.49 dex over-evolution gap as a conservative lower bound; +0.46/+0.83 up to ~+1.1 dex de-biased envelope, sign-robust ×9; +0.13 dex mass-basis robustness; "forms stars too vigorously at high z"), plus Z1 (z≈0 MZR residual +0.12 dex) and Z3 (naive comparison inflates to 3–4×). Caveat on S2–S4: the observed medians inherit a failed load-bearing citation identity (Lisiecki — see CITATION_AND_REVIEW_LINK_AUDIT.md), which must be repaired in the correction ledger; it does not flip any sign because Nakajima et al. (2023) alone anchors the same qualitative elevations and the paper treats the observed points as upper bounds.

**Do not survive:** Z4/Z5 — every matched-Te-scale MZR statement ("largely dissolves", "factor ~1.5", "not significant", "consistent once abundance scales are matched"). The artifact's own body supports at most: *on unmatched scales TNG under-evolves the metallicity deficit by ~2×, and this result is suggestive pending a single-scale re-derivation.*
