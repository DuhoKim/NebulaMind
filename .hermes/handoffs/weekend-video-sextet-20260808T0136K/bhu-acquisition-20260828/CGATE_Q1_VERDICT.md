Q1_ANSWER_REFUTED_UNMEASURED_RECALL_CANNOT_LICENSE_SCREEN

# Q1 adversarial verdict

The operational answer is not established. “Screen, then hand-check every flag” prevents **accepted false positives** only if the hand review is accurate; it neither detects false negatives nor becomes “safe at any accuracy.” Precision/flag rate still determines whether the review queue is affordable, and recall can be measured—imperfectly but directly—by auditing unflagged papers. The source count is also wrong: at least two papers in the claimed 18-unpinned set already have full text in the repository.

## 1. The 18-unpinned count is false

I reran `b26_answer_q1.py`; it prints 51 BHU papers, 33 mapped, and 18 unmapped. That is a property of its parser and `ENTRY_SOURCE_MAP.md`, not a verified filesystem finding.

Two concrete false absences are enough to refute the count:

- **Entry 5, Khakshournia 2010**, is in the alleged unpinned list. A complete five-page paper is present at `reviews/bhu-citation-custody-evidence-20260811/arxiv-1412.0105v1.pdf`, with a text extraction beside it. Its first page gives the exact title, author, arXiv identifier, abstract, and body. The map never indexed it.
- **Entry 56, Gaztañaga 2023**, is also in the alleged unpinned list. The published five-page MNRAS paper is present at `bhu-reading-20260823/sources/gaztanaga_mass_mnras.pdf`. `pdfinfo` identifies the title and DOI `10.1093/mnrasl/slad015`; extracted text contains the complete article. The bibliography itself says entry 56 was read from this published PDF, and `READING_NOTES_01.md` has an entry-56 reading note. The map mentions this file only as an example of a failed DOI-search method and never adds its entry mapping.

Therefore the evidenced state is **at least 35 readable and at most 16 presently unlocated**, not 33/18. I did not establish that all remaining 16 are absent everywhere; a robust repo-wide identity audit would be required for an exact count.

The parser has weaknesses in both directions:

- it treats a backticked `.txt` or `.pdf` string in a map row as source possession without resolving the path, checking existence, checking full-text completeness, or verifying document identity;
- it cannot find real files that the map omitted, as entries 5 and 56 demonstrate;
- it relies on a map whose own narrative contains historical/stale counts and corrected identities.

The acquisition observation is still useful: some corpus papers remain unreadable until acquired. It is not “the finding” that decides whether to screen the readable set, and its advertised exact count is not gated by B26.

## 2. “A verified screen is safe at any precision” is false

The argument conflates three different quantities:

1. **precision**: how many flags are real obstructions;
2. **flag rate/review load**: how many papers must be hand-read;
3. **recall**: how many real obstructions the screen flags at all.

Hand-checking every flag can stop a regex false positive from being filed, subject to reviewer error. It cannot stop a false negative from remaining silently in its old tier. Calling the workflow “safe at any accuracy” is therefore false if “accuracy” includes recall, and misleading even if it means precision alone.

Precision is not beside the point operationally. Let `N` be readable papers, `F` flags, `c` the cost of a sufficiently reliable hand adjudication, and `s` the per-paper screening overhead. Then:

```text
screen + verify cost = sN + cF
hand-sort cost       = cN
```

Screening saves effort only when `sN < c(N-F)`. Precision affects cost indirectly through false-positive flags; the direct variable is `F/N`. B26 measures neither `s` nor `c` and supplies no fatigue/error model.

At the current three flags, manual verification is plausibly cheap. But the brief's stress test breaks the universal claim:

- If 30 of 33 readable papers flag, one-reader verification costs about 30 paper reads versus 33 for hand sorting, before screen overhead—a saving of only three reads.
- If the tier's original two-independent-reviewer standard applies, the comparison is roughly 60 versus 66 reviewer-reads, again before overhead.
- A flood of low-quality flags also increases fatigue and correlated adjudication errors. “Every flag is checked” is a procedure, not a guarantee that every check is correct.
- At `F=N`, screening saves no reading at all and adds overhead.

Thus “safe at any precision” and “precision determines only wasted reading” are too clever. Wasted reading is the very cost Q1 asks Duho to trade against completeness. The current `3/35`-or-similar flag load may be affordable, but that is a small-current-queue fact, not a precision-independent theorem or a basis for future use without a stop rule.

A defensible option B needs an operational guardrail, for example: use the screen only while `F/N` stays below a declared review-budget threshold, require independent adjudication for proposed obstruction moves, and fall back to sampling/hand sorting when flag volume or disagreement exceeds it. B26 states none.

## 3. Recall can be measured; it is merely unmeasured now

“Recall is 1 of 1 at n=1, which is not a measurement” correctly rejects a meaningful positive-control estimate. “It cannot be measured here” is wrong.

The direct design is straightforward:

1. define the readable corpus and freeze the B1 output;
2. randomly sample from the **unflagged** papers, without allowing acquisition history or perceived promise to choose the sample;
3. have reviewers blinded to screen status apply the paper-level obstruction definition;
4. count missed obstructions and report the finite-population uncertainty;
5. optionally continue adaptively or census all unflagged papers if the required bound is tight.

This estimates the false-negative prevalence among unflagged papers. Combined with adjudicated flags, it estimates recall. It also tests exactly what B26 says matters.

The qualification is statistical power, not impossibility. With 30 unflagged papers:

- auditing 10 and finding zero misses still has a 66.7% chance of missing a single hidden obstruction and a 28.1% chance of missing all three if three are hidden;
- to have at least 95% probability of encountering one when 6/30 (20%) are hidden requires 11 random reads;
- for 3/30 (10%), it requires 19;
- for one hidden obstruction, it requires 29—almost a census.

So a cheap sample can expose a gross recall failure, while a strong guarantee against rare misses costs nearly full hand sorting. That is precisely the cost–completeness curve Duho's question asks about. B26 erases the available middle ground by converting “not yet measured and costly to bound tightly” into “cannot be measured.”

Other usable evidence includes leave-one-out tests on independently established obstruction papers, seeded/synthetic paraphrase tests for lexical robustness, and a genuinely independent second screen. None replaces a random unflagged audit, but all are more informative than treating one positive control as the only possible recall evidence.

Most importantly, **absence of evidence that recall is bad is not evidence that recall is acceptable**. The original option B explicitly accepts silent misses. Tori cannot authorize that completeness loss merely because it has not been measured; that was the reason the question was escalated to Duho in the first place.

## 4. The three current flagged papers and tier movement

The narrow historical claim largely checks out:

- **Entry 22** has pinned full text, B24's source/domain audit, two gate verdicts, and is currently `THEORETICAL-OBSTRUCTION`.
- **Entry 25** has pinned full text, `a6_entry25_falsifier.py`, both A6 gate verdicts, and remains `QUALITATIVE-DIRECTIONAL`.
- **Entry 6** has the pinned IOP paper, bibliography reading provenance, and remains `QUALITATIVE-DIRECTIONAL`.

Thus all three currently identified corpus flags have been read and the two false positives were not moved. Entry 22 **did move earlier** from `CONSISTENCY-ONLY` to the newly authorized obstruction tier; the defensible Q1 statement is that applying this latest screen-and-check pass caused no additional tier move, not the context-free “no tier moved.”

“Already done” is also too broad. Positive adjudication of the three current flags is done. A re-sort is not complete until the unflagged set has either been audited enough to satisfy a stated miss tolerance or Duho explicitly accepts the unknown miss risk. New acquisitions—including the already missed entries 5 and 56—must also be normalized into screenable text and run through the criterion if option B is adopted.

## 5. Reframing around acquisition

The acquisition reframe is legitimate as an additional queue-management finding: neither a person nor this text screen can classify unavailable full text. It is an evasion when used to make the screen-versus-hand choice disappear for the readable majority. Q1 still has two independent workstreams:

```text
unavailable papers  -> acquire and verify identity/completeness
readable papers     -> choose a recall-assurance policy
```

Acquisition does not answer how much silent-miss risk to accept on readable papers. Conversely, choosing a classification workflow does not remove the acquisition queue. Both should be stated; neither subsumes the other.

## 6. Predicate audit of `b26_answer_q1.py`

B26's `2/2` is not evidence for its main answer.

### Check 1

The predicate is only `len(lack) >= 15`. It does not test:

- the printed exact count 18;
- filesystem absence of any listed source;
- path existence or document identity for mapped sources;
- that acquisition is the dominant bottleneck;
- that the Q1 choice is malformed.

It would still pass after the two demonstrated corrections and even if several more “missing” sources were found. Its detail presents untested claims as measured findings.

### Check 2

The predicate is only that the bibliography blocks for entries 22, 25, and 6 contain the literal `Testability: **`. Every classified bibliography entry is expected to contain that marker. It does not test:

- that the source files exist or were read;
- that A6/B24 audits and gate verdicts exist;
- that the screen actually flags these three on the current corpus;
- that the labels are correct;
- that no tier moved;
- that the screen-and-check pass is complete.

The check would pass if all three had never been opened or if B1's current criterion flagged a different set. This is a severe predicate/name mismatch.

### Entirely untested answer claims

No predicate measures review cost, screen overhead, reviewer fatigue/error, recall, random-audit feasibility, the 30-paper saving, or safety “at any accuracy.” The two checks validate bookkeeping fragments while the decision rests entirely in prose.

## Required correction

Q1 should not be closed with an unconditional option-B answer. The defensible disposition is:

> At least 35 papers are currently readable; the map must be repaired before stating an exact acquisition queue. The current three screen flags have been hand-adjudicated without a new misfiling. Recall on the unflagged set is unknown but measurable. Before using the screen as the sole shortlist, choose and execute a blinded random-audit/census plan—or explicitly accept the residual miss risk—and set a flag-volume threshold beyond which hand sorting is no more expensive.

That preserves the useful triage idea without pretending positive verification solves recall or that recall cannot be investigated.
