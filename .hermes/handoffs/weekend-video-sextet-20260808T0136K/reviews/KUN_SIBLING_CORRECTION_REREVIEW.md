# Kun independent sibling correction-round rereview — audio, synchronization, deterministic replay, and renderer portability

Review time: **2026-08-09 04:12:37 KST (+0900)**  
Scope authority: `integrator/CORRECTION_ROUND_RECEIPT.md` and its four exact hashes only.  
Prior packets cross-checked: `reviews/KUN_SIBLING_ROLLOUT.md` and `reviews/KUN_MZR_ANCHOR_PORTABILITY_AMENDMENT.md`.

This packet is a read-only technical disposition. It does **not** authorize upload, publication, public/shared MP4 copies, cockpit mutation, database writes, deployment, Git action, or a scientific result claim. Every `video_reportable_now` gate remains `false`.

## Batch verdict

**KUN BATCH VERDICT: `PASS_WITH_RENDERER_PORTABILITY_CAVEATS`**

- **Audio and synchronization: PASS, 4/4 exact hashes.** All four H.264/AAC files full-decoded through EOF. I independently replayed the 48 kHz PCM timeline, all 88 sentence assets, 115 WPM pacing, sentence-to-visual alignment, stream starts, encoded loudness/true peak, introduction extraction and ASR, speech-only soundtrack correlation, peak duration, and motion/no-freeze checks.
- **Deterministic reproducibility: PASS, 4/4 exact hashes.** The three correction candidates each reproduced their frozen MP4 SHA-256 byte-for-byte in a clean temporary build from the frozen spec, timeline, narration master, source snapshot, and exact candidate-local renderer bytes. MZR-anchor retains Kun's prior byte-exact clean replay; this rereview independently cross-checked that replay's hash-bound review packet, build receipt, newly archived renderer, and archive manifest.
- **Renderer byte custody: PASS, 4/4.** Each correction candidate contains exact local `synthesize.py`, `assemble.py`, `render.py`, `qa.py`, environment, and font-hash snapshots bound through its receipts and provenance manifest. MZR-anchor's exact renderer is preserved in the handoff-level renderer archive and matches its build receipt.
- **Portability caveat:** same-host exact replay is proven; arbitrary-host replay is not. Renderers use absolute macOS Avenir Next/Menlo paths, and the environment snapshots record versions/hashes rather than embedding the fonts, Python/Pillow environment, FFmpeg/libx264 binaries, or a dependency lock. MZR-anchor's renderer is handoff-local but not candidate-local. These are archival portability caveats, not exact-hash or current-host reproducibility failures.

| lane | exact MP4 SHA-256 | audio/sync | deterministic replay | renderer portability | Kun lane verdict |
|---|---|---|---|---|---|
| `mzr-census` | `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` | PASS | PASS — clean rerender matched | PASS with environment/execution-copy caveat | **PASS** |
| `fesc` | `47eb0d0b151b51667a4b29a39da74b947086c925dda7ce7e819240ffde25e42d` | PASS | PASS — clean rerender matched | PASS with environment/execution-copy caveat | **PASS** |
| `brightend` | `6e0f4b098d6c5386d08ab7fb670b8b6564e257edeac5dc1c6fec2cc6b97bc7b4` | PASS | PASS — clean rerender matched | PASS with environment/execution-copy caveat | **PASS** |
| `mzr-anchor` | `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970` | PASS | PASS — prior clean replay and fresh custody cross-check | PASS at handoff level; renderer is outside candidate | **PASS WITH PORTABILITY CAVEAT** |

## Independent review method

I did not accept candidate PASS labels as evidence by themselves. For each exact candidate I independently:

1. Recomputed the MP4 hash and byte count and replayed all build, encoded-QA, receipt, post-freeze, source-manifest, and available provenance-manifest bindings.
2. Full-decoded mapped video and audio through EOF and freshly probed/count-read H.264/AAC, 1920×1080, yuv420p, 30/1 fps, 48 kHz mono audio, durations, and stream start times.
3. Checked the synthesis contract attestation: Hermes managed OpenAI audio gateway, `gpt-4o-mini-tts`, Alloy, speed 1.18, `music: false`, and one exact sentence per call.
4. Required 22 unique synthesis records and raw MP3s per lane; exact spec/timeline text and text hashes; fresh 24 kHz mono MP3 probes; and fresh mono s16le 48 kHz decodes byte-identical to every stored decoded WAV payload.
5. Rebuilt every narration raw master sample-for-sample from sentence PCM and zero-filled pauses; replayed cursor continuity, 28,800-sample lead, 115,200-sample tail, sample-derived seconds, frame-derived action times, maximum absolute alignment delta, WPM, and section intervals.
6. Correlated the encoded AAC decode with the speech-only narration master, allowing only ordinary AAC tail padding. No independent music layer was detected.
7. Remeasured loudness using the production filter `loudnorm=I=-20.3:LRA=7:TP=-2.3:print_format=json` and recomputed motion from 160×90 luma at 2 fps with the 0.08 near-unchanged threshold.
8. Re-extracted each encoded introduction with the recorded boundaries and exact 16 kHz PCM command; required WAV identity with the stored transcription input; and ran a second ASR pass with faster-whisper 1.2.1 / `Systran/faster-whisper-small.en`, CPU int8, English, beam size 5, VAD disabled.
9. Compiled all four archived Python tools for every new candidate without writing bytecode, verified their path/hash bindings, replayed environment/font hashes and build-command semantics, and then performed the three clean temporary rerenders.
10. Computed deterministic candidate-tree digests before review and again after all heavy checks; all four remained exactly unchanged. All rerender and ASR temporary artifacts were outside candidates and were removed.

## Shared audio/synchronization findings

- **88/88 sentence receipts passed.** Every lane has 22 unique sentence records and assets. Receipt text, spec text, timeline text, text hash, raw MP3 hash/size/probe, fresh decode, decoded WAV hash, and 48 kHz sample span agree.
- TTS voice, speed, managed route, and call granularity are production attestations rather than codec-forensic properties. The record/asset structure and hashes corroborate the attestations; MP3/AAC headers alone cannot reverse-prove Alloy identity or request speed.
- Every speech-only `narration_raw.wav` payload rebuilt exactly from sentence PCM plus zeros. The scalar masters replayed at −0.710000 dB (`mzr-census`) and −0.280000 dB (`mzr-anchor`); FESC and bright-end carry and replay hash-bound dynamic-loudness-normalization receipts.
- Encoded-master correlations are `0.999993149`–`0.999994756`; AAC tail padding is only 629–941 samples. This is strong independent evidence of narration plus silence and **no music**.
- Delivered pacing is effectively **115.000 WPM** in all lanes. Maximum action-start error is 14.500–16.292 ms, below one 30 fps frame (33.333 ms). Encoded video and audio starts are both 0.000 s in all lanes.
- Fresh loudness is −21.65 to −20.05 LUFS and true peak is −2.32 to −2.29 dBTP. MZR-census's −21.65 LUFS passes the correction-round production tolerance of −21.8 to −19.0 LUFS recorded by the corrected QA; all true peaks remain at or below −2.0 dBTP.
- All four fresh local ASR passes preserve the critical rhetorical clauses `if`, `would`, `but an apparent`, `could instead`, and `how do we tell`.
- The intended `peak` is the longest PCM-derived section in every lane. No near-unchanged interval was observed at the declared motion threshold; longest run is 0.0 s in all lanes.

## Per-lane evidence and verdicts

### 1. MZR-census correction

**Verdict: `KUN_PASS` on `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`.**

