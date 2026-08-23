REFUTED_CHI_CUSTODY_EVIDENCE_V6

# Adversarial gate — `CHI_CUSTODY_20260822.md` v6 and `_evidence_20260822/verify.sh`

## Executive verdict

Both dispatched artifacts matched their pinned SHA-256 values before content review and at the pre-report recheck. The current script ran 26 claims with 26 PASS, 0 FAIL, and exit 0. The current archive also genuinely has one explicitly closed target `<li>` whose visible text contains the exact three-value phrase and whose `<a href>` points to the named report.

The pair is nevertheless refuted. P3/P4 still have false-pass routes because they use a raw-source slice ending at the first textual `</li>` and raw substring counts rather than parsed entry text and an actual `href`. P1 independently accepts an unrelated filename containing `231235` while the target report is absent. The document also retains stale/inaccurate v4 metadata and makes current audio/decision-memo assertions that no printed command checks.

No remedy is proposed.

## Dispatch identity

Verified before review and again immediately before this report:

- `CHI_CUSTODY_20260822.md`: `0b12eaf43a0e35fb95eaadc2447663f226451442c0299bd9bd7609fcf352a766` — exact dispatch match.
- `_evidence_20260822/verify.sh`: `4cb623632d0ec23e0dea3a6f51bb484ee641c69c85ece935653cdd84ee5241b7` — exact dispatch match.
- Prior named gate `GATE_CHI_CUSTODY_EVIDENCE_V5_20260823.md`: `086035f77b9d45a02a90cc59ef09b76e9f676cad9bcb25edaa8d9fd261f7e05a`.
- Exact retained v5 predecessor `CHI_CUSTODY_20260822_V5_SUPERSEDED.md`: `066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5`, exactly the v5 document pin recorded by the prior gate.

The v5 gate mtime was `2026-08-23 15:30:01 +0900`; the exact retained v5 predecessor and current v6 document have mtimes `2026-08-23 15:31:39 +0900`. The predecessor therefore binds the dispatched v5 bytes and the newly added L1 member is not an unrelated same-pattern file.

## Ranked findings

### 1. BLOCKING — P3/P4 still accept content from outside the target entry and accept non-content attributes

The revised predicates are:

- find the raw target opener;
- slice from there to the first textual `</li>` after it;
- count the value phrase or report token anywhere in those raw bytes.

That repairs the v5 explicit-close decoy but does not prove the document's claim that the slice ends at the target element's own close, nor that P3 found visible text or P4 found an `href`.

#### Omitted-target-close / sibling-entry false pass

The probe supplied an HTML optional-end-tag form with no explicit close after the target entry:

- target entry: `data-src` is the named MP3; visible text is only `No disclosure here.`;
- next sibling entry: carries the exact value phrase and an actual report link;
- the next sibling has the first explicit `</li>` in the source.

P3 and P4 both returned `1`. `/usr/bin/xmllint --html --recover --format -` parsed the same bytes into two sibling `<li>` elements and emitted an explicit close after the target's `No disclosure here.` text; the phrase and link remained in the second sibling. Thus the textual first-`</li>` slice consumed the sibling and falsely passed both association claims.

#### Same-entry attribute-only false pass

A well-closed target entry put the value phrase in `data-values` and the report token in `data-report`; its visible text was `No disclosure here.` and it contained no `<a href>`. Exact P3/P4 semantics returned `(1, 1)`. A standard-library `HTMLParser` extraction returned visible-value count `0` and matching-href count `0`.

This directly contradicts the prose at `CHI_CUSTODY_20260822.md:46-47`, which calls the second token a “report href,” and the surrounding “served surfaces” characterization. The command checks a raw report-name substring, not an href.

#### Attacks that failed safely

- With explicit target close and the href in a later entry, P3/P4 returned `(1, 0)`: the requested P4 decoy now fails.
- With explicit target close and the value phrase in a later entry, P3/P4 returned `(0, 1)`.
- A raw literal `</li>` inside a quoted target attribute before genuine visible content truncated the slice and returned `(0, 0)`: false negative, not false pass.
- With the target opener absent, Python raised `ValueError`; `claim()` suppressed the exception text, captured empty stdout, printed `FAIL P3 ... actual  :` with a blank actual value, and exited nonzero. This defaults to failure but is diagnostically the “confusing empty” case in the brief.

