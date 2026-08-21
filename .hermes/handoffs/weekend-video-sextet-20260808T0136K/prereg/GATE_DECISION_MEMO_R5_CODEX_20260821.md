REFUTED_DECISION_MEMO_R5

# Cross-engine adversarial gate — Decision Memo Revision 5 only

## Verdict

Revision 5 is **REFUTED**. The requested repairs do not close the memo. Four independently material defects survive: the DRAFT repeatedly states the decline and resulting study status as already operative; the claim that Revision 4 is retained byte-for-byte is contradicted by the prior gate's pinned Revision-4 hash; the archive pages are multi-reading but their own HTML does attribute each reading to a report, so “not attributable to a particular report” is false; and the memo pins a stale SHA-256 for the generator it names. The footprint arithmetic, condition-1 conclusion on the searchable record, seq-21/22 publication evidence, MP3 identity, and central outside-preregistration procedural theory survived independent attack.

The custody receipt was read only as a source required by this brief. It was not gated as a deliverable here. No remedy is proposed.

## Attack 1 — footprint digests, exact gate citations, and fresh generator output

### Independently computed footprint SHA-256

- Rev1: `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md` — `f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee`
- Rev2: `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md` — `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76`
- Rev3/current: `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` — `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`

### Every `GATE_*.md` exact-digest citation

The map below is exact in the final tree. This required output itself contains all three exact digests above and therefore cites all three; that self-citation is stated explicitly rather than silently omitted.

- Rev1 is cited by:
  - `GATE_DECISION_MEMO_FINAL_20260821.md`
  - `GATE_DECISION_MEMO_R3_20260821.md`
  - `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`
  - `GATE_DECISION_MEMO_R5_CODEX_20260821.md` (this report)
- Rev2 is cited by:
  - `GATE_DECISION_MEMO_20260821.md`
  - `GATE_DECISION_MEMO_FINAL_20260821.md`
  - `GATE_DECISION_MEMO_R2_20260821.md`
  - `GATE_DECISION_MEMO_R3_20260821.md`
  - `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`
  - `GATE_VOID_ON_DESIGN_DEFECT_20260821.md`
  - `GATE_DECISION_MEMO_R5_CODEX_20260821.md` (this report)
- Rev3/current is cited by:
  - `GATE_CHI_CUSTODY_R6_20260821.md`
  - `GATE_DECISION_MEMO_20260821.md`
  - `GATE_DECISION_MEMO_FINAL_20260821.md`
  - `GATE_DECISION_MEMO_R2_20260821.md`
  - `GATE_DECISION_MEMO_R3_20260821.md`
  - `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md`
  - `GATE_VOID_ON_DESIGN_DEFECT_20260821.md`
  - `GATE_DECISION_MEMO_R5_CODEX_20260821.md` (this report)
- `GATE_FOOTPRINT_GEOMETRY_20260821.md` cites none of the three exact digests.

Thus Revision 5's generated conclusion `Revisions whose hash is cited by NO gate: (none)` is correct. Citation still does not establish which bytes a gate reviewed.

### Fresh generator comparison

Before this required output existed, a fresh execution of `_custody_20260821/build_custody_tables.py` produced 3,771 bytes at SHA-256 `e213ebe35a54abebbc1eeb5f0605ae0fb19775c295b64510869f885884e9e686`. The memo's sole fenced block is 1,356 bytes and was byte-identical to a contiguous slice at byte offset 192, including its final newline. That attack failed as a slice comparison.

It was not the complete current A section: the 192 bytes before the slice include the heading and the now-existing `GATE_CHI_CUSTODY_R6_20260821.md` row. More importantly, the memo's composed source pin is false: memo line 43 names generator SHA-256 `681592ffea67b862b5a33444b2af354a0c03594889368ad1c5697d93c6fbd8f8`, while the named current file hashes to `aac8f56211c19bbe1ecfa8ff81145b63f096f35d5acffc2cf4ddb98504dfe6f0`.

After this required gate report was written, a fresh run produced 3,912 bytes at SHA-256 `8cd27a33a69aa89cfd9e9d55bf9fd79c75ec150af872a21325522084068c03c6`. The new row is `GATE_DECISION_MEMO_R5_CODEX_20260821.md / REFUTED_DECISION_MEMO_R5 / Rev1, Rev2, Rev3(current)`. It falls between the memo's R3 and declaration rows, so the memo's fenced block is no longer even a contiguous slice (`find = -1`). The generated gate-history paste is therefore non-closing under the very gate required to approve it.

