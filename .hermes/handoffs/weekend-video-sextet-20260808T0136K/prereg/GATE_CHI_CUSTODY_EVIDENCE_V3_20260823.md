REFUTED_CHI_CUSTODY_EVIDENCE_V3

# Adversarial gate — `CHI_CUSTODY_20260822.md` v3 and `_evidence_20260822/verify.sh`

## Executive verdict

Both dispatched artifacts matched their pins before content review. A fresh execution exited 0, line 1 reported the script's true current full SHA-256, line 2 reported the real static claim-invocation count of 21, and the run produced 21 PASS results and 0 FAIL results.

The gate is nevertheless refuted. The v3 repair claim that the output shows the literal commands is false on the current script; Q1 still passes a sentence that promotes the current Revision-3 footprint finding as having been held by two gates although the two named gates reviewed the original and Revision 2; and P3's one-value regex does not establish the stated plural, report-attributed archive-content claim. P1 also suppresses the source row's `backfilled: true` field while presenting the row as publication-event custody, and material Revision-8 evidence remains omitted without a complete acknowledgment ledger.

No remedy is proposed.

## Dispatch identity

Verified before either target was opened:

- `CHI_CUSTODY_20260822.md`: `1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29` — matches dispatch.
- `_evidence_20260822/verify.sh`: `46a2bcfe8b4432b6c59bba925fba5dd2739aaba88f7a923877d47609e37b667e` — matches dispatch.

## V2 finding 1 / v3 answer — self-digest and claim count hold; semantic quantifier repair does not

### Runtime self-identification — HOLDS

Fresh output began:

- `verify.sh sha256 46a2bcfe8b4432b6c59bba925fba5dd2739aaba88f7a923877d47609e37b667e`
- `claim invocations in this file: 21`

Independent checks found 21 source lines matching the script's own `^claim [A-Z][0-9]` rule and 21 runtime PASS rows. The companion document states neither value. This v3 answer is accurate on the dispatched bytes.

### Freeze-first formulation — NARROW REPAIR HOLDS

The old categorical claim that a document “cannot” contain a neighbouring script's digest is gone. The replacement at document lines 11–14 is accurate in its narrow custody sense: a digest recorded in a separate document remains current only while the target bytes do not change after the digest is recorded. On this execution, runtime self-hashing returned the actual current script hash.

The adjacent phrase `which does not break` is broader than the demonstrated one-run fact, but it is not needed for the blocking semantic survivor below.

### BLOCKING survivor: `contradicted by neither` promotes ungated Revision 3

Q1's literal wordlist count is genuinely 0. The wordlist nevertheless omits `only`, `neither`, `cannot`, and other scope operators. Document lines 69–70 say:

> `The footprint finding stands separately in HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md, held by two gates and contradicted by neither.`

The named live finding is Revision 3, SHA-256 `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`. The first gate, SHA-256 `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`, reviewed the original finding. The re-gate, SHA-256 `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`, explicitly reviewed Revision 2 and its own evidence ledger pins Revision 2 as `a9783371…`, not the live Revision-3 hash. Both gates returned HOLD, but neither is a hash-bound adjudication of the current Revision-3 artifact.

This is the requested sentence that generalises beyond its evidence without using a banned token. It was also named in the V2 gate and remains unrepaired.

The separate standing sentence `The study has not been declined` survived a manual source attack: the current decision memo, SHA-256 `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`, states that exact status at lines 5–9. It is outside `verify.sh`, but it was independently verified here and is not the refutation.

## V2 finding 2 / v3 answer — abbreviated paths resolve, but “literal command” custody is refuted

Script lines 17–22 declare that argument 2 is `the COMMAND ITSELF, shown verbatim`; the v3 brief likewise says descriptions are gone and literal commands are printed. Several current rows contradict that claim:

- S6 prints `grep -c 'One leaning each way...' 231235.txt`; the executed pattern is the full `One leaning each way among the confident pair`. The printed `...` is three regex wildcards, not an inert display ellipsis. A synthetic line `One leaning each way XYZ` returns count 1 under the displayed pattern.
- D2 prints `python3 read coverage from 151843.times.json`; that is English, not the executed `python3 -c ...` command.
- P1 prints `python3 read ledger publish row for 231235`; that is English and omits the executed predicate, first-match `break`, selected fields, and `backfilled` field.
- G2 appends `(recomputes from positions)` to a shortened invocation; it is commentary, not a verbatim command.
- Q1 prints placeholders `BANNED_WORDLIST` and `CHI_CUSTODY.md` rather than the executed regex variable, absolute document path, stderr suppression, and whitespace trimming.

