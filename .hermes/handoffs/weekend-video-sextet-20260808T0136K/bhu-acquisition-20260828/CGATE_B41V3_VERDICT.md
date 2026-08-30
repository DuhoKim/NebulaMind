B41V3_REFUTED_RECEIPT_BINDINGS

# B41V3 adversarial verdict

V3 repairs the two substantive holes identified against V1: entry 5 is now honestly identified as both outside the deployed scan pool and invisible to the criterion when scanned counterfactually, and B43 supplies entry 38's previously missing full sequential read. The underlying record now supports a 39/39 reading census. The submitted closer is nevertheless not sound as a proof: its green receipt predicate still validates loosely combined strings where it claims to bind full-read facts, and it does so in several load-bearing rows.

I read the complete V3 docstring and every check, ran the file unchanged (`14/14`), recomputed the entry-5 counts, inspected every named batch verdict, checked the B29 sample verdict, and traced the flag artifacts.

## 1. Coverage wording

The revised phrase “every readable BHU paper has a receipted read and obstruction adjudication” is materially better than “uniform procedure.” It correctly discloses that entry 6's read predates B28, that the flags use separate artifacts, that the not-located list is inherited rather than reverified, and that current bibliography labels are adjudicated records rather than independent ground truth.

As a description of the accumulated human record, 39/39 is supportable after B43. As the conclusion of this script's predicates, it is not. `covered` is a union of hand-declared sets. The `COVERAGE` check proves only that those declarations partition `READABLE`; it inherits every receipt-binding defect below. Its detail saying “b43 is it” does not inspect the B43 gate verdict.

The wording should therefore distinguish:

- **record-level conclusion:** the reviewed artifacts, including B43 and the prior refreshed receipts cited in CGATE_B41, support 39/39;
- **script-level conclusion:** the current predicates do not prove that every declared set member has the claimed receipt.

## 2. Entry-5 counterfactual

This repair is correct. V3 opens the actual pool-external entry-5 file at `reviews/bhu-citation-custody-evidence-20260811/arxiv-1412.0105v1.txt`, normalizes it in the same way as the deployment loop, applies the same three regexes, and obtains `(0,0,0)` against thresholds `(5,2,2)`. I independently reproduced those counts. `is_obstruction(t5)` is false.

“Double miss” is fair, not spin, provided “screen” is understood operationally: entry 5 was not in the mapped deployment pool at all, and adding its actual text to that pool would still not have flagged it. V3 prints both failure modes and the pool boundary. The extra `"Pathria" in t5` test is only a weak identity landmark, but it does not alter the correctly computed counterfactual.

## 3. Per-batch verdict bindings

The advertised predicate is false as an implementation claim. The comment promises each set is bound to “its own gate verdict (token + read phrase).” The table and loop do not enforce that reliably.

### B37: five full reads are used to receipt nine

The B37 set is nine entries: `{9,23,26,41,44,45,52,53,54}`. `CGATE_B37_VERDICT.md` says:

> I read these five required sources in full for this gate

and names entries 9, 41, 45, 52, and 53. It then says it refreshed prior receipts for 23, 26, 44, and 54. V3 checks only whether the generic substring `in full` occurs anywhere in that verdict. Thus the row would pass even if those four prior receipts did not exist. The set fragment comes from `b37_census_final.py`, while the read phrase comes from an unrelated subset in the verdict; no predicate joins an entry identity to its receipt.

The historical B37 coverage can still be valid—the earlier CGATE_B41 audit manually traced the four refreshed receipts—but V3 does not bind them. It must require either explicit per-entry receipt references or a verdict sentence whose scope is all nine.

### B43: no gate verdict and no token

The B43 row sets both `art` and `vart` to `b43_entry38_fullread.py`, sets `vtok=None`, and searches that self-describing script for `read IN FULL under the census rule`. It never opens `CGATE_B43_VERDICT.md`, whose first-line token is `ENTRY38_NARROWED_THEOREM8_STATEMENT_AND_SCOPE` and whose opening paragraph contains the actual independent full-read declaration.