## Ranked findings

### 1. BLOCKING — the DRAFT says the decline and study status are already operative

Lines 3–4 correctly say `DRAFT`, `Not effective`, no gate/signature, and `NOT in force`. The body contradicts that boundary in unqualified present language:

- lines 16–17: “the investigator **chooses not to carry the study further**”;
- line 21: “It **is adopted** because that ruling is right”;
- line 100: “the expenditure **being declined**”;
- lines 116–120, under “Resulting status”: “**Halted by investigator decision**” and “this study ... **reports nothing**”;
- lines 157–158: “a memo **halting a study** on integrity grounds”;
- lines 160–163, under “What continues”: “**Acquisition runs to completion**.”

These are not descriptions of what would follow signature; they are declarations of current decision, current status, and current continuation policy. A disclaimer at the top does not make the later operative sentences non-operative. The requested status confirmation therefore fails.

### 2. BLOCKING — Revision 4 is not retained byte-for-byte against the bytes the FINAL gate pinned

Revision 5 lines 4–5 say Revisions 1–4 are retained byte-for-byte. Rev1–Rev3 match their earlier gate pins:

- Rev1 `a683bc9424f26fdeabccd414aecdc0b67f08bab86307015e68294612d6a7a5bb`
- Rev2 `7e1b2e2f4f104ce171c6e9e50ed843ef70417a5f76216bf4e0618b0163ded64f`
- Rev3 `bafec8bf5f177830d4eeac75a0a7b29c72ea9b7dcfedd3b33f697a283836c62d`

Rev4 does not. `GATE_DECISION_MEMO_FINAL_20260821.md:164` records the then-current Revision-4 memo as `eeb033ab8e32bd58f2360243d220f2d08f7fb85de2f76fc5e42d556c3010d342`. The present `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV4_SUPERSEDED.md` hashes to `d69be7af81613c3f6a103e5ff833778dd4c036a3e121ac131852d459b38a6efd`, and its mtime (21:37:59 KST) is later than the FINAL gate (20:35:48 KST). Its own text also calls the alongside receipt “Revision 6,” while the FINAL gate identifies its reviewed pair as Memo Revision 4 / Receipt Revision 5. The exact-retention claim is refuted.

### 3. BLOCKING — “multi-reading” is true, but “not attributable to a particular report” is false

The old detector defect is real. Current `archive-2.html` has zero occurrences of all of the following: `first 3 real values`, `zero point 27`, `zero point 20`, `minus zero point 20`, `one leaning each way`, and `0.013161621987819672`. Its `VALUE(words)` hits are unrelated older speech: footprint `zero point 13`, sign-convention `minus zero point 12`, sigma/floor values, and other pre-crossing numbers.

Revision 5 no longer says those empirical values survive in `archive-2.html`; that deletion is honest. Its replacement explanation is not. `archive.html` is multi-reading, but the HTML wraps the exact disclosure in:

- `<li data-src="20260820T231235-hwao-report.mp3" ...>`;
- an adjacent `23:12` time/duration row;
- the exact value/sign narration;
- a link to `report-20260820T231235-hwao-report.html`.

Likewise, the unrelated `zero point 13` speech in `archive-2.html` sits inside `<li data-src="20260814T163726-session-summary.mp3" ...>`. The source pages concatenate readings while preserving explicit per-reading identity. The detector discards those boundaries; the pages do not. Memo lines 133–135 convert a detector limitation into a false source claim, so treating the archive match as “not attributable to a particular report” is evasion, not an accurate repair.

Only `archive.html` contains the empirical three-value/sign/exemplar material. `archive-2.html` through `archive-5.html` contain none of those exact needles.

### 4. MATERIAL — the memo falsely says the receipt “is generated rather than composed”

Memo lines 124–126 describe the Revision-6 receipt as generated rather than composed and as stopping assertion in favor of pasted tool output. The receipt has one generated fenced block, but also composed sections headed “Why there have been six revisions,” “Corrections carried into this revision,” “The breach,” “Limits,” and “Boundary,” including new universal claims. This gate does not adjudicate that receipt as a deliverable; it does adjudicate the memo's sentence about it, and that sentence is false as written.

### 5. MATERIAL cross-reference seam — target correction holds, named successor text does not

