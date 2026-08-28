# GORU Overhaul Review

*Amendment (2026-08-08): Corrected from the 0648 supplemental iteration to the actual watched artifact 0204, per Tori's provenance correction. The findings remain structurally identical.*

## 1. Visual State Timeline

I have inspected the `storyboard_spin_method_canary.json` and the corresponding `contact-sheet.jpg` & `ffprobe.txt` output for the rejected `spin-method-canary-20260808T0204` artifact.

| State | Start (s) | End (s) | Duration (s) | Type | Materially Distinct from Neighbour? |
|-------|-----------|---------|--------------|------|-------------------------------------|
| 1 | 0 | 6 | 6 | Title Card | Yes (new cut) |
| 2 | 6 | 16 | 10 | Point (Text) | Yes (new cut) |
| 3 | 16 | 26 | 10 | Point (Text) | Yes (new cut) |
| 4 | 26 | 33 | 7 | Data (Giant Number) | Yes (new cut) |
| 5 | 33 | 45 | 12 | Figure | Yes (new cut) |
| 6 | 45 | 56 | 11 | Point (Text) | Yes (new cut) |
| 7 | 56 | 68 | 12 | Figure | Yes (new cut) |
| 8 | 68 | 77 | 9 | Point (Text) | Yes (new cut) |
| 9 | 77 | 88 | 11 | Point (Text) | Yes (new cut) |
| 10 | 88 | 102 | 14 | Limit (Text) | Yes (new cut) |
| 11 | 102 | 114 | 12 | Close Card (Hold) | Yes (new cut) |

**Note on Unchanged States:**
There are several unchanged states >8s:
- State 2 (10s)
- State 3 (10s)
- State 5 (12s)
- State 6 (11s)
- State 7 (12s)
- State 8 (9s)
- State 9 (11s)
- State 10 (14s)
- State 11 (12s)

## 2. Graphics Measurement

The order requires **≥75% of runtime** carrying source-grounded plots/diagrams/animated graphics.
- Total Runtime: 114 seconds.
- Runtime with Figures (States 5 and 7): 12s + 12s = 24 seconds.
- **Percentage: 21.1%**
(Measured by extracting card durations from the storyboard JSON and matching with the `figure` kind vs `point`/`data` text slides). 

## 3. Audience Citation Violations

The order strictly forbids using internal filenames as audience citations. 
The video renderer (`nm_paper_video.py`) statically prints the `source` field onto the screen (e.g., `source: sources/T1_FUNNEL.json`). The storyboard defined a `display_citation` field, but the renderer completely ignores it and prints the literal file path instead.

The following internal filenames were incorrectly shown as on-screen citations:
- `sources/STATUS.json` (Card 2)
- `sources/T1_FUNNEL.json` (Cards 3, 4, 5)
- `sources/SOURCE_FREEZE.json` (Cards 6, 7, 9, 10)
- `sources/T1C_COLUMN_INTEGRITY.json` (Card 8)
