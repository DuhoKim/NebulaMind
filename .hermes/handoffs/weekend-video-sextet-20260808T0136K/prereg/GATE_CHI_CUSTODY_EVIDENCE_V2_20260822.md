REFUTED_CHI_CUSTODY_EVIDENCE_V2

# Adversarial gate — `CHI_CUSTODY_20260822.md` v2 and `_evidence_20260822/verify.sh`

## Executive verdict

The dispatched bytes matched both pins before content review. Two fresh executions exited 0, printed the script's correct full SHA-256 on line 1, printed the real static and runtime claim count of 18 on line 2, and ended `18 passed, 0 failed`.

The gate is nevertheless refuted. Q1 returns 0 while the current document itself makes a categorical, false generalisation using `cannot`, a word outside the literal list. The document also promotes local file hashes and caption greps into a publication-breach conclusion after silently dropping the predecessor's publication event and served-surface evidence. Finally, six passing claim descriptions say a file's `shasum` *is* a 16-character value even though the implementation explicitly truncates the 64-character SHA-256; those descriptions are false as written.

No remedy is proposed.

## Dispatch identity

Verified before either target was opened:

- `CHI_CUSTODY_20260822.md`: `3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d` — matches dispatch.
- `_evidence_20260822/verify.sh`: `9437a1c312d43b797377fb094825abb1a989a24db01b434c091d1ce5c202bbfb` — matches dispatch.

Both remained unchanged at the final pre-report recheck.

## Finding 1 — BLOCKING: Q1 passes a sweeping false claim in the current document

Q1's primitive is real: both the script's `grep -Eoi ... | wc -l` and the description's `grep -Eic` return 0 on the pinned document. That does not test the stated scoping rule.

The current document supplies the requested counterexample at lines 10–14:

> `A document cannot hold the digest of a script edited beside it ... That is a self-reference problem`

This is categorical beyond the evidence and false. The document and script are separate byte strings. A document can contain the digest of a separately finalised script; changing the script later makes the recorded digest stale, but no self-reference exists. The sweeping operator is `cannot`, which is absent from Q1's literal list.

A second semantic survivor appears at lines 59–62:

> `The disclosure breaches §4's publication bar and condition 2 independently.`

The script establishes current local digest prefixes and caption strings. It does not establish that the report was published, when it was published, or which served surface carried it. That conclusion outruns the executable evidence without using a banned token.

Q1 therefore demonstrates only that none of twelve listed lexical patterns occurs. The document's stronger statement that “the scoping rule is tested” is refuted by its own current text.

## Finding 2 — BLOCKING: six PASS descriptions are false as written

`h()` at script line 21 runs SHA-256 and then `cut -c1-16`. S1–S4, F1, and F4 nevertheless say `shasum of ... is <16 hex>`, not “the first 16 hexadecimal characters are ...”. A SHA-256 is the full 64-character digest. Independent comparison returned `exact_equal=False, prefix_equal=True` for all six:

| ID | claimed as the shasum | actual full SHA-256 |
|---|---|---|
| S1 | `2a38a887bd897147` | `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168` |
| S2 | `2c85b2028209273a` | `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162` |
| S3 | `1da50dc6878db905` | `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c` |
| S4 | `a9cfedc4ab127794` | `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79` |
| F1 | `c10687595f1f4313` | `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69` |
| F4 | `b06901c8a0f3a057` | `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7` |

The checks honestly bind 64-bit prefixes. They do not establish their descriptions' literal equality claims. This directly defeats the stated repair that each description now equals what the check returns.

## Finding 3 — BLOCKING custody gap: the publication conclusion survives after its evidence is dropped

The last receipt revision supplied load-bearing publication custody:

- report stamp and seq 20;
- recorded time 23:12:35 KST and publish time 23:12:51 KST;
- the 52-minute relationship to the 22:20 authorization;
- the `queue_ledger.jsonl` publication join;
- report HTML and `archive.html` in addition to MP3, caption, deck, and alignment.

V2 deletes all of that. `verify.sh` does not open a publication ledger or a served page. S1–S4 only hash four local files, and S5–S7 only grep one local caption. The document still says those checks support a breach of a *publication* bar. The predecessor's publication evidence may still exist elsewhere, but it was silently removed from the evidence boundary claimed by this document.

Condition 2 is better grounded: the authorization text bars a summary over chi, and the caption contains the sign/count summary. Even there, the script proves current local text, not publication. The §4 conclusion specifically requires the dropped publication event.

