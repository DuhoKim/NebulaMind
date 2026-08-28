# Kun independent sibling-rollout review — audio, synchronization, and reproducibility

Review time: **2026-08-09 03:11:37 KST (+0900)**  
Authority: `HWAO_SIBLING_ROLLOUT_ORDER.md`  
Scope: the four completed local, method-only sibling canaries named by that order. This review does **not** authorize upload, publication, public/shared MP4 copies, cockpit mutation, Git action, deployment, or any result claim.

## Batch verdict

**KUN BATCH VERDICT: `HOLD_REPRODUCIBILITY`**

- **Audio and synchronization:** **PASS on all four exact MP4 hashes.** Full A/V decode reached EOF; stream, pace, PCM-timeline, action-start alignment, loudness/true-peak, encoded-introduction delivery, peak-duration, motion/no-freeze, and candidate hash bindings all independently replayed successfully.
- **Reproducibility:** **PASS for `mzr-anchor` in the current shared rollout workspace**, including a byte-exact clean-room rerender from a temporary candidate copy. **HOLD for `mzr-census`, `fesc`, and `brightend`** because their build receipts name historical renderer hashes whose bytes are no longer present anywhere in the handoff tree.
- The three HOLDs are **not media-quality failures** and do not dispute the exact frozen MP4 bytes. They are exact-rebuild blockers.

| lane | exact MP4 SHA-256 | audio/sync | reproducibility | Kun verdict |
|---|---|---|---|---|
| `mzr-census` | `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536` | PASS | HOLD — renderer `86ae01af…` absent | **HOLD** |
| `fesc` | `b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168` | PASS | HOLD — renderer `d14a5643…` absent | **HOLD** |
| `brightend` | `9a137c61011a3d9629c96ebbf365955295e11082cededa325ceb38f1ce268a2f` | PASS | HOLD — renderer `d14a5643…` absent | **HOLD** |
| `mzr-anchor` | `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970` | PASS | PASS — exact temporary rerender matched | **PASS WITH PORTABILITY CAVEAT** |

## Independent protocol

I did not treat `encoded_qa.json` or `RECEIPT.json` PASS labels as evidence by themselves. Against each exact candidate, I independently:

1. Recomputed the MP4 and all required receipt/manifest hashes; replayed every `source_manifest.json` entry by path, bytes, and SHA-256.
2. Full-decoded the video and audio streams through EOF with **ffmpeg 8.1.2** and independently counted decoded frames with ffprobe.
3. Probed H.264/AAC, 1920×1080, 30/1 fps, 48 kHz mono audio, encoded duration, and stream start times.
4. Checked the synthesis contract (`gpt-4o-mini-tts`, Alloy, speed 1.18, music false, one exact sentence per call), 22 unique sentence records, exact spec text/text hashes, MP3 hashes, sizes, durations, 24 kHz mono MP3 probes, and the matching shared/candidate sentence snapshots.
5. Fresh-decoded all **88** sentence MP3s to mono PCM s16le at 48 kHz and required byte identity with the stored decoded WAVs.
6. Rebuilt each raw narration master exactly from 48 kHz sentence sample spans plus recorded zero-sample gaps, then independently measured the scalar gain into `narration_master.wav`.
7. Recomputed every sample-to-second, frame-to-second, pause, cursor, and audio/visual action-start delta. One 30 fps frame is **33.333 ms**.
8. Recomputed delivered WPM from the first speech sample through the last speech sample, and recomputed every section interval from PCM-derived boundaries.
9. Decoded the AAC soundtrack and correlated it against the speech-only WAV master, establishing that the muxed soundtrack derives from the sentence assets plus silence rather than a music mix.
10. Independently remeasured integrated loudness and true peak from the encoded AAC.
11. Re-extracted each encoded introduction from the MP4 and required PCM identity with the stored STT input. I then ran a second ASR pass using **faster-whisper 1.2.1 / `Systran/faster-whisper-small.en`**, CPU int8, English, beam size 5. All required opening clauses survived.
12. Recomputed motion at 2 fps on 160×90 luma frames, including the longest interval below the 0.08 mean-absolute-difference threshold.
13. Searched **12,041 files smaller than 2 MB** throughout the handoff tree for the three recorded renderer hashes. The renderer is 27 KB, so this search covers any plausible preserved renderer copy.
14. For the only preserved exact renderer (`mzr-anchor`), cloned the candidate to `/tmp`, rerendered there without touching the frozen lane, compared the resulting MP4 SHA-256, and deleted the temporary copy.

