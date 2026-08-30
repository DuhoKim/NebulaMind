SCAN_AND_CUSTODY_NARROWED_ENTRY32_STALE_FULLTEXT_AND_TEXTLAYER

# B42V2/B44 adversarial verdict

The entry-32 scan is authentic, its visually reported identity and numerical claims are correct, and B44's present custody result is confirmed: all nine repaired PDFs are in commit `920d998d5`, every currently enumerated cited artifact exists and is tracked, and no basename collision exists today. The round needs a narrow record correction, however. Entry 32 still ends with **“Full text not held — cited and Crossref-verified only”** immediately after recording a complete six-page scan of the six-page article. That is stale and false. The scan also contains a minimal extractable ADS-bibcode layer, so “no text layer” is literally too broad; the accurate statement is “no extractable article-content/OCR text layer.”

I rendered page 1 independently with PyMuPDF at 120 dpi, visually inspected it, checked all six pages, recomputed the hash, ran both scripts unchanged (`b42`: 4/4; `b44`: 2/2), enumerated every current citation basename and filesystem hit independently, and checked the nine paths directly against commit `920d998d5` and the current Git index.

## 1. Entry 32 scan and visual reading

The pinned file is:

`bhu-theory-phase3-cns-20260821/sources/ads_1994ApJ_423_659_brown_bethe.pdf`

Independent file checks give:

- SHA-256 `4b1cbae677def63c02b261c4befe21aa561cccb4ae6d396f4bc04c966ce8ac69`;
- six PDF pages;
- page span 659–664, matching a complete six-page ApJ article; and
- the expected PDF magic.

The rendered first page clearly shows:

- `THE ASTROPHYSICAL JOURNAL, 423:659–664, 1994 March 10`;
- the full title, `A SCENARIO FOR A LARGE NUMBER OF LOW-MASS BLACK HOLES IN THE GALAXY`;
- the byline `G. E. BROWN` and `H. A. BETHE`; and
- the abstract's quantitative claims: black-hole masses only slightly above `1.5 M_sun`, kaon-condensation stabilization to approximately `1.84 M_sun`, and `M_cutoff = 25 ± 5 M_sun`.

The submitted visual testimony is therefore confirmed. The bibliography's author names, title, journal, volume, initial page, date, scan length, hash prefix, and numerical synopsis are faithful to the scan.

## 2. SCAN handling and predicate honesty

`b42_support_byline_sweep.py` does not pretend to machine-read Brown or Bethe from the page image. Its SCAN predicate computes only:

- pin existence by opening the named path;
- PDF magic;
- the expected hash prefix; and
- presence in the bibliography of the filename and the disclosure `byline checks are VISUAL`.

The docstring and printed output explicitly identify the byline as recorded visual testimony. That is honest predicate scoping.

There is one terminological overstatement. PyMuPDF extracts exactly this 20-character string from every page:

`1994ApJ...423..659B`

Thus the PDF does possess a tiny text layer containing the ADS bibcode. It has no extractable title, byline, abstract, or body text, so surname containment and article-content checking remain impossible. Replace “NO text layer” / “no text layer” with **“no article-content or OCR text layer; only an ADS-bibcode overlay is extractable.”** This does not undermine the visual ruling or the SCAN design.

The `MEASURED` check's `none_entries == []` also does not mean entry 32 became a text-backed entry; the printed class remains SCAN and the measured surname count is expressly limited to the other six text-artifact-backed support entries.

## 3. Entry-32 bibliography repair

The new acquisition paragraph is internally inconsistent. It first records:

> Pinned 2026-08-30: the NASA ADS page scan ... 6 pp

and then ends:

> **Full text not held** — cited and Crossref-verified only.

The article is ApJ 423, 659–664, and the pin contains all six pages 659 through 664. The complete article is held as an image scan. “Crossref-verified only” is likewise obsolete because the primary scan was visually checked.

Required correction:

> **Full article held as a six-page image scan; no extractable article-content/OCR text layer, so title, byline, and abstract checks are visual.**

This is a record-fidelity defect, not an identity or custody failure.

## 4. Nine-pin commit custody

Commit `920d998d56bc4e822bc98d22c1bb8e60c803e20e` contains all nine stated additions:

1. `1309.1487.pdf`;
2. `blau_guendelman_guth_1987_prd35_1747.pdf`;
3. `rothman_ellis_1993_qjras34.pdf`;
4. `rothman_ellis_1993_qjras34_201.pdf`;
5. `smolin_1992_did_the_universe_evolve_cqg9_173.pdf`;
6. `smolin_2004_cns_physica_a340.pdf`;
7. `smoller_temple_1997_oppenheimer_snyder_arma138_cv47.pdf`;
8. `smoller_temple_2000_shockwave_astroph9812063.pdf`; and
9. `ads_1994ApJ_423_659_brown_bethe.pdf`.

All nine are also tracked in the current index. The claim that the ignored-PDF custody hole was closed for these known pins is confirmed.

## 5. B44 enumeration audit

The two routes operate as described:

1. the bibliography sweep extracts basenames from backticked paths ending in `pdf`, `txt`, `html`, `json`, or `tex`, excluding glob expressions;
2. `1309.1487.pdf`, which is cited in prose rather than in the captured backticked form, is added through `KNOWN_UNBACKTICKED`.

The resulting current set has 17 unique basenames. My independent enumeration found:

- 17 tracked;
- zero missing on disk;
- zero on-disk-but-untracked; and
- **zero basename collisions**.

Therefore the permissive collision rule hides nothing today. Each of the 17 basenames resolves to exactly one file in the searched handoff tree.

The admitted missed class is real: prose may cite an artifact without supplying any filename, which neither route can enumerate. B44 does not claim to close that semantic discovery problem and names reading notes as the fallback. Two non-backticked external `.pdf` URL strings currently visible in the bibliography point to Smolin 2004 and Smoller–Temple 1997; both corresponding local pins are separately named in backticks and are included in the 17, so they create no present custody miss.

Minor hardening points do not change the current result:

- basename-only matching could accept the wrong tracked copy if a future collision appears;
- the walker skips paths whose string contains `venv` or `node_modules`, so “anywhere” is slightly broader than the literal implementation; and
- the predicate establishes current Git tracking, while direct `ls-tree` inspection is what establishes membership in the named historical commit.

## Final ruling

- **Entry-32 identity and visual numerical reading:** confirmed.
- **B42 SCAN predicate honesty:** confirmed, with “no text layer” narrowed to “no article-content/OCR text layer.”
- **Entry-32 record edit:** narrowed because “Full text not held — cited and Crossref-verified only” is stale and false.
- **Nine PDFs in commit `920d998d5`:** confirmed.
- **B44 current custody, both enumeration routes, and no present collision:** confirmed.

Correct the two entry-32 phrases; no reacquisition or custody repair is required.