#### Current-state fact

Current `archive.html` remained SHA-256 `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`. It has one target opener; the extracted target source has one `<li>` opener and one explicit `</li>`, one exact visible value phrase, one report token, and one actual `href="report-20260820T231235-hwao-report.html"`. Current content is associated correctly; predicate adequacy is refuted.

### 2. BLOCKING — P1 can pass with the target publication absent

P1 tests:

```text
r.get('event') == 'publish' and '231235' in str(r.get('file', ''))
```

It then prints only sequence, timestamp, and `backfilled`; it neither exact-matches nor prints the filename. The exact loop body was re-executed against a one-row ledger containing only:

```text
file = unrelated-231235-decoy.mp3
seq = 20
stamp_kst = 2026-08-20 23:12:51 KST
backfilled = true
```

It printed the exact expected value:

```text
20 2026-08-20 23:12:51 KST backfilled=True
```

The target report was absent. This is a separate wrong-record false-pass route for the document's “publication event” claim at `CHI_CUSTODY_20260822.md:43-45`.

The current ledger itself holds: it has one substring-matching publish row and one exact-filename publish row, both the real `20260820T231235-hwao-report.mp3`. The finding is the predicate's acceptance set, not a claim that the current ledger row is wrong.

### 3. MAJOR — v6 metadata and execution prose remain stale or inaccurate

Four current statements fail direct source comparison:

1. `CHI_CUSTODY_20260822.md:1` still titles the document `CHI CUSTODY (v4)` while line 3 and the dispatch call it v6.
2. The v6 byline still says `2026-08-23 14:55 KST`, byte-for-byte unchanged from the retained v5 predecessor. That time precedes the v5 gate at 15:30 and the current v6 mtime at 15:31. It is not current revision metadata.
3. Lines 12-13 say P1 and P3 are the multiline Python claims. Current source has three multiline Python claims: P1, P3, and newly changed P4. The extracted P4 block did execute successfully in clean zsh, bash, and sh with the stated standard PATH, but the document's enumeration is incomplete.
4. Lines 17-18 say the strings have “no runtime interpolation beyond the two path prefixes.” G1's displayed and executed string contains eval-time arithmetic and command substitution: `echo $(( $(wc -l < ...csv) - 1 ))`. The path prefixes are not the only runtime interpolation in a claim string.

The script-side header is current: it says v6, fifteen refusals, and qualifies single-line versus multiline commands without claiming all commands are one line. Q1 does not detect any of the four defects above.

### 4. MATERIAL — two reader-facing assertions remain outside the printed-command evidence

#### D1 audio conclusion

`CHI_CUSTODY_20260822.md:39-42` says ASR established that the `151843` audio ends before `200,000 times`, calls the audio defective, and explains why the caption is not amended. D1 checks only that the authored caption contains the phrase. D2 reads only alignment coverage `0.9709`. The script contains no `151843` MP3 path, no MP3 hash, and no audio/ASR command.

The current MP3 is still SHA-256 `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3`, duration `162.312`; the caption and times hashes also match earlier gate records. That externally preserves the earlier ASR conclusion, but the v6 pair can continue to pass if the MP3 changes because neither D1 nor D2 reads it. The prose says more than its printed commands back.

#### Decision-memo status

`CHI_CUSTODY_20260822.md:67` says the decision memo remains a draft, unsigned, and the study has not been declined. No command in `verify.sh` reads or hashes `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`.

The statement is currently true on direct inspection: the memo is SHA-256 `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`, and lines 5-9 say DRAFT, no gate/signature, and not declined. The finding is executable coverage: this source can change without affecting the 26 PASS result.

## The five asserted v5 answers

