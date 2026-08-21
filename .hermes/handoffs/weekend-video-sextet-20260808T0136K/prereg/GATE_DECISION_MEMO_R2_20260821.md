REFUTED_DECISION_MEMO_R2

# Adversarial re-gate — Decision Memo Revision 2 and Chi Custody Receipt Revision 3

## Verdict

The two-artifact record is **REFUTED as an accurate custody and gate-history record**. The central procedural theory survives: the frozen text contains no anti-abandonment duty, the footprint analysis may be the investigator's external reason for declining without becoming HC-6, and Revision 2 does not assert a frozen outcome. The `a` paragraph and the 52/53-minute wall-clock intervals are also repaired.

Two material defects remain. First, the memo's exact-artifact history is still false: Revision 2 of the footprint finding was gated once, not twice; the two HOLDs apply successively to Revision 1 and Revision 2. Revision 3's current `6b2aa9a…` bytes are indeed ungated. Second, the receipt's “complete disclosure ledger” is not complete as a publication ledger or a count ledger. It omits republications of the sign-summary report and exact-value exemplar and does not enumerate several published chi-population counts. The four unique individual values and two distinct observed-sign sentences are now correctly identified, but that narrower count does not make the claimed full ledger complete.

I also rule the receipt's open condition-2 question: publishing all three then-existing chi values together was an **aggregation** and, because it transmitted the complete empirical distribution then in existence, a **summary over chi** within condition 2. The explicit “one leaning each way” sentence independently breached the same condition.

## Ranked findings

### 1. BLOCKING — Revision 2 was not “gated twice”

`DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md:40` says:

> Its Revision 2 was gated twice — both HOLD ... Revision 3's current bytes (`6b2aa9a5…`) have not been gated at all.

The second clause is correct; the first is not.

- `GATE_FOOTPRINT_GEOMETRY_20260821.md` is the first HOLD. Its findings are the defects Revision 2 says it repaired. The current finding's own history says “Revision 2 repaired three defects ruled by `GATE_FOOTPRINT_GEOMETRY_20260821.md`” (`HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md:3-4`). That gate therefore binds Revision 1, not the later repaired Revision 2.
- `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md:1-9` is explicitly the fresh gate of Revision 2. Its evidence ledger pins Revision 2 SHA-256 `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76` (`:272-279`). It returned `HOLD_FOOTPRINT_GEOMETRY_REV2`.
- Live recomputation gives the same `a9783371…` for `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md`.
- The present Revision 3 is SHA-256 `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`. Its current file mtime is 18:18:43 KST, after the Revision-2 re-gate at 17:13:47 KST. No later footprint gate exists in the named gate inventory.

Correct exact-byte history: **Revision 1 — HOLD; Revision 2 — one re-gate, HOLD; Revision 3 current bytes — ungated.** The geometry proposition survived two successive attacks, but Revision 2's bytes were not themselves reviewed twice. Revision 2 repaired the old “current Revision 3 twice gated” sentence only halfway and overshot into a new exact-artifact falsehood.

### 2. MATERIAL — the “complete disclosure ledger” omits publication events and chi-population counts

I reconstructed the post-22:20 corpus from the publication queue and then read the complete authored text, existing report page, existing deck, and relevant archive row for each report. There are 15 queue publication events after the authorization, representing 11 queue report identities because several were republished. A twelfth authored/archive identity, `20260820T232407-20260820T230754-tori-report`, is a Tori BHU duplicate absent from the queue and has no corresponding page/deck on disk.

The receipt's unique-content core is right:

- `20260820T231235-hwao-report.txt:1` publishes three approximate values — `+0.27`, `+0.20`, `-0.20` in spoken form — and “one leaning each way among the confident pair.”
- `20260820T231324-hwao-report.txt:1` repeats the sign pattern and identifies the confident pair as the pair the committee was confident about.
- `20260821T004950-hwao-report.deck.json:49-56` publishes the one exact receipt value `χ = 0.013161621987819672` and raw bits `0x3c57a3d8`.
- No other authored narration, rendered page, rendered deck content, or archive row establishes another real chi value or another observed sign pattern.

But the ledger is not complete in two ways.