Inside Revision 5, no surviving positive sentence says a verdict estimator was built, gated, or frozen. Name scans found no `_verdict_20260821/` directory and no `verdict_runner.py`; `VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md:7–13,47–50` explicitly says implementation does not exist and defines work to build. The memo does not inherit the receipt's false `no code path computes an aggregate` wording.

The named successor note remains inconsistent: `SUCCESSOR_SCOPE_20260821.md:85–87` says “The verdict estimator built under [the spec] becomes the starting point.” That is not a surviving sentence inside the target memo, so it does not refute the target correction by itself, but the line-163 cross-reference still points readers to a false external sentence.

## Attack 2 — detector reality and real-chi tertile search

### Harness behavior

`handcheck/nm_handcheck.py` does compute chi strata. It accepts `authorized_measurement` rows, ranks `abs_chi` (`_rank_tertiles`, lines 279–290), computes real-population cutpoints (lines 557–579), builds the nine `committee_state|tertile` strata, and writes `stratum_populations` to preparation artifacts (lines 490–504). Revision 5 does not repeat the false universal no-code-path claim.

### Search for a real-chi invocation

The on-tree evidence supports the memo's condition-1 conclusion:

- A whole-repository content walk (no symlink following; `.git`, virtual environments, caches, and `node_modules` pruned) found no executable invocation coupling `nm_handcheck` or `--real-population` to `chi_dr10_south`.
- The only current executable source containing the real tree name is `_inference_20260820/chi_wrapper.py`; it does not reference the hand-check harness.
- The only five within-1,000-character co-occurrences were this brief, the Revision-6 custody gate, its audit script/evidence JSON, and the receipt — audit prose/code, not a harness invocation.
- Git contains two historical `nm_handcheck.py` blobs: `cc88fa5e…` at commit `199c3168…` and `65c04377…` at `0923db16…`; neither contains `chi_dr10_south`.
- Four commits in the handoff history change or carry the real-tree token. At each tree, no file containing that token also contains `nm_handcheck`.
- `run_hc1h_stage.sh` is a generic argument-forwarding wrapper and contains no data path.
- A name/content scan found eight canonical prepare/commitment artifacts, all under `_rehearsal_20260820`; none exists outside that directory.

The universal “never” cannot close arbitrary deleted/off-tree shell activity, but the complete current tree, available git history, and extant outputs contain no evidence of a real-chi invocation or tertile. No real-chi tertile was found; condition 1 is not established as breached.

### Every generated output under `handcheck/` dated

The output class here is every `.json` and `.log` under `handcheck/` (21 files). All are synthetic self-test/test/independent-verification artifacts, contain no `chi_dr10_south`, and predate the 2026-08-20 crossing. Their filesystem mtimes are:

- `handcheck/hc1h_full_test_stderr.log` — 2026-08-15 02:56:31 KST — `9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8`
- `handcheck/hc1h_full_test_stdout.log` — 2026-08-15 02:56:25 KST — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `handcheck/hc1h_independent_stderr.log` — 2026-08-15 02:56:39 KST — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `handcheck/hc1h_independent_stdout.log` — 2026-08-15 02:56:40 KST — `51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb`
- `handcheck/hc1h_independent_verification.json` — 2026-08-15 11:19:20 KST — `19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8`
- `handcheck/hc1h_selftest_stderr.log` — 2026-08-15 02:56:31 KST — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `handcheck/hc1h_selftest_stdout.log` — 2026-08-15 02:56:39 KST — `a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b`
- `handcheck/hc1h_synthetic_selftest_receipt.json` — 2026-08-15 11:19:28 KST — `25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40`
- `handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stderr.log` — 2026-08-14 22:47:32 KST — `ebe607be44c62c552a845f0cbdb5986fa5c7c0d53eff9bddd575a5c37ae4a5`
- `handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stdout.log` — 2026-08-14 22:47:28 KST — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `handcheck/superseded_hc1_20260815/full_test_stderr.log` — 2026-08-14 23:07:55 KST — `148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b`
- `handcheck/superseded_hc1_20260815/full_test_stdout.log` — 2026-08-14 23:07:53 KST — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `handcheck/superseded_hc1_20260815/independent_stderr.log` — 2026-08-14 23:07:36 KST — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `handcheck/superseded_hc1_20260815/independent_stdout.log` — 2026-08-14 23:07:36 KST — `b4f51b589170659f0be7c6e38d93c81e35b13a13e4813ede694f9e9bf4a2de63`
- `handcheck/superseded_hc1_20260815/independent_verification.json` — 2026-08-14 23:07:36 KST — `54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae`
- `handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_receipt.json` — 2026-08-14 22:48:04 KST — `9056ef22c89ea8e4606610948ac7b32b959c97ec42d3ea2597bdc4e71bb67ce7`
- `handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stderr.log` — 2026-08-14 22:48:01 KST — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stdout.log` — 2026-08-14 22:48:04 KST — `29a592d8ed9c9c571ff96195e1313815a7cb3ece824fb67e9ae2d539779a1b1e`
- `handcheck/superseded_hc1_20260815/synthetic_selftest_receipt.json` — 2026-08-14 23:07:04 KST — `1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8`
- `handcheck/superseded_hc1_20260815/synthetic_selftest_stderr.log` — 2026-08-14 23:07:01 KST — `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `handcheck/superseded_hc1_20260815/synthetic_selftest_stdout.log` — 2026-08-14 23:07:04 KST — `e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab`

