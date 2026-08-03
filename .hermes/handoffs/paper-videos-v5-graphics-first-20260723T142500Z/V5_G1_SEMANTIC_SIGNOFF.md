# V5-G1 SEMANTIC SIGN-OFF — z9 voice-canary passage

Coordinator: Hwao · Lana semantic hat (honest record: ruling executed by Hwao in-lane, falsifiable via anchors) · 2026-07-24 KST
Scope: `V5_G1_VOICE_CANARY_SPEC.json` only. Gate released: V5-G1 only. No animation, video, or public action; audio synthesis is Tori's bounded next step.

## Contract compliance — PASS on every required element

| Requirement | Where satisfied |
|---|---|
| 85–110 words | 108 words (per-sentence counts recorded in spec: 11+11+15+16+14+12+11+11+7) |
| 45–60 s at 105–125 delivered WPM | ~48 s raw speech at Kokoro speed 1.0 (~134 raw WPM) + 8 pauses × 0.6–1.0 s ⇒ expected ~53–57 s ⇒ ~114–122 delivered WPM, inside band with tuning margin |
| am_michael, natural speed 1.0 | voice_contract; slowdown via pauses only, model speed untouched |
| Short causal sentences | 9 sentences, mean 12 words, explicit causal links ("so", "because") in S2/S4/S5 |
| Oxygen abundance in plain language before any formal method | S1 defines it; the method (S5) comes four sentences later |
| Redshift-9–10 question | S3 (`:26-33`) |
| Five strictly unlensed galaxies | S5 (`:33`) |
| Why lensing/benchmark choices matter | S4 — lensing distorts masses (`:26-31`), benchmark extrapolated (`:73-74`, `:94-96`) |
| Direct electron-temperature measurement | S5 (`:33`), stated without superlative |
| Central result plain-form first, dex after | S6 "near one fifth" then S7 "zero point six nine dex" — arithmetic check: 10^−0.69 ≈ 0.204 ≈ one fifth ✓ (`:34`) |
| Small-sample / absolute-scale uncertainty | S8 — sample-limited (`:101-102`), Te scale 0.1–0.2 dex debated (`:43`, `:113`) |
| Verbatim boundary | S9 = "This is not a formal statistical detection." — exact contract phrase (`:43`, `:135`) |
| Per-sentence synthesis boundaries | Every sentence is a standalone synthesis unit ending in a full stop; no mid-sentence clause splits; pause plan [0.6, 1.0] s |

## Avoid-list verification — CLEAN

- No cosmic-age conversion (redshift stated as redshift; the V4 slot-0 age error cannot recur).
- No "clear answer"/certainty language — S6 says "The result:", S9 bounds it.
- No method superlatives ("most defensible" and kin absent).
- No cover-page wording.
- No invented values: the only numbers are redshift 9–10 (`:26-33`), five galaxies (`:33`), one fifth ↔ 0.69 dex (`:34`), all freeze-anchored; "one fifth" is derived arithmetic from an anchored value, not a new number.

## Anchor audit

All cited lines exist in the G0 current freeze extract `sources-v4/z9-metallicity.md` (text sha `094ae9f6…`, per `V4_SOURCE_FREEZE.json`) and were verified during G1/G2 of the V4 lane; no new anchor was introduced beyond that verified set.

## Ruling

**SIGNED — the passage is approved for V5-G1 audio synthesis exactly as written.** Any wording change voids this sign-off and requires re-signing before synthesis (and, downstream, the exact-audio rule keeps facial animation invalid until V5-G1 and V5-G2 pass).

Next bounded step (Tori, on this sign-off): synthesize per-sentence am_michael audio per the spec's voice_contract, write `V5_G1_AUDIO_RECEIPT.json` (per-sentence durations, total duration, measured delivered WPM, shas) in this lane, then stop for Duho's ear-check. Nothing else.

HWAO_V5_G1_VOICE_CANARY_SIGNED_COMPLETE
