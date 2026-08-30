BYLINE_NARROWED_ANNOTATION_TAUTOLOGY_AND_SURNAME_CONTAINMENT

# B40 adversarial verdict — corpus byline sweep

The substantive cleanup is successful: I found no additional recorded-byline error among the 39 mapped readable entries, entry 44's bibliography record is correct while its ar5iv text extraction is defective, and entries 9/11/12 were false positives caused by the first normalizer. But “39 of 39 source-own bylines match” is too strong. Entry 44 passes only because a repository annotation injects the expected names into the searched window, and the predicate checks one-way normalized surname containment—not full authorship identity.

I reran `b40_byline_sweep.py` unchanged. It reports 39 mapped files, zero missing files, 39 matches, zero candidates, and `2/2` self-checks.

## 1. Entry 44 — correct record, defective extraction

The claim is confirmed, with the stated honesty caveat strengthened into a measurement qualification.

Below the newly added `[EXTRACTION DEFECT ...]` line, `1309.1487_clean.txt` begins:

> Out of the White Hole: A Holographic Origin for the Big Bang
>
> and Robert B. Mann

Neither `Pourhasan` nor `Afshordi` appears anywhere in that underlying extracted body. The only occurrences in the current file are in the added first-line annotation. The git diff confirms that this header is the sole change to the pin.

Independent primary metadata for arXiv `1309.1487` names **Razieh Pourhasan, Niayesh Afshordi, and Robert B. Mann**, matching bibliography entry 44. The title and JCAP identity also agree. Therefore:

- the bibliography record is right;
- the ar5iv-derived text dropped the first two authors;
- the body remains usable for the physics already audited, but its extracted byline is not complete; and
- the annotation documents the defect but cannot simultaneously serve as independent evidence that the extraction contains the correct byline.

This means entry 44 is **resolved by external primary metadata**, not passed by the source-body surname test. The headline should read “38 source-body matches plus one independently resolved defective extraction,” rather than “39 source-own bylines match.” A cleaner implementation would make entry 44 an explicit expected exception, search below the annotation boundary, and separately assert that the body is missing the two names while a pinned metadata receipt supplies them.

## 2. Entries 9, 11, and 12 — normalizer false positives

Confirmed.

Python's NFD normalization leaves `ł` as the undecomposed code point `U+0142` (`LATIN SMALL LETTER L WITH STROKE`); it does not produce `l` plus a combining mark. The original approach of discarding non-`[a-z]` characters therefore converted normalized `Popławski` to `popawski`, while the source heads use ASCII `Poplawski`.

The explicit translation `ł -> l` before NFD correctly fixes this case. Direct checks show:

- entry 9 record: `N. J. Popławski`; source: `Nikodem J. Poplawski`;
- entry 11 record: `N. J. Popławski`; source: `Nikodem Poplawski`;
- entry 12 record: `N. Popławski`; source: `Nikodem Poplawski`.

All three records are correct at the bibliography's abbreviated-name resolution. The new mappings for `đ` and `ø` are sensible defensive additions, though these three flags establish only the `ł` defect.

## 3. Four independent byline spot-checks

I chose records that exercise different source formats and include the formerly wrong control.

### Entry 5

Bibliography: `S. Khakshournia`.

Pinned paper title page: `S. Khakshournia`, with the NSTRI affiliation. Match.

### Entry 20

Bibliography: `K. A. Bronnikov, V. N. Melnikov & H. Dehnen`.

Pinned source byline: `K.A. Bronnikov`, `V.N. Melnikov`, and `Heinz Dehnen`. Match. `J. C. Fabris`, the former erroneous coauthor, is not in the byline; the correction is real.

### Entry 31

Bibliography: `L. Smolin`.

Pinned Physica A first page: `Lee Smolin`. Match.

### Entry 49

Bibliography: `S. K. Blau, E. I. Guendelman & A. H. Guth`.

Pinned PRD first page: `Steven K. Blau`, `E. I. Guendelman`, and `Alan H. Guth`. Match.

These checks found no new error.

### Defect classes the sweep cannot catch

The script does not establish full authorship identity. In particular it can miss:

- the right surname attached to the wrong person, given name, or initials;
- incorrect author order;
- an omitted author, because it tests only recorded-name `->` source-head containment;
- incomplete `et al.` expansions, because unnamed authors are never enumerated;
- duplicate authors;
- a surname found somewhere in the 1,600-character window but not actually in the byline;
- substring collisions, because matching uses `norm(surname) in norm(head)` rather than token equality;
- an annotation or provenance note that repeats the expected surname, as entry 44 demonstrates;
- a wrong source whose head happens to contain the same surnames; and
- bibliography entries outside the manually hardcoded `SRC` map.

Accordingly, B40 is a useful missing-recorded-surname screen plus hand-audited spot check, not a corpus-wide proof of exact person-level byline equality.

## 4. Predicate audit

### Corpus selection

`SRC` is a hardcoded 39-entry map. The run verifies that all 39 paths exist, but it does not derive the readable set from the bibliography or a frozen source map and does not prove that the map is complete. The current census history supports 39 readable BHU entries, so I found no omitted readable entry; nevertheless that completeness lives in external recordkeeping, not in this script.

### Bibliography parsing

The parser cuts the document at `## Ranked:` and collects numbered bold headings. That is adequate for the current layout, but `bl[n]` assumes unique entry numbers before that cut and would silently take the last duplicate if one arose. It does not assert that every `SRC` key resolves to exactly one heading.

### Surname extraction

The regex extracts capitalized surname-like words from the heading prefix before the year and removes a hand-built noise list. It does not parse authors structurally. Initials, particles, group authors, suffixes, lowercase name particles, hyphenation, and `et al.` are not comprehensively modeled. The explicit diacritic fix resolves the observed Popławski failure but is not a general transliteration scheme (`ð`, `þ`, `æ`, `œ`, and other nondecomposing letters remain untreated).

### Head search

For text files the code reads the first 2,400 raw characters, collapses whitespace, and truncates to 1,600; for PDFs it searches only page one. This is a reasonable high-recall heuristic for ordinary paper layouts. It is not byline-aware: title, annotations, affiliations, abstract, or other front matter all count equally.

### Direction of comparison

The predicate asks whether every surname explicitly extracted from the **record** occurs somewhere in the source head. It never checks the reverse direction. It can therefore catch an added wrong recorded author such as old entry 20, but cannot catch missing recorded coauthors. The script's docstring claim that it checks whether “recorded authorship match[es]” should be narrowed to “whether every explicitly recorded surname occurs in the source-head window.”

### Self-check 1 is false as described

The predicate labeled:

> the sweep separates the corpus rather than flagging everything or nothing

is

`0 <= len(flags) < 10 and ok > 25`.

It explicitly permits `len(flags) == 0`, which is the present result. Thus it does **not** prove that the sweep separates anything or avoids flagging nothing. It proves only that fewer than ten candidates appeared and more than 25 entries matched. Rename it accordingly or require a seeded negative control if separation is the intended property.

### Control 2 is post-correction only

The entry-20 predicate proves that the corrected record passes. The assertion that the old Fabris record “would have flagged” is plausible and manually confirmed from the source, but the script does not actually run a seeded old-record negative control. A robust regression test would feed the former heading and require `Fabris` to be reported missing.

### Entry 44 contaminates the result

Because `head_of()` reads from byte zero, the annotation is inside the test window. The entry passes for exactly the reason the test is meant to validate. This is disclosed honestly, but disclosure does not restore independence. The code should either skip bracketed repository annotations or handle entry 44 through an explicit exception/metadata receipt.

## Required correction

Retain all current bibliography bylines; I found no further record change. Report the result as:

> The 39-entry readable-source map was swept. Thirty-eight recorded surname sets occur in their pinned source bodies. Entry 44's extraction lacks Pourhasan and Afshordi; independent arXiv/publication metadata confirms that the bibliography is correct, and the defect is annotated. Four person-level spot checks, including corrected entry 20, found no mismatch. This is one-way surname-containment coverage, not exact full-byline verification.

Then:

1. exclude annotations from entry 44's searched body and make its expected extraction failure a regression check;
2. seed the old entry-20/Fabris heading as a required negative control;
3. derive or cross-check `SRC` against the canonical readable source map;
4. rename the first self-check to describe what its predicate actually tests; and
5. if exact authorship is the goal, compare structured full author lists—including given names/initials and order—against primary metadata, with explicit handling for `et al.`.

The sweep is useful and its substantive “no new mismatch found” result survives. Its evidentiary label and `39/39` interpretation require narrowing.
