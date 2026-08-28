# Goru sibling correction-round independent mechanical and numeric-source re-review

## Overall verdict

**PASS — 4/4 exact correction-set candidates pass Goru's independent mechanical-integrity, numeric-source, preservation, and closed-gate re-review.**

**Exact failures: none.**

This verdict is hash-bound to the four MP4s below. It does **not** authorize promotion, integration, upload, publication, a public/shared MP4, `frontend/public`, `paperVideos.ts`, cockpit mutation, database work, deployment/restart, or any Git action. Scientific-boundary/narrative acceptance and audio/reproducibility acceptance remain Lana's and Kun's independent gates.

## Authority, reviewed inputs, and independent method

- Authority: `HWAO_SIBLING_ROLLOUT_ORDER.md`
- Independently recomputed authority SHA-256: `220b8b60406c9662f2b73e679cbb6205a98beb9176c14d2f987d5aa0967623f5`
- Prior Goru rollout review SHA-256: `8fe6184402707aaaf6db1bd2e926a49b3d2a219eee3fb60b7047d23345cea2e0`
- Correction receipt SHA-256: `29870e0ceab8350d94a9187bee3139709ced0eb18512d96ada7336f351c5c681`
- Correction audit SHA-256: `f26c13b1416ece1e3b99c2a52e4c88b5e07e42075e997577b5b52c6da8b6d1cb`

I read the authority, prior Goru/Lana/Kun reviews, correction receipt, correction audit, every candidate's `spec.json`, `numeric_guard.json`, `audio/timeline.json`, `audio/synthesis_receipt.json`, `build_receipt.json`, `encoded_qa.json`, `source_manifest.json`, `RECEIPT.json`, `POST_ENCODE_FREEZE.json`, and `PREDECESSOR.json`, plus the corrected candidates' provenance manifests/tools and MZR-anchor renderer archive.

I did **not** run the producer QA or mutate/reseal any candidate. Independent replay included fresh hashes; exact receipt/freeze bindings; full `ffprobe -count_frames`; full mapped H.264/AAC decode through EOF; exact encoded-check boolean census; PCM/sample/timeline/WPM reconstruction; section-span reconstruction; 160×90 gray 2-fps motion replay; fresh extraction of all 22 sentence midpoints plus five peak frames per lane; exact comparison of those 108 fresh frame derivatives with the stored derivatives; fresh Tesseract OCR; independent renderer-width caption wrapping plus SRT cue census; normalized introduction similarity and fresh introduction-PCM extraction; renderer-consumed numeric projection; complete source/provenance manifest replay; reviewed-predecessor and original-predecessor hashes; rejected-attempt hashes; accepted-v3 preservation; recursive case-insensitive `SOURCE_FREEZE.json` census; full-file hash/name census of `frontend/public/videos`; and gate-map equality.

## Exact hash custody

| lane | exact MP4 SHA-256 | spec SHA-256 | timeline SHA-256 | narration master SHA-256 |
|---|---|---|---|---|
| `mzr-census` | `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` | `00a0bb580f81985f8bd095f33c46ad6aa9ae4f240f8a89fe4cfe1a6e7ba53c2a` | `d1495001eac971557edab645cdc579e0c8f4635f42282aba45ca4f286f398aa8` | `5c196bf5d6158a085e426387bb473ddc23ceecef8004b5e247d580bdf6c0ee35` |
| `fesc` | `47eb0d0b151b51667a4b29a39da74b947086c925dda7ce7e819240ffde25e42d` | `a75bce7c4f1534fa13a4e47c3dc93dffaf76e7a1b731f73e955ee0a517aa1bb3` | `ceccab164e9fc014490fbd00aae6fc4a35696fddc27930bf4e4f35198e856149` | `8e40e71229fc3e0bf2f21e7f02f8c3370e1042a62ffadb03fb2ff10f96adf156` |
| `brightend` | `6e0f4b098d6c5386d08ab7fb670b8b6564e257edeac5dc1c6fec2cc6b97bc7b4` | `4f8b3b7fbf17af4b49067dc4bd223e2304e81689382f36d6897830539f6df187` | `6634c751ae6713b8f9e2a8b45bb7e1a14152cea05c09fd683ec7fe9dc3efa16d` | `fd8643eebacc898d2bc49a81e3d1a46ed8878de0e65e55db7ed42fae609e3ed6` |
| `mzr-anchor` | `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970` | `c868b5bb7509edf1aa1d183c1dca6265c854081bd7f7f63fff72d9fcdd5f4910` | `4dca3a5e0753dde46bffcdc3ee3a39453db46411317b6d205a4119a928f7e450` | `b0900ec6c8146bedae3497d4c4141e81edfc66ad19478faea90b2211d0053df7` |

