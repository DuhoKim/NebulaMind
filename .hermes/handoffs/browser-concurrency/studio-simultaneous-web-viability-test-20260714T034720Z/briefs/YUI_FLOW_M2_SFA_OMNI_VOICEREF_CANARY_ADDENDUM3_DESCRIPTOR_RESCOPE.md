# ADDENDUM 3 — canary re-scoped to Omni Flash DESCRIPTOR-VOICE test (Duho-approved)

Issued by Hwao 2026-07-17. Amends brief (`315b3657…`), Addendum 1 (`f21be79c…`), Addendum 2 (`b36cd7b2…`), attach map (`35d5b243…`). Marker unchanged: `M2_SFA_OMNI_VOICEREF_CANARY_20260716`.

## Finding of record (canary result #1, zero credits)

The Omni Flash **voice-reference route does not exist in the current Flow UI** for this project. Exact DOM 2026-07-17: the voice picker (composer bottom-left add_2 → Voices tab) lists **built-in voices only** (e.g. Achernar); there is no vo_test_01, Create New Voice, Custom Voice, or Voice Reference item. A dragged media file becomes a generic ingredient chip (cancel+videocam, click-to-remove), not a voice role. `ROUTE_UNAVAILABLE` — record in the acceptance JSON.

## Duho's ruling

The one authorized submit becomes a **descriptor-voice canary**: same exact prompt (narrator descriptor + verbatim line), no voice selection, testing whether Omni Flash's prompt-driven voice passes the series voice-match gate at ~12 credits/clip instead of Veo Quality's 100.

## Amended config gate (replaces "voice reference attached")

- **Composer must be CLEAN: no ingredient/media chip, no voice_selection chip.** A stray media chip would turn the job into ingredients-to-video. Duho removes the generic chip at x219,y800 with one click (verified semantics: click removes), then says "clean".
- Model label exactly **Gemini Omni Flash** · **8s / 16:9 / 1x** · exact displayed credits recorded, **≤30** (expect 12).
- Prompt: the original brief prompt VERBATIM (it already contains the descriptor and the exact narration line). No voice picker interaction.

## Yui resume (on "clean")

1. Broker account-submission lease.
2. Read-only verify: model label · **no chips of any kind in composer** · 8s · 16:9 · 1x · exact credits ≤30.
3. Paste brief prompt → re-verify (config unchanged, still chip-free) → **submit once**.
4. Poll to terminal (accepted-then-Failed = outage, no retry). Download.
5. Post checks unchanged: verbatim word-for-word transcript · voice-match vs `vo_test_01` features within PGR analyzer tolerances · no on-screen speaker/captions/text · ≈8s · sane audio levels.
6. Output per brief: `vo_sfa_canary_01.mp4` + `M2_SFA_VOICEREF_CANARY_ACCEPTANCE.json` (include ROUTE_UNAVAILABLE finding + exact credits) + lane state + lease release. Zero further submits either way.

## Outcome semantics

- **PASS** ⇒ M2 narration route = Omni Flash descriptor voice (~12/clip); Hwao issues the M2 batch brief on the receipt.
- **FAIL** ⇒ M2 narration route = Veo 3.1 Quality descriptor (PGR-proven, ~100/clip); no canary retry.
- STOP + hold on any google.com/sorry or challenge, as always.
