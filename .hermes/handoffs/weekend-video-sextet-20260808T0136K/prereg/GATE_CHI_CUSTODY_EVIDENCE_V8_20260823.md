REFUTED_CHI_CUSTODY_EVIDENCE_V8

# Adversarial gate — `CHI_CUSTODY_20260822.md` v8 and `_evidence_20260822/verify.sh`

## Executive verdict

The dispatched document and script matched their pinned SHA-256 values at opening and immediately before this report was first written. The script executed 28 unique claim IDs with 28 PASS, 0 FAIL, and exit 0. Several intended withdrawals also hold in the dispatched bytes and contemporaneous sources: P1 uses full-filename equality and exposes the full exact-row count first; M1 prints line 5; the dedicated report page contains exactly one value-literal occurrence and is the same path P2 hashes; the archive contains exactly one exact report-page href.

A post-write custody check found both named target paths changed concurrently: the document became `c6138ba1acedf2123270d1f4ef5e073df1e7e2e70f5768ccc2484e26abd52503` at 16:23:20 KST and the script became `5ccf5eef957bc19f052c75ffa0d039d0c47542b4d408f0b106885ae1052ab5ea` at 16:22:58 KST. Those replacement bytes were not opened and did not affect this exact-pin verdict. All target line references and content findings below bind only the dispatched `26b2b949...` / `d5be06cc...` bytes.

The pair is nevertheless refuted. The HTML-parser withdrawal was inserted without deleting the superseded X/D/P prose: v8 defines X1-X3, D1-D3, and P1-P4 twice, and its second P block still says P3/P4 parse `archive.html` with an HTML parser that the v8 script does not contain. The second D block likewise restores the stronger claim that the two digest occurrences are specifically “its finding and its evidence ledger,” contradicting the new caveat that the count ties documents, not content. Independently, P4 does not count an href at all; it counts matching lines containing a bare basename in a mutable, unpinned page. Plain text or script data false-passes with zero hrefs, and two hrefs on one line also return the expected `1`. The claimed withdrawal therefore both remains textually incomplete and loses the archive-link evidence the retained prose still names.

No remedy is proposed.

## Dispatch identity and custody

- `26b2b949bdc85bd029f6a9fe8cdc06ad26795b3bd7ebac1bfea76fdc8af332e3`  `CHI_CUSTODY_20260822.md` — exact dispatch match at opening and pre-report; live path later drifted to `c6138ba1...`.
- `d5be06cc1571c4f9e2edf31b4da12a5d6e5bdbb43585086aad2d4469928b084e`  `_evidence_20260822/verify.sh` — exact dispatch match at opening and pre-report; live path later drifted to `5ccf5eef...`.
- Named prior gate `GATE_CHI_CUSTODY_EVIDENCE_V7_20260823.md` was `33fae886649a425cb9c426e2ad881bd53c91574b74d0af8b6ed621688baf0651` when first read, then changed concurrently to `7337a7c6c84147fbfe938b71dc79cf417f2017553b0bead6b06cb0f9d1548b07`. Both states begin `REFUTED_CHI_CUSTODY_EVIDENCE_V7`; the later edit adds the target path's second v8 transition to v7's custody narrative. No v8 finding depends on that edit.
- `e61fd168adc8fb4fe78727483c1230e9d861fea92db9dd93e23401e811315671`  `CHI_CUSTODY_20260822_V7_SUPERSEDED.md` — the exact predecessor used for the v7→v8 diff.

## Ranked findings

### 0. BLOCKING — both exact-dispatch target paths mutated during the gate

The post-write hashes no longer equal either user-pinned dispatch hash. Only hashes, sizes, and mtimes of the replacements were inspected; their content was not opened. This is a path-custody failure separate from the pinned-byte content findings below.

### 1. BLOCKING — the parser withdrawal was added, not completed

The dispatched document contains two occurrences each of `- **X1-X3**`, `- **D1-D3**`, and `- **P1-P4**`. The exact v7→v8 diff shows the new D/P text inserted after the original X block while the old X/D/P text remained.

The contradictions are direct:

- `CHI_CUSTODY_20260822.md:44-50` says P3 reads the dedicated report page and P4 is page-global; `:60-65` says P3 and P4 parse `archive.html` with an HTML parser, select an exact `data-src` `<li>`, inspect rendered text, and count an exact href attribute.
- `_evidence_20260822/verify.sh:67-69` contains no parser. P2 hashes the dedicated report page, P3 greps that report page, and P4 greps the bare report basename in `archive.html`.
- `CHI_CUSTODY_20260822.md:40-42` candidly says D3's two occurrences tie the documents, not the content; `:55-59` again says the two occurrences are “its finding and its evidence ledger.” D3 itself remains only `grep -c DIGEST GATE_FILE`.
- X1-X3 is repeated verbatim at `:34-37` and `:51-54`.

Thus the v7 parser and D3-semantic findings were not answered by withdrawal in the artifact being gated. The document is internally inconsistent about what its script does.

### 2. MAJOR — P4's printed predicate does not establish an href

P4 is:

`grep -cF 'report-20260820T231235-hwao-report' archive.html`

`grep -c` counts matching lines, not href attributes and not literal occurrences. Exact in-memory fixtures run through the same command produced:

| Fixture | P4 output | exact href count |
|---|---:|---:|
| plain text containing the basename | `1` | `0` |
| `<script>` data containing the basename | `1` | `0` |
| two exact hrefs on one line | `1` | `2` |

The current archive happens to hold one basename occurrence, on one line, as exactly one `href="report-20260820T231235-hwao-report.html"`; its SHA-256 is `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`. That current-state fact was established independently, not by P4's claimed href predicate. Because the document explicitly treats the archive as mutable and does not pin its digest, a later non-href occurrence or two same-line hrefs can retain P4's expected output. Deleting entry binding was a legitimate narrowing; deleting href syntax from the check while still calling the result an href was not.

### 3. MAJOR — “one report per page” is a new unlisted generalisation, not a printed fact

`CHI_CUSTODY_20260822.md:47-49` says “one report per page” and uses that generalisation to say association is guaranteed “by construction” with no second entry able to hide a decoy. P2 and P3 inspect one named page only. They do not inspect a page generator or the report-page population, so they cannot establish the per-page generalisation.

For the exact pinned current page, independent byte inspection is favorable: the value literal occurs once, on one line; the page has one `<title>` and one `<audio>` element; P2 and P3 use the identical full path; and the full page SHA-256 is `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`. That supports the bounded sentence “this dedicated page contains the literal once.” It does not support “one report per page.” Q1 returns zero because “per” phrases the universal around its wordlist, exactly the limitation Q1 admits.

P3 has the same line-count abstraction as P4: a one-line fixture containing the exact value literal twice returns P3=`1`. P2's exact current-page pin and the independent actual occurrence count close that defect for these dispatched bytes, but the prose should not describe `grep -cF` generally as an occurrence counter.

## V7 finding / v8 withdrawal adjudication

| Assigned withdrawal | Adjudication | Evidence |
|---|---|---|
| 1. Remove the HTML parser; P3 uses the dedicated report page; P4 is page-global | **REFUTED as a document withdrawal; current P2/P3 object facts HOLD** | The new block exists at `:44-50`, but the old parser block remains at `:60-65`. Current report has exactly one literal occurrence and P2/P3 use the same path. |
| 2. P1 exact full filename; count all matching rows and print count first | **HOLDS** | One current exact row projects to `1 20 2026-08-20 23:12:51 KST backfilled=True`. Duplicating that exact row changes the projection's first value to `2`, so the claim fails closed. |
| 3. M1 prints line 5 at its position | **HOLDS EXACTLY** | M1 uses `sed -n 5p`; current memo line 5 is `> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.**`. |
| 4. D3 count ties documents, not content | **HOLDS in the new block; REFUTED document-wide** | `:40-42` is honest. The retained old block at `:55-59` restores the unsupported occurrence identities. Direct inspection confirms current occurrence 1 is the ASR finding (`GATE_CHI_CUSTODY_R7_20260821.md:93`) and occurrence 2 is the evidence ledger (`:540`), but D3's count does not establish those roles. |
| 5. Byline, multiline statement, interpolation sentence; sweep for staleness | **The three named repairs HOLD; new staleness FAILS** | Byline minute 16:10 matches document mtime 16:10:50 KST; only P1 is multiline; prefix interpolation wording is positive and the printed output shows expanded paths. The duplicated v7 blocks are new stale copy and contradict current code. |
| 6. Archive observed-tense; Q1 fired once during build | **Observed-tense wording is bounded; current Q1 HOLDS; prior firing unverified testimony** | “has rebuilt on index changes (Blanc)” is attributed observed tense, not a universal. Current Q1 prints `0`. The same sentence remains embedded in the stale parser paragraph, and Q1 misses the new “one report per page” generalisation. |