The decimal patterns are also regexes, not literal-value tests. With no `-F` and no escaped dots, the displayed/executed S5 pattern accepts the synthetic line `0X834336, 0Y384410, and -0Z640352`; P3 accepts `0X834336`. Both decoy counts were 1.

The path-abbreviation attack itself failed: S1–S7 map to the intended `20260820T231235-hwao-report.*` files; F1–F3 use `A`, which is assigned to the exact K-8 authorization; F4 opens the exact frozen preregistration; G1/G2 use the named positions/geometry files; H1/H2 use the named `handcheck/` tree; D1/D2 map to `20260821T151843`; and P1–P3 use the intended ledger/report/archive sources. No short path was found to point at the wrong current source. The refutation is that the displayed strings are not consistently the literal commands or exact predicates v3 says they are.

## V2 finding 3 / v3 P1–P3 restoration

### P1 — primitive holds, but `backfilled: true` is a material omitted qualifier

There is exactly one current ledger row satisfying P1's predicate. It is physical line 21 of `queue_ledger.jsonl` and contains:

- `event: publish`
- `file: 20260820T231235-hwao-report.mp3`
- `seq: 20`
- `recorded_kst: 2026-08-20 23:12:35 KST`
- `stamp_kst: 2026-08-20 23:12:51 KST`
- `backfilled: true`

P1 prints only `20|2026-08-20 23:12:51 KST`. Because the row explicitly marks itself as backfilled, it is reconstructed ledger metadata rather than a contemporaneous append receipt. Current served surfaces corroborate current content, but the P1 output suppresses the field that qualifies the ledger's temporal custody. Ruling on the brief's question: yes, the publication-row claim materially requires the backfilled qualification; as written, “the publication event” overstates what this row alone establishes.

### P2 — current live digest HOLDS

The live file was opened and hashed during this gate rather than inherited from Revision 8 or V2:

`/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html`

Current full SHA-256:

`050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`

Its first 16 characters equal P2's `050a3f6245fc74f1`. The live file currently contains each of `0.834336`, `0.384410`, and `-0.640352` once. Its filesystem mtime is `2026-08-21T22:28:52+09:00`, earlier than the V2 report's `2026-08-22T14:04:38+09:00`; the metadata does not show that this particular report page was rewritten by glossary rounds 4–5. That does not weaken the current-byte result: P2 is current against the live file now.

### P3 — content-not-digest is the right evidence class for current mutable content, but this implementation is underpowered

Revision 8 recorded archive digest prefix `33c4c6c8db63ed27`; the current live archive is full SHA-256 `e763360e107af89283238fc74db3ebda15fc7ee46fdf2f6a6fe460b9ed11d7af`, with mtime `2026-08-23T14:39:34+09:00`, after V2. The volatility rationale is therefore real: a durable claim about current aggregate-page content should not require an old whole-file digest.

The current archive also genuinely holds the desired content. In the `<li>` block bound by `data-src="20260820T231235-hwao-report.mp3"`, all three values occur once and the block links to `report-20260820T231235-hwao-report.html`.

P3 does not establish that fact. It runs only `grep -c '0.834336' archive.html` and expects 1. It does not check the other two values, the exact three-value phrase, `data-src`, or the report-page `href`; because `.` is a regex wildcard, it does not even require the exact first decimal token. It could pass on a different report or malformed token. Content rather than digest is not an evasion in principle, but this one-token unbound predicate is an evasion of the plural, attributable content claim as written.

## Revision-8 evidence still dropped without acknowledgment

V3 explicitly acknowledges two classes of omission:

- archive digest custody is replaced by volatile current-content checking;
- Blanc's moving ASR/caption work is delegated to Blanc's ledger rather than copied.

V3 also restores six named surface checks in aggregate: S1–S4, P2, and P3. Subject to the P3 defect, that directly answers V2's missing-surface finding.

Material Revision-8 content remains absent without an explicit omission accounting:

1. `recorded_kst: 23:12:35 KST` and the claimed 52-minute relation to the 22:20 authorization are not stated or checked.
2. Revision 8's cross-report disclosure inventory (`SOURCES SCANNED`) and its `BLIND SPOTS` boundary are not carried into v3 or named as deliberately outside it.
3. Revision 8's withdrawal of the internal ledger chain as custody, and its distinction between that failed chain and external gate/git witnesses, are absent. V3 does not reassert chain validity, but its supersession statement does not acknowledge dropping this custody analysis.
4. The fresh-ASR clearance and three-divergence detail are absent from the executable block. This part is acknowledged rather than silent: v3 lines 59–62 point the reader to Blanc and state that no figure is copied.
5. Gate/refusal enumeration remains deliberately outside the script and is explained at v3 lines 49–57; that omission is acknowledged.

