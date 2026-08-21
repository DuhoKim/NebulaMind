REFUTED_DECISION_MEMO_FINAL

# Final adversarial gate — Decision Memo Revision 4 and Chi Custody Receipt Revision 5

## Verdict

The two-artifact record is **REFUTED**. All four expressly requested Revision-3 repairs are present, the receipt's fenced table is byte-identical to a fresh generator run, the memo's gate-history excerpt is an exact contiguous slice of that run, the verdict-estimator correction is complete inside the two target documents, and the central procedural/condition-2 theory survives.

The generated record nevertheless contains three independently dispositive defects. First, “Revision 3's hash is cited by NO gate” is false: the exact 64-hex hash occurs in at least five gate artifacts outside the generator's two-file glob. Second, the detector's `VALUE(words)` rule turns unrelated pre-crossing “zero point” speech in `archive-2.html` into a chi disclosure; both target documents then falsely say the three spoken chi values survive on that page. Third, the receipt's composed “No code path computes [an aggregate]” claim is false: the current HC-1H implementation ranks authorized-measurement `abs_chi`, computes two tertile cutpoints, builds nine strata, and records stratum populations. The widened input set is also not complete, although the receipt now discloses several blind spots.

## Closure audit of the four required changes

| Required check | Result | Evidence |
|---|---|---|
| “reviewed” attribution deleted; citation distinguished from review | **HOLDS as a deletion** | `build_custody_tables.py:78-85` prints `hashes cited`, `CITATION IS NOT REVIEW`, and non-determinability; no `reviewed` field remains. |
| hard-coded “at most once” conclusion deleted | **HOLDS as a deletion** | The source contains no such output or multiplicity conclusion; fresh output makes no gating-count claim. |
| input set widened to deck JSON, embedded SVG, report HTML, archive pages | **HOLDS for those four root classes** | `ledger():61-73` scans root narration, root `*.deck.json`, root `report-2026*.html`, and root `archive*.html`. |
| literal `\u03c7` HTML-embedded JSON escape detected | **HOLDS** | `detect():27` matches Unicode chi and a literal escaped form; fresh output reports `VALUE(num)` for both the deck and report HTML at `20260821T004950`. Direct source inspection finds Unicode `χ` in the deck and literal `\u03c7` in the HTML. |

Fresh execution output SHA-256: `b272cfe10ade5bfa2fe8e69ac6af8006bc2737529632daba1d1934c5852fa3f0` (2202 bytes). The receipt's fenced block is exactly all 2,202 bytes including final newline. The memo's 539-byte block occurs byte-for-byte at output offset 71; it is a deliberate excerpt that omits only the generator's `A. GATE HISTORY` heading and following blank line.

## Ranked findings

### 1. BLOCKING — “Revision 3's hash is cited by NO gate” is false

Current footprint Revision 3 SHA-256 is:

`6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`

The generator searches only `GATE_FOOTPRINT_GEOMETRY*.md` (`build_custody_tables.py:39`). A prereg-wide exact-hash search finds that same full hash in these gate artifacts:

- `GATE_DECISION_MEMO_20260821.md:33,233`;
- `GATE_DECISION_MEMO_R2_20260821.md:26,157`;
- `GATE_DECISION_MEMO_R3_20260821.md:178`;
- `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md:137`;
- `GATE_VOID_ON_DESIGN_DEFECT_20260821.md:173,218`.

Those appearances are citations, not proof of which bytes were reviewed. But the generated statement is specifically about **citation**, not review. Its unqualified “NO gate” is therefore refuted by the files. This falsifies the generated A-table line repeated at memo `:57` and receipt `:40`, and the receipt's composed claim at `:85-87`.

### 2. BLOCKING — `archive-2.html: VALUE(words)` is a real false positive, and both documents misdescribe it

`archive-2.html` contains no `first 3 real values`, no `zero point 27`, no `minus zero point 20`, no `one leaning each way`, no exact exemplar, and no raw bits. Its six detector hits are unrelated older speech, including footprint variance “zero point 13”, Longo/sign-convention “minus zero point 12”, and sigma/floor numbers.

The regex `(?i)(zero point|minus zero|real values?:)` has no chi context. It therefore emits `VALUE(words)` for `archive-2.html`, and the B-table labels that result a “CHI DISCLOSURE.” Memo `:113-115` and receipt `:79-80` go further and say the spoken empirical chi values survive on `archive-2.html`. They do not. The actual three spoken values survive in `archive.html` and the 23:12 narration/report HTML, not in `archive-2.html`.

### 3. BLOCKING — the receipt's universal no-aggregate-code claim is false, and its artifact claim remains unverified

Receipt `:100-104` says: “Per-object records only in the chi tree. No aggregate artifact. No code path computes one.” The card-selection subclaim is accurate: `nm_report_graphics.py:441-442` selects `rows[h % len(rows)]` from the seed-key hash, not from chi rank/value.

