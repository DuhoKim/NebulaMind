# TORI — independent source/status, frame, and closed-gate verification

## PRE-BUILD PACKET — PRESERVE THIS SECTION

Timestamp: **2026-08-08 13:16:09 KST** / **2026-08-08 04:16:09 UTC**  
State: **PENDING_NEW_CANDIDATE**  
Scope: independent Tori receipt under `HWAO_OVERHAUL_ORDER.md`; no other Sextet review packet was read before this packet was authored.

This section records the state before the overhaul candidate exists. It is intentionally not a candidate verdict. When the new encoded candidate lands, Tori will append a timestamped amendment below rather than rewriting this evidence.

## 1. Provenance correction bound before review

**Primary rejected/watched artifact:**

`integrator/canaries/spin-method-canary-20260808T0204/spin-method-canary-20260808T0204.mp4`

- SHA-256: `2b1db4974f9830161015828ae44bb617345db476375204f5f079a7fd0485ccc1`
- Bytes: `1,943,640`
- Duration: `114.0 s`
- Encoded video: H.264, 1920×1080, 30 fps
- Audio: none; the file has one video stream only
- Full decode: PASS, `3,420` frames decoded through EOF with exit 0
- Contact-sheet SHA-256: `289cfe3aacceab967d59957aa0f329975e64b9d68a8350321092491ebcfdbce6`

This is the exact file Duho was linked to and rejected. `spin-method-canary-20260808T0648` is supplemental only; it was not the watched file. No amendment to an earlier Tori packet is needed because this packet was first written after the correction.

### What the primary 0204 artifact actually shows

I inspected the 0204 contact sheet and decoded MP4, not only its storyboard. It is an 11-card static deck: title/presenter still; paragraph/status cards; a giant standalone `667,944` card; a static funnel; a static equation; a static two-spiral mirroring schematic; more paragraph cards; a gate paragraph; and a presenter close. On-screen footers use internal filenames such as `T1_FUNNEL.json`, `SOURCE_FREEZE.json`, and `T1C_COLUMN_INTEGRITY.json` as audience provenance. The MP4 has no audio.

The primary artefact therefore directly exhibits the rejected grammar: presenter stills, a giant-number card, paragraph-dominant frames, internal filenames as citations, and long static holds. The later 0648 supplement preserves the same 11-card skeleton and changes only card 05. The diagnosis survives the provenance correction, but 0648 is not used as watch-history evidence.

## 2. Current source/status authority

Current files as read at the pre-build timestamp:

- `lanes/spin/SOURCE_FREEZE.json`: SHA-256 `f7204bd7aa9a96830e22b76456cd2e24b1fda4d543f2d0333c4f72cad8c98183`
- `lanes/spin/STATUS.json`: SHA-256 `38b0c676925c95456882f9a672dc5a78f8d5100ba728223ef61ae8bc4a5bd2fe`
- Corrected `HWAO_OVERHAUL_ORDER.md`: SHA-256 `af52516b021e9f0167a27c87b027fcb6e45022ad0643ad70ee62df20c66c0973`
- Corrected `reviews/REVIEW_BRIEFS.md`: SHA-256 `2a22cf9f67fec6fd5337a9e614f6f5d108411b39062b06bd57a56c2147d23eda`
- `reviews/TORI_USER_WATCHED_ARTIFACT_CORRECTION.md`: SHA-256 `6f4a1c978db681e076b3b0a6074032838bd37766f318ca7fadcd584b772f655b`

Independent hash/size replay: **17/17 freeze-bound files match** the sizes and SHA-256 values recorded by `SOURCE_FREEZE.json`, including the public spin MP4, storyboard of record, shared renderer, nine source artifacts, and five storyboard figures.

Scientific status remains absolute:

- `video_reportable_now: false`
- `decision: BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY`
- T3/T4 result values and figures remain quarantined.
- `FRAME_UNSTATED` and the missing post-run independent verdict record remain blockers.

Audio authority changed, but science authority did not:

- Current `STATUS.json` authorizes narration **only for method-only claims**, with Alloy, speed 1.18, no music, and 105–125 delivered wpm.
- `HWAO_OVERHAUL_ORDER.md` §2 explicitly supersedes the older silent-only restriction.
- The old `candidate_audio_contract` string still present near the end of `SOURCE_FREEZE.json` describes the earlier canary. It does not override the later Hwao order and current `STATUS.json`.
- `video_reportable_now` remains `false`; audio authorization does not authorize a result.

Allowed visual claims remain limited to the frozen sample funnel, symbolic equation with no measured value, handedness/mirroring convention, predeclared bias-control design, and an explicit unresolved-result boundary.

