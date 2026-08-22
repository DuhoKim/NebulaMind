REFUTED_CHI_CUSTODY_R8

# Chi custody receipt Revision 8 — adversarial gate

## Executive finding

Revision 8 is refuted. The dispatched receipt bytes were stable and matched the pinned SHA-256, and most withdrawals are honest. The decisive failure is the claim that the table is reproducible against the printed “exact input set”: that set lists only 12 gate files, while the generator also consumes three unlisted footprint-revision files and 52 unlisted mutable status-audio files. A listed-inventory-only execution does not reproduce the table, and a new non-gate report changed fresh output during this audit. Two additional custody claims fail as written: the named R6 gate records the genesis-ledger digest once in a post-review appendix, not “three times before review,” and neither named commit contains the current Revision-8 receipt or its dispatch snapshot.

No remedy is proposed.

## Scope and dispatch identity

- Live target at opening: `CHI_CUSTODY_RECEIPT_20260821.md`, SHA-256 `c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74`.
- Dispatch snapshot: `_custody_20260821/_gated/CHI_CUSTODY_RECEIPT_20260821.c3e6de5ef640.md`, same full SHA-256.
- Opening byte comparison was exact. The snapshot carried `uchg` and mode `0444`.
- Prior gate: `GATE_CHI_CUSTODY_R7_20260821.md`, SHA-256 `06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa`.
- No file under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, statted, or read. No statistic over private chi records was computed.
- Writes were limited to this report and lane-local names beginning `_tmp_gate_r8_`.

## Finding 1 — BLOCKING: the printed “exact input set” is not the generator's input set

The byte-level repairs hold at the first synchronized evidence cut:

- generator: 7,483 bytes, SHA-256 `bae6a3be5151ca462f7aaf1267332d1cf4e655e955e86f87fc886b922b5cf717`;
- `tables_R8.txt`: 5,390 bytes, SHA-256 `9e4e2a02d8a96bb1d36a7681f0a7dec29f31e4539e077f5e069f9aacc54fc340`;
- receipt fence: the same 5,390 bytes and SHA-256, byte-identical including the terminal newline;
- fresh live generator output at that cut: the same 5,390 bytes and SHA-256;
- every printed 12-hex gate digest matched the corresponding current full SHA-256.

But the printed inventory is only a partial dependency list. Instrumenting every file opened by the generator found 12 listed `GATE_*.md` files, three unlisted `HWAO_FOOTPRINT_GEOMETRY_FINDING_*.md` files required to map cited hashes to revisions, 52 unlisted mutable status-audio inputs, and the generator itself.

A controlled execution with exactly the 12 listed gate files, while still granting the script its unlisted live status-audio tree, produced 5,257 bytes, SHA-256 `3b7cd7876b9fdead3d4469f1f9a030fa0fbbe2639ba93975013d2782332111c5`, not the pinned table. Adding the three unlisted Hwao revision files made that execution match `9e4e2a...` at the first cut. Thus even section A cannot be reproduced from the listed inventory; section B has another 52 unlisted dependencies.

The defect manifested during this audit. At 2026-08-22 00:03:43 KST, a new non-gate report `20260822T000008` had entered `archive.html`. Fresh output became SHA-256 `ba00ffff7af0289a8d76a9bcc1fa02a5a8238436fbd3cba0abdb2d9a4e954494`; the exact diff added that report stamp to section B. No new gate row caused this change. Revision 8 did not solve self-invalidating provenance by printing an inventory; it printed only one subset of the dependencies.

## Finding 2 — MATERIAL: the genesis pin and “two independent witnesses” are overstated

### What the commits do contain

The narrow genesis-by-git claim holds:

- current ledger line 1 plus newline hashes to `dabfa9ee308a6e6a4ca346da1f1ba1ecb8e16612a1b4f022bba7f22b1ce815c7`;
- line 2's `prev_ledger_sha256` equals that digest;
- the first two current lines are byte-identical to the 526-byte ledger committed in `44fbc747`, SHA-256 `7136960fcb89ca9f7e3234c13b2604535cfa8ca005ad6b7cda2bf9b41c1946b7`;
- `acad6b05` contains the decision-memo snapshot named by the genesis row, SHA-256 `3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c`;
- `44fbc747` contains `gate_snapshot.sh`, SHA-256 `f89cf2a463d27b19f9f0eac682e86aa2e73c3332ba707003d491c6566bc1fff5`, and the two-row ledger;
- both commits are contained by the local and `origin/feat/paper-workflow-v2` branches.

### What they do not contain