## Finding 4 — MATERIAL provenance gap around D1/D2

The narrow current checks hold:

- D1: the caption contains `one galaxy at a time, 200,000 times` once.
- D2: the JSON object has `mode: aligned`, `coverage: 0.9709`, and `duration: 162.312`.
- The MP3 is still SHA-256 `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3`, the exact audio independently ASR-checked by `GATE_CHI_CUSTODY_R8_20260821.md` as ending before `200,000`.

The stated decision not to amend D1 is accurately described: the authored caption retains the intended phrase and the frozen audio is the truncated surface. D2's description is now limited to the stored JSON field and is true.

The provenance sentence is not accurate as written. The current cited Blanc ledger, SHA-256 `9d68fe1b9be46db20c8880ace07f74acd1012447f3acae5d9ad04b17ad7b455b`, contains no `20260821T151843` or `200,000` entry. The direct record is `HWAO_TO_BLANC_THREE_DIVERGENCES_20260821.md`, which says the defect was found by `GATE_CHI_CUSTODY_R7_20260821.md` and verified by Hwao. The fact survives; the attribution to “Blanc's reverse-direction numeric check” is unsupported by the named current Blanc artifact.

## Gate-listing removal

The removal itself survives attack. Before this report was written, the document's exact separate command returned 14 filename-to-first-line mappings: 12 `REFUTED_*` verdicts and two footprint `HOLD_*` verdicts. It had no malformed or empty first line. Because no output digest or count is claimed, a newly written gate appearing on the next invocation does not invalidate a frozen claim.

The command is an adequate live substitute for *first-line verdict lookup*. It is not a substitute for the predecessor's revision/provenance mapping: it does not show the bytes or revision each gate reviewed. That limitation matters to the document's line 64–65 statement that the current Revision-3 footprint finding was “held by two gates”. The two visible verdicts are HOLDs; the first reviewed the original finding and the second explicitly reviewed Revision 2. Neither first line binds the current Revision-3 hash `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`.

## H2 scope ruling

H2's scope is stated inside its own runtime description as the absolute `.../prereg/handcheck/` path. The document repeats the `handcheck/` restriction and at lines 61–62 says the result is about that named search and not more. It does not widen H2 to the machine or the forbidden chi tree.

Independent checks found:

- the path exists and is a directory;
- 31 regular files and 0 symlinks;
- unsuppressed `grep -rl chi_dr10_south handcheck/` returned no paths, no stderr, and status 1 (ordinary no-match);
- `_rank_tertiles` has one actual definition at `handcheck/nm_handcheck.py:279`.

Nothing under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read.

## Claim-by-claim adjudication

| ID | Ruling | Independent result |
|---|---|---|
| S1 | FAILS AS WRITTEN | Full SHA-256 starts with the token; it is not equal to the 16-character token. |
| S2 | FAILS AS WRITTEN | Same prefix/equality defect. |
| S3 | FAILS AS WRITTEN | Same prefix/equality defect. |
| S4 | FAILS AS WRITTEN | Same prefix/equality defect. |
| S5 | HOLDS CURRENTLY | Exact substring occurs once and on one line. |
| S6 | HOLDS CURRENTLY | Exact substring occurs once and on one line. |
| S7 | HOLDS CURRENTLY | Exact substring occurs once and on one line. |
| F1 | FAILS AS WRITTEN | Full SHA-256 starts with the token; it is not equal to it. |
| F2 | HOLDS CURRENTLY | Exact substring occurs once in the authorization. |
| F3 | HOLDS CURRENTLY | Exact substring occurs once in the authorization. |
| F4 | FAILS AS WRITTEN | Full SHA-256 starts with the token; it is not equal to it. |
| G1 | HOLDS CURRENTLY | `csv.DictReader` consumed 208,407 rows; all 208,407 had parseable `ra` and `dec`; 0 bad rows. |
| G2 | HOLDS CURRENTLY | Independent `math.fsum` pass returned `0.057984637398`, rounding to `0.057985`; `geom.py` returned the same. Exact coordinates agree with the recorded Galactic-to-ICRS Longo-axis transform. |
| H1 | HOLDS CURRENTLY | One definition, not merely one arbitrary occurrence. |
| H2 | HOLDS AT ITS NAMED SCOPE | Existing 31-file tree; 0 hits; 0 stderr; no symlinks. |
| D1 | HOLDS CURRENTLY | Exact substring occurs once. |
| D2 | HOLDS CURRENTLY | JSON field `coverage` is numeric `0.9709`. It does not itself establish audio content. |
| Q1 | PRIMITIVE HOLDS; SEMANTIC CLAIM REFUTED | Lexical count is 0; current semantic counterexamples survive. The code uses `-Eoi | wc -l` while the description names `-Eic`; both happen to return 0 on these bytes. |

