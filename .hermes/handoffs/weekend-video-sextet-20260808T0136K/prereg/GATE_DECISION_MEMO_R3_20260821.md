REFUTED_DECISION_MEMO_R3

# Adversarial re-gate — Decision Memo Revision 3 and Chi Custody Receipt Revision 4

## Verdict

The two-artifact record is **REFUTED as an accurate generated custody and factual record**. The central procedural theory still survives: the frozen text contains no anti-abandonment duty; footprint-aware power may be the investigator's external reason to decline without becoming HC-6; and the memo does not declare a frozen outcome. The Revision-2 condition-2 ruling is also adopted accurately.

Three independent defects defeat the record. The generator attributes Revision 1 and Revision 2 to the Revision-2 re-gate merely because both hashes occur in its evidence ledger, then prints an “at most once” conclusion it never computes. It cannot see the deck/SVG-only exact chi exemplar that both documents nevertheless credit it with finding. Finally, the memo says the verdict estimator “is still built and hash-frozen,” but the specified `_verdict_20260821/verdict_runner.py` does not exist anywhere in the handoff or repository and no verdict-estimator freeze/gate record exists.

## Ranked findings

### 1. BLOCKING — the generator's gate-history attribution is semantically wrong and its count conclusion is hard-coded

`build_custody_tables.py:20-38` collects **every** current-revision hash mentioned anywhere in a gate and calls the resulting set `reviewed`. It does not distinguish the artifact under review from historical/source artifacts in an evidence ledger.

That failure fires here:

- `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md:3` identifies itself as the fresh re-gate of **Revision 2**.
- Its evidence ledger records Revision 2 SHA-256 `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76` at `:276` and Revision 1 SHA-256 `f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee` at `:277` as a source used for the repair audit.
- The generator therefore emits `reviewed: Revision 1, Revision 2`. Both hashes are genuinely present, but reporting both as reviewed targets is misleading. Revision 1's hash is a historical input; Revision 2 is the target.
- The first footprint gate records no target hash. Printing `UNRESOLVED` is appropriately conservative as an exact-byte claim. Independent semantic reading nevertheless establishes that it predates and is the HOLD that Revision 2 says it repairs.

Correct history after semantic inspection: **Revision 1 — first gate HOLD, target hash not recorded; Revision 2 — re-gate HOLD; Revision 3 — ungated.**

The final line is not derived at all. `build_custody_tables.py:76-77` unconditionally prints:

> `each revision above appears at most once`

No count is computed. Sets at lines 31 and 37 erase multiplicity within and across matches; the first gate remains unresolved; and any gate that merely cites an old hash is counted as reviewing it. “Each revision gated at most once” is historically supportable only after reading the gates. It is not established by this matching rule.

### 2. BLOCKING — the disclosure generator misses the deck/SVG-only exact value that both documents say it established

The rerun output is byte-identical across two executions, SHA-256 `9c256e4885f187fa6e130ce04d802fb3140f51e9e3047352601f8bc78755a5f5`. It contains only a `[COUNT]` row for `20260821T004950-hwao-report.txt`; it contains no exact chi value or raw bits.

The reason is structural and visible in the sources:

- `20260821T004950-hwao-report.txt` contains no `χ`, `0.013161621987819672`, or `0x3c57a3d8`.
- `20260821T004950-hwao-report.deck.json:55` embeds in SVG: `χ = 0.013161621987819672` and `raw bits 0x3c57a3d8`.
- The same deck-only SVG is embedded in `report-20260821T004950-hwao-report.html:79` and the `archive.html` row.
- `queue.json` maps that report to seq 26, 28, and 30.

Thus the independent fact “the exact exemplar was published three times” is true, but it is **not a generator result**. The memo calls it something “the generator establishes” (`DECISION_MEMO...:106-115`), and the receipt says it is something “the generator caught” (`CHI_CUSTODY...:58-65`). Both attributions are false.

The generator's structural blind spots are broader:

1. deck-only headings/body text, notes, `attr` values, embedded SVG text, and image/graphic captions;
2. rendered report HTML content not present in narration, including embedded slide JSON/SVG;
3. archive-only rows and archive mutations;
4. publications outside `queue.json` — it can notice a matching root `.txt` but cannot establish that it was published;
5. queue publications whose `.txt` is absent, renamed, outside the root glob, or whose audio/render differs from the authored narration;
6. files outside `2026*-*.txt` and published surfaces outside this report root;
7. disclosures not matching its three narrow regexes, including literal `χ`, ordinary decimals/raw bits, alternative sign language, `galaxies are measured`, and prospective/process counts;
8. queue-load failures, which are swallowed and converted to an empty publication map rather than failing closed;
9. sentence text after 150 characters — the output calls it `verbatim` but prints only `d['sentence'][:150]`.

Manual blind-spot inspection found real content omitted from the generated ledger:

- the exact exemplar and raw bits above;
- `2,840 galaxies are measured of 208,407` in the narration (missed by the grammar of the count regex);
- a deck-only SVG state showing `29,715` galaxies measured in `20260821T004950-hwao-report.deck.json:78`;
- the rounded/prospective process count “one galaxy at a time, 200,000 times” in `20260821T151843-hwao-report.txt:15` and its deck;
- the denominator `208,407` accompanying the more-than-33,000 progress count.

The rejected deck-note decimals `0.384410`, `0.640352`, and `0.834336` in `20260820T231235-hwao-report.deck.json:53` were also inspected. They are rejection-log metadata, not slide content, and no inspected surface identifies them as chi; they are not counted as chi values.

No additional empirical chi value or observed-sign pattern was established beyond the four individual values and two distinct observed-sign sentences already ruled in the prior gate. The outside-queue duplicate `20260820T232407-20260820T230754-tori-report.txt` is byte-identical to the queued BHU report and contains no chi disclosure. The 19:09 and 20:09 Tori publications are also clean with respect to chi.

### 3. BLOCKING — the memo falsely says a verdict estimator is built and hash-frozen

`DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md:127-130` states:

> `The verdict estimator is still built and hash-frozen per VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md`

The named spec is a build instruction, not a freeze receipt. It says the deliverable **to build** is `_verdict_20260821/verdict_runner.py` (`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md:47-50`) and that only **on PASS** should it be chmod 444 and hash-recorded (`:79-87`). Independent repository searches found:

- no `_verdict_20260821/` directory;
- no `verdict_runner.py` anywhere in this handoff or repository;
- no `PASS_VERDICT`, verdict-estimator freeze note, or verdict-estimator gate artifact.

This is a remaining composed factual sentence, not generated text, and it is false on the current bytes. The neighbouring statement that the estimator is “not run on real chi” cannot rescue the claim that a nonexistent estimator was built and frozen.

### 4. MATERIAL — only the receipt pastes generator output byte-for-byte

Programmatic fenced-block comparison against the latest rerun found:

- `CHI_CUSTODY_RECEIPT_20260821.md:16-56`: **exact match** to the complete generator output, including the final newline; 2,357 UTF-8 bytes.
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md:45-56`: **not byte-identical** to section A of the generator output. Three blank lines were removed: after the heading, between the gate rows and revision summary, and after the final line.

The memo's data fields are otherwise the same as the run. This is a formatting-only delta, but it fails the brief's explicit byte-for-byte claim and proves the memo did not paste the emitted bytes verbatim.

### 5. MATERIAL/HOLD — the carried universal custody claims remain unverified or overbroad

`CHI_CUSTODY_RECEIPT_20260821.md:91-97` re-affirms:

> `No code computes an aggregate; no aggregate artifact exists.`

The current generator does not inspect source code, report pages, decks, archives, or the protected chi tree, so it establishes none of that paragraph. The named prior memo gate had already ruled only the narrower proposition: the inspected current Python paths contain no real-chi aggregate computation; the universal code/artifact claim was unsupported.

Under this brief, nothing under `/Users/duhokim/NebulaMindData/chi_dr10_south/` could be opened or listed. Therefore “per-object records only,” the negative sweep, and absence of a neutral-named aggregate data artifact are **HOLD**, not reverified facts. Read literally across all artifacts, “no aggregate artifact exists” is also overbroad because the published 23:12 and 23:13 reports are artifacts containing a multi-value aggregation/sign summary. If “artifact” is intended to mean only a computational data product inside the protected tree, that narrower claim is unverified here.

### 6. MATERIAL — condition 2 is adopted correctly, but the record omits the independent no-publication boundary

The Revision-2 ruling is represented accurately:

- publishing the complete then-existing multiset of three values together is an aggregation and summary over chi;
- “one leaning each way” is independently a sign summary;
- both breach **condition 2**, not condition 1;
- no inspected artifact says a partial tertile was computed, so condition 1 is not established as breached.

The 23:12 queue time is 23:12:51 KST. Against K-8's minute-stamped 22:20 authorization represented as 22:20:00, the interval is 52m51s, so “52 minutes” is accurate at source precision. Seq 20/21/22 and seq 26/28/30 timestamps match `queue.json`.

However, `K8_CROSSING_AUTHORIZATION_20260820.md:46-50` separately says this authorization does **not** authorize “unblinding anything” or “publication of any kind.” The current receipt's “breach, as it now stands” discusses only condition 2. That does not overstate condition 2, but it understates the governing record: every publication event was independently outside section 4's authorization, including a single per-object exemplar and progress counts even where they are not summaries over chi.

## Ruling on chi-population counts

Counts such as “2,840 galaxies now carry a real chirality value” are **outside condition 2's prohibition on a summary over chi values**. They depend on receipt/measurement existence, not on the numerical value or sign of chi, and reveal no empirical distribution. “One positive and one negative,” by contrast, groups records by the sign of chi and is a condition-2 summary.

The heading “No aggregation” is broad, but its operative text immediately distinguishes per-object measurements from sky statistics, dipoles, and summaries **over chi**. A progress count is an aggregate of custody state, not an aggregation of chi values. This confirms the prior gate's narrower ruling. It does **not** make publication permitted: section 4 independently withheld authorization for publication of any kind.

## Composed-fact and procedural audit

### Facts that held

- The generator SHA-256 printed in both documents is correct: `0d4053fb0365b1e2a78efd820781030e405a79fb7e0ede223dafd12385d0f0cc`.
- Superseded memo Revision 1/2 and custody Revision 1/2/3 hashes match the hashes recorded by their prior gates, supporting byte retention.
- Freeze-time HC-6 figures `N=130,076`, `a=0.999711`, `A_eff=0.04077642`, and power approximately `1.0000` match the frozen preregistration and BS-8 receipt.
- `sim_power.py` draws `costheta` uniformly on `[-1,1]`, states `mean(cos^2)=1/3`, and uses a two-sided analytical p-value, while frozen F-3 is one-sided.
- The second HC-6 evaluation cannot yet occur because realized accepted `N` and the lower-bound full-HC-1H `a` do not exist. The optional 150-label pilot and full 850-label HC-1H are now distinguished correctly, and the downstream uses of `a` are no longer understated.
- The footprint figures `Var(c)=0.057985`, 36,253 full-sphere-equivalent upper bound, noncentrality bound `4.4888`, and one-sided 0.95 requirement `4.7351` match Revision 3 and derivations in its re-gate.
- The four unique individual-value disclosures, two distinct observed-sign sentences, and named republication seq numbers are accurate after independent surface inspection.
- The predecessor declarations exist and their gates refuted them.

### Procedural theory and frozen-outcome drift

No frozen-outcome drift was found. The memo explicitly leaves HC-6 unexecuted, asserts no PASS, declares none of the four frozen outcomes, and labels the halt as an investigator decision. The frozen text contains no anti-abandonment clause and does not require manufacture of an outcome when the statistic is not run. A footprint calculation used as a human's external reason is not substitution inside HC-6. The Longo, sky, BHU, and mechanics-versus-statistics boundaries remain appropriately scoped.

The procedural theory therefore survives. It does not cure the generator-history failure, false generator attribution, nonexistent-estimator claim, or unverified universal custody claims.

## Failed attacks

- **Frozen-outcome attack failed:** no F-6 disposition, PASS, VOID, or new outcome is asserted.
- **Anti-abandonment attack failed:** no frozen completion duty was found.
- **External-reason-as-HC-6 attack failed:** the footprint analysis remains outside the frozen gate.
- **Power-number attack failed:** the memo's named power/geometry numbers trace to the frozen receipt and footprint gate record.
- **Pilot/full-hand-check attack failed:** Revision 3 accurately distinguishes the optional 150-label pilot from full 850-label HC-1H.
- **Condition-number attack failed:** condition 2, not condition 1, is now named correctly.
- **Timing/sequence attack failed:** 52 minutes and seq 20/21/22/26/28/30 match queue evidence.
- **Additional-value/sign hunt failed:** the complete post-crossing root-text/page/deck/archive sweep found no fifth individual value and no third observed-sign sentence.
- **Outside-queue BHU duplicate attack failed:** it is byte-identical to the queued Tori report and contains no chi disclosure.
- **Receipt byte-paste attack failed:** Revision 4's fenced ledger is exactly the latest generator output.

## Corpus closure and generator run

At final inventory time the post-crossing corpus comprised 16 queue publication events, 12 unique queued MP3 identities, 13 root authored `.txt` identities, 12 matching report pages, 12 matching deck JSON files, and five archive pages. Every queue event had an existing root `.txt`; one additional root text (`20260820T232407-20260820T230754-tori-report.txt`) was outside the queue. Only `archive.html` contained post-crossing rows. The generator was rerun after the seq-36 publication appeared; its output remained byte-identical because that new Tori report contains no chi disclosure.

## SHA-256 evidence ledger — every reviewed artifact

### Prereg/source artifacts

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/sim_power.py` — `f2867dbf4f5ab8ad82d645324a525a75af38006ff03e8ee08b90589cff50b1ce`
- `CHI_CUSTODY_RECEIPT_20260821.md` — `acfbe00cdf53aa1bc5c060da3af98473139e9cdc486a37cdf6cb5b248dd3f67b`
- `CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md` — `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e`
- `CHI_CUSTODY_RECEIPT_20260821_REV2_SUPERSEDED.md` — `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c`
- `CHI_CUSTODY_RECEIPT_20260821_REV3_SUPERSEDED.md` — `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md` — `bafec8bf5f177830d4eeac75a0a7b29c72ea9b7dcfedd3b33f697a283836c62d`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV1_SUPERSEDED.md` — `a683bc9424f26fdeabccd414aecdc0b67f08bab86307015e68294612d6a7a5bb`
- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821_REV2_SUPERSEDED.md` — `7e1b2e2f4f104ce171c6e9e50ed843ef70417a5f76216bf4e0618b0163ded64f`
- `DECLARATION_INCONCLUSIVE_BY_POWER_20260821_REFUTED.md` — `af51507a43fcdee4e53b51502c332e3624611bb27de6d0bede120b33c8b38ebb`
- `DECLARATION_VOID_ON_DESIGN_DEFECT_20260821_REFUTED.md` — `e55460743358bbb0b8c16b8d99e5f4260d0f57a88096dc2c0328f6a675b805ba`
- `GATE_DECISION_MEMO_20260821.md` — `a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa`
- `GATE_DECISION_MEMO_R2_20260821.md` — `59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066`
- `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md` — `94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e`
- `GATE_FOOTPRINT_GEOMETRY_20260821.md` — `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`
- `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md` — `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`
- `GATE_VOID_ON_DESIGN_DEFECT_20260821.md` — `38e789547e750d21b38fd9d1fa3515bc44ed8f95d542476183d45274c7518b3c`
- `GORU_BS8_POWER_RECEIPT_20260814.md` — `b6207c7fc93ea7bfeb8045d0e635693010644633b747b298eb51b6233f014a92`
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` — `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md` — `f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee`
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md` — `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76`
- `K8_CROSSING_AUTHORIZATION_20260820.md` — `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `SUCCESSOR_SCOPE_20260821.md` — `cfca55edaf7d9fe7a8d1dc70f069f4d865ec41b1fb243b3a06f8020e6784b112`
- `VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` — `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`
- `_custody_20260821/build_custody_tables.py` — `0d4053fb0365b1e2a78efd820781030e405a79fb7e0ede223dafd12385d0f0cc`

### Status-audio corpus

- `20260820T230754-tori-report.deck.json` — `d84bf963ce608387298041262614314c1cb7fa4608666178c4ed341a10677928`
- `20260820T230754-tori-report.txt` — `7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47`
- `20260820T231235-hwao-report.deck.json` — `1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c`
- `20260820T231235-hwao-report.txt` — `7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad`
- `20260820T231324-hwao-report.deck.json` — `855da9448492112c0529476cf451466934c63474068419cb3382009bfb9108ab`
- `20260820T231324-hwao-report.txt` — `5ba48ea353bb94a3a5740c4be8160e552e996670287f124fb66b69d5cf781842`
- `20260820T232407-20260820T230754-tori-report.txt` — `7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47`
- `20260820T235925-tori-report.deck.json` — `1af45a7e0cb275f3a3605aa3f3b68e78f899421939306ebac45f8448b66a1f12`
- `20260820T235925-tori-report.txt` — `e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e`
- `20260821T004950-hwao-report.deck.json` — `c49c71978ee27eedab93076906a27f188eee3b4b905caed13b674127feab091b`
- `20260821T004950-hwao-report.txt` — `f1096d51b237dbeaddf92b034194ed9f23d89401b54bb26335b74d1ead81b258`
- `20260821T080428-blanc-report.deck.json` — `81e12c9a380d2f8a5bb65f2b81d45a0da8dc2877cf8dd22f9bb1dc5da504a3cb`
- `20260821T080428-blanc-report.txt` — `452f13b624ff952df0987b7f54feccc632fde6c0f2eb569c365fa92ab968a982`
- `20260821T105930-blanc-report.deck.json` — `88394b89139669d66bef04ea85c62f591490f11ef767b5f14421784b2a54f131`
- `20260821T105930-blanc-report.txt` — `ada74c9a1761ba02f9f0c0fb6c31a3415d4fc80a2619a8776905101d1e146951`
- `20260821T145923-hwao-report.deck.json` — `8b3ddead69fb6764df63a35352eca9332b52b9472d4626a6e5e05430f20b4ad1`
- `20260821T145923-hwao-report.txt` — `c3aefdeea36b45e60f63e297bfed77358fda8db3d63560c245386b3d20cba8b2`
- `20260821T151249-hwao-report.deck.json` — `0fe5ecac190cfcb490cdcc42aa52b1069e7bf2a3b97d996d3faf13ae0030b8cc`
- `20260821T151249-hwao-report.txt` — `5648a55e23f6fddfdd9d215c1c64ea8eaf83c6a51fdec991a5f67ba31dc6e37b`
- `20260821T151843-hwao-report.deck.json` — `6437b0993110b9dca73b811017a0ba49803faa255a413cb89a2ad1c754a691ad`
- `20260821T151843-hwao-report.txt` — `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c`
- `20260821T190931-tori-report.deck.json` — `ec91f2ed3499f2bb2d291154b9a18c43b00841082853ac46c31f57a97d192998`
- `20260821T190931-tori-report.txt` — `c42bc1d4500a8e0db4411715c1237da0ebf9a39d9d88eb1fa7d633367281770b`
- `20260821T200910-tori-report.deck.json` — `f208eaab7cec9040fa0063bb9f722aab36046ffbae4c49216fb8dc305def1d55`
- `20260821T200910-tori-report.txt` — `1b7d622e8ef866752b1c9e82ae5d3edb97ebd85c0a9de18847801f32ea658940`
- `archive-2.html` — `56b88cd95c311e7873b4ad9cfb9a2265231d97383391489b9d5e73e736ead294`
- `archive-3.html` — `0ddd4df64cc83208cc0bdd1af390f3e9a9edb66720aa6435125ef4f09ef536a9`
- `archive-4.html` — `24f82b0f9d7030565df169370a5eb82847630f4116b9f4924fc33d376ac58da2`
- `archive-5.html` — `ca997cfda47a5638f1f66fe7846cee2bd2999ac46dee4c6c1dc1373b7a320cd7`
- `archive.html` — `103f7d20094575c330be1ed9bbfe1b737223ea778b0c663afcbcfc8a9a3b7599`
- `queue.json` — `33bffde3766639a20d24bc849ddd170a6b4ae4f91590a8f90b94c2f02cdcaf7c`
- `report-20260820T230754-tori-report.html` — `8db823083a03eb9afbc20e12631a44665a4f8081eca6b6e4a23f18eed2db8913`
- `report-20260820T231235-hwao-report.html` — `c5d5d5b81f5ae997e239203d2cd8e7e6c3065dc043069830ba138a29b9f6e9e7`
- `report-20260820T231324-hwao-report.html` — `861e633683a49c70ca15d7d2a0e0e1fe21f7ea163111085cc13f4c03ebd82ad1`
- `report-20260820T235925-tori-report.html` — `1ebde8a62d1393996e7bca9350e9c84aa2993a57cffd7b93a5b9ed358e04d256`
- `report-20260821T004950-hwao-report.html` — `d4693eb627d5785354cfa0c27057f48508f24cb88697297941c5b51c01fbbb85`
- `report-20260821T080428-blanc-report.html` — `18734d3fdd389a1e000ffed169652a61d1a6cdcd695b201d7798b236f296fb9d`
- `report-20260821T105930-blanc-report.html` — `b832d6104df258bf8bed779d24229ce0ae49974f65e6026ce678e4a547f08b29`
- `report-20260821T145923-hwao-report.html` — `7dcf8e2ba41917e28987cbaf3317766499b361310030133535b2bff29bdeca77`
- `report-20260821T151249-hwao-report.html` — `f11078cce4e69efa4f59d37fd3681e18243cad80adce59571c99ca79588da0dd`
- `report-20260821T151843-hwao-report.html` — `849829d266274149e6a9f1d4fb22200929cbd218b3adef291502fdc07074cb87`
- `report-20260821T190931-tori-report.html` — `1071f27aee6325973e0b04664274568e8fdbbe4345f8576ee3f85b109421ca27`
- `report-20260821T200910-tori-report.html` — `51216d69a089dd4240c5b75e9ea5f737e4faa4b4b140bb2c3f26a68ce9ac7a14`

### Lane-local temporary evidence reviewed

- `_tmp_gate_memo3_generator.txt` — `9c256e4885f187fa6e130ce04d802fb3140f51e9e3047352601f8bc78755a5f5`
- `_tmp_gate_memo3_generator_latest.txt` — `9c256e4885f187fa6e130ce04d802fb3140f51e9e3047352601f8bc78755a5f5`
- `_tmp_gate_memo3_inventory.py` — `74520f3ed4d53a308bac469f592475eda822cfdeab39fe468a04a9fe70b1d024`
- `_tmp_gate_memo3_inventory.json` — `442f33261e729627132823b804e038a0f4416a5011ffc232ce139ec065f7b1a4`

## Mechanical evidence and hard boundaries

Performed: two generator executions; byte comparison of generated output against each fenced table; exact SHA-256 matching of all three footprint revisions and both gates; semantic target-versus-source reading of the gate histories; queue reconstruction with republications; full post-crossing root-text/page/deck/archive inventory; manual inspection of candidate narration, deck bodies, embedded SVG, `attr`, notes, HTML, archive rows, outside-queue text, and missing-text closure; exact-value/raw-bits searches; interval arithmetic; repository-wide search for the claimed verdict estimator and freeze/gate markers.

No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, or read. No chi value came from that tree and no statistic over chi was computed. All chi content inspected was already present in published narration, deck, report-page, or archive surfaces. No remedy is proposed. No reviewed artifact, report surface, queue, database, runtime, git state, or source file was changed. Writes were limited to this gate report and lane-local `_tmp_gate_memo3_*` evidence files permitted by the brief.
