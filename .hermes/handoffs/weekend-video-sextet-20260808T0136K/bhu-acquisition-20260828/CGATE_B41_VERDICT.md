COVERAGE_REFUTED_ENTRY38_UNRECEIPTED

# B41 adversarial verdict — census coverage proof

The set arithmetic is reproducible, but one of its premises is false as an evidentiary claim. B32 explicitly records a full read of entry 57; neither B32 gate verdict records a full read of entry 38. B41 binds `{38,57}` only to a sentence in the later `b33_census_batch2.py` that asserts they were already “done.” That is circular testimony, not a binding to the adjudication artifacts. On the lane's own full-read standard, the demonstrated coverage is therefore **38 of 39 readable papers**, and the unflagged-unsampled remainder is **24 of 25**, with entry 38 still requiring a full obstruction-rule read.

I read `b41_census_coverage.py`, reran it unchanged (`10/10`), checked every declared batch against its brief and both gate verdicts, traced all three screen flags, inspected the live map parser and its relevant map rows, and compared the denominator to the recorded claim-level exclusions.

## 1. Binding-by-substring

### B33, B34, B36, B37, B38, and B39 sets

These declared sets agree with the papers actually adjudicated in their named rounds:

| B41 declaration | actual gate record | result |
|---|---|---|
| B33 `{8,43,55}` | both B33 verdicts state all three were read in full | bound correctly |
| B34 `{51,31,12}` | both B34 verdicts state all three were read in full | bound correctly |
| B36 `{39,21,11}` | both B36 verdicts state all three were read in full | bound correctly |
| B37 `{9,23,26,41,44,45,52,53,54}` | CGATE lists full reads for 9/41/45/52/53 and refreshed prior full-read receipts for 23/26/44/54; AGATE adjudicates the same nine | set correct |
| B38 `{15,17,20,28}` | both B38 verdicts state all four were read in full | bound correctly |
| B39 `{19}` | both gates read the capture; CGATE also checked it against the original article | bound correctly |

B37's result later changed at Q7, but the reading receipt remains valid. B34's seats split over entry 51's paper-level tier, but both read and adjudicated the same three papers. Those are classification disputes, not coverage defects.

### The B32 `{38,57}` declaration is not bound

B41 declares:

`"b32 gate-reads": ({38,57}, "b33_census_batch2.py", "38 and 57 were done in b32's")`.

This does not inspect `GATE_BRIEF_B32.md`, `CGATE_B32_VERDICT.md`, or `AGATE_B32_VERDICT.md`. It searches a later script for that later script's own assertion.

The actual B32 record is asymmetric:

- the B32 brief orders a proper full read of **entry 57**;
- CGATE says, in its opening sentence, “I read entry 57 in full, all 39 PDF pages”;
- AGATE likewise says “I have read Entry 57 in full using fitz”;
- neither verdict says entry 38 was read in full;
- CGATE analyzes entry 38's relevant Section 4 argument and two limitation passages, while AGATE says it “audited the claims surrounding Entry 38,” but neither supplies a sequential/full-read receipt.

The later B33 script upgrades this into “38 and 57 were done in b32's gate” and, still more strongly, prints “38, 57 by full gate reads.” B41 then treats that later assertion as proof of the earlier event. Exact substring matching prevents silent textual drift; it does not establish truth.

This matters because every later batch brief expressly required full reads or identified prior full-read receipts. Entry 38 cannot be held to a weaker, implied standard only because including it makes the union close.

**Corrected coverage:** remove entry 38 from the receipted batch union pending a full source read under the fixed rule. Then:

- covered readable papers: `38/39`;
- batch remainder read: `24/25`;
- missing paper: entry `38`.

The existing B32 work makes the outstanding read targeted and cheap; it does not make the receipt exist.

## 2. Provenance of flags 6, 22, and 25

The three flags have substantive adjudication artifacts, although B41 does not bind them.

### Entry 6

The bibliography's batch-9 note and `bhu-reading-20260823/READING_NOTES_01.md` record a full read of Smolin 1992 and its reclassification to `QUALITATIVE-DIRECTIONAL`. B25 then applies the obstruction question to the matched passages and paper framing; both B25 gates rule it a paper-level false positive.