#### 2a. Omitted republication events

`queue.json` records:

- the 23:13 sign-summary report first published at 23:13:40 KST (`queue.json:295-307`) and republished at 23:24:55 KST (`:310-322`);
- the exact-value exemplar first published at 00:50:18 KST (`:340-352`), then republished at 10:37:53 KST (`:370-382`) and again at 11:02:45 KST (`:400-412`);
- Tori's 23:59 BHU report republished at 16:07:09 KST (`:460-472`), which remains clean with respect to chi.

The receipt lists only the original 23:13 and 00:49 appearances. Republication does not create a new unique value or a new distinct sign sentence, but it is another publication/exposure event. A “full disclosure ledger” needs to distinguish unique disclosed content from every event that published that content; Revision 3 does not.

#### 2b. Omitted chi-population counts

The receipt's table does not enumerate these published counts:

- **23:12:** `2,725 galaxies measured` (`20260820T231235-hwao-report.txt:1`; repeated in its deck at `:35-40`).
- **23:13:** `3 galaxies were read`, a confident committee pair of two, and `2,725 galaxies measured` (`20260820T231324-hwao-report.txt:1`). The table quotes the first two facts but does not treat the measurement count as its own disclosure.
- **00:49:** `2,840 galaxies now carry a real chirality value`, versus `0` the day before, and `2,840 measured of 208,407` (`20260821T004950-hwao-report.txt:1`; deck `:8-16,59-65`).
- **14:59:** `more than 33,000 galaxies now carry a chirality value` out of `208,407` (`20260821T145923-hwao-report.txt:17`).
- **15:18:** the explanatory report says the computation is being performed “one galaxy at a time, 200,000 times” (`20260821T151843-hwao-report.txt:15`). This is a rounded/prospective process count, not a realized sign distribution, but it is still chi-process count language in the published corpus.

`CHI_CUSTODY_RECEIPT_20260821.md:28-29` acknowledges counts categorically and gives two examples, so it no longer makes Revision 2's false “no other ... count” claim. But a parenthetical containing two examples is not a complete count ledger, especially when the document titles itself “the full disclosure ledger.” These counts are not themselves summaries of the numeric chi values: they describe how many measurements exist, not their values or distribution. Their omission is a custody-completeness defect, not an additional condition-2 breach.

Non-chi counts in Tori's BHU reports and Blanc's format report (for example 77 audit rows, 48 checks, 7 load-bearing failures) are unrelated to the chirality run and are not chi-ledger entries. I read them rather than inferring cleanliness from speaker identity. Tori's post-crossing reports and both Blanc reports contain no real chi value, observed chi-sign pattern, or chirality committee state.

#### 2c. Unresolved deck-metadata literals — not counted as chi

The published `20260820T231235-hwao-report.deck.json:52-57` contains a rejection note naming three otherwise unattributed decimals: `0.384410`, `0.640352`, and `0.834336`, saying they were rejected because they were not in the audio. The same literals occur only in `postprocess.log`; no published narration, slide, page, archive row, or semantic label identifies them as chi. I therefore do **not** count them as chi values. Their provenance cannot be resolved from the permitted published surfaces, so no stronger claim about what they are is verified.

### 3. MATERIAL RULING — the three-value publication itself breached condition 2

The receipt correctly moves the breach from condition 1 to condition 2.

- Condition 1 is only the partial-tertile prohibition (`K8_CROSSING_AUTHORIZATION_20260820.md:28-31`). No inspected published artifact says a partial tertile was computed.
- Condition 2 says: “**No aggregation.** χ is a per-object measurement with a receipt. No sky statistic, no dipole, no summary over χ of any kind...” (`:32-33`).

Publishing the three then-existing values together was an aggregation under the ordinary meaning of collecting multiple per-object measurements into one disclosure. It was also a summary over chi in the relevant information sense: at N=3 the complete multiset `{+0.27,+0.20,-0.20}` is the entire empirical distribution. A summary need not be lossy; the identity representation of a three-member population transmits at least as much distributional information as any compressed statistic. Condition 2's per-object-receipt sentence authorizes per-object custody, not joint publication. Section 4 separately says publication of any kind was not authorized (`K8...:46-50`).