| lane | synthesis receipt | build receipt | encoded QA | source manifest | receipt | post-encode freeze |
|---|---|---|---|---|---|---|
| `mzr-census` | `7fdb79a6cf97d429686240b8048568387a221611261d73dfbf0bb943a164ddf5` | `dc3e062599b5f9b62785361fc3c0e0a244589012b788ed5efeda65f3445ebffc` | `d42b845ec6e0671b424dad29586b32377e7b306fa40ad99c62153b0c96a4767e` | `572fe84f84be0271f314ceea80d107e2cab2abfa255e865b1b4894a770a8d7bd` | `dd3b1469c17577e8f8996a8f08fc3ac387bcce442ec03e1f064cf3bf9889bc5e` | `7e1ae8588329b63943bfbb4c8866cd0640088340194e673333ad802a5444cd79` |
| `fesc` | `796bb3a64aab9f1e24a23185c020f1e47e94a738ac21e4b4359ed9cc3d703372` | `0b8f5512aac6e360d08ede9775aa873f092c39d3414a07cb7f4d81ae0bae91a3` | `7f78b75ead8ba6b686d1bd226bd49a9cb125af29ceb53cb015b6353467f521a9` | `555b2d58cb56f309c439d87b0db3f4ba0e5a8822511a0fee7f6de99905e0c088` | `c4201a6d3af8e1f94514ba7346af89ed90b232a0d3a24e96afef2c9f77f56800` | `5691d9df902c0eeddfa3375b3281b7de2cab1c0a392c49eab6a778d543cc48de` |
| `brightend` | `e13ff5ddb20bd82f5dfe2d145709e1c66ce5c6b25ac7fc40528940765ff8b569` | `c93c6bd4c22054e77bf0f7ebe2e3a9ce3ac1a08997bbafc38f723fad2dd13294` | `f090cfa42d08c8f8c010b9706901b1cd649422b7d13e75fb81b3aef92e0869a6` | `63921f5dedb05a335e5f4c9dcb1db8d8b78a96e15cdcddfa93a03385620a591f` | `159b9cc981f80cdba45a1197260f765fde56bfcd6a663d03c7c07983d67c5574` | `fcdcbe6c4d82da22da828898fe59edc89f686503728020bc80ee482aaaef80f9` |
| `mzr-anchor` | `2e172e19340ac288d730e46846fd3e9a9a785931997e6a29db4d7d4f0a81784f` | `2e62e157adacc30eb21e459c53e3db43432cbb8731e2d12f98c8ee61699439fe` | `02efc107be0a903e955e6b530134d81cbe93cca106835f3b49f7fb832e41da38` | `449300fb705ba5853d57d6e52eb52262164ba4c5c5cf7c219f5692369cf61d55` | `4f9bcd93ab48c16db8809280e546eef47c31fb6fca627a300fdfda7bb1d2c23d` | `0870ef2fe6e441bfa946e4090a18baa1180435fc665e69dba883df186f568993` |

For every lane, actual MP4 byte count equals the build receipt; actual MP4/spec/timeline/audio hashes equal all binding fields; actual receipt hash equals `POST_ENCODE_FREEZE.json.receipt_sha256`; and the receipt's predecessor object equals `PREDECESSOR.json` exactly.

## Tool and environment custody

