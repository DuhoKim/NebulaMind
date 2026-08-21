REFUTED_DECISION_MEMO_R6

# Cross-engine adversarial gate — Decision Memo Revision 6 only

## Verdict

Revision 6 is **REFUTED**. The dispatched bytes were stable and matched the required SHA-256, but two new custody mechanisms do not provide what the memo says they provide, the embedded generator block is not a fresh-output match, and the disclosure section calls a caption-based ledger authoritative after that ledger's own correction says its clearance method is unsound. The frozen-protocol theory itself survived: the preregistration creates no anti-abandonment duty, HC-6 has no footprint input, and Revision 6 declares no frozen F-6 outcome.

No remedy is proposed.

## Dispatch pin

Before content review, the live target and the dispatch snapshot both hashed to:

`3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`

- live: `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`
- snapshot: `_custody_20260821/_gated/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.3ec5f2498483.md`

The same equality held again at the final evidence cut. The snapshot was mode `0444`, 11,693 bytes. The live target did not mutate during this gate.

## Ranked findings

### 1. BLOCKING — `gate_snapshot.sh` does not make an immutable snapshot, and its ledger is not append-only in practice

The mechanism claimed at memo lines 17–18 fails its own stated property.

- `_custody_20260821/gate_snapshot.sh:14` does `cp` followed by `chmod 444`. On this host the real snapshot reports mode `-r--r--r--` and **no filesystem flags**. The owner can restore write permission, alter the file, unlink it, or replace it. A controlled lane-local probe changed mode `0444` back to owner-writable and changed the bytes from SHA-256 `25718360e05d3c2d0963d1381e9dd4dae5fca789244ee4b9f861adcc0cc96218` to `57673254e78a37754096338ffc388492d4778b0e1c831193a3b781e7bd64cd30`.
- Line 14 trusts any pre-existing destination with the same 12-hex prefix and does not verify that destination's full digest. After a snapshot is replaced, rerunning the script skips the copy yet appends a row claiming the current source hash.
- The 12-hex filename is not the full content identity. Prefix collision is not the immediate attack; pre-creation or later replacement is enough because existing bytes are never checked.
- `_gated/GATED_SNAPSHOTS.jsonl` is ordinary mode `0644`, has no append-only flag, no hash chain, no signature, no external anchor, and is written with shell `>>`. A controlled lane-local ledger was appended and then truncated/replaced successfully. Its final probe SHA-256 is `f63d5d090bbc6c98ee37c9e7a0a0c154672b739647d1690efac3750a155858b1`.

The current dispatch snapshot happens to match the target. That is a successful current hash comparison, not immutability or append-only custody.

### 2. BLOCKING — the memo's fenced generator block is not a fresh-run match, and the self-digest does not bind the pasted table

The stable-path part holds: a fresh execution printed

`GENERATOR: build_custody_tables.py sha256 94e941093c716b5a1a276a30a270a477b4aec7893d758b5f6edb336ea86a2ba3`

and the script's actual SHA-256 was exactly the same.

The embedded-block claim fails mechanically:

- Fresh stdout SHA-256 before this report existed: `217d836f13795ebfabefd6c7883ad83795cd5cd1e0519446f6ec267d6e58ea33`.
- The memo's only fenced block is 1,725 bytes.
- Exact search of that block in fresh stdout returned `-1`.
- Immediately after the generator line, fresh stdout contains the heading `A. GATE HISTORY — verdicts, and which revision HASHES each gate cites`; the memo removes that heading, inserts an extra blank line, and then pastes the rows. It is a composed splice, not a contiguous output slice and not the full output.

After this gate report existed, a second fresh run had SHA-256 `d928dd1f65d4293e2a64424f46e46308676c8898f14e1e9e94fa8599d5936ca6`, included the new `GATE_DECISION_MEMO_R6_20260821.md / REFUTED_DECISION_MEMO_R6` row, and still returned `-1` for the memo-block search. The generated history is dynamic under the gate required to approve it.

Therefore the copied digest line authenticates only the script path bytes read by `self_sha()`. It does not authenticate the rows pasted beneath it, the dynamic files scanned, or the composed excerpt. Arbitrary table text could be placed below a genuine first line without changing that digest.

