# Data-first mapping: what each paper project could actually measure
Built 2026-08-05 on Duho's instruction: "you should survey the data for each paper project and
actually study it". Method: `tools/nm_data_survey.py` — VizieR TAP_SCHEMA metadata only, two
enumeration channels (UCD + case-complete name), then joint intersections. No science rows
fetched, nothing computed, no verdicts. Counts are availability, not usability: the Shape-1
eligibility discipline (per-table verdicts with source receipts) still has to run before any
table becomes a number.

## The finding that frames everything

| quantity | tables | reachable ONLY by UCD |
|---|---|---|
| gas metallicity | 5,560 | 5,263 |
| redshift (spec) | 6,684 | 5,941 |
| stellar mass | 6,206 | 4,367 |
| Lyman continuum / ionizing | 2,909 | 2,876 |
| UV luminosity | 2,392 | 2,356 |
| star formation | 1,006 | 39 |

**~95% of the relevant archive is invisible to name-based search.** Every project so far was
built on a handful of literature values while thousands of tables carrying the same quantities
sat unqueried — not because they were checked and rejected, but because nothing looked.

## Joint availability — what combination of columns a measurement needs

| measurement | tables carrying all required axes |
|---|---|
| UV LF / number density (absMag + z) | 681 |
| SFRD (SFR + z) | 477 |
| main sequence (SFR + mass + z) | 404 |
| abundance evolution (abundance + z) | 345 |
| MZR (mass + abundance + z) | 174 |

Reality check on the high-z end (description-text proxy, recorded as a proxy): 49 catalogs
mention JWST, 4 mention reionization, 2 mention an escape fraction.

## Per project

### 1. Reionization photon budget — f_esc z-sweep (flagship, frontier 16) + landscape note
**Kun already said it**: "a well-measured number about a model of the literature, not about the
sky"; on the landscape note, "zero new data". Never actioned because it lived in a merit score,
not a referee finding.
**Data reality**: 2,909 LyC/ionizing-tagged tables exist, but only 2 catalogs describe an escape
fraction at all, and f_esc is not directly observable at z>6 — the physics, not the archive, is
the limit.
**What could make it a measurement**: pivot to what the 477 SFRD-capable and 681 LF-capable
tables do deliver — the ionizing *emissivity* side (ρ_UV and its evolution) measured from
archive data rather than adopted from Robertson-style anchors, with f_esc left as the declared
unknown. That converts "our model of the literature says X" into "the archive says ρ_UV does Y,
and here is what f_esc would have to be".
**Honest alternative**: retire both from flagship status, as with the z9–10 paper.

### 2. Mass–metallicity — anchor-gap census (flagship, frontier 41), z7-MZR (orphan), z9–10 (rejected)
**Data reality**: 174 MZR-capable tables (mass + abundance + z together); 345 with abundance+z.
The anchor-gap census surveyed *auroral-line* tables only (79 → 5 anchors) — a deliberately
narrow slice of those 174.
**What could make it a measurement**: the census instrument re-run over the full 174 with the
eligibility layer, giving the MZR its own archive-wide census rather than a literature
comparison. This is the most tractable upgrade on the board: the machinery exists and was
already proven on a harder case.

### 3. Bright-end UV LF — Shape-1 gap paper (compiled, referee ESTABLISHED)
**Data reality**: 681 absMag+z tables archive-wide; the census used 112 candidates after the
frozen z>7.5 frame. The gap result stands — but it is a statement about the *published-LF*
record, and the 681 is the number that shows how much object-level data exists beneath it.
**Next**: no rewrite needed. The paper is honest about its scope; §7 already says VizieR is not
the only archive.

### 4. Star-forming main sequence / quenching (frontier drafts, AGN Step-7 lane)
**Data reality**: 404 tables carry SFR + mass + z together — the richest untouched intersection
on the board, and the one with no paper attached.
**What this enables**: a scaling-relation study built from archive data from the first step,
which is exactly the shape Duho has been asking for.

### 5. What no project currently uses
1,006 SFR tables, 6,206 mass tables, 6,684 redshift tables. Only **SDSS and COSMOS2020** are
marked in use on the Surveys page (2 of 39 catalogued surveys).

## Recommended order (mine, for Duho to accept or overrule)
1. **MZR archive census** — instrument exists, 174 tables, highest chance of a real measurement.
2. **Main sequence** — 404 tables, no incumbent paper to unwind.
3. **Reionization pivot to emissivity** — keeps frontier 16 alive on measured ρ_UV.
4. **Shape-1** — land as is; it is already a data paper about the archive.
