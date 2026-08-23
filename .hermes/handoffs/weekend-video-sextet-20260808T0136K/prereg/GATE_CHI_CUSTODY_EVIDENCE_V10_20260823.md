REFUTED_CHI_CUSTODY_EVIDENCE_V10

# Adversarial gate — `CHI_CUSTODY_20260822.md` v10 and `_evidence_20260822/verify.sh`

## Executive verdict

The dispatched document and script matched their pinned SHA-256 values at opening, immediately before execution, and immediately before this report write. The exact advertised command, `zsh _evidence_20260822/verify.sh`, self-reported the pinned script digest, enumerated 28 claim invocations, printed 28 PASS and 0 FAIL, and exited 0. `/bin/zsh -f` independently did the same.

V10 is nevertheless refuted. The class is **purpose-layer factual overreach**: bullets labelled as purpose/limits still make provenance, artifact-linkage, delegated-computation, and served-state assertions that are not coupled to the printed predicates and can be false while those predicates pass. Most decisively, V9's explicit P1 ownership-attribution finding survives unchanged; D3 still counts a hard-coded digest only inside the gate report but says that count ties the gate to the current MP3 and its ASR meaning.

No remedy is proposed.

## Dispatch identity and custody

- `9f9ae01885f383c414999e19bedd8d9d0351f7a0609a267bad9bffe8a4f3d937`  `CHI_CUSTODY_20260822.md` — exact dispatch match at opening, pre-execution, and pre-report.
- `6509bb14fee659adcbcd3c3571de84dd898f5b289e6318227be0a72237b47d7e`  `_evidence_20260822/verify.sh` — exact dispatch match at opening, pre-execution, and pre-report.
- `e5f1364531a59a72d9d13ef45803492fd1ec7262e83f7c011978fb4da41d0d73`  `_custody_20260821/_gated/GATE_CHI_CUSTODY_EVIDENCE_V9_20260823.e5f1364531a5.md` — the immutable prior-gate snapshot named by the brief.
- `c6138ba1acedf2123270d1f4ef5e073df1e7e2e70f5768ccc2484e26abd52503`  `_custody_20260821/_gated/CHI_CUSTODY_20260822.c6138ba1aced.md` — v9 document snapshot used only for the exact v9→v10 diff.
- `5ccf5eef957bc19f052c75ffa0d039d0c47542b4d408f0b106885ae1052ab5ea`  `_custody_20260821/_gated/verify.sh.5ccf5eef957b.md` — v9 script snapshot used only for the exact v9→v10 diff.

## V9 finding-closure audit

| Assigned v10 answer | Result | Independent evidence |
|---|---|---|
| 1. Bullets are now purpose/limits only; hunt surviving paraphrase | **FAILS** | The disclaimer at `CHI_CUSTODY_20260822.md:22-23` is followed by factual descriptions including “recomputed,” “ties,” “ledger owner's own predicate,” “served pages,” “one hashes it, one counts,” “counts,” and “prints.” Findings 1-3 show assertions that can be false while their commands pass. |
| 2. “one report per page, association by construction” deleted | **HOLDS EXACTLY** | Exact phrase count is zero. The v9→v10 diff deletes it. P2 and P3 use the identical report-page path. |
| 3. S publication and MP3-content overclaim deleted/deferred | **PARTIAL** | The old “published as the 23:12 report” and “values themselves are in the mp3” phrases have zero occurrences. S1-S4 now say local files. But S5-S7/D3 still assert an R7-to-current-MP3/ASR tie that D3 does not establish; see Finding 2. |
| 4. P3 line-count replaced by literal-count | **HOLDS EXACTLY** | P3 now uses Python `str.count`. In-memory fixtures returned 1 for one occurrence, 2 for two same-line occurrences, and 0 for none. |
| 5. H1 semantic promotion removed | **HOLDS EXACTLY** | The old “tertile ranker is defined there” phrase has zero occurrences. V10 expressly disclaims code semantics beyond the matches shown. |
| V9 snapshot Finding 5: P1 ownership attribution unverified | **UNCHANGED / FAILS** | “P1 is the ledger owner's own predicate” survives verbatim at `CHI_CUSTODY_20260822.md:38`. The command and selected ledger row contain no predicate-authorship evidence. |

