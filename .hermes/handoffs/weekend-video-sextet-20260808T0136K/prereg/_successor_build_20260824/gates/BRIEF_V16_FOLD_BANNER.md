# EDIT BRIEF — put the fold record in V16's banner, and fix the stale title.

Target: `../PREREG_SUCCESSOR_DRAFT_V16_20260827.md`, current sha256
`fc2fa7bab12e7606d9194e37c80f7f82ba7fdf65b47d6189fca961be1a8c3e48`. **Verify before you start.**

**Edit V16 in place. Do not create a new version. Do not touch
`../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` — it is the immutable base at
`efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28` and a previous fold run wrongly
modified it. It will be checked before and after this run.**

## 1. Fix the title

V16's first line reads `# PREREGISTRATION DRAFT V13 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN
FOOTPRINT`. **V13, V14 and V15 all carried this same stale title.** Change V16's to read **V16**.
A document whose own title is three versions stale is the defect class the referees have been finding
in §6 all evening, in the one place every reader looks first.

## 2. Add the fold record near the top, with the revision banners

**In the document's own text. Not a footnote, not an appendix, not a separate file.** V16 already
carries a fold record at the end of §6; this is the short banner version a reader meets before
reading anything else. It may cross-reference the §6 subsection for detail, but it must state these
things itself:

**a. What was folded.** `SECTION6_DRAFT_AGY_R15.md`, sha256
`d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a` — independently verified. Its
Part 1 is byte-identical to the R14 §6 body both referee seats credited.

**b. Under what authority and against what state.** Folded **on Duho's instruction at 21:48 KST on
2026-08-27, while R15's referee verdicts did not yet exist.** The referee round ran in parallel with
the fold.

**c. What the verdicts said when they landed during the fold.**
- **CODEX, 21:52:33 KST — CLEAR.** No blocking finding; Part 2 completeness holds at
  fold-instruction level. One **LOW / NON-BLOCKING** note: Part 5 line 159 uses a stale status label
  for the R14 completeness finding. CODEX states this does not weaken any required edit.
- **GPT56, 21:53:46 KST — NOT CLEAR.** One **HIGH / BLOCKING** finding: **the canonical
  unblinding-receipt schema is still absent from the asserted-complete Part 2 list.**
- Both agree four of the five R14 seams are **CLOSED** — §7 count and DESIGN inventory, §5 guard
  seam, §2.5 producer-checksum narrowing, and the Clause 10 / §10 repair-trace seam. The canonical
  receipt/schema seam is **narrowed but not closed**: the slot-schema portion is done; the
  unblinding-receipt schema itself is still omitted.

**d. That the GPT56 blocker is OPEN in this folded text.** Say it plainly. State that §6 remains
**tracked as open**, and that this draft carries a live blocking finding rather than a settled
section.

## 3. State the other carried-open items in the same banner

Findings 1, 2, 2b and 3 **UNRESOLVED** pending the refused BS-2a design; **BS-2a REFUSED by all three
seats**; rows C2 and E cannot run; **BS-6 and the first image byte remain blocked**; `verify_lock()`
required work, **not implemented**.

## 4. One known defect in V16 itself

`prereg_lint.py` reports on V16: **BS-2f is called a class-P prerequisite in prose while sitting in
class E.** V15 linted clean, so the fold introduced it. **Fix it if Part 2 item 7 already directs the
correct disposition — BS-2f is value-only per V15 lines 341–342 and 624. If fixing it requires a
judgement Part 2 does not supply, leave it and name it in the banner as an open lint finding.**

## What must not happen

Do not alter §6's body, the lifecycle table, any clause, any threshold, or §7's slot rows beyond the
BS-2f class disposition in item 4 above. Do not touch V15.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V16_20260827.md`, edited in place, single write. Report the new sha256.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch.