The three new correction candidates each have a complete five-row provenance manifest whose listed paths, byte counts, and hashes equal the actual candidate-local files.

| lane | synthesize.py | assemble.py | render.py | qa.py | render environment JSON |
|---|---|---|---|---|---|
| `mzr-census` | `10cbdcb256e7bfb60e79472adf2d8d7bae6490f26a2e28203de45cdbdbc4263b` | `1ee6a9aaf03355242ebdcf6fc146f7d6f0fad0172649dabcc635c083a8fb9e44` | `2174ff9fec9fcfbc81e078f8ca43df807206eb6b7dffdb6ab210a499d07d9981` | `32d1d9cf839907802fb02dcde59c8c2fcc48cc98fa9a23ae1d89a59725a89ae2` | `7c1972495bbf6de10df7e32c8d5aec96e8b89e66fc43a95732278ecc27d4883b` |
| `fesc` | `10cbdcb256e7bfb60e79472adf2d8d7bae6490f26a2e28203de45cdbdbc4263b` | `2f9248f9af61030b012ba7d9bed1fb9f8d302350b5ecea3db24c541b1ea3bb84` | `71953059e2555cae36bf056aa80bdc7440170eb82c106606136dcc4daa74c884` | `32d1d9cf839907802fb02dcde59c8c2fcc48cc98fa9a23ae1d89a59725a89ae2` | `0cf2274391e3ffc21d03a830504f10a6b52837a46a8401fe0d4dc0a5a4b33245` |
| `brightend` | `10cbdcb256e7bfb60e79472adf2d8d7bae6490f26a2e28203de45cdbdbc4263b` | `2f9248f9af61030b012ba7d9bed1fb9f8d302350b5ecea3db24c541b1ea3bb84` | `71953059e2555cae36bf056aa80bdc7440170eb82c106606136dcc4daa74c884` | `32d1d9cf839907802fb02dcde59c8c2fcc48cc98fa9a23ae1d89a59725a89ae2` | `f4c2734ffc13c7a53965932aff9965b212a3c4675bbbcb64cbdc9134ed2ddd5c` |

The synthesis receipt binds `synthesize.py`, the timeline binds `assemble.py`, the build receipt binds `render.py` and the environment JSON, and the final receipt binds the complete provenance manifest; every binding reproduced.

The unchanged MZR-anchor does not gain a candidate-local provenance directory in this correction round. Its external renderer archive is intact: archived renderer actual/declared SHA-256 `7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53`; `ARCHIVE.json` SHA-256 `bf5e8521c1ce68d59812fd98f96ea8f40a4e27f9612d27a46fe89fdc38ce6a98`; archived candidate and build-receipt hashes match the unchanged candidate; and current Avenir Next/Menlo bytes reproduce archived font hashes `98dec241f3ee712a37fad61aafdb83e225ed54c3e5b6e9f0abeb24eba13743ba` / `dc256e0b39c2a6fec947129d421fef41b8b429f58f9b6e5d1b148c87f775c1f6`.

## Encoded media and timing replay

Exact encoded-check arithmetic is **28 + 28 + 28 + 27 = 111/111 literal `true` values**. Each JSON has exactly the declared number of uniquely named checks, `status=PASS`, `passed=total`, and no non-boolean truthy substitute.

