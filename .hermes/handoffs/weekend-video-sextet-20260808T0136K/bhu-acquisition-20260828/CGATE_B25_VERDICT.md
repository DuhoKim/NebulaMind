PRECISION_NARROWED_CURRENT_SUBSET_ONLY

# B25 adversarial verdict

B25's headline arithmetic happens to reproduce on the current files: the actual B1 criterion flags the same six identifiers B25 hardcodes, and three of those are mapped corpus papers. Under the existing **primary-paper-tier** labels, one of those three is the accepted no-go, hence `1/3 = 0.33`. But B25 misdescribes the population, does not itself rerun or import the screen, and cannot promote this selected pinned-subset estimate into “the screen's real precision.”

## Attack 1 — independent rerun of B1's criterion

I copied B1's three regexes and thresholds, enumerated every current `*_clean.txt`, normalized whitespace exactly as B1 does, and applied:

```text
impossibility >= 5 AND domain >= 2 AND refutable/escape >= 2
```

There are 41 current clean-text files. The criterion itself flags exactly:

| file | impossibility | domain | escape |
|---|---:|---:|---:|
| `1807.06209_clean.txt` | 12 | 8 | 4 |
| `2002.12778_clean.txt` | 6 | 16 | 11 |
| `2503.14738_clean.txt` | 5 | 4 | 3 |
| `2606.25023_clean.txt` | 35 | 6 | 3 |
| `smolin_1992_clean.txt` | 8 | 29 | 3 |
| `sym14091849_clean.txt` | 5 | 4 | 2 |

Thus B25's six-name list is currently correct by coincidence/manual transcription. B1's printed “4 of 29” is stale: its live loop now emits six, while its prose and check name remain fixed at four. B25 should call the shared `score`/`is_obstruction` implementation or reproduce and compare its output, not use filename prefixes from a prior printout. A newly pinned file or criterion edit can otherwise leave all four B25 predicates green while its precision is wrong.

## Attack 2 — the denominator is not the claimed population

The claim “27 corpus entries and 14 receipts/not entries” is false. The map file itself identifies:

- entry 9 as arXiv `1007.0587`;
- entry 11 as arXiv `1410.3881`.

Current copies named `1007.0587_clean.txt` and `1410.3881_clean.txt` are present in the source directory and plainly have the corresponding paper titles. B25's parser misses them because the map's extension rows point to differently named files in another directory and its regex accepts only backticked names ending `_clean.txt`. They are corpus sources, not receipts. Therefore, within this 41-file directory, the defensible identity count is at least **29 corpus papers and at most 12 receipt/support papers**, not 27 and 14. Neither missed corpus paper is flagged, so the flagged-paper calculation remains three candidates and `1/3` under the adopted labels.

More importantly, “corpus entries only” is the right **kind** of deployment domain but these 29 are not the full deployment population. The bibliography defines 51 BHU papers; the current directory contains an acquisition-selected subset, and the source map itself describes 32 auditable entries repo-wide. A precision denominator is the number of flagged items, so absent unflagged papers do not mechanically change the fraction—but applying the screen to the 22 untested bibliography papers could produce new true or false positives and change it substantially. Acquisitions were targeted by research needs, ranked targets, measurement receipts, and later audits, not sampled to estimate classifier precision.

Accordingly:

- `1/3` is coherent as **observed precision among the three flagged, identifiable corpus papers in this current source-directory subset**;
- it is not a corpus-wide precision estimate and should not be called “the corrected figure” or “what the screen's precision actually is” without that qualifier;
- 41 all-source files, 29 identified corpus files, the map's repo-wide 32, and the bibliography's 51 are four different frames. B25 currently treats the first two as exhaustive alternatives when they are not.

## Attack 3 — direction of the restriction