| Brief item | Adjudication | Evidence |
|---|---|---|
| 1. P3/P4 bounded by target entry's `</li>` | **REFUTED** | Explicit-close separated entries now fail in the safe direction, but an omitted target close makes the first textual close belong to the next sibling and both predicates pass. Attribute-only values also pass. Target absence produces a FAIL with blank diagnostic output. |
| 2. P4 decoy in another entry | **HOLDS ONLY FOR EXPLICITLY CLOSED TARGET SOURCE** | The requested explicit sibling-entry decoy returned P4=`0`. The omitted-close sibling and same-entry non-href attribute routes still return P4=`1`. |
| 3. S1-S4 relabelled from “carrying” | **SUBSTANTIVE RELABEL HOLDS** | The exact deck has five slides and does not present the three values; the number strings occur only in its rejected-slide note, with no exact `-0.640352`. The alignment JSON contains timing/coverage only. The page and archive embed the exact five slide objects and matching slide times. The caption contains the exact values; the unchanged MP3 hash is tied by the reviewed R6 ASR gate to three independent transcriptions of those values. S3/S4 themselves remain local digest checks, not publication-association checks. |
| 4. “a list, not a promise” | **HOLDS** | The revised sentence expressly disclaims completeness and states that a prior gate found the list incomplete. Revision 8 still contains material not named in the list, but v6 no longer promises otherwise. |
| 5. stale header/copy-paste metadata | **PARTIAL / FAILS AS A PAIR** | Script header now says v6/fifteen and qualifies multiline commands. Document title remains v4; its revision time remains the v5 time; it omits multiline P4; and its no-runtime-interpolation sentence is false as written. |

## L1: thirteen holds mechanically

L1 expanded to thirteen distinct top-level predecessor forms: eight receipt forms and five V1-V5 superseded custody documents. The new V5 member is SHA-256 `066dc90b...`, exactly the prior gate's v5 dispatch pin. The prior gate predates the V5 predecessor/current-v6 mtimes. A fourteenth matching path would make the fixed expected value fail, so the count is not always-pass tuning.

The dispatch premise that fifteen adversarial refusals precede v6 was treated as instructed. L1 is a separate claim about thirteen superseded forms, not a machine count of refusal reports.

## Mechanism and other claim adjudication

- Runtime: script self-reported SHA-256 `4cb623...`; 26 claim invocations; 26 PASS; 0 FAIL; exit 0.
- `claim()` still eval-runs `$2` and prints the same `$2`; no second curated label was found.
- The newly multiline P4 command extracted from actual script stdout returned `1` with empty stderr in `/bin/zsh -f`, clean `/bin/bash --noprofile --norc`, and `/bin/sh`, from `/Users/duhokim` under `PATH=/usr/bin:/bin:/usr/sbin:/sbin`.
- S1-S7 current digests and literal caption strings hold.
- F1-F4 current digest prefixes and literal-source occurrences hold. Direct K-8 inspection confirms §4's publication bar and condition 2's no-summary language.
- G1 independently closed at 208,407 data rows. Independent CSV recomputation using the constants in `geom.py` gave population variance `0.057984637398096485`, formatting to `0.057985`.
- H2's current traversal set has 31 regular files, zero symlinks, and zero literal target-tree-name hits. This remains only a statement about that directory search.
- X1-X3's printed primitives hold.
- D1's caption fact and D2's stored coverage field hold; their audio conclusion is finding 4.
- P2's full report-page hash is `050a3f...`; current P3/P4 content holds in the real target entry, while their false-pass acceptance set is finding 1.
- Q1 returns zero and accurately calls itself only a listed-word tripwire.
- Direct source inspection supports the final §4/condition-2 breach statement and the current unsigned-draft status; the latter is not covered by the script.

## Failed attacks / facts that held

- Both dispatch pins matched before review and immediately before report writing.
- Exact v5 predecessor identity and L1's 13-member closure held.
- The one-string display/eval construction held; no mechanism-level display/execution divergence was found.
- Newly multiline P4 pasted and ran across all three tested shells under the document's PATH qualification.
- The requested explicit-close P4 decoy in another entry failed.
- Missing target source caused an overall claim failure and nonzero exit rather than a pass.
- Current archive source genuinely has an explicitly closed target entry with visible exact values and an actual matching href.
- The S1-S4 relabel no longer claims the deck/alignment carry the values. Deck/page/archive/timing cross-comparison supported their same-report relationship.
- The revised Revision-8 omission paragraph is candidly a non-exhaustive list, not a completeness promise.
- Script-side v6/fifteen header metadata is current.
- Geometry, H2 current scope, X primitives, caption literals, K-8 source clauses, and the current decision-memo status held.