## Shared audio and synchronization findings

- All four synthesis receipts record the required managed OpenAI audio route, `gpt-4o-mini-tts`, voice `alloy`, speed `1.18`, `music: false`, and `one exact sentence per call`.
- Each lane has 22 unique sentence records and 22 unique raw sentence assets. Text, text hashes, raw MP3 hashes, fresh 48 kHz PCM decodes, and timeline text all agree with the lane’s `spec.json`.
- Every `narration_raw.wav` was reconstructed **byte-for-byte** from decoded sentence PCM and silence. Lead is 28,800 samples (0.600 s); tail is 115,200 samples (2.400 s) in every lane.
- Encoded AAC-to-master correlations range from **0.99999323 to 0.99999399**, with only normal AAC tail padding (629–941 samples). This independently supports “no music.”
- Delivered pace is effectively **115.000 WPM** in every lane, inside the required 105–125 WPM range.
- Maximum sentence action-start deltas are **12.979–16.458 ms**, below one 30 fps frame. Encoded audio/video stream starts are both 0.000 s in every lane.
- Encoded loudness ranges from **−21.51 to −20.92 LUFS**; true peak ranges from **−2.31 to −2.30 dBTP**. All pass the production gate used by the candidate QA (−21.6 to −19.0 LUFS; no higher than −2.0 dBTP).
- The independently transcribed encoded introductions retain `if`, `would`, `but an apparent`, `could instead`, and the closing `how do we tell` question in all four lanes.
- The intended `peak` is independently the longest PCM-derived section in all four lanes.
- No near-unchanged run was observed at the encoded motion threshold; longest measured run is **0.0 s** in all four lanes.

## Per-lane findings

### 1. `mzr-census-method-overhaul-canary-20260809T0214K`

**Hash-bound verdict:** `KUN_HOLD_REPRODUCIBILITY` on MP4 `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536`.

Audio/sync evidence:

- Full decode: PASS; 6,727 decoded video frames and 10,511 decoded AAC frames.
- Media: H.264/AAC, 1920×1080, 30/1 fps, yuv420p, 48 kHz mono; encoded duration 224.233333 s versus 224.217396 s PCM timeline (15.937 ms delta).
- Pace: 424 words over 221.217396 occupied seconds = **114.999998 WPM**.
- Maximum action-start delta: **16.458 ms**; encoded stream-start delta: **0 ms**.
- Loudness/peak: **−21.51 LUFS / −2.31 dBTP**.
- Speech-only master correlation: **0.999993504**; no music layer detected.
- Independent local encoded-intro ASR similarity: **1.000000**; all five critical opening phrase checks pass. The packet’s independent `whisper-1` receipt similarity is 0.992519 and its input WAV was reproduced byte-for-byte from the MP4.
- Peak: **47.598250 s**, longer than runner-up motivation at 29.758687 s.
- Motion: mean luma difference **0.446229**; longest near-unchanged run **0.0 s**.
- Source manifest: 10/10 paths, byte counts, and hashes replayed.
- All non-renderer audit checks: PASS.

Required-file hash ledger:

