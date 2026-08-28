# Pre-render QA — fesc-method-overhaul-canary-20260809T1420K

Timestamp: 2026-08-09T14:20:17+0900
Status: `CLEARED_FOR_LOCAL_FULL_RENDER`

- Frozen predecessor: `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0`; untouched.
- Scope is primitive-level and FESC-only: all eight `params.icon='curve'` declarations are now `paired_strokes` in both spec and timed records.
- Renderer no longer exposes a `curve` icon branch; validation rejects curve icons and unknown icon types.
- `paired_strokes` is two separated equal-length horizontal strokes with no axes, slope, relative response, order, intersection, or crossing.
- Preview contact sheet was inspected tile by tile. i01–i04, d01–d02, and x01–x02 show only the paired-stroke symbol. No former crossing glyph remains.
- Peak remains clean: equal-height `DECLARED CALCULATION ARM` cards, `MATCHED SWEEP DESIGN · NO RESULT GEOMETRY`, synchronous emphasis, no plot or crossing.
- Persistent title remains `An apparent photon-budget mismatch has two explanations` in every preview tile.
- Conditional introduction, FESC-specific science stake, discriminating peak, discipline framing, payoff close, and withheld `D(z)` value/sign are preserved.
- Narration is unchanged. Predecessor audio is reused byte-identically: managed OpenAI `gpt-4o-mini-tts`, Alloy voice, speed 1.18, one sentence per call, no music; audio master SHA-256 `8e40e71229fc3e0bf2f21e7f02f8c3370e1042a62ffadb03fb2ff10f96adf156`.
- No clipping, internal path/name exposure, sibling content, measured value, result direction, or interpretation appears.
- MZR-census and bright-end candidates were not touched.
- All external gates remain closed.

A post-encode actual-frame sweep is mandatory before local self-QA may pass.