| lane | full decode / media | frames / duration | WPM (words / occupied seconds) | max A/V action delta | peak vs runner-up | motion mean MAD / longest <0.08 | loudness / true peak |
|---|---|---|---|---|---|---|---|
| `mzr-census` | PASS; H.264/AAC, yuv420p, 1920×1080, 30 fps, 48-kHz mono | 6,899 / 229.966667 s | 115.000000459 (435 / 226.956521) | 0.016292 s | 50.043083 s vs motivation 32.486313 s | 0.440571593 / 0.0 s | -21.65 LUFS / -2.32 dBTP |
| `fesc` | PASS; H.264/AAC, yuv420p, 1920×1080, 30 fps, 48-kHz mono | 7,102 / 236.739000 s | 115.000002674 (448 / 233.739125) | 0.015333 s | 52.253667 s vs motivation 33.004250 s | 0.395180526 / 0.0 s | -20.24 LUFS / -2.30 dBTP |
| `brightend` | PASS; H.264/AAC, yuv420p, 1920×1080, 30 fps, 48-kHz mono | 6,836 / 227.869000 s | 115.000001390 (431 / 224.869563) | 0.014500 s | 47.053000 s vs motivation 29.475750 s | 0.411422924 / 0.0 s | -20.05 LUFS / -2.29 dBTP |
| `mzr-anchor` | PASS; H.264/AAC, yuv420p, 1920×1080, 30 fps, 48-kHz mono | 6,586 / 219.533333 s | 115.000005292 (415 / 216.521729) | 0.016250 s | 47.459667 s vs motivation 28.316750 s | 0.439633752 / 0.0 s | -20.92 LUFS / -2.30 dBTP |

Additional independent timing/audio facts:

- All 88 spec sentence IDs equal timeline and synthesis-record IDs in order.
- Each first-four sequence is exactly `i01`, `i02`, `i03`, `i04`, all `section=motivation`, `visual=intro`.
- Every sample-to-second, frame-to-second, cursor/pause, decoded-WAV format/frame-count, and text/text-hash relation replayed. Each narration master is mono signed 16-bit PCM at 48 kHz with the exact timeline frame count and duration.
- Every recomputed section span equals the timeline map; `peak` is strictly longest in all four lanes.
- Fresh introduction PCM extractions are byte-identical to the stored derivatives. Recomputed normalized transcript similarities are `1.000000`, `1.000000`, `0.997722096`, and `0.998760843` in rollout order; `if`, `would`, `could instead`, and `how do we tell` survive in all four.
- MZR-census's -21.65 LUFS measurement passes its preserved -21.80 to -19.00 LUFS correction tolerance and remains below the -2.0 dBTP ceiling. FESC's preserved first render, not the accepted correction render, is the -22.01 LUFS hold described below.

## Frames, captions, and OCR

For each lane, I freshly extracted all 22 sentence-midpoint frames and five peak samples from the exact MP4 using the timeline times. All **108/108** fresh JPEG hashes equal the stored encoded-frame hashes. Each lane has exactly five distinct peak hashes. The 160×90/2-fps motion replay above independently confirms positive motion and no near-unchanged run at the 0.08 threshold.

Caption replay: **22/22 SRT cues per lane**, in spec/timeline order with exact sentence text; renderer-width wrapping using the recorded Avenir Next bold face gives a maximum of **2 lines** in every lane and equals each stored caption map. Total: **88/88 cues covered**.

Fresh Tesseract on the 108 fresh encoded-frame derivatives finds no forbidden internal term (`/Users/`, `.json`, `.md`, `SOURCE_FREEZE`, `STATUS.json`, `T1_`, `T2_`, `T3_`, or `internal path`). OCR's standalone digit-like tokens are auxiliary false positives from diagrams/icons, not numeric-source evidence:

- MZR-census: `2`, `3`, `5`, `7`
- FESC: `2`, `5`
- Bright-end: `0`, `5`
- MZR-anchor: `4`

Examples include noise strings such as `@ —2®`, `GAS-PHASE ABUNDANCE 3 ° >`, `i 4`, and `5 DISCOVERY RECEIPTS`. None equals `178`, `21`, or `157`; none exists in the renderer-consumed audience strings. I therefore do not promote these OCR hallucinations into displayed scientific numerics.

## Numeric-source and no-result audit

I rebuilt the audience projection from renderer-consumed surfaces only: `short_title`, `series_label`, narration captions, display citations, and visible sentence `params`; I excluded IDs, revisions, paths, hashes, timestamps, source filenames, and contact-sheet labels. I applied the archived renderer's numeric grammar `(?<![A-Za-z0-9_])(\d[\d,]*\.?\d*)(?![A-Za-z0-9_])`, normalizing commas.