This is not testimony with no artifact. The full read predates the census and was aimed at classification rather than this precise rule, but the later B25 adjudication supplies the rule-specific decision.

### Entry 22

Entry 22 has the strongest receipt of the three. B24's CGATE states that it read the complete source, including Propositions 1 and 2, Theorem 1, extensions, escapes, and conclusion. Its paper-level obstruction classification and scoped domain were gated. It is a valid true-positive adjudication.

### Entry 25

B25 directly audits the flag, reads the matched passages plus abstract and conclusion, and both gates reject a paper-level obstruction tier. CGATE also preserves the narrower Buchdahl-based claim-level exclusion. The source is pinned and the current bibliography keeps the constructive/directional paper-level tier.

That is an artifact-backed flag adjudication, though it illustrates why “hand-checked” should not be expanded to “every flag received a fresh sequential full read under B28.” The directive at issue concerns the **unflagged remainder**, so this distinction does not itself leave another member of that remainder unread.

B41 should bind each flag to these actual artifacts rather than merely declare `FROZEN_FLAGS` and describe them as hand-checked.

## 3. Map-parse misattribution

The three live corpus flags are mapped correctly on the current files:

- `smolin_1992_clean.txt -> 6`;
- `2606.25023_clean.txt -> 22`;
- `sym14091849_clean.txt -> 25`.

I found no current misnumbering of those three.

The parser nevertheless does not prove mapping integrity:

1. It extracts all one- or two-digit strings from the first table cell and takes `nums[-1]`; this happens to handle the corrected `~~1~~ **46**` row but is not a structural entry-number parse.
2. It treats every backticked item on a row as a potential file, including hashes and prose literals.
3. `setdefault` silently preserves the first mapping if two rows normalize to the same stem; it never reports collisions.
4. It checks no title, byline, DOI, hash, or one-to-one uniqueness.
5. It scans only `*_clean.txt` in one source directory, while the canonical map contains PDFs and sources elsewhere in the repository.
6. Most importantly, the binding check is `FROZEN_FLAGS <= live_flags`, not equality. An additional live mapped flag would leave the check green and would be excluded from `FROZEN_FLAGS`, the precision denominator, and the coverage partition.

The present printed `live_flags` happens to equal `{6,22,25}`, so this is a predicate weakness rather than a discovered fourth flag. Replace the subset check with equality and independently validate the three stem-to-entry joins (or consume a canonical, uniquely keyed map).

## 4. Miss-rate denominator

For the screen's stated deployment target—the **paper-level `THEORETICAL-OBSTRUCTION` tier**—the denominator `{5,22}` is conceptually correct under the corpus's adopted one-label-per-paper convention. Entry 22 is hit and entry 5 is missed, so:

- paper-level recall on the currently adjudicated readable census: `1/2`;
- paper-level miss rate: `1/2`;
- paper-level precision among the three flags: `1/3`.

The outstanding full read of entry 38 prevents calling that result final over a closed 39-paper census, although B32's extensive claim audit makes a tier-changing surprise unlikely. The honest current wording is “provisional paper-level result on 38 fully receipted papers plus a partial entry-38 audit,” not “measured over a FULL census.”

The denominator is **not** an honest measure of sensitivity to obstruction content anywhere in a paper. The record contains claim-level exclusions in at least entries 37, 38, 51, 52, 53, and 57, with further adjudicated examples in entries 15, 17, 19, 20, 21, 25, 41, and 55. Some are strong no-solution or necessary-condition results. Parsing only the primary `Testability:` label intentionally erases them.

That erasure is legitimate only because B1 was defined as a paper-tier screen. If the lane wishes to report claim-content sensitivity, it needs a separately frozen claim-level ground-truth table and a rule for multiple claims per paper. Using only the six claim-level examples named in the B41 brief plus paper-level entries 5 and 22, B1 hits only entry 22: it misses **7 of those 8 papers**. But I would not print `7/8` as a corpus metric, because that list is illustrative and incomplete (entry 25 is itself both a screen hit and a recorded claim-level exclusion). The correct report is:

> Paper-tier miss rate: provisionally `1/2`. Claim-level exclusion recall: not measured; known examples show it is materially worse and require a separate denominator.