## What V2 silently drops

Direct diffs were run against both `CHI_CUSTODY_20260822_V1_SUPERSEDED.md` and `CHI_CUSTODY_RECEIPT_20260821.md`.

Material dropped predecessor claims/evidence:

1. Publication custody: seq 20, publish timestamp, 52-minute-after-authorization timing, and the queue-ledger join.
2. Two served surfaces and their digests: report HTML and `archive.html`; V2 keeps only four local files.
3. Reverse-repair causation for the caption and served-page hash moves.
4. Fresh-ASR clearance of the 23:12 MP3. V2 hashes audio but semantically checks only caption text.
5. The broader disclosure inventory across narration, decks, report pages, archive pages, `_drafts/`, and publication joins, including its blind-spot statement.
6. Dispatch-snapshot/`uchg` observations, claimed Git witnesses, and the explicit withdrawal of the internal hash chain as evidence.
7. The Revision-8 three-divergence detail and the distinction among digit-summing, connector-splitting, and TTS truncation; V2 delegates Blanc's moving work but retains D1 without a correct source attribution.
8. V1's first-run H1 invented-count history and its recorded `tail_overlap 0.92` failure. These are historical rather than load-bearing, but the deletion is unannounced.
9. V1's gate-refusal/accountability narrative. V2 says only that it supersedes an eight-revision line; it no longer records the predecessor's gate/refusal count.

The removals of stale self-digests and the dynamic gate listing are explicit and therefore are not silent drops. The narrowed H2 language and the refusal to relay Blanc's current totals are also explicit.

## Failed attacks / facts that held

- Both dispatch pins matched before content review and at the final pre-report recheck.
- Two full runs exited 0 with 18 PASS lines, 0 FAIL lines, and `18 passed, 0 failed`.
- Output line 1 exactly matched the script's current full SHA-256.
- Output line 2 matched both 18 static `claim` lines and 18 runtime claim results.
- S5–S7, F2–F3, H1, D1, and D2 are true on the current bytes, not merely obtainable by decoys.
- G1 survived a real CSV parse of every row; G2 survived independent recomputation to twelve decimals before rounding.
- H2 is scoped inside its own description, and the document does not widen it.
- The decision not to rewrite D1's caption is described accurately.
- The dynamic gate listing no longer self-invalidates script output.
- The decision memo is a draft, says it lacks a gate and signature, and says the study has not been declined.

## Commands and evidence methods

1. `shasum -a 256 CHI_CUSTODY_20260822.md _evidence_20260822/verify.sh` — both pins matched before content review.
2. Coordinator relay: read-only `tmux list-panes`/`capture-pane`, one `send-keys` relay to Hwao, then `capture-pane` verification. No execution or artifact mutation was requested of Hwao.
3. `zsh _evidence_20260822/verify.sh` — exit 0, 18 passed, 0 failed.
4. A second subprocess run plus independent static/runtime count and SHA comparison — line 1 and line 2 exact; 18 runtime result lines.
5. Independent full hashes and exact-substring counts for S/F/D inputs.
6. Independent `csv.DictReader` and `math.fsum` geometry pass — 208,407 valid rows; variance `0.057984637398`.
7. Unsuppressed H2 grep plus no-follow filesystem inventory — 31 regular files, 0 symlinks, 0 hits, 0 stderr.
8. `head -1 GATE_*.md` — 14 mapped verdicts before this report, all nonempty.
9. `git diff --no-index` V1→V2 and Revision-8 receipt→V2 — exit 1 as expected for differences.
10. Exact hash inventories for reviewed core, media, gate, and H2 traversal artifacts.
11. Scoped pre-write `git status`; the target report did not exist. Two `_tmp_gate_ev2_*` names already existed before this gate and were names-only; this gate created no temporary file.

## SHA-256 ledger — reviewed artifacts

Path aliases: `B` = the dispatched prereg directory; `R` = `/Users/duhokim/HermesOps/reports/status-audio`; `H` = `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs`.

### Core and comparison artifacts