The absolute claim in `self_sha()`'s docstring also fails under concurrent mutation. It hashes `open(__file__, "rb")` at call time, not the bytes the interpreter originally loaded, and there is no lock between that read and printing. A controlled probe using the same function shape printed SHA-256 `849fc9413b3a746bb694f56008efb8a8e73b0f5856b0a7df68b59b73bcfedb69`; the path was changed after the read and before output, and the file that completed the print hashed to `87979893c6debd31ec51d47db3b48c76de8b19a5665d64573be7dc1164b053d8`. Stable execution matched; “can never disagree” does not.

### 3. BLOCKING — the disclosure section defers to a ledger whose own correction invalidates its clearance method

Memo lines 140–145 call Blanc's commit-`d53fd6c1` Markdown and JSON twin authoritative and repeat the `220 transcripts / 18 decimals / exactly one real` conclusion. That deference is not supportable as written.

- The committed Markdown bytes at `d53fd6c1` hash to `b092052adcacf4dd9fd727f0453ec75355a2e83613d7f7940cc3575dbb4ab857`. They record the **caption's wrong values** as what the audio says.
- The machine-readable twin remains at SHA-256 `d0c670037ab0f3b802c301647e91b6956b5cd4170929ad06ebfe3b56be026e04` and likewise records `zero point 27`, `zero point 20`, and `minus zero point 20`.
- During this gate the live Markdown changed from the committed `b092…` bytes to SHA-256 `79d89c9d0c5232e572aec2650c3680e55904f58f9b4c2d63286b8a1c5a8fac31`. Its new lines 13–18 state that the method is unsound where it clears anything: the 17 exclusions and clean conclusions used captions, not audio, and are unverified until ASR.
- `nm_disclosure_audit.py:90–123` confirms that limitation. It scans `.txt` files and classifies them; it never transcribes an MP3. Its `surfaces()` function counts the MP3 and alignment file by existence and counts pages by stamp presence, not by checking that each artifact carries the disclosed values.
- A fresh run still returns `transcripts_scanned=220`, one disclosing caption and 17 caption-based exclusions, but that reproduces the caption classifier, not the audio-wide claim. Fresh result SHA-256: `856454c5d675fcfd10cd6478f26ca2fa7605c7c0ce1e7b059de6b43d8b8771dd`.

The positive audio fact does hold independently. A fresh isolated `faster-whisper base.en` run against MP3 SHA-256 `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168` transcribed at 11.20–22.72 seconds:

`The first three real values, 0.834336, 0.384410, and minus 0.640352`

The ASR JSON hashes to `166a9d4d833c149eb0ee6bd35a6d952edd174884cea519114c91595309ff7edd`. The queue ledger has exactly one `publish` row for this MP3: seq 20 at `2026-08-20 23:12:51 KST`.

The memo's next universal sentence is nevertheless false. Memo lines 146–148 say **every text surface** fabricates the full-precision values as `0.27/0.20/-0.20`. The unchanged deck JSON contains the three full-precision values in its notes at lines 52–57; the alignment JSON contains no values at all. The current caption and served pages have now been corrected to full precision, while the preserved corrupt caption carries the old fabricated values. Thus the accurate statement is not “every text surface,” and the six-path inventory is not proof that all six artifacts carry the same disclosure.

Observed path facts:

- Six paths are enumerated and exist.
- Exactly one publication event exists for the MP3.
- Audio full precision is independently verified.
- `times.json` contains only mode, coverage, duration, sentence count and end times.
- The deck's rendered slide set omitted the values; its notes contain the exact values while falsely saying they were “not in the audio.”
- Caption, report page and archive were mutated after the old disclosure snapshot. The old caption survives at SHA-256 `7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad`; the current caption is `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`.

The current Hwao ASR finding, SHA-256 `f5d7f276d666867f70f6eba388793496adff96e5ec293f162b43976c87c76fb2`, agrees on the audio values and states that the custody receipt and decision memo were not rebuilt on the finding. Revision 6 incorporates the exact values but still calls the superseded caption ledger authoritative and repeats its unverified clearance totals.

### 4. MATERIAL — the DRAFT boundary is explicit, but the body still fails the literal “no operative sentence” attack

The new blockquote is materially stronger than Revision 5: it says nothing is in force, no signature/gate exists, the study has not been declined, and every later statement is what a signed memo would record. That global frame prevents me from treating the draft as proof that an actual decline occurred.