Forbidden content remains: T3/T4 results or figures; a measured asymmetry value or implied result direction; significance; dipole/parity/cosmology; GRB, SN Ia, dark energy, quasar, H0; black-hole-universe; or new DESI/Ganalyzer claims.

## 3. Pre-build candidate state

At 13:16:09 KST there is **no new overhaul directory and no new overhaul MP4** under `integrator/canaries/`. Therefore the following checks are not waived and are not guessed:

| Required encoded-candidate check | Pre-build state |
|---|---|
| Candidate path/hash/streams/duration | `PENDING_NEW_CANDIDATE` |
| Decode every encoded video frame through EOF | `PENDING_NEW_CANDIDATE` |
| Inspect actual frames, including figure text, axes, labels, and legends | `PENDING_NEW_CANDIDATE` |
| Forbidden-content negative sweep on encoded pixels | `PENDING_NEW_CANDIDATE` |
| Audio stream exists and is audible | `PENDING_NEW_CANDIDATE` |
| Private local playback reaches the end without truncation | `PENDING_NEW_CANDIDATE` |
| Final closed-gate recheck | `PENDING_NEW_CANDIDATE` |

## 4. Closed-gate pre-build receipt

These are task-scoped checks for the Sextet overhaul. They do not claim that unrelated, pre-existing host services are globally quiescent.

- **Upload/publication/YouTube:** PASS in observable task scope. No overhaul candidate exists, and no upload/publication action or receipt was produced.
- **Public/shared MP4 replacement:** PASS. `frontend/public/videos` has 5 MP4s and `/Users/duhokim/HermesOps/cockpit/videos` has 30 MP4s; zero have a modification time at or after the 13:02 KST overhaul order. The public spin alias still has frozen SHA-256 `dfc8be91c47bf55b34c0040d1b6572b5960e31942c9a0cec1465d8bcf4f44585` and size `1,059,019` bytes.
- **`frontend/public/videos`, `paperVideos.ts`, shared tools:** PASS for this task. No task write observed. The freeze-bound shared renderer still matches `919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c`.
- **Git writes:** PASS. Branch `feat/paper-workflow-v2`; HEAD remains `ebe9c7f587bfbdad30ea8cb62d42e51294e1599e`; cached diff is empty; `.git/index` SHA-256 remains `2b79ff47d5b9f8f0845f29246b877db512c4bc1b786b01c5c7d778afe57fffad`; latest reflog entry remains the 01:38 KST fast-forward. The review file itself is an untracked handoff artefact, not a Git operation.
- **Deletion of prior attempts:** PASS. All 11 pre-existing canary directories are present: spin `0204`, `0235`, `0256`, `0315`, `0325`, `0335`, `0345`, `0448`, `0648`; MZR census `1254`; and FESC `1259`. Their file counts and per-directory manifest hashes match the earlier Tori inventory. In particular, 0204 remains 14 files with manifest SHA-256 `23ef0235a438da9bcbf490ac384e6c58f4f5fa55378d157d4e73a7b38e685cae`, and 0648 remains 14 files with manifest SHA-256 `4ed944f4ebb8d0af37bda25da862cb4d4870332337d5421dd515c11c27874319`.
- **Cockpit, DB/SQL, deploy/restart, browser automation, billing/provider/config, secrets:** no such action was performed by Tori or observed in the candidate task, and no new candidate exists. This row must be rechecked after the build rather than inherited as a final assertion.

## 5. Pre-build disposition

**PENDING_NEW_CANDIDATE — no candidate verdict issued.**

The source/status gate is internally clear: narration is authorized only for method-only claims, while scientific reportability remains false. The corrected primary rejection evidence is 0204, not 0648. All encoded-frame, encoded-audio, private-playback, and final gate checks remain explicitly pending until the new versioned candidate lands.

---

## POST-BUILD AMENDMENT

### Encoded-candidate re-run — 2026-08-08 14:03:05 KST / 05:03:05 UTC

This is the required second pass. The pre-build evidence above is preserved unchanged.

**Exact frozen candidate reviewed:**

`integrator/canaries/spin-method-overhaul-canary-20260808T1312K/spin-method-overhaul-canary-20260808T1312K.mp4`