| lane | visible numeric occurrences | guard evidence rows | source manifest | grounded runtime | verdict |
|---|---:|---:|---:|---:|---|
| `mzr-census` | 0 | 0 | 11 listed = 11 actual | 99.739081111% | PASS |
| `fesc` | 0 | 0 | 9 listed = 9 actual | 99.746556468% | PASS |
| `brightend` | 0 | 0 | 11 listed = 11 actual | 99.736691468% | PASS |
| `mzr-anchor` | 0 | 0 | 10 listed = 10 actual | 99.726678538% | PASS |

Every source-manifest path exists, and every listed byte count and SHA-256 matches current bytes. Every sentence `grounding` resolves to a manifest-listed candidate-local source. Grounded runtime was recomputed from record starts through the next record/master end, not copied from build receipts.

**MZR-census correction closure:** `178`, `21`, and `157` are absent from renderer-consumed narration/params and fresh OCR. Every sample-stage `count` is the empty string. Narration explicitly withholds retrieval totals, filter totals, stage totals, final eligibility count, and fraction. The current empty numeric guard is therefore valid: **no realized count is displayed or narrated**.

**Cross-lane closure:** the other three lanes also have zero renderer-supplied digit occurrences and zero guard rows. Their stage counts remain blank; estimators remain symbolic/unevaluated; any possibility labels are equal unselected states rather than a stated value/sign/outcome. No lane gains a numeric result.

## Preservation

### Reviewed predecessors and original predecessors

| lane | reviewed predecessor MP4 actual/declared | original predecessor MP4 actual/declared | original storyboard actual/declared |
|---|---|---|---|
| `mzr-census` | `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536` | `07f08990124748e2e074cf393e5d34e064ed655a85ea827356bc98b44d3cc274` | `8ddd7951bd0d20673e6832cd66b6993e0c65a4ae54f2a4ec734af72db296c842` |
| `fesc` | `b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168` | `840ced2b52c2007bc5387fc69b49527c548daca6f6d81b3f14bc9a43b7e9b5af` | `e470ca87d630d797acd235b3f4927139971e655805ec36efac81282e5b0bac55` |
| `brightend` | `9a137c61011a3d9629c96ebbf365955295e11082cededa325ceb38f1ce268a2f` | `1d84b8755e0baf726c86625baac6335fb9ca91f3356786b5b363976aa26c76d2` | `f29b8cb4b5790773c516f264d8c449125645c3027c8b6bcb24b6909bc1524482` |
| `mzr-anchor` | unchanged correction target `973daba3…` | `02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8` | `71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c` |

All actual hashes equal their declarations. The correction candidates' predecessor objects equal their receipts. The three superseded reviewed canaries and each one's original predecessor video/storyboard remain present; MZR-anchor remains byte-identical.

### Rejected correction attempts

- **MZR-census QA hold:** preserved directory tree digest `c9098d1351921f67089d73dbff4ce3a0d32fab81691626758272f53023e9ac58` (4 files). Preserved `encoded_qa.HOLD1.json` SHA-256 `b2b207581ef34dbf56d6b04543f61120c261f92ef9bcb591e2cde429ecfca5d2` is `HOLD`, 27/28, with only `loudness_in_target_band=false`; it binds the current unchanged MP4 `d6014ac0…`. Preserved/current contact-sheet hashes match. This confirms the QA threshold correction did not rewrite the media.
- **FESC first correction render:** preserved directory tree digest `3830e823b90df74d6aec847c77da514ccbf430ec3047966b099635563148b0aa` (13 files). Preserved MP4 actual/declared SHA-256 `b5013cd341cab940188db82df0ae57d64f9ec08c0f786a90d6b782bb75599af1`, 9,929,556 bytes. Preserved QA is `HOLD`, 27/28, only loudness false. Timeline `874cfdac8fdd5beafb0abbbaf9e89aeb701f1410af087715a0f575a6fb41ed0d`, audio `c333c18297370d8a1832d58761decf03d8627e73811fbf7e6d1f14b566656a5a`, renderer `71953059…`, and environment `0cf22743…` all reproduce the preserved build receipt.