The body nevertheless continues in unqualified indicative language:

- lines 26–28: “the investigator chooses not to carry the study further” and “nothing … is amended by stopping”;
- line 31: “It is adopted”;
- lines 107–116: “the sample cannot deliver,” “the expenditure being declined”;
- lines 132–136 under `Resulting status`: “Halted by investigator decision” and “this study … reports nothing”;
- lines 183–189: “a memo halting a study” and “Acquisition runs to completion.”

The blockquote itself calls such indicative clauses drafting errors. On the brief's literal sentence-level test, those clauses remain. I do not rely on this finding alone because the top-level conditional frame is unmistakable; the custody and disclosure failures independently refute Revision 6.

### 5. MATERIAL — archive attributability is real, but the memo overstates the `href` mechanism

The core Revision-5 correction survives:

- `20260820T231235` occurs twice in current `archive.html` and zero times in `archive-2.html`.
- The relevant `archive.html` reading is in `<li data-src="20260820T231235-hwao-report.mp3">` and includes `href="report-20260820T231235-hwao-report.html"`.
- Every `VALUE(words)` detector hit found in `archive-2.html` belongs to a pre-crossing `20260814…` reading with its own `data-src`. The archive-2 hit is genuinely a different earlier reading, not the 23:12 disclosure being explained away.

The exact sentence at memo lines 158–161 says **each reading** is bound by `data-src` **and** a report `href`. The six archive-2 detector-hit `<li>` elements had `data-src` values but no report-page `href` in their bodies. They are attributable by `data-src`, so the substantive correction holds; the universal two-mechanism wording does not.

## Revision-retention audit

Only Revision 4 has the disclosed post-gate mutation. Direct current hashes and earlier gate pins are:

| revision | retained SHA-256 | earlier gated SHA-256 | result |
|---|---|---|---|
| Rev1 | `a683bc9424f26fdeabccd414aecdc0b67f08bab86307015e68294612d6a7a5bb` | same | holds |
| Rev2 | `7e1b2e2f4f104ce171c6e9e50ed843ef70417a5f76216bf4e0618b0163ded64f` | same | holds |
| Rev3 | `bafec8bf5f177830d4eeac75a0a7b29c72ea9b7dcfedd3b33f697a283836c62d` | same | holds |
| Rev4 | `d69be7af81613c3f6a103e5ff833778dd4c036a3e121ac131852d459b38a6efd` | `eeb033ab8e32bd58f2360243d220f2d08f7fb85de2f76fc5e42d556c3010d342` | mutated, accurately disclosed in R6 |
| Rev5 | `276363f36e7c726d39fed811d011552ff8a1e998915d179bcd00d1c2e003dc5e` | same, pinned by the R5 gate | holds |

No second retained-revision mutation was found.

## Frozen-text substance — attacks that failed

### No anti-abandonment duty

**HOLDS.** The frozen preregistration defines the four F-6 outcomes and exact triggered stop/void paths. It does not impose a duty on the investigator to continue until one occurs. Its own preamble has an authorization-dependent STOP rule. Section 7 governs handling **if** an outcome exists; it does not manufacture an outcome from a human decision not to continue.

### A footprint-aware reason does not become HC-6

**HOLDS.** Frozen HC-6 at lines 319–329 takes `A_eff=(2a-1)*0.0408` and bound `N` through the pinned normal-approximation logic. `sim_power.py` draws uniform-sphere `costheta` and uses the full-sphere `mean(cos^2)=1/3`; it does not accept or read a footprint statistic. A footprint-aware external reason can therefore motivate a non-preregistration decision without becoming an HC-6 input. No HC-6 verdict is issued here.

### No frozen outcome declared

**HOLDS.** Memo lines 22–24 expressly reject all four F-6 outcomes and void. The separate `Halted by investigator decision` language is a draft-status problem, not a hidden F-6 category.

## Other failed attacks / facts that survived

- The target remained byte-identical to the dispatch snapshot throughout review.
- The generator's printed digest equals the stable current script digest.
- Rev1, Rev2, Rev3 and Rev5 retention matches prior gate pins; only Rev4 differs and Revision 6 admits it.
- The 23:12 disclosure is attributable in `archive.html`; `archive-2.html` is a different pre-crossing reading.
- The exact full-precision audio values survived fresh independent ASR.
- Exactly one publish event exists for the 23:12 MP3.
- The procedural theory survived direct review of the frozen preregistration and `sim_power.py`.
- No frozen F-6 outcome is asserted.

