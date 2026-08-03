# G1 — AFFECTED-CLAIMS REGISTER (current freeze vs V3 narration/cards/captions)

Coordinator: Hwao · Written: 2026-07-23 ~14:30 KST (05:30Z)
Gate: G1 of `HWAO_V4_SOURCE_REFRESH_AMENDMENT.md` · Lane-only receipt; nothing outside this directory was written. No render/audio/lip-sync, YouTube, website, DB, git, runtime, deploy, restart, cron, or old-artifact mutation.

## Inputs

- Current freeze: `V4_SOURCE_FREEZE.json` (marker `NEBULAMIND_FIVE_PAPER_V4_CURRENT_SOURCE_FREEZE_COMPLETE`, 2026-07-23T12:16:15Z, `all_expected_live_hashes_matched: true`) + `sources-v4/*.md` extracts (line anchors below refer to these files).
- V3 narration/cards: `paper-videos-v2-20260723T034035Z/paper_video_specs_v2.json` — verified as the exact text V3 built audio from (`build_v3_audio_and_layouts.py:23` `SPEC_PATH`); V3 captions equal narration by the builder's deterministic SRT check, so this register covers narration, cards, and captions at once.
- Method: mechanical number-by-number diff (Goru role) + per-claim semantic ruling (Lana role), both executed by Hwao inside this lane this turn; verdicts are falsifiable via the cited line anchors.

Verdicts: **CONFIRMED** (claim stands in current freeze) · **REFRAMED** (number stands, interpretation superseded) · **SUPERSEDED** (number/claim replaced) · **REFINED** (compatible, sharper value available).

## z9-metallicity — 0 superseded · V4 may reuse claims

| V3 scene | V3 claim | Current freeze | Verdict |
|---|---|---|---|
| 3 | 5 unlensed Pollock galaxies, z=9.3–9.9, direct Te | present (abstract) | CONFIRMED |
| 4 | −0.69±0.03 dex vs Curti; leave-one-out spread 0.04 | `z9-metallicity.md:34` | CONFIRMED (`:135-138` adds inverse-variance −0.68±0.03 — optional REFINED) |
| 5 | anchor swap → −0.65 dex (0.04 shift) | `:37` (`:115` gives −0.645/0.042) | CONFIRMED |
| 6 | GN-z11 z=10.6, 7.82±0.35, population −0.64…−0.68 | `:139-142` | CONFIRMED |
| 7 | ~1500-gal stacked JADES, z=4–10, −0.5…−0.6 dex | `:38-39`, `:84`, Z8=7.62±0.10 `:92-94` | CONFIRMED |
| 8 | Te scale 0.1–0.2 dex dominates; not a detection | `:43`, `:113`, `:135` | CONFIRMED |

G2 action: none mandatory; optionally adopt the −0.68±0.03 inverse-variance phrasing.

## scaling-relations — central interpretation REFRAMED (Tori T2 confirmed)

Title itself is now "…A Selection-Aware Reassessment…". As-measured numbers survive; the meaning of the SFMS elevation below z≈6 does not.

| V3 scene | V3 claim | Current freeze | Verdict |
|---|---|---|---|
| 2 | 490k SDSS; 180 NIRSpec / 145 with metallicity; 3743 MIRI/CEERS | `scaling-relations.md:87` (4.9×10⁵), `:108`, `:110`, `:114` | CONFIRMED |
| 3 | 200k SDSS rebuilt on Te-anchored scale | `:71` (N=2.0×10⁵ galSpecLine) | CONFIRMED |
| 4 | "+0.77 dex ≈6× (z 3.5) … +1.94 dex ≈87× (z 6.7): early galaxies form stars much faster" | values as-measured stand (`:132-133`) **but** below z≈6 the elevation is consistent with pure selection; paper explicitly makes **no SFR-evolution claim below z≈6** (`:26-33`, `:63-65`); per-bin inflation +0.63/+0.51/+0.44 with residual envelopes reaching ≤0 (`:191-195`, `:164-166`) | **REFRAMED — rewrite required.** V4 must present +0.77→+1.94 as *as-measured* offsets and immediately attribute the sub-z≈6 part to selection-vs-physics ambiguity |
| 5 | "last bin 46 galaxies; elevation may be inflated, read cautiously" | n=46 persists (`:165`); caution upgraded to the central result: sub-z≈6 = possibly pure selection; **what survives is the z>6 residual ~1.3–1.5 dex** (`:33`) | **REFRAMED — rewrite required** (from "caveat" to "central deflationary result + surviving z>6 signal") |
| 6 | metallicity −0.43/−0.37/−0.40 dex at z 4.6/5.3/7.2 ≈40% | `:190-191`, Te-anchored | CONFIRMED (now explicitly "the more robust of the two signals", `:160-162` — optional strengthen) |
| 7 | flat median z 4–7; 68% span ~0.5 dex; some within 0.15 dex | ≈−0.4 flat `:183`; span/outlier lines persist in extract | CONFIRMED |
| 8 | ~0.1 dex scale uncertainty; low-mass extrapolation | stands; **new**: Tremonti anchor ~0.24 dex high would have overstated the deficit by ~0.1–0.13 dex (`:74-75`) | REFINED — add the anchor-overstatement note |

