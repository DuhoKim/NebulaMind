REFUTED_CHI_CUSTODY_EVIDENCE

# Adversarial gate — `CHI_CUSTODY_20260822.md` and `_evidence_20260822/verify.sh`

## Executive verdict

The replacement is refuted. The dispatched document and script matched both pinned SHA-256 values before review, and a pre-report fresh run did print `17 passed, 0 failed` with byte-identical recorded output. But the frozen document misidentifies its own script and recorded-output hashes and says `15 claims, 15 passing`; the actual script has 17 claim invocations. The absolute quantifier rule is also breached in the document, in H2's claim description, and in both final SCOPE lines. Finally, several PASS mechanisms can return the expected scalar while their descriptions are false, and the mandatory gate report itself changes the verifier's unpinned `GATE_*.md` output.

No remedy is proposed.

## Finding 1 — BLOCKING: the frozen document's executable custody block is false

Dispatch identity held:

- `CHI_CUSTODY_20260822.md`: `2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866` — matches the brief.
- `_evidence_20260822/verify.sh`: `57b5b3d320cc70ca6f59e355c318a511be1426ba18b0a801fd7681128c470b06` — matches the brief.

The bytes inside the pinned document do not describe those artifacts:

- Document line 22 prints script SHA-256 `b8ac8b2c53d8d52cea16104553d218de49abab44da5d48e38f92d1f168a9a29f`; the dispatched script is `57b5b3d3...`.
- Document line 23 prints recorded-output SHA-256 `fe399a784135705d38c0cfcf390f0910cff6de10fd32a08eb4fa4265e24ce40c`; `_evidence_20260822/verify_output.txt` is `da5b281af67fbda8794eaa8d2230da2b61b945a31baa26b5105306ac8b9cb08e`.
- Document line 25 says `15 claims, 15 passing`; `grep -Ec '^claim [A-Z][0-9]' verify.sh` returns 17, and the fresh output says `17 passed, 0 failed`.

This is not a moved-input failure detected by the script. The script exits 0 while the reader-facing custody instructions are false.

## Finding 2 — BLOCKING: the absolute no-universal-quantifier rule has direct survivors

The brief makes one survivor a finding. There are many.

Document examples:

- line 4: `all retained`;
- line 8: `Not once`;
- lines 9–10: quoted survivors `no code path` and `cited by no gate`;
- line 14: `no universal quantifier appears in any claim` and `any claim`;
- lines 15–16: `never` and `everywhere`;
- line 40: `on every run`;
- lines 43–44: H2 `returning no lines` and `no code anywhere`;
- lines 47–48: `No count, no summary, no inference` and `any gate`;
- line 59: `no breach established`;
- line 67: `I state no count from it`.

Claim-description survivor:

- script line 50: H2 says `returns no lines`.

SCOPE-line survivors:

- script line 63: `nothing else`;
- script line 64: `any other path`.

Quoted, negated, scoped, or self-referential uses still remain present. The rule was stated as absolute, not as a semantic exception list.

## Finding 3 — BLOCKING design refutation: PASS can be obtained without establishing the description

Concrete decoys against the exact primitives returned:

- F2: a line saying `This document rejects the sentence: No sky statistic, no dipole` gives grep count `1` although it establishes no bar.
- F3: `This is not a Partial-tertile prohibition` gives grep count `1` although it establishes the opposite context.
- H1: `# def _rank_tertiles(rows): pass` gives grep count `1` although Python defines no function.
- H2: the exact suppressed-error pipeline against a nonexistent directory returns `0` with pipeline status `0`. Missing/unreadable search input can therefore PASS as “returns no lines.”
- D2: a JSON object containing only `{"coverage": 0.9709}` returns the expected value while establishing no alignment or audio coverage.
- G2: an executable containing only `print("0.057985")` returns the expected scalar. The live `geom.py` is not pinned by the document or script, so the pinned verifier does not bind the computation it executes.

Additional underbinding:

- `h()` truncates SHA-256 to 16 hexadecimal characters. S1–S4 and F1/F4 bind 64-bit prefixes, not the full digests described elsewhere as SHA-256 custody.
- G1 is `wc -l - 1`; it does not establish CSV parseability, required fields, or valid data rows. The current CSV happens to pass an independent parse, but the claim mechanism does not enforce that.
- Gate verdicts are uncounted, dynamically globbed first lines. No digest binds the gate files printed.

The current F2/F3/H1 inputs happen to support their descriptions when read in context. That failed attack does not cure the demonstrated ability of the checks to PASS false descriptions.