### Accepted v3

The accepted spin-v3 MP4 remains SHA-256 `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240` (16,065,978 bytes), matching its build receipt and the nested MP4 row in `POST_ENCODE_FREEZE_V3.json`. Build receipt SHA-256 is `3dd4155681c10c90eef0e5b5d1f7a9262d47cb1b7e9f83c906e60f090a2f511f`; freeze SHA-256 is `ff06913e1d630172da02a4aa02c0b73ab9478897ed72f9cb4f1591d2583afdc9`; accepted Hwao verdict SHA-256 remains `432d729882f097841b78c3dd799768757378f0984abcd55be2b689125b2ae315`.

## Source-freeze absence, public absence, and gates

- Recursive case-insensitive filename census finds **no `SOURCE_FREEZE.json` anywhere in any of the four exact candidate trees**.
- A full-file SHA-256 and exact-filename census of all files under `frontend/public/videos` finds **zero name hits and zero hash hits** for all four correction candidates. The root currently contains only the pre-existing baseline/review files; tracked diff is empty. Git reports the entire public-video root as pre-existing untracked state, and this review did not modify it.
- Both `RECEIPT.json` and `POST_ENCODE_FREEZE.json` contain exactly this false-valued map for every lane: `upload=false`, `cockpit_or_video_root_copy=false`, `git=false`, `video_reportable_now=false`.
- `spec.json.video_reportable_now=false` and `build_receipt.json.video_reportable_now=false` for every lane.
- No candidate/public/cockpit/DB/deploy/Git/upload change was made by this re-review.

## Per-lane verdicts

- **MZR-census — PASS.** Exact candidate `d6014ac0…`; 28/28 encoded checks; full decode/timing/motion/caption/OCR/manifests/hash custody pass; no audience digit, no `178`/`21`/`157`, no realized stage or eligibility count; predecessor/rejected-hold/public-absence/gates pass. **Exact failures: none.**
- **FESC — PASS.** Exact candidate `47eb0d0b…`; 28/28 encoded checks; full decode/timing/motion/five-peak/caption/OCR/manifests/tool-environment custody pass; zero audience digits/results; reviewed predecessor and rejected `b5013cd3…` attempt preserved; public absence/gates pass. **Exact failures: none.**
- **Bright-end — PASS.** Exact candidate `6e0f4b09…`; 28/28 encoded checks; full decode/timing/motion/five-peak/caption/OCR/manifests/tool-environment custody pass; zero audience digits/results; predecessor/public-absence/gates pass. **Exact failures: none.**
- **MZR-anchor — PASS.** Exact unchanged candidate `973daba3…`; 27/27 encoded checks; full decode/timing/motion/five-peak/caption/OCR/manifests pass; zero audience digits/results; exact archived renderer, archive environment/font custody, predecessor/public-absence/gates pass. **Exact failures: none.**

## Two-ended non-mutation custody

Opening deterministic candidate-tree digests (sorted relative path + file hash + byte count):

- MZR-census: `283d65be04961eb55d2c3ad0d9481cffa868212b16083541da1e4870eb0d59b0` (141 files)
- FESC: `3cfc338931c0f0b85f08c6aa2bd4b924503204444479d52a646f3856efb6e33e` (148 files)
- Bright-end: `7bf76a096a2e71af53f5574b5134a8388b55220cb4d12a57280b085b9895aab6` (137 files)
- MZR-anchor: `a69eeec7bd43404c56efd172b427938b6c6c1b521fcbcb501e3fb1cfbeb2b268` (129 files)

Closing replay after the packet write reproduces all four opening tree digests and file counts exactly. Authority, prior Goru review, correction receipt, and correction-audit hashes also reproduce their opening values. **Start/close custody: PASS; candidate or governing-input drift: none.**

**Final Goru disposition: PASS — 4/4. Exact failures: none. Promotion remains withheld pending the complete independent review set and coordinator action.**