## SHA-256 ledger — every artifact selected for content/hash review

### Target, snapshots, revisions and gates

- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md` — `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`
- `_custody_20260821/_gated/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.3ec5f2498483.md` — `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`
- `_custody_20260821/_gated/GATED_SNAPSHOTS.jsonl` — `dabfa9ee308a6e6a4ca346da1f1ba1ecb8e16612a1b4f022bba7f22b1ce815c7`
- `_custody_20260821/gate_snapshot.sh` — `6f4c34cda12e6eecdd8a480fb97789f8bdca2074d2c55dcd6a066365a2c0f6a5`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV1_SUPERSEDED.md` — `a683bc9424f26fdeabccd414aecdc0b67f08bab86307015e68294612d6a7a5bb`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV2_SUPERSEDED.md` — `7e1b2e2f4f104ce171c6e9e50ed843ef70417a5f76216bf4e0618b0163ded64f`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV3_SUPERSEDED.md` — `bafec8bf5f177830d4eeac75a0a7b29c72ea9b7dcfedd3b33f697a283836c62d`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV4_SUPERSEDED.md` — `d69be7af81613c3f6a103e5ff833778dd4c036a3e121ac131852d459b38a6efd`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV5_SUPERSEDED.md` — `276363f36e7c726d39fed811d011552ff8a1e998915d179bcd00d1c2e003dc5e`
- `GATE_DECISION_MEMO_20260821.md` — `a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa`
- `GATE_DECISION_MEMO_R2_20260821.md` — `59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066`
- `GATE_DECISION_MEMO_R3_20260821.md` — `c1ad25fd6574bb9bf3386d8d6fb7448ed62015384035f9110dbde3e94ec0c453`
- `GATE_DECISION_MEMO_FINAL_20260821.md` — `1cf7ba7780a556428e691d76bb54e08949fb375eb7a3112257ff7986a100ad01`
- `GATE_DECISION_MEMO_R5_CODEX_20260821.md` — `c9a144e256d2c7ef6c63d11c60b5002e25c7268483a4dc0bbd112ffdfeb24707`
- `CHI_DISCLOSURE_ASR_FINDING_20260821.md` — `f5d7f276d666867f70f6eba388793496adff96e5ec293f162b43976c87c76fb2`

### Generator and frozen statistical sources

- `_custody_20260821/build_custody_tables.py` — `94e941093c716b5a1a276a30a270a477b4aec7893d758b5f6edb336ea86a2ba3`
- `_tmp_gate_r6memo_generator.out` — `217d836f13795ebfabefd6c7883ad83795cd5cd1e0519446f6ec267d6e58ea33`
- `_tmp_gate_r6memo_generator_post.out` — `d928dd1f65d4293e2a64424f46e46308676c8898f14e1e9e94fa8599d5936ca6`
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `../spike/sim_power.py` — `f2867dbf4f5ab8ad82d645324a525a75af38006ff03e8ee08b90589cff50b1ce`

### Blanc ledger, audit code and selected ASR code

- commit-`d53fd6c1` / initially observed `DISCLOSURE_LEDGER_AUDIO_20260821.md` — `b092052adcacf4dd9fd727f0453ec75355a2e83613d7f7940cc3575dbb4ab857`
- corrected live `DISCLOSURE_LEDGER_AUDIO_20260821.md` — `79d89c9d0c5232e572aec2650c3680e55904f58f9b4c2d63286b8a1c5a8fac31`
- `disclosure_audit_20260821.json` — `d0c670037ab0f3b802c301647e91b6956b5cd4170929ad06ebfe3b56be026e04`
- `HermesOps/scripts/nm_disclosure_audit.py` — `9127b33d78205914a259d332c139e8168fe474d04f4ea2282e004c7f2860c20e`
- `HermesOps/scripts/nm_caption_norm.py` — `ffcc51a730d72e86b070829886d7b4462f1a80125c77c0a946a65127b4a02946`
- `HermesOps/scripts/nm_audio_align.py` — `4d63e4a540e8f0c4de57a521c10c311ffabdacd506b95bdd51505aa8bd942085`
- selected independent ASR reference script `qa_audio_asr.py` — `9b66b8ce7d2f116061c6dee7bab043940565642b7a005fe71924d8d670df34d5`