## Ranked findings

### 1. BLOCKING — V9's P1 ownership-attribution finding survives unchanged

`CHI_CUSTODY_20260822.md:38-39` says:

> P1 is the ledger owner's own predicate, count printed first.

P1 (`_evidence_20260822/verify.sh:62-66`) parses `queue_ledger.jsonl`, selects rows by exact `event` and `file`, then prints count, sequence, stamp, and backfill state. The current selected row is favorable and unique: `(20, '2026-08-20 23:12:51 KST', True, '20260820T231235-hwao-report.mp3')`. Its fields contain no owner, author, or predicate provenance, and the command does not inspect any such evidence.

The predicate therefore passes independently of who authored or owned it. This is the exact provenance-attribution gap already recorded in the immutable V9 snapshot at lines 102-104. Moving the statement under a purpose/limits disclaimer does not couple it to evidence.

Class: **purpose-layer provenance attribution**.

### 2. BLOCKING — D3's digest count does not tie the live MP3 to the gate or check the asserted ASR meaning

`CHI_CUSTODY_20260822.md:35-37` says the caption retains a phrase the audio lacks “per the R7 gate's ASR record” and that “D3 ties that gate file to the mp3 by digest count.” D3 (`_evidence_20260822/verify.sh:56`) is only:

`grep -c 5ce21d… $P/GATE_CHI_CUSTODY_R7_20260821.md`

It never opens or hashes `/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.mp3`. It also does not inspect what either matching line says. The current state is favorable under independent review: the MP3's full SHA-256 is the hard-coded needle, and R7 lines 91-94 say the caption has the phrase while the MP3 ASR ends before it. That favorable state is not D3's predicate.

An exact `grep -c` counterexample contained the digest on two lines while saying the audio **includes** the phrase. It returned stdout `2`, exit 0. The fixture content SHA-256 was `4fad057fa6433115f61b8cdcc7711bfc198bd50e746ac28198eed57625440c61`. Independently changing the MP3 would likewise leave D3 at 2 because the MP3 is not an input.

Class: **hard-coded-identifier bridge plus semantic-count overreach**.

### 3. MAJOR — other “purpose” bullets still promote delegated/local predicates to untested behavior or state

Two additional instances satisfy the brief's requested test: the bullet phrase could be wrong while its command passes.

1. `CHI_CUSTODY_20260822.md:30` says G1-G2 are “two numbers recomputed from the positions file on each run.” G1 directly counts the CSV. G2 only prints `python3 .../_evidence_20260822/geom.py`; verify.sh neither hashes nor displays `geom.py`'s implementation. The current `geom.py` was independently read and genuinely recomputes the variance from the CSV, so current behavior is favorable. But a constant-output analogue containing only `print("0.057985")` returned the expected output and exit 0 while reading zero positions; its SHA-256 was `4910284bc4e9b6b73b0957241242c873bca9416b514c48abbd31699237a2d8ab`.
2. `CHI_CUSTODY_20260822.md:38` characterizes P1-P4 as “the publication event and served pages.” P2 hashes a local HTML file; P3 reads that same local file; P4 reads local archive source. None probes a server, route, HTTP response, or external publication surface. Current local files and ledger state pass, but served state is not an input.

The issue is not that every bullet must reproduce shell syntax. It is that these factual purpose/status descriptions add predicates absent from the command's input surface.

Class: **delegated-implementation semantics and local-artifact-to-served-state promotion**.

## Claim-block adjudication

