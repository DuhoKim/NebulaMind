REFUTED_CHI_CUSTODY_EVIDENCE_V9

# Adversarial gate — `CHI_CUSTODY_20260822.md` v9 and `_evidence_20260822/verify.sh`

## Executive verdict

The document and script matched the dispatched SHA-256 values at opening, immediately before execution, and immediately before this report write. `/bin/zsh -f _evidence_20260822/verify.sh` self-reported the pinned script digest, enumerated 28 claim invocations, produced 28 PASS and 0 FAIL, and exited 0. The v8 duplication/parser-prose defect is closed, P4 now implements the narrowly disclosed exact source-substring count, and the v7-gate concurrent edit recorded by v8 does not enter either v9 artifact or any v9 claim input.

The pair is nevertheless refuted. V8's separate finding that “one report per page, association by construction” is an untested generalisation survives verbatim in v9. The claims prose also says four companions were published and that the values are in the MP3 although S1-S4 only hash local files and no printed command checks either proposition. P3 still describes a literal count while executing a matching-line count, and H1 still promotes a grep needle to a Python-definition claim. These are description-to-command gaps of the class this gate was asked to attack.

No remedy is proposed.

## Dispatch identity and custody

- `c6138ba1acedf2123270d1f4ef5e073df1e7e2e70f5768ccc2484e26abd52503`  `CHI_CUSTODY_20260822.md` — exact dispatch match at opening, execution, and pre-report.
- `5ccf5eef957bc19f052c75ffa0d039d0c47542b4d408f0b106885ae1052ab5ea`  `_evidence_20260822/verify.sh` — exact dispatch match at opening, execution, and pre-report.
- `GATE_CHI_CUSTODY_EVIDENCE_V8_20260823.md` was `b923515d78cfa1ecd8ef952aea5c7fbccea127d969e6c4cc9f917fbfbe85909c` at opening and changed concurrently to `8bb16c0359a2c1708bbd2f96bfad52118ab2df61aae3267f79af7438beb73449` at 16:25:52 KST. Its first line remained `REFUTED_CHI_CUSTODY_EVIDENCE_V8`; targeted reread confirmed that its v7-gate digest record and v8 findings remained present. This prior-report self-update did not change the pinned v9 pair.
- `7337a7c6c84147fbfe938b71dc79cf417f2017553b0bead6b06cb0f9d1548b07`  `GATE_CHI_CUSTODY_EVIDENCE_V7_20260823.md` — current digest, stable across this pass.

## The three assigned v8 answers

### 1. Duplicate blocks / parser prose — structure repair HOLDS; semantic correspondence still FAILS

The eleven exact bullet labels each occur once:

`S1-S4, S5-S7, F1-F4, G1-G2, H1-H2, X1-X3, D1-D3, P1-P4, L1, M1, Q1`.

Static enumeration of the script found 28 invocations and 28 distinct IDs:

`S1-S7,F1-F4,G1-G2,H1-H2,X1-X3,D1-D3,M1,P1-P4,L1,Q1`.

The target document contains zero occurrences of `HTMLParser`, `data-src`, `rendered text`, or the former “parse archive.html” description. The exact v8→v9 diff shows one X block, one D block, and one P block after the rebuild. Every named command family in the claims section has corresponding claim IDs in the script.

That structural result does not establish that the prose describes only what those commands prove. Findings 1-4 below are the remaining semantic gaps.

### 2. P4 source-substring count — HOLDS EXACTLY at the disclosed narrow scope

P4 now executes Python `str.count` over the complete decoded archive source for the exact literal:

`href="report-20260820T231235-hwao-report.html"`

Current `archive.html` has SHA-256 `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`, one exact-literal occurrence, one bare full-basename occurrence, and one matching source line.

In-memory mutation matrix, using the exact `str.count` predicate:

| Fixture | P4 value | Adjudication against v9's stated literal-substring scope |
|---|---:|---|
| one exact double-quoted literal | 1 | pass |
| entity in `.html` (`&#46;`) | 0 | expected narrowing; not the same source literal |
| single-quoted href | 0 | expected narrowing; not the same source literal |
| whitespace around `=` | 0 | expected narrowing; not the same source literal |
| newline between `=` and quote | 0 | expected narrowing; not the same source literal |
| two exact literals on one line | 2 | fails closed against expected 1 |
| one exact literal plus one single-quoted semantic link | 1 | semantic link count is not claimed |
| the exact literal in a comment only | 1 | demonstrates why this is only a source-substring count, which v9 now expressly says |