The statement that the R6 gate pinned the genesis digest “three times before review” does not survive inspection. `GATE_DECISION_MEMO_R6_20260821.md` contains the full `dabfa9ee...` digest exactly once, at line 154 in its post-review SHA appendix. Its dispatch-pin section at lines 11–20 pins the memo and memo snapshot, not `GATED_SNAPSHOTS.jsonl`. The gate file contains no timestamped pre-review receipt for the ledger digest and no three occurrences of it.

The broader “two independent witnesses” framing also does not bind Revision 8. Both `HEAD` and `origin/feat/paper-workflow-v2` contain the Revision-7 receipt bytes, SHA-256 `879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e`. The current Revision-8 receipt (`c3e6de5e...`) is a tracked modification; its `c3e6de5e...` snapshot is absent from both Git trees and is untracked; the three-row live ledger is a tracked modification. The commits preserve the genesis row, mechanism, and Revision 7. They are not a Git witness for Revision 8's current bytes.

## Finding 3 — MATERIAL wording overflow: condition 1 is still stated once at universal strength

The evidence-bounded sentence is correct: no breach was established within the authorized boundary. Current `handcheck/nm_handcheck.py` can compute real-population chi tertiles and cutpoints (`_rank_tertiles` at lines 279–290; real HC-1H strata/cutpoints at 557–579). A bounded scan of all 21 extant handcheck JSON/JSONL/log outputs found zero `chi_dr10_south` tokens; the two `authorized_measurement` hits were unit-test names in test stderr. The current executable containing the private-tree name is the inference wrapper, not a handcheck invocation. No real-chi tertile artifact or invocation was established without opening the forbidden tree.

Revision 8 nevertheless begins the paragraph with the categorical bold clause **“Condition 1 is not breached”** before giving the narrower, correct formulation. That first clause is stronger than “no breach established within the authorized evidence boundary.” The later qualifier prevents a universal inference for a careful reader, but it does not make the categorical clause itself true at the claimed evidence strength.

## Finding 4 — MATERIAL current-state drift: five of six named live paths still match, one does not

At the first synchronized cut, all six listed surface hashes matched Revision 8:

- MP3 `2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168`;
- caption `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`;
- deck `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`;
- timing JSON `a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79`;
- report page `050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f`;
- archive `33c4c6c8db63ed278945bd06fd714b352777857372e72b185358e982bd573710`.

By the closing evidence cut, the first five still matched. The bare mutable `archive.html` path had moved to SHA-256 `c104ea59992472cc5e22b9666432ba2c1fddc4a03240863260650eede8b3e31d` as the new report was added. This is not evidence that the target row changed; it is evidence that a bare whole-archive digest is a historical observation, not a currently matching path identity.

The reverse-repair causation held against the earlier `33c4c6...` bytes:

- replacing the one corrected value phrase in the report page reconstructed historical SHA-256 `c5d5d5b81f5ae997e239203d2cd8e7e6c3065dc043069830ba138a29b9f6e9e7` exactly;
- reversing the row-scoped repairs in the `20260820T173007` and `20260820T231235` archive `<li>` blocks reconstructed historical SHA-256 `36a0499615eb74ca1fdacf7338084d9744891f34025630bb833a2e2e78710178` exactly.

The six-item count is an artifact-bundle count, not six value-rendering surfaces: the timing JSON has no chi value; the deck carries the decimals only in a diagnostic note. This does not change the digest results.

## Attack 1 — the four Revision-7 findings

### 1. Table self-invalidation

**Fails in Revision 8.** The fence/table/live bytes initially matched, but the advertised input inventory is incomplete. The table is achievable only with unlisted revision-map and status-audio inputs. It is not reproducible against the listed inventory alone.

### 2. Ledger-chain claim withdrawn

**Withdrawal holds.** An independently invented two-row ledger with recomputed predecessor hash verified under the same prefix-hash rule, SHA-256 `1dc360a499db9e4d04a2ebf5490714c59242a2797770220210d14e9138fbda30`. The unmodified `gate_snapshot.sh` appended a legitimate third row with exit 0; the resulting three-row ledger verified, and truncating it back to the invented two-row prefix also verified. Revision 8 does not use that chain as evidence. Its `queue_ledger.jsonl (append-only)` wording refers to the separate publication-event source, not the withdrawn snapshot-chain property. The snapshot script's old “tamper-EVIDENT” comments remain false, but Revision 8 explicitly calls the script unmodified and gives the chain zero evidentiary weight.

### 3. “Complete set of values” withdrawn

**Withdrawal holds.** The corrected caption says `2,725 galaxies measured`, and fresh beam-5 ASR independently says `2,725 galaxies measured`. Three values were not three of three. Revision 8 no longer relies on that premise. Condition 2 instead rests on the explicit sign/count sentence, and section 4 independently bars publication.

