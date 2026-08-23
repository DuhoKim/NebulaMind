REFUTED_CHI_CUSTODY_EVIDENCE_V5

# Adversarial gate — `CHI_CUSTODY_20260822.md` v5 and `_evidence_20260822/verify.sh`

## Executive verdict

Both dispatched artifacts matched their pinned SHA-256 values before either was opened, and still matched at the pre-report recheck. The one-variable `claim()` mechanism held: the current script produced 26 PASS rows and 0 FAIL rows; controlled runs from the prereg directory and another working directory had byte-identical stdout; and all 26 complete displayed commands reproduced their values in clean zsh, bash, and sh with a standard PATH. The document's revised single-line/multiline/standard-PATH qualification is accurate.

The gate is nevertheless refuted. P3 is not bounded to the HTML entry opened by the named `data-src`; it is bounded only to the next textual `data-src=`. A value phrase in a later, separate `<li>` before that later entry's `data-src` passes P3, and when the target is last, any matching phrase after its closing `</li>` passes through EOF. P4 remains global and accepts its href in another entry. Two material V4 findings also survive unchanged: S1-S4 are still described as four files “carrying” the disclosure even though the deck and alignment do not, and the “nothing leaves unannounced” sentence still omits Revision 8 material identified by V4. The artifact pair also retains stale v4/thirteen-refusal metadata and unqualified copy-paste advocacy in the script header.

No remedy is proposed.

## Dispatch identity

Verified before content review:

- `CHI_CUSTODY_20260822.md`: `066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5` — exact dispatch match.
- `_evidence_20260822/verify.sh`: `5e0424def4b6970cad5e84be3a8ddcb8bc842273ce1cfb078d629aae8ce91ab6` — exact dispatch match.
- Prior gate `GATE_CHI_CUSTODY_EVIDENCE_V4_20260823.md`: `91b6fefb84e6c9681737e2f93a6b20034918f1c6c1468d578767e202dbb57b0d`.
- `CHI_CUSTODY_20260822_V4_SUPERSEDED.md`: `d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7`; this exactly equals the V4 document pin recorded by the prior gate.
- Revision 8 source `CHI_CUSTODY_RECEIPT_20260821.md`: `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`.

The V4 predecessor was created at `2026-08-23 15:12:35 +0900`; the v5 document and script mtimes are `2026-08-23 15:12:53 +0900`. The V4 predecessor therefore existed as the exact prior bytes before the v5 pair's current mtimes.

## Ranked findings

### 1. BLOCKING — P3's split is not an entry boundary, and P4 remains globally separable

Current-state fact first: the reviewed `archive.html` hash was `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`. It had 43 `<li>` blocks; the named `data-src`, exact value phrase, and report href token each occurred once, and one actual `<li>` contained all three. The target was block 23 using zero-based indexing. The desired association currently exists.

The predicate does not establish that association. P3 executes:

- split after `data-src="20260820T231235-hwao-report.mp3"`;
- then take everything before the next textual `data-src=`;
- then count the exact value phrase.

Three synthetic attacks re-executed those exact semantics:

1. Target entry first, but closed before the phrase: a following `<li>` placed the phrase before its own later `data-src`. P3 returned `1`; the target `<li>` contained zero phrases. With the report href in a third `<li>`, P4 also returned `1`, while no `<li>` contained all three predicates.
2. Target entry last: the target `<li>` closed, then a footer carried the phrase. With no later `data-src=`, P3 consumed through EOF and returned `1`; the target `<li>` again contained zero phrases.
3. Target entry genuinely carried the phrase but the target report href lived in another `<li>`. P3=`1`, P4=`1`, and no `<li>` contained the source, phrase, and href jointly.

Valid target-first and target-last fixtures also returned P3=`1`; the defect is not inability to handle first/last position. It is that “next `data-src=`” is not the close boundary of the entry. The first-position case can swallow the beginning of a later entry, and the last-position case is unbounded through EOF. The V4 separated-record decoy therefore survives in a stronger form.

### 2. MAJOR — the unchanged S1-S4 description still says four files carry content that two do not carry

Document lines 23-24 still describe S1-S4 as digest prefixes “of the four files carrying the 23:12 disclosure: mp3, caption, deck, alignment.” That text is unchanged from the exact V4 predecessor.

Independent literal scans found:

- the caption contains the full exact value phrase, sign summary, and `2,725 galaxies measured`;
- the deck does not contain the full exact phrase or sign summary; it contains positive numeric substrings and `0.640352` only inside a `REJECTED slide ... not in the audio` note, with no negative `-0.640352` exact disclosure;
- the alignment `times.json` contains none of the three values, the sign summary, or the 2,725 count.

