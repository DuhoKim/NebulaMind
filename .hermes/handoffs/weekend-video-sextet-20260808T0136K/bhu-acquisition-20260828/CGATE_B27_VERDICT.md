READABILITY_REFUTED_FALSE_ABSENCE_AND_FALSE_POSITIVE

# B27 adversarial verdict

B27 fails in both directions. It calls **entry 41 not located even though its full text is pinned and explicitly indexed**, because the arXiv and published titles differ. It simultaneously calls **entry 1 readable by matching entry 1's short title inside entry 5's different paper**. The headline 34/17 split survives only by cancellation of these two errors; the claimed membership lists and the method do not.

## Attack 1 — independent search of the not-located list

I searched the handoff repository independently for all 17 candidates using the bibliography DOI, title, author surnames, stated arXiv identifier where available, alternate-title clues, filenames, text/HTML headers, and first-page PDF text. Citation-only hits were rejected.

### Decisive false absence: entry 41

Entry 41 is present at:

```text
bhu-reading-20260823/sources/2007.11556_clean.txt
bhu-reading-20260823/sources/ar5iv_2007.11556.html
```

The clean text begins with arXiv identifier `2007.11556`, author Nikodem Popławski, and the title:

> The universe as a closed anisotropic universe born in a black hole

Its abstract describes the Kantowski–Sachs anisotropic black-hole universe, torsion, particle production, bounce, inflation, and isotropization. This is entry 41's paper. `ENTRY_SOURCE_MAP.md` independently maps `2007.11556_clean.txt` to entry 41, and the bibliography says entry 41 was read on 2026-08-23.

B27 searches only the bibliography's later published title:

> A nonsingular, anisotropic universe in a black hole with torsion and particle production

The first 44 normalized characters do not occur in the arXiv title, so B27 produces exactly the alternate/preprint-title false negative its own limitations section names. Its two positive controls do nothing about this known title-changing paper.

Entry 41 must be removed from the not-located list. This alone refutes claim 2 and the asserted source inventory.

### Other 16 candidates

For entries 2, 3, 4, 13–20, 28, 42, 47, 48, and 50, my identifier/author/title/header searches found no verified copy of the paper itself. The repository contains many citations to these papers—especially in Gaztañaga, Easson, and related source texts—but a citation is not possession. Examples I rejected include DOI/title hits for Stuckey, Frolov–Markov–Mukhanov, Easson–Brandenberger, Bronnikov–Fabris, Sato et al., and Farhi–Guth in reference lists of other papers.

This is a repo-search result, not proof of global unavailability. It also does not rule out another locally held alternate-title or OCR-mangled file. The corrected candidate not-located set supported by this pass is therefore:

```text
2, 3, 4, 13, 14, 15, 16, 17, 18, 19, 20, 28, 42, 47, 48, 50
```

That is 16 candidates, subject to further identity checking.

## Attack 2 — false positive in the readable list

B27's own selected-hit mapping reveals:

```text
entry 1 -> reviews/.../arxiv-1412.0105v1.pdf
entry 5 -> reviews/.../arxiv-1412.0105v1.pdf
```

That PDF is **entry 5**, Khakshournia's *“A note on Pathria's model of the universe as a black hole.”* It is not entry 1, Pathria's *“The Universe as a Black Hole.”* Entry 1's normalized title key, `theuniverseasablackhole`, appears as a substring inside entry 5's longer title, so the 44-character rule cannot help: entry 1's entire normalized title is only 23 characters.

This is the exact “document about the paper rather than being it” false positive requested by the attack. Entry 5 discusses and cites Pathria and includes Pathria's title phrase in its own title; it is still a different paper by a different author, four decades later. The bibliography and map correction already say Pathria's full text remains unobtained.

Entry 1 must be removed from the readable list. After removing false-positive entry 1 and adding false-negative entry 41, the arithmetic happens to remain **34 readable / 17 candidate-not-located**. That numerical cancellation does not confirm the headline. A source inventory is about identities, not merely a total, and the same method may contain further compensating errors.

The remaining 33 readable matches I spot-checked are, in contrast, plausibly the paper itself: their chosen files carry the matching paper's header/title and expected authors or identifiers. I found no second concrete false positive, but I did not manually authenticate every page of all 33.

## Attack 3 — the head and length rules are not defensible as a binary readability test

### The 8,000-character threshold is not what the PDF code measures

For text files, B27 uses actual raw character count. For PDFs, it sets:

```python
n = d.page_count * 4000
```

This is an invented page-count proxy, not extracted character count. Consequently:

- every two-page PDF automatically “passes 8,000 characters,” regardless of how little readable text it contains;
- every one-page paper automatically fails, regardless of whether its complete text is perfectly readable;
- an image-heavy or scanned multi-page PDF can pass the length proxy after one extractable title page even if its body is not machine-readable.

This matters concretely because entry 2 is a one-page Physics Today note. A genuine complete local copy could be rejected solely for being short. Readability must mean possession of the complete work appropriate to its form, not exceeding an arbitrary length.

### Head-only matching is useful but insufficient

Checking the header/page 1 is a sound defense against reference-list false positives. It should remain one signal. It fails when:

- arXiv and journal titles differ, as entry 41 proves;
- a cover sheet, repository wrapper, OCR damage, translation, or two-column extraction alters the title;
- a short generic title is contained inside another paper's title, as entries 1 and 5 prove.

Removing all spaces helps split-word extraction but increases substring collisions. Truncating long titles to 44 normalized characters also discards potentially discriminating suffixes.

A defensible identity check should combine at least two independent header attributes: exact/fuzzy full title or known alternate title **plus** author, DOI/arXiv identifier, venue/year, or a curated mapping. It should resolve the selected path and check body completeness. Short papers need format-aware completeness rules rather than a global character floor.

## Attack 4 — the near-miss list is not recall evidence

The near-miss rule (`imp>=3`, `dom>=1`, `ref>=1`) is an arbitrary second rectangle around B1's arbitrary first rectangle. A paper can be “near” in counts while its matched phrases occur in unrelated contexts; B1's known false positives already demonstrate that aggregate vocabulary counts do not identify a proof.

Entries 23, 26, and 27 are all from Gaztañaga's linked BHU series. Their clustering is therefore not three independent signals. It is expected lexical correlation from shared author, framework, references, and argumentative vocabulary. It may be useful for a **failure-mode stress test** of this regex, but it says nothing quantitative about corpus recall.

Entry 55's `7,1,1` and entries 23/27's `3,4,2`/`3,4,8` also illustrate that “distance to threshold” has no calibrated meaning: the missing dimensions and surplus counts are not commensurable, and none tests semantic co-location of impossibility, domain, and escape.

I would not prioritize these four as the primary recall audit. Doing so would repeat the selection bias already identified: choosing papers the screen nearly liked tests a hand-picked boundary, not misses among all unflagged papers. The correct sequence is:

1. preregister and draw a blinded random sample from the authenticated unflagged-readable population;
2. classify it by hand under the paper-level obstruction rule;
3. only then run a separately labeled purposive near-threshold stress sample if resources permit.

The purposive sample can diagnose lexical boundary behavior; only the random sample supports an estimate of miss prevalence.

## Predicate audit

B27's `4/4` does not validate its inventory or recall framing.

1. **Usable-key check:** `len(keys) >= len(E)-3` tests quantity, not uniqueness or discriminative power. All 51 keys can exist while entry 1's key matches entry 5 and entry 41's key misses its alternate title.
2. **Positive controls:** finding entries 5 and 56 proves those two exact-title cases are reachable. It does not test alternate-title recall, false-positive identity, short-paper handling, or completeness. Entry 41 fails alongside the passing controls.
3. **Difference-from-18 check:** `len(missing) != 18` rewards disagreement with a known-bad old number, not correctness. Any result other than 18 passes—even zero or 51. It does not validate a single missing identity.
4. **Recall-probe check:** `0 < len(flag) < len(scored)` proves only that the screen is nonconstant on the selected files. It does not make the near-miss threshold meaningful, validate any near miss as an obstruction, measure recall, or support the quoted audit costs.

Additional untested defects:

- PDF “length” is fabricated from page count;
- the script chooses the largest matching document, not the strongest identity match;
- it permits one document to satisfy multiple entries without an ambiguity check;
- it has no uniqueness predicate over selected paths—exactly why entries 1 and 5 silently share one PDF;
- it does not compare against known alternate titles or the existing source map as a reconciliation control.

## Required correction

Do not publish the present membership lists. At minimum:

- map entry 41 to `2007.11556_clean.txt` and record both titles;
- mark entry 1 not located and reject entry 5's PDF as its match;
- add a one-path-to-multiple-entries collision check;
- replace `page_count * 4000` with actual extractability/completeness checks;
- match title together with author or identifier and maintain alternate-title aliases;
- keep near-threshold review separate from a blinded random recall audit.

The coincidentally unchanged 34/17 total may be retained only as **provisional after manual identity correction**, not as confirmation of B27's algorithm or its printed lists.