Thus B41's `1/2` is not inherently dishonest, but its label must say **paper-level**, and “the screen” must not be generalized to obstruction-content discovery.

## 5. Does prior work discharge Duho's order?

The natural reading of “read the unflagged remainder” is outcome-oriented, not a demand to reread papers solely because the instruction arrived after equivalent work. The question-3 precedent—“then look harder with more entries”—supports continuing and broadening the survey, not ritual duplication. Prior full reads under the same fixed obstruction rule can discharge the order if their identities, scope, and completeness are receipted.

Accordingly, it is honest to count entry 57's B32 full gate read even though it predates the order. It would waste effort to exclude it merely on chronology. The same is true of the other properly receipted batches.

It is not honest to count entry 38 as a **full census read** merely because B32 examined the passages relevant to a particular candidate. The record supports prior-work credit; it does not support manufacturing a full-read receipt retrospectively. Duho's directive is therefore almost discharged, but not completely: perform the missing full read of entry 38 and gate its fixed-rule paper-level verdict.

## 6. Predicate audit

### Checks that compute useful arithmetic

- `PARTITION` genuinely checks the cardinalities and disjointness of the hand-declared `BHU`, `NOT_LOCATED`, and derived `READABLE` sets.
- `RE-DRAWN` genuinely reproduces the 11-paper sample from the stated seed and frame.
- `COVERAGE` and `REMAINDER` genuinely compute set equality and differences from the supplied sets.
- the final hit/miss calculation genuinely computes intersections between parsed paper-level labels and `FROZEN_FLAGS`.

Those calculations are correct conditional on their inputs.

### Checks that validate strings or circular declarations

1. **Not-located binding:** one substring in the wrap-up proves only that the same list is repeated. It does not verify current file absence, readability, BHU/support status, or the detail claim that all twelve are paywalled.
2. **BHU/support frame:** the 51-paper universe and seven support IDs are re-declared, not parsed from the current bibliography.
3. **Live flags:** the regex is rerun, but only on mapped `*_clean.txt` files in one directory. Map correctness and source completeness are assumed. The check permits extra live flags because it uses subset rather than equality.
4. **B28 frame binding:** exact presence of the list proves fidelity to B28 text, not that every member is readable or correctly identified.
5. **Batch binding:** the global `all(frag in artifact)` proves only phrase presence. It does not compare declared set members with briefs/verdicts, verify full reads, require both gates, or bind dispositions. The entry-38 failure is the concrete counterexample.
6. **Obstruction parsing:** the parser reads only the first bold `Testability:` token per block. It measures current bibliography labels, not independently adjudicated truth. The assertion `obs == {22,5}` then hardcodes the expected answer on top of that circular source.
7. **Discharge:** no predicate examines Duho's instruction, its timing, or whether prior work meets the intended reading standard.
8. **Read completeness:** no source is opened for a full-read check; no verdict language such as “read in full” is required.

### Additional structural weaknesses

- The bibliography block parser assumes unique numbered headings before `## Ranked:` and silently overwrites duplicates.
- The coverage proof counts papers, not gate agreement or correctness; that is acceptable for a reading census but must not be described as unanimous ground truth.
- Classification changes after a batch (notably Q7's retained tiers after correcting the threshold rationale) do not invalidate the read, but parsing only today's label conceals the adjudicative history.
- The printed detail “measured over a FULL census” is prose; no predicate establishes full-read provenance.

## Required repair

1. Fully read entry 38 under the fixed B28 rule and gate the result.
2. Bind `{57}` to the explicit B32 full-read statements; do not bind `{38,57}` to B33's retrospective comment.
3. Bind every other batch to its brief and both verdicts, preferably with machine-readable entry sets and read-status fields.
4. Bind flags 6, 22, and 25 to the actual B25/B24/reading-note artifacts.
5. Require `live_flags == FROZEN_FLAGS` after validated one-to-one source mapping.
6. Report `1/2` only as the provisional **paper-tier** miss rate; report claim-level sensitivity as unmeasured.
7. After entry 38 closes, rerun the arithmetic and then report the census discharged. Prior qualifying reads may count regardless of whether they predate the order.

The closer is one paper short. Its arithmetic did not discover that because the hand-declared set already contained the answer it was supposed to prove.