## Finding 4 — BLOCKING: the claimed one-command evidence boundary omits load-bearing assertions

The document says it makes only claims checkable in one command, but `verify.sh` does not check these reader-facing assertions:

- ten gates / ten refusals;
- eight revisions and retention;
- the predecessor's `13 of 72 inputs` coverage;
- Duho's approval of the approach;
- the first-run H1 history (`1` expected versus `4` occurrences);
- Blanc's sweep being reworked twice and its clearance being retracted;
- the pointer target being `current by construction`;
- `tail_overlap 0.92`;
- the footprint's inability to reach preregistered power.

More importantly, the executable contains no publication-state check. S1–S4 prove only current local file-prefix identities; S5–S7 grep the current caption. The §4 finding requires proof that a report was published. I independently established publication from `queue_ledger.jsonl`, but that file is not consumed or pinned by the verifier. The script also does not establish what the MP3 says: it hashes the audio but checks content only in the mutable/corrected caption.

The footprint sentence has a second custody gap. The two named gates begin `HOLD_FOOTPRINT_GEOMETRY_FINDING` and `HOLD_FOOTPRINT_GEOMETRY_REV2`; they preserve central arithmetic while withholding PASS on the reviewed revisions. The current Revision-3 finding's later absolute power conclusion is not a claim in `verify.sh`.

## Finding 5 — Blanc section: a literal count survives, the path needs an unstated base, and “current by construction” is not established

The document's `I state no count from it` is literally contradicted one line later/earlier by its historical `218-report` and `three divergences` count language. Those numbers are labelled stale, so they are not presented as current results, but they are still relayed from the sweep under an absolute “no count” assertion.

From the brief's declared base directory, the written path
`blanc-ops-overhaul-20260820/DISCLOSURE_LEDGER_AUDIO_20260821.md` does not exist. It resolves only after silently changing the base to `.hermes/handoffs/`; the actual artifact there has SHA-256 `79d89c9d0c5232e572aec2650c3680e55904f58f9b4c2d63286b8a1c5a8fac31`.

The target file's own correction header says its clearance method is unsound and its “excluded”/“clean” lines are unverified. It also still prints sweep counts (`220`, `18`, `1`, `17`). That does not establish the replacement's statement that the file is “current by construction.”

A failed attack did hold: the first two divergences from Revision 8 have been repaired in current captions. Their MP3 bytes still match the R8-audited hashes, while the current caption hashes moved to `ba35d434...` and `3799ae2a...` and now say `832,000` and `130,000`. The remaining Hwao divergence at `20260821T151843` is byte-identical to the R8-audited audio/caption pair.

## Finding 6 — G2's live arithmetic holds, but its custody and axis description do not

The live `geom.py` does read `_positions_20260820/positions_parent_20260820.csv` via `csv.DictReader`; the result is not hardcoded in `geom.py`. A separate standard-library computation parsed 208,407 rows and returned population variance `0.057984637398`, rounding to `0.057985`.

The literal `0.057985` is nevertheless hardcoded as the expected value in `verify.sh` line 41 and repeated in the document. More importantly, `geom.py` itself is an unpinned executable dependency. Its axis coordinates are hardcoded at `(216.984434295527, 32.060611193471)`. Those coordinates are reproduced in the two footprint gate reports, but the frozen preregistration checked by F4 does not contain them. G2 therefore establishes “this current script over this current CSV at these embedded coordinates prints this scalar,” not the full description “about Longo's frozen axis” under pinned custody.

## Finding 7 — D1 holds; D2 does not establish the divergence

Current identities:

- caption: `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`;
- alignment: `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848`;
- MP3: `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3`;
- MP3 duration: `162.312000` seconds.

The caption still says `one galaxy at a time, 200,000 times`, and the document accurately states its decision not to edit that caption. The MP3 is byte-identical to the artifact for which `GATE_CHI_CUSTODY_R8_20260821.md` reported fresh ASR ending at `One galaxy at a time` with no `200,000`.

I did not run a new speech recognizer in this gate. D2 checks only the JSON's stored `coverage` field `0.9709`; it neither recomputes alignment nor checks the audio's final words. The divergence is retained by exact-byte identity to the prior ASR gate, not independently established by D1/D2.

## Finding 8 — prior receipt claims silently dropped

I compared the eight top-level receipt states (Revision 1 through Revision 8). The replacement explicitly discloses the broad withdrawals (`complete ledger`, `no code path`, gate-citation mapping, exact input set, witness/commit overclaims), scopes H2, and delegates Blanc's changing sweep. The following Revision-8 evidence/claims disappear without being named as dropped:

