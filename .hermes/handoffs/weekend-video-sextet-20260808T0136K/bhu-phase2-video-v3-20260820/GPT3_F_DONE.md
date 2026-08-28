GPT3_F_COMPLETE

# GPT3 build-seat completion — BHU Phase 2 explainer v3

Packet gate: `PASS_P2V3_PACKET — token kimi-p2v3-gate-20260820T0215K`
Final MP4: `build/BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.mp4`
Final MP4 SHA-256: `46b670a5ee083153a07629b90f80ec71a1b362d0a191f6178bfaa9035d51bd96`
Final MP4 bytes: `36409327`
Duration: `706.833 s` (11.781 min)
Media: `1920x1080` at `30 fps`

## Final QA judgment

- Overall: `PASS_LOCAL_V3_RENDER_QA_READY_FOR_BOUNDED_KIMI_GATE`
- Full final-MP4 ASR: `PASS_FULL_FINAL_MP4_ASR_NO_CONTRACT_RESIDUALS`
- Cosmetic residuals: `1`
- Contract-bearing residuals: `0` — none accepted
- Captions: `PASS_EXACT_ENCODED_CAPTION_PAYLOADS`
- Plot walkthroughs: `PASS_FOUR_PINNED_PAPER_PLOTS_LARGE_ATTRIBUTED_WITH_ANIMATED_WALKTHROUGHS`
- Stills: `PASS_16_STILLS_1920X1080`
- Equations: `PASS_ONLY_THREE_PERMITTED_EQUATIONS`
- Full decode: `PASS`

Judgment: every residual reported by ASR is explicitly classified cosmetic versus contract-bearing in `ASR_QA.md`. The freeze is permitted only because contract-bearing residuals are zero.

## Narration contract

- Gateway model / voice: `gpt-4o-mini-tts` / `alloy`
- TTS speed parameter: `0.88`; voice sped up: `False`
- Measured narration-only pace: `126.208 wpm`
- Explicit panel-turn silence floor: `1.750 s`
- All 16 TTS input strings are byte-identical to `STORYBOARD.json`.

## Frozen narration WAV SHA-256

- Panel 01: `7f64034775795db162fd23410fba881e7a525bc017ca1658b00ec527133e7a0b`  `audio/narration-01.wav`
- Panel 02: `2d849040a13be8e3d233de0b3edd41150895fa49d9bc5ca503445be6565ec9ef`  `audio/narration-02.wav`
- Panel 03: `85d22dacfc17daf93792a4aa21580783f71c478fe6d8881f8223ba7d45d6da73`  `audio/narration-03.wav`
- Panel 04: `17993483cb19564c0052fb417c3b9ccb8f6874d6ab85595d174c727cb35587a6`  `audio/narration-04.wav`
- Panel 05: `c1d2689f89c70cc949c89bd489b2e0361dab08732662af4c105c60aefb18fa9e`  `audio/narration-05.wav`
- Panel 06: `d556605c572731287185aa301662cf07652d86f152f8c8b4ab9c85891685a407`  `audio/narration-06.wav`
- Panel 07: `d6120bebd9fc730b2eedbc2010d2bed44541dfae4892a41835ee91fec06f4d4b`  `audio/narration-07.wav`
- Panel 08: `f02ab09a8c00c2d1909c938243264f74ebafd830b0c20ba86e79c9efae15a1bf`  `audio/narration-08.wav`
- Panel 09: `575f7d77988aaca780c262639cd194c98460ca4cb9786912a21e9fb03fa679f8`  `audio/narration-09.wav`
- Panel 10: `68d726ebb07e3fc52a4d9e4adfb47d22519e1d20bb662552ec629fe862c3361f`  `audio/narration-10.wav`
- Panel 11: `335e1570e1c58ea40425c1e3658961d4ee7f6e542fe015714f83391551464ff3`  `audio/narration-11.wav`
- Panel 12: `68f4777337c22d1a4042773ddad5755274184a2c0f2ca85b7ef9094c22dec74c`  `audio/narration-12.wav`
- Panel 13: `4f19e74acbc9e58bd47889583ceb52cdf3aab643b9a84c9f7cc0a31f0bb59e29`  `audio/narration-13.wav`
- Panel 14: `9f1b19f370a9eb7d8dcdf13cc85610ff105b60a8109e422a5ab0412d1a3bae60`  `audio/narration-14.wav`
- Panel 15: `d864b53dfd586d7d4eb3a3fd0865265a2c9bd7a80bc98643db096be0d9e11c0d`  `audio/narration-15.wav`
- Panel 16: `c5dc27fb42733cdbf796d8b4a5a4777059c47525f618546dbb462dd92d1a7eba`  `audio/narration-16.wav`