The explicit “one leaning each way among the confident pair” sentence is independently a compressed sign summary and breached condition 2 even if one adopted a narrower definition of aggregation. The receipt's decision to leave the three-value question open is therefore not the ruling of this gate.

### 4. MATERIAL/HOLD — no automatic consequence attaches to a condition-2 breach as such; HC-7 has a separate contingent trigger

Independent reading confirms no clause maps “condition 2 was breached” directly to a frozen disposition.

- K-8 defines consequences for parameter changes after real chi (F-9 void), apparent/confirmed polarity defects (HOLD, then F-9 if a sign-changing repair is required), gated-program refusals (stop and come to Duho), and named code changes (`K8...:20-24,37-44`). It gives no automatic consequence for condition 1 or 2 breach itself.
- F-6 exhaustively maps numeric results and triggered section-4/section-6 rules to the four frozen outcomes (`PREREG...V3.md:141-145`). A publication/aggregation breach is not added as an F-6 trigger.
- F-10 expressly adds no new kill switch (`PREREG...V3.md:470-474`). F-9 requires a parameter change; the published surfaces do not establish one.

HC-7 does define a consequence for the distinct predicate “machine/instrument signs visible to the checker”: hard INCONCLUSIVE and the affected measurement void (`PREREG...V3.md:311-318`). Duho is the named checker (`:279-289`). The reports prove publication and public availability of sign information, but the permitted surfaces do not prove that Duho actually saw/heard it before hand-checking, nor that any sign was linked to an image he would later label. Therefore:

- **automatic consequence of the condition-2 breach itself:** none defined;
- **whether the separate HC-7 visibility predicate fired:** HOLD on the permitted evidence;
- **if actual checker visibility is established:** HC-7 already defines hard INCONCLUSIVE for that predicate.

This is narrower than saying HC-7 is irrelevant and more conservative than declaring it fired from mere publication.

### 5. Repair audit of the memo's remaining factual claims

#### Gate history — FAIL

As finding 1 establishes: Revision 3 ungated is correct; Revision 2 gated twice is false.

#### The `a` paragraph — PASS

`DECISION_MEMO...:25-29,51-56` now distinguishes the optional 150-label pilot from the full 850-label HC-1H and states the pilot's two outcomes correctly.

The frozen text confirms:

- full HC-1H is 850 labels: 500 real, 200 synthetic, 150 mirrored (`PREREG...V3.md:279-284`);
- final `a` is the synthetic-error-corrected HC-1H attenuation estimate (`:290-300`);
- the optional 150-label pilot has only PASS-TO-FULL-HC1H or INCONCLUSIVE, and its 40 synthetics do not enter final epsilon (`:331-333`);
- `a` enters `A_eff` for HC-6 (`:319-329`), `sigma_ours` and the propagated F-6 bands (`:290-301`), as well as the corrected amplitude and F-6 formulas (`:130-150`).

The memo no longer says the pilot itself yields final `a` and no longer says HC-6 is `a`'s only use. The word “optional” prevents its “pilot first” phrasing from becoming a claim that the pilot is mandatory.

#### 52-minute and 53-minute intervals — PASS at the source's precision

K-8 is timestamped only to 22:20 KST (`K8...:3-4`). The queue records 23:12:51 and 23:13:40. If the authorization minute is represented as 22:20:00, elapsed times are 52m51s and 53m40s. The report pages display only 23:12 and 23:13. Thus “52 minutes” and “53 minutes” are correct minute-label intervals; the source does not support second-level precision for the authorization.

### 6. Procedural theory — survives; no frozen-outcome drift found

I found no frozen clause requiring an investigator to continue, requiring entry into an F-6 decision region once acquisition begins, or defining withdrawal itself as a preregistered event.

- F-6 defines outcomes when its numeric or named trigger predicates exist (`PREREG...V3.md:141-145`).
- Section 7 requires publication of all outcomes, but does not require manufacture of an outcome when the statistic is not run (`:396-406`).
- K-8 authorizes incremental per-object chi under conditions and contains its own stop paths (`K8...:26-56`).