1. Publication custody: seq 20, publish time 23:12:51 KST, 52-minute-after-authorization timing, and the queue-ledger join.
2. Two served surfaces and their digests: report HTML and `archive.html`. The replacement pins only MP3, caption, deck, and alignment.
3. Caption-repair causation: reconstruction of the prior caption and served-page hashes.
4. Fresh-ASR clearance of the 23:12 MP3. The replacement hashes audio but semantically greps only caption text.
5. Dispatch-snapshot/`uchg` byte-custody evidence and the claimed external git witnesses.
6. The generated disclosure table's other report stamps and source classes (archive pages, report pages, `_drafts/`, publication joins). `Not covered here` names Blanc's ledger and ASR sweep, but does not say that this wider publication/source scan was removed.

These deletions matter because item 1 is the evidence needed for the replacement's §4 publication-bar finding. The finding remains independently true on current evidence, but it is not established by the replacement's command.

## Re-derived rulings from frozen/current evidence

### §4 publication bar — breach established independently, not by `verify.sh`

`K8_CROSSING_AUTHORIZATION_20260820.md` lines 46–50 say publication of any kind was not authorized. `queue_ledger.jsonl` line 21 records a `publish` event for `20260820T231235-hwao-report.mp3` at 23:12:51 KST. The authorization is timestamped 22:20 KST; the independent delta is 3,171 seconds (52.85 minutes). The publication bar was breached.

### Condition 2 — breach established

Authorization lines 32–33 bar any summary over chi until the frozen order reaches it. The caption says `One leaning each way among the confident pair`, a sign/count summary, and the publication ledger joins that transcript to seq 20. Condition 2 was breached independently of the three numeric values.

### Condition 1 — no breach established by the searched scope

H2's current result holds at its literal scope. An independent byte scan of the 31 regular files under `handcheck/` found zero `chi_dr10_south` matches, zero read errors, and zero symlinks. The document does not promote this into “no code anywhere”; line 59 keeps the negative scoped. This establishes only that this literal tree name was not found in those 31 files. It does not search runtime invocation receipts or alternate input names, and the forbidden chi tree was not opened.

## Mandatory self-invalidation check

Before this report existed, fresh verifier output had SHA-256 `da5b281af67fbda8794eaa8d2230da2b61b945a31baa26b5105306ac8b9cb08e` and was byte-identical to `_evidence_20260822/verify_output.txt`.

After creating the mandatory top-level `GATE_CHI_CUSTODY_EVIDENCE_20260822.md`, the script's unpinned `for g in $LANE/GATE_*.md` loop gained this report's first-line verdict. The post-write run still exited 0 and printed `17 passed, 0 failed`, but its SHA-256 became `d2804fb194eea4158359c4dadd8508acf1357fc09861a833a93088a61f1553c8`; byte comparison to the recorded `da5b281a...` output failed. The exact diff is one added row:

`GATE_CHI_CUSTODY_EVIDENCE_20260822.md                REFUTED_CHI_CUSTODY_EVIDENCE`

## Failed attacks / facts that held

- Both dispatch pins matched before any content was opened and still matched at the final pre-report recheck.
- A fresh pre-report run exited 0, printed `17 passed, 0 failed`, and byte-matched the recorded output.
- S1–S7's current files and exact caption strings held.
- F1/F4 full current hashes begin with the expected prefixes; F2/F3's actual frozen contexts support their descriptions.
- G1's current line count also survived a real CSV parse: 208,407 valid rows were consumed by the independent geometry calculation.
- H1's current source genuinely defines and uses `_rank_tertiles`; the lexical check is underpowered, but the current semantic fact is true.
- H2's named scope is printed honestly, and the document does not promote it to a global negative.
- G2 recomputed from the positions CSV and matched independently to twelve decimal places before rounding.
- D1's caption assertion and the document's no-edit decision are current.
- The first two previously reported audio/caption divergences are repaired in the current captions.
- The document presents no *current* Blanc sweep total, although it still contains historical numeric sweep language.

## Uncertainties and deliberate exclusions

- Nothing under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read.
- No fresh ASR was run. The D audio statement is bound by current SHA-256 to the prior gate's ASR result.
- I did not re-derive the separate Revision-3 absolute power theorem; I independently re-derived only row count and `var(cos theta)`. The two cited footprint gates are HOLD verdicts.
- I treated returned content snippets as reviewed artifacts and recorded their hashes below. Names-only search results were not treated as content review.
- Writes were limited to this report and the permitted `_tmp_gate_ev_fresh_verify.txt` / post-report verifier capture.

