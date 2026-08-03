# P0 Hwao Disposition — TNG-Validation Served Artifact

Adjudicator: Hwao / Fable, final-rollup lane. Written 2026-07-27 ~22:45 KST (13:45 UTC), inside the approved window. Stop files (`GLOBAL_STOP_OVERNIGHT_PB_20260727.md`, `CONTENT_FREEZE_OVERNIGHT_PB_20260727.md`) checked before writing: absent.

## Disposition

**`MZR_STATE_CONTRADICTORY__CORRECTION_LEDGER_ONLY` — UPHELD.** No manuscript revision tonight. The correction ledger (below) is the only sanctioned next state; any revision is a separate next-day gate.

## Receipts relied upon

| Receipt | Lane / role | Marker | Verdict |
|---|---|---|---|
| `input/P0/lana/RECEIPT.json` + 6 artifacts (`LANA_SCIENCE_REVIEW.md`, `SECTION_CLAIM_LEDGER.md`, `NUMERIC_INVARIANTS.json`, `REPRESENTATION_MATRIX.json`, `ARTIFACT_IDENTITY.md`, `CITATION_AND_REVIEW_LINK_AUDIT.md`) | Lana, primary | `P0_LANA_PRIMARY_COMPLETE_20260727` | `MZR_STATE_CONTRADICTORY__CORRECTION_LEDGER_ONLY` |
| `input/P0/kun/RECEIPT.json`, `CROSSREVIEW.md`, `VALIDATION.json` | Kun, custody/representation cross-review | `P0_KUN_CROSSREVIEW_COMPLETE_20260727` | `ISSUES` — Lana's custody, SFMS survival, MZR contradiction, and review-link defect all upheld; no overstatement found in primary |
| `input/P0/goru/RECEIPT.json`, `CROSSREVIEW.md`, `VALIDATION.json` | Goru, mechanical claim-citation/numeric map | `P0_GORU_CROSSREVIEW_COMPLETE_20260727` | `PASS` (mechanical scope; **advisory, not proof**) |
| `input/TORI_BROWSER_SOURCE_CHECK.md` | Tori, independent custody/source check | `TORI_INDEPENDENT_SOURCE_IDENTITY_CHECK_20260727` | Browser-confirmed 4-page served identity and the Figure 2 unmatched-scale annotation from the 300-dpi crop |
| `input/VALIDATION_T1.json` public-identity block | Tori validator | — | `p0_pdf` 200 with SHA-256 `0866…62ef` identity match; `p0_review` 404 as expected; `p0_history` 200 identity match |

No lane reviewed its own primary output. Lana's receipt attests direct pinned-byte access (hash recomputed, pages rendered and visually inspected); Kun and Goru independently re-verified all manifest hashes; Tori independently opened the public URL in a browser. Receipt custody requirements are met.

## Adjudicated claim outcomes

**Survive (consistently represented and, where checkable, arithmetically reproduced):**

- S1–S6, the full SFMS chain: z≈0 residual −0.30 dex; two-level differencing; internal growth +1.30/+1.45/+1.61 dex; over-evolution gap **+0.41/+0.49 dex at z≈4.7/5.4** as a conservative lower bound; de-biasing envelope +0.46/+0.83 up to ~+1.1 dex, sign-robust across all 9 (σ, F_lim) configurations; +0.13 dex mass-basis offset cancelling to ~0.08 dex raw-plane effect; headline "TNG forms stars too vigorously at high z". Arithmetic independently reproduced by Lana, Kun, Goru, and the T1 validator (0.41/0.49/0.0793 exact).
- Z1 (z≈0 MZR residual +0.12 dex) and Z3 (naive cross-survey factor 3–4 as an abundance-scale artifact; 0.50/0.13 = 3.8 checks).

Mandatory caveats riding with the survivors: (a) the observed medians +0.89/+0.96 blend Nakajima+2023 with a supplement whose Lisiecki citation **fails identity and role** — direction survives on Nakajima alone, exact values carry unresolved provenance; (b) the −0.30/+0.12/envelope computations are internally consistent but not recomputable from pinned inputs (no data/code in packet).

**Do not survive:**