G2 action: rewrite scenes 4–5 (mandatory), strengthen 6, extend 8; YouTube description must drop any "stars form much faster at all redshifts" framing.

## massive-abundance — four scenes SUPERSEDED (Tori T2 confirmed)

Root cause of the drift: TNG side now uses like-for-like total mass — aperture-to-total +0.13 dex, 20 subhalos ⇒ n(>10^10.5)=1.47×10⁻⁵ Mpc⁻³ at z=5, replacing 1.1×10⁻⁵/15 subhalos (`massive-abundance.md:28-29`, `:77-84`).

| V3 scene | V3 claim | Current freeze | Verdict |
|---|---|---|---|
| 2 | threshold 10^10.5 M☉ (≈32 billion suns) | `:28-29`, `:64` | CONFIRMED |
| 3 | observed 3×10⁻⁵ vs TNG 1.1×10⁻⁵ ⇒ raw **2.7×** | observed 3×10⁻⁵ stands (Weibel, `:30`); TNG now **1.47×10⁻⁵** ⇒ factor **≈2.04 (0.31 dex)** (`:28-30`) | **SUPERSEDED — rewrite required** |
| 4 | required shift **0.28 dex** (÷1.9) | now **≈0.20 dex** (`:32`, `:80-81`); slope re-measured between logM⋆=10.0–… (`:88`) — Goru must re-anchor the slope card at G3 | **SUPERSEDED — rewrite required** |
| 5 | "smaller than the roughly **1 dex** literature budget" | "~1 dex" explicitly replaced by a **committed 0.46–0.55 dex quadrature budget**; required shift ≈0.4× budget; ±0.10 dex Poisson floor; IMF-independent (`:32-35`, `:77-84`) | **SUPERSEDED — rewrite required** |
| 6 | z 7–9 candidates ≈**13×**, correction **0.44 dex**, photometric | now **≈13.6× (1.13 dex)** requiring **≈0.72 dex**, which **exceeds** the 0.55 dex budget (`:44-45`) — the conclusion flips from "uncertain masses could cover it" to "not covered by the committed budget" | **SUPERSEDED — rewrite required** |
| 7 | quiescent z>6 ≈2 dex residual unresolved | `:47` | CONFIRMED |
| 8 | z 4–6 counts need no new cosmology within mass errors | stands, now on the tighter 2.04/0.20-dex footing | CONFIRMED (numbers inside it update via scenes 3–5) |

G2 action: rewrite scenes 3, 4, 5, 6; description line "dissolve the z 4–6 tension" survives but its supporting numbers change.

## mzr-framework — freeze identical, no diff

G0 hash `bb0869aa…` equals the V3 freeze; `all_expected_live_hashes_matched` covers it. All eight scenes CONFIRMED by identity; no G2 rewrite. (V4 still changes its *visuals* per the direction: procedure diagram, no cover page.)

## tng-validation — one REFINED number, rest CONFIRMED

| V3 scene | V3 claim | Current freeze | Verdict |
|---|---|---|---|
| 4 | starting residuals −0.30 (SFMS) / +0.12 (MZR) | `tng-validation.md:28`, `:77-78` | CONFIRMED |
| 5 | TNG internal growth +1.3…+1.6 vs observed "**0.9–1.0**" (card said +0.8–1.0) | current: observed **∼+0.8–1.0 dex** (`:29-30`); adds per-z growth +1.30/+1.45/+1.61 (`:88`) and over-evolution gap +0.41/+0.49 dex at z≈4.7/5.4 (`:30`) | **REFINED — narration must say 0.8–1.0** (fixes the V3 narration/card inconsistency); optionally cite the gap values |
| 6 | three scales disagree; SDSS ~0.2–0.3 dex above Te | `:83-84` region + abstract | CONFIRMED |
| 7 | observed −0.40 vs TNG −0.27, within 0.1–0.15 systematic ⇒ not significant | `:43-45` ("factor ∼1.5 short") | CONFIRMED |
| 8 | robust = SF over-growth; metallicity scale-limited | abstract `:45` | CONFIRMED |

G2 action: correct scene 5 to 0.8–1.0 dex; optional gap/per-z values.

## Summary

- Mandatory G2 rewrites: **massive-abundance scenes 3–6 (superseded numbers), scaling-relations scenes 4–5 (superseded interpretation), tng-validation scene 5 (0.9→0.8–1.0)**.
- Strengthen/extend (recommended): scaling-relations 6+8, z9 scene 4 precision, tng scene 5 gap values.
- No rewrite: z9-metallicity (all confirmed), mzr-framework (identical freeze).
- Live-V3 implication (decision already flagged to Duho, no action): public V3 currently narrates 2.7×/0.28 dex/~1 dex/13×-covered and the pre-selection-aware SFMS story — all superseded by the papers' own current versions.

## Exact next gate

**G2 — V4 narration rewrite (Hwao drafts, Lana signs), scope exactly the scenes listed above, every number anchored to `sources-v4/*.md` lines, before any audio/lip-sync/layout work.** Then G3 (plot inventory + Kun crop|redraw verdicts — G0's vector crops and figure inventory give it a head start).

HWAO_V4_G1_CLAIM_DIFF_COMPLETE