- Full decode/probe: 6,899 video frames; 10,780 AAC frames; H.264/AAC, 1920×1080, yuv420p, 30 fps, 48 kHz mono.
- Container 229.966667 s versus PCM 229.956521 s: **+10.146 ms**. Stream-start delta: **0 ms**.
- 435 words over 226.956521 occupied seconds: **115.000000 WPM**. Maximum action-start delta: **16.292 ms**.
- Fresh encoded audio: **−21.65 LUFS / −2.32 dBTP**. Encoded-master correlation: **0.999993149**; AAC tail: 807 samples; no music detected.
- Encoded introduction WAV SHA-256: `0e37b5f25706bbc2eae3facb24b06c09fa4d9b8921652a4ead19164fc45e13b7`. Managed `whisper-1` and fresh local ASR both normalize to similarity **1.000000**; all five critical clause checks pass.
- Peak: **50.043083 s**, longer than motivation at 32.486313 s.
- Motion: mean luma difference **0.440572**; longest near-unchanged run **0.0 s**.
- Source manifest: 11/11; provenance manifest: 5/5. Independent mechanical checks: **33/33 PASS**.
- Clean replay renderer `2174ff9fec9fcfbc81e078f8ca43df807206eb6b7dffdb6ab210a499d07d9981` reproduced the exact MP4 hash.

Required-file hash ledger:

| artifact | SHA-256 |
|---|---|
| `audio/synthesis_receipt.json` | `7fdb79a6cf97d429686240b8048568387a221611261d73dfbf0bb943a164ddf5` |
| `audio/timeline.json` | `d1495001eac971557edab645cdc579e0c8f4635f42282aba45ca4f286f398aa8` |
| `build_receipt.json` | `dc3e062599b5f9b62785361fc3c0e0a244589012b788ed5efeda65f3445ebffc` |
| `encoded_qa.json` | `d42b845ec6e0671b424dad29586b32377e7b306fa40ad99c62153b0c96a4767e` |
| `RECEIPT.json` | `dd3b1469c17577e8f8996a8f08fc3ac387bcce442ec03e1f064cf3bf9889bc5e` |
| `POST_ENCODE_FREEZE.json` | `7e1ae8588329b63943bfbb4c8866cd0640088340194e673333ad802a5444cd79` |
| `source_manifest.json` | `572fe84f84be0271f314ceea80d107e2cab2abfa255e865b1b4894a770a8d7bd` |
| `provenance_manifest.json` | `faf7a7630eaea7b4aa608c63ce163b0262e0984600e0868eb4bf428e3bd6d590` |

### 2. FESC correction

**Verdict: `KUN_PASS` on `47eb0d0b151b51667a4b29a39da74b947086c925dda7ce7e819240ffde25e42d`.**

- Full decode/probe: 7,102 video frames; 11,098 AAC frames; required H.264/AAC media profile.
- Container 236.739000 s versus PCM 236.739125 s: **−0.125 ms**. Stream-start delta: **0 ms**.
- 448 words over 233.739125 occupied seconds: **115.000003 WPM**. Maximum action-start delta: **15.333 ms**.
- Fresh encoded audio: **−20.24 LUFS / −2.30 dBTP**. Encoded-master correlation: **0.999994573**; AAC tail: 874 samples; no music detected.
- Encoded introduction WAV SHA-256: `5c773d8f186af6e8323a6d2486048dd90ba03deca98124e659dc7bf926d8e8b2`. Managed and local ASR similarity: **1.000000**; all critical clauses pass.
- Peak: **52.253667 s**, longer than motivation at 33.004250 s.
- Motion: mean luma difference **0.395181**; longest near-unchanged run **0.0 s**.
- Source manifest: 9/9; provenance manifest: 5/5. Independent mechanical checks: **33/33 PASS**.
- Clean replay renderer `71953059e2555cae36bf056aa80bdc7440170eb82c106606136dcc4daa74c884` reproduced the exact MP4 hash.

Required-file hash ledger:

| artifact | SHA-256 |
|---|---|
| `audio/synthesis_receipt.json` | `796bb3a64aab9f1e24a23185c020f1e47e94a738ac21e4b4359ed9cc3d703372` |
| `audio/timeline.json` | `ceccab164e9fc014490fbd00aae6fc4a35696fddc27930bf4e4f35198e856149` |
| `build_receipt.json` | `0b8f5512aac6e360d08ede9775aa873f092c39d3414a07cb7f4d81ae0bae91a3` |
| `encoded_qa.json` | `7f78b75ead8ba6b686d1bd226bd49a9cb125af29ceb53cb015b6353467f521a9` |
| `RECEIPT.json` | `c4201a6d3af8e1f94514ba7346af89ed90b232a0d3a24e96afef2c9f77f56800` |
| `POST_ENCODE_FREEZE.json` | `5691d9df902c0eeddfa3375b3281b7de2cab1c0a392c49eab6a778d543cc48de` |
| `source_manifest.json` | `555b2d58cb56f309c439d87b0db3f4ba0e5a8822511a0fee7f6de99905e0c088` |
| `provenance_manifest.json` | `a4d26b471bd0f37deeb4a1b6d7b810385217a5826e69be47c2918311756b7149` |

### 3. Bright-end correction

**Verdict: `KUN_PASS` on `6e0f4b098d6c5386d08ab7fb670b8b6564e257edeac5dc1c6fec2cc6b97bc7b4`.**

- Full decode/probe: 6,836 video frames; 10,682 AAC frames; required H.264/AAC media profile.
- Container 227.869000 s versus PCM 227.869563 s: **−0.563 ms**. Stream-start delta: **0 ms**.
- 431 words over 224.869563 occupied seconds: **115.000001 WPM**. Maximum action-start delta: **14.500 ms**.
- Fresh encoded audio: **−20.05 LUFS / −2.29 dBTP**. Encoded-master correlation: **0.999994756**; AAC tail: 629 samples; no music detected.
- Encoded introduction WAV SHA-256: `100296fefbc50ffb70ff3f2fa333434b39a84df3972f36b7e658ced6c2f4603e`. Managed and fresh local ASR similarity: **0.997722**; all critical clauses pass.
- Peak: **47.053000 s**, longer than motivation at 29.475750 s.
- Motion: mean luma difference **0.411423**; longest near-unchanged run **0.0 s**.
- Source manifest: 11/11; provenance manifest: 5/5. Independent mechanical checks: **33/33 PASS**.
- Clean replay renderer `71953059e2555cae36bf056aa80bdc7440170eb82c106606136dcc4daa74c884` reproduced the exact MP4 hash.

Required-file hash ledger:

| artifact | SHA-256 |
|---|---|
| `audio/synthesis_receipt.json` | `e13ff5ddb20bd82f5dfe2d145709e1c66ce5c6b25ac7fc40528940765ff8b569` |
| `audio/timeline.json` | `6634c751ae6713b8f9e2a8b45bb7e1a14152cea05c09fd683ec7fe9dc3efa16d` |
| `build_receipt.json` | `c93c6bd4c22054e77bf0f7ebe2e3a9ce3ac1a08997bbafc38f723fad2dd13294` |
| `encoded_qa.json` | `f090cfa42d08c8f8c010b9706901b1cd649422b7d13e75fb81b3aef92e0869a6` |
| `RECEIPT.json` | `159b9cc981f80cdba45a1197260f765fde56bfcd6a663d03c7c07983d67c5574` |
| `POST_ENCODE_FREEZE.json` | `fcdcbe6c4d82da22da828898fe59edc89f686503728020bc80ee482aaaef80f9` |
| `source_manifest.json` | `63921f5dedb05a335e5f4c9dcb1db8d8b78a96e15cdcddfa93a03385620a591f` |
| `provenance_manifest.json` | `af66a9c5a43e169f51cbc620703fb3ae6219292ea80428fa62438d172b557e81` |

### 4. MZR-anchor unchanged candidate

**Verdict: `KUN_PASS_WITH_PORTABILITY_CAVEAT` on `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970`.**

