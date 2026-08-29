# Entry -> pinned-source map (Step 0)

Built 2026-08-28 by script, not by seat. 12 auto-matched on title at score 1.00;
8 resolved by reading each file's own title. One file is NOT a bibliography entry.

| entry | tier | pinned file | sha256 (12) |
|---|---|---|---|
| ~~1~~ **46** | CONSISTENCY-ONLY | `1111.1017_clean.txt` | `c9780a259194` | **CORRECTED 2026-08-29 — see below** |
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

---

## EXTENSION 2026-08-28 (2) — the ranked targets, acquired. +6 entries

`a1_fetch_unpinned.py` in `bhu-acquisition-20260828/`, 3/3 self-checks, exit 0.

Cross-referencing the bibliography's OWN ranked target list against the pinned set showed the
ranking was mostly unacquired — ranks 3, 4 and 5 entirely, and rank 1 missing exactly one paper:

| entry | pinned file | sha256 (12) | why it was on the list |
|---|---|---|---|
| 8 | `0902.1994_clean.txt` | `6c22823e60a6` | rank 1 — the only missing member of the Popławski spine |
| 21 | `2203.13295_clean.txt` | `82f0d604d5b4` | rank 4 — Roupas "detectable" |
| 22 | `2606.25023_clean.txt` | `14e2200090a9` | rank 5 — Easson no-go theorems |
| 23 | `2003.11544_clean.txt` | `25cf2122ba7b` | rank 3 — parent of entry 54's causal-horizon chain |
| 24 | `2104.00521_clean.txt` | `ff5670f8ff9a` | rank 3 supporting |
| 27 | `2204.11608_clean.txt` | `c1e91c0a88a6` | rank 3 supporting |

**Auditable corpus: 24 → 30 of 51.**

### The paywall claim below is WRONG for the targets that matter

The section that follows says the unpinned set carries "a DOI and nothing else, so acquisition
means a per-paper lookup with real paywall risk (Elsevier, Springer, APS)." That framing cost
this lane time. In fact **EPJC is gold OA via SCOAP3, Symmetry and Universe are MDPI OA, and
Popławski, Gaztañaga and Easson all post to arXiv.** Six of eight targets resolved on a single
arXiv title query and downloaded in one pass, in under a minute, with no paywall encountered.

The correct statement is narrower: the *bibliography* records DOIs only, so the identifiers are
missing from our record — not from the world. A title query recovers them.

**Still genuinely unresolved: entries 25 and 26** (Gaztañaga, "The Black Hole Universe" Parts I
and II, Symmetry 14, 1849 and 14, 1984). No arXiv posting under those titles. Both are MDPI
open access, so they are *available* — they just need fetching from mdpi.com rather than arXiv.
These are rank 3's two primary papers and remain the largest single hole.

---

---

## EXTENSION 2026-08-28 (3) — entries 25/26, rank 3's two primary papers. +2

| entry | pinned file | sha256 (12) | route |
|---|---|---|---|
| 25 | `sym14091849_clean.txt` | `391a2510c8be` | publisher page, browser |
| 26 | `sym14101984_clean.txt` | `01aad28a7d44` | publisher page, browser |

**Auditable corpus: 30 → 32 of 51.** The Gaztañaga series (23, 24, 25, 26, 27) is now complete,
which closes the hole under entry 54: phase 6 audited the 2025 PRD paper in depth while its
parent series sat unacquired.

### Every scripted route was bot-blocked; the papers were never paywalled

    mdpi.com article + /pdf + doi.org ......... HTTP 403 (Cloudflare)
    hal.science /document and /file/*.pdf ..... HTTP 200, "Making sure you're not a bot!"
    digital.csic.es bitstream ................. HTTP 200, 4,455-byte HTML

The CSIC result is the one to remember: an invented path, `blackhole1.pdf`, returned **the same
4,455 bytes** as the real `blackhole2.pdf`. A 200 and a plausible size prove nothing. Metadata
came from the OpenAlex and HAL APIs, which are open; the text came through Chrome, which clears
the challenge. These are CC-BY articles — the obstacle was anti-bot, not access.

### Two traps recorded because they will recur

**The preprint-title trap.** OpenAlex and HAL both title entry 25 *"The Black Hole Universe (BHU)
from a FLRW cloud"*, and HAL's deposit is `BHUelsaV2.pdf`. That is the preprint title; the
published article is *"Part I"*. This is exactly why the arXiv title sweep in extension (2) found
entries 21/22/23/24/27 and missed 25/26. Searching a published title against an index that
carries the preprint title returns nothing, and looks like absence.

**The truncation trap, which I walked into.** `a3_pin_mdpi.py` pinned both papers and passed
3/3 — while entry 25 was missing 36% of its text. `get_page_text` cuts at 50,000 characters, and
a truncated file still contains its DOI, its title, and the word "Conclusion". `a4_stitch_mdpi.py`
rebuilds both from three overlapping captures and checks landmarks from the **start, middle and
end** of each paper, because only an end-landmark can fail on a truncation.

---

### Still unpinned: 19 of 51 (was 21)

Entries 2, 3, 4, 5, 13, 14, 15, 16, 17, 18, 19, 20, 21, 28, 42, 46,
47, 48, 50, 56. The bibliography names an arXiv id for only two of them; the rest carry a DOI and
nothing else, so acquisition means a per-paper lookup with real paywall risk (Elsevier, Springer,
APS). `LIBRARY_REQUEST_20260825.md` already exists and covers part of this set.


---

## CORRECTION 2026-08-29 — entry 1 was mis-mapped; the file belongs to entry 46

**Found by the depth-selection rule on its first pick** (`b3_entry1_mismap.py`, 3/3). The rule was
fixed in advance, ranked entry 1 top on numeric density, and sent me to a paper my own judgement
had not chosen. It was the wrong paper.

| | claimed | actually |
|---|---|---|
| `1111.1017_clean.txt` | entry 1 — Pathria (1972), *"The Universe as a Black Hole"*, Nature 240, 298–299 | entry 46 — *"Quantization of the Universe as a Black Hole"* (Alfonso-Faus), preprint of ApSS 337, 19–20 |

The pinned file contains the **10¹²² bits** Bohr-quantization result that this bibliography
already attributes to **entry 46**. It is entry 46's paper.

**How the map got it wrong, in its own words:** *"12 auto-matched on title at score 1.00"*. The
string *"The Universe as a Black Hole"* is a **substring** of *"Quantization of the Universe as a
Black Hole"*, so a containment-scoring matcher returns a perfect 1.00 — on the wrong paper. The
score was honest; it meant something other than what it was read as.

**Corrected state:**
- **Entry 46 is PINNED** — `1111.1017_clean.txt`. It was listed among the unpinned.
- **Entry 1 has NO pinned source.** The bibliography always said so: its full text is *"still
  unobtained"* and the paywalled body *"remains [VERIFY]"*.
- **The auditable-corpus COUNT is unchanged** (one entry pinned either way). Its **composition**
  was wrong.
- **No tier changes.** Entries 1 and 46 are both CONSISTENCY-ONLY and both stay. This is a
  provenance correction.

**And the part that matters most:** entry 1 was in the random-draw pool for the selection-bias
control. Had it been drawn, the lane would have depth-audited Alfonso-Faus under the label
"Pathria 1972" and reported a tier verdict for a paper nobody had opened. It was not drawn — that
is luck, not method.