This directly contradicts the check name “its own gate verdict (token + read phrase)” and the detail's attempt to excuse the omission with “b43's gate verdicts land separately.” The gate verdict has landed and is present. Bind it.

### B32 and the other rows

The B32 row uses `CGATE_B32_VERDICT.md` as both batch artifact and verdict. Its entry-57 full-read sentence is real and its token is checked, so the underlying receipt is sound, although the “committed artifact AND verdict” distinction collapses to one file.

B33, B34, B36, B38, and B39 have verdict phrases that genuinely scope their named sets. Their tokens are checked. The predicate is still syntactic rather than semantic, but those particular bindings agree with their records.

### The eleven-paper sample is not receipt-bound

V3 binds the B28 frame literal and recomputes the seeded eleven-paper set, but it never opens either B29 gate verdict. `CGATE_B29_VERDICT.md` explicitly says all eleven pinned papers were reread; that is the obvious receipt. The `SAMPLE` set is nevertheless inserted directly into `covered` after only a draw check. A reproducible draw proves membership, not reading or obstruction adjudication.

Consequently the closer's most important predicate can pass after deleting or corrupting the B29 read receipt. That is another string/fact gap outside the `BATCHES` loop.

## 4. Other string predicates presented as fact checks

Several check labels claim more than their predicates establish:

- **Flag 6:** the predicate looks only for the batch-9 heading in the notes and for existence of `AGATE_B25_VERDICT.md`. It does not test the notes' global full-read declaration, the entry-6 read statement, the `QUALITATIVE-DIRECTIONAL` reclassification, either B25 token, or either B25 paper-level ruling. The underlying artifacts support the narrative, but the predicate does not.
- **Flag 25:** the predicate checks only the two B25 first-line tokens. Neither token identifies entry 25 or says it was read/adjudicated. The detailed CGATE text does rule on it, but V3 does not test that connection.
- **Not-located binding:** exact occurrence of the twelve-number list proves fidelity to the wrap-up's string, not present nonlocation or login status. The docstring properly discloses this limitation, so this is acceptable only as record binding, not current acquisition proof.
- **Current ground truth:** parsing the first bold `Testability:` label computes current paper tiers, not independent truth. V3 discloses that correctly.
- **Receipt generally:** phrase occurrence cannot prove a human read. Here it can bind a signed/manual record, but only when the phrase's grammatical scope and entry identities are also checked. B37 fails that minimum.

The live-flag equality is a genuine improvement: it recomputes the criterion over its explicitly stated mapped-source pool and now fails on either an added or lost flag. It still assumes the map parser and pool membership are correct, but V3 no longer disguises the pool boundary.

## 5. Metrics and final ruling

Conditional on the adopted current paper-tier labels and the explicitly bounded deployment outcome:

- readable-paper coverage in the accumulated record is **39/39** after B43;
- the paper-tier truth set is `{5,22}`;
- the operational screen caught entry 22 and missed entry 5, so paper-tier miss rate is **1 of 2**;
- among its three mapped corpus flags `{6,22,25}`, one is a paper-tier true positive, so observed precision is **1 of 3**;
- claim-level sensitivity is **not measured**, because no frozen claim table and multiple-claims-per-paper rule exist.

Those are appropriately scoped facts, not a claim-level metric. The prose that follows is less clean: it first names recorded claim-level carriers `{25,37,38,51,52,53,57}` and says only 25 was flagged, then separately repeats AGATE's different paper list (“caught 22; missed 5,37,51,52,53”). V3 correctly refuses to turn either opportunistic list into a sensitivity denominator, but it should label them as two distinct observations rather than run them together as “AGATE's fact.”

Final ruling: the substantive census result and scoped metrics survive, but **B41V3 is refuted as the census closer submitted**. Its `14/14` score falsely represents receipt provenance. Repair the B37 four-entry prior-receipt bindings, bind B43 to `CGATE_B43_VERDICT.md` with its token, bind the B29 eleven-paper sample to its full-read verdict, and make the flag predicates test the facts named in their labels. After those changes, the same 39/39, 1-of-2, and 1-of-3 outputs can be confirmed.
