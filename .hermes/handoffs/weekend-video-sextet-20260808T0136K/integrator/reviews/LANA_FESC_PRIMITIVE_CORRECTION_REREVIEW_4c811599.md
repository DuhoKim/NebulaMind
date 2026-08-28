# Lana — FESC primitive-correction exact-hash re-review

**Decision: PASS**  
**HOLD: no**  
**Blocking timestamps: none**  
**Reviewer:** Lana  
**Scope:** narrative/science/visual re-gate of one frozen FESC lane only; no promotion, upload, deployment, public-file copy, or candidate mutation authorized or performed.

## Exact object reviewed

- Candidate: `canaries/fesc-method-overhaul-canary-20260809T1420K/fesc-method-overhaul-canary-20260809T1420K.mp4`
- **Independently measured SHA-256:** `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9`
- Required SHA-256: `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9`
- Size: `9,993,751` bytes
- Probe: H.264, 1920×1080, 30 fps, 236.733333 s video; mono AAC, 48 kHz, 236.739000 s audio; container duration 236.739000 s.
- Full video+audio decode with `ffmpeg -xerror`: **PASS**, no decode error.
- Correction receipt independently measured SHA-256: `50a305b03d1a6b9b0395ad407342fbf7a600426aa4dbf70454d9b64378f40334` (**matches required**).

The decision is bound only to the exact MP4 hash above. It does not transfer to the held predecessor `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0` or to any future render.

## Encoded-frame review performed

I reviewed the actual encoded output, not only the spec or renderer:

1. Freshly decoded the whole MP4 at 2 fps, 960×540: **473 frames**.
2. Compared the fresh decode against `frame-review-2fps/frames/`: **473/473 files byte-identical and pixel-identical**. This binds the existing frame-review set to the exact reviewed MP4.
3. Inspected all ten full-sequence sheets covering **0.000–236.000 s**, including scene transitions, title/chrome, captions, and the complete narrative progression.
4. Freshly decoded the eight former-blocker timestamps at 1920×1080. All **8/8 fresh JPEGs were byte-identical and pixel-identical** to the stored `exact-reported-times` frames.
5. Inspected full-resolution calculation-peak frames at 83.130, 84.911, 87.137, 89.363, and 91.143 s, plus every 2 fps peak frame throughout approximately 59.5–111.5 s.
6. Bound the encoded AAC to `audio/narration_master.wav`: zero measured lag at 16 kHz; normalized correlation `0.9999955134` over the opening 40 s and `0.9999956398` over the full track. The 18.1875 ms decoded-duration tail difference is AAC padding, not narrative drift.

## Former-blocker disposition

| Former blocker time | Encoded narrative state | Primitive observed | Result-bearing geometry / overclaim | Status |
|---:|---|---|---|---|
| 5.052 s | `WHY THE BUDGET NEEDS A DISCRIMINANT` | blue and purple pairs of separated, equal-length horizontal strokes | none | **CLEAR** |
| 15.013 s | `THE PHYSICAL POSSIBILITY` | blue and purple pairs of separated, equal-length horizontal strokes | none | **CLEAR** |
| 24.243 s | `THE MODEL POSSIBILITY` | blue and purple pairs of separated, equal-length horizontal strokes | none | **CLEAR** |
| 31.816 s | `THE QUESTION THAT DRIVES THE METHOD` | blue and purple pairs of separated, equal-length horizontal strokes | none | **CLEAR** |
| 42.050 s | `WHY ONE SLICE CANNOT SETTLE IT` | one amber pair of separated, equal-length horizontal strokes | none | **CLEAR** |
| 51.592 s | `THE AMBIGUITY LIVES ACROSS A SWEEP` | one amber pair of separated, equal-length horizontal strokes | none | **CLEAR** |
| 222.410 s | `GALAXIES OR ASSUMPTIONS?` | blue and purple pairs of separated, equal-length horizontal strokes | none | **CLEAR** |
| 231.051 s | `THE METHOD EARNS THE ANSWER` | blue and purple pairs of separated, equal-length horizontal strokes | none | **CLEAR** |

At all eight exact times the old rising/falling intersecting-curve glyph is gone. The primitive has no axes, point marks, changing height, slope, rise/fall, intersection, crossing, branch ordering, curve shape, or selected result. Rounded endcaps do not form a curve trace. Symmetric arrows elsewhere on the cards are process connectors only; they do not encode a scientific order or slope.

## Fresh narrative / science / visual findings

### Opening and persistent title — PASS

The encoded opening remains conditional and FESC-lane-specific:

- the apparent budget can arise from a genuine galaxy shortfall **or** transported/frozen assumptions;
- `If ... would ...` introduces the genuine physical possibility;
- `could instead ... not about the galaxies` introduces the apparent/model possibility;
- the opening closes with the discriminating question rather than a result.

The corrected title **“An apparent photon-budget mismatch has two explanations”** is present from the opening through the final frame across the exhaustive 2 fps sweep. I found no stale title, typo, replacement title, clipping, or title dropout.

### Result-geometry and selection gate — PASS

Across all 473 reviewed narrative frames and all eight exact-time frames, I found:

- no readable scientific/result order between the two explanations;
- no crossing or intersection geometry;
- no slope, rise/fall, or trend trace;
- no plotted result, curve, point, threshold, count, or positional result geometry;
- no selected sign, value, estimator state, explanation, or evidence-supported branch;
- no numeric result claim.

The visible left-to-right arrows and step labels describe method topology (`DECLARE`, `PROPAGATE`, `PAIR`, `CHALLENGE`, `COMPARE`) only. They do not rank or order the scientific alternatives. The estimator keeps `VALUE WITHHELD`, presents `REQUIRED LOWER`, `ENVELOPES OVERLAP`, and `REQUIRED HIGHER` with equal inactive styling, and states `NO SIGN SELECTED`.

The renderer snapshot corroborates the encoded result: the only icon kind used by this lane is `paired_strokes`; `icon="curve"` is rejected; the curve-icon rendering branch is absent. The internal peak-mode name `curve` remains only as a renderer mode label—the encoded peak contains matched cards, not curve geometry.

### Equal-height calculation-arm peak — PASS

The encoded peak preserves equal visual rank. Every inspected peak state shows two matched declared-calculation cards with aligned tops and bottoms, joined to `SAME GRID / SAME PRIORS` by horizontal connectors. Full-resolution frames show no vertical offset, sloped comparison, crossing, or positional winner. The renderer snapshot independently corroborates identical arm geometry: both cards are 650×255 px at y=315–570.

The peak still teaches the intended method: matched redshift sweep, declared prior propagation, dual-proxy non-circularity, challenged source-density corner, and external proxy-transport boundary. Banners continue to say `NO RESULT GEOMETRY`, `VALUES WITHHELD`, or `OUTCOME WITHHELD` where required.

### Discipline, boundary, and payoff close — PASS

The discipline sequence remains intact:

- anchors, redshift grid, estimator, and systematic corners are locked before inspection;
- later choice is prohibited;
- `WHOLE SWEEP FIRST · CLAIM LAST` remains explicit.

The scientific boundary remains intact and non-overclaiming:

- **KNOWN NOW:** budget formalism, sweep design, systematic controls;
- **NOT REPORTABLE:** curve values, crossing or sign, claim about galaxies;
- **NEXT SCIENTIFIC GATE:** independent source freeze, numeric verification, explicit result gate.

The payoff returns to the opening alternatives without choosing one. It retains `METHOD DESIGNED · VALUE AND SIGN WITHHELD`, then closes with `NO RESULT CLAIM IN THIS CANARY` and the statement that the method can separate the explanations **without asserting which one the unfrozen evidence supports**.

The spec/timeline contains 22 grounded records, no numeric literal in narration or visual parameters, and `video_reportable_now: false`. I found no scientific overclaim in captions, banners, branch labels, controls, discipline, boundary, or payoff.

## Gates closed

- **G0 exact-hash custody:** CLOSED / PASS
- **G1 stream probe and full decode:** CLOSED / PASS
- **G2 exhaustive full-narrative 2 fps frame sweep:** CLOSED / PASS
- **G3 eight former-blocker exact-time full-resolution checks:** CLOSED / PASS
- **G4 primitive/non-graph geometry:** CLOSED / PASS
- **G5 no scientific order, crossing, slope, or result geometry:** CLOSED / PASS
- **G6 no selected sign/value/result branch:** CLOSED / PASS
- **G7 conditional FESC introduction and corrected persistent title:** CLOSED / PASS
- **G8 equal-height matched calculation arms:** CLOSED / PASS
- **G9 source/sample result suppression and estimator withholding:** CLOSED / PASS
- **G10 discipline and scientific-boundary language:** CLOSED / PASS
- **G11 payoff close and no-overclaim boundary:** CLOSED / PASS
- **G12 encoded-audio narrative lineage:** CLOSED / PASS

## Final disposition

**PASS. Blockers: none.**

The eight primitive-correction blocker times are clear on the exact reviewed hash. The frozen predecessor's decorative-curve hold is resolved in this candidate without weakening the conditional introduction, persistent title, calculation-arm parity, method discipline, scientific boundary, or payoff close. This packet is a review verdict only; it is not a promotion or publication authorization.