Entities, quote changes, and attribute whitespace therefore defeat semantic-link equivalence but do not refute the narrow v9 statement. A second exact literal changes the result to 2. P4 no longer claims parsed-link or entry association evidence.

### 3. V7 concurrent-edit anomaly — DOES NOT AFFECT v9 inputs

V8 records that `GATE_CHI_CUSTODY_EVIDENCE_V7_20260823.md` changed from `33fae886...` to `7337a7c6...`. Its current digest is exactly the recorded later value:

`7337a7c6c84147fbfe938b71dc79cf417f2017553b0bead6b06cb0f9d1548b07`.

Neither the v7 gate filename nor that digest occurs in the v9 document or v9 script. L1's two filename patterns match custody receipts and superseded custody documents, not `GATE_CHI_CUSTODY_EVIDENCE_V7_20260823.md`. The v7 gate is not read by any of the 28 commands. The anomaly therefore has no dependency path into v9's pinned inputs or outputs.

## Ranked findings

### 1. BLOCKING — V8's “one report per page” generalisation survives unchanged

`CHI_CUSTODY_20260822.md:44-46` still says P3 establishes the literal in the same page and then adds “one report per page, association by construction.” P2 and P3 inspect one named page only. They do not inspect the page generator, the population of report pages, or a one-report invariant. The current page is favorable — one title opener, one audio opener, and one exact value-literal occurrence — but one instance cannot establish the general rule.

The exact Q1 regex run against `one report per page, association by construction` returns no match. Q1's disclaimer accurately admits this blind spot, but that does not supply evidence for the unlisted generalisation. V8 identified this exact gap; v9 retains it.

### 2. MAJOR — S1-S4 hash four local files but the prose asserts publication and MP3 content

`CHI_CUSTODY_20260822.md:22-24` calls the MP3, caption, deck, and alignment “the four files published as the 23:12 report,” calls deck/alignment “other published parts,” and says the values themselves are in the MP3 and caption.

S1-S4 only compute 16-hex SHA-256 prefixes at four local paths. S5 verifies the value string in the caption. P1 finds one exact publish row for the MP3; that row names the transcript, but no printed command checks the MP3's audible content. Independent current-ledger enumeration found:

| Exact filename | publish rows |
|---|---:|
| `20260820T231235-hwao-report.mp3` | 1 |
| `20260820T231235-hwao-report.txt` | 0 |
| `20260820T231235-hwao-report.deck.json` | 0 |
| `20260820T231235-hwao-report.times.json` | 0 |

The exact MP3 publish row carries a `transcript` field naming the caption, but no deck/alignment fields. The current dedicated page and archive source each reference the MP3 filename once and reference the caption/deck/alignment filenames zero times. This does not prove that the companions were never published elsewhere; it proves that the printed commands do not back the four-part publication claim. No fresh ASR or other content check connects S1's MP3 bytes to the three values.

### 3. MAJOR — P3 still counts matching lines, not literal occurrences

`CHI_CUSTODY_20260822.md:44-45` says “P3 counts the three-value literal.” P3 is `grep -cF`, which counts lines containing the literal. An exact `/usr/bin/grep -cF` in-memory fixture with the literal twice on one line returned `1`, the expected P3 value, while direct substring count was `2`.

The present P2-pinned page independently contains one literal on one matching line, so the current-page fact holds. The description-to-command contract does not: the predicate can pass with two same-line occurrences. P2's current digest freezes the favorable page only for this byte state; it does not change what P3 counts.

### 4. MAJOR — H1's grep needle does not establish a Python definition

`CHI_CUSTODY_20260822.md:31` says “the tertile ranker is defined there.” H1 only runs `grep -cF 'def _rank_tertiles' handcheck/nm_handcheck.py`. An exact grep fixture containing only `# def _rank_tertiles is intentionally absent` returned the expected value `1`.

Current direct inspection is favorable: `handcheck/nm_handcheck.py:279` is an actual `def _rank_tertiles(...)` statement, and its current SHA-256 is `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4`. The finding is predicate adequacy: H1 does not parse Python and does not hash that file inside the v9 script, so the printed search does not prove the semantic statement it is said to prove.

### 5. MINOR — P1's ownership attribution is not in the command or ledger row

`CHI_CUSTODY_20260822.md:42` calls P1 “the ledger owner's own predicate.” The predicate is text embedded in `verify.sh:62-66`. The selected ledger row records event/file/sequence/stamps/backfill and report metadata, but no predicate authorship. Exact filename equality, full matching-row count, count-first output, and `backfilled=True` all hold; the ownership attribution is unverified prose.