The unacknowledged omissions do not make the 21 narrow primitives false. They do refute any reading that P1–P3 fully restore the predecessor's publication custody rather than a narrower current-state subset.

## Claim-by-claim adjudication

| ID | Ruling | Independent result |
|---|---|---|
| S1–S4 | HOLDS AS 16-HEX PREFIX CHECKS | All four current full SHA-256 values begin with the printed prefixes. Short source aliases resolve correctly. |
| S5 | CURRENT FACT HOLDS; PREDICATE IS BROADER | The exact three-value phrase occurs once, but unescaped decimal dots accept malformed decoys. |
| S6 | CURRENT FACT HOLDS; DISPLAY CLAIM FAILS | The exact full phrase occurs once; the shown wildcard ellipsis is not the executed full pattern. |
| S7 | HOLDS | Exact substring occurs once. |
| F1/F4 | HOLDS AS 16-HEX PREFIX CHECKS | Both current full hashes begin with the printed prefixes. |
| F2/F3 | HOLDS | Exact authorization substrings occur once. |
| G1 | HOLDS | Independent `csv.DictReader` pass consumed 208,407 rows. |
| G2 | HOLDS | Independent `math.fsum` recomputation gave `0.057984637398`, rounding to `0.057985`. |
| H1 | HOLDS | AST inspection found one `_rank_tertiles` function definition, at line 279. |
| H2 | HOLDS AT NAMED SCOPE | 31 regular files, 0 symlinks, and 0 byte hits under `handcheck/`. |
| D1 | HOLDS | Exact caption phrase occurs once. |
| D2 | HOLDS ONLY AS STORED FIELD | JSON `coverage` is numeric `0.9709`; the displayed string is not the executed command and the field does not establish audio content. |
| P1 | VALUE HOLDS; CUSTODY QUALIFIER OMITTED | One matching row yields seq/stamp, but that row is explicitly backfilled. |
| P2 | HOLDS CURRENTLY | Live full SHA-256 is `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`. |
| P3 | PRIMITIVE HOLDS; STATED CONTENT CLAIM NOT ESTABLISHED | One regex line hit for the first token; no check of the remaining values or attribution. |
| Q1 | PRIMITIVE HOLDS; SEMANTIC CLAIM REFUTED | Literal banned count is 0; `neither` carries the surviving overgeneralisation. |

## Failed attacks / facts that held

- Both dispatch pins matched before content review.
- The script completed with status 0, 21 PASS rows, 0 FAIL rows, and `21 passed, 0 failed`.
- Runtime line 1 matched the script's true full SHA-256; line 2 matched both static and runtime claim counts.
- The narrow freeze-first replacement is accurate on the current custody model.
- All shortened source paths resolve to the intended current files.
- Independent exact checks confirmed the present S/F/G/H/D facts rather than accepting the script's self-report.
- P2 is current against the live report page after a fresh full hash.
- The volatile archive's current report-bound block actually contains all three values and the correct report link.
- P1 found one, not several, matching rows, with the printed seq and timestamp.
- H2's tree has no symlink escape. No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read.

## Evidence methods and boundary ledger

Read-only methods included: pre-review `shasum -a 256` pin verification; fresh `zsh _evidence_20260822/verify.sh`; independent Python SHA/substr/CSV/geometry/AST/JSON/HTML-block checks; no-follow `handcheck/` inventory; Q1 lexical-survivor scan; stdin-only malformed-regex decoys; exact target `git status`; and final source-pin rechecks. One read-only output-formatting pipeline used `sed` only on command stdout; it changed no file.

No temporary file was created by this gate. Pre-existing `_tmp_gate_ev3_stdout.log` and `_tmp_gate_ev3_stderr.log` were names-listed only and never opened. The only file written by this gate is this report.

### SHA-256 ledger — 52 reviewed artifacts

Aliases: `B` = the dispatched prereg directory; `R` = `/Users/duhokim/HermesOps/reports/status-audio`.

#### Core, comparison, and publication artifacts

