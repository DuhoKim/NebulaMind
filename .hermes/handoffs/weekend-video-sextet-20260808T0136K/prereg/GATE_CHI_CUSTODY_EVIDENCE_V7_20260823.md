REFUTED_CHI_CUSTODY_EVIDENCE_V7

# Adversarial gate — `CHI_CUSTODY_20260822.md` v7 and `_evidence_20260822/verify.sh`

## Executive verdict

Both dispatched artifacts matched their pinned SHA-256 values before review and again immediately before this report was first written. The dispatched script ran 28 unique claims with 28 PASS, 0 FAIL, and exit 0. The current archive and ledger also contain the intended target records.

A post-report custody recheck then found both named target paths changed concurrently: the document became `6a1725ac26fbcff9b4b4852fd5e231b00d5256512ccc6b480e473d9cb6ff1eff` at 16:10:35 KST and changed again to `26b2b949bdc85bd029f6a9fe8cdc06ad26795b3bd7ebac1bfea76fdc8af332e3` at 16:10:50; the script became `d5be06cc1571c4f9e2edf31b4da12a5d6e5bdbb43585086aad2d4469928b084e` at 16:10:11. Those replacement bytes were not opened and are not part of this exact-pin gate. Every content finding below binds only the dispatched `e61fd168...` / `a097a647...` bytes reviewed before that drift.

The pair is nevertheless refuted. The new `HTMLParser` class still falsely associates sibling or post-list content with a target `<li>` whenever the target uses HTML's optional `</li>` end tag, and P3 counts non-rendered script/hidden data as “rendered text.” M1 does not print or locate a header; it only counts the sentence anywhere. D3's corrected count of two is factually right for the current R7 gate, but the count does not verify that either occurrence is an ASR finding. Three stale execution/metadata statements identified by v6 also remain unchanged.

No remedy is proposed.

## Dispatch identity

- `e61fd168adc8fb4fe78727483c1230e9d861fea92db9dd93e23401e811315671`  `CHI_CUSTODY_20260822.md` — exact dispatch match at opening and pre-report; live path later drifted through `6a1725ac...` to `26b2b949...`.
- `a097a64736163af4bad1c7a99cf70cc52913ed21e22f217e729561d1f704e49f`  `_evidence_20260822/verify.sh` — exact dispatch match at opening and pre-report; live path later drifted to `d5be06cc...`.
- `58f76c220d78bb453e7e259fb74728e30ba435b4687632dfaec82411a31a8eb2`  named prior gate `GATE_CHI_CUSTODY_EVIDENCE_V6_20260823.md`.

The Hwao coordinator pane showed that it had dispatched these exact v7 pins and was watching for this verdict before content review began; no duplicate gate was launched.

## Ranked findings

### 0. BLOCKING — the named dispatch paths mutated during the gate

The report file was first written at 16:10:02 KST. The script path changed at 16:10:11 and the document path at 16:10:35 and 16:10:50. Their later hashes no longer equal the user's dispatch pins. No content from the replacements was read or allowed to affect this verdict. This is direct path-custody failure in addition to the pinned-byte content refutations below.

### 1. BLOCKING — P3/P4 still false-pass outside the target `<li>`

The v7 class is not an HTML tree parser. It is a token callback with a counter that starts at `1` on the target opener, increments on every later `<li>` opener while active, and decrements only on an explicit `</li>`. `HTMLParser` does not synthesize HTML's implicit list-item closes.

The copied-exact parser logic was run against two optional-end-tag fixtures:

| Fixture | v7 P3/P4 | html5lib target text/href | Result |
|---|---:|---:|---|
| target has no values; next sibling `<li>` has values/link; target omits `</li>` | `1 / 1` | `0 / 0` | false pass |
| target has no values; `</ul>` closes the list; later `<p>` has values/link | `1 / 1` | `0 / 0` | false pass |

The standards-oriented html5lib parse gave both optional-close fixtures the same single global missing-doctype diagnostic as the well-closed control; there was no additional optional-`</li>` error. In both DOMs the target was one distinct `<li>` and contained neither the phrase nor the href. The v7 counter remained active and consumed content that the HTML tree placed in a sibling or after the list.

Two additional parser-class false passes were reproduced:

- Duplicate attributes: `<li data-src="other.mp3" data-src="TARGET">...`. `dict(attrs)` keeps the last duplicate and v7 returned `1 / 1`; html5lib retained the first attribute, found zero target elements, and returned `0 / 0`. This is malformed HTML, as requested by the brief, but it demonstrates that “the `data-src` attribute EQUALS the filename” is not what the class necessarily tests.
- Rendered-text claim: P3's `handle_data` appends data under every descendant without excluding `<script>`, `<style>`, `<template>`, or a `hidden` subtree. A well-closed target with the exact phrase only inside `<script>` returned P3=`1`; a target with the phrase only in `<span hidden>` also returned P3=`1`. Those bytes are element data, not rendered text.

The present archive is not alleged to exploit these holes. It remained SHA-256 `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`; html5lib reported zero parse errors, exactly one target `<li>`, one phrase, one exact href, and no `hidden` descendant. Current-state association holds; predicate adequacy is refuted.

### 2. MAJOR — M1 neither prints nor header-binds the memo sentence

The document says twice that M1 “prints the decision memo's own header line” (`CHI_CUSTODY_20260822.md:69`, and the dispatch brief's asserted answer). The command is:

`grep -cF 'THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.' DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`

Its output is only `1`. The phrase visible in the printed command is a self-authored search needle, not source output. The predicate also searches the complete file, not a header line.

A permitted decoy with first line `# DECISION MEMO — SIGNED AND IN FORCE` and the draft sentence quoted once in its body returned the exact expected M1 value `1`. Thus M1 can pass while its “own header line” claim is false.

Direct current inspection does support the present memo status: SHA-256 `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`, line 5 is the quoted DRAFT sentence, and lines 6-9 say it has neither gate nor signature. The finding is the printed-command coverage claimed by the v7 pair, not current memo falsity.

### 3. MAJOR — D3's `2` is numerically right but does not verify an ASR record

The 1→2 update is factually correct for current `GATE_CHI_CUSTODY_R7_20260821.md` (SHA-256 `06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa`):

- line 93 is the finding: the MP3 digest is tied to beam-1 and beam-5 transcripts ending after “one galaxy at a time”;
- line 540 is the evidence-ledger row for the same MP3.

The live MP3 still has that full digest: `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3`.

D3 itself only runs `grep -c DIGEST GATE_FILE` and prints `2`. It does not output either context, search for ASR/transcript language, or pin the gate bytes. A permitted decoy containing the digest twice in statements explicitly unrelated to ASR returned the exact expected D3 value `2`. Therefore D3 proves “this mutable path contains this digest twice,” not the document's substantive sentence that the gate is the ASR record establishing truncation.

Current direct evidence supports the truncation sentence. The v7 command does not back it to the level the prose claims.

### 4. MAJOR — three v6 execution/metadata defects remain unchanged

The v6-to-v7 document diff shows that these prior findings were not edited:

1. `CHI_CUSTODY_20260822.md:12-13` says “P1 and P3 are multi-line python.” Static enumeration of the v7 script finds three multiline Python claims: `P1,P3,P4`.
2. `CHI_CUSTODY_20260822.md:17-18` says the claim strings carry “no runtime interpolation beyond the two path prefixes.” G1 is literally `echo $(( $(wc -l < ...csv) - 1 ))`, so eval-time arithmetic and command substitution occur beyond prefix expansion.
3. The byline still says `Hwao, v7, 2026-08-23 14:55 KST`. The prior v6 gate was written at 15:49 KST, the v7 script at 15:51:00, and the v7 document at 15:51:38. The v6-to-v7 diff changed only the revision token and refusal count on this line, not the stale time.

Q1 returns zero despite the false broad statement “no runtime interpolation beyond...”; `no` is an unlisted generalisation around the wordlist. The document also states that the mutable archive “rebuilds on each index change,” another universal claim not tested by Q1 or any printed command. Q1 candidly says it cannot catch such phrasing, but that disclaimer does not make the unverified prose executable evidence.

The requested visible metadata updates do hold: the title is v7, the byline says v7/sixteen, and the script header says v7/sixteen. The stale sweep fails beyond those two tokens.

## V6 finding closure