- SHA-256: `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- Bytes: `13,697,038`
- Duration: `159.000 s`
- Video: H.264 High, 1920×1080, 30 fps, `4,770` frames
- Audio: AAC LC, 48 kHz, mono, `159.000 s`
- Stability: the same byte size and SHA-256 were re-read after a further ≥20 s interval.

## 6. Source/status recheck at encoded-review time

The live lane authorities remain unchanged:

- `SOURCE_FREEZE.json`: SHA-256 `f7204bd7aa9a96830e22b76456cd2e24b1fda4d543f2d0333c4f72cad8c98183`
- `STATUS.json`: SHA-256 `38b0c676925c95456882f9a672dc5a78f8d5100ba728223ef61ae8bc4a5bd2fe`
- Freeze-bound replay: **17/17 files match** their recorded sizes and SHA-256 values.
- `video_reportable_now` is still **`false`**.
- `BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY` still governs.
- Narration remains authorized only for method claims. The encoded narration stays inside that method-only boundary.

Audio did not reopen the scientific gate. The candidate repeatedly marks itself `METHOD DESIGN · NO MEASURED VALUE`, withholds the estimator value, names no result direction, and closes on an unresolved gate-cleared answer.

## 7. Actual encoded-frame forbidden-content sweep

### Decode and pixel audit performed

- FFmpeg decoded both encoded streams through EOF with exit 0: all `4,770` video frames and the full AAC stream.
- I independently decoded and visually inspected all 24 sentence-midpoint frames from the MP4.
- I separately inspected six native-resolution end-state frames for the funnel, equation, controls, gates, boundary, and final payoff.
- I OCR-scanned independently decoded actual pixels at **2 fps** across the full runtime: `318/318` frames completed with zero OCR failures.
- The OCR forbidden-token sweep returned **0 hits** for T3, T4, significance/sigma, dipole, parity, cosmology, GRB, SN Ia, dark energy, quasar, H0, black-hole-universe, DESI, Ganalyzer, Legacy Survey, p-value, and z-score.
- A separate scan of all 357 renderer string literals and all 24 spoken sentences returned **0 forbidden-topic hits**. This supplements rather than substitutes for the pixel sweep.

OCR produced a few spurious small numerals while reading spiral strokes, grid marks, and equation glyphs (`25`, `35`, `555`, `6`, `7`, `8`). I opened those actual frames: none is rendered text or a scientific value.

### What is actually visible in the encoded figures

1. **Mirror sequence:** a single conceptual spiral undergoes a real horizontal transform. The visible disclaimer is `CONCEPTUAL — illustration, not data`. The labels resolve from `appears CLOCKWISE · CW` to `appears ANTICLOCKWISE · ACW`; the two design branches read `IMAGE-LINKED / MUST INVERT` and `LABELING PROCESS / NEED NOT INVERT`. No measured outcome is shown.
2. **Funnel:** `Galaxy Zoo 1 data release · Table 2` is the audience citation — no internal filename. The only counts/thresholds are the frozen allowed values: `667,944` source rows; `190,225` spiral-flag rows split into `161,172 decisive` and `29,053 ties`; `51,157` at dominance `≥ 0.60`; and `30,412` at dominance `≥ 0.80`. The branches are explicitly labelled `PARALLEL — NOT SEQUENTIAL`.
3. **Estimator:** the encoded equation is `A = (N_CW − N_ACW) / (N_CW + N_ACW)`. Numerator and denominator annotations are legible. The sign rail defines `A < 0 · more ACW`, `A = 0 · equal`, and `A > 0 · more CW`, while simultaneously showing `VALUE WITHHELD` and `no sign selected`. No value or direction is selected.
4. **Bias-control matrix:** the rows are `HORIZONTAL MIRROR → label response does not follow image inversion`, `0.60 / 0.80 THRESHOLDS → classification depends on one decisiveness cut`, and `PAIRED SAME OBJECT → aggregate change comes from sample composition`. The frame is explicitly marked `DESIGN ONLY · NO OUTCOMES`.
5. **Scientific gates:** `FROZEN METHOD → NEXT GATE INDEPENDENT VERDICT → EVIDENCE → RECEIPT → REFEREE` stops before a dim `ANSWER` node. The frame states `STORED-DIRECTION FRAME ALSO UNRESOLVED` and `STANDARD HOLDS HERE`; it contains no result.
6. **Boundary/payoff:** `KNOWN NOW` lists only the sample, symbolic estimator, mirror discriminant, and control design. `NOT REPORTABLE` lists measured value, result direction, and interpretation. The close re-poses `IMAGES OR LABELING PROCESS?` and leaves the gate-cleared answer absent.

There are no plot axes or data legends in this candidate; every diagram label, annotation, branch label, equation label, and audience citation was included in the checks above. No internal filename is rendered. No forbidden content or substantive result appears in the encoded pixels.

**Actual-frame/content verdict: PASS.**

## 8. Encoded audio and private playback

- The AAC stream exists, is coextensive with the video at `159.000 s`, and decodes without error.
- Measured integrated loudness is `−20.3 LUFS`; true peak is `−2.3 dBFS`; no clipping, NaN, Inf, or denormal sample was found.
- The 299-word master is inside the authorized 105–125 wpm band (`115.0` wpm on the recorded occupied interval; `112.8` words per full 159 s file).
- Local private playback used `ffplay` against this exact hash at volume 20. It started `13:59:56 KST`, reached EOF at `14:02:36 KST`, and exited 0.
- The encoded stream begins with about `0.67 s` of intentional silence and ends with about `2.60 s` of tail silence. The last narration ends before the file tail; audio and video both reach 159 s. Nothing is truncated.

**Audio/audibility/end-to-end playback verdict: PASS.**

## 9. Final closed-gate receipt

| Closed gate | Result | Evidence |
|---|---|---|
| External upload/publication/YouTube action | PASS in observable process/source scope | No uploader/publisher command, process, source call, or receipt was found. The only network operation in the build source is the explicitly authorized managed TTS synthesis. |
| `frontend/public/videos` | PASS | Still 5 MP4s; zero post-order MP4 mtimes. Frozen public spin alias remains `dfc8be91…`, 1,059,019 bytes. |
| `paperVideos.ts` | PASS | SHA-256 `e80eb76426067a671de834fb487a79b483542b6bb6a64b29f5489ff9e8c75f91`; mtime predates the order. |
| Shared renderer/tools | PASS | `tools/nm_paper_video.py` remains freeze hash `919af6b1…`; all 17 freeze-bound files still match. |
| Git writes | PASS | HEAD remains `ebe9c7f587bfbdad30ea8cb62d42e51294e1599e`; branch unchanged; cached diff empty; index SHA-256 `2b79ff47…`; latest reflog remains the 01:38 KST fast-forward. |
| Prior-attempt deletion/mutation | PASS | All 11 pre-build canary directories remain present and **11/11 manifest hashes match** the pre-build receipt, including primary 0204 and supplemental 0648. |
| DB/SQL, deploy/restart, browser automation, billing/provider/config, secrets | PASS in task scope | No such candidate-source operation or secret-named file was found. |
| **Shared/public MP4 and cockpit mutation** | **FAIL** | At `13:57:59 KST`, the exact candidate bytes were copied to `/Users/duhokim/HermesOps/cockpit/videos/_weekend-canaries/spin-method-overhaul-canary-20260808T1312K.mp4`. It is 13,697,038 bytes with the same SHA-256 `40804f86…`. This increased the cockpit MP4 count from 30 to 31 and is the only post-order MP4 there. |

The violating copy sits under `/Users/duhokim/HermesOps`, a root currently served by a long-running local `http.server` process; a long-running `cloudflared` tunnel is also present. I did not probe or infer an external URL, so I do not claim an external upload occurred. The copy itself is nevertheless a direct violation of the closed **shared/public MP4** and **cockpit** gates. I did not delete, move, or alter it.

## 10. Final disposition

### **HOLD — one closed gate failed**

- **PASS:** exact-hash stability, source/status authority, 17/17 freeze custody, actual-frame forbidden-content sweep, method-only claim boundary, encoded audio, local end-to-end playback, Git integrity, public frontend integrity, and preservation of every prior attempt.
- **HOLD:** the exact candidate was copied into a shared cockpit video path after the 13:02 KST order. The order required output only to a new versioned `integrator/canaries/` directory and explicitly closed cockpit/shared-public MP4 mutation.
- Scientific reportability remains **false** regardless of this presentation verdict.

No automatic cleanup is authorized. The exact next action is for Hwao/Duho to decide whether to authorize removal/containment of the shared cockpit copy or explicitly waive/reopen that gate; after that decision, Tori must recheck the served/shared roots and hashes before this HOLD can become PASS.

Evidence receipt: `reviews/tori-overhaul-evidence/40804f86/AUDIT_RECEIPT.json`.

---

## CONTAINMENT RECHECK AMENDMENT — 2026-08-08 14:18:38 KST / 05:18:38 UTC

This is an append-only containment decision. It does **not** rewrite or withdraw the 14:03 KST HOLD above: the cockpit-route breach happened, and that HOLD remains the permanent incident record. This section answers only whether the independently verified containment clears the candidate's current custody blocker.

I read `reviews/HWAO_GATE_BREACH_CONTAINMENT.md` as a containment claim and then reproduced its decisive checks rather than accepting Hwao's self-audit.

## 11. Four-file containment custody

The containment directory initially contained exactly the four staged payloads named by Hwao, each a regular non-symlink file. Every payload is byte-identical to its authoritative source under `integrator/canaries/`:

| Contained payload | Bytes | SHA-256 | Independent source comparison |
|---|---:|---|---|
| `spin-method-overhaul-canary-20260808T1312K.mp4` | 13,697,038 | `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9` | exact byte identity to the authoritative 1312K MP4 |
| `overhaul-1312K-contact-sheet.jpg` | 158,523 | `e1f1e9c4e8a6b74065d77ddf701bde11cf40ef37a4e26dfe3bee65a9b6834522` | exact byte identity to the authoritative 1312K contact sheet |
| `spin-method-canary-20260808T0648.mp4` | 2,308,085 | `6d81e1830febe5260df9093a84c4670c7e86179398125a8a64e6953897db6271` | exact byte identity to the supplemental 0648 MP4 |
| `spin-method-canary-20260808T0648-contact-sheet.jpg` | 285,047 | `b9724f423b87adac7dad498596399617b7a4ff0c6d89e30f8df9ac1bc505674e` | exact byte identity to the supplemental 0648 contact sheet |

The authoritative 1312K MP4 in the canary directory remains 13,697,038 bytes with SHA-256 `40804f86…`; containment did not modify or replace it. All 11 prior-attempt directory manifests also still match the pre-build inventory, including primary 0204 and supplemental 0648. Thus the move retained the breach evidence and did not delete a prior attempt.

## 12. Served/shared-root and withdrawn-route recheck

- `/Users/duhokim/HermesOps/cockpit/videos/_weekend-canaries/` is absent and is not a symlink.
- `/Users/duhokim/HermesOps/cockpit/videos` now contains 29 MP4s. The reduction from the 30-file pre-build state is explained by moving the already-staged 0648 MP4 as well as the post-order 1312K MP4 into the lane evidence directory; both still exist byte-identically in their authoritative canary directories and containment evidence.
- I size-filtered and SHA-256-checked `/Users/duhokim/HermesOps`, the working `frontend/public`, and the live-root `frontend/public` for **all four** staged payload identities. Every root returned zero hits for every staged SHA-256.
- A cache-bypassed GET to the old local cockpit backend path, `http://127.0.0.1:8093/cockpit/videos/_weekend-canaries/spin-method-overhaul-canary-20260808T1312K.mp4`, now returns HTTP `404`. The old directory URL also returns `404`, and the live cockpit-videos directory listing contains neither `_weekend-canaries` nor the candidate filename.
- The frontend-public probe for the same staged path returns `404`. `paperVideos.ts` remains SHA-256 `e80eb764…`, and the frozen public spin alias remains SHA-256 `dfc8be91…`.
- The long-running cockpit server and tunnel have no open deleted file descriptor naming `_weekend-canaries` or the candidate.

