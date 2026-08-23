REFUTED_CHI_CUSTODY_EVIDENCE_V4

# Adversarial gate — `CHI_CUSTODY_20260822.md` v4 and `_evidence_20260822/verify.sh`

## Executive verdict

Both dispatched artifacts matched their pins before content review. The script ran twice with byte-identical output, including its self-digest; both runs produced 26 PASS rows and 0 FAIL rows. All `$P` and `$R` path prefixes were expanded to full literals in the printed commands, and all 26 complete displayed command strings reproduced their claimed values in clean zsh, bash, and sh tests with a standard PATH, including from another working directory.

The gate is nevertheless refuted. The document's fresh-shell copy-paste promise is broader than the mechanism: P1 is not one copyable printed line, and an exact printed command returns a different result in a clean shell whose PATH lacks `/usr/bin`. P3/P4 still do not bind the three-value phrase to the named report entry and accept a separated-record decoy; P3 also accepts malformed decimal separators. X1-X3 do not establish the prose inference that the gates reviewed earlier revisions. The Revision-8 omission accounting is incomplete and incorrectly says H2 carries the former condition-1 claim at the same strength. Q1 also leaves explicit arguing prose.

No remedy is proposed.

## Dispatch identity

Verified before either target was opened:

- `CHI_CUSTODY_20260822.md`: `d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7` — matches dispatch.
- `_evidence_20260822/verify.sh`: `c3d1d09f09fc0a41a3026d96c81f34dedc8111f5d425c79861bf747a98ebe2a8` — matches dispatch.

Filesystem metadata supports the document's dates but not its actor attribution: the current document's birth time is `2026-08-22 13:03:12 +0900` and mtime is `2026-08-23 14:55:21 +0900`. The words “un-parked by Duho” were not independently established from artifact bytes. The dispatch brief itself supplies the preceding-refusal count of thirteen.

## Ranked findings

### 1. BLOCKING — the fresh-shell copy-paste promise diverges even though the one-string identity holds

The narrow structural fact holds: `claim` evaluates `$2` and prints the same post-construction string, and no curated command label remains. The complete commands extracted from actual runtime output reproduced all 26 claimed values under:

- `/bin/zsh -f` from the prereg directory;
- `/bin/zsh -f` from `/Users/duhokim`;
- `/bin/bash --noprofile --norc`;
- `/bin/sh`;
- clean environment `HOME=/Users/duhokim PATH=/usr/bin:/bin:/usr/sbin:/sbin LC_ALL=C`.

The document promises more at lines 16–17: “copy a printed line after `$` and run it yourself.” P1's displayed command spans six physical lines. Copying its actual `$` line alone gives `python3 -c "`, which returned status 1, no stdout, and `zsh:1: unmatched "`; it does not return P1's claimed ledger value. Copying the full multiline block does work, but that is not the stated line-level interface.

The commands also depend on unprinted executable resolution. The exact displayed S1 command, run in a fresh zsh with `env -i HOME=/Users/duhokim PATH=/bin`, returned status 127 with `command not found: shasum` and `command not found: cut`, rather than `2a38a887bd897147`. Data-file paths are absolute, but executable paths and environment are not. This is a concrete fresh-shell divergent result of the kind the brief made dispositive.

The eval-time arithmetic and command substitution in G1 are printed as `$(( $(wc ...) - 1 ))`; they are not hidden, and they reproduced under the tested shells. No unexpanded `$P`, `$R`, `${P}`, or `${R}` survived in runtime output.

### 2. BLOCKING — P3/P4 remain two unbound global predicates

Current-state fact: `archive.html` has 42 `<li>` blocks; exactly one block contains the exact three-value phrase, the target report token, and `data-src="20260820T231235-hwao-report.mp3"`. The desired association happens to hold now.

The claims do not establish that association. A two-record decoy with the full phrase in one `<li>` and the target href in another produced P3=`1` and P4=`1`, while no block contained both. Thus P4 does not “tie that page to this report”; it only proves that the archive contains the href token somewhere.

