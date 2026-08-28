# Integration ledger — introduction rebuild v3

Candidate workspace: `spin-method-overhaul-canary-20260808T1959K`
Current state: `BLOCKED_BEFORE_SYNTHESIS_OPENAI_AUDIO_GATEWAY_UNAVAILABLE`

## 2026-08-08T19:59:44+0900 — introduction order accepted

Read `reviews/HWAO_INTRODUCTION_ORDER.md` in full. The accepted-with-incident predecessor remains:

- MP4 SHA-256 `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- narration v2 SHA-256 `3f033dd02d00767c6bb4cc1baf8b7197a78847bad076411cbaed9aab732cd416`

Neither predecessor file was edited, copied over, or replaced.

## 2026-08-08T20:00–20:08+0900 — work completed before audio

1. Authored `narration_script_v3.json` with the four required opening moves before the existing technical question:
   - two handednesses;
   - conditional sky/universe motivation;
   - conditional human-sorters alternative;
   - `How do we tell the two apart?`
2. Preserved the mirror as the largest spoken section: 64 words versus 46 for the new motivation.
3. Preserved the v2 mirror climax, frozen-method discipline, parallel funnel, withheld symbolic estimator and symmetric sign rail, design-only control matrix, self-imposed scientific gates, boundary, and closing payoff.
4. Created `storyboard_v3.json` with 27 states and explicitly provisional preview timing. It is not audio timing and cannot authorize encoding.
5. Added four graphics-first opening states to the isolated `build.py`: paired CW/ACW spirals, an `IF GENUINE` sky/universe lane, a `COULD ARISE IN SORTING` sorters lane, and both lanes pointing into `HOW DO WE TELL THEM APART?`.
6. Rendered native-resolution provisional storyboard frames and `storyboard-contact-sheet-v3.jpg`. No audio or MP4 was created.
7. Updated the isolated synthesis, PCM assembly, renderer, and encoded-QA scripts to the v3 paths. The renderer hard-fails if final PCM timing and the Alloy master do not exist.
8. Refroze current authority and predecessor identities in `source_manifest_v3.json`; `video_reportable_now` remains false.

## 2026-08-08T20:09:29+0900 — hard blocker recorded

Coordinator-reported managed-gateway state:

- `resolve_managed_tool_gateway('openai-audio')` repeatedly returns `None`;
- `logged_in=false`;
- `is_paid=false`;
- `tool_gateway_entitled=false`;
- `tool_access=null`.

Classification: logged-out/entitlement failure, not a balance question.

Decision:

- did not invoke synthesis;
- did not create `audio_v3/`;
- did not invoke Edge TTS or another voice;
- did not render a provisional MP4;
- did not copy anything into cockpit, shared video, or public roots.

A dry render-guard check exited nonzero with `BLOCKED_BEFORE_SYNTHESIS` and left no MP4.

## Exact resume point

When the managed OpenAI audio gateway is restored, run the already-prepared v3 lineage in this order:

1. `python3 synthesize_v3.py` — 27 fresh Alloy calls at speed 1.18.
2. `python3 assemble_audio_v3.py` — derive all starts, pauses, subtitles, and duration from decoded PCM sample counts.
3. `python3 build.py --preview` — regenerate final-timing frames and inspect introduction plus inherited critical states.
4. `python3 build.py --render` — encode one new MP4 only in this versioned directory.
5. `python3 qa_encoded.py` — full encoded QA and reviewer handoff.

No action beyond this synthesis boundary is authorized while the gateway is unavailable.

## 2026-08-09T00:11:29+0900 — gateway restored; v3 rendered and self-QA cleared

The Mac Studio authentication store was restored. The earlier blocker was machine-local: prior login
actions occurred on the MacBook Pro, not on the Studio where synthesis runs.

Execution:

1. Synthesized all 27 v3 sentences afresh through the managed OpenAI audio gateway using
   `gpt-4o-mini-tts`, voice `alloy`, speed `1.18`; no predecessor audio and no fallback voice were used.
2. Decoded every sentence master to PCM and derived the final timeline from sample counts. Final
   narration is 354 words at 115.000 WPM; master duration is 187.695646 seconds; maximum start-frame
   quantization delta is 0.016584 seconds.
3. Regenerated and inspected the final-timing contact sheet. The mirror remains the longest section:
   28.440 seconds versus 17.370 seconds for the motivation.
4. Encoded one isolated MP4:
   `spin-method-overhaul-canary-20260808T1959K.mp4`, SHA-256
   `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`.
5. Full H.264/AAC decode passed. Encoded QA passed 26/26 checks; all 27 sentence frames are nonblack,
   five mirror positions are unique, no freeze reaches eight seconds, and OCR has no forbidden or
   internal-filename hits.
6. Transcribed the four-sentence introduction from the encoded MP4. Whisper returned the exact expected
   text, including `If one were`, `would be`, `apparent excess`, `could instead`, and the complete final
   question; normalized match is 1.0.
7. Re-verified predecessor preservation: MP4 `40804f86…` and `narration_script_v2.json` retain their
   frozen hashes.

Disposition: local self-QA PASS; pending independent post-encoded review. `video_reportable_now` remains
false. No upload, cockpit/video-root copy, Git action, deletion, or public operation was performed.