| V6 finding / v7 answer | Adjudication | Evidence |
|---|---|---|
| P3/P4 changed from raw slicing to `HTMLParser` | **REFUTED** | Exact-logic optional-`</li>` fixtures and duplicate-attribute fixture false-pass; P3 also counts non-rendered script/hidden data. |
| P1 changed from substring filename to full equality | **HOLDS** | Source uses exact equality. Current ledger has one exact row and one substring row, the same row; an unrelated `unrelated-231235-decoy.mp3` does not match. |
| Audio sentence tied through D3 | **PARTIAL / INADEQUATE** | Current R7 contexts genuinely contain finding + ledger, hence expected `2` is right; count-only D3 accepts two unrelated occurrences. |
| Memo sentence replaced by M1 | **PARTIAL / INADEQUATE** | Current memo's line 5 holds, but M1 outputs a count and accepts a body quotation under a contradictory header. |
| Stale metadata now v7/sixteen | **PARTIAL** | Title/count/script header corrected. Multiline-P4 omission, runtime-interpolation denial, and stale byline time remain. |

## D3 and L1 update adjudication

- **D3 expected 2:** arithmetic correction holds exactly; adequacy fails for the semantic reason in finding 3.
- **L1 expected 14:** holds exactly. Fourteen distinct matching regular files were hashed. The new member `CHI_CUSTODY_20260822_V6_SUPERSEDED.md` is SHA-256 `0b12eaf43a0e35fb95eaadc2447663f226451442c0299bd9bd7609fcf352a766`, byte-identical to the v6 document pin recorded by the named prior gate. The 13→14 update is not arbitrary tuning.

## Mechanism and current-state facts that held

- `/bin/zsh -f _evidence_20260822/verify.sh` while the path still matched the dispatch pin: self-reported the dispatch script SHA, 28 claim invocations, 28 PASS, 0 FAIL, exit 0.
- Static parsing found 28 unique IDs: `S1-S7,F1-F4,G1-G2,H1-H2,X1-X3,D1-D3,M1,P1-P4,L1,Q1`.
- The one-string display/eval construction remains present; no second curated claim label was found.
- Current `archive.html` has one valid target entry with one phrase and one exact href.
- Current `queue_ledger.jsonl` has one exact target publish row, projected as `(20, '2026-08-20 23:12:51 KST', True)`; the v6 substring decoy now fails.
- Comment and HTML-CDATA decoys returned P3/P4=`0/0`.
- Attribute-order changes returned `1/1`.
- `&#46;` entities in the three decimal points rendered to the exact phrase and returned `1/1`, consistent with parsed text semantics.
- A self-closing target returned `0/0`; html5lib treats the slash on non-void `<li>` differently, but this tested mismatch failed in the safe direction for the chosen fixture.
- L1's fourteen-member closure and the new exact v6 predecessor identity held.
- Direct inspection supports the current R7 ASR finding and current memo DRAFT header, although D3/M1 do not adequately print or bind them.

## Evidence ledger

### Commands and probes

Read-only execution and permitted probes included:

- `shasum -a 256 CHI_CUSTODY_20260822.md _evidence_20260822/verify.sh GATE_CHI_CUSTODY_EVIDENCE_V6_20260823.md` plus byte/line counts;
- full reads of the dispatched document, dispatched script, and named v6 gate;
- targeted read/search of `GATE_CHI_CUSTODY_R7_20260821.md` around both MP3-digest occurrences;
- first 30 lines of `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`;
- `/bin/zsh -f _evidence_20260822/verify.sh`;
- `git diff --no-index -- CHI_CUSTODY_20260822_V6_SUPERSEDED.md CHI_CUSTODY_20260822.md`;
- Python exact-ID/multiline-claim enumeration of `verify.sh`;
- Python exact/substr P1 enumeration against current `queue_ledger.jsonl` plus an in-memory unrelated-filename decoy;
- Python L1 glob enumeration, regular-file hashing, and exact predecessor comparison;
- `_tmp_gate_ev7_parser_probe.py`: copied v7 parser logic against well-closed control, optional-close sibling and container-end fixtures, duplicate attributes, comments, CDATA, entity dots, attribute order, self-closing `<li>`, script text, and hidden text; html5lib supplied an independent HTML-tree comparison;
- `_tmp_gate_ev7_current_archive_probe.py`: current archive SHA, parse errors, target count, phrase/href counts, descendant tags, and hidden-attribute count;
- exact D3/M1 grep predicates against `_tmp_gate_ev7_d3_decoy.md` and `_tmp_gate_ev7_m1_decoy.md`;
- pre-report SHA-256 manifest over every regular file opened or content-reviewed by the pass, including H2's local `handcheck/` traversal set;
- read-only `git status`, branch, stat/mtime, tmux pane inventory, and coordinator-pane capture.

