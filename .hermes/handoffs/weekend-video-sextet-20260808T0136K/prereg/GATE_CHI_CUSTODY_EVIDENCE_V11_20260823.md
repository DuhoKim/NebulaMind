REFUTED_CHI_CUSTODY_EVIDENCE_V11

# Adversarial gate — `CHI_CUSTODY_20260822.md` v11 and `_evidence_20260822/verify.sh`

## Executive verdict

The dispatched document and script matched their pinned SHA-256 values at opening, immediately before execution, and immediately before this report write. The exact advertised command, `zsh _evidence_20260822/verify.sh`, self-reported the pinned script digest, enumerated 28 unique claim invocations, printed 28 PASS and 0 FAIL, and exited 0. `/bin/zsh -f` independently did the same.

V11 is nevertheless refuted. D3's hard-coded-digest defect is closed exactly: the printed D3 command recomputes the current MP3 digest, an exact paste returned 2, and a same-path swap fixture changed the predicate from 2 to 0. The remaining class is **purpose/testimony-layer factual overreach**: the document's absolute statement that command-unsupported assertions live in Testimony “and nowhere else” is false. Multiple assertions remain outside Testimony, including unchanged V10 instances about delegated recomputation and served state; the script also prints semantic headings that exceed the predicates beneath them.

No remedy is proposed.

## Dispatch identity and custody

- `aa74f8786edf83c73e1a1e6772828267f37aadede349e3c0938326906580ff25`  `CHI_CUSTODY_20260822.md` — exact dispatch match.
- `b4aeac90cf253bcf5ea82dc00d70dc09867439dfc5436bcc5ba5bdfc02c748f4`  `_evidence_20260822/verify.sh` — exact dispatch match.
- `3575968dff87be6e536d54a7542d1f80c354b6560d59c5328197ff30392b028e`  `GATE_CHI_CUSTODY_EVIDENCE_V10_20260823.md` — named prior gate.
- `9f9ae01885f383c414999e19bedd8d9d0351f7a0609a267bad9bffe8a4f3d937`  `CHI_CUSTODY_20260822_V10_SUPERSEDED.md` — exact v10 document used for the v10→v11 diff.
- `6509bb14fee659adcbcd3c3571de84dd898f5b289e6318227be0a72237b47d7e`  `_custody_20260821/_gated/verify.sh.6509bb14fee6.md` — exact v10 script used for the v10→v11 diff.

## V10 finding-closure audit

| Assigned v11 answer | Result | Independent evidence |
|---|---|---|
| D3 hard-coded digest replaced by a run-time digest | **HOLDS EXACTLY** | The v10→v11 script diff changes only D3's hard-coded needle (plus revision/count text and L1's expected count) to `$(shasum ...)` inside the stored command string. The exact printed command pasted into zsh returned `2`. A same-path fixture returned `2` for content A and `0` after content B replaced it. |
| Printed command reproduces D3's coupling | **HOLDS EXACTLY** | The output prints the literal command substitution, not a pre-expanded digest. Pasting that one line recomputed `5ce21d…` from the current MP3 and found two lines in the current R7 gate. |
| Unsupported statements moved into Testimony and nowhere else | **FAILS** | `CHI_CUSTODY_20260822.md:23-24` makes that exclusivity promise, but lines 3-4, 31, 35, 37-39, 57-62, and 66 retain command-unsupported assertions. `_evidence_20260822/verify.sh:53,61,71` also prints semantic headings outside any Testimony label. |
| Testimony entries contradict checkable reality | **NO CONTRADICTION FOUND** | The final-round order is corroborated by the dispatch. Current R7 lines 91-96 bind the current MP3 digest to the ASR record and say the 23:12 values cleared. The earlier “values then in existence” wording exists in retained drafts. Blanc's message provenance and the archive's observed rebuild history remain unverified author testimony; no inspected artifact contradicts them. |

## Ranked findings

### 1. BLOCKING — Testimony is not the exclusive home of assertions the commands do not establish

The document says:

> Statements no command establishes live in the Testimony section and nowhere else.

That is refuted by the following surviving instances.

1. **Delegated recomputation semantics.** `CHI_CUSTODY_20260822.md:31` says G1-G2 “recompute two numbers from the positions file on each run.” G1 directly counts that file. G2 only prints and runs `python3 .../geom.py`; verify.sh neither pins nor displays `geom.py`'s implementation. The current `geom.py` is favorable and genuinely reads the CSV, but a permitted constant-output analogue with SHA-256 `4910284b…` printed the same expected `0.057985` while reading no positions. The predicate can therefore pass while the bullet is false. This is the same delegated-implementation class identified in V10.