| artifact | SHA-256 |
|---|---|
| `audio/synthesis_receipt.json` | `4ddb3a49641449c9d61ede057ad450992bc93083e1edff7a203d02561a8f21f4` |
| `audio/timeline.json` | `af224f225fae4ac4b9821a2589f9ab47e51795ea19215d7d93caa4bd58feb820` |
| `build_receipt.json` | `bc0006781e362751ae02985f04c97c44974a8e7f444c4e0f1fc369833baf7a54` |
| `encoded_qa.json` | `1da92b8a1a3d45c498632a471d26a4bf37b9f4dcd04c7f13704c7b44c68f9204` |
| `RECEIPT.json` | `513a6899713ed38723595434b922dba5568c4a62381ffbce2b76474676bedcc7` |
| `source_manifest.json` | `afc98610f18d034beabbd2c5c43e489e628b2bec4ce0fd9a676dc24a328a29b8` |

**Exact blocker:** `build_receipt.json` binds this MP4 to renderer SHA-256 `86ae01af1388423978de90682fd1e771569c13357cb6efb397d158a13a04ae53`. That byte sequence is absent from the handoff tree. The only current shared `render.py` is `7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53`. Exact rerender cannot be attempted until the historical renderer bytes are recovered.

### 2. `fesc-method-overhaul-canary-20260809T0227K`

**Hash-bound verdict:** `KUN_HOLD_REPRODUCIBILITY` on MP4 `b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168`.

Audio/sync evidence:

- Full decode: PASS; 7,102 decoded video frames and 11,098 decoded AAC frames.
- Media: H.264/AAC, 1920×1080, 30/1 fps, yuv420p, 48 kHz mono; encoded duration 236.739000 s versus 236.739125 s PCM timeline (0.125 ms delta).
- Pace: 448 words over 233.739125 occupied seconds = **115.000003 WPM**.
- Maximum action-start delta: **12.979 ms**; encoded stream-start delta: **0 ms**.
- Loudness/peak: **−21.48 LUFS / −2.31 dBTP**.
- Speech-only master correlation: **0.999993230**; no music layer detected.
- Independent local encoded-intro ASR similarity: **1.000000**; all critical opening phrase checks pass. Packet `whisper-1` similarity is 1.000000; encoded STT input extraction also reproduced byte-for-byte.
- Peak: **48.981750 s**, longer than runner-up motivation at 33.022313 s.
- Motion: mean luma difference **0.487524**; longest near-unchanged run **0.0 s**.
- Source manifest: 8/8 paths, byte counts, and hashes replayed.
- All non-renderer audit checks: PASS.

Required-file hash ledger:

| artifact | SHA-256 |
|---|---|
| `audio/synthesis_receipt.json` | `f2c7d230bec636d6bb609ddfe4c57b8062d198b17dba53b10b58724f0f6f29a3` |
| `audio/timeline.json` | `b3e33fc40724f5816fd8cf8c0cd9afced82435898744ecd3b6919645db4711de` |
| `build_receipt.json` | `67408f7bd5ebcc90e7be8874b49bdc8534df120a459b31cf49854b2320b6186f` |
| `encoded_qa.json` | `6e2ebef25891858ea7d3480633db77db53f9156c94a7f861f0e4e8a721bce1b5` |
| `RECEIPT.json` | `f1f2e6b34f41d9fc8200452ad46844dca7e7d90e472a2d91c3ac9eedc1d0a178` |
| `source_manifest.json` | `dae7a4d2e4b99159ce06b0b4af48efcda5649c076d297e67d18e9ad242755581` |

**Exact blocker:** the receipt requires renderer SHA-256 `d14a5643fb305d65aa374b90ad71827f275e2826c9b0a7a17f60b340c18b4481`, but those bytes are absent from the handoff tree. Current shared renderer is `7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53`.

### 3. `brightend-method-overhaul-canary-20260809T0235K`

**Hash-bound verdict:** `KUN_HOLD_REPRODUCIBILITY` on MP4 `9a137c61011a3d9629c96ebbf365955295e11082cededa325ceb38f1ce268a2f`.