- `1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29`  `B/CHI_CUSTODY_20260822.md`
- `46a2bcfe8b4432b6c59bba925fba5dd2739aaba88f7a923877d47609e37b667e`  `B/_evidence_20260822/verify.sh`
- `3c2cb2de4882fb0c7bb28f611d64f9316c96e80850acd90a92516d11ae29c9ec`  `B/GATE_CHI_CUSTODY_EVIDENCE_V2_20260822.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `B/CHI_CUSTODY_RECEIPT_20260821.md`
- `3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c`  `B/_evidence_20260822/geom.py`
- `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`  `B/_positions_20260820/positions_parent_20260820.csv`
- `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`  `B/K8_CROSSING_AUTHORIZATION_20260820.md`
- `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`  `B/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`  `B/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`
- `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`  `B/GATE_FOOTPRINT_GEOMETRY_20260821.md`
- `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`  `B/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`
- `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`  `B/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`
- `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`  `R/20260820T231235-hwao-report.mp3`
- `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`  `R/20260820T231235-hwao-report.txt`
- `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`  `R/20260820T231235-hwao-report.deck.json`
- `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`  `R/20260820T231235-hwao-report.times.json`
- `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`  `R/20260821T151843-hwao-report.txt`
- `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848`  `R/20260821T151843-hwao-report.times.json`
- `5b7ef6b9593a741738407271827e11e5757e83b7a913dc00df06d69e50653b2d`  `R/queue_ledger.jsonl`
- `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`  `R/report-20260820T231235-hwao-report.html`
- `e763360e107af89283238fc74db3ebda15fc7ee46fdf2f6a6fe460b9ed11d7af`  `R/archive.html`

#### H2 traversal set — 31 regular files

- `db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f`  `B/handcheck/OPERATING_INSTRUCTIONS.md`
- `ccb217287424bbac06e4bc6f3c6e3c8f54a300c5e2f0ed42e64896cca8bd8d18`  `B/handcheck/SELFTEST.md`
- `d5b2ce3a2d938d8baa88861f4f2983d8fcfedd7582d25ec9f7225835d2381697`  `B/handcheck/YUI_HANDCHECK_HARNESS_20260814.md`
- `9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8`  `B/handcheck/hc1h_full_test_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/hc1h_full_test_stdout.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/hc1h_independent_stderr.log`
- `51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb`  `B/handcheck/hc1h_independent_stdout.log`
- `19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8`  `B/handcheck/hc1h_independent_verification.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/hc1h_selftest_stderr.log`
- `a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b`  `B/handcheck/hc1h_selftest_stdout.log`
- `25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40`  `B/handcheck/hc1h_synthetic_selftest_receipt.json`
- `15f48274ccf81d476a3a92c2241a279dfe4b098d018a83e68368d2ad0000936e`  `B/handcheck/independent_verify_hc1h.py`
- `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4`  `B/handcheck/nm_handcheck.py`
- `2698ab1768656649c881a862d70f72011464f4614923391e6bd5e5dc8339f206`  `B/handcheck/run_hc1h_synthetic_selftest.py`
- `727aef49cbf2f0ac7e6bf29ab94b7d9154132e80a0833640c305d5ce71094382`  `B/handcheck/superseded_hc1_20260815/README.md`
- `ebe607be44c62c552a845f0cbdbdb5986fa5c7c0d53eff9bddd575a5c37ae4a5`  `B/handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stdout.log`
- `148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b`  `B/handcheck/superseded_hc1_20260815/full_test_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/superseded_hc1_20260815/full_test_stdout.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/superseded_hc1_20260815/independent_stderr.log`
- `b4f51b589170659f0be7c6e38d93c81e35b13a13e4813ede694f9e9bf4a2de63`  `B/handcheck/superseded_hc1_20260815/independent_stdout.log`
- `54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae`  `B/handcheck/superseded_hc1_20260815/independent_verification.json`
- `c10ca1b5cc3f9e178e5551b4b48459f11f8fafbb0734ce4531af481f1e9aec98`  `B/handcheck/superseded_hc1_20260815/independent_verify.py`
- `9056ef22c89ea8e4606610948ac7b32b959c97ec42d3ea2597bdc4e71bb67ce7`  `B/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_receipt.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stderr.log`
- `29a592d8ed9c9c571ff96195e1313815a7cb3ece824fb67e9ae2d539779a1b1e`  `B/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stdout.log`
- `cc3c077ec613d4745ae7743cbc6e24a5b8a12e04efe361359560a07e5ef42821`  `B/handcheck/superseded_hc1_20260815/run_synthetic_selftest.py`
- `1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8`  `B/handcheck/superseded_hc1_20260815/synthetic_selftest_receipt.json`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/superseded_hc1_20260815/synthetic_selftest_stderr.log`
- `e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab`  `B/handcheck/superseded_hc1_20260815/synthetic_selftest_stdout.log`
- `ffa2910edb610892f7ca742feb0756f3ed212bf79b48e58f8c2ee2bd5e97fc71`  `B/handcheck/test_nm_handcheck.py`

## Deliberate exclusions and uncertainty

- No external publication platform was inspected. Publication custody was tested against the local backfilled ledger and current local served files.
- No fresh ASR was run. D1/D2 were adjudicated as caption/JSON primitives only.
- Names-only reconnaissance results were not promoted to reviewed artifacts.
- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened.