## Command/result ledger

1. `shasum -a 256 CHI_CUSTODY_20260822.md _evidence_20260822/verify.sh` — both dispatch pins matched.
2. `zsh _evidence_20260822/verify.sh > _tmp_gate_ev_fresh_verify.txt` — exit 0; `17 passed, 0 failed`.
3. `cmp`/`diff` and SHA-256 on fresh versus recorded output — byte-identical, both `da5b281a...` before this report existed.
4. Full SHA inventories over verifier dependencies, 31 `handcheck/` regular files, 13 top-level `GATE_*.md` files, eight receipt revisions, and independently reviewed sources — recorded below.
5. Independent `csv.DictReader` + `statistics.pvariance` calculation — 208,407 rows; `0.057984637398`; six decimals `0.057985`.
6. Independent recursive byte scan of `handcheck/` — 31 regular files, 0 symlinks, 0 hits, 0 errors.
7. Exact primitive decoys for F2/F3/H1/H2/D2/G2 — returned `1,1,1,0(status 0),0.9709,0.057985` respectively.
8. `queue_ledger.jsonl` exact-stem search and timestamp subtraction — publish event found; 3,171 seconds after authorization.
9. Pointer existence checks — absent relative to the declared base; present relative to `.hermes/handoffs/`.
10. `ffprobe` on D MP3 — duration `162.312000` seconds.
11. Two preliminary shell hash-inventory attempts failed before a complete ledger (unsupported Bash/Zsh glob syntax); a third stopped at the nonexistent document-relative Blanc path. No artifact was changed by those attempts.
12. Core-pin recheck immediately before report write — unchanged.
13. `zsh _evidence_20260822/verify.sh > _tmp_gate_ev_post_report_verify.txt`, followed by SHA-256/`cmp`/`diff` — exit 0 and `17 passed, 0 failed`, but byte mismatch; one added gate row; post-report output `d2804fb1...`.

## SHA-256 ledger — every content-reviewed artifact

Path aliases: `B` = the declared prereg base; `R` = `/Users/duhokim/HermesOps/reports/status-audio`; `H` = `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs`.

### Primary deliverable and verifier inputs

- `2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866`  `B/CHI_CUSTODY_20260822.md`
- `57b5b3d320cc70ca6f59e355c318a511be1426ba18b0a801fd7681128c470b06`  `B/_evidence_20260822/verify.sh`
- `da5b281af67fbda8794eaa8d2230da2b61b945a31baa26b5105306ac8b9cb08e`  `B/_evidence_20260822/verify_output.txt`
- `da5b281af67fbda8794eaa8d2230da2b61b945a31baa26b5105306ac8b9cb08e`  `B/_tmp_gate_ev_fresh_verify.txt`
- `d2804fb194eea4158359c4dadd8508acf1357fc09861a833a93088a61f1553c8`  `B/_tmp_gate_ev_post_report_verify.txt`
- `3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c`  `B/_evidence_20260822/geom.py`
- `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`  `B/_positions_20260820/positions_parent_20260820.csv`
- `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`  `B/K8_CROSSING_AUTHORIZATION_20260820.md`
- `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`  `B/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`

### Report surfaces

- `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`  `R/20260820T231235-hwao-report.mp3`
- `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`  `R/20260820T231235-hwao-report.txt`
- `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`  `R/20260820T231235-hwao-report.deck.json`
- `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`  `R/20260820T231235-hwao-report.times.json`
- `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3`  `R/20260821T151843-hwao-report.mp3`
- `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`  `R/20260821T151843-hwao-report.txt`
- `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848`  `R/20260821T151843-hwao-report.times.json`
- `78471d4147bce699f29fa0343220068656d2847f8e718a5b175c3b111e286c02`  `R/20260814T160157-variance-pass.mp3`
- `ba35d4347afda92f63a9a206a487ac9bcb8bcfb3b9d223f9920a3be11b96d2db`  `R/20260814T160157-variance-pass.txt`
- `3913befc8faf7c4fbcbf4add6d7c3c4c263aad4bdbb58899a4b97faca614eafb`  `R/20260814T161526-ten-blockers.mp3`
- `3799ae2ab7733ce3a87d0d846440cb1e417971b6ab21ff82bc5c364f798113d7`  `R/20260814T161526-ten-blockers.txt`
- `d7f08d26fd197396ce0625afaa8f2a97b522b02256a4235e135d66318d0323be`  `R/queue_ledger.jsonl`

