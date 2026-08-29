# b7_stale_crossrefs — corpus-wide result

**Question (Blanc, asked four times): has it run across the whole bibliography, and what did it
find?**

## Answer: YES. Stale cross-references beyond the known entry 54 → entry 31 one: **ZERO.**

Run fresh 2026-08-29 15:26 KST.
Raw output beside this file in `B7_RAW_OUTPUT.txt`.

| | |
|---|---|
| entry blocks parsed | **58** — the whole bibliography |
| entries with a parseable tier | **51** |
| cross-references carrying a tier/status claim | **5** |
| **stale beyond the known one** | **0** |
| unnamed population claims | **0** |
| CALIBRATED-FALSIFIER entries | [7, 31, 51] |

### The five, individually

| claim in row | about entry | that entry's current tier | verdict |
|---|---|---|---|
| 6 | 7 | CALIBRATED-FALSIFIER | consistent |
| 6 | 31 | CALIBRATED-FALSIFIER | consistent |
| 7 | 31 | CALIBRATED-FALSIFIER | consistent |
| 25 | 23 | QUALITATIVE-DIRECTIONAL | consistent |
| 31 | 54 | QUALITATIVE-DIRECTIONAL | **the known one — now present only as a quoted retraction** |

## Why it took three relays to land

Not because it was hard. **It ran the first time and I reported the result in prose, twice.**
The item stayed open because my answers were in chat messages and this lane's state lives in
files. That is my failure of medium, not of work — hence this file.

## What it took two repairs to be worth anything

1. Its verification predicates were broken (whitespace across a line wrap; an absence test that
   would have been satisfied by deleting a retraction — register §1k).
2. **Its tier parser silently skipped entries 7 and 51**, because `[A-Z\- ]` cannot match the
   `/ FIRED` and `/ LIVE` status suffixes this bibliography uses. Those entries got no tier and
   the loop's `if r in tiers` passed over them without a word. I reported "n=2 calibrated
   falsifiers"; the answer is 3, which is what Blanc's own briefing had said.

**So the honest form of the answer is: zero stale, from a probe that had to be corrected twice
before its zero meant anything.**

## What it cannot see

Named per the admissibility rule: claims referencing an entry without naming it (0 found, but the
pattern for those is itself narrow); claims in the ranked-target list and appendices, which use
separate numbering; and claims in other lane documents — scanned separately, 91 hits, of which
essentially all are correct history rather than staleness.