One attempted isolated-browser corroboration did not run: Browser Use refused pending an interactive Chrome remote-debugging approval. No browser result was used. Its bootstrap reported installing 103 harness packages and creating managed workspace `/Users/duhokim/.hermes/cache/browser-use/workspace/f829b7ca-766b-4be5-a921-d7966923e3b6`; this is disclosed as the sole tool-managed write outside the permitted lane-temp prefix.

### SHA-256 — dispatched pair and principal reviewed sources

- `e61fd168adc8fb4fe78727483c1230e9d861fea92db9dd93e23401e811315671`  `CHI_CUSTODY_20260822.md` (reviewed dispatch bytes; live path later drifted)
- `a097a64736163af4bad1c7a99cf70cc52913ed21e22f217e729561d1f704e49f`  `_evidence_20260822/verify.sh` (reviewed dispatch bytes; live path later drifted)
- `58f76c220d78bb453e7e259fb74728e30ba435b4687632dfaec82411a31a8eb2`  `GATE_CHI_CUSTODY_EVIDENCE_V6_20260823.md`
- `06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa`  `GATE_CHI_CUSTODY_R7_20260821.md`
- `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`  `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`
- `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`  `K8_CROSSING_AUTHORIZATION_20260820.md`
- `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`  `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c`  `_evidence_20260822/geom.py`
- `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`  `_positions_20260820/positions_parent_20260820.csv`
- `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`  `GATE_FOOTPRINT_GEOMETRY_20260821.md`
- `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`  `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`

### SHA-256 — report surfaces and D1/D3 artifacts

- `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`  `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.mp3`
- `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`  `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt`
- `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`  `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.deck.json`
- `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`  `/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.times.json`
- `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`  `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html`
- `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`  `/Users/duhokim/HermesOps/reports/status-audio/archive.html`
- `e940179cfe1da1d17cfe5be08c0f8145991dfc65b24374885d0ac229653a52db`  `/Users/duhokim/HermesOps/reports/status-audio/queue_ledger.jsonl`
- `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3`  `/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.mp3`
- `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`  `/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.txt`
- `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848`  `/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.times.json`

### SHA-256 — L1's fourteen regular files

