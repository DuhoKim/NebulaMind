REFUTED_CHI_CUSTODY_R6

# Adversarial gate — Chi Custody Receipt Revision 6 only

## Verdict

Revision 6 is **REFUTED as an accurate custody receipt**. Its central condition-1 conclusion survived this pass: I found no real-chi invocation of `handcheck/nm_handcheck.py`, no real-chi tertile artifact, and no evidence that condition 1 fired. But the receipt is still materially false and incomplete.

The sixth missed disclosure surface is the rendered MP3. Three independent local ASR runs of the exact 23:12 MP3 agree that it says the first three real values are `0.834336`, `0.384410`, and `-0.640352`, not the `0.27`, `0.20`, and `-0.20` encoded in the authored `.txt`/HTML surfaces. The generator expressly skips MP3s. A seventh missed surface is the still-unlisted YouTube video `4q9afgp3tzU`; its encoded frame at 01:45 visibly publishes `χ = 0.013161621987819672` and `raw bits 0x3c57a3d8`. Revision 1 knew this upload existed, but Revision 6 and its generator omit it.

Revision 6 also says the footprint Revision-3 hash is cited by five gates. Exact-hash search finds six. It says every output in `handcheck/` is dated 2026-08-15; thirteen retained output files are dated 2026-08-14 KST. Its detector still labels an unrelated `archive-2.html` “VALUE(words)” under the heading “CHI DISCLOSURES,” and its claimed detector-reversion history is not independently retained.

## Ranked findings

### 1. BLOCKING — rendered audio is the sixth missed surface, and it contradicts the receipt's authored-text disclosure record

The exact file is:

- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.mp3`
- SHA-256 `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`
- duration `70.704 s`

The generator skips every `.mp3` (`build_custody_tables.py:79-81` for drafts; root MP3s are never globbed at all) and calls authored `.txt` “narration” (`:69-71`). Those are not equivalent here.

Three independently loaded local Whisper models transcribed the encoded audio:

| model | pinned cached snapshot | transcription of 00:13–00:23 |
|---|---|---|
| faster-whisper base.en | local cached model used for the corpus ASR sweep | “The first three real values, `0.834336`, `0.384410`, and minus `0.640352`...” |
| faster-whisper small.en | `d1d751a5f8271d482d14ca55d9e2deeebbae577f` | same three decimals |
| faster-whisper medium | `08e178d48790749d25932bbc082711ddcfdfbc4f` | same three decimals |

The small.en word probabilities for the decimal tokens are `0.9699`, `0.9870`, and `0.9844`; medium gives `0.9511`, `0.9694`, and `0.9964`. The cross-check receipt is `_tmp_gate_r6_asr_crosscheck.json`, SHA-256 `6926e630df2c03edc89c24eed4f63970e34d4d3d614c017b15c76831682648a6`.

This is not an ASR-only coincidence. `20260820T231235-hwao-report.deck.json:53` preserves the same three six-decimal values in a rejected-slide note. The note says they were “not in the audio,” but `nm_deck_build.py:60-64` actually compares slide numbers to the authored transcript's number set, not to decoded audio. `nm_caption_norm.py:4-8` separately admits that the display copy can differ because “the audio already spoke whatever it spoke.”

The authored `.txt` and report HTML instead publish “zero point 27, zero point 20, and minus zero point 20.” Thus the current record contains two incompatible three-value disclosures:

- authored/display surfaces: `+0.27`, `+0.20`, `-0.20`;
- rendered MP3: `+0.834336`, `+0.384410`, `-0.640352`.

Without opening the protected chi tree, I cannot determine whether these are two representations of the same objects, different objects, or a transcript/audio mismatch. Default is HOLD on identity. What is independently established is that Revision 6's surface inventory and disclosure ledger omit the actual audio values.

This does **not** establish a real-chi tertile or condition-1 breach. It refutes custody completeness and strengthens the already-accepted condition-2/publication breach.

### 2. BLOCKING — the known unlisted YouTube publication is a seventh missed surface

`CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md:62-69` explicitly recorded the unlisted video `4q9afgp3tzU`. Revision 6 omits it even though the on-machine publication registry still records it:

- `/Users/duhokim/HermesOps/cockpit/videos/published.json:356-371`;
- title: “The night we started measuring — and why the achievement was not measuring”;
- state: `unlisted` on channel `NebulaMind`;
- registry source: the 00:49 report HTML, deck JSON, and MP3.

Direct current web extraction returned the video as Unlisted, uploaded 2026-08-21, length 02:35. I downloaded the current YouTube transcode read-only to a permitted gate temp:

- `_tmp_gate_r6_youtube.mp4` — SHA-256 `b87746997ae1d31bfc4659c5d66dba0c2ddffe0685042af7a29008241a05aa14`, duration `154.554 s`.

The encoded frame at 01:45 visibly reads:

- `object-395ad25aa…`
- `χ = 0.013161621987819672`
- `raw bits 0x3c57a3d8`
- hashes for weights, input tensor, code, and receipt.

Frame `_tmp_gate_r6_youtube_105.png` is SHA-256 `fbd67fd1632060593837054e3cb0a7328e38c12a788ebcb3930eb4ab7ebcf032`. The YouTube transcript does not speak the exact decimal; this is a visual-only disclosure, which is exactly why narration-only custody is insufficient.

The generator reaches neither the publication registry nor YouTube. Revision 6's statement that off-machine surfaces are “unreachable” (`:149-151`) is false for this named, locally registered, currently accessible upload.

### 3. MATERIAL — “cited by five” is wrong; the exact hash appears in six gates

Current footprint Revision-3 SHA-256 is `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`.

It appears in six gate artifacts, ten total occurrences:

1. `GATE_DECISION_MEMO_20260821.md` — 2;
2. `GATE_DECISION_MEMO_FINAL_20260821.md` — 2;
3. `GATE_DECISION_MEMO_R2_20260821.md` — 2;
4. `GATE_DECISION_MEMO_R3_20260821.md` — 1;
5. `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md` — 1;
6. `GATE_VOID_ON_DESIGN_DEFECT_20260821.md` — 2.

The generated table itself lists all six as citing `Rev3(current)` (`CHI_CUSTODY_RECEIPT_20260821.md:29-52`). The composed sentence immediately below says “Scanning all gates shows it cited by five” (`:116-118`). The correction therefore contains a new count error even while its qualitative correction (“not zero”) is right.

This count is stated at the target's audit boundary, before the required gate report existed. A post-write generator rerun necessarily adds `GATE_CHI_CUSTODY_R6_20260821.md` itself, whose evidence cites the hash, and changes stdout to SHA-256 `e213ebe35a54abebbc1eeb5f0605ae0fb19775c295b64510869f885884e9e686`. That self-referential drift does not rescue “five”; it shows why an unpinned `GATE_*.md` corpus cannot remain byte-stable while gates are added.

### 4. MATERIAL/HOLD — the ledger is observed append-only now, but historical completeness is not independently established

What held:

- The current generator joins `queue_ledger.jsonl`, not `queue.json` (`build_custody_tables.py:47-63`).
- At first review, queue and ledger had 37 matching publish rows over 32 distinct files; no `(seq,file,stamp_kst)` row existed in only one.
- During this gate, seq 40 was published. The old 43-line ledger bytes (17,409 bytes, SHA-256 `89746ce9ad7f3419bcb8937dccedb5bf65c7f299db162ac42e95b42df608dd3e`) remain the exact prefix of the new 44-line ledger (SHA-256 `b1474cbdf49e71673c7cd6be187d04aaaf515c3eb8e9b06251349a128e6dddf2`). This is direct observed append behavior.
- The active publisher opens the ledger with mode `a`, writes one line, flushes, and fsyncs (`/Users/duhokim/HermesOps/scripts/nm_audio_publish.py:41-48`), and appends before updating the rolling queue (`:200-206`).
- After seq 40, queue and ledger had 38 matching publish rows; the read-only admin audit reported 38 publish events over 33 files, five republications, two withdrawals, and zero in-window audio files not enumerated.

What does not close:

- The ledger opened post hoc after `queue.json` had already been mutated. Its first line says it was backfilled from the rolling queue.
- The two restored drafts use seq 37/38 even though their own `restored` notes say the original seq numbers are unrecoverable (`queue_ledger.jsonl:26-33`). This is a reconstructed identity, not an immutable contemporaneous publication receipt.
- The outside-pipeline duplicate is represented as both `event: publish` and `event: discovered` (`:24-25`), while `nm_queue_admin.py:96-101` says discovery is “NOT a claim” of publication. The implementation itself appends both events (`:136-145`).
- The generated table prints blank timestamps for `restored` and `withdraw` because it reads only `stamp_kst`; those events use `at_kst` (`build_custody_tables.py:58-61`).
- “Today the two agree only because 37 rows is under the window” (`CHI_CUSTODY...:105-109`) is causally incomplete: the deleted rows had to be reconstructed and the outside-pipeline file reconciled before the two current structures agreed.

Therefore current append behavior and current queue parity are verified. A complete, contemporaneous historical publication ledger before its opening is HOLD. The pasted ledger columns do match the ledger's publish rows, but they do not preserve all event timestamps or resolve the reconstructed-sequence problem.

### 5. MATERIAL — the handcheck date claim is false, although no real-chi tertile was found

The source claim about capability is correct and more extensive than the receipt's two cited lines:

- `_rank_tertiles` ranks values (`nm_handcheck.py:279-290`);
- the legacy prepare path builds two ranked tertiles and nine chi×size strata (`:333-351`);
- the HC-1H path computes real-population chi cutpoints and nine committee-state×chi-tertile strata (`:561-590`, `:702-706`);
- receipts record stratum populations and cutpoints (`:1016-1017`, `:1171-1172`).

The whole working-tree/handoff/HermesOps search found:

- only the synthetic rehearsal command files invoke the harness with a population path;
- `_rehearsal_20260820/hc1h_prepare.command.json:7-18` points both populations, roots, and passphrase into `_rehearsal_20260820/`;
- the real population rows are explicitly `data_class: synthetic` and use `synthetic-*` identities;
- no current or historical line combines `nm_handcheck`/`--real-population` with `chi_dr10_south`;
- the two commits touching the harness are `199c3168` and `0923db16`; a 9,275-line history extraction contains one `chi_dr10_south` occurrence, in the inference wrapper, and zero handcheck/path co-occurrences;
- no real-chi strata/tertile output was found outside the synthetic rehearsal.

Every retained handcheck output was inspected. Their receipts say `synthetic_only:true`, `population_is_synthetic_900_of_900:true`, or `real_data_accessed:false`; full-test logs are unit tests constructing synthetic fixtures, including negative tests that relabel synthetic rows `authorized_measurement` to test refusal/frozen-count behavior.

However, “every output in `handcheck/` is dated 2026-08-15” (`CHI_CUSTODY...:125-127`) is false. The eight active top-level outputs are dated 2026-08-15 KST, but thirteen retained outputs in `handcheck/superseded_hc1_20260815/` have mtimes from 2026-08-14 22:47–23:07 KST. The wording says every output, not only current top-level outputs.

The adjacent “no strata file exists outside the rehearsal directory” is also false literally: synthetic self-test receipts containing strata/stratum-population results live under `handcheck/`, outside `_rehearsal_20260820/`, and an unrelated `matched_control_by_strata_20260708T162615Z.csv` exists elsewhere in the repo. Neither is real chi. The defensible result is narrower: **no real-chi tertile or strata artifact was found**. Condition 1 is not established as breached.

### 6. MATERIAL — current detector catches the authored 23:12 text but remains unsound and incomplete

The required true-positive test holds for the `.txt`: current `detect()` returns `VALUE(words), SIGN, COUNT` on `20260820T231235-hwao-report.txt`.

The current function fails basic adversarial cases:

Under-matches:

- `CHI = 0.25`;
- `χ: 0.25`;
- `χ = −0.25` (Unicode minus);
- “the two chi signs are opposite”;
- “one clockwise and one counterclockwise”;
- “2,840 galaxies now have real chirality values”;
- `chi raw bits 0x3c57a3d8`.

Over-matches:

- “The photometric zero point is stable.” → `VALUE(words)`;
- “Three real values: latency, throughput, and cost.” → `VALUE(words)`;
- policy “one leaning positive ... one leaning negative” → `SIGN`;
- “Galaxies carry dust” → `COUNT`;
- “Galaxies were measured for redshift” → `COUNT`.

The actual `archive-2.html: VALUE(words)` row remains a false positive from unrelated pre-crossing “zero point” language; merely labelling the archive multi-reading/unattributable does not make the row a chi disclosure. The detector also cannot see the rendered-audio values in finding 1 because MP3 is outside its input set.

No retained alternative detector source or diff independently proves the composed history that a tightening was attempted, broke this true positive, and was reverted (`CHI_CUSTODY...:131-134`). The current true-positive behavior is verified; the claimed edit/revert history is HOLD.

## Attack 1 — correction-by-correction ruling

| Claimed correction | Ruling |
|---|---|
| Publications join `queue_ledger.jsonl`, not `queue.json` | **HOLDS in current generator.** Current row parity and one live append verified. Historical completeness remains HOLD; reconstructed seq/discovery semantics remain defective. |
| `_drafts/` scanned; two withdrawn reports carry counts only | **HOLDS at empirical-chi scope.** Both `.txt`, both deck JSONs, both timing files, and both MP3s were checked. They disclose a `2,771` chirality-measurement count and prohibitions/projections about future strata, but no empirical chi value or observed-sign result. “sign convention frozen” is design text, not a data-sign statement. |
| Revision-3 hash is cited, not uncited | **QUALITATIVE CORRECTION HOLDS; COUNT FAILS.** It is cited by six gates, not five. |
| Handcheck computes tertiles but has not been pointed at real chi | **NARROW CORE HOLDS.** No real invocation/output found. The universal/date/no-strata support sentences are false or overbroad. |
| Detector tightening was reverted; current detector catches 23:12 | **CURRENT TRUE POSITIVE HOLDS; HISTORY HOLD; QUALITY FAILS.** The detector is unsound/incomplete and rendered audio is not an input. |

## Attack 2 — complete surface matrix

| Possible disclosure surface | Generator reaches it? | Independent result |
|---|---:|---|
| Root authored narration `.txt` | Yes | Finds 23:12/23:13/count rows, but authored text is not the rendered audio. |
| Root deck `.json`, including embedded SVG | Yes | Finds existing deck disclosures; raw JSON includes headings, body, attrs, SVG, notes. |
| Root report HTML | Yes | Finds caption/deck disclosures, including escaped `\u03c7`. |
| Archive HTML pages | Yes | Multi-reading and time-unattributable; `archive-2` detector row is false positive. |
| `_drafts/*.txt` and `*.deck.json` | Yes | Two withdrawn Hwao reports carry counts only at empirical-chi scope. |
| `_drafts/*.mp3` | No | Independently transcribed; counts/prohibitions only, no empirical value/sign. |
| Root rendered MP3 | **No** | **Sixth missed surface.** 23:12 audio contains three six-decimal values different from `.txt`. |
| Per-report `*.times.json` | No | Checked all post-crossing files; timing mode, coverage, duration, sentence count, and end times only. |
| `latest.txt`, `latest_transcript.txt`, `latest.mp3` | No | Current aliases are clean Tori content; historical alias states are mutable and unreconstructible. |
| External PNG graphics referenced by decks | No | Four cutout grids contain pixels only. Two skymaps contain brick/parent-sample counts and sky-coordinate labels, no chi value/sign/raw bits/tertile. |
| `queue.json` / `queue_ledger.jsonl` | Ledger only | Publication metadata; current parity holds. They do not enumerate YouTube. |
| `played.jsonl` playback receipts | No | No value text, but proves seq 30 exemplar audio STARTED/COMPLETED on `Duhoui-MacBookPro-8`; remote playback is a distinct exposure surface. |
| `status.html`, `listen.html`, `play*.html`, `deck.html`, `catchup.html` | No | Shells fetch the already listed audio/text/deck/queue surfaces; no extra current value found. |
| Tailnet-served report URLs | Not as a public-surface class | Direct HTTPS downloads are byte-identical to local 23:12, 23:13, and 00:49 pages. |
| Active cockpit HTML/status/mobile | No | Exact-value/sign phrase search clean on all three active files. |
| Local/status video files | No | No local original DESI MP4 found under its registry filename. |
| YouTube/unlisted upload | **No** | **Seventh missed surface.** Current encoded frame visibly carries exact chi/raw bits. |
| Git history | No | Contains synthetic handcheck/rehearsal history and custody documents; no real handcheck invocation found. |
| Files on MacBook/Mac Pro | No | Named status-audio copies absent on both hosts; MacBook streamed seq 30 according to playback receipt. |
| Deleted/overwritten surfaces or unknown hosts | No | Not closeable from current evidence; HOLD. |

## Attack 3 — composed-sentence audit

| Composed claim | Ruling |
|---|---|
| Generator SHA-256 `aac8f...e6f0` | **HOLDS.** Recomputed exact. |
| Fenced table is generator output | **HOLDS.** Fresh stdout, saved table, and receipt fence are byte-identical, SHA-256 `8ab711dc12f4fce71d3b55bbbaad7d6e3870a03d01e53c087605c05a39cceba0`. A later clean seq-40 publication did not change output. |
| Revisions 1–5 retained byte-for-byte | **HOLDS against current hashes and predecessor pins.** |
| Defect 1 found by gate | **HOLDS.** `GATE_VOID_ON_DESIGN_DEFECT_20260821.md:8-10,132-151` found the three-value/sign disclosure. It found the authored-text values, not the different rendered-audio values now established. |
| Defect 2 found by gate | **HOLDS.** `GATE_DECISION_MEMO_20260821.md:15-27` opened the missed 23:12 file and rejected the fabrication accusation. |
| Defect 3 found by gate | **HOLDS.** `GATE_DECISION_MEMO_R2_20260821.md:30-63` found republications/count omissions. |
| Defect 4 found by gate | **HOLDS.** `GATE_DECISION_MEMO_R3_20260821.md:32-67,83-100` found structural coverage/attribution failures. |
| Defect 5 found by gate | **HOLDS.** `GATE_DECISION_MEMO_FINAL_20260821.md:24-52` found the hash-glob and handcheck capability failures. |
| Defect 6 found by Blanc | **HOLDS as attribution.** `PUBLICATION_LEDGER.md:1-42` describes the queue/ledger infrastructure and Blanc's own deleted rows. |
| “Six adversarial gates did not find” defect 6 | **HOLD.** No exact six-gate set is named; the receipt's own gate table includes eight heterogeneous gates. |
| Queue has `QUEUE_KEEP=50`; rows were deleted | **HOLDS** against active publisher source and Blanc's writeup. |
| Today queue/ledger agree only because 37 is under window | **FAILS as “only because.”** Restoration/reconciliation was also necessary; live state later became 38 rows. |
| Drafts were withdrawn at 00:15; publish→restored→withdraw lines exist | **HOLDS**, with reconstructed seq and blank generated timestamps noted above. |
| Revision-3 hash cited by five | **FALSE: six.** |
| `_rank_tertiles` line 279; `chi_tertiles` line 344; nine strata | **HOLDS** for the legacy path; HC-1H also computes real-population cutpoints/strata at later lines. |
| Every handcheck output dated 2026-08-15 | **FALSE.** Thirteen retained outputs are dated 2026-08-14 KST. |
| Every handcheck output is synthetic self-test | **HOLDS on inspected output evidence.** Empty logs inherit only their paired run context; no real path/identity appears. |
| No strata file outside rehearsal | **FALSE literally; HOLDS only after adding “real-chi.”** |
| No aggregate over real chi has been computed | **No counterexample found; HOLD as a universal.** Whole-tree/current-history evidence supports it, but absence outside inspected sources cannot be proven. |
| Only program that could compute one has never received real path | **Overbroad/HOLD.** No real invocation of this harness was found; “only program that could” is not established. |
| Archive pages cannot be report-attributed | **HOLDS.** They concatenate readings. |
| Detector edit broke a true positive and was reverted | **HOLD on history.** Current true positive verified; no retained failed version. |
| K-8 condition-2 quotation | **HOLDS.** `K8_CROSSING_AUTHORIZATION_20260820.md:32-33`. |
| Authorization text was Duho's “freeze it and authorize the crossing” at 22:20 | **HOLDS against K-8 record** (`:1-4,58-59`). Speaker authenticity outside that record is not independently re-proved. |
| Breach at 23:12, 52 minutes later | **HOLDS at source precision.** 22:20:00 representation to 23:12:51 is 52m51s; authorization has minute precision only. |
| Seq 20/21/22 and their timestamps | **HOLDS** in ledger. |
| R2 gate ruled complete three-value publication an aggregation | **HOLDS.** `GATE_DECISION_MEMO_R2_20260821.md:11,71-80`. |
| Three values of 208,407; no positions/axis relation | **HOLDS for authored 23:12 disclosure.** Rendered audio adds different values but no positions/axis relation. |
| “Nothing that can move a stratum boundary” | **HOLD as causal/materiality inference.** No computed boundary was found, but the absolute inability claim is not proven by publication content. |
| No protected-tree read by generator | **HOLDS from generator source.** |
| No chi statistic computed in producing receipt | **HOLDS for generator execution; HOLD for all human composition history.** |
| Off-machine surface unreachable | **FALSE for named YouTube URL and Tailnet status host.** |
| “Absence ... only claim never corrected” | **Not verifiable as an exhaustive history claim.** |

## Failed attacks / facts that held

- Fresh generator stdout exactly matches both the receipt fence and `tables_20260821.txt`.
- Generator hash is correct.
- Current ledger join really uses `queue_ledger.jsonl`.
- Queue and ledger publish rows matched at 37 rows and again after a live append at 38 rows.
- The old ledger bytes remained an exact prefix after seq 40 was appended.
- The two withdrawn Hwao draft narrations, decks, timing files, and MP3s carry measurement counts but no empirical chi value or observed-sign result.
- Current detector fires on the authored 23:12 text.
- Exact footprint Revision-3 hash is cited, not uncited.
- No real-chi handcheck invocation, tertile output, cutpoint output, or strata artifact was found in current files or relevant git history.
- All inspected handcheck receipts/runs are synthetic or refusal tests built from synthetic fixtures.
- Condition 2 attribution, 52-minute interval, seq numbers, and R2 aggregation ruling hold.
- All six referenced PNG graphics were independently pixel-inspected; no chi value/sign/raw bits/tertile was found.
- Post-crossing timing JSON files contain timing metadata only.
- Active cockpit surfaces contain no target value/sign phrases.
- The seq-40 report published during this gate is chi-clean and leaves generator stdout byte-identical.

## Handcheck-output date and SHA ledger

| Output | mtime KST | SHA-256 | Synthetic evidence |
|---|---|---|---|
| `hc1h_full_test_stderr.log` | 2026-08-15 02:56:31 | `9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8` | unit tests; authorized labels are refusal/contract tests over generated fixtures |
| `hc1h_full_test_stdout.log` | 2026-08-15 02:56:25 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty paired stdout |
| `hc1h_independent_stderr.log` | 2026-08-15 02:56:39 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty paired stderr |
| `hc1h_independent_stdout.log` | 2026-08-15 02:56:40 | `51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb` | paired with independent synthetic receipt |
| `hc1h_independent_verification.json` | 2026-08-15 11:19:20 | `19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8` | `selftest-synthetic-only`; no real access |
| `hc1h_selftest_stderr.log` | 2026-08-15 02:56:31 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty paired stderr |
| `hc1h_selftest_stdout.log` | 2026-08-15 02:56:39 | `a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b` | synthetic self-test |
| `hc1h_synthetic_selftest_receipt.json` | 2026-08-15 11:19:28 | `25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40` | `synthetic_only:true` |
| `superseded.../attempt1_synthetic_selftest_stderr.log` | 2026-08-14 22:47:32 | `ebe607be44c62c552a845f0cbdbdb5986fa5c7c0d53eff9bddd575a5c37ae4a5` | synthetic script path |
| `superseded.../attempt1_synthetic_selftest_stdout.log` | 2026-08-14 22:47:28 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty paired stdout |
| `superseded.../full_test_stderr.log` | 2026-08-14 23:07:55 | `148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b` | synthetic unit tests |
| `superseded.../full_test_stdout.log` | 2026-08-14 23:07:53 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty paired stdout |
| `superseded.../independent_stderr.log` | 2026-08-14 23:07:36 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty paired stderr |
| `superseded.../independent_stdout.log` | 2026-08-14 23:07:36 | `b4f51b589170659f0be7c6e38d93c81e35b13a13e4813ede6949e9bf4a2de63` | paired with synthetic verification |
| `superseded.../independent_verification.json` | 2026-08-14 23:07:36 | `54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae` | `real_data_accessed:false` |
| `superseded.../pre_review_synthetic_selftest_receipt.json` | 2026-08-14 22:48:04 | `9056ef22c89ea8e4606610948ac7b32b959c97ec42d3ea2597bdc4e71bb67ce7` | synthetic receipt |
| `superseded.../pre_review_synthetic_selftest_stderr.log` | 2026-08-14 22:48:01 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty paired stderr |
| `superseded.../pre_review_synthetic_selftest_stdout.log` | 2026-08-14 22:48:04 | `29a592d8ed9c9c571ff96195e1313815a7cb3ece824fb67e9ae2d539779a1b1e` | synthetic self-test |
| `superseded.../synthetic_selftest_receipt.json` | 2026-08-14 23:07:04 | `1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8` | 900 generated synthetic images; zero real |
| `superseded.../synthetic_selftest_stderr.log` | 2026-08-14 23:07:01 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty paired stderr |
| `superseded.../synthetic_selftest_stdout.log` | 2026-08-14 23:07:04 | `e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab` | synthetic self-test |

## SHA-256 evidence ledger — every reviewed task artifact

The appendix records first-review bytes for live files; where a live file later changed, both first-review and later hashes are named above or below. Search corpora were names/content searched; every matched or independently opened artifact is included.

The lane-local source used to insert this appendix, `_tmp_gate_r6_hash_appendix.md`, is SHA-256 `647796d698d11c295c4a5b7f055b3250b722b336db294fd190da428ae2e53231` (87,667 bytes). It is not listed inside itself.

### Complete artifact hash list

- `/Users/duhokim/HermesOps/cockpit/live-steering-cockpit.html` — `3f57c2700a1d5069761b5f588ece67c1943d601ff183b456937de14743af7e2a` — 54401 bytes — later/current review
- `/Users/duhokim/HermesOps/cockpit/live-steering-status.json` — `f5c88f6b6ded3c59633a84305bb71100a2b3ca41ea1a37a91cb6a96a1258a93a` — 115651 bytes — later/current review
- `/Users/duhokim/HermesOps/cockpit/mobile.html` — `14c58b239aadb771449c728fe2986004bd59a8b36efa0bb7b22ca61501589b22` — 7899 bytes — later/current review
- `/Users/duhokim/HermesOps/cockpit/videos/published.json` — `99298e3883044ceb61d50ab0e8610ee3077aec9f9dfac32c965242c729414098` — 25589 bytes — later/current review
- `/Users/duhokim/HermesOps/reports/status-audio/.durations.json` — `3dc7491ff2d9d2b42276bb64b05e221d22c7f9b4a97042468c5ed06a149b1a65` — 11040 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.deck.json` — `d84bf963ce608387298041262614314c1cb7fa4608666178c4ed341a10677928` — 1585 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.mp3` — `27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0` — 616320 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.times.json` — `5fcf940bc7346ddb1854c5afd3f4870b8d1396b1a733b6062df6db690d768c4e` — 116 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.txt` — `7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47` — 577 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.deck.json` — `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c` — 2543 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.mp3` — `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168` — 1131264 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.times.json` — `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79` — 163 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt` — `7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad` — 1055 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.deck.json` — `855da9448492112c0529476cf451466934c63474068419cb3382009bfb9108ab` — 3292 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.mp3` — `785aed20de80d27118f915d7a05b02daac1520fc52e919231bd1f575bea0a1ad` — 1272192 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.times.json` — `6b0b7294e93b2d5a6df7a7dc9698691b5c9dea180f2958a2c01804e21647cc4a` — 159 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.txt` — `5ba48ea353bb94a3a5740c4be8160e552e996670287f124fb66b69d5cf781842` — 1131 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T232407-20260820T230754-tori-report.mp3` — `27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0` — 616320 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T232407-20260820T230754-tori-report.times.json` — `5fcf940bc7346ddb1854c5afd3f4870b8d1396b1a733b6062df6db690d768c4e` — 116 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T232407-20260820T230754-tori-report.txt` — `7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47` — 577 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.deck.json` — `1af45a7e0cb275f3a3605aa3f3b68e78f899421939306ebac45f8448b66a1f12` — 12914 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.mp3` — `693998040c0e1f72d9331a083b48f5509a7c4d269fcb1aaaf37f0589494566e6` — 1861632 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.times.json` — `0575577109fa86270e12d89a03b2c76174fb77bb086347ccdd8e3a38ed398f63` — 214 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.txt` — `e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e` — 1853 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.deck.json` — `c49c71978ee27eedab93076906a27f188eee3b4b905caed13b674127feab091b` — 10840 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.mp3` — `b730dfc2b28b05835f548f0aedc1096c7e51e2067a087091b1448384a4092ed2` — 2472192 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.times.json` — `5c50db87a9e6389755f159501d3754c97233121bdd496f837c5fd3c7fa522f60` — 254 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.txt` — `f1096d51b237dbeaddf92b034194ed9f23d89401b54bb26335b74d1ead81b258` — 2562 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.deck.json` — `81e12c9a380d2f8a5bb65f2b81d45a0da8dc2877cf8dd22f9bb1dc5da504a3cb` — 2112 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.mp3` — `264d8731fdf523ac588b13aed142b0f3d4283ba00fd7f8a41b586fd55430c91f` — 652032 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.times.json` — `cba21eae867fdbb9b68307a41cb0d6bbbeaef927fec6fcdab0b12383d10ee752` — 133 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.txt` — `452f13b624ff952df0987b7f54feccc632fde6c0f2eb569c365fa92ab968a982` — 627 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.deck.json` — `88394b89139669d66bef04ea85c62f591490f11ef767b5f14421784b2a54f131` — 712 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.mp3` — `5492a78d89d136e0a9b497da8781e28d33a190e34f286e55454a6c78172a55c6` — 86400 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.times.json` — `37a1d3c6938c2decd29ba6d798ecc9370e8323ad60437af3ce1713f0a6dd5741` — 82 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.txt` — `ada74c9a1761ba02f9f0c0fb6c31a3415d4fc80a2619a8776905101d1e146951` — 67 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.deck.json` — `8b3ddead69fb6764df63a35352eca9332b52b9472d4626a6e5e05430f20b4ad1` — 4340 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.mp3` — `21de44c997065b03c8ac4460217f863904e5ba085c110f5cbe38cbb1eea92d00` — 2921856 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.times.json` — `729f892f96a5c2e37597bf3184a3274b32e9e552d9bd8f61ceb9e447a4d75f7b` — 333 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.txt` — `c3aefdeea36b45e60f63e297bfed77358fda8db3d63560c245386b3d20cba8b2` — 2991 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.deck.json` — `0fe5ecac190cfcb490cdcc42aa52b1069e7bf2a3b97d996d3faf13ae0030b8cc` — 2997 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.mp3` — `f468c515b5d852d82d08da0c5a41ee04cd75e7d70139ae9633d77a0e611df53a` — 1776768 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.times.json` — `80bcaeddd92bf9e348e10efb257afff179a389e8bfe33187327c1037a21c4cbb` — 261 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.txt` — `5648a55e23f6fddfdd9d215c1c64ea8eaf83c6a51fdec991a5f67ba31dc6e37b` — 1818 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.deck.json` — `6437b0993110b9dca73b811017a0ba49803faa255a413cb89a2ad1c754a691ad` — 3604 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.mp3` — `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3` — 2596992 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.times.json` — `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848` — 390 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.txt` — `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c` — 2702 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.deck.json` — `ec91f2ed3499f2bb2d291154b9a18c43b00841082853ac46c31f57a97d192998` — 2299 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.mp3` — `a897ce35c324e6d356350b728f6b16e7398581501718d1991ef72bb4c54fc999` — 1083264 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.times.json` — `8d0285545d13b7aeeadbbab1bddd8c33a59093ae2475eb7bb8ff36d42fe5a618` — 175 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.txt` — `c42bc1d4500a8e0db4411715c1237da0ebf9a39d9d88eb1fa7d633367281770b` — 1163 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.deck.json` — `f208eaab7cec9040fa0063bb9f722aab36046ffbae4c49216fb8dc305def1d55` — 2546 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.mp3` — `2a55b081db5861e57390c927e077ae98558dd666ec71d2f677e0f47bdf4d2ee3` — 1248768 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.times.json` — `899d1c3f7cf9c5996edff78876aded729aa233a76a91ca0ed08a84f92b2d558c` — 187 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.txt` — `1b7d622e8ef866752b1c9e82ae5d3edb97ebd85c0a9de18847801f32ea658940` — 1335 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.deck.json` — `83988126c6ef8c6fef4bb696c345fc03c833620158bad0496aa19fa300cdad23` — 1442 bytes — later/current review
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.mp3` — `97065f66cdffade0081f5350b4ac702998fc42193608bc711c4a58f7209cf6c5` — 1328256 bytes — later/current review
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.times.json` — `3f20ae30e68e43bc0238d5c177f9b4bfd64573cb32375646daf5d77bfe6ca50c` — 208 bytes — later/current review
- `/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.txt` — `6e35f60af1cefff0f8d03dfb5bdc6c22e99f9be81e4961493b59f23cbee86556` — 1324 bytes — later/current review
- `/Users/duhokim/HermesOps/reports/status-audio/_caption_backup_20260820/status-20260810T1049.txt` — `3d5f884fcbfd568b0bf15a1916b34bbbc7fc1cc0b8038872f084f39bb494c640` — 668 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.deck.json` — `abbcc68d5b715a85f78a0b920882c2af03319810ad46ba1b3ddb579f7ae3ea3c` — 10398 bytes — first review: content
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.mp3` — `245d5c815cbda18a43f11eb0da2fee885882b1d74f2b29770873d301b17d5eb8` — 2019456 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.times.json` — `b92fd0a3b628c99c010519ee58ab34d97078817df7359c806179a8c3932e1293` — 217 bytes — first review: content
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.txt` — `ced123258db9e2eb517c1cea8335ab743c5411256d9d6704a2dbe60405b9bf26` — 1974 bytes — first review: content
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.deck.json` — `1caeef29733b84df1eac2ae02ae91d15f108967ad14be4e2ed54a798625d8f39` — 3516 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.mp3` — `693998040c0e1f72d9331a083b48f5509a7c4d269fcb1aaaf37f0589494566e6` — 1861632 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.times.json` — `0575577109fa86270e12d89a03b2c76174fb77bb086347ccdd8e3a38ed398f63` — 214 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.txt` — `e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e` — 1853 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.deck.json` — `f82d7bf828dce0ce6e697f47d636bddd3db01745cc146afe6bd5b82c6990ce56` — 11692 bytes — first review: content
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.mp3` — `c4789881734e557c0a1c877a2ddeac6e42cdb261cb2cd60c5c2e82885ad8c6da` — 1944960 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.times.json` — `8c69e8075645312ab0a28183883b5aa9c5037cdb18755c158a6bcb4a78754716` — 217 bytes — first review: content
- `/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.txt` — `8666d0fa246e33bd2f8cd65aba20a60732c482f247b0abea7a303ce3bab028bd` — 2002 bytes — first review: content
- `/Users/duhokim/HermesOps/reports/status-audio/_tests/latest.mp3` — `ff909af1fe5333dcac65d12ebf3cbf5a1af77b6d52e749d9d0c0811c66c7de8b` — 104832 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_tests/latest.txt` — `e2ccd7695fa21f3879a793175f7e8702c585bd2d986fc943e02475e229c834d7` — 57 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_tests/latest.txt.bak` — `1aa7167a756b25c059e7c65d5f37182eb42085fa0f85fa297c268e30f468973e` — 48 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/_tests/latest_transcript.txt` — `cca3f690d58c1229c9dbd04d57fabd4b223bff19b41aa3c29a4dff1551854e2a` — 1285 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/align.log` — `7bd9b7a18303caa0283b86a73af18794577fa83f363fa63b8bea2bf06eff8f2b` — 3660 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/approval-frame-20260810T1740.asr.json` — `353ff4e269becd7dea9390b2e45fd949b5224fffff901ccb30ce2a9cbf2a6692` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/approval-frame-20260810T1740.mp3` — `0776f8051ebab2afe887d20f176aeb92191555fa27f95411862550fe8f02b1f7` — 2636160 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/approval-frame-20260810T1740.txt` — `efac6d1ea790b9ec2351c15639523245042d9ffd8e3b12c02cc52b5c59542e41` — 2627 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/archive-2.html` — `2ffca8642ef0ff81094ef00264fc15e4d050e6bff3996aa70a545a9708e2bba6` — 97177 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/archive-3.html` — `12486d3c6f65433309cc192a8db473ef6173afe94c7172d0bfd9ee8f6df7c3e0` — 159359 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/archive-4.html` — `a6fa6819316cf0826a42e5808851bc74a137c71eaf5bda7d71e2c90760004fec` — 210170 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/archive-5.html` — `e9851841ba3df6a084d62354fbd07083d6652a4469b1dbbe31f5c3726b8b4c99` — 83216 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/archive.html` — `b994449a1c1a247462faa949db45cf20d060d334910ccc5ed3f1a7edc37afa53` — 204231 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/autoread-20260811T1100.asr.json` — `863d7a264e3b58dce059b8a37e82b4885954b4d01a5616b0c4eb69434413b191` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/autoread-20260811T1100.mp3` — `7201f7c5d268b8d470e7b6cb2d5893f59e7a3d2ed8dbf33ed1681c41704fc430` — 1895424 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/autoread-20260811T1100.txt` — `a4b9aae3745289954320ef9d3266af3ab0362e10c105d2bc0e5a2aa62d198fad` — 1946 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/backfill.log` — `7b3e774f64e9a4c2a605114f1c24b059e3fece9f86d66923b95ca23adfd6f1bf` — 677 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/catchup.html` — `66e72073bd3ad28418767c4c80a0400e05852d58dd92e52aa4665cf70756dbfc` — 2935 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/cleannote-20260811T1432.asr.json` — `f16a30d5bbf000adb6d4c2416bbe585c67949ef18a3259771d8ed64c8b96a094` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/cleannote-20260811T1432.mp3` — `6da95fa93ccbe24002806998eab1e9ea4ec763e3ba3d58dc4c5849519cc92ee6` — 1355520 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/cleannote-20260811T1432.txt` — `ed2372b737de1e5bbb6a907988bafa31f0da4a9314be20c88cc9b8b4d3ca9d5d` — 1445 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/closespin-20260810T2208.asr.json` — `ad222cba7e4d31c820f31cf4c1c0a5dfca821847ae31c10bb13eb57a2470a3d9` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/closespin-20260810T2208.mp3` — `5c8558f1de38e3d2b160e9fab2f8cf08adddc32302a5ca16f571ba9e7a3dce25` — 2343168 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/closespin-20260810T2208.txt` — `f82df2942cc144b0d39bc1e120ea501a25741e91f2d54dee91a058c95e38c4d9` — 2433 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/dec2-armed-20260810T1822.asr.json` — `1e2c3d7d15bc19243c6478561941583170622370f86a16e18aacc69fd2c7c24d` — 172 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/dec2-armed-20260810T1822.mp3` — `d28569ed9bb2e0f15721913996695bdbd4d82e81aa4d932e8e2f78a35f62cd02` — 1382400 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/dec2-armed-20260810T1822.txt` — `00ad3628728a1bd9bcfea82b0f571d03fb6ac85791f70f4af2d72111e7215dfe` — 1378 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/deck.html` — `76f835dbf73889b789c4913dcb584204c4794b9205d61145d307cbbdd0262e6f` — 4936 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/dispatch-20260810T1716.asr.json` — `9570519c935656a5bbe21fdebc33b676d3de5eeb2c74214eb6078a93ed802f94` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/dispatch-20260810T1716.mp3` — `07aa07fbf7f4dc8c2c35edf8d8712dfe95609e52392191655e337d9742ad330b` — 1879296 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/dispatch-20260810T1716.txt` — `189531b0232d52c69e346fa64a9affaf40e7627a15672c973f36e613c4c632ba` — 1802 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/framescope-20260810T1436.asr.json` — `489e9a6d0dea88155670eeb8d9dc624575decb342adafe348b3cb3d1057b8191` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/framescope-20260810T1436.mp3` — `bb3ca29568f7891fde28f11c034cd370282733964cdb83b6b9a855c5b87aeb5a` — 1963392 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/framescope-20260810T1436.txt` — `eb91acbd6b3bfc462a1774b30edfe0ef2094862f93118c13bd8acbb9804406e3` — 2038 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/freshlabel-20260810T2158.asr.json` — `cda7ff8ad8a94aeea2867a09a596219b2930df0eccecbc7f3fab9fb5b17efe31` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/freshlabel-20260810T2158.mp3` — `7f5506aa06b7e935557c03428c8c1dc46c85d897f70c77a72c76099c73fcd102` — 2305920 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/freshlabel-20260810T2158.txt` — `9b1aab1eedc96b348f94cb78670a004024d5cb0a1d8f4040be5afba0547eae94` — 2318 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/gate-block-20260810T2145.asr.json` — `eea20ad1b027ddf174c871d08fdbb1f8d7de6ad4bb718b111fff90242cfdcea5` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/gate-block-20260810T2145.mp3` — `fe55a3a744d00ca11983d0626eeebd323d760aa05905bb231d16e3169314b528` — 2123520 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/gate-block-20260810T2145.txt` — `33df410cc44b76b96eb840e8a0b4ed5fb5b7503aad5f35e87b64c0de341d2383` — 2117 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/cutgrid_12_6242.png` — `6f0c8e44e968af17818efd001a99b8960fa149689e915d5a9e0ab57888b46af7` — 151783 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/cutgrid_12_7939.png` — `0ceaece29686afc983a5330bd62cf03699a418df7c954a85dc789b3100e66b89` — 160328 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/cutgrid_12_9852.png` — `7e8916020c28463f94d587d5018fa7b63931595c8b2ebfe5274bfeecc5c57838` — 134805 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/cutgrid_6_3886.png` — `c960975a336f91caf959aba23cc11c0b98fd69cbfacc8f2644cbf7b5ccd50504` — 54984 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/cutgrid_6_640.png` — `5616e4e230ad85280fa7996fc2f880e2dbe7adf513c6aaec58442bc5595073a0` — 70342 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/cutgrid_6_716.png` — `dc1d97ba894aeb105263abadf81abc9bab9ee914ffc2ea5f5b08c4c73bcaacc0` — 74296 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/cutgrid_6_8424.png` — `4e7627bd7e71c7de8678e3771825a6c4a20718b1408af2f788697c02e378f9cf` — 76903 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/skymap_9088.png` — `9e1d421e0e7aa6d891d2b4858f844b46abd9a20a6201b78b82a55a52f73189c5` — 103757 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/skymap_9093.png` — `587d91e1ae71a6527062978a2d811e2ba7631de56afed9badb831eb6885498bd` — 110006 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/skymap_9153.png` — `88a69745d08c70cabdfe21e036d5b04f517791cf3278dfcdb53acac861582dc9` — 113591 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/skymap_9404.png` — `7d46f607847e8abf8385ae2529d5770429c0e000f9da3d08252f5029eb25605a` — 113007 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/graphics/skymap_9412.png` — `c782ed52719a1c15ad2b16fc30f71ad5e9c24716aaea3cb1feb38a60a2e7812b` — 112986 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/index.log` — `7c8a3e826db682d029dbf1aaec630adafdb3cd52e7ca7a6d80dc5c876329cb57` — 826 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunblock-20260811T1330.asr.json` — `3acea78bff0ea41a048c76d2261c77c24c073fb169333d04eeb9f9cce3f706e4` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunblock-20260811T1330.mp3` — `9eac05d4b1fc131d98c04a8dcca49c8b79850630a5a4103c1c19bbc6cd038d2e` — 1921920 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunblock-20260811T1330.txt` — `ecae4c909cfb151b2debd77545e144bddd971d0e911f911b7714c0173332834e` — 2063 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kungate-20260811T1330.asr.json` — `a50ba46f9df1382f99f8fa666df72a472f676dae26b3df014d7ffe3e742cf026` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kungate-20260811T1330.mp3` — `00ba01a39c2e5bb394971a0d9b4b08ffd89f56b6408d18fd378136d90695219f` — 1626624 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kungate-20260811T1330.txt` — `9c4648c0d64b80c86ffabf745648995933fb48263e04d539de2ff54363f3184f` — 1655 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunpass-20260811T1425.asr.json` — `94a5a9277c127c63a4bc49141c91b03d67618f53e9bec3d0c95c5b0eda2e784b` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunpass-20260811T1425.mp3` — `e6e6e6eb1c46a4de351bbaede4beb87976234b5a074e3afac78c8edcfa0a4c2e` — 2023296 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunpass-20260811T1425.txt` — `8e751329b202f041e36e48a410aa1fb28bd45dce9d904a0bfee0ad0697ced43d` — 2056 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunverdict-20260811T1345.asr.json` — `52c9cb0195db3738393dd3a76074c905a64c1b95b7867a529aa6ddb3cd5401df` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunverdict-20260811T1345.mp3` — `613b63d5f73dcfed1a763a9a4098e5594c44465062a4c264bb4a5a803f110f33` — 1696128 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/kunverdict-20260811T1345.txt` — `85834b101b791dce5c85f67f205bbfeec6c981f8e347792678b30d3c6a7c26c3` — 1724 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/lanaunblocked-20260811T1422.asr.json` — `997e42ad115ac31d73ee5caa39f6f1c605b17c32fd47b4ebfd466455d5606d42` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/lanaunblocked-20260811T1422.mp3` — `215ade284632acffebfa3c9477019f7ccb2816db8ae26abd701137934e735f1f` — 1235328 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/lanaunblocked-20260811T1422.txt` — `1c30910587b4a00e9e161c1a6a693c45bb4e5341dbfeec4b95dbd9a684dada98` — 1293 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/latest.mp3` — `2a55b081db5861e57390c927e077ae98558dd666ec71d2f677e0f47bdf4d2ee3` — 1248768 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/latest.txt` — `c61fd95d8b413c79c103564a82808abcfdc382dd27fb8ae47e88fdb59f659b6f` — 57 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/latest_transcript.txt` — `1b7d622e8ef866752b1c9e82ae5d3edb97ebd85c0a9de18847801f32ea658940` — 1335 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/listen.html` — `37f8c133b185993b79500490ca0835608cc33408224c4581430b62b56a479da6` — 312 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/loosen-20260811T1105.asr.json` — `82078c8b6b865c65aa37fa21abfd749bb51ee92295783cadb9639211a4a6c4c7` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/loosen-20260811T1105.mp3` — `d3504fab7a602fd9b55677b2b7c10f094ecc9a123f3b6ab612a0d0ea1e81469e` — 2577792 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/loosen-20260811T1105.txt` — `011c1b261c16ffb6ff6958b409ceb1d4c11463aee8c9197696d8ad43c9103006` — 2657 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/methodsnote-20260811T1325.asr.json` — `9421e2c04df10da2310e4c80885240188d0775282d35142cc4496df6678461d2` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/methodsnote-20260811T1325.mp3` — `cb3cc4cd540e6173ecef5d9ba24226c0e14281b6359a8d13a3e9224d545487bc` — 2639232 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/methodsnote-20260811T1325.txt` — `36569b18a5991ad336a447de9f6c63ac2917a00375ee0a23fd81d40512e19303` — 2874 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/moonshot-current-20260810T1758.asr.json` — `ce4f3f65956dbffb43b7489c9d52c7d0a06a51159d7a9b2f8598a0393e489912` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/moonshot-current-20260810T1758.mp3` — `b31103951e76bf6cac1e9313e3d802c0a7b3868c92741db6504faa1cd167bdbe` — 1909632 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/moonshot-current-20260810T1758.txt` — `6083e733badd9df8b9b749c2c29474c8254becf6544874aaf5e2f6168abfb1ea` — 1922 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/morning-20260811T0837.asr.json` — `7166dc3ff0515c57825baed1380d29e630b9e48c1695186a84bf7d50512e640d` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/morning-20260811T0837.mp3` — `fe96ace17d9a6fadf42cc7a5c8f1ffe13760f3064a0744e0d8e1f4cf243fb0e5` — 3383424 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/morning-20260811T0837.txt` — `f123e7e6671a6a679ed0257338e474047d1582d877c20efbf908303868a094eb` — 3621 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/net.nebulamind.status-listener.plist` — `03b70e931f4a60fc74a587d4ad6d1f1d9d7cf86755a5a8f212b88e847cd26dfd` — 457 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/nm_listen_daemon.sh` — `2e2dbf8e8b2a352000125fa33b6f69c1ed6c0debaed8dea1ff28e110b1b709b6` — 3237 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/note-20260811T1315.asr.json` — `29e8f615614c1d6198c7f8ec16c902c4130bb20616dc865985fe20615521766d` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/note-20260811T1315.mp3` — `4a6df9edd73943a219d80d087d915a9afa710e6566a481137ae3034a39e60a44` — 2065920 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/note-20260811T1315.txt` — `3c078c2c2be100267ee5c613e4eec0669b125ba98b91da6c5b3f1c28b92580f8` — 2175 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/notewatch-20260811T1320.asr.json` — `24d2b057030f3d7a777fc7679cefa7f6ab053482bc4130d78c0f7eff18dd3e8b` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/notewatch-20260811T1320.mp3` — `2c01e69f73725ea87964a010a7de433801288a943e6870d9065414e0e274a8b0` — 966528 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/notewatch-20260811T1320.txt` — `078cd6888a7d42654f46eec8ae87ba39dd636eabfb7296ee9a224a2d74361a0a` — 948 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/novelty-20260811T1100.asr.json` — `7bee4baef94e6242907f23b431c1a183a0044216eee296f9f7907a53300efe14` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/novelty-20260811T1100.mp3` — `a6fe4b65e62ac1c45e6b2efdc6273bbac8a2560339c23e13ac6a530f647567de` — 3150720 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/novelty-20260811T1100.txt` — `61cf5964196a0318f2a12598fd3fa79e109e51771180310d521e1407d817b6bf` — 3250 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/pathc-20260810T2152.asr.json` — `254674d27f0820d51ed61256260b7bff813d2b6c3ecc1acfa8e09e0e0c2da621` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/pathc-20260810T2152.mp3` — `5e2ab4dcaee5565fff4f8bb15d39dd48b104c156608600efe00e5c6302802e76` — 2755968 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/pathc-20260810T2152.txt` — `d1132b62da543a29ec0c731787c5d5e58a06d22843769c2ce7caf86a12004df7` — 2900 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/plan-20260810T1710.asr.json` — `609ebbccc756a7dff0b93b5f5cf6e2832baa2b6a77d45e04f9cfb19219ed0fe1` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/plan-20260810T1710.mp3` — `792e501fb57fb89ef8c2c34389f17d85e7ca54f397a7dfd2abb9386e26302565` — 2509824 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/plan-20260810T1710.txt` — `23f5639fa1c1746ab48983476b22a754d0c729679530558b9d7e1d3f24b317cd` — 2480 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/play-20260820T232407.html` — `21e214119aab56addbd769b1531f62525ef64359f59da027dc27a315b5f8a46d` — 4197 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/play.html` — `ea0c83f472b18ecb74e7891ed6fe6560964928e054ef6e7cd62ea3405fef2526` — 983 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/played.jsonl` — `dcfcc4047d428b22ceb576155c9403cfaf6c749cf8a412eb7f563f8afc18acbb` — 2642 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/postprocess.log` — `680161290c36039b269588e65529417ac3a7a8ce796f77749483889e43145219` — 12374 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/preflight-20260810T1902.asr.json` — `0b3a6298703d5aea55b8ed866d1ec336bb61fb788a36d04e24f56f3b9148896e` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/preflight-20260810T1902.mp3` — `213dc40b6a926f13e6a5871a29bff752f5a22c4ab5c945f0028da7406c8dfcfd` — 2156160 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/preflight-20260810T1902.txt` — `1e4ff2e9dff0a3279bbce632b02b013ad81b323b9b3aa4e5df1cb601538ee0fe` — 2034 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/provenance-finding-20260810T1730.asr.json` — `66480c9a936731b2da73c7ee62dbfe1425b47b209a98068c97fd28476989a48b` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/provenance-finding-20260810T1730.mp3` — `491f38b0684f102f38670405cb3419ed824c1afc76db41560d4474e053f5f392` — 2824320 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/provenance-finding-20260810T1730.txt` — `a342b5d9f1f446d5c81170ba625e0b063a2c3a4182d06bc6d0381de4bcba7492` — 2700 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/quaia-20260811T1050.asr.json` — `47dd54739aa4412cae7d2e4b2f58f6b1b06c71ffa7e4f75f59455e4abc2a525f` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/quaia-20260811T1050.mp3` — `bb3fc677650d4ea6bbc7ff99b91d35fd7f7728afa75d97a1de2a06ae5f07e939` — 2011392 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/quaia-20260811T1050.txt` — `add9ed9a871a39b95adf206d365b781582c1e5b2610c8447c83f89937399a092` — 1832 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/queue.json` — `19edf5d32fe352765662a9dbd36b22bd3c8210107387c825a873e6ae322d7e09` — 17097 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/queue.json` — `256f3215379b85d7851c5166e0143b9d3d3f8aac9b4df2a2132aca160c7e484e` — 17528 bytes — later/current review
- `/Users/duhokim/HermesOps/reports/status-audio/queue.seq` — `a4b2c5db15348c29451e18b8307e5ef81625ea638e807935f39ceaa8d9ac7758` — 3 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/queue_ledger.jsonl` — `89746ce9ad7f3419bcb8937dccedb5bf65c7f299db162ac42e95b42df608dd3e` — 17409 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/queue_ledger.jsonl` — `b1474cbdf49e71673c7cd6be187d04aaaf515c3eb8e9b06251349a128e6dddf2` — 17810 bytes — later/current review
- `/Users/duhokim/HermesOps/reports/status-audio/quota-coord-20260810T1733.asr.json` — `cc308a585cfc0d572eaac8f63db366ed55420bfc9c5dfda60fe7c2f4d839fe8a` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/quota-coord-20260810T1733.mp3` — `12c65ddaf3d6cfad05461eb71f0363ea890f8d3b5704ebb8d76183fcc3dce421` — 2365824 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/quota-coord-20260810T1733.txt` — `27f28d63152c8737b61cb05703275dadb1669099a73c1ce855b76b7548116570` — 2343 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/recommendation-20260810T2113.asr.json` — `0ff5093a8a867c452b7df2c3dc2086c5f3a00424754a8a09cb850c71bb946e7e` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/recommendation-20260810T2113.mp3` — `391cf20a84e66b118f95d13908881cbf0c4ad026325d947fef52e3968dd0dfc5` — 1869696 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/recommendation-20260810T2113.txt` — `2ecda8e5590cbf01d76532567c77566f6d578bdbc1de856a845636374615e336` — 1989 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/reframe-20260810T2205.asr.json` — `46c769b754e53fe918da87ea2d9181aa7430c5b55dfd9b5497735d47252039db` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/reframe-20260810T2205.mp3` — `41caa30dcbcd7999ed603866261dfbc8c038bd5d5a286ebd0c0e944289bcd10d` — 1923456 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/reframe-20260810T2205.txt` — `ac1e85f82c6adce364c07c36e7c41b09ecfe493d85949d2f8998106e437535ee` — 2011 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regate-armed-20260811T1015.asr.json` — `5f32b9378a52db4a788662ffdd4ccb5c45da896f81b1bd5bb3d3b8545d960229` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regate-armed-20260811T1015.mp3` — `1f5ee0c5732089db6ef8ee2cba30f54b5a96a21ae69849238402b7f703c6ecab` — 1379328 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regate-armed-20260811T1015.txt` — `8301d26df2624ef456c71704a1c6e657e77968dd39e900a1080e6a2c3e7588e6` — 1479 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regate2-20260811T1032.asr.json` — `e2555af1a50e94e57b34c5059d394468d4942841f15b541847bf2bdf81f09a57` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regate2-20260811T1032.mp3` — `d06e9ea034b7293b54154d665d17787ab37f342b31366df17001ca8103dd54ce` — 2421120 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regate2-20260811T1032.txt` — `d3ad1090e918d0c03afd8656b53591c78adab2baefeae32a217ee2bfeed74e4b` — 2516 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regatedispatch-20260811T1335.asr.json` — `d3b01812d9c6aaf0d9c39412773da7e8da22cf2feed4ad5c9c2ff252f4fb8b5e` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regatedispatch-20260811T1335.mp3` — `bf28d5c9a10d1838dd906ba206f3b7b01c9cbe57ab8db41fed414251b43328d4` — 1635456 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/regatedispatch-20260811T1335.txt` — `48b1584cdb72779182161e89792e32ac6a62f1559a4e586a34c4033499df8dfe` — 1822 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/relwatch-20260811T1102.asr.json` — `a4ff48656289b66b53fc6f5ca92f8813ece4c4c39b02ce5f922393ec4c7c1189` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/relwatch-20260811T1102.mp3` — `713b1e39c7cc48ad3a45e623b904a8f3a7b574668af9a9c4e5059da5faad1cd1` — 1223424 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/relwatch-20260811T1102.txt` — `996ce9367c13e0188adb91f29a5e1abe43a2ac6617810d6319f1a97abea82bef` — 1336 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T165959-hwao-report.html` — `76a84dae22a98c2d9ad28ab67051ca09ee3976d9932dff27d6c4753182a70c04` — 8316 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T171915-blanc-report.html` — `4b8bfb932ded6bf568b572ba17f937d0b2b2c891d449e2e3ec98a712a4faddf4` — 7116 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T173007-hwao-report.html` — `c0f3e44aa9a433364c5a2d580e03d5503e06135b2a9346d9581fd0ce115dda83` — 8636 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T173124-hwao-report.html` — `5a0616ba2ce4571b74ba5f686d2e1edf196098c43237a4cf5218e91f6ea7799d` — 9452 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T184851-tori-report.html` — `f36db2126ca7ce9401d143cd2913dc5e90146a8c432ace94c8e6970386308be5` — 9868 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T201107-tori-report.html` — `9a51511aeec21d31dbf9675d46428a42b519c39f4b37b85e6ea45e24cdb5312f` — 10373 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T204136-tori-report.html` — `dff5234724f1b1b641ae867f58524f173e71bc6fcc198e93a7800b6c72ffd0ee` — 6298 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T230754-tori-report.html` — `8db823083a03eb9afbc20e12631a44665a4f8081eca6b6e4a23f18eed2db8913` — 7672 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html` — `c5d5d5b81f5ae997e239203d2cd8e7e6c3065dc043069830ba138a29b9f6e9e7` — 8876 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231324-hwao-report.html` — `861e633683a49c70ca15d7d2a0e0e1fe21f7ea163111085cc13f4c03ebd82ad1` — 9874 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T235925-tori-report.html` — `1ebde8a62d1393996e7bca9350e9c84aa2993a57cffd7b93a5b9ed358e04d256` — 27446 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T004950-hwao-report.html` — `d4693eb627d5785354cfa0c27057f48508f24cb88697297941c5b51c01fbbb85` — 19499 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T080428-blanc-report.html` — `18734d3fdd389a1e000ffed169652a61d1a6cdcd695b201d7798b236f296fb9d` — 8213 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T105930-blanc-report.html` — `b832d6104df258bf8bed779d24229ce0ae49974f65e6026ce678e4a547f08b29` — 6264 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T145923-hwao-report.html` — `7dcf8e2ba41917e28987cbaf3317766499b361310030133535b2bff29bdeca77` — 13098 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T151249-hwao-report.html` — `f11078cce4e69efa4f59d37fd3681e18243cad80adce59571c99ca79588da0dd` — 10490 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T151843-hwao-report.html` — `849829d266274149e6a9f1d4fb22200929cbd218b3adef291502fdc07074cb87` — 11983 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T190931-tori-report.html` — `1071f27aee6325973e0b04664274568e8fdbbe4345f8576ee3f85b109421ca27` — 9051 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T200910-tori-report.html` — `51216d69a089dd4240c5b75e9ea5f737e4faa4b4b140bb2c3f26a68ce9ac7a14` — 10135 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/report-20260821T210530-tori-report.html` — `a93fe2cec33b675dbeaf48cb55a3fe7627fa1f9fe77d2ac05f8a40f58335b1e4` — 8443 bytes — later/current review
- `/Users/duhokim/HermesOps/reports/status-audio/response-20260810T1420.asr.json` — `dd3623db15a98378d281a2fda2674e95ddbbccaf0d8d79605938dd63bdbce23d` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/response-20260810T1420.mp3` — `5371e1b10c9f0788beace688dd25d157e7e280a6032b99e6d290f945765e6817` — 1890432 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/response-20260810T1420.txt` — `22d4e8075889fc07ae5891f774b017a35510d341f0a87ae44a998ac4bf890192` — 1959 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/rev4dispatch-20260811T1431.asr.json` — `88436e0f40c6d73e43e7e98f1390a9527b59128a18a8713fab6a795ff62d32a0` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/rev4dispatch-20260811T1431.mp3` — `72c07c54f30875b1ca867b29f1842b5fd8011c9ad3a24c401c330b552dd614a8` — 1538688 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/rev4dispatch-20260811T1431.txt` — `6aa6d9f3797fed1ff5b7cbc3f6fc7e575d0e19bf0e526ab6d6a99d2133405b24` — 1626 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/sentback-20260810T2148.asr.json` — `7c24e9335a5476295b1ffe9bdbde0d09dcaace2e1cc1bd0e2ac5731676eff96d` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/sentback-20260810T2148.mp3` — `bcfa6319ec8488658bf70448fe46df1b9e68987288ca222db1a0aa3848dab7b5` — 2070528 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/sentback-20260810T2148.txt` — `d5481b9b52d08b8174a501f0ee51f7738e8ba49c474256203665375a72d86729` — 2150 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/split-20260811T1108.asr.json` — `87282ff820a1cb31692a821a7660f6a41a75a02448fb67987bb78c2178da3be3` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/split-20260811T1108.mp3` — `89594dc0171653be1c53cd62edea9f295cc9f56c7858a1761b41ad5a7a251181` — 2278656 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/split-20260811T1108.txt` — `e16d400ed8f4d770e6274c401b79685206a5d311c74f9f106cbbfcdfa81c42a3` — 2479 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/status-20260810T1049.m4a` — `0d02d3612198723c04f5d74d7b71f93a371c9959913e16be3fa06c8bdcc74b0d` — 491516 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/status-20260810T1049.mp3` — `47a69974ab6e77fed2821f037a2e4dc258e8e40267065a3a63605a1f91a01166` — 450814 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/status-20260810T1049.times.json` — `b1a703288934c5d1728bb3c93fdc2dd569c2f049f29164cf6299e6d7575849c2` — 149 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/status-20260810T1049.txt` — `d8871fd9b7b6746e402a4ffe7b072f3240722954374c95f0552e2ec8df963e6b` — 654 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/status-alloy-20260810T1105.asr.json` — `2942e524cda8c3de97c5c04d3bc915c41e9162d9dbf1fca3d552406f80a34a93` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/status-alloy-20260810T1105.mp3` — `6ee64aaf6f3f08d54b7e9ed4ae4c0029fc1a6c2d63947c3a0025557fe92bd0b3` — 501120 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/status-alloy-20260810T1105.txt` — `2e702e2302174fb353f7108b8e5b6907a3261a0b83307cd8e9fc5c03fc5f7d30` — 486 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/status.html` — `d7109d3c622c4039c5827518e86965897ec2f24afb4151861f95d636decc771c` — 16501 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/torigate-20260811T1050.asr.json` — `cc77e534baf5c4a7c3cc57e56c5fe9cd9596121288dae1c46a80fa3d35dbe351` — 174 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/torigate-20260811T1050.mp3` — `79476c2d7a55f3d15dd5d37da86cbdb35d3d11b916fcc7be7022e39f3c4b9bb7` — 2961792 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/torigate-20260811T1050.txt` — `7b801445443f544d4e209870cadd07d5ffeb11ab29995f41cda9777e704b0233` — 2741 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/torirelease-20260811T1312.asr.json` — `dfb0f31282b511328b5663e676e4d3431cbf07db6e39994ae6ae30e14d6f17d9` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/torirelease-20260811T1312.mp3` — `db498a10e4a89c4fdf946d2bf3a4ff359b17f54b4703350617d2553bded1a797` — 2198400 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/torirelease-20260811T1312.txt` — `7d24603a2338d547960953ea6d7736c875ee3f43ba28ae77ea5fbc2ff10d2029` — 2298 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/voice-input-20260810T1444.asr.json` — `4b2f3a7a2d78d58be910b7e30e6a65491349e46398fbbbb60cf954d64e01e380` — 172 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/voice-input-20260810T1444.mp3` — `879fb1c3b5d59a44892e24d0ca9d4ce2a9bc32c4ec23b09f632b4a05701b5273` — 1056000 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/voice-input-20260810T1444.txt` — `01831a8e3545fcf06b30bdcbf55fb79ca1c80ba7b6af999448217691bd1d2d11` — 1028 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/voices.json` — `d1e6c05ec6476c620b0bc3c5d629922b7ec1e2ebecffa5eeb35f6c42d7c15365` — 706 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/why-method-only-20260810T1440.asr.json` — `1e41991ee976001c5ed1aa05f05e5dbadb7faa33554af5e086c128a3e0c4e1a4` — 173 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/why-method-only-20260810T1440.mp3` — `5d1905dc2281465af7338e25a2b15a892faa82f09cb380e1af0134516dc28a70` — 1393920 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/reports/status-audio/why-method-only-20260810T1440.txt` — `665c9bfe39e36a5c4af1899887d307be681c7ce8ca58facb96319aad5227802f` — 1539 bytes — first review: surface inventory
- `/Users/duhokim/HermesOps/scripts/nm_audio_align.py` — `4d63e4a540e8f0c4de57a521c10c311ffabdacd506b95bdd51505aa8bd942085` — 4145 bytes — first review: content
- `/Users/duhokim/HermesOps/scripts/nm_audio_index.py` — `70e9983ede8d12b1336158254a49bb37817b14a1077edac5d1ede51ae461580d` — 35781 bytes — first review: content
- `/Users/duhokim/HermesOps/scripts/nm_audio_publish.py` — `00d22295491526c75a6d7386dde25025a25eafc3a0fb6587c2a3b57942021bd4` — 10056 bytes — first review: content
- `/Users/duhokim/HermesOps/scripts/nm_caption_norm.py` — `5b44d0a73780329a5ea4c16f4eed2df5bf7c0884843a3c09dff3fd8309c4e2b5` — 4964 bytes — later/current review
- `/Users/duhokim/HermesOps/scripts/nm_deck_build.py` — `807a90fe1c619fb405395b176a861acadd31eb5349fdbb5a6fded8471717eafc` — 6352 bytes — later/current review
- `/Users/duhokim/HermesOps/scripts/nm_queue_admin.py` — `796400a7b11794e0a227ac0e0c3fddd10979851f1afad8f35c131c69eca0e78f` — 8175 bytes — first review: content
- `/Users/duhokim/HermesOps/scripts/nm_report_graphics.py` — `cd7ed009b9b90bc6445d0ef5a682d39849744e5427d7470a2dd1483ab22d0403` — 28797 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/HermesOps/scripts/nm_report_postprocess.sh` — `b91ce49d5c1d4868bb28d11f698ac7a55c4053c907258f9c11354e8f994d6e09` — 1385 bytes — first review: content
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/blanc-ops-overhaul-20260820/PUBLICATION_LEDGER.md` — `41feac582cef7cbe28e487c89c0712c5be6c43d04da96aa347b15d4381f43df7` — 4543 bytes — first review: content
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/DESI_GRAPHICS_ANSWER_20260820.md` — `08a99c05743e9cdc9ea39335927b4fdfae88c1e879c737b5ba24ef6dcc4ac4ff` — 5102 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/HWAO_EXEMPLAR_REPORT_SPEC_20260821.md` — `299ee93c8f530aad51e41836428889a2f65d9a37c85bb508d4f79024af6f24fe` — 5698 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/TORI_TO_HWAO_MISROUTED_BLANC_TRAFFIC_20260821T2055K.md` — `56a76294dbc1a0d263077953a68266f586e8d122549dcf0e79ea5508bf829b4a` — 5577 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/AMENDMENT_PREK8_20260820.md` — `161547400e47ed66df616ba14756d9ab066c547f54b39bc161e6b4eaa26478c0` — 60400 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821.md` — `5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043` — 8545 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md` — `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e` — 5164 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md` — `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c` — 4636 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md` — `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093` — 5350 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md` — `acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b` — 6246 bytes — first review: content
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md` — `2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65` — 5970 bytes — first review: content
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CSEAT_AMENDMENT_DONE.md` — `48ae45bc73bd99a60c2e75ef5c69692f26f70e1219ea8062a0ddc486ae03953d` — 4681 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CSEAT_AMEND_REPAIR_DONE.md` — `ab6493ce234763d2a04b3afb1dc5e82b6eb9936c895ed737f92835be93545ec1` — 7566 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/DECLARATION_INCONCLUSIVE_BY_POWER_20260821_REFUTED.md` — `af51507a43fcdee4e53b51502c332e3624611bb27de6d0bede120b33c8b38ebb` — 5847 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_20260821.md` — `a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa` — 23903 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_FINAL_20260821.md` — `1cf7ba7780a556428e691d76bb54e08949fb375eb7a3112257ff7986a100ad01` — 36764 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R2_20260821.md` — `59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066` — 18434 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R3_20260821.md` — `c1ad25fd6574bb9bf3386d8d6fb7448ed62015384035f9110dbde3e94ec0c453` — 24867 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md` — `94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e` — 15172 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_FOOTPRINT_GEOMETRY_20260821.md` — `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1` — 12861 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md` — `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b` — 23416 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_VOID_ON_DESIGN_DEFECT_20260821.md` — `38e789547e750d21b38fd9d1fa3515bc44ed8f95d542476183d45274c7518b3c` — 22552 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GPT2_PLUMBING_DONE.md` — `b6c462cf213e08c7c88ae2cc375dcfd972d47f04c3d1e2e8414dcc661fb806f4` — 3434 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/K8_CROSSING_AUTHORIZATION_20260820.md` — `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69` — 3710 bytes — first review: content
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KICKOFF_GATE_A_AMENDMENT.txt` — `c91e1c1efc032d81f839b39ce7277daa087a9335521a9762d8b61f9e8d75ddc8` — 2488 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KICKOFF_KIMI_AMEND_PLUMB.txt` — `f569058542382ba91e3aeb5cf25c1ba2d6dc77a73b4c6dc448268f91a93b8766` — 3757 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KUN_GATE_A2_REGATE_20260820.md` — `65ebcd76da90c41dbd2545e2e34c310321e111cd327102956153ff48f6640674` — 15574 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KUN_GATE_A_AMENDMENT_20260820.md` — `a991af772c870744125aee251817c0c13bd275628808c555378d4deb9dba2c45` — 25067 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KUN_GATE_B_PLUMBING_20260820.md` — `88d8d844fd9ae9a375c709f5d55326467f57673d972e920e64ce8fdf25a05371` — 8571 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KUN_HARNESS_GATE_20260815.md` — `8936b54b140e043f1050403e68239c30a3d56e81f2cfc9a1db9e0e0284efae0f` — 8846 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/RUN_ENVIRONMENTS.md` — `25ee0be369419b744cdd78ab0507f34e68a3c64a49142258d51d6efcb941fe9c` — 2163 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/YUI_BLINDED_HANDCHECK_HARNESS_20260814.md` — `902d7421afa08cb311acce0a28baae515c42375e947b675fb970885aeb41dbd9` — 5996 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/build_custody_tables.py` — `aac8f56211c19bbe1ecfa8ff81145b63f096f35d5acffc2cf4ddb98504dfe6f0` — 6435 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/tables_20260821.txt` — `8ab711dc12f4fce71d3b55bbbaad7d6e3870a03d01e53c087605c05a39cceba0` — 3652 bytes — first review: content
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_inference_20260820/chi_wrapper.py` — `e9b0ed122f298e531d97e870281b1593444587ec2908a760be10b94b3c03aec3` — 3345 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt2_hold/hc1h_prepare.command.json` — `59b85f818d0aeee58cd3972dc83ab71e9427cb270d66148293eb7c0fcbd2c817` — 1408 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/hc1h_checking/commitment.json` — `2fdcb164800d3dabcf75ca4f1b6439c88ef1c438e14a1f13de3e35eab9e26883` — 1953 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/hc1h_prepare.command.json` — `59b85f818d0aeee58cd3972dc83ab71e9427cb270d66148293eb7c0fcbd2c817` — 1408 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/hc1h_prepare.stdout.log` — `9799d08eb4799e4710edc827ae2c17a7885810afa8d3ba2ea058a40c1da5a8aa` — 2056 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/hc1h_private/prepare_receipt.json` — `e9d77ba140872a995a0a6454bcc12d5767f74ff4760e166227d1dccbb2d822af` — 1754 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_checking/commitment.json` — `4a2e01407752f9c183898063e49ba8101c97d48db604a44f958452acaaaac15a` — 1952 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_prepare.command.json` — `59b85f818d0aeee58cd3972dc83ab71e9427cb270d66148293eb7c0fcbd2c817` — 1408 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_prepare.stdout.log` — `eb4ef2eb1d61634d166beaed35727b49f2374b87124a97c945c40240677db04f` — 2063 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_private/prepare_receipt.json` — `fb10e2d26f5bbe76a392850aa9e3db1195571749153fa25164ed5a3731179a9b` — 1761 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/run_rehearsal.py` — `fa0be824fb8da360acda97ba29c2262ad48e5229f29fe9be6be408e1602aaa32` — 33876 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_DECLARATION_20260821.md` — `b718832db8924ce7cfca307aa3e050218fca0ea77ac3240cd24fd85d0082f158` — 2675 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_FINAL_20260821.md` — `a129711deadd41ff8d29d5cad8b33647b90e9249748a8094e831e59818bca25b` — 3141 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_FOOTPRINT_GEOMETRY_20260821.md` — `fd6512ad42e15eb9e01c7f978d136876d25f7f4c78578c307d7cfa1f75cbcdce` — 3804 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_FOOTPRINT_GEOMETRY_REGATE_20260821.md` — `b36fb6fbaaf897849f8e98d6de60d5159234270a78e3bc8ad2f79d1067a90ca5` — 4047 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_MEMO_20260821.md` — `41c59777ff176a7a5d72ad095af6f4b8e2ed54283d4b2caf361b48ef1febede4` — 4052 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_MEMO_R2_20260821.md` — `5b34532bff9d696b3e26eb911d86a19d9e9d77323813e0ae3c8a0983c3ce5f52` — 3591 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_MEMO_R3_20260821.md` — `e1d43ee2eb6c380b4b67352b9ef4425f9ce5b2c01db9d7348471cb695735f497` — 3548 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_RECEIPT_R6.md` — `1a501da106133406d04b03e4a8afde910c5a6d8b4dd3455f26ef7a20278cc78d` — 3575 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_VOID_20260821.md` — `2f58fa04104ef7118f424583b2a3d811c5b0665344c9de4c2ffcdc6d3fa32d19` — 3714 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_KUN_HARNESS_GATE_BRIEF.md` — `b37fd9852a491e5a64387e8bb7d73ddef9fdfd4f2d2015f4b7c44ea2e837b98e` — 2035 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_YUI_HANDCHECK_BRIEF.md` — `84aef531041694c949da5f2a0906746e1c8f0d709cd5fc2dca6ea4b4c2684f8c` — 3933 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_YUI_HARNESS_HC1H_BRIEF.md` — `143c49720c0fd3005a7ce0b0d5d43bf877fd19c3120164e942a9b15d2bd2d015` — 3282 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_final_stdout.log` — `c98ccf9547425825b2164977ef5c9d3aff4251a638cc7930d803c9eca8e09789` — 11276 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_memo2_stdout.log` — `2001b8dd10765d78a872e68b08320d5feb5f9272a497946f74e9b566e5fd2c95` — 13621 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_memo3_stdout.log` — `da9d374718458402a39de06696b10954e3fc18959e105d9590ab4a4f46b3b849` — 15490 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_memo_stdout.log` — `2f217d842beb8af715ce364d8819b7992471302ee5a16a8902c8c0d68dac994e` — 12291 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_asr.json` — `243f2404240515e10b2d17791cb2f2b2772aa9b8c8eaf13020fbbccb05822d75` — 30645 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_asr.py` — `4fcdf4605288afc3267bec52e99887fc5e67a411f6420a99de3b43e2860276ad` — 1521 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_asr_crosscheck.json` — `6926e630df2c03edc89c24eed4f63970e34d4d3d614c017b15c76831682648a6` — 53375 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_asr_crosscheck.py` — `cadd070964d72737d2bede59798b583e6f5c1d0db3acae97afc24de6a7358bf8` — 1301 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_audit.json` — `916eb6d4262e9fba8896afcf2d617ac825b13de72fff64b2db03cf9fadcf5636` — 282773 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_audit.py` — `cb201032af7336d4f440d71ec64fd478b8e746371ec1f95ebc1f2ccc49d4d348` — 12236 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_audit.py` — `cb201032af7336d4f440d71ec64fd478b8e746371ec1f95ebc1f2ccc49d4d348` — 12236 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_generator.txt` — `8ab711dc12f4fce71d3b55bbbaad7d6e3870a03d01e53c087605c05a39cceba0` — 3652 bytes — first review: generated stdout
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_generator.txt` — `8ab711dc12f4fce71d3b55bbbaad7d6e3870a03d01e53c087605c05a39cceba0` — 3652 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_generator_latest.txt` — `8ab711dc12f4fce71d3b55bbbaad7d6e3870a03d01e53c087605c05a39cceba0` — 3652 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_generator_postreport.txt` — `e213ebe35a54abebbc1eeb5f0605ae0fb19775c295b64510869f885884e9e686` — 3771 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_git_history.txt` — `7eb4f170921ccfbada12a77aafa5857cc0b7af351dfb72660e24f513c086876c` — 530991 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_hash_appendix.py` — `8c760246938815eec7954ce59f74d219d98c085768ca64be537fdeadab9db301` — 2192 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_remote_004950.html` — `d4693eb627d5785354cfa0c27057f48508f24cb88697297941c5b51c01fbbb85` — 19499 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_remote_231235.html` — `c5d5d5b81f5ae997e239203d2cd8e7e6c3065dc043069830ba138a29b9f6e9e7` — 8876 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_remote_231324.html` — `861e633683a49c70ca15d7d2a0e0e1fe21f7ea163111085cc13f4c03ebd82ad1` — 9874 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_remote_ledger.jsonl` — `b1474cbdf49e71673c7cd6be187d04aaaf515c3eb8e9b06251349a128e6dddf2` — 17810 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_stderr.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_stdout.log` — `bdf39fa4835f32870ac95599e9d2155b2cddc697b26825292626fd13e52ee4e5` — 3233 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_stdout.log` — `6cf4397cc04fa3c5313911fc4e389e4e74489e7dc0204d1ac42b64d1619da123` — 16254 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_youtube.mp4` — `b87746997ae1d31bfc4659c5d66dba0c2ddffe0685042af7a29008241a05aa14` — 6022637 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_youtube_105.png` — `fbd67fd1632060593837054e3cb0a7328e38c12a788ebcb3930eb4ab7ebcf032` — 336054 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_youtube_95.png` — `80b3209b7834351d01efc54c989f22f5046694ee54d78840e8cd009ecb37e34e` — 279254 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_yt-dlp` — `0f192b7ec147ab6288885d6351d9ab67367640029b4377576ef46dd79cf7b202` — 37146048 bytes — later/current review
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_void_stdout.log` — `8c6632354134ee6aa4ae9715d7a68e6867a797d4ec7bd91068b3ede5ee5d95de` — 10150 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/OPERATING_INSTRUCTIONS.md` — `db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f` — 10429 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/SELFTEST.md` — `ccb217287424bbac06e4bc6f3c6e3c8f54a300c5e2f0ed42e64896cca8bd8d18` — 8211 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/YUI_HANDCHECK_HARNESS_20260814.md` — `d5b2ce3a2d938d8baa88861f4f2983d8fcfedd7582d25ec9f7225835d2381697` — 24608 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_full_test_stderr.log` — `9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8` — 3464 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_full_test_stdout.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_independent_stderr.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_independent_stdout.log` — `51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb` — 43 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_independent_verification.json` — `19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8` — 2573 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_selftest_stderr.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_selftest_stdout.log` — `a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b` — 929 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_synthetic_selftest_receipt.json` — `25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40` — 869 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/independent_verify_hc1h.py` — `15f48274ccf81d476a3a92c2241a279dfe4b098d018a83e68368d2ad0000936e` — 10928 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/nm_handcheck.py` — `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4` — 161895 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/run_hc1h_synthetic_selftest.py` — `2698ab1768656649c881a862d70f72011464f4614923391e6bd5e5dc8339f206` — 12395 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/README.md` — `727aef49cbf2f0ac7e6bf29ab94b7d9154132e80a0833640c305d5ce71094382` — 592 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stderr.log` — `ebe607be44c62c552a845f0cbdbdb5986fa5c7c0d53eff9bddd575a5c37ae4a5` — 697 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stdout.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/full_test_stderr.log` — `148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b` — 1776 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/full_test_stdout.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/independent_stderr.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/independent_stdout.log` — `b4f51b589170659f0be7c6e38d93c81e35b13a13e4813ede694f9e9bf4a2de63` — 56 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/independent_verification.json` — `54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae` — 1861 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/independent_verify.py` — `c10ca1b5cc3f9e178e5551b4b48459f11f8fafbb0734ce4531af481f1e9aec98` — 7814 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_receipt.json` — `9056ef22c89ea8e4606610948ac7b32b959c97ec42d3ea2597bdc4e71bb67ce7` — 2523 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stderr.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stdout.log` — `29a592d8ed9c9c571ff96195e1313815a7cb3ece824fb67e9ae2d539779a1b1e` — 131 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/run_synthetic_selftest.py` — `cc3c077ec613d4745ae7743cbc6e24a5b8a12e04efe361359560a07e5ef42821` — 15332 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/synthetic_selftest_receipt.json` — `1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8` — 3032 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/synthetic_selftest_stderr.log` — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/synthetic_selftest_stdout.log` — `e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab` — 131 bytes — first review: handcheck full inventory
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/test_nm_handcheck.py` — `ffa2910edb610892f7ca742feb0756f3ed212bf79b48e58f8c2ee2bd5e97fc71` — 69590 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/run_hc1h_stage.sh` — `5b91b8d7b5a8135950b6b829632b8b568dafe9780776016f2311543e6215a9af` — 347 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/test_committee_state_vocabulary.py` — `6cae8be7cae5aded9e1a8eb9876847760c94db3a332c9476020879c0978e0b9d` — 2150 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/test_run_environments.py` — `ce116729dedea22035474fcae925dcfbeb239dc3f6b609db2455101aa98bda53` — 1847 bytes — first review: whole-tree matched artifact
- `/Users/duhokim/NebulaMind/NebulaMind/tools/audio-reports/nm_audio_publish.py` — `57324635b59a7b8eaafd45409ffb48d019572dbb1bb86ec9b467f0668ad8bca6` — 8776 bytes — first review: content
- `/Users/duhokim/NebulaMind/NebulaMind/tools/audio-reports/nm_report_graphics.py` — `223e346f7b5a57e8e7497b6d98efb78c0e4b7fbb971f0171a6473685af0b6f65` — 28660 bytes — first review: whole-tree matched artifact

## Mechanical evidence and hard boundaries

Performed read-only: two generator executions plus a later live-drift rerun; exact fence/table comparison; queue-vs-ledger event reconstruction; observed append-prefix verification; read-only queue audit; semantic reading of all six receipt revisions and relevant gates; every `handcheck/` artifact; whole-tree/handoff/HermesOps invocation and strata search; relevant git-history extraction; detector battery; full post-crossing status-audio surface inventory; local ASR of every post-crossing root/draft MP3; independent small.en/medium cross-check of the 23:12 values; all six referenced graphics pixel inspection; active cockpit search; Tailnet-served byte downloads; remote host presence checks; current YouTube metadata/transcript extraction; current YouTube transcode download and encoded-frame inspection; interval/sequence/hash arithmetic.

No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, or read. No chi value came from that tree and no statistic over its records was computed. All values cited here came from already-published text, HTML, MP3, deck-note, or YouTube pixels.

No remedy is proposed. No target receipt, source, queue, ledger, report surface, cockpit, video, database, runtime, process, git state, or remote host was changed. Task evidence writes were limited to the required gate report and lane-local names beginning `_tmp_gate_r6_*`.

One tooling deviation is disclosed: a Browser Use attempt failed before opening YouTube because Chrome remote debugging required user approval; during its own bootstrap the managed browser harness installed runtime packages in its tool-managed cache outside `prereg/`. No browser navigation or page action occurred. All substantive audit evidence files created by this seat remain under the permitted `_tmp_gate_r6_*` prefix.