P3 is also a regex, not a literal-string check. Its unescaped decimal points accepted `0X834336, 0Y384410, and -0Z640352` and returned `1`. The v4 answer to V3 finding 4 is therefore inadequate even though the current archive content is correct.

### 3. BLOCKING — the carried/not-carried section is incomplete, and H2 is not the same-strength replacement claimed

Document lines 59–64 say “nothing leaves unannounced,” then name four omitted classes. Direct comparison with Revision 8 found these material categories still absent and unannounced:

- `recorded_kst: 2026-08-20 23:12:35 KST` and the 52-minute relation to the 22:20 authorization;
- the `SOURCES SCANNED` inventory and `BLIND SPOTS` boundary;
- fresh-ASR clearance of the 23:12 report and the full three-divergence accounting;
- the withdrawal of the internal ledger chain as custody evidence and its external-witness limitation.

D1-D2 carry one of the three divergences, but they do not announce that the other two, the fresh-ASR result, or the sweep boundary were dropped.

The stated reason for dropping Revision 8's condition-1 prose is also false: “H2 carries the same strength alone.” Revision 8 reported two searches — no real-chi tertile artifact and no real-chi invocation of `nm_handcheck.py` found — with an explicit authorized-evidence boundary. H2 only recursively searches the static `handcheck/` tree for the literal path string `chi_dr10_south`. It does not search for a tertile artifact or an invocation record. The narrower final wording at v4 lines 69–70 is honest, but the omission-accounting sentence still overstates equivalence.

The v4 answer to V3 finding 5 therefore fails.

### 4. MAJOR — X3's primitive holds, but its advertised gate-history inference does not follow

X1 and X2 correctly print the two HOLD first lines. X3 correctly establishes that the exact 64-hex Revision-3 hash occurs on zero lines in each gate file; it returns `2`. Independent searches also found no 12-, 16-, or 32-character prefix of that hash in either current gate file.

That is all the pipeline establishes. It cannot establish absence of a truncated hash citation in general because it searches only the full hash; replacing a full hash with a 12- or 16-hex citation would leave X3 at `2`. More importantly, first-line verdicts plus absence of the current full hash do not prove “they reviewed earlier revisions.” A gate may review current bytes without printing their hash, and Revision 8 itself warned that citation is not review and that subject revision was not determinable from hash mentions alone.

Independent content review does support the historical conclusion: the re-gate explicitly identifies Revision 2 and pins it as `a9783371…`, while the first gate predates and quotes the original finding. But that conclusion comes from reading the gate bodies and revision history, not from X1-X3. The document presents it as the output of the replacement claims, so the answer to V3 finding 2 remains overstated.

### 5. MAJOR — S1-S4 are digest checks, not proof that all four files carry the disclosure content

The four digest prefixes are correct. The content description at lines 26–27 is not:

- the caption contains the exact value phrase, sign summary, and `2,725 galaxies measured`;
- the deck does not contain the exact value phrase or sign summary; two positive value substrings appear only in a `REJECTED slide` note, and the negative literal is absent;
- the alignment `times.json` contains none of the three values, the sign summary, or the 2,725 count.

S3/S4 pin files associated with the report, but their digests do not establish that those files carry the reader-facing disclosure. This does not undo the independently verified caption/report/archive disclosure or the ledger's audio-ASR correction record; it refutes the v4 block description.

### 6. MAJOR — Q1 is accurately described as a tripwire, but arguing prose survives

Q1's listed-token count is genuinely zero. The requested surviving arguing prose is document lines 3–8:

> “what DESCRIBES itself has lost thirteen times … What COMPUTES itself has not lost once … This revision moves the last remaining prose into the computing class.”