This refutes the receipt's literal supporting sentence that every output is dated 2026-08-15: thirteen superseded outputs have 2026-08-14 KST mtimes. It does not refute the memo's narrower condition-1 conclusion. Two superseded synthetic receipts outside the rehearsal directory contain stratum summaries; they are explicitly synthetic and contain neither `authorized_measurement` nor the real-tree path. No real-chi stratum artifact was found.

## Attack 3 — material added after Revision 4

Both claims hold independently.

1. `queue_ledger.jsonl` contains `20260820T231324-hwao-report.mp3` twice:
   - line 22: publish seq 21, `2026-08-20 23:13:40 KST`;
   - line 23: publish seq 22, `2026-08-20 23:24:55 KST`.
2. The two MP3s are byte-identical, both 616,320 bytes and SHA-256 `27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0`:
   - `20260820T230754-tori-report.mp3`
   - `20260820T232407-20260820T230754-tori-report.mp3`

The prefixed identity is now present in both `queue.json` and the append-only ledger; the ledger's `discovered` row records the historical fact that it was found on disk with no queue entry. The memo's past-tense wording is therefore supported, while current absence would not be.

## Attack 4 — status, estimator, procedural theory, and composed facts

### Status

- DRAFT / no signature / not in force: stated at lines 3–4; no Duho signature appears. **HOLDS as header metadata.**
- No sentence reads as if operative: **FAILS**, finding 1.

### Verdict estimator

- No `_verdict_20260821/` directory or `verdict_runner.py` exists anywhere in the repository name walk. The build spec says no implementation exists. Revision 5 contains no positive built/gated/frozen claim. **HOLDS inside the target.**
- The named successor note's old sentence remains. **External seam disclosed in finding 5.**

### Procedural theory, independently tested

- **No frozen anti-abandonment duty: HOLDS.** The frozen preregistration defines conditional outcomes and stop/refusal paths but no duty to continue until an outcome exists. K-8 condition 6 expressly stops on specified refusals. The frozen text does not manufacture an outside-preregistration human decision category, but it also does not compel continued execution.
- **External reason is not HC-6: HOLDS.** Frozen HC-6 takes bound `N` and `A_eff=(2a-1)*0.0408` through the pinned uniform-sphere analytical logic. It names no footprint statistic. A footprint-aware reason can motivate an investigator's external decision without becoming an HC-6 input, so long as the memo does not issue an HC-6 verdict.
- **No frozen outcome declared: HOLDS.** Revision 5 expressly declines all four F-6 outcomes and void. The operative-language defect is a status defect, not a hidden F-6 category.
- **Condition 2 / condition 1: HOLDS.** K-8 condition 2 bars any aggregation or summary over chi. Publishing the complete then-existing three-value multiset and the sign summary breached it. No real partial tertile was found, so condition 1 is not established as breached.

### Composed numeric, interval, sequence, hash, and quotation audit