**Containment of the protected cockpit/shared-path copy: PASS.** The old protected-path route has been withdrawn, and no staged bytes remain under the checked served/shared roots.

## 13. User-directed private canary-root reachability

The candidate is deliberately reachable again through a different, private route supplied for this recheck:

`http://100.84.12.101:8765/spin-method-overhaul-canary-20260808T1312K.mp4`

Independent route receipt:

- HEAD: HTTP `200`, `Content-Type: video/mp4`, `Content-Length: 13,697,038`.
- Cache-bypassed full GET: `13,697,038` bytes, SHA-256 `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`, pipeline exit 0.
- `100.84.12.101` is inside the non-global CGNAT/Tailscale range `100.64.0.0/10`; it is not a globally routable address.
- The listener is PID `33243`, bound specifically to `100.84.12.101:8765`.
- Its command-line `--directory` and process working directory both resolve to the isolated authoritative canary directory:
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/integrator/canaries/spin-method-overhaul-canary-20260808T1312K`

This active route serves the authoritative canary bytes directly. It creates no copy under `cockpit/videos`, `frontend/public`, or another checked protected root. The newer user direction explicitly requests private viewing and this route recheck; it does not erase or retroactively authorize the earlier cockpit mutation.

The precise current statement is therefore: the **old breach route is dead**, while the **new private direct canary-root route is intentionally live and hash-correct**. It would be false to say the candidate is unreachable everywhere, and this report does not say that.

## 14. Continuity recheck

- Candidate: SHA-256 `40804f86…`, unchanged.
- `SOURCE_FREEZE.json`: SHA-256 `f7204bd7…`; **17/17** bound files still match.
- `STATUS.json`: SHA-256 `38b0c676…`; `video_reportable_now` remains **`false`**.
- Git: HEAD `ebe9c7f5…`, index SHA-256 `2b79ff47…`, cached diff empty.
- Prior-attempt custody: **11/11** pre-build manifests still match.
- Earlier encoded-pixel, forbidden-content, audio, and private-playback PASS findings remain bound to the same candidate bytes and do not require reinterpretation.

## 15. Current Tori disposition

### **PASS WITH INCIDENT**

- **Why not clean PASS:** the protected cockpit/shared-path mutation was real. The original HOLD remains valid for the time at which it was issued and stays above as incident history.
- **Why no longer HOLD:** all four staged payloads survive byte-identically in lane-scoped evidence; the violating directory is absent; the old route returns 404; all four staged hashes are absent from the checked served/shared roots; the authoritative candidate and all prior attempts remain intact; and private viewing now serves the authoritative canary directly from its isolated source directory.
- **Scope:** this clears Tori's current candidate custody blocker only. It does not change `video_reportable_now: false`, authorize scientific-result rendering or publication, erase the breach, or substitute for Hwao's coordination of the remaining seat/self-QA gates.

Current containment receipt: `reviews/tori-overhaul-evidence/40804f86/CONTAINMENT_RECHECK.json`.

### Queued-retry single-route confirmation — 2026-08-08 14:23:10 KST / 05:23:10 UTC

The queued containment instruction arrived after the independent amendment above had already landed. I did not duplicate or rewrite that verdict. I reran its decisive checks and add this idempotence receipt:

- The four containment payloads remain present, regular, and byte-identical to their authoritative canary sources.
- All four staged SHA-256 identities still have zero hits under `/Users/duhokim/HermesOps`, the working `frontend/public`, and the live-root `frontend/public`; `_weekend-canaries` remains absent.
- The old cockpit backend path still returns HTTP `404`.
- Port `8098` has no listener, and a direct probe fails with HTTP `000`/connection failure.
- Port `8765` is the only matching canary listener. Its full GET still returns 13,697,038 bytes with SHA-256 `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`, served in place from the isolated authoritative canary directory.

**Disposition unchanged: PASS WITH INCIDENT.** The retry confirms single-path containment; it does not erase the historical breach or the preserved HOLD.

---

## SUPERSEDING INTRODUCTION-REBUILD AMENDMENT — 2026-08-09 00:37:11 KST / 2026-08-08 15:37:11 UTC

This is an append-only review of a **different artifact**. It does not rewrite or reinterpret the earlier evidence for SHA-256 `40804f86…`. That predecessor remains preserved byte-for-byte with its **ACCEPTED WITH INCIDENT** disposition. The new artifact below supersedes it only for the next presentation decision.

## 16. Exact candidate binding and decode

- Candidate: `integrator/canaries/spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4`.
- Independently measured SHA-256: `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240` — exact match to the dispatched identity.
- Size: `16,065,978` bytes. Container duration: `187.695 s`.
- Streams: one H.264 High video stream, 1920×1080 at 30 fps; one AAC-LC mono audio stream at 48 kHz.
- Actual video stream: `5,630` decoded frames through EOF, duration `187.666667 s`. Audio reaches `187.695 s`; the sub-frame `0.028333 s` difference is below one 30-fps frame and does not truncate speech or a visual state.
- Full mapped video-plus-audio decode reached EOF with exit 0 and no decoder error.
- The post-encode freeze's 12 named files replay **12/12**, including this MP4, script, master audio, timeline, renderer, subtitles, encoded QA, and source manifest.

**Encoded-file identity/integrity verdict: PASS.**

## 17. Current source and status boundary

- `lanes/spin/SOURCE_FREEZE.json`: SHA-256 `f7204bd7…`; all **17/17** bound files still match their frozen hashes.
- `lanes/spin/STATUS.json`: SHA-256 `679cb3f6…`; `BLOCK_SUBSTANTIVE_RESULT_RENDER` and `video_reportable_now: false` remain in force.
- Current STATUS authorizes narration for the method-only overhaul while leaving scientific reportability unchanged. Its accepted-canary field still names predecessor `40804f86…`; it does not yet claim that this new artifact has been accepted.
- The candidate source manifest replays 16/17 against *current mutable origins*. The sole difference is `reviews/LANA_OVERHAUL.md`: its current 39,360-byte file begins with the exact frozen 32,578-byte copy and has a 6,782-byte append. The candidate-bound frozen copy remains exact. This is later review progress, not a source substitution; SOURCE_FREEZE and STATUS themselves are unchanged.
- The accepted-with-incident predecessor MP4 remains SHA-256 `40804f86…`, and `narration_script_v2.json` remains SHA-256 `3f033dd0…`.

**Source/status/continuity verdict: PASS.** Scientific result rendering remains blocked.

## 18. Independent actual-frame forbidden-content sweep

I decoded frames from the exact `c5e7deed…` MP4 rather than trusting the renderer, storyboard, self-QA, or pre-encode images:

- all 5,630 video frames decoded through EOF;
- **375** uniformly sampled actual encoded frames at 2 fps underwent independent OCR;
- **27** actual sentence-midpoint frames, **22** one-second opening frames, and **13** native critical frames were extracted independently;
- **62** decoded contact-sheet cells were inspected visually, including the opening, mirror sequence, funnel, full estimator and sign rail, controls, scientific gates, boundary, and final payoff;
- OCR completed on 375/375 samples with zero engine errors.

The OCR and visual sweep found **zero** occurrences of T3/T4 result material, significance, dipole, parity, cosmology, GRB, SN Ia/supernova, dark energy, quasar, H0, black-hole language, DESI, Ganalyzer, internal filenames, handoff paths, or source-code names. No measured result value, observed excess, preferred hand, selected sign, sky direction, significance, or cosmological interpretation appears.

### Introduction claim-boundary check

- The opening shows two equal conceptual handedness glyphs, `CLOCKWISE · CW` and `ANTICLOCKWISE · ACW`, under `TWO HANDEDNESSES`; neither is selected or assigned a count.
- The image-linked lane is explicitly conditional: `IF GENUINE` → `IMAGE-LINKED · SKY` → `FACT ABOUT THE UNIVERSE`.
- The alternative is explicitly non-assertive: `COULD ARISE IN SORTING` → `FACT ABOUT THE SORTERS`.
- The narration/caption uses `If one were … would be` and `apparent excess could instead`; both unresolved lanes feed `HOW DO WE TELL THEM APART?`.
- `universe` and `sky` occur only from OCR samples `4.25–21.25 s`; `sorters` only `9.75–21.25 s`; `excess` only `9.75–14.75 s`. None occurs after the introduction.
- Across all opening samples there is no count, selected direction, observed-result wording, significance, or claim that an excess exists. The language is motivation, not a visual or spoken scientific result.

### Figures, labels, legends, and numbers

- Funnel numbers are frozen source/sample counts only: `667,944`; `190,225` (`161,172` decisive + `29,053` ties); `51,157` at `0.60`; and `30,412` at `0.80`. The figure says `PARALLEL — NOT SEQUENTIAL`.
- The estimator remains symbolic: `A = (N_CW − N_ACW) / (N_CW + N_ACW)`. It carries `VALUE WITHHELD`, a symmetric `A < 0 / A = 0 / A > 0` definition rail, and `no sign selected`.
- The control matrix says `DESIGN ONLY · NO OUTCOMES`.
- The gate diagram stops before `ANSWER`; `STORED-DIRECTION FRAME ALSO UNRESOLVED` remains explicit.
- The boundary lists measured value, result direction, and interpretation as `NOT REPORTABLE`.

**Actual-frame forbidden-content and introduction-boundary verdict: PASS.** Sky/universe language remains wholly conditional and never becomes a result claim.

## 19. Required inherited presentation structure

- **Mirror as peak:** the mirror section occupies `28.440 s`, longer than the `17.370 s` motivation and every other section. Its conceptual animation, `MUST INVERT` versus `NEED NOT INVERT` predictions, and `MIRROR DISCRIMINANT` endpoint are present.
- **Frozen-method discipline:** `RULES FIXED BEFORE ANY NUMBER` and `WE TIED OUR OWN HANDS` survive; later-choice arrows are blocked rather than framed as tickets.
- **Withheld estimator:** full equation, symmetric sign rail, `VALUE WITHHELD`, and `no sign selected` survive.
- **Bias-control boundary:** the mirror/threshold/same-object matrix remains `DESIGN ONLY · NO OUTCOMES`.
- **Closing payoff:** the close returns to `IMAGES OR LABELING PROCESS?`, then `THE MIRROR TELLS THE EXPLANATIONS APART`; the gate-cleared answer remains explicitly missing/not yet reportable.
- **Method-design banner:** `METHOD DESIGN · NO MEASURED VALUE` is present from the first decoded opening frame through the final pre-fade samples.

**Inherited-deliverables verdict: PASS.**

## 20. Narration, loudness, timing, and private playback

- Script and SRT contain **27 sentences/cues** and normalize to the same text.
- Ordinary whitespace count is **353 words**, matching the dispatched description. The timing contract counts spoken `gate-cleared` as two words, for **354 delivered words**; this is a counting convention, not a script difference.
- `universe`, `sky`, and `sorters` each occur exactly once in the script.
- First narration starts at `0.600 s`; last sentence ends at `185.296 s`. The 354-word timing contract over `184.696 s` is `115.0 wpm`, within the authorized 105–125 band.
- Maximum recorded action-start/frame quantization delta is `0.016584 s`, below one 30-fps frame. Actual sentence-midpoint frames carry the corresponding captions and visual states.
- Encoded loudness is `−20.3 LUFS`; true peak is `−2.3 dBFS`; mean volume is `−21.5 dB`. Audio is non-silent and unclipped.
- Silence detection places the final speech end at about `184.988 s`, leaving about `2.724 s` of tail silence. The close is not cut off.
- Private full playback used `ffplay -nodisp -autoexit` against this exact candidate. It ran `00:28:10–00:31:18 KST` and exited 0 at EOF.

**Audio/private-playback verdict: PASS.**

## 21. Closed-gate and private-route receipt

| Gate | Independent result |
|---|---|
| Protected cockpit/shared-root copy | **PASS.** Candidate filename and exact hash have zero hits under `/Users/duhokim/HermesOps`, working `frontend/public`, and live-root `frontend/public`. `_weekend-canaries` remains absent. |
| Public video and registry | **PASS.** Public spin alias remains SHA-256 `dfc8be91…`; `paperVideos.ts` remains SHA-256 `e80eb764…` with zero worktree or cached diff. |
| Git | **PASS.** HEAD `ebe9c7f5…`, branch `feat/paper-workflow-v2`, index SHA-256 `2b79ff47…`, cached diff empty. |
| Predecessor preservation | **PASS.** `40804f86…` MP4 and `3f033dd0…` script remain exact. |
| Private route | **PASS.** Correct in-place URL is `http://100.84.12.101:8766/spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4`; independent HEAD/GET returned HTTP 200, `video/mp4`, 16,065,978 bytes, and SHA-256 `c5e7deed…`. PID 38142 is bound only to the non-global tailnet address and serves the authoritative `integrator/canaries` root in place. |
| Upload/publication/scientific release | **PASS in reviewed scope.** No protected-root copy or public registry mutation exists. The user-authorized tailnet viewing route is private; `video_reportable_now` remains false. |