Removing those sentences loses no claim checked by the script. They are historical advocacy, and the last sentence is contradicted by the document's own extensive prose plus the uncomputed X3 inference and surface descriptions above. Lines 52–55 then argue that the defense is “the deletion of arguing prose” and that the prior refuted sentence “was the last”; that self-assessment is likewise not checked by Q1. The v4 answer to the prose-survivor attack fails at its expressly acknowledged lexical boundary.

## V3 finding closure table

| V3 finding | v4 answer | Adjudication |
|---|---|---|
| 1. Curated command labels | One command string is both printed and eval-run | NARROWLY HOLDS. All 26 complete printed commands reproduced under standard clean shells. The separate line-level/environment-independent copy promise fails. |
| 2. Unsupported two-gate sentence | Deleted; X1-X3 added | PARTIAL / OVERSTATED. First lines and exact-full-hash absence hold; “reviewed earlier revisions” does not follow from those predicates. |
| 3. P1 suppressed `backfilled: true` | P1 prints it; prose calls the row reconstructed | HOLDS. One matching row has `seq=20`, `stamp_kst=23:12:51`, `recorded_kst=23:12:35`, and `backfilled=true`; ledger line 1 says the ledger was later opened and backfilled from `queue.json`. The framing no longer presents it as contemporaneous custody. |
| 4. P3 plural/unattributed | Full phrase plus P4 href | FAILS. Current association holds, but separated records and malformed decimal separators pass the claims. |
| 5. Revision-8 omissions | Carried/not-carried section plus L1 | FAILS. L1's count is right; the omission list is not complete, and H2 is not same-strength condition-1 evidence. |

## Claim-by-claim adjudication

| Claims | Ruling | Independent result |
|---|---|---|
| S1-S4 | DIGESTS HOLD; DESCRIPTION PARTLY FAILS | Full hashes begin with all four prefixes. Deck/alignment do not carry the disclosed content as described. |
| S5-S7 | CURRENT FACTS HOLD | Exact caption phrase, sign summary, and 2,725 string each occur once. S5's regex remains wider than literal decimal matching. |
| F1/F4 | HOLD AS 16-HEX PREFIX CHECKS | Full hashes match the prefixes. |
| F2/F3 | HOLD | Each authorization substring occurs once. |
| G1 | HOLD | Independent CSV pass counted 208,407 data rows. |
| G2 | HOLD | Independent `math.fsum` recomputation gave variance `0.05798463739809634`, rounding to `0.057985`. |
| H1 | HOLD | AST inspection found one `_rank_tertiles` definition, line 279. |
| H2 | HOLD ONLY AT ITS PRINTED SCOPE | 31 regular files, 0 symlinks, 0 byte hits under `handcheck/`; it proves no broader execution/artifact claim. |
| X1-X2 | HOLD | First lines match. |
| X3 | PRIMITIVE HOLDS; PROSE INFERENCE FAILS | Full current hash absent from both files; pipeline returns 2. It does not identify what bytes were reviewed. |
| D1 | HOLD AS CAPTION FACT | Phrase occurs once. Revision 8 says the audio ends before it. No fresh ASR was run in this gate. |
| D2 | HOLD AS STORED FIELD | JSON coverage is numeric `0.9709`; it is not itself audio-content evidence. |
| P1 | HOLDS WITH HONEST QUALIFIER | Exactly one matching row; `20 2026-08-20 23:12:51 KST backfilled=True`. |
| P2 | HOLDS | Full current page hash is `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`. |
| P3-P4 | CURRENT FACTS HOLD; JOINT PROOF FAILS | Current target block contains both, but the claims are globally unbound; P3 is regex-broader than the stated string. |
| L1 | HOLDS | 11 predecessor forms: Revision-8 receipt, seven explicitly superseded receipt revisions, and v1-v3 superseded custody documents. Ten filenames contain `_SUPERSEDED`; the eleventh is the Revision-8 base-name predecessor. |
| Q1 | HOLDS LEXICALLY ONLY | Independent listed-token scan found zero; arguing prose survives. |