The S1-S4 digest prefixes themselves are correct. The finding is the unchanged block description, not the hashes. This was V4 ranked finding 5 and is absent from the brief's claimed answer list.

### 3. MAJOR — “nothing leaves unannounced” remains false; the incomplete Revision-8 omission accounting was not answered

Document lines 55-60 retain the sentence “Not carried, so nothing leaves unannounced,” changing only the H2 clause. Direct comparison with Revision 8 still finds omitted, unannounced material:

- the `recorded_kst` timestamp and 52-minute relation to the authorization (Revision 8 lines 11-12);
- the `SOURCES SCANNED` inventory and `BLIND SPOTS` boundary (lines 206-215);
- fresh-ASR clearance of the 23:12 report and the full three-divergence accounting (lines 58-73);
- withdrawal of the internal ledger chain as custody evidence and the external-witness limitation (lines 75-100).

A bounded search of v5 for `recorded_kst`, `52 minutes`, `SOURCES SCANNED`, `BLIND SPOTS`, `fresh ASR`, `three divergences`, `ledger chain`, `external witness`, and `caption_corrected` returned zero matches. D1-D2 preserve one divergence but not the other two, the fresh-ASR clearance, or the sweep boundary. V5 correctly repairs only the H2 same-strength statement; it does not repair the other half of V4 ranked finding 3.

The sentence is also the clearest surviving arguing prose: the list itself is checkable; “so nothing leaves unannounced” is advocacy and is contradicted by the source comparison. Removing that clause loses no checkable item.

### 4. MAJOR — the v5 pair's own metadata and script-side history remain stale and internally inconsistent

The exact document is bylined `v5` at line 3 but still titled `CHI CUSTODY (v4)` at line 1. The exact script says `Executable custody claims, v4` at line 2 and “Thirteen gate refusals” at lines 3-4, while the document and dispatch say fourteen precede v5.

The script header also retains the unqualified claim at line 7: “what you see is what ran, copy-pasteable.” The document now correctly limits that statement to single-line commands under a standard PATH and identifies P1/P3 as multiline blocks. The execution mechanism passed under that stated environment; the finding is that the companion artifact's own description layer still carries the broader wording that V5 says it narrowed.

The script comments at lines 3-7 are also arguing history whose removal would lose nothing executed or checked. They attribute prior losses to a description layer, proclaim same-byte success, and assert copy-pasteability; none is part of the 26 runtime predicates.

## The six asserted V4 answers

| Brief item | Adjudication | Evidence |
|---|---|---|
| 1. Copy-paste promise restated at true strength | DOCUMENT HOLDS; PAIR PARTIAL | All 24 single-line commands and the P1/P3 multiline blocks reproduced in zsh/bash/sh from another directory with `PATH=/usr/bin:/bin:/usr/sbin:/sbin`. A stripped PATH is expressly disclaimed. Script line 7 still says merely “copy-pasteable.” |
| 2. P3/P4 decoy repaired by target-marker split | FAILS | P3 accepts the phrase in a later closed-separate entry before its `data-src`, and accepts a tail phrase after a last target entry; P4 accepts a report href in another entry. |
| 3. Literal decimal matching | HOLDS | S5 and the other literal greps use `-F`; P3 uses Python literal `.count`. The malformed `0X834336, 0Y384410, and -0Z640352` fixture returned P3=`0`. H2 and X3 use regex-inert underscore/hex strings; X3's `:0$` and Q1's ERE are intentionally structural regexes. No claim uses an unescaped decimal dot as a regex wildcard. |
| 4. X prose inference deleted | HOLDS | Lines 34-37 now state only two first lines and exact full-hash absence, then explicitly assign any consequence to the reader. No sentence saying the gates reviewed earlier revisions survives. |
| 5. H2 called narrower, deliberate, stated | HOLDS AS CHARACTERIZATION | Revision 8 lines 50-53 asserted no real-chi tertile artifact and no invocation within its evidence boundary. H2 only searches `handcheck/` for one literal tree name. “Narrower” is accurate; no same-strength claim survives. |
| 6. Arguing prose removed | FAILS | The opening paragraph is now factual/testimonial and the Q1 defense argument was cut, but “Not carried, so nothing leaves unannounced” remains both argumentative and false. The script header's history/copy-paste claims also remain non-executed advocacy. |

## L1: working claim, not pass-tuning

L1 holds as the claim working. The glob itself expanded to twelve distinct predecessor forms: eight receipt forms (Revision 8 base plus REV1-REV7) and V1-V4 superseded custody documents. The newly counted V4 file has SHA-256 `d090ca53...`, exactly the V4 dispatch pin, and predates the v5 pair's current mtimes. The transition 11→12 follows mechanically from preserving the newly superseded exact V4 bytes. A stray additional matching file would produce 13 and fail the fixed expected value, so this is not an always-pass count.