The universal code claim is not accurate. `handcheck/nm_handcheck.py` accepts `authorized_measurement` rows (`:508-554`), ranks `abs_chi` into tertiles (`:557-565`), computes two numerical cutpoints (`:568-574`), builds nine `committee_state|tertile` strata (`:575-590`), and records stratum populations (`:490-494`). That is a code path computing summaries/aggregates over chi by the frozen design. The generator never scans source code and proves none of this paragraph.

The separate “Per-object records only in the chi tree / No aggregate artifact” state claim is **HOLD**, not verified: this gate obeyed the prohibition on opening or listing the protected chi tree. Read without an implicit tree-only qualifier, “no aggregate artifact” is also overbroad because the 23:12 publication artifact contains the complete then-existing three-value aggregation.

### 4. MATERIAL — widened scanning is not a complete surface inventory

Every place found where a disclosure could live was classified and checked:

1. root authored narration `.txt` — scanned by generator; content checked;
2. root deck JSON — scanned; headings, bodies, attributes, notes, and embedded SVG are all present in the raw JSON;
3. root report HTML — scanned; includes caption and embedded deck JSON/SVG;
4. five root archive HTML pages — scanned, but without a crossing-time filter, causing finding 2;
5. rendered MP3 audio — **not transcribed**, expressly disclosed by the receipt; 14 selected root/alias MP3s and three draft MP3s were hash-inventoried only;
6. external PNG graphics referenced by post-crossing decks — **not scanned by the generator**; six root/draft-referenced images were inspected. Four cutout grids contain galaxy pixels only. Two sky maps contain transfer/parent counts, but no chi value, sign, or raw bits;
7. `_drafts/` — **not reached by the root-only globs**. Twelve on-machine draft artifacts exist. Two Hwao draft narrations/decks contain a `2,771 galaxies have real chirality values` count; their MP3s were not transcribed. `postprocess.log` proves both Hwao stamps were processed into archive builds before their root copies disappeared;
8. dynamic/static page shells (`status.html`, `deck.html`, `play.html`, `play-20260820T232407.html`, `listen.html`, `catchup.html`) — checked. Current shells contain no extra empirical value/sign; they fetch the already-enumerated queue/text/deck/audio surfaces;
9. queue, playback receipts, timing JSON, latest aliases, sequence/duration metadata, and logs — checked. They add publication/playback/processing custody, not a new current empirical value/sign. `latest_transcript.txt` and `latest.mp3` are mutable aliases outside the generator's content globs;
10. ASR JSON — a possible authored-text replacement class, but no post-crossing report in this corpus has one; the generator would not scan it if present;
11. deleted/overwritten files, off-machine copies, and publication outside `queue.json` — not closeable from current bytes and appropriately named as blind spots.

The generic “outside queue / deleted / off machine” caveats keep the receipt from claiming closed-world absence. They do not make the widened input set complete, and they do not cure affirmative false positives.

### 5. MATERIAL — detectors are neither sound nor complete

The lane-local adversarial battery exercised the actual `detect()` function on 23 cases; 17 failed their semantic expectation. Representative under-matches:

- `CHI = 0.4`, `&chi; = 0.4` in raw deck JSON, `χ: 0.4`, `χ equals 0.4`, and `χ = −0.4`;
- alternative spoken numbers (`plus point two and minus point one`);
- sign disclosures (`one clockwise and one counterclockwise`; `the two chi signs are opposite`);
- count disclosures (`2,840 objects now have chirality values`; `2,840 galaxies now have real chirality values`);
- raw bits alone (`chi raw bits 0x3c57a3d8`).

Representative over-matches:

- `The photometric zero point is stable.` → `VALUE(words)`;
- `Three real values: latency, throughput, and cost.` → `VALUE(words)`;
- policy/telescope “leaning” → `SIGN`;
- `Galaxies carry dust` and `Galaxies were measured for redshift` → `COUNT`.

Thus a positive detector row is not intrinsically a chi disclosure, and a missing row is not proof of absence. The receipt states the latter but not the former. Actual over-match in finding 2 makes this a present defect, not a hypothetical test-quality advisory.

### 6. MATERIAL cross-reference seam — the target correction is complete, but its named successor note still states the old falsehood

Inside the two target documents, the verdict-estimator correction holds: no surviving sentence says a verdict estimator executable is built, gated, or frozen; searches find no `_verdict_20260821/` and no `verdict_runner.py`; the build spec itself says no implementation exists and describes work still to be built. Memo `:134-139` is accurate and makes no forward estimator claim.

However, memo `:132` directs the reader to `SUCCESSOR_SCOPE_20260821.md`, whose `:85-87` still says “The verdict estimator built under [the spec] becomes the starting point.” That external source contradicts the corrected record. I do **not** treat it as a surviving sentence inside either target document, but it remains a factual seam in the memo's named successor cross-reference.