2. **Served-state promotion and duplicated mutability testimony.** `CHI_CUSTODY_20260822.md:37-39` calls P1-P4 “the publication event and served pages” and calls `archive.html` mutable; lines 57-58 again say “served pages.” P1 reads a local ledger, P2/P3 read one local HTML file, and P4 reads a second local HTML file. A static scan found no HTTP URL, client, host, or service probe anywhere in verify.sh. The script itself prints `== publication event and served surfaces ==` at line 61. The archive's observed mutability is correctly labelled Testimony at document line 52, but line 39 repeats it as ordinary claim prose. These predicates can pass with no page being served and with no evidence of mutability.

3. **Author intent and divergence semantics outside Testimony.** `CHI_CUSTODY_20260822.md:35` says “my open divergence, unrepaired on purpose.” `_evidence_20260822/verify.sh:53` prints “my open divergence, left unrepaired on purpose.” D1 checks a caption phrase, D2 prints a timing-JSON field, and fixed D3 couples the current MP3 digest to two occurrences in R7. None establishes authorship, intent, or “left unrepaired.” The audio-side fact needed to call this a divergence is separately and correctly labelled Testimony at document lines 50-51, so the same semantic conclusion appearing outside Testimony defeats the claimed partition.

4. **History/provenance assertions exceed L1 and the other printed predicates.** `CHI_CUSTODY_20260822.md:3-4` says twenty refusals preceded v11, their reports are beside it, and L1 counts the forms those reports refuted. L1 prints only the count `18` for two filename globs; it does not inspect gate reports, verdict tokens, or a report→form relation. Lines 58-62 also assert Revision 8 history, a deliberate narrowing, Blanc-ledger record status, and reachability of republication rows. Those are not established by any claim command. The dispatch itself supplies the “twenty refusals” context, so this is not adjudicated as factually false; it is an uncoupled assertion under the pair's own stricter rule.

5. **The final breach conclusion is not command-complete.** `CHI_CUSTODY_20260822.md:66` says the publication breached §4's publication bar and condition 2. Independent reading supports the current conclusion: K-8 lines 46-50 bar publication, K-8 lines 32-33 bar summaries, and the caption contains the sign/count summary. But no command prints or searches §4's publication-bar text. F2 counts only the shorter `No sky statistic, no dipole` needle, S6 counts the caption string, and P1 prints a local ledger row. Thus the conclusion requires independent semantic reading beyond what the commands print, contrary to the document's stated claim boundary.

Class: **purpose/testimony-layer factual overreach**, with **delegated-implementation semantics** and **local-artifact-to-served-state promotion** as concrete subtypes.

## Claim-block adjudication

| Block | Result |
|---|---|
| S1-S4 | Current disclosed 16-hex SHA-256 prefixes pass. |
| S5-S7 | Current caption-string predicates pass. No audio-content inference is granted from them. |
| F1-F4 | Current prefixes and phrase-count predicates pass. “Rulings rest on” remains provenance prose, not command output. |
| G1-G2 | Current outputs pass and current `geom.py` genuinely recomputes. The bullet's recomputation guarantee is not coupled to G2's output predicate. |
| H1-H2 | Pass at the expressly narrow local grep scope. Before execution, `handcheck/` had 31 regular files and zero symlinks. |
| X1-X3 | Current first-line and digest-count predicates pass. |
| D1-D3 | All pass. D3's run-time digest and swap sensitivity hold; purpose/divergence headings still exceed the commands. |
| M1 | Passes exactly; current line 5 is the DRAFT banner. |
| P1-P4 | Current local ledger row, report-page prefix/count, and archive source-substring count pass. No served-state predicate exists. |
| L1 | Current command returns 18, and all 18 current matches are regular files. It does not establish report→refuted-form history. |
| Q1 | Current banned-wordlist count is zero. Its disclosed lexical blind spot remains a limit, not a separate finding. |

## Failed attacks and favorable current-state facts