- Full decode/probe: 6,586 video frames; 10,291 AAC frames; required H.264/AAC media profile.
- Container 219.533333 s versus PCM 219.521729 s: **+11.604 ms**. Stream-start delta: **0 ms**.
- 415 words over 216.521729 occupied seconds: **115.000005 WPM**. Maximum action-start delta: **16.250 ms**.
- Fresh encoded audio: **−20.92 LUFS / −2.30 dBTP**. Encoded-master correlation: **0.999993981**; AAC tail: 941 samples; no music detected.
- Encoded introduction WAV SHA-256: `07ee2ae76a88db4477aeb98b451f2c53a1e55fdee7497a96af8a06ef819e3fa1`. Stored ASR similarity is 0.998761; fresh local ASR similarity is **1.000000**; all critical clauses pass.
- Peak: **47.459667 s**, longer than motivation at 28.316750 s.
- Motion: mean luma difference **0.439634**; longest near-unchanged run **0.0 s**.
- Source manifest: 10/10. Independent rereview mechanical checks: **26/26 PASS**.
- Build receipt, archive manifest, and archived source all bind renderer SHA-256 `7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53`.
- Archived `render.py` SHA-256: `7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53`; `ARCHIVE.json` SHA-256: `bf5e8521c1ce68d59812fd98f96ea8f40a4e27f9612d27a46fe89fdc38ce6a98`.
- Archive bindings also replayed candidate hash, build-receipt hash `2e62e157adacc30eb21e459c53e3db43432cbb8731e2d12f98c8ee61699439fe`, and prior Kun review hash `a1d73e2e6933228da3caa68ddb24ab70871d7c180371ed141e67f031c10bfde0`. The archived source compiles.
- I rely on Kun's already completed clean exact replay, as allowed by the correction order; its review packet says the generated MP4 was byte-identical. The newly archived bytes are exactly the same renderer bytes used by that replay.

Required-file hash ledger:

| artifact | SHA-256 |
|---|---|
| `audio/synthesis_receipt.json` | `2e172e19340ac288d730e46846fd3e9a9a785931997e6a29db4d7d4f0a81784f` |
| `audio/timeline.json` | `4dca3a5e0753dde46bffcdc3ee3a39453db46411317b6d205a4119a928f7e450` |
| `build_receipt.json` | `2e62e157adacc30eb21e459c53e3db43432cbb8731e2d12f98c8ee61699439fe` |
| `encoded_qa.json` | `02efc107be0a903e955e6b530134d81cbe93cca106835f3b49f7fb832e41da38` |
| `RECEIPT.json` | `4f9bcd93ab48c16db8809280e546eef47c31fb6fca627a300fdfda7bb1d2c23d` |
| `POST_ENCODE_FREEZE.json` | `0870ef2fe6e441bfa946e4090a18baa1180435fc665e69dba883df186f568993` |
| `source_manifest.json` | `449300fb705ba5853d57d6e52eb52262164ba4c5c5cf7c219f5692369cf61d55` |

## Candidate-local provenance and clean replay ledger

All new tool sources compiled. Their exact manifest entries and receipt bindings are:

| lane | `synthesize.py` | `assemble.py` | `render.py` | `qa.py` | environment | provenance manifest |
|---|---|---|---|---|---|---|
| `mzr-census` | `10cbdcb256e7f…263b` | `1ee6a9aaf033…9e44` | `2174ff9fec9f…9981` | `32d1d9cf8399…ae2` | `7c1972495bbf…883b` | `faf7a7630eae…d590` |
| `fesc` | `10cbdcb256e7f…263b` | `2f9248f9af61…bb84` | `71953059e255…c884` | `32d1d9cf8399…ae2` | `0cf2274391e3…3245` | `a4d26b471bd0…7149` |
| `brightend` | `10cbdcb256e7f…263b` | `2f9248f9af61…bb84` | `71953059e255…c884` | `32d1d9cf8399…ae2` | `f4c2734ffc13…dd5c` | `af66a9c5a43e…e81` |

All three environment snapshots record Python 3.11.15, macOS 26.6.1 arm64, Pillow 12.3.0, FFmpeg 8.1.2 with libx264, and exact current font hashes:

- Avenir Next: `98dec241f3ee712a37fad61aafdb83e225ed54c3e5b6e9f0abeb24eba13743ba`
- Menlo: `dc256e0b39c2a6fec947129d421fef41b8b429f58f9b6e5d1b148c87f775c1f6`