### Blanc / related evidence

- `79d89c9d0c5232e572aec2650c3680e55904f58f9b4c2d63286b8a1c5a8fac31`  `H/blanc-ops-overhaul-20260820/DISCLOSURE_LEDGER_AUDIO_20260821.md`
- `51bd298e8b426ae4caef016871ef5623520976088afeb163ee91baf53da83627`  `H/blanc-ops-overhaul-20260820/CAPTION_CORRUPTION_20260821.md`
- `1a12cf7b08c36f774b79547b3bae907075f21172877c998e7c1e3f6c9617a55b`  `H/blanc-ops-overhaul-20260820/HWAO_TO_BLANC_THREE_DIVERGENCES_20260821.md`

### Receipt revisions and snapshots

- `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e`  `B/CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md`
- `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c`  `B/CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md`
- `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093`  `B/CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md`
- `acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b`  `B/CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md`
- `2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65`  `B/CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md`
- `5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043`  `B/CHI_CUSTODY_RECEIPT_20260821_REV6_SUPERSEDED.md`
- `879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e`  `B/CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `B/CHI_CUSTODY_RECEIPT_20260821.md`
- `879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e`  `B/_custody_20260821/_gated/CHI_CUSTODY_RECEIPT_20260821.879ec60426ea.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `B/_custody_20260821/_gated/CHI_CUSTODY_RECEIPT_20260821.c3e6de5ef640.md`

### Gate files read by the verifier

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

### Handcheck files traversed by H2

- `d5b2ce3a2d938d8baa88861f4f2983d8fcfedd7582d25ec9f7225835d2381697`  `B/handcheck/YUI_HANDCHECK_HARNESS_20260814.md`
- `ffa2910edb610892f7ca742feb0756f3ed212bf79b48e58f8c2ee2bd5e97fc71`  `B/handcheck/test_nm_handcheck.py`
- `ccb217287424bbac06e4bc6f3c6e3c8f54a300c5e2f0ed42e64896cca8bd8d18`  `B/handcheck/SELFTEST.md`
- `2698ab1768656649c881a862d70f72011464f4614923391e6bd5e5dc8339f206`  `B/handcheck/run_hc1h_synthetic_selftest.py`
- `db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f`  `B/handcheck/OPERATING_INSTRUCTIONS.md`
- `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4`  `B/handcheck/nm_handcheck.py`
- `15f48274ccf81d476a3a92c2241a279dfe4b098d018a83e68368d2ad0000936e`  `B/handcheck/independent_verify_hc1h.py`
- `25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40`  `B/handcheck/hc1h_synthetic_selftest_receipt.json`
- `a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b`  `B/handcheck/hc1h_selftest_stdout.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/hc1h_selftest_stderr.log`
- `19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8`  `B/handcheck/hc1h_independent_verification.json`
- `51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb`  `B/handcheck/hc1h_independent_stdout.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/hc1h_independent_stderr.log`
- `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  `B/handcheck/hc1h_full_test_stdout.log`
- `9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8`  `B/handcheck/hc1h_full_test_stderr.log`
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

### Other returned-content artifacts reviewed during provenance comparison

- `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`  `B/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`
- `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`  `B/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`
- `3e44b39505f2f734e97d50e6a9185398b2142e6039a60aba576d5b1b4db5b554`  `B/_tmp_GATE_BRIEF_MEMO_R6.md`
- `0fc1ca5f7742fb3ba023fe79f8469d9a232d9902ef48c8232d698795b2e771fd`  `B/_tmp_GATE_BRIEF_RECEIPT_R7.md`
- `6c9d2513525f6a471acc9c3024862572ded10cd3f748173d4a8eca50e8c518d9`  `B/_tmp_GATE_BRIEF_EVIDENCE_20260822.md`
- `ddffe06cce8e41a3601931e36a92fc8d83d3aeff3c09be4cc6765311295ccbe2`  `B/_tmp_gate_r8_repro/GATE_DECISION_MEMO_R6_20260821.md`
- `06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa`  `B/_tmp_gate_r8_repro/GATE_CHI_CUSTODY_R7_20260821.md`
- `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`  `B/_tmp_gate_r8_repro/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`
- `635ed8e6bda6b20fe8ae3283a8d89cbecb83037245981b96ff373a253dbd8b7a`  `B/_tmp_gate_r8_report_complete.md`
- `df52c2031b1508f27768710ece0ca7d7cf03b33c394159b7a00b4781d7af7532`  `B/_tmp_gate_r8_report_body.md`