- The dispatched pair remained hash-stable at opening, pre-execution, and pre-report.
- `zsh -n _evidence_20260822/verify.sh` exited 0.
- Static parsing found 28 claim invocations, 28 unique IDs, and no duplicates.
- Exact advertised execution: 28 PASS, 0 FAIL, exit 0.
- `/bin/zsh -f` execution: 28 PASS, 0 FAIL, exit 0.
- Static mechanism inspection confirms the same `$2` string is passed to `eval` and to `printf`; path variables are expanded while constructing that argument, while D3's escaped command substitution survives into the stored/printed string and expands only at eval or when pasted.
- Exact pasted D3 command returned `2`.
- D3 same-path swap fixture: content A SHA-256 `376ffa13…` produced `2`; after replacing it with content B SHA-256 `d0505d31…`, the unchanged command produced `0`. The fixture gate SHA-256 was `9cd77794…`.
- Current 20260821 MP3 full digest is `5ce21d…`; current R7 text contains it twice and records the relevant ASR result.
- Current `geom.py` reads the positions CSV and computes `s2/n - (s/n)**2`; current output is `0.057985`.
- P1's selected local ledger row remains unique and prints `1 20 2026-08-20 23:12:51 KST backfilled=True`.
- `handcheck/` had 31 regular files, zero symlinks, and the script contains zero occurrences of the forbidden absolute data-tree prefix.
- No inspected evidence contradicted the five explicitly labelled Testimony entries. Unverified testimony was not promoted to checked fact.

## Evidence ledger

### Commands and probes

Read-only work, except the three permitted `_tmp_gate_ev11_*` fixtures and this report, included:

1. Opening, pre-execution, and pre-report `shasum -a 256` checks for the dispatched pair; opening and pre-report checks for the named V10 gate.
2. Full reads of v11 document, v11 script, and V10 gate; exact v10→v11 document/script diffs against pinned v10 snapshots.
3. Full or targeted reads of K-8 authorization, current `geom.py`, R7 ASR context, decision-memo header, and both relevant captions.
4. SHA-256 over all explicit script inputs, both v10 snapshots, all 31 regular files in H2's traversal surface, and all 18 L1 matches.
5. Static claim-ID uniqueness, shell syntax, forbidden-prefix, local-symlink, and network/service-input scans.
6. Exact `zsh _evidence_20260822/verify.sh` execution.
7. Exact copy/paste execution of the printed D3 command.
8. `/bin/zsh -f _evidence_20260822/verify.sh` execution.
9. Same-path D3 swap-sensitivity fixture under `_tmp_gate_ev11_*`, with pre/post content hashes.
10. Constant-output G2 counterexample under `_tmp_gate_ev11_*`, executed and hashed.
11. Targeted retained-draft searches for the earlier “values then in existence” wording and Blanc/P1 provenance wording.
12. Read-only scoped `git status` checks before and after the report write.

### SHA-256 — principal reviewed artifacts and explicit inputs

```text
aa74f8786edf83c73e1a1e6772828267f37aadede349e3c0938326906580ff25  CHI_CUSTODY_20260822.md
b4aeac90cf253bcf5ea82dc00d70dc09867439dfc5436bcc5ba5bdfc02c748f4  _evidence_20260822/verify.sh
3575968dff87be6e536d54a7542d1f80c354b6560d59c5328197ff30392b028e  GATE_CHI_CUSTODY_EVIDENCE_V10_20260823.md
9f9ae01885f383c414999e19bedd8d9d0351f7a0609a267bad9bffe8a4f3d937  CHI_CUSTODY_20260822_V10_SUPERSEDED.md
6509bb14fee659adcbcd3c3571de84dd898f5b289e6318227be0a72237b47d7e  _custody_20260821/_gated/verify.sh.6509bb14fee6.md
26b2b949bdc85bd029f6a9fe8cdc06ad26795b3bd7ebac1bfea76fdc8af332e3  _custody_20260821/_gated/CHI_CUSTODY_20260822.26b2b949bdc8.md
6a1725ac26fbcff9b4b4852fd5e231b00d5256512ccc6b480e473d9cb6ff1eff  _custody_20260821/_gated/CHI_CUSTODY_20260822.6a1725ac26fb.md
aa74f8786edf83c73e1a1e6772828267f37aadede349e3c0938326906580ff25  _custody_20260821/_gated/CHI_CUSTODY_20260822.aa74f8786edf.md
c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69  K8_CROSSING_AUTHORIZATION_20260820.md
b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7  PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md
90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9  _positions_20260820/positions_parent_20260820.csv
3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c  _evidence_20260822/geom.py
1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1  GATE_FOOTPRINT_GEOMETRY_20260821.md
aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b  GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa  GATE_CHI_CUSTODY_R7_20260821.md
3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c  DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md
2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.mp3
2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt
1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.deck.json
a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.times.json
5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.mp3
fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.txt
bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.times.json
e940179cfe1da1d17cfe5be08c0f8145991dfc65b24374885d0ac229653a52db  /Users/duhokim/HermesOps/reports/status-audio/queue_ledger.jsonl
050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f  /Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html
c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb  /Users/duhokim/HermesOps/reports/status-audio/archive.html
376ffa13eebcb043ce7a1ccd5122f9f1843a25184c998ba5824fd477605c09a0  ephemeral `_tmp_gate_ev11_swap.mp3` content A
d0505d318866eb07a0e6eace7742a3defbf26522c16b64ce8bfd89940c3cd2ca  `_tmp_gate_ev11_swap.mp3` content B (current fixture)
9cd7779419a0d41339affc9d703c17f7171f93fbf7fa8e72bb69e1de08bca53b  `_tmp_gate_ev11_swap_gate.txt`
4910284bc4e9b6b73b0957241242c873bca9416b514c48abbd31699237a2d8ab  `_tmp_gate_ev11_geom_constant.py`
```