### Status-audio artifacts at the first synchronized evidence cut

- `20260820T231235-hwao-report.mp3` — `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`
- `20260820T231235-hwao-report.txt` — `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`
- `20260820T231235-hwao-report.txt.corrupt-20260821` — `7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad`
- `20260820T231235-hwao-report.deck.json` — `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`
- `20260820T231235-hwao-report.times.json` — `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`
- `report-20260820T231235-hwao-report.html` — `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`
- `archive.html` — `33c4c6c8db63ed278945bd06fd714b352777857372e72b185358e982bd573710`
- `archive-2.html` — `b1625dc12554fbcc76226849aa45a5ad4925e891b6eccaee4a1e163ad675ee3f`
- `queue_ledger.jsonl` — `c59fba618a7cf6850a253bd65c0edc532fa67bdde74c9c8c4f1692282ae59bf2`

At the last recheck, concurrent archive/ledger activity had moved `archive-2.html` to `d13fbb3f157c9533ae06bca6a74bff7cb0bd3a9ef7cd538ca9b540efb4000ef7` and `queue_ledger.jsonl` to `b92adc4577fa6a7c42f6be9e89913822c034e262c44dd5f9d2522ce48d1ddee4`. The one seq-20 publish row persisted. The rebuilt `archive-2.html` still had zero `20260820T231235` occurrences and now had no `VALUE(words)` hit at all; the earlier six pre-crossing hits are bound to the `b162…` bytes above.

Historical pins additionally checked: replacing the corrected report caption in memory with the preserved corrupt caption exactly reconstructs old report-page SHA-256 `c5d5d5b81f5ae997e239203d2cd8e7e6c3065dc043069830ba138a29b9f6e9e7`. The old archive bytes at pin `36a0499615eb74ca1fdacf7338084d9744891f34025630bb833a2e2e78710178` are no longer present at the mutable live path and were not independently reconstructed.

### Lane-local temporary evidence reviewed

- `_tmp_gate_r6memo_asr_base.json` — `166a9d4d833c149eb0ee6bd35a6d952edd174884cea519114c91595309ff7edd`
- `_tmp_gate_r6memo_disclosure_fresh.json` — `856454c5d675fcfd10cd6478f26ca2fa7605c7c0ce1e7b059de6b43d8b8771dd`
- `_tmp_gate_r6memo_mode_probe` — initial `25718360e05d3c2d0963d1381e9dd4dae5fca789244ee4b9f861adcc0cc96218`; mutated `57673254e78a37754096338ffc388492d4778b0e1c831193a3b781e7bd64cd30`
- `_tmp_gate_r6memo_ledger_probe.jsonl` — `f63d5d090bbc6c98ee37c9e7a0a0c154672b739647d1690efac3750a155858b1`
- `_tmp_gate_r6memo_selfsha_probe.py` — final `87979893c6debd31ec51d47db3b48c76de8b19a5665d64573be7dc1164b053d8`
- `_tmp_gate_r6memo_selfsha_probe.out` — `ba58610e975f7d4d833d75488b3eb7f4cca2571aac3df4eff39804d3173b8dd3`

## Evidence methods and limits

- SHA-256s were recomputed from bytes; prior-report hashes were used only as allegations until direct comparison.
- The generator was source-inspected before execution and run with stdout only to a permitted `_tmp_gate_r6memo_*` file.
- Memo fenced-block equality was tested byte-for-byte, not visually.
- Archive attribution was parsed per `<li data-src>` block, including each detector hit's report-stamp and `href` list.
- The disclosure script was source-inspected and freshly executed; publication rows were parsed from `queue_ledger.jsonl`.
- Fresh ASR ran in an isolated lane-local `uv`/Hugging Face cache and temporary directory, all named `_tmp_gate_r6memo_*`.
- The self-hash and mode/ledger attacks used only lane-local temporary probes; no live snapshot or live ledger was altered.
- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read.
- No source, target, snapshot, queue, archive, runtime, database, git state, or public artifact was changed by this gate. The only non-temporary write is this required report.
- The Blanc Markdown and status-audio text/HTML sources changed concurrently during the pass. Both observed ledger hashes are recorded; final observations are bound to the final hashes above. The pinned target remained unchanged.