Clean replay used Python 3.11.15 plus Pillow 12.3.0 and the live FFmpeg 8.1.2/libx264 and font bytes. The archived candidate-local renderer bytes were copied to a reviewer-owned temporary execution path because `render.py` snapshots itself to `candidate/provenance/render.py`; direct invocation from that destination would target the source file itself. Each temporary candidate contained only frozen spec, timeline, narration master, source files needed for validation, and exact renderer bytes. Input copies hash-matched before execution.

| lane | frozen spec | frozen timeline | frozen master | renderer | rerender MP4 result |
|---|---|---|---|---|---|
| `mzr-census` | `00a0bb580f81…3c2a` | `d1495001eac9…aa8` | `5c196bf5d615…ee35` | `2174ff9fec9f…9981` | `d6014ac09636…1061b` — exact |
| `fesc` | `a75bce7c4f15…1bb3` | `ceccab164e9f…6149` | `8e40e71229fc…f156` | `71953059e255…c884` | `47eb0d0b151b…5e42d` — exact |
| `brightend` | `4f8b3b7fbf17…f187` | `6634c751ae67…a16d` | `fd8643eebacc…3ed6` | `71953059e255…c884` | `6e0f4b098d6c…c7b4` — exact |

## Non-mutation proof

The digest is SHA-256 over sorted `relative-path NUL file-SHA256 LF` rows for every candidate file. Pre- and post-review values and file counts are identical:

| lane | files | pre-review tree digest | post-review tree digest | result |
|---|---:|---|---|---|
| `mzr-census` | 141 | `024ed6b31dbe28fb2c362b046b5ac6ca8db2058b6bba21cf2586600949ab479b` | same | UNCHANGED |
| `fesc` | 148 | `1f2f5b4aaed54811592cb779436ee45fea746151b4d8d74df53c559e7b69dfc9` | same | UNCHANGED |
| `brightend` | 137 | `0e9dc06b9da09ea8ddf3a9edf247008d1b5226482a9d23169703b71d15ea9a62` | same | UNCHANGED |
| `mzr-anchor` | 129 | `73c9eb86608369c627e167ca9023c1668630a0fc1481658678c38dce012fabcb` | same | UNCHANGED |

The clean-rerender root was deleted after all three matches. The local ASR WAVs and reviewer scripts/results were deleted after this packet was written. No candidate, public tree, cockpit, database, Git history, upload, deployment, or gate was changed.

## Residual caveats

1. **TTS parameters are attestations:** Alloy identity, speed 1.18, provider routing, and call boundaries are not recoverable from codec headers alone. Exact receipt structure and unique hash-bound sentence assets are consistent with the contract.
2. **Recorded sentence paths are shared-root-style:** receipt/timeline paths include `audio/<slug>/...`, while candidate snapshots store the same bytes under `audio/raw` and `audio/decoded`. I resolved both forms deliberately and required hash identity. Exact rendering depends only on the preserved master WAV, but resynthesis/assembly tooling should retain this resolver convention.
3. **Cross-host rendering remains bounded:** absolute macOS font paths and version-only environment capture make this proven current-host replay, not proof that a materially different OS, font build, Pillow, or libx264 will emit the same MP4 bytes.
4. **MZR-anchor packaging remains handoff-scoped:** its renderer is now preserved and hash-bound under `integrator/renderer-archive/...`, closing the missing-byte defect, but the candidate directory by itself still lacks that source/environment packet.
5. **MZR-anchor STT provenance remains thin:** unlike the three corrections, its old `encoded_qa.json` does not name the transcription provider/model. This rereview did not rely on that omission: it reproduced the exact transcription input and ran a fresh local ASR pass.

## Final disposition

Kun independently accepts the correction-round set for **audio quality, synchronization, 48 kHz timing, managed-audio receipt consistency, no-music evidence, introduction delivery, peak/motion behavior, deterministic exact replay, and renderer-byte custody** on the four hashes above.

**Final: `KUN_PASS_WITH_RENDERER_PORTABILITY_CAVEATS`.** All publication/reporting gates remain closed unless and until the integrator separately acts on the complete independent review set.