## Quotations, numbers, and final support statement

- Runtime claim count: 26 source invocations, 26 PASS rows, 0 FAIL rows.
- Two normal runs and the clean-environment run were byte-identical: SHA-256 `9acdbde1c9a312fc0284b71034c59ad20bf607857e077182adb0633cb850e384`; all stderr files were empty.
- K-8 line 49 bars “publication of any kind.” Condition 2 lines 32–33 bars “No sky statistic, no dipole, no summary over χ of any kind.” The caption contains the sign/count summary. The document's final §4/condition-2 breach statement is supported.
- K-8 contains the exact `Partial-tertile prohibition` and `No sky statistic, no dipole` strings once each.
- The one P1 row supports seq 20 and the two timestamps. The “reconstructed” framing is supported by `backfilled=true` and the ledger-open declaration.
- The current decision memo says `THIS IS A DRAFT`, says it has neither gate nor signature, and says the study has not been declined. The final status sentence is supported.
- D1's caption and D2's `0.9709` field are exact. The stronger audio-truncation statement is supported here only by Revision 8's recorded audit statement, not by fresh ASR.
- The exact archive association currently holds in one block; the finding is predicate adequacy, not current-content falsity.
- The current archive SHA-256 is `e763360e107af89283238fc74db3ebda15fc7ee46fdf2f6a6fe460b9ed11d7af`, confirming the predecessor's old whole-file digest is stale.

## Failed attacks / facts that held

- Both dispatch pins matched before review and still matched at the pre-report recheck.
- Two normal script executions were byte-identical, including the self-digest line.
- The clean standard-PATH execution from another working directory was byte-identical too.
- All 26 complete displayed commands reproduced in zsh, bash, and sh; no `$P`/`$R` token remained unexpanded.
- The one-string print/eval identity itself held; the refutation is the broader copy-interface/environment promise.
- P1 now exposes `backfilled=True`, and the accompanying reconstruction framing is honest.
- P3/P4's desired association actually exists in the current archive block.
- X1/X2 and the narrow full-hash-absence fact in X3 are true.
- G1/G2 independently reproduced to the stated precision.
- H2's allowed tree had no symlink escape and no literal hit.
- L1 independently counted 11 predecessor forms.
- Q1 independently found zero listed tokens.
- The final §4/condition-2 breach and unsigned-draft status statements survived source review.

## Evidence ledger

### Commands and probes

Read-only work included:

- pre-review and pre-report `shasum -a 256` checks of both dispatched artifacts;
- two `zsh _evidence_20260822/verify.sh` executions captured only to permitted `_tmp_gate_ev4_*` files;
- clean-environment execution with `env -i ... /bin/zsh -f` from another working directory;
- `cmp -s`, SHA-256, stderr-size, and source-claim-count checks;
- extraction of the actual printed command strings followed by clean zsh/bash/sh execution;
- an exact printed S1 command under clean `PATH=/bin` to test environment divergence;
- independent CSV/geometry, AST, no-follow handcheck inventory, JSONL, HTML-block, decoy, banned-token, surface-content, and omission-accounting probes;
- exact file metadata `stat` checks;
- read-only `git status` scoped to the task artifacts.

### SHA-256 ledger — 62 reviewed source artifacts

Aliases: `P` = dispatched prereg directory; `R` = `/Users/duhokim/HermesOps/reports/status-audio`.

#### Core and publication artifacts