| Block | Result |
|---|---|
| S1-S4 | Current 16-hex SHA-256 prefixes pass; old four-part publication and MP3-content wording is deleted. |
| S5-S7 | Current caption-string presence passes; R7/current-MP3 linkage language is not established by D3. |
| F1-F4 | Current prefixes and phrase counts pass. “Two digests” is read conservatively as the two disclosed digest-prefix checks; no broader freezing inference is granted. |
| G1-G2 | Current outputs pass and current `geom.py` genuinely recomputes; the bullet's recomputation guarantee is not coupled to G2's output predicate. |
| H1-H2 | Pass at the expressly narrow grep scope. The semantic-definition promotion is closed. |
| X1-X3 | Pass at first-line and digest-search scope. |
| D1-D3 | Current outputs pass; the asserted file/ASR tie exceeds D3's input surface. |
| M1 | Passes exactly; current line 5 is the DRAFT banner. |
| P1-P4 | Current row/hash/literal counts pass; P1 ownership and served-state characterizations do not. |
| L1 | Current command returns 17; the 17 matching current regular files were independently enumerated and hashed. |
| Q1 | Current zero result passes. Its disclosed lexical blind spot remains a limit, not a separate finding. |

## Failed attacks and favorable current-state facts

- The dispatched pair and immutable prior-gate snapshot remained hash-stable through the pre-report check.
- Static parsing found 28 claim invocations, 28 unique IDs, and the expected 11 one-time bullet labels.
- `zsh -n _evidence_20260822/verify.sh` exited 0.
- Exact advertised execution: 28 PASS, 0 FAIL, exit 0.
- `/bin/zsh -f` execution: 28 PASS, 0 FAIL, exit 0.
- Static mechanism inspection confirms the same `$2` command string is passed to `eval` and to `printf`; path variables are expanded into that argument before both uses.
- P3 now fails closed on a second same-line literal: 2 rather than expected 1.
- P4 remains a candid exact source-substring predicate: one exact literal gives 1, two give 2, and a single-quoted semantic link gives 0.
- The old “one report per page,” four-part publication, MP3-values, and H1-definition phrases are absent.
- Current `geom.py` reads the positions CSV and computes `s2/n - (s/n)**2`; current output is `0.057985`.
- The current 20260821 MP3 full digest equals D3's hard-coded needle; current R7 text contains the relevant ASR finding and exactly two matching lines. This favorable independent fact does not repair D3's predicate.
- The current ledger has one exact P1 row; the report page has one value-literal occurrence; the archive has one exact P4 href literal.
- `handcheck/` had 31 regular files and zero symlinks before either verifier execution.
- The script contains zero occurrences of the forbidden absolute data-tree prefix.

## Evidence ledger

### Commands and probes

Read-only work, except the permitted ephemeral fixtures and this report, included:

1. `git status --short --untracked-files=all -- .` at opening.
2. `shasum -a 256` and `wc -l` for the dispatched pair and immutable V9 gate snapshot.
3. Full reads of v10 document, v10 script, and immutable V9 gate snapshot.
4. SHA-256 plus an in-memory unified diff for the v9 document/script snapshots versus v10.
5. SHA-256 over every explicit script input listed below.
6. Full or targeted reads of K-8 authorization, current `geom.py`, R7 gate contexts, footprint-gate first sections, decision-memo header, both relevant captions, and the 20260821 timing JSON.
7. Static shell syntax, claim-ID, bullet-label, and forbidden-prefix scans.
8. Exact current queue-ledger row selection and owner/author/predicate-field scan; exact report/archive occurrence counts.
9. Non-following `handcheck/` symlink and regular-file inventory, followed by SHA-256 of all 31 regular files.
10. SHA-256 of all 17 current regular files matched by L1.
11. Pre-execution pair hash check and exact `zsh _evidence_20260822/verify.sh` run.
12. Exact phrase-presence scan for claimed v9 deletions and surviving v10 statements.
13. Permitted `_tmp_gate_ev10_*` D3 and G2 analogue fixtures, executed and deleted in the same process; fixture content hashes are recorded above.
14. In-memory P3/P4 occurrence matrices.
15. `/bin/zsh -f` rerun with independently captured script exit and PASS/FAIL counts.
16. Pre-report SHA-256 check for document, script, and immutable V9 snapshot.
17. Read-only `git status` and deliverable-contract verification are reserved for the post-write check.