## Mechanism and claim adjudication

- Runtime: 26 claim invocations, 26 PASS, 0 FAIL, empty stderr, exit 0.
- Controlled prereg-directory and home-directory runs had byte-identical stdout SHA-256 `e4b0d63c82985c99735954604f316908d7f4bd199cd627e7edb28a91bc175175`.
- All 26 complete displayed command strings reproduced their shown values in `/bin/zsh -f`, `/bin/bash --noprofile --norc`, and `/bin/sh` with the standard PATH. No `$P`, `$R`, `${P}`, or `${R}` token remained in displayed commands.
- `claim()` eval-runs `$2` and later prints the same `$2`; no second curated command label exists. No eval/display divergence was found.
- G1/G2 independently recomputed from the CSV rather than trusting `geom.py`: 208,407 rows and variance `0.05798463739809634`, which prints as `0.057985`.
- H2's current scope exists: 31 regular files, zero symlinks, zero literal hits. This supports only the named-tree search.
- P1 has exactly one current matching publish row: ledger line 21, seq 20, `2026-08-20 23:12:51 KST`, `backfilled=true`, target mp3 filename.
- P2's full current report-page hash is `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`.
- P3/P4 current content holds in one real `<li>`; predicate adequacy fails as finding 1.
- X1-X3's primitives hold, and v5 no longer claims their former inference.
- L1 holds for the mechanical reason above.
- Q1's listed-token result is zero; it remains only a lexical tripwire.
- The final support statement holds against current source hashes: K-8 lines 32-33 bar summaries over chi and lines 48-50 bar publication; the decision memo lines 5-9 say DRAFT, ungated, unsigned, and not declined.

## Failed attacks / facts that held

- Both dispatch pins matched before review and at the pre-report recheck.
- The exact V4 predecessor matches the old dispatch pin, so supersession did not substitute different bytes.
- The one-string print/eval construction held under direct source inspection.
- Complete displayed commands reproduced across three shells and another working directory under the now-stated standard PATH.
- P1 and P3 paste and execute successfully as multiline blocks.
- Malformed decimal separators no longer pass S5/P3; literal-vs-regex handling is sound for the stated literal claims.
- Current `archive.html` genuinely has one target entry carrying the named source, exact phrase, and report href.
- X's earlier inferential sentence is deleted; the current X paragraph stops at facts.
- The H2 comparison with Revision 8 now calls the new predicate narrower rather than same-strength.
- L1's 12 is independently closed and caused by the exact newly superseded V4 file.
- Independent geometry, P1 uniqueness, H2 no-symlink inventory, K-8 clauses, and unsigned-draft status held.

## Evidence ledger

### Commands and probes

Read-only work included:

- pre-review, pre-report, and source-ledger `shasum -a 256` checks;
- full reads of the two dispatched artifacts, the V4 gate, exact V4 predecessor, Revision 8, K-8 authorization, decision memo, and `geom.py`;
- direct `/bin/zsh -f _evidence_20260822/verify.sh` execution;
- lane-local `_tmp_gate_ev5_probe.py` runs that extracted actual displayed command blocks, executed each under zsh/bash/sh from `/Users/duhokim`, independently recomputed geometry, counted P1 rows, inventoried H2/L1, parsed current `<li>` blocks, and ran first/last/separated-entry/malformed-decimal decoys;
- literal content scans of caption, deck, alignment, v5, Revision 8, and script;
- V4→v5 byte diff, metadata `stat`, filename inventories, and scoped read-only `git status`.

### SHA-256 ledger — core, current sources, and L1 set

Aliases: `P` is this prereg directory; `R` is `/Users/duhokim/HermesOps/reports/status-audio`.

- `066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5`  `P/CHI_CUSTODY_20260822.md`
- `5e0424def4b6970cad5e84be3a8ddcb8bc842273ce1cfb078d629aae8ce91ab6`  `P/_evidence_20260822/verify.sh`
- `91b6fefb84e6c9681737e2f93a6b20034918f1c6c1468d578767e202dbb57b0d`  `P/GATE_CHI_CUSTODY_EVIDENCE_V4_20260823.md`
- `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`  `P/K8_CROSSING_AUTHORIZATION_20260820.md`
- `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`  `P/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c`  `P/_evidence_20260822/geom.py`
- `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`  `P/_positions_20260820/positions_parent_20260820.csv`
- `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`  `P/GATE_FOOTPRINT_GEOMETRY_20260821.md`
- `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`  `P/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`
- `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`  `P/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`
- `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`  `R/20260820T231235-hwao-report.mp3`
- `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`  `R/20260820T231235-hwao-report.txt`
- `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`  `R/20260820T231235-hwao-report.deck.json`
- `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`  `R/20260820T231235-hwao-report.times.json`
- `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`  `R/report-20260820T231235-hwao-report.html`
- `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`  `R/archive.html`
- `e940179cfe1da1d17cfe5be08c0f8145991dfc65b24374885d0ac229653a52db`  `R/queue_ledger.jsonl`
- `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`  `R/20260821T151843-hwao-report.txt`
- `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848`  `R/20260821T151843-hwao-report.times.json`

