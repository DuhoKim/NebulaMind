# Kun post-order audio / synchronization / reproducibility / renderer-portability re-review — exact HWAO sibling fix set

Review timestamp: `2026-08-09 14:03:55 +0900` (`KST`)  
Reviewer: **Kun**  
Review posture: **fresh post-order independent re-review; local-only; no candidate, integrator, public-video, or Git mutation authorized**

## 1. Ordered set, later stand-down, and frozen scope

I read `HWAO_SIBLING_FIX_ORDER.md` in full before reaching a verdict and re-hashed it as:

`96fc45cf633e406c0b9bbe71529b2f78021c68c8595c8a143c839f686ff69aea`

That is the ordered packet named in the handoff. I also read Tori's required re-review, `reviews/TORI_SIBLING_HWAO_FIX_REREVIEW.md`, whose current SHA-256 is:

`284a793729ae8cac945ab4cffd44d50ecd3b65dca442ebfe43df700673ff3dba`

Tori's packet was context, not a substitute for the checks below. The exact media set I independently inspected is:

I also observed the later superseding record `integrator/HWAO_SIBLING_FIX_ORDER_STAND_DOWN_20260809T1400K.md` (recorded `2026-08-09T14:00:31+0900`, status `STAND_DOWN_AT_SAFE_BOUNDARY_NO_NEW_CANDIDATE_HASHES_MINTED`). That record withdraws the order and says any delayed post-order reviewer completion is **receipt-only**. This packet therefore reports the technical result of the already-dispatched exact-hash review; it does not revive the withdrawn order, authorize more work, or carry promotion authority.

| lane | exact candidate | frozen MP4 SHA-256 | post-order Kun verdict |
|---|---|---|---|
| MZR-census | `mzr-census-method-overhaul-canary-20260809T0320K` | `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` | **PASS** |
| FESC | `fesc-method-overhaul-canary-20260809T0327K` | `47eb0d0b151b51667a4b29a39da74b947086c925dda7ce7e819240ffde25e42d` | **PASS** |
| bright-end | `brightend-method-overhaul-canary-20260809T0337K` | `6e0f4b098d6c5386d08ab7fb670b8b6564e257edeac5dc1c6fec2cc6b97bc7b4` | **PASS** |
| MZR-anchor, unchanged | `mzr-anchor-method-overhaul-canary-20260809T0245K` | `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970` | **PASS WITH PORTABILITY CAVEAT** |

**Overall Kun technical disposition for this review lane: PASS; administrative disposition: STAND DOWN / RECEIPT ONLY.** The three exact replacements pass the audio, sample-derived synchronization, encoded-media, and renderer-replay checks. The unchanged MZR-anchor remains a pass through its handoff-level exact-renderer archive, with the narrower custody caveat recorded below. This does **not** open any reporting or external gate and does not supersede the later stand-down.

## 2. Fresh check method

For every candidate I performed the following from the frozen bytes rather than accepting self-QA summaries at face value:

1. Re-hashed the MP4, spec, synthesis receipt, PCM timeline, raw and mastered WAVs, build receipt, encoded-QA packet, receipt/freeze chain, source manifest, and available provenance manifest. Receipt and freeze bindings resolved without a mismatch.
2. Checked all 22 sentence records against the exact spec text and text hash. I fresh-decoded all **88** recorded MP3 sentence assets with FFmpeg to mono 48 kHz signed 16-bit PCM and compared every decoded PCM payload byte-for-byte with its stored decoded WAV payload.
3. Reassembled each raw master from the decoded sentence PCM, its sample-indexed starts, inter-sentence pauses, 28,800-sample lead, and 115,200-sample terminal silence. All four raw-master PCM payloads reproduced byte-for-byte. I recomputed WPM, section spans, nearest-frame action starts, and maximum A/V action-start delta from sample and frame integers.
4. Fully decoded each H.264 and AAC stream to end-of-file; fresh-probed codec, pixel format, resolution, frame rate, audio layout, stream starts, frame counts, and duration. I decoded AAC back to PCM and compared it with the mastered narration. Correlation is at least `0.9999931`, with only normal AAC encoder padding, which independently rejects a separate music bed.
5. Re-ran FFmpeg EBU R128 loudness analysis and a 2 Hz, 160×90 gray-frame motion scan. I also re-extracted each encoded introduction; each extracted WAV was byte-identical to the stored encoded-introduction artifact.
6. Ran a fresh local `Systran/faster-whisper-small.en` introduction transcription. This is independent of the stored managed `whisper-1` transcript. I compared normalized text with the exact first four narration sentences and checked that the conditional motivation clauses survived.
7. Built minimal off-tree replay directories under `/tmp` with the exact spec, PCM timeline, mastered narration, and sources. For the three replacements I used their candidate-local renderer bytes; for MZR-anchor I used the exact handoff-level archived renderer bytes. Python `3.11.15`, Pillow `12.3.0`, FFmpeg `8.1.2` with `libx264`, and the recorded Avenir Next / Menlo font bytes were present. **All four clean replay MP4s matched the frozen MP4s byte-for-byte.** The replay trees were then removed.

The automated fresh-check totals were `58/58` for each replacement and `48/48` for unchanged MZR-anchor; the anchor has fewer candidate-local provenance assertions by design, not failed media checks.

## 3. Cross-lane encoded and synchronization results

All four files independently probe as H.264 `yuv420p`, 1920×1080, constant `30/1` fps, plus mono AAC at 48 kHz. Video and audio stream starts are both zero in every file.

| lane | words / delivered WPM | PCM / container duration | frames | max sample-derived A/V delta | fresh LUFS-I / dBTP | fresh intro similarity | motion mean / longest near-unchanged |
|---|---:|---:|---:|---:|---:|---:|---:|
| MZR-census | 435 / `115.000000` | `229.956521` / `229.966667` s | 6,899 | `0.016292` s | `-21.65` / `-2.32` | `1.000000` | `0.440572` / `0.0` s |
| FESC | 448 / `115.000003` | `236.739125` / `236.739000` s | 7,102 | `0.015333` s | `-20.24` / `-2.30` | `1.000000` | `0.395181` / `0.0` s |
| bright-end | 431 / `115.000001` | `227.869563` / `227.869000` s | 6,836 | `0.014500` s | `-20.05` / `-2.29` | `0.997722` | `0.411423` / `0.0` s |
| MZR-anchor | 415 / `115.000005` | `219.521729` / `219.533333` s | 6,586 | `0.016250` s | `-20.92` / `-2.30` | `1.000000` | `0.439634` / `0.0` s |

Every maximum A/V action-start delta is less than one 30 fps frame (`0.033333` s). Every loudness result is inside the sibling target band and every true peak is at or below `-2.0` dBTP. The 2 Hz scan found no sampled near-unchanged run at all, and the complete streams decoded without error. The encoded-audio/master-PCM correlations were, respectively, `0.9999931493`, `0.9999945727`, `0.9999947564`, and `0.9999939811`; AAC padding was 807, 874, 629, and 941 samples.

In every fresh introduction transcript, the conditional structure remained recognizable: `if`, `would`, `but an apparent`, `could instead`, and `how do we tell` were all present after normalization.

## 4. Per-lane findings

### 4.1 MZR-census — PASS