**Closed-gate verdict: PASS.** The initial filename-only URL directly under port 8766 returns 404 because the server root is the parent `integrator/canaries`; the candidate-qualified URL above is the verified route.

## 22. Nonblocking raw-TTS receipt caveat

One reproducibility defect exists outside the final encoded-byte gate:

- `audio_v3/synthesis_receipt.json` and `timeline.json` record stale raw-MP3 hashes/sizes for `s21`, `s22`, and `s23`.
- Actual raw hashes are `522c975e…`, `64a93399…`, and `822cabda…`; the recorded hashes are `a7d7ff2e…`, `886b6a28…`, and `0370903d…`.
- All three actual files predate the synthesis receipt and the post-encode freeze. A candidate-tree ctime sweep found no build-input change after the post-encode freeze.
- Independently decoding the current raw MP3s to normalized PCM matches the stored decoded WAVs **27/27**, including those three records. The decoded-WAV hashes match the timeline 27/27; the frozen narration master, timeline, build receipt, and final MP4 all remain exact.

Therefore this is a **pre-freeze intermediate receipt inconsistency**, not an ambiguity in which audio reached the candidate and not a post-pickup mutation. It does not require a rerender and does not block the actual-frame/audio/closed-gate charge. If exact raw-TTS response-byte provenance is promoted to a hard package gate, the integrator should add an append-only correction for those three fields rather than rewriting this frozen candidate.

