# Kun report + Tori progress video — final receipt

Marker: `KUN_TORI_PROGRESS_VIDEO_FINAL_PASS_V1`
Completed: `2026-07-22T11:10:39Z`
Status: **PASS · local review master complete**

## Deliverables

- Video: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-tori-progress-video-20260722T105357Z/KUN_REPORT_TORI_PROGRESS_REVIEW_V1.mp4`
- Captions: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-tori-progress-video-20260722T105357Z/KUN_REPORT_TORI_PROGRESS_REVIEW_V1.srt`
- Narration: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-tori-progress-video-20260722T105357Z/kun_tori_progress_female_narration.wav`
- Plan: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-tori-progress-video-20260722T105357Z/plan.md`
- Source freeze: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-tori-progress-video-20260722T105357Z/source_freeze.json`
- Reproducible builder: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-tori-progress-video-20260722T105357Z/build.py`
- Temporal contact sheet: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-tori-progress-video-20260722T105357Z/qa/final_temporal_sheet.png`
- Independent ASR transcript: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-tori-progress-video-20260722T105357Z/qa/asr_base_en.txt`

## Media contract

- Duration: `88.000000` seconds
- Resolution: `1280 × 720`
- Frame rate: `30/1`
- Video: H.264, 2,640 frames, yuv420p
- Audio: AAC, stereo, 48 kHz
- Size: `4,629,734` bytes
- Full video/audio decode: PASS
- Fast-start flag requested during final mux
- Black intervals longer than 0.9 seconds: none

## Audio contract

- Voice: `en-US-EmmaNeural`
- Voice metadata: clearly female
- Music: none
- Mean volume: `−19.2 dB`
- Peak volume: `−4.5 dB`
- Silent portrait opening: intentional
- Silent portrait outro: intentional
- Scene-boundary pauses: intentional breathing room
- Presenter policy: the approved synthetic Flow astronomer appears only during silent opening and outro; she is never shown narrating without exact lip-sync.

Independent faster-whisper `base.en` ASR recovered the complete semantic arc, counts, failure/pass order, frozen/uncommitted status, and gated boundary. It substituted ordinary English variants for custom names (`Kun`, `Tori`, `Hwao`) and read `Git` as `get`; the burned-in captions and SRT retain the canonical spellings and are authoritative for proper nouns.

## Semantic contract

Required caption phrases: `11 / 11` present.

- healthy, with risks
- 36 files
- 380 worktree entries
- rework piecemeal
- 20 modified files
- custody and receipt verification
- two honest failures
- unconditional pass
- 18 test database files
- cleanup has not started
- remain gated

Forbidden implications found: none.

- No `cleanup approved`
- No `cleanup has started`
- No claim that the whole Kun plan is complete
- No volatile branch-behind count
- No attribution of sole Surveys authorship to Tori

SRT:

- 18 cues
- monotonic, non-overlapping timing
- first cue: `00:00:03,350`
- final cue ends: `00:01:25,300`
- SHA-256: `2a0daf3304315ca0c920a442e052864e95c5e6e7ea6e560e2c24ccd072100e03`

## Visual QA

PASS on actual encoded frames.

- Eight-scene narrative order is correct.
- Approved astronomer portrait is polished and consistently integrated.
- No title, card, caption, or footer clipping.
- Classification counts and exact-proportion bar are readable.
- Surveys timeline reads `FAIL → FAIL → PASS → HWAO CLOSED`.
- Tori is correctly credited with custody and receipt verification.
- Surveys V2 is visibly `FROZEN · UNCOMMITTED`.
- Kun scope reads `18 test database files`, `10 cache directories`, `2 + 8`, and `0 safety counters`.
- Complete work and held/closed work are visually separated.
- Phase 4 is described as scope-defined; the video does not imply that cleanup started.

The first render truncated the last burned-in narration line in scenes 5 and 6. That master was rejected. The builder was corrected to fit all narration into three lines and to fail rather than truncate if future text exceeds the panel. The final master was fully re-rendered and re-QA'd.

## Source integrity

- Frozen source records: 8
- Source drift before build: none
- Source drift immediately before final mux: none
- Hwao boundary marker: `HWAO_KUN_TORI_VIDEO_SOURCE_BOUNDARY_COMPLETE_20260722`
- Kun live marker: `KUN_PHASE4_CORRECTED_SCOPE_VERIFIED_20260722`

## Hashes

- Video: `5b43cb9cb26c7a3fb91f709734346b3377cf1569af7e28e40ea5f4c457d769db`
- Narration: `ef3400cb42615ae01f60ee3574724230690010d2aacfb26c7336077e93a2477f`
- Scene sheet: `0a96beff132f250fb9f10f3a544fde823a8b881dd1511ea2ac74c4ece6fe198b`
- Temporal contact sheet: `d9426ad19643e808c67a788584094b7bf5e6e6f16cd4696c4e1fdb79b654500e`
- Source freeze: `e205e45170865a2e3235cd01730c6fcf29125d9a538e7017095294015e4782b1`
- Plan: `75e5ac9292ff0366178617301ceb0eb10ab78dfad3e060f7cd9406afef97b4b0`
- Builder: `8776635763581c39b73eeaf2c54c7f4dfe6cf51fe628dfc9a4366e210d9286cc`

## Safety and publication state

- Local review artifact only
- No upload or publication
- No website or cockpit change
- No runtime, deploy, or restart
- No DB, SQL, or migration action
- No Git commit, push, merge, branch, or worktree action
- No cleanup, file deletion, or quarantine execution
- No secret or `.env` content read