- `2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866`  `CHI_CUSTODY_20260822_V1_SUPERSEDED.md`
- `3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d`  `CHI_CUSTODY_20260822_V2_SUPERSEDED.md`
- `1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29`  `CHI_CUSTODY_20260822_V3_SUPERSEDED.md`
- `d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7`  `CHI_CUSTODY_20260822_V4_SUPERSEDED.md`
- `066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5`  `CHI_CUSTODY_20260822_V5_SUPERSEDED.md`
- `0b12eaf43a0e35fb95eaadc2447663f226451442c0299bd9bd7609fcf352a766`  `CHI_CUSTODY_20260822_V6_SUPERSEDED.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `CHI_CUSTODY_RECEIPT_20260821.md`
- `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e`  `CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md`
- `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c`  `CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md`
- `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093`  `CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md`
- `acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b`  `CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md`
- `2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65`  `CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md`
- `5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043`  `CHI_CUSTODY_RECEIPT_20260821_REV6_SUPERSEDED.md`
- `879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e`  `CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md`

### SHA-256 — permitted v7 probes

- `a0ea1aa432a84a8c9eb75c9ef0711727427ed4800d0b69236f9010786c9c501b`  `_tmp_gate_ev7_parser_probe.py`
- `2d360fb562f680b45afc0d99d98cbf8f1c99d69c508424dbeb139eecea71175b`  `_tmp_gate_ev7_current_archive_probe.py`
- `c8660f689848f40fbffcba192742a7a5ce0686b521f3bbf7b189cb2e774547aa`  `_tmp_gate_ev7_d3_decoy.md`
- `4155f3df309dd77d383f7198bbd91d40c2ca6e15b520d5e25eab3d89e2559d58`  `_tmp_gate_ev7_m1_decoy.md`

### SHA-256 — H2's local 31-file traversal set

- `db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f`  `handcheck/OPERATING_INSTRUCTIONS.md`
- `ccb217287424bbac06e4bc6f3c6e3c8f54a300c5e2f0ed42e64896cca8bd8d18`  `handcheck/SELFTEST.md`
- `d5b2ce3a2d938d8baa88861f4f2983d8fcfedd7582d25ec9f7225835d2381697`  `handcheck/YUI_HANDCHECK_HARNESS_20260814.md`
- `9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8`  `handcheck/hc1h_full_test_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `handcheck/hc1h_full_test_stdout.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `handcheck/hc1h_independent_stderr.log`
- `51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb`  `handcheck/hc1h_independent_stdout.log`
- `19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8`  `handcheck/hc1h_independent_verification.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `handcheck/hc1h_selftest_stderr.log`
- `a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b`  `handcheck/hc1h_selftest_stdout.log`
- `25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40`  `handcheck/hc1h_synthetic_selftest_receipt.json`
- `15f48274ccf81d476a3a92c2241a279dfe4b098d018a83e68368d2ad0000936e`  `handcheck/independent_verify_hc1h.py`
- `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4`  `handcheck/nm_handcheck.py`
- `2698ab1768656649c881a862d70f72011464f4614923391e6bd5e5dc8339f206`  `handcheck/run_hc1h_synthetic_selftest.py`
- `727aef49cbf2f0ac7e6bf29ab94b7d9154132e80a0833640c305d5ce71094382`  `handcheck/superseded_hc1_20260815/README.md`
- `ebe607be44c62c552a845f0cbdbdb5986fa5c7c0d53eff9bddd575a5c37ae4a5`  `handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stdout.log`
- `148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b`  `handcheck/superseded_hc1_20260815/full_test_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `handcheck/superseded_hc1_20260815/full_test_stdout.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `handcheck/superseded_hc1_20260815/independent_stderr.log`
- `b4f51b589170659f0be7c6e38d93c81e35b13a13e4813ede694f9e9bf4a2de63`  `handcheck/superseded_hc1_20260815/independent_stdout.log`
- `54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae`  `handcheck/superseded_hc1_20260815/independent_verification.json`
- `c10ca1b5cc3f9e178e5551b4b48459f11f8fafbb0734ce4531af481f1e9aec98`  `handcheck/superseded_hc1_20260815/independent_verify.py`
- `9056ef22c89ea8e4606610948ac7b32b959c97ec42d3ea2597bdc4e71bb67ce7`  `handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_receipt.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stderr.log`
- `29a592d8ed9c9c571ff96195e1313815a7cb3ece824fb67e9ae2d539779a1b1e`  `handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stdout.log`
- `cc3c077ec613d4745ae7743cbc6e24a5b8a12e04efe361359560a07e5ef42821`  `handcheck/superseded_hc1_20260815/run_synthetic_selftest.py`
- `1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8`  `handcheck/superseded_hc1_20260815/synthetic_selftest_receipt.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `handcheck/superseded_hc1_20260815/synthetic_selftest_stderr.log`
- `e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab`  `handcheck/superseded_hc1_20260815/synthetic_selftest_stdout.log`
- `ffa2910edb610892f7ca742feb0756f3ed212bf79b48e58f8c2ee2bd5e97fc71`  `handcheck/test_nm_handcheck.py`

## Boundaries and uncertainty

- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read. H2 searched only the literal text `chi_dr10_south` inside the local `prereg/handcheck/` directory.
- No fresh ASR was run. The current audio conclusion was verified only against unchanged MP3 SHA-256 and the named R7 gate's existing ASR record.
- No external publication platform was inspected. Publication/surface checks are bounded to the local report tree and ledger.
- No source, reviewed script, gate predecessor, database, process, git state, or published artifact was intentionally changed by this gate. Concurrent external writes changed both named target paths after the report was first written; only their hashes/mtimes were inspected after drift.
- Intentional writes were limited to this report and the four permitted `prereg/_tmp_gate_ev7_*` probes listed above.
- The failed Browser Use attempt caused the disclosed managed-cache bootstrap outside the lane-temp prefix before refusing interaction. No result from that attempt was relied upon, but literal full compliance with the temp-location boundary cannot be claimed.
- No remedy is proposed.