## Mechanism and current-state facts that survived attack

- `/bin/zsh -f _evidence_20260822/verify.sh` self-reported the exact dispatched script SHA, 28 claim invocations, 28 PASS, 0 FAIL, and exit 0.
- Static enumeration found 28 distinct IDs: `S1-S7,F1-F4,G1-G2,H1-H2,X1-X3,D1-D3,M1,P1-P4,L1,Q1`.
- The one-string display/eval mechanism remains: the command string passed as argument 2 is both printed and evaluated.
- P1 currently finds exactly one publish row with exact event and full filename equality. The selected row is sequence 20, stamp `2026-08-20 23:12:51 KST`, `backfilled=True`. An in-memory duplicate changes the leading count to `2`.
- P2 and P3 use `/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html`. Independent byte count finds the three-value literal exactly once.
- Current `archive.html` independently has exactly one bare-basename occurrence and exactly one exact report-page href. This current fact survives; P4's predicate description does not.
- M1 prints the current memo's literal line 5.
- Current R7 gate occurrence contexts are exactly the ASR finding at line 93 and the MP3 evidence-ledger row at line 540. The new D3 caveat correctly limits what its own count proves.
- L1's glob set has 15 distinct current members: seven document predecessors V1-V7 and eight receipt forms (current plus REV1-REV7 superseded).
- Q1 returns zero against the exact dispatched v8 document.
- The substantive bounded conclusion is independently supported: K-8 condition 2 bars any summary over χ (`K8_CROSSING_AUTHORIZATION_20260820.md:32-33`), §4 bars publication of any kind (`:46-50`), the exact ledger has the publish row, and the served report caption contains both the three values and the sign summary. This does not cure the document/script contract defects above.

## Evidence ledger

### Commands and probes

Read-only execution and probes included:

- opening and pre-report `shasum -a 256` over the dispatched document, script, and named prior gate;
- full reads of the dispatched document and script; full opening read plus current-state targeted reread of the named v7 gate;
- `/bin/zsh -f _evidence_20260822/verify.sh`;
- full read of the dedicated report page and K-8 authorization; targeted reads of the decision memo header and both D3 digest contexts in `GATE_CHI_CUSTODY_R7_20260821.md`;
- targeted searches in `archive.html`, the frozen preregistration, the K-8 authorization, the memo, and local gate/report references;
- Python byte-occurrence, line-occurrence, title/audio-element, and exact-href counts for the report and archive;
- Python exact-row parsing of `queue_ledger.jsonl` plus an in-memory duplicate-row pressure test;
- Python static exact-ID enumeration of `verify.sh`;
- Python in-memory P3/P4 fixtures executed through the system `grep -cF` binary; no fixture file was written;
- `git diff --no-index -- CHI_CUSTODY_20260822_V7_SUPERSEDED.md CHI_CUSTODY_20260822.md` (expected exit 1 because differences exist);
- L1 glob enumeration and SHA-256 over every regular member;
- SHA-256 manifest over all content-read or command-traversed regular files; local `handcheck/` was walked without following links and contained zero symlinks;
- read-only `stat`, `git status`, and branch checks. One attempted `git status` exclusion pathspec failed with an unsupported pathspec-magic parse error and made no change.