## Frozen representative panel-still SHA-256

- Panel 01: `65480e9d867fdb0f16d91366edac8c5a8ae534b3a0dcce3512c1f9a3818c8540`  `PANEL_STILLS/panel_01.png`
- Panel 02: `33ee1dcd9b728fb6745391b47049ebb4dec34ce7a325c2121fac5dbffed7114b`  `PANEL_STILLS/panel_02.png`
- Panel 03: `a2054bf6156af953243cd36a9e79c75b481b0c22269c9a26bb20007fd33dc704`  `PANEL_STILLS/panel_03.png`
- Panel 04: `3ecc27cb3cbc77ab2f1dba668c55b56bc5ff45206f35a261c642a53f2f31af67`  `PANEL_STILLS/panel_04.png`
- Panel 05: `619f910573e04712cae3c09f709c6f581f75a79370065baed640e82f3bf2b620`  `PANEL_STILLS/panel_05.png`
- Panel 06: `3ed756e3c24e2d7be3cb10c9eb6caf2ced0868e58d66b98964867e36a44c9cf5`  `PANEL_STILLS/panel_06.png`
- Panel 07: `211f64cf81e99423c165da676987d4e81cc684815e1badba522320dfd0942306`  `PANEL_STILLS/panel_07.png`
- Panel 08: `19cf6a939366c307aef6cadcb3af0384eee16a591b44acce46bd7808797f8587`  `PANEL_STILLS/panel_08.png`
- Panel 09: `2837da6129b445f8b095b261684e2c7df26f100bbbc8eaebdd238c3208823480`  `PANEL_STILLS/panel_09.png`
- Panel 10: `28a2d0a30455a25a514abbbd87387c52f18347c8746ebeccffbfbe60daf43dc8`  `PANEL_STILLS/panel_10.png`
- Panel 11: `47170684e9c112fc212fd6a6f10782a6c42e91b5a661eee2a95aa00546822186`  `PANEL_STILLS/panel_11.png`
- Panel 12: `72fbc78cb5b717036ee0e5fbd739a3100ff8dceb02776583ef3791c0c11e634b`  `PANEL_STILLS/panel_12.png`
- Panel 13: `b9e6857d67b7f3d0fa8443da56292612c9c10b80de09ab2d5628fc0edfc45068`  `PANEL_STILLS/panel_13.png`
- Panel 14: `ebc2e1242fe5ce71feac5fce19368a66126cf2a79badf056bf59036f4cb2be27`  `PANEL_STILLS/panel_14.png`
- Panel 15: `fd8ac7db0231b2aa5f25d01fd1e36d7a4d3202d6b41aa996b61792341bf54bd4`  `PANEL_STILLS/panel_15.png`
- Panel 16: `9005395bc12b32f08af1e0848bb87e0d57f5b66d521d781bd10664317f6ebf0c`  `PANEL_STILLS/panel_16.png`

## CHIP-FIX PASS

- Re-encoded MP4 SHA-256: `46b670a5ee083153a07629b90f80ec71a1b362d0a191f6178bfaa9035d51bd96`  `build/BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.mp4`
- Panel 01 still SHA-256: `65480e9d867fdb0f16d91366edac8c5a8ae534b3a0dcce3512c1f9a3818c8540`  `build/PANEL_STILLS/panel_01.png`
- Panel 02 still SHA-256: `33ee1dcd9b728fb6745391b47049ebb4dec34ce7a325c2121fac5dbffed7114b`  `build/PANEL_STILLS/panel_02.png`
- Panel 11 still SHA-256: `47170684e9c112fc212fd6a6f10782a6c42e91b5a661eee2a95aa00546822186`  `build/PANEL_STILLS/panel_11.png`
- Change scope: the standard `NebulaMind rendering — Concept Illustration Only` DESIGN_SYSTEM pill was overlaid on P01, P02, and P11 only. Content and timing are otherwise unchanged.
- No audio change: the original AAC elementary stream was stream-copied byte-for-byte; SHA-256 before and after is `b4435da79b8432278f717bc7e4438af71510ff4c3ee302b80ba56a23c2d73efe`. All 16 narration WAVs and the narration master remain byte-identical.
- ASR is unaffected because audio was untouched; no ASR rerun was required.

## Boundary

Local-only review artifact. No upload, publication, deploy, cockpit write, database write, git write, generation-credit spend, or portal.nersc.gov access occurred.