## 23. Tori disposition for `c5e7deed…`

### **PASS WITH NONBLOCKING RECEIPT CAVEAT**

- **PASS:** exact candidate identity and full decode; 17/17 SOURCE_FREEZE custody; current STATUS boundary; conditional introduction; 375-frame OCR sweep; 62-cell visual inspection; all inherited presentation elements; complete audio/private playback; predecessor preservation; Git/public-root integrity; and the verified in-place private route.
- **CAVEAT:** three raw intermediate MP3 hash/size fields in the synthesis receipt are stale, while the independently proved 27/27 PCM chain and all 12 post-encode frozen artifacts remain exact.
- **No scientific release:** `video_reportable_now` remains false. This is a presentation/custody review, not a scientific-result verdict or publication authorization.
- **Scope:** this passes Tori's assigned frame, source/status, playback, and closed-gate review. Hwao retains the final board accept/hold decision and any requirement for an append-only raw-receipt correction.

Evidence:

- `reviews/tori-overhaul-evidence/c5e7deed/AUDIT_RECEIPT.json`
- `reviews/tori-overhaul-evidence/c5e7deed/OCR_AUDIT_SUMMARY.json`
- `reviews/tori-overhaul-evidence/c5e7deed/ocr-2fps.json`
- `reviews/tori-overhaul-evidence/c5e7deed/contact-intro-actual-01.jpg` through `-04.jpg`
- `reviews/tori-overhaul-evidence/c5e7deed/contact-sentences-actual-01.jpg` through `-05.jpg`
- `reviews/tori-overhaul-evidence/c5e7deed/contact-critical-actual-01.jpg` through `-03.jpg`