The memo keeps the footprint analysis in the role of an investigator's external reason. It explicitly leaves the second HC-6 evaluation unexecuted, says no PASS is asserted, and reports “Halted by investigator decision. No preregistered outcome reported” (`DECISION_MEMO...:21-36,73-77`). It does not call the footprint bound an HC-6 failure, does not declare INCONCLUSIVE-BY-POWER, and does not invent a frozen VOID category. Using a non-frozen analysis as the human reason to stop is therefore not substitution inside HC-6.

The continued-acquisition sentence does not itself create a frozen outcome. K-8 contains no automatic authorization revocation for a condition-2 breach, but it also does not affirmatively re-clear post-breach custody. The abstract claim that no frozen anti-abandonment rule bars investigator withdrawal survives; any actual HC-7 checker-exposure predicate remains HOLD as stated above.

## Failed attacks

- **Condition attribution attack failed:** the receipt now correctly identifies condition 2, not condition 1.
- **Unique value/sign recount attack failed:** the corpus establishes four unique individual values and two distinct observed-sign sentences, all in Hwao artifacts; no additional real chi value or observed sign pattern was established.
- **Tori/Blanc attack failed:** all post-crossing Tori and Blanc narrations/pages/decks/archive rows were read; their counts are BHU/operations counts, not chi disclosures.
- **Current-Revision-3 custody attack failed:** SHA-256 `6b2aa9a5…` is correct and those bytes are ungated.
- **`a`-mechanism attack failed:** pilot/full-HC-1H outcomes and downstream uses are now correctly stated.
- **Timing attack failed:** 52 and 53 minutes are correct at the source timestamps' minute precision.
- **Anti-abandonment attack failed:** no frozen completion duty was found.
- **Reason-as-HC-6-substitution attack failed:** the memo preserves HC-6 unexecuted and issues no frozen result.
- **Frozen-outcome-drift attack failed:** the memo remains an outside-preregistration decision request, not an F-6 disposition.
- **Automatic-consequence attack failed:** condition 2 has no automatic mapped disposition; HC-7 is contingent on a separately established checker-visibility predicate.

These failed attacks show that an accurately custodied Revision 2 memo could be procedurally coherent. They do not cure the exact gate-history falsehood or the incomplete disclosure-event/count ledger.

## Evidence ledger and boundaries

### Read as content

- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md` — SHA-256 `7e1b2e2f4f104ce171c6e9e50ed843ef70417a5f76216bf4e0618b0163ded64f`;
- `CHI_CUSTODY_RECEIPT_20260821.md` Revision 3 — `9c2c9cad6b85b8917f09af190e149fa49f63d9b15ebdb05e8d7fcb76938e7093`;
- prior memo gate and the superseded memo/receipt revisions needed to identify the repairs;
- `K8_CROSSING_AUTHORIZATION_20260820.md` — `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`;
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`;
- all three footprint-finding revisions and both footprint gates; current Revision 3 is `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`, superseded Revision 2 is `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76`;
- `queue.json` for every post-authorization publication timestamp, including republications;
- all 12 post-crossing authored report texts in the report root;
- all 11 existing matching report pages and all 11 existing matching deck JSON files;
- all five `archive*.html` files; only `archive.html` contains post-crossing rows, 12 in total.

### Mechanical checks

- exact corpus inventory by timestamp and publication queue;
- full-text extraction of every page and every matching archive row, followed by semantic reading rather than numeric-pattern inference;
- direct reading of every authored narration and decoded deck, including spoken-word numbers and deck metadata notes;
- SHA-256 and mtime recomputation for memo, receipt, footprint revisions, footprint gates, frozen preregistration, and K-8 authorization;
- elapsed-time arithmetic from the queue timestamps.

### Limits and hard-boundary compliance

No path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, or read. No chi value was obtained from that tree, and no statistic over chi was computed. Every disclosure cited here came from already-published narration, page, deck, archive, or publication-queue artifacts. The footprint result was assessed only through published finding/gate records; no underlying science-data tree was opened. No remedy is proposed.

The only temporary files created were lane-local files beginning `_tmp_gate_memo2_`. No reviewed artifact, public report, database, process, git state, or runtime was changed. This gate report is the only substantive output write.