### 4. “0 genuine divergences” withdrawn

**Withdrawal holds; all three divergences reproduce independently.** Fresh `faster-whisper 1.2.1` / `ctranslate2 4.8.1`, `base.en`, CPU int8, beam 5 produced:

1. MP3 SHA-256 `78471d4147bce699f29fa0343220068656d2847f8e718a5b175c3b111e286c02`: `832,000 objects`; caption SHA-256 `fa46299e4a502ac08f9d9ed4c89a653988e031be53973db6ba832ec6726fcfe2`: `800 and 32,000 objects`.
2. MP3 SHA-256 `3913befc8faf7c4fbcbf4add6d7c3c4c263aad4bdbb58899a4b97faca614eafb`: `130,000`; caption SHA-256 `d8feafae500939283af646440e7d22f05634fc4d7a058eba69be8594c0944e45`: `a 100 and 30,000`.
3. MP3 SHA-256 `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3` ends `That is what we are computing. One galaxy at a time.` and contains no `200,000`; caption SHA-256 `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c` adds `200,000 times`.

The first two are the connector-splitting family; the third is synthesis truncation, not that normalizer family.

## Attack 2 — newly claimed facts

### `chflags uchg` and byte custody

**Holds at current-host strength.** The dispatch snapshot carried `uchg`. A lane-local equivalent probe was set `uchg`; a direct `write_bytes` overwrite failed with errno 1 / `EPERM`, and the before/after SHA-256 remained `1fd69338d8a9a6d4ca043e7635da5da2a4f67d8b2d319ce5db402a2428a3d0c9`. The live receipt and dispatch snapshot still matched `c3e6de5e...` at the final pre-report pin check. This is accidental-write resistance, not owner-proof immutability, exactly as Revision 8 states.

### Genesis row and commits

**Mixed.** The row and its named snapshot are in the two commits, and the committed chain prefix matches. The “three times before review” description is false/unsupported in the named R6 gate, and the commits do not contain Revision 8.

### Six digests and reverse-repair causation

**Historical causation holds; current bare-path digest set does not.** All six matched at the initial cut, the reverse transformations reconstructed both old served-page hashes exactly, and five stable paths still match. `archive.html` later moved through an ordinary new publication.

## Attack 3 — standing authorization reading re-derived from frozen text

The standing reading holds without inheriting prior gates:

- K-8 section 2, lines 20–24, explicitly says this authorization **spends the chirality-label clause**.
- Condition 1, lines 28–31, expressly permits per-object chi to accumulate incrementally while forbidding any partial tertile.
- Section 5, lines 52–59, directs Hwao to launch incremental chi and says the first real receipt marks the crossing.
- Condition 2, lines 32–33, separately forbids any summary over chi until the frozen order reaches it. Nothing in K-8 says this condition was spent.
- Section 4, lines 46–50, separately lists `publication of any kind` as not authorized.

Thus K-8 licensed measuring but did not license publication or spend condition 2. The spoken/captioned sentence `One leaning each way among the confident pair` is a sign/count summary and independently violates condition 2. The three-value “complete empirical distribution” theory is unnecessary and has been correctly withdrawn.

## Failed attacks / facts that held

- The live receipt matched its dispatch snapshot at opening and at the final pre-report pin check.
- The R8 fence is byte-identical to `tables_R8.txt`, including the terminal newline.
- The generator self-digest and every listed gate digest prefix were correct.
- The ledger-chain withdrawal is honest in Revision 8; independent forgery, append-after-forgery, and truncation tests reproduced its stated weakness.
- The caption and fresh target ASR both establish `2,725 galaxies measured`.
- Fresh target ASR states the three values `0.834336`, `0.384410`, and minus `0.640352`, plus the sign-summary sentence.
- All three R7 audio/caption divergences independently reproduced.
- The current snapshot carried `uchg`; equivalent direct overwrite produced `EPERM`; target/snapshot bytes held.
- The narrow genesis row plus named decision snapshot are preserved across `acad6b05` and `44fbc747`.
- The first five named target-artifact hashes remained stable, and reverse repair reconstructed the two historical served-page hashes exactly at the initial archive cut.
- The K-8 reading “measurement licensed; condition 2 and publication bar unspent” follows directly from the frozen text.

## Evidence methods and limits