### SHA-256 — H2's complete local 31-regular-file traversal surface

```text
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
db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f  handcheck/OPERATING_INSTRUCTIONS.md
2698ab1768656649c881a862d70f72011464f4614923391e6bd5e5dc8339f206  handcheck/run_hc1h_synthetic_selftest.py
ccb217287424bbac06e4bc6f3c6e3c8f54a300c5e2f0ed42e64896cca8bd8d18  handcheck/SELFTEST.md
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
727aef49cbf2f0ac7e6bf29ab94b7d9154132e80a0833640c305d5ce71094382  handcheck/superseded_hc1_20260815/README.md
cc3c077ec613d4745ae7743cbc6e24a5b8a12e04efe361359560a07e5ef42821  handcheck/superseded_hc1_20260815/run_synthetic_selftest.py
1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8  handcheck/superseded_hc1_20260815/synthetic_selftest_receipt.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  handcheck/superseded_hc1_20260815/synthetic_selftest_stderr.log
e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab  handcheck/superseded_hc1_20260815/synthetic_selftest_stdout.log
ffa2910edb610892f7ca742feb0756f3ed212bf79b48e58f8c2ee2bd5e97fc71  handcheck/test_nm_handcheck.py
d5b2ce3a2d938d8baa88861f4f2983d8fcfedd7582d25ec9f7225835d2381697  handcheck/YUI_HANDCHECK_HARNESS_20260814.md
```

### SHA-256 — L1's complete 18-file match set

```text
7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e  CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md
efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c  CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md
9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093  CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md
acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b  CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md
2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65  CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md
5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043  CHI_CUSTODY_RECEIPT_20260821_REV6_SUPERSEDED.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e  CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md
c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74  CHI_CUSTODY_RECEIPT_20260821.md
2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866  CHI_CUSTODY_20260822_V1_SUPERSEDED.md
9f9ae01885f383c414999e19bedd8d9d0351f7a0609a267bad9bffe8a4f3d937  CHI_CUSTODY_20260822_V10_SUPERSEDED.md
3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d  CHI_CUSTODY_20260822_V2_SUPERSEDED.md
1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29  CHI_CUSTODY_20260822_V3_SUPERSEDED.md
d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7  CHI_CUSTODY_20260822_V4_SUPERSEDED.md
066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5  CHI_CUSTODY_20260822_V5_SUPERSEDED.md
0b12eaf43a0e35fb95eaadc2447663f226451442c0299bd9bd7609fcf352a766  CHI_CUSTODY_20260822_V6_SUPERSEDED.md
e61fd168adc8fb4fe78727483c1230e9d861fea92db9dd93e23401e811315671  CHI_CUSTODY_20260822_V7_SUPERSEDED.md
26b2b949bdc85bd029f6a9fe8cdc06ad26795b3bd7ebac1bfea76fdc8af332e3  CHI_CUSTODY_20260822_V8_SUPERSEDED.md
c6138ba1acedf2123270d1f4ef5e073df1ec7262e83f7c011978fb4da41d0d73  CHI_CUSTODY_20260822_V9_SUPERSEDED.md
```

## Boundaries and uncertainty

- Nothing under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, hashed, or read. H2 searched only for that literal inside local `prereg/handcheck/`, after a non-following local inventory found zero symlinks.
- No fresh ASR was run. Audio testimony was attacked against the existing R7 record and current MP3 digest only.
- No external publication platform, HTTP service, or live route was inspected. That deliberate limit is also why the pair's “served” wording remains unsupported.
- The only temporary writes were `_tmp_gate_ev11_swap.mp3`, `_tmp_gate_ev11_swap_gate.txt`, and `_tmp_gate_ev11_geom_constant.py`, all under the permitted prefix.
- No source artifact, claim input, database, process, git state, public surface, cockpit, or protected data tree was changed. The only intentional persistent deliverable is this report.
- No remedy is proposed.