- Z4/Z5, every matched-Te-scale MZR statement (PP04 O3N2 recompute of 2.0×10⁵ galaxies, ~0.24 dex removal, −0.40 vs −0.27, factor ~1.5, "not significant"/"consistent once abundance scales are matched"). Methods contain no PP04 step; Results report only unmatched-scale numbers (−0.23/−0.25/−0.25 vs ≈−0.50, factor ~2); Figure 2 right plots only Tremonti-scale series with the annotation still reading "factor ~2"; Discussion states present-tense that the scales differ and the result is "suggestive". Two independent arithmetic refutations stand: −0.50 + 0.24 = −0.26 ≠ −0.40, and TNG internal evolution is anchor-independent so −0.27 has no possible derivation from the body's −0.25. Confirmed independently by Lana (rendered-page inspection), Kun (render + extraction), Goru (arithmetic), and Tori (browser crop). The maximum body-supported statement is: *on unmatched scales TNG under-evolves the metallicity deficit by ~2×, and this result is suggestive pending a single-scale re-derivation.*

## Preserved defects (none repaired tonight)

1. **Served identity**: 4-page PDF, 132,831 B, SHA-256 `086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef` is the audit target; the 3-page July 17 copy (`f037d89d…75d6`) is divergence evidence, not a substitute. Not interchangeable.
2. **Dead review link**: configured review URL returns HTTP 404 (baseline 13:02Z, Lana live re-check ~22:15 KST, T1 re-check 13:29Z) while the board card still links it. Artifact-integrity defect; no referee artifact exists; no verdict inferred from the human-direction history JSON by any lane or by this disposition.
3. **Figure 2 unmatched-scale annotation**: right panel annotation "obs −0.50 vs TNG internal −0.25 → factor ~2 (not 3–4×); also a calib-scale caveat" — no matched-Te series, no −0.40/−0.27 anywhere in any figure.
4. **Unsupported matched-Te abstract/conclusion**: preserved verbatim as the controlling contradiction (inherited from the July 17 revision, not introduced on July 23; the history JSON's claimed MZR landing never landed).
5. Lisiecki 2025 A&A 708 A235 citation identity+role FAIL (resolves to a 2026 quiescent-galaxy selection paper; ADS path for Goru-style bibcode checks 404s); missing PP04 and Kennicutt bibliography entries; "~3×10⁴" TNG count QUESTIONABLE vs the frozen invariant TNG=23,722; "2.0×10⁵" PP04 subset BLOCKED (belongs to the unsupported claim; adjacent invariant SDSS=120,000 also differs).

## Disagreement resolution

No substantive disagreement among lanes. Goru's `PASS` is scoped to the mechanical validity of Lana's audit and is advisory only — it does not offset Kun's `ISSUES`, which governs the artifact state. All four independent looks (Lana, Kun, Goru, Tori) converge on the same core defect.

## Remaining unsupported / blocked / disputed rows

- BLOCKED: `matched_scale_claim` (−0.40/−0.27/×1.5) and the 2.0×10⁵ PP04 subset count.
- QUESTIONABLE: "~3×10⁴" TNG sample count vs invariant 23,722.
- UNRESOLVED: existence of any PP04 recompute outside this packet; true provenance of the z=3–6 supplement medians; exact TNG selection count.
- CONSISTENT_UNVERIFIABLE (not rescued, not blocked): −0.30/+0.12 residuals, de-biasing envelope, +0.13 dex catalogue value, N=965, SDSS 4.9×10⁵.

## Correction ledger (carried forward from Lana, endorsed; NOT applied tonight)

The seven items in `LANA_SCIENCE_REVIEW.md` §"Correction-ledger items" are adopted verbatim: (1) supply or retract the matched-Te analysis in abstract+conclusion; (2) reconcile −0.27 vs −0.23/−0.25/−0.25; (3) replace/remove Lisiecki and re-provenance the blended medians; (4) add PP04 and Kennicutt entries or remove the dependent claims; (5) repair or remove the dead review link; (6) correct/substantiate the TNG count against 23,722; (7) regenerate Figure 2 right panel to the corrected MZR state.

Automated reviews and this adjudication are not human validation or peer review. No manuscript, public artifact, or project state was modified by this disposition.