## Claim-block adjudication

| Block | Result |
|---|---|
| S1-S4 | Hash prefixes HOLD; publication/package and MP3-content prose FAILS |
| S5-S7 | Current caption-string presence HOLDS |
| F1-F4 | Current prefixes and exact-needle presence HOLD; K-8 lines 28-33 and 46-50 directly support the bounded condition-2/§4 reading |
| G1-G2 | HOLDS; G1 returned 208,407 and `geom.py` genuinely reads the positions CSV and recomputes the variance |
| H1-H2 | H2 narrow zero-search statement HOLDS; H1 semantic “defined” description FAILS despite favorable current code |
| X1-X3 | HOLDS at the printed first-line and zero-matching-line scope |
| D1-D3 | Current outputs HOLD; D3 is candidly bounded to a digest tie, and the current MP3 digest equals its needle |
| M1 | HOLDS EXACTLY; literal line 5 is printed |
| P1 | Exact-row predicate/output HOLDS; ownership attribution unverified |
| P2 | Current report-page prefix HOLDS |
| P3 | Current page fact HOLDS independently; general predicate description FAILS |
| P4 | HOLDS EXACTLY at source-literal scope |
| L1 | HOLDS; 16 distinct regular members currently match |
| Q1 | Current zero result HOLDS; it misses the surviving unlisted generalisation as disclosed |

## Failed attacks and current-state facts that survived

- Exact dispatch identity held throughout the content review and immediately pre-report.
- The script's one-string mechanism statically has 28 unique IDs and dynamically returned 28 PASS / 0 FAIL / exit 0.
- Each of the eleven claim-block bullet labels occurs exactly once; the v8 parser block and duplicate X/D/P blocks are gone.
- P4's entity, quote, and whitespace variants fail in the narrow direction v9 discloses; a second exact literal changes 1 to 2.
- Current report page: full SHA-256 `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`, one direct value-literal occurrence, one matching line, one `<title>` opener, one `<audio>` opener.
- Current archive: full SHA-256 `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`, one exact P4 literal and one bare full-basename occurrence.
- P1 has exactly one current full-filename publish row and exposes count, sequence, stamp, and backfill state.
- `geom.py` is not a hard-coded printer; it reads the named positions CSV and computes `s2/n - (s/n)**2`.
- H2's local traversal surface contains 31 regular files and zero symlinks; it cannot reach the forbidden tree through a local symlink in the current state.
- L1 resolves to 16 distinct current regular files.
- M1 prints the current memo's literal line 5.
- The current 20260821 MP3 SHA-256 equals D3's full digest needle, and the current R7 gate contains that digest on two lines. The stale `_tmp_gate_r8_repro` copy surfaced incidentally in one recursive search, was excluded from reasoning, and is byte-identical to the current R7 gate.

## Evidence ledger

### Commands and probes

Read-only work included:

- opening, execution-time, and pre-report SHA-256 checks for the dispatched pair;
- full reads of the v9 document, v9 script, named v8 gate, and named v7 gate;
- `/bin/zsh -f _evidence_20260822/verify.sh` with direct stdout and exit capture;
- exact bullet-label counts and static claim-ID enumeration;
- stale-parser token sweep and exact v8-superseded→v9 no-index diff;
- Python in-memory P4 entity/single-quote/whitespace/newline/duplicate/comment fixtures;
- exact `/usr/bin/grep -cF` in-memory P3 duplicate-on-one-line and H1 comment-only fixtures;
- Q1-regex probe against the surviving “one report per page” sentence;
- direct current queue-ledger exact-row enumeration and selected-row field inspection;
- direct report-page/archive literal, filename-reference, title, and audio counts;
- full read of `geom.py`, full read of K-8 authorization, and targeted source read around `_rank_tertiles`;
- current MP3 digest and R7-gate digest-context check;
- safe-tree symlink scan before running H2;
- SHA-256 manifests over the script's regular input/traversal set;
- read-only `git status`, stat/mtime, and branch checks.

No `_tmp_gate_ev9_*` probe was needed or deliberately created by this pass, and no output was intentionally redirected. Two lane-local runner logs nevertheless appeared under the permitted prefix while the pass was active. Only their names, stats, and hashes were inspected; their contents were not opened.

### SHA-256 — principal reviewed artifacts and claim inputs