## Evidence ledger

Aliases below: `P` is this prereg directory; `R` is `/Users/duhokim/HermesOps/reports/status-audio`.

### Commands and probes

Read-only execution included:

- pre-review and pre-report `shasum -a 256` identity checks;
- full reads of the dispatched document/script, named v5 gate, exact v5 predecessor, Revision-8 receipt, relevant R6 exact-hash ASR record, K-8 authorization, decision memo, captions, deck, timing JSONs, report page, and `geom.py`;
- `/bin/zsh -f P/_evidence_20260822/verify.sh`;
- independent CSV row/variance recomputation;
- current ledger exact/substr match enumeration and archive target extraction;
- lane-local `_tmp_gate_ev6_probe.py` tests for explicit-entry decoys, attribute-only values, omitted-close sibling capture, literal-close truncation, missing-target behavior, current target content, P1 selection, and P4 shell replay;
- `/usr/bin/xmllint --html --recover --format -` on the omitted-close fixture;
- exact P1 loop execution against `_tmp_gate_ev6_p1_decoy.jsonl`;
- v5-to-v6 byte diff, mtimes, L1 hashes, handcheck traversal hashes/symlink count, scoped git status, and gate first-line inventory.

### SHA-256 — dispatched pair, named prior, and principal sources

- `0b12eaf43a0e35fb95eaadc2447663f226451442c0299bd9bd7609fcf352a766`  `P/CHI_CUSTODY_20260822.md`
- `4cb623632d0ec23e0dea3a6f51bb484ee641c69c85ece935653cdd84ee5241b7`  `P/_evidence_20260822/verify.sh`
- `086035f77b9d45a02a90cc59ef09b76e9f676cad9bcb25edaa8d9fd261f7e05a`  `P/GATE_CHI_CUSTODY_EVIDENCE_V5_20260823.md`
- `066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5`  `P/CHI_CUSTODY_20260822_V5_SUPERSEDED.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `P/CHI_CUSTODY_RECEIPT_20260821.md`
- `19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083`  `P/GATE_CHI_CUSTODY_R6_20260821.md`
- `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`  `P/K8_CROSSING_AUTHORIZATION_20260820.md`
- `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`  `P/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`  `P/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`
- `3739020515d5a7fbfc6854e4bcf29051cfac4ecf687ebe3e19f0d9e200e6c07c`  `P/_evidence_20260822/geom.py`
- `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`  `P/_positions_20260820/positions_parent_20260820.csv`
- `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`  `P/GATE_FOOTPRINT_GEOMETRY_20260821.md`
- `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`  `P/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`

### SHA-256 — report surfaces and D1 artifacts

- `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`  `R/20260820T231235-hwao-report.mp3`
- `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`  `R/20260820T231235-hwao-report.txt`
- `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`  `R/20260820T231235-hwao-report.deck.json`
- `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`  `R/20260820T231235-hwao-report.times.json`
- `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`  `R/report-20260820T231235-hwao-report.html`
- `c7085da9f63244e1c40d0f8c7e328ce3a41c69887a81e9fff7e32798f32b2edb`  `R/archive.html`
- `e940179cfe1da1d17cfe5be08c0f8145991dfc65b24374885d0ac229653a52db`  `R/queue_ledger.jsonl`
- `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3`  `R/20260821T151843-hwao-report.mp3`
- `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`  `R/20260821T151843-hwao-report.txt`
- `bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848`  `R/20260821T151843-hwao-report.times.json`

### SHA-256 — L1's thirteen members

- `2d56a952dff88bc175c1ebec3acbc1e0bf43a45cfe25fa4c79a598f11f920866`  `P/CHI_CUSTODY_20260822_V1_SUPERSEDED.md`
- `3a9ee82201e3f4f132d8540387a766805015b5c662a1e69a43006b76a141c97d`  `P/CHI_CUSTODY_20260822_V2_SUPERSEDED.md`
- `1c036d1861267b820ebd3d85382e6cc417b881750d374473c202108cacd01f29`  `P/CHI_CUSTODY_20260822_V3_SUPERSEDED.md`
- `d090ca53afd2d2ff82794f7ae1eb2a2e398d97e795862f1f051e3af1a43296e7`  `P/CHI_CUSTODY_20260822_V4_SUPERSEDED.md`
- `066dc90bb17ff7f30557d086850a702e660d7c796755252bab650060a07339e5`  `P/CHI_CUSTODY_20260822_V5_SUPERSEDED.md`
- `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`  `P/CHI_CUSTODY_RECEIPT_20260821.md`
- `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e`  `P/CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md`
- `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c`  `P/CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md`
- `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093`  `P/CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md`
- `acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b`  `P/CHI_CUSTODY_RECEIPT_20260821_REV4_SUPERSEDED.md`
- `2a237fc48a582c68b5ed9afe89c527bed5e650e0c9b70e97e1b95e02d7b19e65`  `P/CHI_CUSTODY_RECEIPT_20260821_REV5_SUPERSEDED.md`
- `5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043`  `P/CHI_CUSTODY_RECEIPT_20260821_REV6_SUPERSEDED.md`
- `879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e`  `P/CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md`

### SHA-256 — first-line-only refusal-report inventory

- `19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083`  `P/GATE_CHI_CUSTODY_R6_20260821.md`
- `06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa`  `P/GATE_CHI_CUSTODY_R7_20260821.md`
- `df6c92d785b4db9af455af32f4a74ba1096761120bd9983284e02b4a08b48501`  `P/GATE_CHI_CUSTODY_R8_20260821.md`
- `ffe19920a8465582269ad666a44d61375e92216b19bf90b5680bec18dc2c9eb1`  `P/GATE_CHI_CUSTODY_EVIDENCE_20260822.md`
- `3c2cb2de4882fb0c7bb28f611d64f9316c96e80850acd90a92516d11ae29c9ec`  `P/GATE_CHI_CUSTODY_EVIDENCE_V2_20260822.md`
- `e7900c1f7429b1ae91b8440cdfaad089175b4c1734033452e21112b34a0024f1`  `P/GATE_CHI_CUSTODY_EVIDENCE_V3_20260823.md`
- `91b6fefb84e6c9681737e2f93a6b20034918f1c6c1468d578767e202dbb57b0d`  `P/GATE_CHI_CUSTODY_EVIDENCE_V4_20260823.md`
- `086035f77b9d45a02a90cc59ef09b76e9f676cad9bcb25edaa8d9fd261f7e05a`  `P/GATE_CHI_CUSTODY_EVIDENCE_V5_20260823.md`

### SHA-256 — H2's 31-file traversal set

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

### SHA-256 — permitted gate probes

- `a35f5290a9fb2f4c201c3f1fc18ae1d4f7c46f7eb0c0f85d46807f5fb40eaeb8`  `P/_tmp_gate_ev6_probe.py`
- `a228b4af32318ea5f69b8b6bfb445ee7885ea04607aceef66f3eb933ca345d78`  `P/_tmp_gate_ev6_p1_decoy.jsonl`

Filename inventories were names-only unless listed above. Broad content searches were reconnaissance; only artifacts and exact snippets named in this report were relied upon.

## Boundaries and uncertainty

- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read.
- No fresh ASR was run. The 23:12 and 15:18 audio-content statements are bounded to unchanged current MP3 hashes and the reviewed prior exact-hash ASR records; current media were hash/metadata-read only.
- No external publication platform was inspected. Publication and served-surface findings are bounded to the local ledger, local report tree, and reviewed receipt/gate records.
- No source, script, gate predecessor, database, process, git state, or published artifact was changed.
- Writes were limited to this report and the two permitted `P/_tmp_gate_ev6_*` probes named above.
- Scoped pre-report git status showed the target document and script already modified, and the v5 gate already untracked. The gate probe paths are ignored by repository status.