Audio/sync evidence:

- Full decode: PASS; 6,836 decoded video frames and 10,682 decoded AAC frames.
- Media: H.264/AAC, 1920×1080, 30/1 fps, yuv420p, 48 kHz mono; encoded duration 227.869000 s versus 227.869563 s PCM timeline (0.563 ms delta).
- Pace: 431 words over 224.869563 occupied seconds = **115.000001 WPM**.
- Maximum action-start delta: **15.729 ms**; encoded stream-start delta: **0 ms**.
- Loudness/peak: **−21.38 LUFS / −2.31 dBTP**.
- Speech-only master correlation: **0.999993721**; no music layer detected.
- Independent local encoded-intro ASR similarity: **0.997722**; all critical opening phrase checks pass. Packet `whisper-1` similarity is also 0.997722; encoded STT input extraction reproduced byte-for-byte.
- Peak: **44.812750 s**, longer than runner-up motivation at 31.497563 s.
- Motion: mean luma difference **0.414502**; longest near-unchanged run **0.0 s**.
- Source manifest: 10/10 paths, byte counts, and hashes replayed.
- All non-renderer audit checks: PASS.

Required-file hash ledger:

| artifact | SHA-256 |
|---|---|
| `audio/synthesis_receipt.json` | `bdf18fe8cbab2d31f7887ecf85c60764b75ba4b36dc5a1dd9974a87f698a0410` |
| `audio/timeline.json` | `c2d4c804bfa5d68a9b54c33dd2a5bc06c762fc1d5fee79d98d4a52a094836b35` |
| `build_receipt.json` | `05bcf00539d2b60b14ee87f12819de8a33800573fe7656d5a1cc42402051dbb3` |
| `encoded_qa.json` | `73d15d17a3fd1aebd4f4f3fb936c0ea66af2f672fad0c3b4787dd5507fb0cc14` |
| `RECEIPT.json` | `07e8d0a5a3fe27ae77644076f62f44ccdd1e61c11eec792b8b1ada2f7cc51b6d` |
| `source_manifest.json` | `6a0256c8806cd00a88c0bfa877870517aee9048103e8153abb836734d3c10e71` |

**Exact blocker:** like `fesc`, this candidate requires renderer SHA-256 `d14a5643fb305d65aa374b90ad71827f275e2826c9b0a7a17f60b340c18b4481`, which is absent. One recovered historical renderer can unblock both lanes, but each must still be rerendered in a temporary copy and compared to its own MP4 hash.

### 4. `mzr-anchor-method-overhaul-canary-20260809T0245K`

**Hash-bound verdict:** `KUN_PASS_WITH_PORTABILITY_CAVEAT` on MP4 `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970`.

Audio/sync evidence:

- Full decode: PASS; 6,586 decoded video frames and 10,291 decoded AAC frames.
- Media: H.264/AAC, 1920×1080, 30/1 fps, yuv420p, 48 kHz mono; encoded duration 219.533333 s versus 219.521729 s PCM timeline (11.604 ms delta).
- Pace: 415 words over 216.521729 occupied seconds = **115.000005 WPM**.
- Maximum action-start delta: **16.250 ms**; encoded stream-start delta: **0 ms**.
- Loudness/peak: **−20.92 LUFS / −2.30 dBTP**.
- Speech-only master correlation: **0.999993985**; no music layer detected.
- Independent local encoded-intro ASR similarity: **1.000000**; all critical opening phrase checks pass. Packet `whisper-1` similarity is 0.998761; encoded STT input extraction reproduced byte-for-byte.
- Peak: **47.459667 s**, longer than runner-up motivation at 28.316750 s.
- Motion: mean luma difference **0.439634**; longest near-unchanged run **0.0 s**.
- Source manifest: 10/10 paths, byte counts, and hashes replayed.
- All 26 audit checks, including exact renderer availability: PASS.