```text
c6138ba1acedf2123270d1f4ef5e073df1e7e2e70f5768ccc2484e26abd52503  CHI_CUSTODY_20260822.md
5ccf5eef957bc19f052c75ffa0d039d0c47542b4d408f0b106885ae1052ab5ea  _evidence_20260822/verify.sh
b923515d78cfa1ecd8ef952aea5c7fbccea127d969e6c4cc9f917fbfbe85909c  GATE_CHI_CUSTODY_EVIDENCE_V8_20260823.md (opening state)
8bb16c0359a2c1708bbd2f96bfad52118ab2df61aae3267f79af7438beb73449  GATE_CHI_CUSTODY_EVIDENCE_V8_20260823.md (later current state)
7337a7c6c84147fbfe938b71dc79cf417f2017553b0bead6b06cb0f9d1548b07  GATE_CHI_CUSTODY_EVIDENCE_V7_20260823.md
2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.mp3
2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt
1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.deck.json
a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79  /Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.times.json
c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69  K8_CROSSING_AUTHORIZATION_20260820.md
b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7  PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md
90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9  _positions_20260820/positions_parent_20260820.csv
3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c  _evidence_20260822/geom.py
1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1  GATE_FOOTPRINT_GEOMETRY_20260821.md
aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b  GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.txt
bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.times.json
5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3  /Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.mp3
06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa  GATE_CHI_CUSTODY_R7_20260821.md
3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c  DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md
e940179cfe1da1d17cfe5be08c0f8145991dfc65b24374885d0ac229653a52db  /Users/duhokim/HermesOps/reports/status-audio/queue_ledger.jsonl
050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f  /Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html
c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb  /Users/duhokim/HermesOps/reports/status-audio/archive.html
06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa  _tmp_gate_r8_repro/GATE_CHI_CUSTODY_R7_20260821.md (incidental stale match; excluded)
```

### SHA-256 — lane-local runner logs, hash-only observation

```text
ce57fcc5235aabda849b485c214cbab11d39753eb7b53293b4c05ffed9d51363  _tmp_gate_ev9_stdout.log (8,067 bytes at 16:35:13 KST; potentially active)
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  _tmp_gate_ev9_stderr.log (0 bytes at 16:23:47 KST)
```

### SHA-256 — L1's 16 current members

```text
2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866  CHI_CUSTODY_20260822_V1_SUPERSEDED.md
3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d  CHI_CUSTODY_20260822_V2_SUPERSEDED.md
1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29  CHI_CUSTODY_20260822_V3_SUPERSEDED.md
d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7  CHI_CUSTODY_20260822_V4_SUPERSEDED.md
066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5  CHI_CUSTODY_20260822_V5_SUPERSEDED.md
0b12eaf43a0e35fb95eaadc2447663f226451442c0299bd9bd7609fcf352a766  CHI_CUSTODY_20260822_V6_SUPERSEDED.md
e61fd168adc8fb4fe78727483c1230e9d861fea92db9dd93e23401e811315671  CHI_CUSTODY_20260822_V7_SUPERSEDED.md
26b2b949bdc85bd029f6a9fe8cdc06ad26795b3bd7ebac1bfea76fdc8af332e3  CHI_CUSTODY_20260822_V8_SUPERSEDED.md
c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74  CHI_CUSTODY_RECEIPT_20260821.md
7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e  CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md
efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c  CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md
9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093  CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md
acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b  CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md
2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65  CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md
5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043  CHI_CUSTODY_RECEIPT_20260821_REV6_SUPERSEDED.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e  CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md
```

### SHA-256 — H2's local 31-file traversal surface

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

## Boundaries and uncertainty

- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read. H2 searched only for that literal text inside the local `prereg/handcheck/` tree; the pre-run local symlink count was zero.
- No fresh ASR was run. The 20260820 MP3's claimed audible values therefore remain unsupported by the printed commands. The separate 20260821 divergence was checked only by current MP3 digest plus the existing R7 gate contexts.
- No external publication platform was inspected. Publication and surface checks are bounded to the local queue ledger and report tree.
- An unrestricted local recursive digest search was not used. One targeted search for the D3 digest unintentionally returned the current R7 gate and a stale `_tmp_gate_r8_repro` copy; the stale copy was hashed, disclosed, and excluded from adjudication.
- No source, reviewed artifact, database, process, git history, or published surface was changed. The only intentional write is this report.
- The named v8 report changed concurrently during this pass; both observed digests are recorded. The pinned v9 document and script did not change.
- The two `_tmp_gate_ev9_*` runner logs appeared under the user-permitted prefix without a deliberate write by this pass. The stdout log may have been active; its digest is explicitly an observation at the stated size/mtime, not a stability claim.
- No remedy is proposed.