| Memo claim | Independent result |
|---|---|
| Freeze-time HC-6 `N=130,076`, `a=0.999711`, `A_eff=0.04077642`, power about `1.0000` | **HOLDS** against `GORU_BS8_POWER_RECEIPT_20260814.md` and frozen HC-6. |
| Second HC-6 firing awaits complete sample/strata/full HC-1H lower-bound `a`; pilot is optional 150 and full stream is 850 | **HOLDS** against frozen §5 and hand-check instructions. |
| HC-6 inputs omit footprint geometry; `sim_power.py` draws uniform `costheta` and uses `mean(cos^2)=1/3`; F-3 is one-sided while the harness power logic is two-sided | **HOLDS** against source and frozen F-3/HC-6. |
| `Var(c)=0.057985`, subset bound 36,253, geometric bound `4.4888`, one-sided 95%-power requirement `4.7351` | **HOLDS independently.** Recomputed from 208,407 position rows: `Var=0.05798463739809634`, `3*SSE=36253.21297867519`, bound `4.48884449002089`, requirement `4.735085933119285`. No chi was opened. |
| Exact source position file identity | `positions_parent_20260820.csv` SHA-256 `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`. |
| Seq 20 quote and sign quote | **HOLDS verbatim** in `20260820T231235-hwao-report.txt`. |
| “52 minutes” after 22:20 authorization | **HOLDS as whole-minute wording:** seq 20 is 23:12:51; elapsed 3,171 s = 52 min 51 s. |
| Seq 21/22 and seq 26/28/30 times | **HOLDS** against append-only ledger rows. |
| Exact exemplar `0.013161621987819672` in deck/report HTML | **HOLDS**, one exact occurrence in each source. |
| Seq 30 playback-receipt context | STARTED 11:02:52 / COMPLETED 11:05:28 in `played.jsonl`; “mine” and purpose remain Hwao's first-person attestation, not independently actor-proven. |
| Two predecessor declarations retained | **HOLDS** by current hashes and their gate records. |
| Revisions 1–4 retained byte-for-byte | **FALSE for Rev4**, finding 2. |
| Generator SHA-256 `681592…` | **FALSE for current named path**, current hash `aac8f562…`. |
| Generated block is a fresh byte slice | **HOLDS pre-output as a 1,356-byte contiguous slice**, but it omits the then-current leading gate row and is non-closing under the required new gate; see post-write result. |
| Archive matches cannot be attributed to reports | **FALSE**, finding 3. |
| Receipt is generated rather than composed | **FALSE**, finding 4. |
| No built/gated/frozen estimator | **HOLDS inside target**; external successor seam remains. |
| BHU scope without BHU inference; Longo/sky boundaries | **HOLDS at the stated boundary.** The frozen headline excludes BHU/isotropy inference, and the memo claims no F-6 outcome. |
| “Acquisition runs to completion” | **Forward plan, not a verified completed fact; also reads as operative despite DRAFT**, finding 1. |

## Failed attacks / facts that survived

- The repaired `cited by NO gate: (none)` conclusion is correct.
- Before this report existed, the embedded block was byte-identical to a fresh output slice.
- All footprint figures used by the memo independently recompute from positions-only data.
- The optional/full hand-check counts and uses of `a` match the frozen protocol.
- The target does not inherit the receipt's false no-aggregate-code-path claim.
- No real-chi hand-check invocation or real-chi tertile artifact was found in current tree, git history, or extant outputs.
- Seq 21/22 and the MP3 byte identity both hold.
- Publication timestamps, 52-minute interval, report quotations, exact exemplar, and playback events hold mechanically.
- The outside-preregistration procedural theory survives; the failure is the draft's operative wording and factual custody/source claims, not an invented frozen outcome.

## SHA-256 ledger — every source artifact selected for content/hash review

### Target, predecessor custody, generator, and gate artifacts

- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md` — `276363f36e7c726d39fed811d011552ff8a1e998915d179bcd00d1c2e003dc5e`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV1_SUPERSEDED.md` — `a683bc9424f26fdeabccd414aecdc0b67f08bab86307015e68294612d6a7a5bb`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV2_SUPERSEDED.md` — `7e1b2e2f4f104ce171c6e9e50ed843ef70417a5f76216bf4e0618b0163ded64f`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV3_SUPERSEDED.md` — `bafec8bf5f177830d4eeac75a0a7b29c72ea9b7dcfedd3b33f697a283836c62d`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV4_SUPERSEDED.md` — `d69be7af81613c3f6a103e5ff833778dd4c036a3e121ac131852d459b38a6efd`
- `DECLARATION_INCONCLUSIVE_BY_POWER_20260821_REFUTED.md` — `af51507a43fcdee4e53b51502c332e3624611bb27de6d0bede120b33c8b38ebb`
- `DECLARATION_VOID_ON_DESIGN_DEFECT_20260821_REFUTED.md` — `e55460743358bbb0b8c16b8d99e5f4260d0f57a88096dc2c0328f6a675b805ba`
- `CHI_CUSTODY_RECEIPT_20260821.md` — `5097a917f51015d50bb399282e7886ab931b55cfd0bcc2badde3ef2306e42043` — source only, not gated as deliverable
- `_custody_20260821/build_custody_tables.py` — `aac8f56211c19bbe1ecfa8ff81145b63f096f35d5acffc2cf4ddb98504dfe6f0`
- `_tmp_GATE_BRIEF_MEMO_R5_CODEX.md` — `820300e956021d11bf817ff0bf7c7954b205a3ed3e95a7d754964d942d01651c`
- `_tmp_gate_final_audit.json` — `9e8d50af4d81648bd4f763dbdb560a872bf3ecf5246f98330a50c16702888e2c`
- `_tmp_gate_r6_audit.py` — `cb201032af7336d4f440d71ec64fd478b8e746371ec1f95ebc1f2ccc49d4d348`
- `_tmp_gate_r6_audit.json` — `916eb6d4262e9fba8896afcf2d617ac825b13de72fff64b2db03cf9fadcf5636`
- `GATE_CHI_CUSTODY_R6_20260821.md` — `19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083`
- `GATE_DECISION_MEMO_20260821.md` — `a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa`
- `GATE_DECISION_MEMO_FINAL_20260821.md` — `1cf7ba7780a556428e691d76bb54e08949fb375eb7a3112257ff7986a100ad01`
- `GATE_DECISION_MEMO_R2_20260821.md` — `59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066`
- `GATE_DECISION_MEMO_R3_20260821.md` — `c1ad25fd6574bb9bf3386d8d6fb7448ed62015384035f9110dbde3e94ec0c453`
- `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md` — `94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e`
- `GATE_FOOTPRINT_GEOMETRY_20260821.md` — `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`
- `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md` — `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`
- `GATE_VOID_ON_DESIGN_DEFECT_20260821.md` — `38e789547e750d21b38fd9d1fa3515bc44ed8f95d542476183d45274c7518b3c`

### Frozen/statistical/source artifacts

- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md` — `f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee`
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md` — `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76`
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` — `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`
- `_positions_20260820/positions_parent_20260820.csv` — `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `GORU_BS8_POWER_RECEIPT_20260814.md` — `b6207c7fc93ea7bfeb8045d0e635693010644633b747b298eb51b6233f014a92`
- `K8_CROSSING_AUTHORIZATION_20260820.md` — `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`
- `../spike/sim_power.py` — `f2867dbf4f5ab8ad82d645324a525a75af38006ff03e8ee08b90589cff50b1ce`
- `VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` — `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`
- `SUCCESSOR_SCOPE_20260821.md` — `cfca55edaf7d9fe7a8d1dc70f069f4d865ec41b1fb243b3a06f8020e6784b112`
- `LANG_REPLY_RECORD_20260821.md` — `7d0d17067ae4a741de9aa731f610a0934fdbfaf6dace0d050404dcb3d09a5163`

### Hand-check source/history and canonical output-name scan

- `handcheck/nm_handcheck.py` — `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4`
- historical blob at `199c3168…` — `cc88fa5ee6e7d7f2ab32ad4b7b0d7d843f9a77ed777c11d259755197eda03bbc`
- historical blob at `0923db16…` — `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4`
- `handcheck/OPERATING_INSTRUCTIONS.md` — `db0623854c3cbc837d91499cf578ddbf974507079df623c5ad78ac001a5eba8f`
- `run_hc1h_stage.sh` — `5b91b8d7b5a8135950b6b829632b8b568dafe9780776016f2311543e6215a9af`
- `_inference_20260820/chi_wrapper.py` — `e9b0ed122f298e531d97e870281b1593444587ec2908a760be10b94b3c03aec3`
- `_rehearsal_20260820/hc1h_private/sealed_key.nmhc` — `483ac84acd99a024af17816e252eb95b4ddd4d093b790c6448a7512fc3ec1cc2`
- `_rehearsal_20260820/hc1h_private/prepare_receipt.json` — `fb10e2d26f5bbe76a392850aa9e3db1195571749153fa25164ed5a3731179a9b`
- `_rehearsal_20260820/hc1h_checking/commitment.json` — `4a2e01407752f9c183898063e49ba8101c97d48db604a44f958452acaaaac15a`
- `_rehearsal_20260820/hc1h_checking/commitment.sha256` — `a7d63d46d9812c152700c8987e2efdeea772e2f8db5851052ba717ce73a1dba4`
- `_rehearsal_20260820/attempt3_hold/hc1h_private/sealed_key.nmhc` — `cd8dbe2c514e5bd0f638d3ce193e36b87b74d6cd5b7204c7be4f146ceffed554`
- `_rehearsal_20260820/attempt3_hold/hc1h_private/prepare_receipt.json` — `e9d77ba140872a995a0a6454bcc12d5767f74ff4760e166227d1dccbb2d822af`
- `_rehearsal_20260820/attempt3_hold/hc1h_checking/commitment.json` — `2fdcb164800d3dabcf75ca4f1b6439c88ef1c438e14a1f13de3e35eab9e26883`
- `_rehearsal_20260820/attempt3_hold/hc1h_checking/commitment.sha256` — `7b444267c12545ff5784317a281c5734cc527e634c0c0c9fe6e92c58dba3d30f`

The 21 `handcheck/` generated-output hashes are recorded with dates in Attack 2 and are part of this ledger.

### Status-audio source artifacts

Live files are identified by the synchronized final-review hashes below; earlier queue-ledger hashes observed during the pass were `b1474cbdf49e71673c7cd6be187d04aaaf515c3eb8e9b06251349a128e6dddf2` and `4bab2e76c8f0caf6050195a289353c5482fd3bcfb4af7434636092aaa0a455d2` before later append-only growth. The evidentiary rows persisted.

- `queue_ledger.jsonl` — `727fc064b55ac952f6fb708b2b950e6e8fd1c3c81a2fc65b76aec912baa8d13f`
- `queue.json` — `256f3215379b85d7851c5166e0143b9d3d3f8aac9b4df2a2132aca160c7e484e`
- `played.jsonl` — `4b7b8fc0821ef94eba61e8c35d7baf0a62d99968310d049d3e4d8e03ccce9a96`
- `archive.html` — `36a0499615eb74ca1fdacf7338084d9744891f34025630bb833a2e2e78710178`
- `archive-2.html` — `b1625dc12554fbcc76226849aa45a5ad4925e891b6eccaee4a1e163ad675ee3f`
- `archive-3.html` — `07176092ef8f9c72fd20f112ea6fa5e43840f18da2a970e9efebbf7cc96a071c`
- `archive-4.html` — `21a8031c647d9f2c8aff544e9788ebcffad5dcb7be93927ed2f8d4b3ba47e08d`
- `archive-5.html` — `9c1d188d4fe5582addd2fcb8551cbbbdb7eae94c89c0d288ff9dde5dfeb436e0`
- `20260820T231235-hwao-report.txt` — `7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad`
- `20260820T231324-hwao-report.txt` — `5ba48ea353bb94a3a5740c4be8160e552e996670287f124fb66b69d5cf781842`
- `20260821T004950-hwao-report.txt` — `f1096d51b237dbeaddf92b034194ed9f23d89401b54bb26335b74d1ead81b258`
- `20260821T004950-hwao-report.deck.json` — `c49c71978ee27eedab93076906a27f188eee3b4b905caed13b674127feab091b`
- `report-20260821T004950-hwao-report.html` — `d4693eb627d5785354cfa0c27057f48508f24cb88697297941c5b51c01fbbb85`
- `20260820T230754-tori-report.mp3` — `27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0`
- `20260820T232407-20260820T230754-tori-report.mp3` — `27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0`

## Evidence methods and limits

- SHA-256s were computed from current bytes, not copied from the memo.
- Exact digest searches covered every current `GATE_*.md`.
- The custody builder was source-inspected before execution; it does not open the protected chi tree.
- Geometry was independently recomputed from the positions CSV only using the frozen axis and population moments.
- Archive statements were tested against raw current HTML structure and exact phrase counts.
- Publication rows were parsed from the append-only JSONL; MP3 equality was a full byte comparison.
- Current repository text, current executable paths, extant output names/content, and available git history were searched for a real-tree hand-check invocation.
- No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read. No chi value was obtained from it and no statistic over its records was computed.
- No source, target, receipt, archive, queue, runtime, database, git state, or public artifact was changed. No temporary file was created. The only write is this required gate report.
- Live status-audio files can append/change; the synchronized hashes above bind the cited observations, and the relevant rows/phrases were rechecked at the final evidence cut.