No adversarial fixture temp file was intentionally created by this pass; all fixtures were in memory. Lane-local runner logs that appeared under the permitted prefix are disclosed under boundaries below.

### SHA-256 manifest — principal artifacts and script inputs

The named v7 gate's two observed states are recorded above. The manifest below is the synchronized review cut after that concurrent change.

```text
1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.deck.json
2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.mp3
a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.times.json
2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt
5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.mp3
bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.times.json
fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.txt
c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb  /Users/duhokim/HermesOps/reports/status-audio/archive.html
e940179cfe1da1d17cfe5be08c0f8145991dfc65b24374885d0ac229653a52db  /Users/duhokim/HermesOps/reports/status-audio/queue_ledger.jsonl
050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f  /Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html
26b2b949bdc85bd029f6a9fe8cdc06ad26795b3bd7ebac1bfea76fdc8af332e3  CHI_CUSTODY_20260822.md
e61fd168adc8fb4fe78727483c1230e9d861fea92db9dd93e23401e811315671  CHI_CUSTODY_20260822_V7_SUPERSEDED.md
3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c  DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md
7337a7c6c84147fbfe938b71dc79cf417f2017553b0bead6b06cb0f9d1548b07  GATE_CHI_CUSTODY_EVIDENCE_V7_20260823.md
06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa  GATE_CHI_CUSTODY_R7_20260821.md
1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1  GATE_FOOTPRINT_GEOMETRY_20260821.md
aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b  GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69  K8_CROSSING_AUTHORIZATION_20260820.md
b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7  PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md
3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c  _evidence_20260822/geom.py
d5be06cc1571c4f9e2edf31b4da12a5d6e5bdbb43585086aad2d4469928b084e  _evidence_20260822/verify.sh
90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9  _positions_20260820/positions_parent_20260820.csv
```

### SHA-256 manifest — L1's 15 current members

```text
2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866  CHI_CUSTODY_20260822_V1_SUPERSEDED.md
3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d  CHI_CUSTODY_20260822_V2_SUPERSEDED.md
1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29  CHI_CUSTODY_20260822_V3_SUPERSEDED.md
d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7  CHI_CUSTODY_20260822_V4_SUPERSEDED.md
066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5  CHI_CUSTODY_20260822_V5_SUPERSEDED.md
0b12eaf43a0e35fb95eaadc2447663f226451442c0299bd9bd7609fcf352a766  CHI_CUSTODY_20260822_V6_SUPERSEDED.md
e61fd168adc8fb4fe78727483c1230e9d861fea92db9dd93e23401e811315671  CHI_CUSTODY_20260822_V7_SUPERSEDED.md
c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74  CHI_CUSTODY_RECEIPT_20260821.md
7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e  CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md
efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c  CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md
9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093  CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md
acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b  CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md
2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65  CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md
5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043  CHI_CUSTODY_RECEIPT_20260821_REV6_SUPERSEDED.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e  CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md
```

### SHA-256 manifest — H2's local 31-file traversal surface