## Remaining composed-fact audit

| Claim | Ruling |
|---|---|
| Freeze-time HC-6: `N=130,076`, `a=0.999711`, `A_eff=0.04077642`, power about `1.0000` | **HOLDS** against BS-8 and frozen HC-6. |
| Second HC-6 firing awaits complete accepted `N`, strata, full HC-1H lower-bound `a` | **HOLDS**; the optional 150-label pilot is distinguished from the full 850-label HC-1H. |
| HC-6 formal inputs are only bound `N` and `(2a-1)*0.0408`, not footprint geometry | **HOLDS** against frozen `HC-6:319-329`. |
| `sim_power.py` uses uniform `costheta`, `mean(cos^2)=1/3`, and two-sided p logic while F-3 is one-sided | **HOLDS** against source lines `5-9`, `76-89`, `96-106`, and frozen F-3. |
| Footprint `Var(c)=0.057985`, subset SSE bound `36,253`, geometric bound `4.4888`, one-sided requirement `4.7351` | **HOLDS** against footprint Revision 3 and its independent re-gate. |
| Weights/tau/antisymmetry/committee/hand-check mechanics untouched; statistical estimator/power protocol impeached | **HOLDS at stated scope** against the geometry finding and frozen F-1/F-4/F-7 seam. |
| Seq 20/21/22 and 26/28/30 timestamps | **HOLDS** by direct `queue.json` parse. |
| “52 minutes” from 22:20 to seq 20 at 23:12:51 | **HOLDS at minute-source precision**: 3,171 seconds = 52.85 minutes, 52 whole minutes from the authorization minute's start. |
| Three publications of the exact exemplar; sign statement three times across two reports | **HOLDS** by queue mapping and direct content inspection. |
| Seq 30 playback-receipt context | **HOLDS mechanically**: seq 30 was enqueued 11:02:45 and has STARTED/COMPLETED playback receipts; “mine” and purpose are author self-attestation. |
| Four prior custody versions and three prior memo versions retained byte-for-byte | **HOLDS** against predecessor gate hashes; current superseded hashes match their prior pinned states. |
| Two refuted predecessor declarations retained | **HOLDS** by filename, hash, and gate record. |
| BHU scope without BHU inference; Longo/sky boundaries | **HOLDS**; no result is claimed and frozen headline excludes BHU/isotropy inference. |
| Acquisition-to-completion / successor preservation | **PLAN/forward status, not a verified completed fact**; it does not create a frozen outcome. |
| Archive-2 spoken-value survival | **FALSE** — finding 2. |
| Revision 3 hash cited by no gate | **FALSE** — finding 1. |
| No aggregate code path / aggregate artifact | **FALSE / HOLD** — finding 3. |

## Procedural theory and condition-2 ruling

These attacks failed:

- **No anti-abandonment duty:** the frozen text defines conditional outcomes/reporting but no duty to manufacture an outcome or continue to a statistic. K-8 itself contains stop paths.
- **External reason is not HC-6:** footprint-aware power is not an HC-6 input and the memo does not substitute it into HC-6.
- **No frozen outcome declared:** the memo expressly declines INCONCLUSIVE-BY-POWER, INCONCLUSIVE, REPRODUCED-LONGO, REJECTED-AT-LONGO-AMPLITUDE, and void; it reports an investigator halt outside the preregistration.
- **Condition 2 is adopted accurately and not widened:** the three-value complete multiset and the sign summary are summaries/aggregations over chi; no inspected source establishes a partial tertile, so condition 1 is not declared breached. K-8 section 4's separate no-publication authorization remains a distinct boundary, not a reason to relabel condition 2.

## Failed attacks and facts that held

- The four expressly requested deletions/coverage changes are actually present in source and output.
- The receipt table is exact full output; the memo excerpt is an exact output slice.
- The HTML `\u03c7` repair fires on the real exemplar page.
- No additional root publication event for a fifth individual chi value or third distinct observed-sign sentence was established from current text/deck/report/archive bytes.
- The six inspected external graphics contain no chi value, sign summary, or raw bits.
- Queue arithmetic, publication multiplicity, and 52-minute interval hold.
- The target documents' verdict-estimator correction holds on current repository bytes.
- Power/geometry figures and source quotations survive.
- Procedural theory, condition numbering, and absence of a frozen outcome survive.

## Live-source drift during the gate

The status-audio root was live while this read-only pass ran. Eight generated/index artifacts changed after their first content review: `.durations.json`, all five `archive*.html` pages, `queue.json`, and `status.html`. The SHA ledger below records the **first-review bytes** against which the content findings were made. A later simultaneous recheck sampled these newer hashes:

- `.durations.json` — `3dc7491ff2d9d2b42276bb64b05e221d22c7f9b4a97042468c5ed06a149b1a65`;
- `archive-2.html` — `2ffca8642ef0ff81094ef00264fc15e4d050e6bff3996aa70a545a9708e2bba6`;
- `archive-3.html` — `12486d3c6f65433309cc192a8db473ef6173afe94c7172d0bfd9ee8f6df7c3e0`;
- `archive-4.html` — `a6fa6819316cf0826a42e5808851bc74a137c71eaf5bda7d71e2c90760004fec`;
- `archive-5.html` — `e9851841ba3df6a084d62354fbd07083d6652a4469b1dbbe31f5c3726b8b4c99`;
- `archive.html` — `b994449a1c1a247462faa949db45cf20d060d334910ccc5ed3f1a7edc37afa53`;
- `queue.json` — `19edf5d32fe352765662a9dbd36b22bd3c8210107387c825a873e6ae322d7e09`;
- `status.html` — `d7109d3c622c4039c5827518e86965897ec2f24afb4151861f95d636decc771c`.

The generator stdout remained byte-identical at SHA-256 `b272cfe10ade5bfa2fe8e69ac6af8006bc2737529632daba1d1934c5852fa3f0`. The later `archive-2.html` recheck still contained none of the three empirical spoken values/sign/exemplar/raw bits and still triggered `VALUE(words)` only from the same six unrelated older “zero point” passages, so findings 1–3 and the verdict are unaffected by the live drift.

## SHA-256 ledger — every task artifact reviewed

Execution output (not a disk artifact): fresh generator stdout — `b272cfe10ade5bfa2fe8e69ac6af8006bc2737529632daba1d1934c5852fa3f0`.