- `d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7`  `P/CHI_CUSTODY_20260822.md`
- `c3d1d09f09fc0a41a3026d96c81f34dedc8111f5d425c79861bf747a98ebe2a8`  `P/_evidence_20260822/verify.sh`
- `e7900c1f7429b1ae91b8440cdfaad089175b4c1734033452e21112b34a0024f1`  `P/GATE_CHI_CUSTODY_EVIDENCE_V3_20260823.md`
- `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`  `P/K8_CROSSING_AUTHORIZATION_20260820.md`
- `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`  `P/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c`  `P/_evidence_20260822/geom.py`
- `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`  `P/_positions_20260820/positions_parent_20260820.csv`
- `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`  `P/GATE_FOOTPRINT_GEOMETRY_20260821.md`
- `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`  `P/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`
- `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`  `P/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`
- `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`  `P/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `P/CHI_CUSTODY_RECEIPT_20260821.md`
- `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`  `R/20260820T231235-hwao-report.mp3`
- `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`  `R/20260820T231235-hwao-report.txt`
- `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`  `R/20260820T231235-hwao-report.deck.json`
- `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`  `R/20260820T231235-hwao-report.times.json`
- `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`  `R/report-20260820T231235-hwao-report.html`
- `e763360e107af89283238fc74db3ebda15fc7ee46fdf2f6a6fe460b9ed11d7af`  `R/archive.html`
- `5b7ef6b9593a741738407271827e11e5757e83b7a913dc00df06d69e50653b2d`  `R/queue_ledger.jsonl`
- `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`  `R/20260821T151843-hwao-report.txt`
- `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848`  `R/20260821T151843-hwao-report.times.json`

#### L1 predecessor forms

- `2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866`  `P/CHI_CUSTODY_20260822_V1_SUPERSEDED.md`
- `3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d`  `P/CHI_CUSTODY_20260822_V2_SUPERSEDED.md`
- `1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29`  `P/CHI_CUSTODY_20260822_V3_SUPERSEDED.md`
- `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e`  `P/CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md`
- `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c`  `P/CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md`
- `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093`  `P/CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md`
- `acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b`  `P/CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md`
- `2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65`  `P/CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md`
- `5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043`  `P/CHI_CUSTODY_RECEIPT_20260821_REV6_SUPERSEDED.md`
- `879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e`  `P/CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md`

Revision 8 itself is already listed in the core group and is L1's eleventh predecessor.

#### H2 traversal set — 31 regular files

- `db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f`  `P/handcheck/OPERATING_INSTRUCTIONS.md`
- `ccb217287424bbac06e4bc6f3c6e3c8f54a300c5e2f0ed42e64896cca8bd8d18`  `P/handcheck/SELFTEST.md`
- `d5b2ce3a2d938d8baa88861f4f2983d8fcfedd7582d25ec9f7225835d2381697`  `P/handcheck/YUI_HANDCHECK_HARNESS_20260814.md`
- `9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8`  `P/handcheck/hc1h_full_test_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `P/handcheck/hc1h_full_test_stdout.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `P/handcheck/hc1h_independent_stderr.log`
- `51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb`  `P/handcheck/hc1h_independent_stdout.log`
- `19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8`  `P/handcheck/hc1h_independent_verification.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `P/handcheck/hc1h_selftest_stderr.log`
- `a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b`  `P/handcheck/hc1h_selftest_stdout.log`
- `25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40`  `P/handcheck/hc1h_synthetic_selftest_receipt.json`
- `15f48274ccf81d476a3a92c2241a279dfe4b098d018a83e68368d2ad0000936e`  `P/handcheck/independent_verify_hc1h.py`
- `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4`  `P/handcheck/nm_handcheck.py`
- `2698ab1768656649c881a862d70f72011464f4614923391e6bd5e5dc8339f206`  `P/handcheck/run_hc1h_synthetic_selftest.py`
- `727aef49cbf2f0ac7e6bf29ab94b7d9154132e80a0833640c305d5ce71094382`  `P/handcheck/superseded_hc1_20260815/README.md`
- `ebe607be44c62c552a845f0cbdbdb5986fa5c7c0d53eff9bddd575a5c37ae4a5`  `P/handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `P/handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stdout.log`
- `148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b`  `P/handcheck/superseded_hc1_20260815/full_test_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `P/handcheck/superseded_hc1_20260815/full_test_stdout.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `P/handcheck/superseded_hc1_20260815/independent_stderr.log`
- `b4f51b589170659f0be7c6e38d93c81e35b13a13e4813ede694f9e9bf4a2de63`  `P/handcheck/superseded_hc1_20260815/independent_stdout.log`
- `54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae`  `P/handcheck/superseded_hc1_20260815/independent_verification.json`
- `c10ca1b5cc3f9e178e5551b4b48459f11f8fafbb0734ce4531af481f1e9aec98`  `P/handcheck/superseded_hc1_20260815/independent_verify.py`
- `9056ef22c89ea8e4606610948ac7b32b959c97ec42d3ea2597bdc4e71bb67ce7`  `P/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_receipt.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `P/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stderr.log`
- `29a592d8ed9c9c571ff96195e1313815a7cb3ece824fb67e9ae2d539779a1b1e`  `P/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stdout.log`
- `cc3c077ec613d4745ae7743cbc6e24a5b8a12e04efe361359560a07e5ef42821`  `P/handcheck/superseded_hc1_20260815/run_synthetic_selftest.py`
- `1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8`  `P/handcheck/superseded_hc1_20260815/synthetic_selftest_receipt.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `P/handcheck/superseded_hc1_20260815/synthetic_selftest_stderr.log`
- `e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab`  `P/handcheck/superseded_hc1_20260815/synthetic_selftest_stdout.log`
- `ffa2910edb610892f7ca742feb0756f3ed212bf79b48e58f8c2ee2bd5e97fc71`  `P/handcheck/test_nm_handcheck.py`

### Permitted temporary evidence hashes

- `9acdbde1c9a312fc0284b71034c59ad20bf607857e077182adb0633cb850e384`  `_tmp_gate_ev4_run1.out`
- `9acdbde1c9a312fc0284b71034c59ad20bf607857e077182adb0633cb850e384`  `_tmp_gate_ev4_run2.out`
- `9acdbde1c9a312fc0284b71034c59ad20bf607857e077182adb0633cb850e384`  `_tmp_gate_ev4_freshenv.out`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  each of `_tmp_gate_ev4_run1.err`, `_tmp_gate_ev4_run2.err`, `_tmp_gate_ev4_freshenv.err`, `_tmp_gate_ev4_independent.stderr`
- `e5c2cc6ea5a479ac54f84e2ff4a8e8662ecb0f1a6cd4712b151078ee8e7d74eb`  `_tmp_gate_ev4_copyprobe.py`
- `8866c5d6dcdb18d380bab8faf5c2381671d49f487db03de49506ee52ab29b3be`  `_tmp_gate_ev4_copyprobe.json`
- `ce89778d83b26276e6c42b39664f9b4caaf8f23389f13259de2c0c94bf5c71eb`  `_tmp_gate_ev4_independent.py`
- `6e373dbbe2b9a05ff584fe5ce54cbb592eedd827ef708ae008e78be4b484b3b1`  `_tmp_gate_ev4_independent.json`
- `16e21fe05c4d4256d2b57e43fec0d71f213fead595970898669f08e249e493ed`  `_tmp_gate_ev4_independent.stdout`

## Boundaries and uncertainty

- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read.
- No fresh ASR was run. Audio-truncation adjudication is explicitly limited to the existing Revision-8/ledger audit record.
- No external publication platform was inspected; publication custody was tested against the local ledger and current local served artifacts.
- No preregistration, source, gate, git state, database, process, or public artifact was changed.
- Writes were limited to this report and lane-local files beginning `_tmp_gate_ev4_`.
- Post-write verification found the first line to be the required single token, both dispatched source pins unchanged, and scoped git status showing only this report as untracked; the permitted `_tmp_gate_ev4_*` evidence files are ignored by the repository. `_tmp_gate_ev4_stdout.log` and `_tmp_gate_ev4_stderr.log` predated this pass's first temporary file and were names/stat-listed only, never opened or attributed to this gate.