1. Full SHA-256 plus byte comparison of live receipt and dispatch snapshot at opening and final pre-report cut.
2. Source inspection and instrumented generator execution with every opened file recorded.
3. Controlled listed-inventory-only and listed-plus-unlisted-revision executions.
4. Fresh generator re-execution after the concurrent non-gate publication, with exact unified diff.
5. In-memory reverse repair of the report page and row-scoped archive blocks; no served file was written.
6. Fresh local beam-5 ASR of the target and all three divergence MP3s using the hashed local model snapshot. ASR is used for spoken numeric/content agreement, not word-for-word fidelity.
7. Read-only Git object/path inspection of `acad6b05`, `44fbc747`, `HEAD`, and `origin/feat/paper-workflow-v2`.
8. Independent temp-only snapshot-chain forgery/append/truncation probe.
9. Independent temp-only `uchg`/EPERM overwrite probe.
10. Bounded inspection of current handcheck source, launcher, role-name contract, and all 21 extant handcheck machine outputs.

No external publication platform was inspected. The private chi tree was deliberately not opened, so condition 1 cannot be universally proved clean. The first archive evidence cut was reviewed at SHA-256 `33c4c6...`; the closing path was `c104ea...`. The queue ledger likewise moved from observed SHA-256 `b92adc4577fa6a7c42f6be9e89913822c034e262c44dd5f9d2522ce48d1ddee4` to `d8f9866f89a3524451ab6277717eccc47f0f39f45a24669e5130942c8b4878c5`. These concurrent states are reported rather than collapsed.

Assembly-only temp artifacts created/read after the manifest cut were `_tmp_gate_r8_report_body.md` (`df52c2031b1508f27768710ece0ca7d7cf03b33c394159b7a00b4781d7af7532`), `_tmp_gate_r8_report_complete.md` (`635ed8e6bda6b20fe8ae3283a8d89cbecb83037245981b96ff373a253dbd8b7a`), and `_tmp_gate_r8_write_probe.txt` (`25be323556dad377abb57fe7ec8c4b99a6527f488dda28d0c9b686528659c909`). They carry no evidentiary claim; their hashes are recorded for read-set completeness.

## Complete SHA-256 ledger of reviewed artifacts

The mechanically assembled ledger below has 171 rows. Its standalone TSV bytes hash to `4b201580130f986a5ce5c4e8350abb951521b68af76d0d9e984d3d3f51e2fc89`. The earlier mutable archive/queue states are separately recorded above because those bytes moved before the final manifest cut.