- `CHI_CUSTODY_RECEIPT_20260821.md` — `2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65` — content, full
- `CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md` — `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e` — hash/custody
- `CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md` — `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c` — hash/custody
- `CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md` — `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093` — hash/custody
- `CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md` — `acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b` — hash/custody
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md` — `eeb033ab8e32bd58f2360243d220f2d08f7fb85de2f76fc5e42d556c3010d342` — content, full
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV1_SUPERSEDED.md` — `a683bc9424f26fdeabccd414aecdc0b67f08bab86307015e68294612d6a7a5bb` — hash/custody
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV2_SUPERSEDED.md` — `7e1b2e2f4f104ce171c6e9e50ed843ef70417a5f76216bf4e0618b0163ded64f` — hash/custody
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV3_SUPERSEDED.md` — `bafec8bf5f177830d4eeac75a0a7b29c72ea9b7dcfedd3b33f697a283836c62d` — hash/custody
- `DECLARATION_INCONCLUSIVE_BY_POWER_20260821_REFUTED.md` — `af51507a43fcdee4e53b51502c332e3624611bb27de6d0bede120b33c8b38ebb` — hash/custody and cited text
- `DECLARATION_VOID_ON_DESIGN_DEFECT_20260821_REFUTED.md` — `e55460743358bbb0b8c16b8d99e5f4260d0f57a88096dc2c0328f6a675b805ba` — hash/custody and cited text
- `GATE_DECISION_MEMO_20260821.md` — `a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa` — content, full
- `GATE_DECISION_MEMO_R2_20260821.md` — `59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066` — content, full
- `GATE_DECISION_MEMO_R3_20260821.md` — `c1ad25fd6574bb9bf3386d8d6fb7448ed62015384035f9110dbde3e94ec0c453` — content, full
- `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md` — `94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e` — relevant exact-hash citation lines
- `GATE_FOOTPRINT_GEOMETRY_20260821.md` — `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1` — content, full
- `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md` — `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b` — content, full
- `GATE_VOID_ON_DESIGN_DEFECT_20260821.md` — `38e789547e750d21b38fd9d1fa3515bc44ed8f95d542476183d45274c7518b3c` — relevant exact-hash citation lines
- `GORU_BS8_POWER_RECEIPT_20260814.md` — `b6207c7fc93ea7bfeb8045d0e635693010644633b747b298eb51b6233f014a92` — content, full
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` — `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7` — content, full
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md` — `f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee` — hash/custody
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md` — `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76` — hash/custody
- `K8_CROSSING_AUTHORIZATION_20260820.md` — `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69` — content, full
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7` — content, full
- `SUCCESSOR_SCOPE_20260821.md` — `cfca55edaf7d9fe7a8d1dc70f069f4d865ec41b1fb243b3a06f8020e6784b112` — content, full
- `VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` — `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7` — content, full
- `_custody_20260821/build_custody_tables.py` — `681592ffea67b862b5a33444b2af354a0c03594889368ad1c5697d93c6fbd8f8` — content, full; executed
- `_inference_20260820/chi_wrapper.py` — `e9b0ed122f298e531d97e870281b1593444587ec2908a760be10b94b3c03aec3` — content, full
- `_inference_20260820/inference_runner.py` — `fa1e033d6c501854eae3517f23c03c270c6108c47383fa18f5960922fc83c45c` — content, full
- `_tmp_gate_final_audit.json` — `9e8d50af4d81648bd4f763dbdb560a872bf3ecf5246f98330a50c16702888e2c` — content, full; lane-local evidence
- `_tmp_gate_final_audit.py` — `d4093f829d34f1135942ab3ed689eebc664eab6922e4e5b2ea8def074e736040` — content, full; lane-local test harness
- `handcheck/nm_handcheck.py` — `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4` — relevant complete implementation sections
- `repo/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/sim_power.py` — `f2867dbf4f5ab8ad82d645324a525a75af38006ff03e8ee08b90589cff50b1ce` — content, full
- `repo/tools/audio-reports/nm_report_graphics.py` — `223e346f7b5a57e8e7497b6d98efb78c0e4b7fbb971f0171a6473685af0b6f65` — relevant complete generator sections
- `status-audio/.durations.json` — `329e5124bc4af4bf22a143cd56704b5c2fbd445cdbeb81bf27a81dec76649b7d` — content (first-review bytes; later live hash above)
- `status-audio/20260820T230754-tori-report.deck.json` — `d84bf963ce608387298041262614314c1cb7fa4608666178c4ed341a10677928` — content
- `status-audio/20260820T230754-tori-report.mp3` — `27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0` — hash/metadata only; audio not transcribed
- `status-audio/20260820T230754-tori-report.times.json` — `5fcf940bc7346ddb1854c5afd3f4870b8d1396b1a733b6062df6db690d768c4e` — content
- `status-audio/20260820T230754-tori-report.txt` — `7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47` — content
- `status-audio/20260820T231235-hwao-report.deck.json` — `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c` — content
- `status-audio/20260820T231235-hwao-report.mp3` — `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168` — hash/metadata only; audio not transcribed
- `status-audio/20260820T231235-hwao-report.times.json` — `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79` — content
- `status-audio/20260820T231235-hwao-report.txt` — `7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad` — content
- `status-audio/20260820T231324-hwao-report.deck.json` — `855da9448492112c0529476cf451466934c63474068419cb3382009bfb9108ab` — content
- `status-audio/20260820T231324-hwao-report.mp3` — `785aed20de80d27118f915d7a05b02daac1520fc52e919231bd1f575bea0a1ad` — hash/metadata only; audio not transcribed
- `status-audio/20260820T231324-hwao-report.times.json` — `6b0b7294e93b2d5a6df7a7dc9698691b5c9dea180f2958a2c01804e21647cc4a` — content
- `status-audio/20260820T231324-hwao-report.txt` — `5ba48ea353bb94a3a5740c4be8160e552e996670287f124fb66b69d5cf781842` — content
- `status-audio/20260820T232407-20260820T230754-tori-report.mp3` — `27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0` — hash/metadata only; audio not transcribed
- `status-audio/20260820T232407-20260820T230754-tori-report.times.json` — `5fcf940bc7346ddb1854c5afd3f4870b8d1396b1a733b6062df6db690d768c4e` — content
- `status-audio/20260820T232407-20260820T230754-tori-report.txt` — `7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47` — content
- `status-audio/20260820T235925-tori-report.deck.json` — `1af45a7e0cb275f3a3605aa3f3b68e78f899421939306ebac45f8448b66a1f12` — content
- `status-audio/20260820T235925-tori-report.mp3` — `693998040c0e1f72d9331a083b48f5509a7c4d269fcb1aaaf37f0589494566e6` — hash/metadata only; audio not transcribed
- `status-audio/20260820T235925-tori-report.times.json` — `0575577109fa86270e12d89a03b2c76174fb77bb086347ccdd8e3a38ed398f63` — content
- `status-audio/20260820T235925-tori-report.txt` — `e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e` — content
- `status-audio/20260821T004950-hwao-report.deck.json` — `c49c71978ee27eedab93076906a27f188eee3b4b905caed13b674127feab091b` — content
- `status-audio/20260821T004950-hwao-report.mp3` — `b730dfc2b28b05835f548f0aedc1096c7e51e2067a087091b1448384a4092ed2` — hash/metadata only; audio not transcribed
- `status-audio/20260821T004950-hwao-report.times.json` — `5c50db87a9e6389755f159501d3754c97233121bdd496f837c5fd3c7fa522f60` — content
- `status-audio/20260821T004950-hwao-report.txt` — `f1096d51b237dbeaddf92b034194ed9f23d89401b54bb26335b74d1ead81b258` — content
- `status-audio/20260821T080428-blanc-report.deck.json` — `81e12c9a380d2f8a5bb65f2b81d45a0da8dc2877cf8dd22f9bb1dc5da504a3cb` — content
- `status-audio/20260821T080428-blanc-report.mp3` — `264d8731fdf523ac588b13aed142b0f3d4283ba00fd7f8a41b586fd55430c91f` — hash/metadata only; audio not transcribed
- `status-audio/20260821T080428-blanc-report.times.json` — `cba21eae867fdbb9b68307a41cb0d6bbbeaef927fec6fcdab0b12383d10ee752` — content
- `status-audio/20260821T080428-blanc-report.txt` — `452f13b624ff952df0987b7f54feccc632fde6c0f2eb569c365fa92ab968a982` — content
- `status-audio/20260821T105930-blanc-report.deck.json` — `88394b89139669d66bef04ea85c62f591490f11ef767b5f14421784b2a54f131` — content
- `status-audio/20260821T105930-blanc-report.mp3` — `5492a78d89d136e0a9b497da8781e28d33a190e34f286e55454a6c78172a55c6` — hash/metadata only; audio not transcribed
- `status-audio/20260821T105930-blanc-report.times.json` — `37a1d3c6938c2decd29ba6d798ecc9370e8323ad60437af3ce1713f0a6dd5741` — content
- `status-audio/20260821T105930-blanc-report.txt` — `ada74c9a1761ba02f9f0c0fb6c31a3415d4fc80a2619a8776905101d1e146951` — content
- `status-audio/20260821T145923-hwao-report.deck.json` — `8b3ddead69fb6764df63a35352eca9332b52b9472d4626a6e5e05430f20b4ad1` — content
- `status-audio/20260821T145923-hwao-report.mp3` — `21de44c997065b03c8ac4460217f863904e5ba085c110f5cbe38cbb1eea92d00` — hash/metadata only; audio not transcribed
- `status-audio/20260821T145923-hwao-report.times.json` — `729f892f96a5c2e37597bf3184a3274b32e9e552d9bd8f61ceb9e447a4d75f7b` — content
- `status-audio/20260821T145923-hwao-report.txt` — `c3aefdeea36b45e60f63e297bfed77358fda8db3d63560c245386b3d20cba8b2` — content
- `status-audio/20260821T151249-hwao-report.deck.json` — `0fe5ecac190cfcb490cdcc42aa52b1069e7bf2a3b97d996d3faf13ae0030b8cc` — content
- `status-audio/20260821T151249-hwao-report.mp3` — `f468c515b5d852d82d08da0c5a41ee04cd75e7d70139ae9633d77a0e611df53a` — hash/metadata only; audio not transcribed
- `status-audio/20260821T151249-hwao-report.times.json` — `80bcaeddd92bf9e348e10efb257afff179a389e8bfe33187327c1037a21c4cbb` — content
- `status-audio/20260821T151249-hwao-report.txt` — `5648a55e23f6fddfdd9d215c1c64ea8eaf83c6a51fdec991a5f67ba31dc6e37b` — content
- `status-audio/20260821T151843-hwao-report.deck.json` — `6437b0993110b9dca73b811017a0ba49803faa255a413cb89a2ad1c754a691ad` — content
- `status-audio/20260821T151843-hwao-report.mp3` — `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3` — hash/metadata only; audio not transcribed
- `status-audio/20260821T151843-hwao-report.times.json` — `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848` — content
- `status-audio/20260821T151843-hwao-report.txt` — `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c` — content
- `status-audio/20260821T190931-tori-report.deck.json` — `ec91f2ed3499f2bb2d291154b9a18c43b00841082853ac46c31f57a97d192998` — content
- `status-audio/20260821T190931-tori-report.mp3` — `a897ce35c324e6d356350b728f6b16e7398581501718d1991ef72bb4c54fc999` — hash/metadata only; audio not transcribed
- `status-audio/20260821T190931-tori-report.times.json` — `8d0285545d13b7aeeadbbab1bddd8c33a59093ae2475eb7bb8ff36d42fe5a618` — content
- `status-audio/20260821T190931-tori-report.txt` — `c42bc1d4500a8e0db4411715c1237da0ebf9a39d9d88eb1fa7d633367281770b` — content
- `status-audio/20260821T200910-tori-report.deck.json` — `f208eaab7cec9040fa0063bb9f722aab36046ffbae4c49216fb8dc305def1d55` — content
- `status-audio/20260821T200910-tori-report.mp3` — `2a55b081db5861e57390c927e077ae98558dd666ec71d2f677e0f47bdf4d2ee3` — hash/metadata only; audio not transcribed
- `status-audio/20260821T200910-tori-report.times.json` — `899d1c3f7cf9c5996edff78876aded729aa233a76a91ca0ed08a84f92b2d558c` — content
- `status-audio/20260821T200910-tori-report.txt` — `1b7d622e8ef866752b1c9e82ae5d3edb97ebd85c0a9de18847801f32ea658940` — content
- `status-audio/_drafts/20260820T235839-hwao-report.deck.json` — `abbcc68d5b715a85f78a0b920882c2af03319810ad46ba1b3ddb579f7ae3ea3c` — content
- `status-audio/_drafts/20260820T235839-hwao-report.mp3` — `245d5c815cbda18a43f11eb0da2fee885882b1d74f2b29770873d301b17d5eb8` — hash/metadata only; audio not transcribed
- `status-audio/_drafts/20260820T235839-hwao-report.times.json` — `b92fd0a3b628c99c010519ee58ab34d97078817df7359c806179a8c3932e1293` — content
- `status-audio/_drafts/20260820T235839-hwao-report.txt` — `ced123258db9e2eb517c1cea8335ab743c5411256d9d6704a2dbe60405b9bf26` — content
- `status-audio/_drafts/20260820T235925-tori-report.deck.json` — `1caeef29733b84df1eac2ae02ae91d15f108967ad14be4e2ed54a798625d8f39` — content
- `status-audio/_drafts/20260820T235925-tori-report.mp3` — `693998040c0e1f72d9331a083b48f5509a7c4d269fcb1aaaf37f0589494566e6` — hash/metadata only; audio not transcribed
- `status-audio/_drafts/20260820T235925-tori-report.times.json` — `0575577109fa86270e12d89a03b2c76174fb77bb086347ccdd8e3a38ed398f63` — content
- `status-audio/_drafts/20260820T235925-tori-report.txt` — `e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e` — content
- `status-audio/_drafts/20260820T235940-hwao-report.deck.json` — `f82d7bf828dce0ce6e697f47d636bddd3db01745cc146afe6bd5b82c6990ce56` — content
- `status-audio/_drafts/20260820T235940-hwao-report.mp3` — `c4789881734e557c0a1c877a2ddeac6e42cdb261cb2cd60c5c2e82885ad8c6da` — hash/metadata only; audio not transcribed
- `status-audio/_drafts/20260820T235940-hwao-report.times.json` — `8c69e8075645312ab0a28183883b5aa9c5037cdb18755c158a6bcb4a78754716` — content
- `status-audio/_drafts/20260820T235940-hwao-report.txt` — `8666d0fa246e33bd2f8cd65aba20a60732c482f247b0abea7a303ce3bab028bd` — content
- `status-audio/align.log` — `7bd9b7a18303caa0283b86a73af18794577fa83f363fa63b8bea2bf06eff8f2b` — content
- `status-audio/archive-2.html` — `56b88cd95c311e7873b4ad9cfb9a2265231d97383391489b9d5e73e736ead294` — content (first-review bytes; later live hash above)
- `status-audio/archive-3.html` — `0ddd4df64cc83208cc0bdd1af390f3e9a9edb66720aa6435125ef4f09ef536a9` — content (first-review bytes; later live hash above)
- `status-audio/archive-4.html` — `24f82b0f9d7030565df169370a5eb82847630f4116b9f4924fc33d376ac58da2` — content (first-review bytes; later live hash above)
- `status-audio/archive-5.html` — `ca997cfda47a5638f1f66fe7846cee2bd2999ac46dee4c6c1dc1373b7a320cd7` — content (first-review bytes; later live hash above)
- `status-audio/archive.html` — `103f7d20094575c330be1ed9bbfe1b737223ea778b0c663afcbcfc8a9a3b7599` — content (first-review bytes; later live hash above)
- `status-audio/backfill.log` — `7b3e774f64e9a4c2a605114f1c24b059e3fece9f86d66923b95ca23adfd6f1bf` — content
- `status-audio/catchup.html` — `66e72073bd3ad28418767c4c80a0400e05852d58dd92e52aa4665cf70756dbfc` — content
- `status-audio/deck.html` — `76f835dbf73889b789c4913dcb584204c4794b9205d61145d307cbbdd0262e6f` — content
- `status-audio/graphics/cutgrid_6_3886.png` — `c960975a336f91caf959aba23cc11c0b98fd69cbfacc8f2644cbf7b5ccd50504` — pixels inspected
- `status-audio/graphics/cutgrid_6_640.png` — `5616e4e230ad85280fa7996fc2f880e2dbe7adf513c6aaec58442bc5595073a0` — pixels inspected
- `status-audio/graphics/cutgrid_6_716.png` — `dc1d97ba894aeb105263abadf81abc9bab9ee914ffc2ea5f5b08c4c73bcaacc0` — pixels inspected
- `status-audio/graphics/cutgrid_6_8424.png` — `4e7627bd7e71c7de8678e3771825a6c4a20718b1408af2f788697c02e378f9cf` — pixels inspected
- `status-audio/graphics/skymap_9404.png` — `7d46f607847e8abf8385ae2529d5770429c0e000f9da3d08252f5029eb25605a` — pixels inspected
- `status-audio/graphics/skymap_9412.png` — `c782ed52719a1c15ad2b16fc30f71ad5e9c24716aaea3cb1feb38a60a2e7812b` — pixels inspected
- `status-audio/index.log` — `7c8a3e826db682d029dbf1aaec630adafdb3cd52e7ca7a6d80dc5c876329cb57` — content
- `status-audio/latest.mp3` — `2a55b081db5861e57390c927e077ae98558dd666ec71d2f677e0f47bdf4d2ee3` — hash/metadata only; audio not transcribed
- `status-audio/latest.txt` — `c61fd95d8b413c79c103564a82808abcfdc382dd27fb8ae47e88fdb59f659b6f` — content
- `status-audio/latest_transcript.txt` — `1b7d622e8ef866752b1c9e82ae5d3edb97ebd85c0a9de18847801f32ea658940` — content
- `status-audio/listen.html` — `37f8c133b185993b79500490ca0835608cc33408224c4581430b62b56a479da6` — content
- `status-audio/nm_listen_daemon.sh` — `2e2dbf8e8b2a352000125fa33b6f69c1ed6c0debaed8dea1ff28e110b1b709b6` — content
- `status-audio/play-20260820T232407.html` — `21e214119aab56addbd769b1531f62525ef64359f59da027dc27a315b5f8a46d` — content
- `status-audio/play.html` — `ea0c83f472b18ecb74e7891ed6fe6560964928e054ef6e7cd62ea3405fef2526` — content
- `status-audio/played.jsonl` — `dcfcc4047d428b22ceb576155c9403cfaf6c749cf8a412eb7f563f8afc18acbb` — content
- `status-audio/postprocess.log` — `680161290c36039b269588e65529417ac3a7a8ce796f77749483889e43145219` — content
- `status-audio/queue.json` — `33bffde3766639a20d24bc849ddd170a6b4ae4f91590a8f90b94c2f02cdcaf7c` — content (first-review bytes; later live hash above)
- `status-audio/queue.seq` — `a4b2c5db15348c29451e18b8307e5ef81625ea638e807935f39ceaa8d9ac7758` — content
- `status-audio/report-20260820T230754-tori-report.html` — `8db823083a03eb9afbc20e12631a44665a4f8081eca6b6e4a23f18eed2db8913` — content
- `status-audio/report-20260820T231235-hwao-report.html` — `c5d5d5b81f5ae997e239203d2cd8e7e6c3065dc043069830ba138a29b9f6e9e7` — content
- `status-audio/report-20260820T231324-hwao-report.html` — `861e633683a49c70ca15d7d2a0e0e1fe21f7ea163111085cc13f4c03ebd82ad1` — content
- `status-audio/report-20260820T235925-tori-report.html` — `1ebde8a62d1393996e7bca9350e9c84aa2993a57cffd7b93a5b9ed358e04d256` — content
- `status-audio/report-20260821T004950-hwao-report.html` — `d4693eb627d5785354cfa0c27057f48508f24cb88697297941c5b51c01fbbb85` — content
- `status-audio/report-20260821T080428-blanc-report.html` — `18734d3fdd389a1e000ffed169652a61d1a6cdcd695b201d7798b236f296fb9d` — content
- `status-audio/report-20260821T105930-blanc-report.html` — `b832d6104df258bf8bed779d24229ce0ae49974f65e6026ce678e4a547f08b29` — content
- `status-audio/report-20260821T145923-hwao-report.html` — `7dcf8e2ba41917e28987cbaf3317766499b361310030133535b2bff29bdeca77` — content
- `status-audio/report-20260821T151249-hwao-report.html` — `f11078cce4e69efa4f59d37fd3681e18243cad80adce59571c99ca79588da0dd` — content
- `status-audio/report-20260821T151843-hwao-report.html` — `849829d266274149e6a9f1d4fb22200929cbd218b3adef291502fdc07074cb87` — content
- `status-audio/report-20260821T190931-tori-report.html` — `1071f27aee6325973e0b04664274568e8fdbbe4345f8576ee3f85b109421ca27` — content
- `status-audio/report-20260821T200910-tori-report.html` — `51216d69a089dd4240c5b75e9ea5f737e4faa4b4b140bb2c3f26a68ce9ac7a14` — content
- `status-audio/status.html` — `95e2c6e8faf5ce83e25317498998e5bef4eacb3a28b94f799905d274a0ae17aa` — content (first-review bytes; later live hash above)

## Hard-boundary and custody statement

No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, or read. No value was obtained from that tree and no statistic over its chi records was computed. The chi material inspected came only from already-rendered status-audio narration, deck, report/archive/page surfaces, on-machine drafts, published graphics, queue/playback metadata, and source code. Rendered audio was not transcribed; audio files were hash/metadata-only review.

No remedy is proposed. No target artifact, source, report surface, queue, archive, database, runtime, git state, or public file was changed. Writes were limited to the required final report and the permitted lane-local `_tmp_gate_final_audit.py` / `_tmp_gate_final_audit.json` evidence files.