### SHA-256 — principal reviewed artifacts and inputs

```text
9f9ae01885f383c414999e19bedd8d9d0351f7a0609a267bad9bffe8a4f3d937  CHI_CUSTODY_20260822.md
6509bb14fee659adcbcd3c3571de84dd898f5b289e6318227be0a72237b47d7e  _evidence_20260822/verify.sh
e5f1364531a59a72d9d13ef45803492fd1ec7262e83f7c011978fb4da41d0d73  _custody_20260821/_gated/GATE_CHI_CUSTODY_EVIDENCE_V9_20260823.e5f1364531a5.md
c6138ba1acedf2123270d1f4ef5e073df1e7e2e70f5768ccc2484e26abd52503  _custody_20260821/_gated/CHI_CUSTODY_20260822.c6138ba1aced.md
5ccf5eef957bc19f052c75ffa0d039d0c47542b4d408f0b106885ae1052ab5ea  _custody_20260821/_gated/verify.sh.5ccf5eef957b.md
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
06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa  _tmp_gate_r8_repro/GATE_CHI_CUSTODY_R7_20260821.md (incidental bounded search hit; excluded from reasoning)
4fad057fa6433115f61b8cdcc7711bfc198bd50e746ac28198eed57625440c61  ephemeral D3 counterexample fixture content (deleted)
4910284bc4e9b6b73b0957241242c873bca9416b514c48abbd31699237a2d8ab  ephemeral G2 constant-output fixture content (deleted)
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  _tmp_gate_ev10_stdout.log (0 bytes at 16:36:59 KST; hash/stat only, not opened)
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  _tmp_gate_ev10_stderr.log (0 bytes at 16:36:59 KST; hash/stat only, not opened)
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

### SHA-256 — L1's 17 current regular-file members

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
3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d  CHI_CUSTODY_20260822_V2_SUPERSEDED.md
1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29  CHI_CUSTODY_20260822_V3_SUPERSEDED.md
d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7  CHI_CUSTODY_20260822_V4_SUPERSEDED.md
066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5  CHI_CUSTODY_20260822_V5_SUPERSEDED.md
0b12eaf43a0e35fb95eaadc2447663f226451442c0299bd9bd7609fcf352a766  CHI_CUSTODY_20260822_V6_SUPERSEDED.md
e61fd168adc8fb4fe78727483c1230e9d861fea92db9dd93e23401e811315671  CHI_CUSTODY_20260822_V7_SUPERSEDED.md
26b2b949bdc85bd029f6a9fe8cdc06ad26795b3bd7ebac1bfea76fdc8af332e3  CHI_CUSTODY_20260822_V8_SUPERSEDED.md
c6138ba1acedf2123270d1f4ef5e073df1e7e2e70f5768ccc2484e26abd52503  CHI_CUSTODY_20260822_V9_SUPERSEDED.md
```

## Boundaries and uncertainty

- Nothing under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, hashed, or read. H2 searched only for that literal string inside local `prereg/handcheck/`, after a non-following local inventory found zero symlinks.
- No fresh ASR was run. Current MP3/R7 linkage was checked by full current MP3 digest plus the existing R7 text, not by retranscription.
- No external publication platform or HTTP service was inspected. That deliberate limit is why “served pages” remains unverified by P2-P4.
- The broad first digest-context search incidentally surfaced `_tmp_gate_r8_repro/GATE_CHI_CUSTODY_R7_20260821.md`; it was hash-recorded, found byte-identical to the current R7 gate, and excluded from adjudication. The targeted rerun used only the current R7 path.
- The two permitted `_tmp_gate_ev10_*` counterexample fixtures were deleted in-process. Two separate zero-byte runner logs under the same permitted prefix were observed by name/stat/hash only and left untouched.
- No source, claim input, database, process, git state, published surface, or cockpit was changed. The only intentional persistent write is this report.
- No remedy is proposed.