Required-file hash ledger:

| artifact | SHA-256 |
|---|---|
| `audio/synthesis_receipt.json` | `2e172e19340ac288d730e46846fd3e9a9a785931997e6a29db4d7d4f0a81784f` |
| `audio/timeline.json` | `4dca3a5e0753dde46bffcdc3ee3a39453db46411317b6d205a4119a928f7e450` |
| `build_receipt.json` | `2e62e157adacc30eb21e459c53e3db43432cbb8731e2d12f98c8ee61699439fe` |
| `encoded_qa.json` | `02efc107be0a903e955e6b530134d81cbe93cca106835f3b49f7fb832e41da38` |
| `RECEIPT.json` | `4f9bcd93ab48c16db8809280e546eef47c31fb6fca627a300fdfda7bb1d2c23d` |
| `source_manifest.json` | `449300fb705ba5853d57d6e52eb52262164ba4c5c5cf7c219f5692369cf61d55` |

Reproducibility replay:

- Build receipt renderer SHA-256: `7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53`.
- Current shared `sibling-rollout-20260809T0200K/render.py`: the same SHA-256.
- A clean temporary-copy rerender produced MP4 SHA-256 `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970`, exactly matching the frozen candidate. The temporary copy was deleted.

**Caveat, not blocker:** the exact renderer resolves through the shared rollout workspace rather than from inside the candidate directory. The present workspace is sufficient for exact replay; the candidate packet by itself is not portable.

## Caveats common to all four lanes

1. **TTS request parameters are attestations, not codec metadata.** Alloy identity, speed 1.18, managed-gateway routing, and sentence-per-call granularity cannot be forensically recovered from MP3/AAC headers. They are consistently recorded in the hash-bound synthesis receipts and corroborated by 22 unique sentence assets per lane. No silent provider substitution is evident.
2. **No-music is independently stronger than receipt-only evidence.** The raw masters reconstruct exactly from sentence PCM plus zeros, the gain stage replays, and the encoded AAC correlates near one with those speech-only masters.
3. **STT provenance is incomplete in the candidate JSON.** `encoded_qa.json` records transcript and similarity but not provider/model. The current QA script shows `whisper-1`; this review did not rely on that alone and performed a separate local `faster-whisper-small.en` pass.
4. **Audio paths are shared-root-relative.** Synthesis/timeline records use paths such as `audio/<slug>/raw/...`, while each candidate snapshot stores the same bytes under `audio/raw/...`. Both current locations hash-match, so custody passes now; moving a candidate alone would require a documented path rewrite/resolver.
5. **Exact environment capture is thin.** The receipts do not freeze ffmpeg, libx264, Pillow, Python, font, or command versions. `mzr-anchor` nevertheless replayed byte-exactly on the current host. Archival portability remains weaker than current-host reproducibility.

## Exact unblock actions

Do **not** edit the frozen candidates. To clear the batch HOLD:

1. Recover the historical renderer bytes matching `86ae01af1388423978de90682fd1e771569c13357cb6efb397d158a13a04ae53`; preserve them under a new immutable, versioned provenance path; rerender a temporary copy of `mzr-census`; require MP4 hash `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536`.
2. Recover renderer bytes matching `d14a5643fb305d65aa374b90ad71827f275e2826c9b0a7a17f60b340c18b4481`; rerender temporary copies of `fesc` and `brightend`; require their respective frozen MP4 hashes.
3. If either renderer cannot be recovered, create **new versioned candidates** with the current preserved renderer and fresh receipts/review. Never replace the three frozen MP4s under review.
4. In the amendment or new candidates, record renderer path+hash, build command, ffmpeg/libx264/Pillow/Python/font versions, and STT provider/model.

Until those exact renderer blockers are resolved, Kun concurs with the media/audio/sync quality of all four hashes but does **not** concur with batch-wide reproducibility acceptance.