For the files presently pinned, the direction is arithmetically real. The six flags split into three corpus candidates and three observational/review receipts (Planck 2018, Carr's PBH review, and DESI DR2). Removing the latter changes the conditional count from `1/6` to `1/3`, assuming one accepted true positive.

That does **not** establish that corpus restriction generally improves the screen. It establishes only that these three particular flagged receipts were false positives. Receipt acquisition is highly non-random and especially rich in long collaboration/review texts containing assumptions, hypotheses, exclusions, and “unless” language—the very tokens B1 counts. Conversely, the unpinned corpus papers have never been scored. The favourable direction may therefore be an acquisition-composition effect. It is safe to report the within-current-files comparison; it is unsafe to use its magnitude as an expected improvement on the whole bibliography.

## Attack 4 — entries 6 and 25

### Entry 6, Smolin 1992

Entry 6 is a false positive for a theoretical-obstruction **paper tier**. Reading the matched passages shows why the aggregate count fails:

- “cannot be causally influenced,” “cannot be explained,” and “cannot be determined by observation” concern unrelated local statements;
- the many domain hits are the paper's numerous speculative assumptions and hypotheses;
- the three escape hits are ordinary `unless` clauses in different arguments.

The paper proposes CNS mechanisms and candidate falsifiers. It even says whether a detailed, falsifiable mechanism can be developed “remains to be seen.” Its simplified model contradicts one hypothesis under its assumptions, but it does not prove that no member of a stated CNS/model class can satisfy a conjunction. The criterion manufactures the required triplet by pooling distant sentences.

### Entry 25, Gaztañaga 2022 Part I

Entry 25 is also a false positive **for its primary paper-level tier**: the abstract and conclusion construct and advocate a BHU solution, describe observational discriminants, and do not present the paper as a class-wide impossibility theorem. Its five impossibility hits include event-horizon inaccessibility, coordinate/metric regions that cannot be reached, and a nonlinear mass expression; the domain and escape hits likewise are not a co-located theorem/domain/evasion structure.

There is nevertheless an arguable local no-go inside entry 25 that B25 should acknowledge. The introduction says a static black-hole interior made of regular matter or radiation cannot exist because the Buchdahl radius exceeds the Schwarzschild radius. That excludes a specified subcase and has a counterexample-shaped refutation condition. If tiers were assigned to **every claim** rather than to each paper's operative contribution, entry 25 would contain obstruction material. It does not make B1's flag correct under the current primary-paper classification, and B1's actual regex matches do not demonstrate or validate that Buchdahl application. But this ambiguity means `CORRECT = 2606.25023` is a labeling assumption requiring an explicit paper-level rule, not a measured fact. Under a claim-level convention, precision could be argued as `2/3`, illustrating why B25 cannot silently hardcode ground truth.

## Predicate audit

B25 reports 4/4, but none of the four predicates validates all the prose in its name/detail:

1. `len(allsrc) > 29` proves growth only. It does not test that B1 prints six flags, that the live list differs from four, or that the added sources are relevant.
2. `len(receipts) > 0` proves only that the parser leaves something unmapped. It does not prove all 14 unmapped files are receipts or “could never be tier candidates.” Two are known corpus entries, so the accompanying count and characterization are false.
3. `prec_entries > prec_all` is correct for the hardcoded arrays and map. It does not rerun B1, validate mapping completeness, adjudicate the sole `CORRECT`, or establish a population-general direction.
4. `prec_entries < 0.5` tests only a derived hardcoded fraction. It does not establish that entries 6 and 25 are wrong classifications or that the screen is wrong more often than right beyond this selected subset.

There is also no predicate for uniqueness/coverage of mapped entry IDs, no reconciliation with the map's extension rows, and no source-text connection in the precision labels.

## Does B25 “decide nothing”?

It is honest only in the narrow constitutional sense: a precision estimate does not decide the normative tradeoff between reviewer time, false positives, and missed papers. But the file plainly supplies favourable directional evidence and says Duho “should rule on this number.” It therefore influences the live decision and must meet evidentiary standards appropriate to that role. Calling it “not an answer” cannot neutralize the hardcoded screen output, hardcoded ground truth, incomplete population, or selection bias.

## Disposition

Preserve the narrow observation:

> On the current source-directory subset, B1 flags six files. Three are identifiable corpus papers; under primary-paper labels, one is the accepted theoretical obstruction, for observed precision 1/3. This selected-subset estimate is not corpus-wide, and the screen's recall is unmeasured.

Correct B25 to rerun the criterion, recognize entries 9 and 11, separate current-subset precision from corpus precision, and state the paper-level labeling convention. The result remains evidence against unattended classification, but it is not a reliable standalone number on which to choose hand sorting versus screening.