Exact candidate: `mzr-census-method-overhaul-canary-20260809T0320K`  
Exact MP4: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` (`9,539,823` bytes)

- **Synthesis contract:** 22 exact sentence records attest `Hermes managed OpenAI audio gateway`, model `gpt-4o-mini-tts`, voice `alloy`, speed `1.18`, one sentence per call, and `music: false`. Synthesis-receipt SHA-256: `7fdb79a6cf97d429686240b8048568387a221611261d73dfbf0bb943a164ddf5`.
- **Replacement audio is new:** against rejected predecessor `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536`, the synthesis receipt, PCM timeline, mastered WAV, and all `22/22` raw sentence assets differ.
- **PCM custody and synchronization:** raw master `6f70ed7aad4dd0e2a4103a3ceaae21df79b7930247a439c08dabb1eb06228520` and mastered narration `5c196bf5d6158a085e426387bb473ddc23ceecef8004b5e247d580bdf6c0ee35`; timeline `d1495001eac971557edab645cdc579e0c8f4635f42282aba45ca4f286f398aa8`. Fresh PCM reconstruction is byte-exact. `peak` is longest at `50.043083` s versus `motivation` at `32.486313` s.
- **Encoded QA:** H.264/AAC full decode pass; 115.000000 WPM; `-21.65` LUFS-I and `-2.32` dBTP; maximum action-start delta `0.016292` s; fresh intro ASR similarity `1.000000`; no sampled freeze.
- **Renderer custody/replay:** candidate-local renderer `2174ff9fec9fcfbc81e078f8ca43df807206eb6b7dffdb6ab210a499d07d9981`; candidate-local environment receipt `7c1972495bbf6de10df7e32c8d5aec96e8b89e66fc43a95732278ecc27d4883b`. The off-tree clean rerender reproduced `d6014ac…e1061b` byte-for-byte.
- **Frozen tree checkpoint:** 141 files; tree digest `024ed6b31dbe28fb2c362b046b5ac6ca8db2058b6bba21cf2586600949ab479b`.

**Verdict: PASS.** No Kun audio, synchronization, motion, or exact-render replay blocker remains for this replacement.

### 4.2 FESC — PASS

Exact candidate: `fesc-method-overhaul-canary-20260809T0327K`  
Exact MP4: `47eb0d0b151b51667a4b29a39da74b947086c925dda7ce7e819240ffde25e42d` (`9,998,675` bytes)

- **Synthesis contract:** 22 exact sentence records attest the managed OpenAI audio route, `gpt-4o-mini-tts`, Alloy, speed `1.18`, one sentence per call, and no music. Synthesis-receipt SHA-256: `796bb3a64aab9f1e24a23185c020f1e47e94a738ac21e4b4359ed9cc3d703372`.
- **Replacement audio is new:** against rejected predecessor `b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168`, the synthesis receipt, PCM timeline, mastered WAV, and all `22/22` raw sentence assets differ.
- **PCM custody and synchronization:** raw master `bcde94e0e607bbd6e10b23e47cc4ed24b57ce1cd9436b7bb2e626a6f6817047b`; mastered narration `8e40e71229fc3e0bf2f21e7f02f8c3370e1042a62ffadb03fb2ff10f96adf156`; timeline `ceccab164e9fc014490fbd00aae6fc4a35696fddc27930bf4e4f35198e856149`. Fresh PCM reconstruction is byte-exact. `peak` is longest at `52.253667` s versus `motivation` at `33.004250` s.
- **Encoded QA:** H.264/AAC full decode pass; 115.000003 WPM; `-20.24` LUFS-I and `-2.30` dBTP; maximum action-start delta `0.015333` s; fresh intro ASR similarity `1.000000`; no sampled freeze.
- **Renderer custody/replay:** candidate-local renderer `71953059e2555cae36bf056aa80bdc7440170eb82c106606136dcc4daa74c884`; candidate-local environment receipt `0cf2274391e3ffc21d03a830504f10a6b52837a46a8401fe0d4dc0a5a4b33245`. The off-tree clean rerender reproduced `47eb0d0b…25e42d` byte-for-byte.
- **Frozen tree checkpoint:** 148 files; tree digest `1f2f5b4aaed54811592cb779436ee45fea746151b4d8d74df53c559e7b69dfc9`.

**Verdict: PASS.** No Kun audio, synchronization, motion, or exact-render replay blocker remains for this replacement.

### 4.3 bright-end — PASS

Exact candidate: `brightend-method-overhaul-canary-20260809T0337K`  
Exact MP4: `6e0f4b098d6c5386d08ab7fb670b8b6564e257edeac5dc1c6fec2cc6b97bc7b4` (`9,747,250` bytes)

- **Synthesis contract:** 22 exact sentence records attest the managed OpenAI audio route, `gpt-4o-mini-tts`, Alloy, speed `1.18`, one sentence per call, and no music. Synthesis-receipt SHA-256: `e13ff5ddb20bd82f5dfe2d145709e1c66ce5c6b25ac7fc40528940765ff8b569`.
- **Replacement audio is new:** against rejected predecessor `9a137c61011a3d9629c96ebbf365955295e11082cededa325ceb38f1ce268a2f`, the synthesis receipt, PCM timeline, mastered WAV, and all `22/22` raw sentence assets differ.
- **PCM custody and synchronization:** raw master `80c4ebae67d34bc1db01caff12032728189d64bd1956ae6127f33be6ca45b0d6`; mastered narration `fd8643eebacc898d2bc49a81e3d1a46ed8878de0e65e55db7ed42fae609e3ed6`; timeline `6634c751ae6713b8f9e2a8b45bb7e1a14152cea05c09fd683ec7fe9dc3efa16d`. Fresh PCM reconstruction is byte-exact. `peak` is longest at `47.053000` s versus `motivation` at `29.475750` s.
- **Encoded QA:** H.264/AAC full decode pass; 115.000001 WPM; `-20.05` LUFS-I and `-2.29` dBTP; maximum action-start delta `0.014500` s; fresh intro ASR similarity `0.997722`; no sampled freeze.
- **Renderer custody/replay:** candidate-local renderer `71953059e2555cae36bf056aa80bdc7440170eb82c106606136dcc4daa74c884`; candidate-local environment receipt `f4c2734ffc13c7a53965932aff9965b212a3c4675bbbcb64cbdc9134ed2ddd5c`. The off-tree clean rerender reproduced `6e0f4b09…7bc7b4` byte-for-byte.
- **Frozen tree checkpoint:** 137 files; tree digest `0e9dc06b9da09ea8ddf3a9edf247008d1b5226482a9d23169703b71d15ea9a62`.

**Verdict: PASS.** No Kun audio, synchronization, motion, or exact-render replay blocker remains for this replacement.

### 4.4 MZR-anchor unchanged — PASS WITH PORTABILITY CAVEAT

Exact candidate: `mzr-anchor-method-overhaul-canary-20260809T0245K`  
Exact MP4: `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970` (`9,649,802` bytes)

- **Unchanged scope:** the order names this already-accepted hash unchanged. I found no byte drift.
- **Synthesis contract:** 22 exact sentence records attest the managed OpenAI audio route, `gpt-4o-mini-tts`, Alloy, speed `1.18`, one sentence per call, and no music. Synthesis-receipt SHA-256: `2e172e19340ac288d730e46846fd3e9a9a785931997e6a29db4d7d4f0a81784f`.
- **PCM custody and synchronization:** raw master `f5ebd2dc95ddba5d1babc6a26e877a8bf02c6cf52add8e5aef8da5bc2a412036`; mastered narration `b0900ec6c8146bedae3497d4c4141e81edfc66ad19478faea90b2211d0053df7`; timeline `4dca3a5e0753dde46bffcdc3ee3a39453db46411317b6d205a4119a928f7e450`. Fresh PCM reconstruction is byte-exact. `peak` is longest at `47.459667` s versus `motivation` at `28.316750` s.
- **Encoded QA:** H.264/AAC full decode pass; 115.000005 WPM; `-20.92` LUFS-I and `-2.30` dBTP; maximum action-start delta `0.016250` s; fresh intro ASR similarity `1.000000`; no sampled freeze.
- **Renderer custody/replay:** the candidate itself does not contain the exact renderer or environment receipt. The handoff archive at `integrator/renderer-archive/7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53/` binds renderer SHA-256 `7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53`, candidate hash `973daba3…e1970`, and build-receipt hash `2e62e157adacc30eb21e459c53e3db43432cbb8731e2d12f98c8ee61699439fe`. I copied those renderer bytes to an off-tree execution location and reproduced `973daba3…e1970` byte-for-byte.
- **Frozen tree checkpoint:** 129 files; tree digest `73c9eb86608369c627e167ca9023c1668630a0fc1481658678c38dce012fabcb`.

**Verdict: PASS WITH PORTABILITY CAVEAT.** Exact replay is freshly demonstrated, so this is not a media or reproducibility failure. Custody is handoff-local rather than candidate-local and must travel with the candidate. If the archive is separated from the candidate, the replay claim is no longer self-contained.

## 5. Caveats and claim boundary

These caveats are explicit and do not convert the four lane verdicts to FAIL:

1. **Voice and speed are receipt-level attestations.** The per-sentence receipts consistently name the managed gateway, `gpt-4o-mini-tts`, Alloy, and speed `1.18`, and all raw bytes/hashes resolve. They do not carry vendor-signed request IDs or another cryptographic proof that independently identifies voice or speed from the waveform alone.
2. **The renderer replay is stronger than an end-to-end resynthesis replay.** I proved that exact prepared spec + PCM timeline + mastered narration + sources + pinned renderer reproduce every MP4 byte-for-byte. I did not call the managed TTS service again; stochastic TTS would not be expected to recreate the same MP3 bytes. Candidate provenance snapshots of synthesis/assembly remain evidence, but some recorded raw/decoded paths retain their original workspace shape (`audio/<slug>/…`) while the frozen candidate stores the assets under candidate-local `audio/raw` and `audio/decoded`. The assets are complete and hash-resolvable by basename, but the snapshots are not a turnkey candidate-directory rebuild from TTS through assembly without path adaptation.
3. **Synchronization is state/action-start synchronization, not lip sync.** The videos use sample-derived sentence timing and nearest-frame visual action starts. There is no animated mouth/phoneme track to evaluate.
4. **The no-freeze result is a 2 Hz motion scan plus full stream decode.** It strongly excludes the governed eight-second freeze condition; it is not a proof that every adjacent 30 fps frame differs.
5. **Byte-exact portability is environment-pinned.** Exact equality was demonstrated on macOS arm64 with Python `3.11.15`, Pillow `12.3.0`, FFmpeg `8.1.2`/`libx264`, Avenir Next SHA-256 `98dec241f3ee712a37fad61aafdb83e225ed54c3e5b6e9f0abeb24eba13743ba`, and Menlo SHA-256 `dc256e0b39c2a6fec947129d421fef41b8b429f58f9b6e5d1b148c87f775c1f6`. This does not promise identical bytes from arbitrary FFmpeg, font, Pillow, OS, or architecture versions.
6. **MZR-anchor custody is narrower.** Its renderer is preserved at the handoff level, not inside the candidate. The three replacements do carry candidate-local renderer and environment receipts.

## 6. Gate disposition

This packet is an independent technical review only.

- superseding stand-down: **in force; receipt-only completion**
- `video_reportable_now`: **false for all four lanes**
- upload: **closed**
- cockpit or public-video-root copy: **closed**
- Git action: **closed**
- deployment/publication: **closed**
- scientific/source-freeze and all other external acceptance gates: **unchanged and closed**

**Final Kun answer:** the exact HWAO sibling replacement set passes this post-order audio/synchronization/reproducibility/renderer-portability lane, with the stated receipt, path-layout, environment-pin, motion-sampling, and MZR-anchor custody caveats. The later stand-down remains controlling; this delayed packet is receipt-only. Nothing in this review makes any video reportable now.