L1's twelve reviewed names and hashes:

- `2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866`  `P/CHI_CUSTODY_20260822_V1_SUPERSEDED.md`
- `3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d`  `P/CHI_CUSTODY_20260822_V2_SUPERSEDED.md`
- `1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29`  `P/CHI_CUSTODY_20260822_V3_SUPERSEDED.md`
- `d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7`  `P/CHI_CUSTODY_20260822_V4_SUPERSEDED.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `P/CHI_CUSTODY_RECEIPT_20260821.md`
- `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e`  `P/CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md`
- `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c`  `P/CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md`
- `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093`  `P/CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md`
- `acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b`  `P/CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md`
- `2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65`  `P/CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md`
- `5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043`  `P/CHI_CUSTODY_RECEIPT_20260821_REV6_SUPERSEDED.md`
- `879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e`  `P/CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md`

### SHA-256 ledger — H2's 31-file traversal set

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

### SHA-256 ledger — first-line/history-search artifacts and permitted probe

These files were content-read only at matched first-line/history snippets unless already listed above:

- `ffe19920a8465582269ad666a44d61375e92216b19bf90b5680bec18dc2c9eb1`  `P/GATE_CHI_CUSTODY_EVIDENCE_20260822.md`
- `3c2cb2de4882fb0c7bb28f611d64f9316c96e80850acd90a92516d11ae29c9ec`  `P/GATE_CHI_CUSTODY_EVIDENCE_V2_20260822.md`
- `e7900c1f7429b1ae91b8440cdfaad089175b4c1734033452e21112b34a0024f1`  `P/GATE_CHI_CUSTODY_EVIDENCE_V3_20260823.md`
- `19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083`  `P/GATE_CHI_CUSTODY_R6_20260821.md`
- `06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa`  `P/GATE_CHI_CUSTODY_R7_20260821.md`
- `df6c92d785b4db9af455af32f4a74ba1096761120bd9983284e02b4a08b48501`  `P/GATE_CHI_CUSTODY_R8_20260821.md`
- `635ed8e6bda6b20fe8ae3283a8d89cbecb83037245981b96ff373a253dbd8b7a`  `P/_tmp_gate_r8_report_complete.md`
- `df52c2031b1508f27768710ece0ca7d7cf03b33c394159b7a00b4781d7af7532`  `P/_tmp_gate_r8_report_body.md`
- `19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083`  `P/_tmp_gate_r8_repro/GATE_CHI_CUSTODY_R6_20260821.md`
- `06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa`  `P/_tmp_gate_r8_repro/GATE_CHI_CUSTODY_R7_20260821.md`
- `2b5fe78b64161bccb19da2cbbc41745ab9d6c1e99eb309d759e0fea64190cf8a`  `P/_custody_20260821/_gated/CHI_CUSTODY_20260822.2b5fe78b6416.md`
- `066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5`  `P/_custody_20260821/_gated/CHI_CUSTODY_20260822.066dc90bb17f.md`
- `d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7`  `P/_custody_20260821/_gated/CHI_CUSTODY_20260822.d090ca53afd2.md`
- `816af5a72ab0e053edae5cfa110d07fc7779dc3da141a93b47fee539b6488b70`  `P/_tmp_gate_ev5_probe.py`

## Boundaries and uncertainty

- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read.
- No fresh ASR was run and the mp3 was hash-read only. Audio-truncation statements are bounded to the reviewed Revision-8 record and unchanged source hashes.
- No external publication platform was inspected. Current publication claims were tested against the local ledger and local served artifacts.
- No source, gate, git state, database, process, or public artifact was changed.
- Writes were limited to this report and `P/_tmp_gate_ev5_probe.py`. The pre-existing zero-byte `_tmp_gate_ev5_stdout.log` and `_tmp_gate_ev5_stderr.log` were names/stat-listed only and never opened or attributed to this pass.
- The target document and script were already modified in scoped git status before this report; the V4 predecessor and V4 gate were already untracked. The probe is ignored by repository status.
