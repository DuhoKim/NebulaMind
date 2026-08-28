# Entry -> pinned-source map (Step 0)

Built 2026-08-28 by script, not by seat. 12 auto-matched on title at score 1.00;
8 resolved by reading each file's own title. One file is NOT a bibliography entry.

| entry | tier | pinned file | sha256 (12) |
|---|---|---|---|
| 1 | CONSISTENCY-ONLY | `1111.1017_clean.txt` | `c9780a259194` |
| 6 | QUALITATIVE-DIRECTIONAL | `smolin_1992_clean.txt` | `3da9aaab5f80` |
| 31 | CALIBRATED-FALSIFIER | `smolin_2004_cns_clean.txt` | `b051f707ca42` |
| 36 | CONSISTENCY-ONLY | `smoller_temple_2000_clean.txt` | `13d07d24a6d4` |
| 37 | CONSISTENCY-ONLY | `0210105_clean.txt` | `82fd83229be2` |
| 38 | CONSISTENCY-ONLY | `math-ph_0302036_clean.txt` | `47c47ac44788` |
| 39 | CONSISTENCY-ONLY | `1105.6127_clean.txt` | `5289e4b7dde3` |
| 40 | CONSISTENCY-ONLY | `2008.02136_clean.txt` | `30adcbcfee01` |
| 41 | CONSISTENCY-ONLY | `2007.11556_clean.txt` | `d94c72e4e4db` |
| 43 | CONSISTENCY-ONLY | `2304.12018_clean.txt` | `589bfda50476` |
| 44 | QUALITATIVE-DIRECTIONAL | `1309.1487_clean.txt` | `e8e1f1071636` |
| 45 | CONSISTENCY-ONLY | `2210.15186_clean.txt` | `2765b415a4f8` |
| 49 | CONSISTENCY-ONLY | `blau_guendelman_guth_1987_clean.txt` | `f25a944c12de` |
| 51 | QUALITATIVE-DIRECTIONAL | `0910.1181_clean.txt` | `9a2359a10141` |
| 52 | CONSISTENCY-ONLY | `1808.08327_clean.txt` | `b8c9ca327683` |
| 53 | CONSISTENCY-ONLY | `1906.11824_clean.txt` | `a02d0cff45e3` |
| 54 | QUALITATIVE-DIRECTIONAL | `2505.23877_clean.txt` | `5b56ab59eb51` |
| 55 | CONSISTENCY-ONLY | `2007.06664_clean.txt` | `b34183bf58eb` |
| 57 | CONSISTENCY-ONLY | `smoller_temple_1997_clean.txt` | `37d2869df53e` |
| — | (not an entry) | `2512.09486_clean.txt` | `37f097db4a78` |

**Entries with pinned full text: 19** — [1, 6, 31, 36, 37, 38, 39, 40, 41, 43, 44, 45, 49, 51, 52, 53, 54, 55, 57]

`2512.09486_clean.txt` is the DESI wCDM curvature paper pulled for phase 6 C2/C4; it is
reference material, not a BHU bibliography entry.

## The gap this fixes

The bibliography records DOIs, not arXiv IDs, so no string search links an entry to its
own pinned text — entry 54's record never contains `2505.23877`. This map is the missing
join. It should be maintained alongside the bibliography, or the next sweep rebuilds it.


---

## EXTENSION 2026-08-29 — repo-wide sweep, +5 entries

The original map covered only `bhu-reading-20260823/sources/`. Sweeping the whole repo found
five more entries whose full text was already on disk, in three different directories:

| entry | pinned file | sha256 (12) |
|---|---|---|
| 7 | `../brown-prl.txt` | `648812d88b6a` |
| 9 | `../bhu-podcasts-20260820/arxiv_1007.0587.txt` | `16b8cae74b44` |
| 10 | `../bhu-podcasts-20260820/arxiv_1111.4595.txt` | `752f2f8f55e5` |
| 11 | `../bhu-podcasts-20260820/arxiv_1410.3881.txt` | `71a27bfab91f` |
| 12 | `../reviews/bhu-citation-custody-evidence-20260811/arxiv-2509.11468v2.txt` | `8297f879829f` |

**Auditable corpus: 19 -> 24 of 51 classified entries.** Three of the five sat in
`bhu-podcasts-20260820/` — a directory nobody would search for paper sources. Entry 7's text
(`brown-prl.txt`) was in the handoff root; I had found it by hand during the entry-7 audit and it
was never indexed here.

### Method note — the first attempt produced 27 false positives

Searching for each entry's **DOI anywhere in a file** returned 27 "hits" and every one worth
checking was wrong. Eleven pointed at the same file, `gaztanaga_mass_mnras.pdf`, because its
REFERENCE LIST contains those DOIs. Others matched our own audit notes, gate verdicts and
`LIBRARY_REQUEST_20260825.md` — files that mention a DOI are not that paper.

The fix is a constraint, not a better pattern: **the identifier must appear in the document's
header region** (first ~4 kB), and the file must be a full text rather than an abstract stub or
one of our own notes. That drops 27 to 5, and the 5 survive inspection.

Recorded because the failure mode is generic: a citation-shaped string proves the paper was
*cited*, not that it is *present*. Any future acquisition sweep will hit this.

### Still unpinned: 27 of 51

Entries 2, 3, 4, 5, 8, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 42, 46,
47, 48, 50, 56. The bibliography names an arXiv id for only two of them; the rest carry a DOI and
nothing else, so acquisition means a per-paper lookup with real paywall risk (Elsevier, Springer,
APS). `LIBRARY_REQUEST_20260825.md` already exists and covers part of this set.