```tsv
sha256	bytes	artifact
78471d4147bce699f29fa0343220068656d2847f8e718a5b175c3b111e286c02	682368	/Users/duhokim/HermesOps/reports/status-audio/20260814T160157-variance-pass.mp3
fa46299e4a502ac08f9d9ed4c89a653988e031be53973db6ba832ec6726fcfe2	648	/Users/duhokim/HermesOps/reports/status-audio/20260814T160157-variance-pass.txt
3913befc8faf7c4fbcbf4add6d7c3c4c263aad4bdbb58899a4b97faca614eafb	734592	/Users/duhokim/HermesOps/reports/status-audio/20260814T161526-ten-blockers.mp3
d8feafae500939283af646440e7d22f05634fc4d7a058eba69be8594c0944e45	659	/Users/duhokim/HermesOps/reports/status-audio/20260814T161526-ten-blockers.txt
d84bf963ce608387298041262614314c1cb7fa4608666178c4ed341a10677928	1585	/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.deck.json
7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47	577	/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.txt
1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c	2543	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.deck.json
2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168	1131264	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.mp3
a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79	163	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.times.json
2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162	1035	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt
7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad	1055	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt.corrupt-20260821
855da9448492112c0529476cf451466934c63474068419cb3382009bfb9108ab	3292	/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.deck.json
5ba48ea353bb94a3a5740c4be8160e552e996670287f124fb66b69d5cf781842	1131	/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.txt
7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47	577	/Users/duhokim/HermesOps/reports/status-audio/20260820T232407-20260820T230754-tori-report.txt
1af45a7e0cb275f3a3605aa3f3b68e78f899421939306ebac45f8448b66a1f12	12914	/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.deck.json
e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e	1853	/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.txt
c49c71978ee27eedab93076906a27f188eee3b4b905caed13b674127feab091b	10840	/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.deck.json
f1096d51b237dbeaddf92b034194ed9f23d89401b54bb26335b74d1ead81b258	2562	/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.txt
81e12c9a380d2f8a5bb65f2b81d45a0da8dc2877cf8dd22f9bb1dc5da504a3cb	2112	/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.deck.json
452f13b624ff952df0987b7f54feccc632fde6c0f2eb569c365fa92ab968a982	627	/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.txt
88394b89139669d66bef04ea85c62f591490f11ef767b5f14421784b2a54f131	712	/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.deck.json
ada74c9a1761ba02f9f0c0fb6c31a3415d4fc80a2619a8776905101d1e146951	67	/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.txt
8b3ddead69fb6764df63a35352eca9332b52b9472d4626a6e5e05430f20b4ad1	4340	/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.deck.json
c3aefdeea36b45e60f63e297bfed77358fda8db3d63560c245386b3d20cba8b2	2991	/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.txt
0fe5ecac190cfcb490cdcc42aa52b1069e7bf2a3b97d996d3faf13ae0030b8cc	2997	/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.deck.json
5648a55e23f6fddfdd9d215c1c64ea8eaf83c6a51fdec991a5f67ba31dc6e37b	1818	/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.txt
6437b0993110b9dca73b811017a0ba49803faa255a413cb89a2ad1c754a691ad	3604	/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.deck.json
5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3	2596992	/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.mp3
fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c	2702	/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.txt
ec91f2ed3499f2bb2d291154b9a18c43b00841082853ac46c31f57a97d192998	2299	/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.deck.json
c42bc1d4500a8e0db4411715c1237da0ebf9a39d9d88eb1fa7d633367281770b	1163	/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.txt
f208eaab7cec9040fa0063bb9f722aab36046ffbae4c49216fb8dc305def1d55	2546	/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.deck.json
1b7d622e8ef866752b1c9e82ae5d3edb97ebd85c0a9de18847801f32ea658940	1335	/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.txt
83988126c6ef8c6fef4bb696c345fc03c833620158bad0496aa19fa300cdad23	1442	/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.deck.json
6e35f60af1cefff0f8d03dfb5bdc6c22e99f9be81e4961493b59f23cbee86556	1324	/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.txt
abbcc68d5b715a85f78a0b920882c2af03319810ad46ba1b3ddb579f7ae3ea3c	10398	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.deck.json
ced123258db9e2eb517c1cea8335ab743c5411256d9d6704a2dbe60405b9bf26	1974	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.txt
1caeef29733b84df1eac2ae02ae91d15f108967ad14be4e2ed54a798625d8f39	3516	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.deck.json
e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e	1853	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.txt
f82d7bf828dce0ce6e697f47d636bddd3db01745cc146afe6bd5b82c6990ce56	11692	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.deck.json
8666d0fa246e33bd2f8cd65aba20a60732c482f247b0abea7a303ce3bab028bd	2002	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.txt
475e463419af4ac14b5e66b596b2fb2cec636f0bd141428e8a4159f74d1fb636	97771	/Users/duhokim/HermesOps/reports/status-audio/archive-2.html
dca2c6c7d40fa912b0608c854890333fdf900ec3b354fbeb62cc09ea90dca660	159359	/Users/duhokim/HermesOps/reports/status-audio/archive-3.html
771882062c0b7cbe08397539b65e135cd8de41c5f1d4df4778b793ba8da1f29e	210170	/Users/duhokim/HermesOps/reports/status-audio/archive-4.html
17895e01a9dde9f9fa4d23db51e8210ff8adddd2a3df35ddc01caef69443e444	83216	/Users/duhokim/HermesOps/reports/status-audio/archive-5.html
c104ea59992472cc5e22b9666432ba2c1fddc4a03240863260650eede8b3e31d	212397	/Users/duhokim/HermesOps/reports/status-audio/archive.html
d8f9866f89a3524451ab6277717eccc47f0f39f45a24669e5130942c8b4878c5	27074	/Users/duhokim/HermesOps/reports/status-audio/queue_ledger.jsonl
8db823083a03eb9afbc20e12631a44665a4f8081eca6b6e4a23f18eed2db8913	7672	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T230754-tori-report.html
050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f	8856	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html
861e633683a49c70ca15d7d2a0e0e1fe21f7ea163111085cc13f4c03ebd82ad1	9874	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231324-hwao-report.html
1ebde8a62d1393996e7bca9350e9c84aa2993a57cffd7b93a5b9ed358e04d256	27446	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T235925-tori-report.html
d4693eb627d5785354cfa0c27057f48508f24cb88697297941c5b51c01fbbb85	19499	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T004950-hwao-report.html
18734d3fdd389a1e000ffed169652a61d1a6cdcd695b201d7798b236f296fb9d	8213	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T080428-blanc-report.html
b832d6104df258bf8bed779d24229ce0ae49974f65e6026ce678e4a547f08b29	6264	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T105930-blanc-report.html
7dcf8e2ba41917e28987cbaf3317766499b361310030133535b2bff29bdeca77	13098	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T145923-hwao-report.html
f11078cce4e69efa4f59d37fd3681e18243cad80adce59571c99ca79588da0dd	10490	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T151249-hwao-report.html
849829d266274149e6a9f1d4fb22200929cbd218b3adef291502fdc07074cb87	11983	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T151843-hwao-report.html
1071f27aee6325973e0b04664274568e8fdbbe4345f8576ee3f85b109421ca27	9051	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T190931-tori-report.html
51216d69a089dd4240c5b75e9ea5f737e4faa4b4b140bb2c3f26a68ce9ac7a14	10135	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T200910-tori-report.html
a93fe2cec33b675dbeaf48cb55a3fe7627fa1f9fe77d2ac05f8a40f58335b1e4	8443	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T210530-tori-report.html
c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74	12085	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e	10057	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821_REV7_SUPERSEDED.md
48ae45bc73bd99a60c2e75ef5c69692f26f70e1219ea8062a0ddc486ae03953d	4681	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CSEAT_AMENDMENT_DONE.md
af51507a43fcdee4e53b51502c332e3624611bb27de6d0bede120b33c8b38ebb	5847	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/DECLARATION_INCONCLUSIVE_BY_POWER_20260821_REFUTED.md
19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083	117105	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_CHI_CUSTODY_R6_20260821.md
06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa	113961	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_CHI_CUSTODY_R7_20260821.md
a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa	23903	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_20260821.md
1cf7ba7780a556428e691d76bb54e08949fb375eb7a3112257ff7986a100ad01	36764	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_FINAL_20260821.md
59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066	18434	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R2_20260821.md
c1ad25fd6574bb9bf3386d8d6fb7448ed62015384035f9110dbde3e94ec0c453	24867	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R3_20260821.md
c9a144e256d2c7ef6c63d11c60b5002e25c7268483a4dc0bbd112ffdfeb24707	30942	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R5_CODEX_20260821.md
ddffe06cce8e41a3601931e36a92fc8d83d3aeff3c09be4cc6765311295ccbe2	21165	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R6_20260821.md
94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e	15172	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md
1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1	12861	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_FOOTPRINT_GEOMETRY_20260821.md
aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b	23416	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
38e789547e750d21b38fd9d1fa3515bc44ed8f95d542476183d45274c7518b3c	22552	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_VOID_ON_DESIGN_DEFECT_20260821.md
6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7	12167	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md
f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee	4821	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md
a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76	8490	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md
c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69	3710	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/K8_CROSSING_AUTHORIZATION_20260820.md
65ebcd76da90c41dbd2545e2e34c310321e111cd327102956153ff48f6640674	15574	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KUN_GATE_A2_REGATE_20260820.md
a991af772c870744125aee251817c0c13bd275628808c555378d4deb9dba2c45	25067	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KUN_GATE_A_AMENDMENT_20260820.md
88d8d844fd9ae9a375c709f5d55326467f57673d972e920e64ce8fdf25a05371	8571	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/KUN_GATE_B_PLUMBING_20260820.md
25ee0be369419b744cdd78ab0507f34e68a3c64a49142258d51d6efcb941fe9c	2163	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/RUN_ENVIRONMENTS.md
902d7421afa08cb311acce0a28baae515c42375e947b675fb970885aeb41dbd9	5996	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/YUI_BLINDED_HANDCHECK_HARNESS_20260814.md
c3e6de5ef640145a1a409c0222cc474c0bb494e39e7d709e497917ef58799f74	12085	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/_gated/CHI_CUSTODY_RECEIPT_20260821.c3e6de5ef640.md
700bd573e196445f0775b0a444af5a1d0570b36bcad218c590a928a64b7b3ff2	820	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/_gated/GATED_SNAPSHOTS.jsonl
bae6a3be5151ca462f7aaf1267332d1cf4e655e955e86f87fc886b922b5cf717	7483	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/build_custody_tables.py
f89cf2a463d27b19f9f0eac682e86aa2e73c3332ba707003d491c6566bc1fff5	1563	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/gate_snapshot.sh
9e4e2a02d8a96bb1d36a7681f0a7dec29f31e4539e077f5e069f9aacc54fc340	5390	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/tables_R8.txt
e9b0ed122f298e531d97e870281b1593444587ec2908a760be10b94b3c03aec3	3345	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_inference_20260820/chi_wrapper.py
fd6512ad42e15eb9e01c7f978d136876d25f7f4c78578c307d7cfa1f75cbcdce	3804	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_FOOTPRINT_GEOMETRY_20260821.md
5b34532bff9d696b3e26eb911d86a19d9e9d77323813e0ae3c8a0983c3ce5f52	3591	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_MEMO_R2_20260821.md
820300e956021d11bf817ff0bf7c7954b205a3ed3e95a7d754964d942d01651c	4067	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_MEMO_R5_CODEX.md
3e44b39505f2f734e97d50e6a9185398b2142e6039a60aba576d5b1b4db5b554	3673	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_MEMO_R6.md
2f58fa04104ef7118f424583b2a3d811c5b0665344c9de4c2ffcdc6d3fa32d19	3714	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_GATE_BRIEF_VOID_20260821.md
b37fd9852a491e5a64387e8bb7d73ddef9fdfd4f2d2015f4b7c44ea2e837b98e	2035	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_KUN_HARNESS_GATE_BRIEF.md
c98ccf9547425825b2164977ef5c9d3aff4251a638cc7930d803c9eca8e09789	11276	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_final_stdout.log
bf60bd74cd005b741bf0ec057cccc4ce4dee1242a92bdc7ec73ef031b09fc6c5	8444	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r5codex_stdout.log
cb201032af7336d4f440d71ec64fd478b8e746371ec1f95ebc1f2ccc49d4d348	12236	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_audit.py
647796d698d11c295c4a5b7f055b3250b722b336db294fd190da428ae2e53231	87667	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_hash_appendix.md
ae3415cba99cc66125b92d23fc25e2d4cd965cd38d858f9b2582654a41ee4e5e	18351	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_stdout.log
9eb3814687a3dc0423065c0ae8e6e28b23d0316711d11c7fe154831bf3f76c14	96365	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_final_reviewed_sha256.tsv
1a0a08b05cd2f4164ec81055f962121d0533fa48ef6fe5950b2a6724677e3bbe	3384	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_fresh_asr_beam5_adjudication.py
da0fcfe4afcfd7cc931cb63ef718d505c527a8a4b7de528ecf34faedb52a0840	6859	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_test.py
929c5252409436dce1b38a75d1abbcb5e132d170d8e324e4e04ed915fa2d22df	2128466	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/blobs/15d7bdf9ba25718ca2504eec6a8f02bc55af0a6a
2a166925539a16005f14ff328359f9b9adb9dc4fb631bb3b227526862e93e2ef	145216508	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/blobs/2a166925539a16005f14ff328359f9b9adb9dc4fb631bb3b227526862e93e2ef
f3bc3821e9fc76a27bae538e11ae5b677dcdd352b4600429ce7951d398569aeb	2227	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/blobs/594369787efe617005d199b03739ee0ead7e3ab7
ff77588746d3a2595d32ab5b69ffd7b95ce2441ac57533cb66fc3eb575a115cf	422309	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/blobs/ee695b8d3e3c10d488304e04468efec4ca27554a
172f0a0b03e1dfa042d6416586b209512c813a1a5bae5028a8bc8363ddb6994d	23777	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_asr_verify.jsonl
88bcbc2ac38081fa6f4b0bc2330a2143dc2461979ba078b63cb3ed3a21d831d1	3055	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_asr_verify.py
d4b65cc49c582a5e14f9c096ae9110cb0a66d02f6c3392adbb70d7b878f34eb5	666	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_chain_probe/_gated/GATED_SNAPSHOTS.jsonl
718f8dce87c09ea402bc3482f33c026bb1397c9381f324d1dc3af1eb5d73a99a	41	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_chain_probe/_gated/legitimate.718f8dce87c0.md
f89cf2a463d27b19f9f0eac682e86aa2e73c3332ba707003d491c6566bc1fff5	1563	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_chain_probe/gate_snapshot.sh
718f8dce87c09ea402bc3482f33c026bb1397c9381f324d1dc3af1eb5d73a99a	41	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_chain_probe/legitimate.md
7f680a0c3a3676b2c1c0e92780df5907a0df231f6d1e958e0f2cbb816b12407e	2309	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_chain_test.py
ee2ff31f081bf454c049f4bd02c2a24ba3a5d7f5874d8cc9def68f472ef01b56	6902	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_make_manifest.py
19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083	117105	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_CHI_CUSTODY_R6_20260821.md
06dc332d2783223242a1a2a994c94f6f9174f3c39c44a7d4cd6503acb38bfdfa	113961	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_CHI_CUSTODY_R7_20260821.md
a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa	23903	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_DECISION_MEMO_20260821.md
1cf7ba7780a556428e691d76bb54e08949fb375eb7a3112257ff7986a100ad01	36764	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_DECISION_MEMO_FINAL_20260821.md
59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066	18434	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_DECISION_MEMO_R2_20260821.md
c1ad25fd6574bb9bf3386d8d6fb7448ed62015384035f9110dbde3e94ec0c453	24867	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_DECISION_MEMO_R3_20260821.md
c9a144e256d2c7ef6c63d11c60b5002e25c7268483a4dc0bbd112ffdfeb24707	30942	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_DECISION_MEMO_R5_CODEX_20260821.md
ddffe06cce8e41a3601931e36a92fc8d83d3aeff3c09be4cc6765311295ccbe2	21165	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_DECISION_MEMO_R6_20260821.md
94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e	15172	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md
1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1	12861	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_FOOTPRINT_GEOMETRY_20260821.md
aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b	23416	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
38e789547e750d21b38fd9d1fa3515bc44ed8f95d542476183d45274c7518b3c	22552	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/GATE_VOID_ON_DESIGN_DEFECT_20260821.md
6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7	12167	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md
f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee	4821	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md
a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76	8490	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md
d0d8a91898f87470aa434a83afdd15eaef6ddee4f9e679e1d87b6e192f06f7ff	3656	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_repro_result.json
627087925494c9ac712f8768fd3aaebf3224e50d4e6de6575a08ac0764a1af73	4548	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_reproduce.py
b16bb949c555b4cf9b92626e272a8035fb0f8343008960032492ee913a31e679	15242	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_reviewed_sha256.tsv
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_stderr.log
ff50fba5b71e197ec94eed5a0d1845f3fde08e16b9709bebe324422e1316f68b	12930	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_stdout.log
1fd69338d8a9a6d4ca043e7635da5da2a4f67d8b2d319ce5db402a2428a3d0c9	25	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r8_uchg_probe.txt
9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8	3464	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_full_test_stderr.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_full_test_stdout.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_independent_stderr.log
51f42024f3284f91ca2a5fd9d521a60a45c99ac4d01e89f139a930ff7bdec5cb	43	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_independent_stdout.log
19a6881f8258e064d848968984a650ea3e97cc6ecc59ad5100ed3d2d475a87a8	2573	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_independent_verification.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_selftest_stderr.log
a37714358b4df5b043d0630c84c67410edecf6102070c5c73372f70f4ff1403b	929	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_selftest_stdout.log
25d02f109aba05d8a200a540e126ecba3c3c3607c0a6c9df2371566cafe2eb40	869	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_synthetic_selftest_receipt.json
65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4	161895	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/nm_handcheck.py
ebe607be44c62c552a845f0cbdbdb5986fa5c7c0d53eff9bddd575a5c37ae4a5	697	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stderr.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/attempt1_synthetic_selftest_stdout.log
148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b	1776	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/full_test_stderr.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/full_test_stdout.log
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/independent_stderr.log
b4f51b589170659f0be7c6e38d93c81e35b13a13e4813ede694f9e9bf4a2de63	56	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/independent_stdout.log
54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae	1861	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/independent_verification.json
9056ef22c89ea8e4606610948ac7b32b959c97ec42d3ea2597bdc4e71bb67ce7	2523	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_receipt.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stderr.log
29a592d8ed9c9c571ff96195e1313815a7cb3ece824fb67e9ae2d539779a1b1e	131	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/pre_review_synthetic_selftest_stdout.log
1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8	3032	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/synthetic_selftest_receipt.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/synthetic_selftest_stderr.log
e853c00c547de7241f26dbf333dd14f6fd0915cbbe09fde9dbaa7e7ab8ecd7ab	131	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/synthetic_selftest_stdout.log
5b91b8d7b5a8135950b6b829632b8b568dafe9780776016f2311543e6215a9af	347	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/run_hc1h_stage.sh
ce116729dedea22035474fcae925dcfbeb239dc3f6b609db2455101aa98bda53	1847	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/test_run_environments.py
cb29f6384c2231d42c6eac75c105b6ee6abec49377c6921f3cf5fe5e725fa9d7	1408	git-commit:44fbc74734e5f0fef0791384253ec01b94c1b7c6
3f25d02c04f664cd69b09b2c77eb0721e730a13fc836277abad625dbd65c4d82	1630	git-commit:acad6b0565714226e0277c75340e75f522a4ef71
7136960fcb89ca9f7e3234c13b2604535cfa8ca005ad6b7cda2bf9b41c1946b7	526	git:44fbc747:.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/_gated/GATED_SNAPSHOTS.jsonl
f89cf2a463d27b19f9f0eac682e86aa2e73c3332ba707003d491c6566bc1fff5	1563	git:44fbc747:.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/gate_snapshot.sh
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e	10057	git:HEAD:.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e	10057	git:acad6b05:.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e	10057	git:acad6b05:.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/_gated/CHI_CUSTODY_RECEIPT_20260821.879ec60426ea.md
3ec5f2498483338220b1596629f76b6102f8a9eedef59519f41dd72117af7d7c	11693	git:acad6b05:.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/_gated/DECISION_MEMO_DECLINE_TO_PROCEED_20260821.3ec5f2498483.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e	10057	git:origin/feat/paper-workflow-v2:.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821.md
```