- `3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d`  `B/CHI_CUSTODY_20260822.md`
- `9437a1c312d43b797377fb094825abb1a989a24db01b434c091d1ce5c202bbfb`  `B/_evidence_20260822/verify.sh`
- `ffe19920a8465582269ad666a44d61375e92216b19bf90b5680bec18dc2c9eb1`  `B/GATE_CHI_CUSTODY_EVIDENCE_20260822.md`
- `2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866`  `B/CHI_CUSTODY_20260822_V1_SUPERSEDED.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `B/CHI_CUSTODY_RECEIPT_20260821.md`
- `3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c`  `B/_evidence_20260822/geom.py`
- `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`  `B/_positions_20260820/positions_parent_20260820.csv`
- `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`  `B/K8_CROSSING_AUTHORIZATION_20260820.md`
- `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`  `B/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87`  `B/TORI_SURVEY_ROUTE_BINDING_20260812.md`
- `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`  `B/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`
- `f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee`  `B/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md`
- `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76`  `B/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md`
- `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`  `B/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`
- `9d68fe1b9be46db20c8880ace07f74acd1012447f3acae5d9ad04b17ad7b455b`  `H/blanc-ops-overhaul-20260820/DISCLOSURE_LEDGER_AUDIO_20260821.md`
- `1a12cf7b08c36f774b79547b3bae907075f21172877c998e7c1e3f6c9617a55b`  `H/blanc-ops-overhaul-20260820/HWAO_TO_BLANC_THREE_DIVERGENCES_20260821.md`

### Media and metadata checked by S/D

- `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`  `R/20260820T231235-hwao-report.mp3`
- `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`  `R/20260820T231235-hwao-report.txt`
- `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`  `R/20260820T231235-hwao-report.deck.json`
- `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`  `R/20260820T231235-hwao-report.times.json`
- `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3`  `R/20260821T151843-hwao-report.mp3`
- `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`  `R/20260821T151843-hwao-report.txt`
- `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848`  `R/20260821T151843-hwao-report.times.json`

### Gate files whose first lines were reviewed

- `ffe19920a8465582269ad666a44d61375e92216b19bf90b5680bec18dc2c9eb1`  `B/GATE_CHI_CUSTODY_EVIDENCE_20260822.md`
- `19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083`  `B/GATE_CHI_CUSTODY_R6_20260821.md`
- `06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa`  `B/GATE_CHI_CUSTODY_R7_20260821.md`
- `df6c92d785b4db9af455af32f4a74ba1096761120bd9983284e02b4a08b48501`  `B/GATE_CHI_CUSTODY_R8_20260821.md`
- `a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa`  `B/GATE_DECISION_MEMO_20260821.md`
- `1cf7ba7780a556428e691d76bb54e08949fb375eb7a3112257ff7986a100ad01`  `B/GATE_DECISION_MEMO_FINAL_20260821.md`
- `59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066`  `B/GATE_DECISION_MEMO_R2_20260821.md`
- `c1ad25fd6574bb9bf3386d8d6fb7448ed62015384035f9110dbde3e94ec0c453`  `B/GATE_DECISION_MEMO_R3_20260821.md`
- `c9a144e256d2c7ef6c63d11c60b5002e25c7268483a4dc0bbd112ffdfeb24707`  `B/GATE_DECISION_MEMO_R5_CODEX_20260821.md`
- `ddffe06cce8e41a3601931e36a92fc8d83d3aeff3c09be4cc6765311295ccbe2`  `B/GATE_DECISION_MEMO_R6_20260821.md`
- `94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e`  `B/GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md`
- `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`  `B/GATE_FOOTPRINT_GEOMETRY_20260821.md`
- `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`  `B/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`
- `38e789547e750d21b38fd9d1fa3515bc44ed8f95d542476183d45274c7518b3c`  `B/GATE_VOID_ON_DESIGN_DEFECT_20260821.md`

### H2 traversal set (31 regular files)

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

## Uncertainties and deliberate exclusions

- No fresh ASR was run. D1's audio statement is retained by exact MP3 identity to prior fresh-ASR gates, not re-recognised here.
- No external publication platform was inspected. The publication event was evaluated only as predecessor evidence and as an input absent from V2's script.
- The broad search results used to locate exact axis and D1 provenance were reconnaissance snippets; files not relied on above were not treated as reviewed evidence.
- Pre-existing `_tmp_gate_ev2_stdout.log` and `_tmp_gate_ev2_stderr.log` were names-listed only and never opened.
- No artifact was changed except this report. No temporary file was created.