```text
db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f  handcheck/OPERATING_INSTRUCTIONS.md
ccb217287424bbac06e4bc6f3c6e3c8f54a300c5e2f0ed42e64896cca8bd8d18  handcheck/SELFTEST.md
d5b2ce3a2d938d8baa88861f4f2983d8fcfedd7582d25ec9f7225835d2381697  handcheck/YUI_HANDCHECK_HARNESS_20260814.md
9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8  handcheck/hc1h_full_test_stderr.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/hc1h_full_test_stdout.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/hc1h_independent_stderr.log
51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb  handcheck/hc1h_independent_stdout.log
19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8  handcheck/hc1h_independent_verification.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/hc1h_selftest_stderr.log
a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b  handcheck/hc1h_selftest_stdout.log
25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40  handcheck/hc1h_synthetic_selftest_receipt.json
15f48274ccf81d476a3a92c2241a279dfe4b098d018a83e68368d2ad0000936e  handcheck/independent_verify_hc1h.py
65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4  handcheck/nm_handcheck.py
2698ab1768656649c881a862d70f72011464f4614923391e6bd5e5dc8339f206  handcheck/run_hc1h_synthetic_selftest.py
727aef49cbf2f0ac7e6bf29ab94b7d9154132e80a0833640c305d5ce71094382  handcheck/superseded_hc1_20260815/README.md
ebe607be44c62c552a845f0cbdbdb5986fa5c7c0d53eff9bddd575a5c37ae4a5  handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stderr.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stdout.log
148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b  handcheck/superseded_hc1_20260815/full_test_stderr.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/superseded_hc1_20260815/full_test_stdout.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/superseded_hc1_20260815/independent_stderr.log
b4f51b589170659f0be7c6e38d93c81e35b13a13e4813ede694f9e9bf4a2de63  handcheck/superseded_hc1_20260815/independent_stdout.log
54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae  handcheck/superseded_hc1_20260815/independent_verification.json
c10ca1b5cc3f9e178e5551b4b48459f11f8fafbb0734ce4531af481f1e9aec98  handcheck/superseded_hc1_20260815/independent_verify.py
9056ef22c89ea8e4606610948ac7b32b959c97ec42d3ea2597bdc4e71bb67ce7  handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_receipt.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stderr.log
29a592d8ed9c9c571ff96195e1313815a7cb3ece824fb67e9ae2d539779a1b1e  handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stdout.log
cc3c077ec613d4745ae7743cbc6e24a5b8a12e04efe361359560a07e5ef42821  handcheck/superseded_hc1_20260815/run_synthetic_selftest.py
1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8  handcheck/superseded_hc1_20260815/synthetic_selftest_receipt.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/superseded_hc1_20260815/synthetic_selftest_stderr.log
e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab  handcheck/superseded_hc1_20260815/synthetic_selftest_stdout.log
ffa2910edb610892f7ca742feb0756f3ed212bf79b48e58f8c2ee2bd5e97fc71  handcheck/test_nm_handcheck.py
```

### SHA-256 — incidental search matches excluded from exact-regate reasoning

A broad local identifier search surfaced these stale sibling/temp artifacts. They were not allowed to bind the verdict; their hashes are recorded because fragments appeared in search output.

```text
3c2cb2de4882fb0c7bb28f611d64f9316c96e80850acd90a92516d11ae29c9ec  GATE_CHI_CUSTODY_EVIDENCE_V2_20260822.md
42333ad73e67c1d16d6320acf36ad83a933c517b5ea554535f4fe2e570247a09  _tmp_GATE_BRIEF_EVIDENCE_V5.md
df52c2031b1508f27768710ece0ca7d7cf03b33c394159b7a00b4781d7af7532  _tmp_gate_r8_report_body.md
635ed8e6bda6b20fe8ae3283a8d89cbecb83037245981b96ff373a253dbd8b7a  _tmp_gate_r8_report_complete.md
```

## Boundaries and uncertainty

- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read. H2 searched only for the literal text `chi_dr10_south` inside local `prereg/handcheck/`; that local tree contained zero symlinks.
- No fresh ASR was run. Audio files were hashed only. D3's current underlying content was checked against the unchanged MP3 digest and the named R7 gate's existing ASR record.
- No external publication platform was inspected. Publication and served-surface checks are bounded to the local report tree and queue ledger.
- The prior Q1 firing during the build was not independently observable from current bytes; only the current zero result and current wording were verified.
- No source, reviewed artifact, database, process, git history, or published surface was changed by this pass. The only intentional write is this report. Concurrent external activity changed both named targets after the report was first written. Lane-local runner logs not intentionally created by this pass also appeared under the permitted prefix: `_tmp_gate_ev8_stdout.log` was active/mutable (`f352c8dc7fa792b141fa80abafe84f9235137cba93f56e9bfd4c9c201fd3b2d3` at the first identity cut; `ce0422a4893401b1a82b1de9fc302ce4bc2c3edce28e1cb64754502d039a3b2e` at the later verification cut), while `_tmp_gate_ev8_stderr.log` was empty (`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`). Only their names, stats, and hashes were inspected, not their contents.
- No remedy is proposed.
