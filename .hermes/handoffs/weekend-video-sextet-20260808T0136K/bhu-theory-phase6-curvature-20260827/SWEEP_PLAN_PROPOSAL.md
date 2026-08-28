# Sweep plan — proposal, not yet run

Tori, 2026-08-28. Blanc asked me to propose before running if the shape was not obvious. It was
not. Two things I found while scoping change the design.

---

## What the inventory established (testimony, verifiable)

**The count reconciles.** 63 entry headers = 51 classified papers + 7 support entries (Brown–Bethe
max mass, Harada–Yamawaki, Ferdman, Tauris, Longo — instruments cited *by* the chain, correctly
carrying no Testability line) + 5 headers from a second numbered list summarising branches.
Blanc's 51 is right; there is no hidden pool of unclassified papers.

**But the entry→source mapping cannot be derived mechanically.** This is the obstacle.
`bhu-reading-20260823/sources/` holds 28 pinned files (20 `_clean.txt` + PDFs). I could
auto-link only 12 of them to entries. The rest fail because **the bibliography records DOIs, not
arXiv IDs** — entry 54's record cites `10.1103/physrevd.111.103537` and never the string
`2505.23877`, so the file I read from this morning does not match its own entry by any string
search. The mapping exists, but only as prose in `READING_NOTES_01.md` (`## Entry NN — Author,
"Title"`).

**Consequence:** any sweep must start by building that map, and no plan that assumes ~48
re-readable entries is honest. On current evidence the sweepable set is **roughly 20**, not 48.

---

## The design problem, stated plainly

All three failures so far were **overclaims**, and all three were found by me re-reading entries I
had classed. That is a biased sample: I looked where I suspected. A sweep run the same way will
find more overclaims and will systematically miss underclaims — Blanc's point 2, and the thing
worth more than another demotion.

**A seat told our prior tier will anchor on it.** That is the whole risk.

---

## Proposed method: blind re-classification, with a measured control

**Step 0 — build the map.** Delegate. One seat, `READING_NOTES_01.md` + the sources directory,
output a CSV of `entry_number, title, pinned_file, sha256`. Mechanical, no judgement. This is
also the artifact that fixes the DOI/arXiv gap permanently.

**Step 1 — the falsifier-shape screen.** Mine, scriptable, costs no context. Grep every pinned
text for threshold-shaped language: `falsif`, `rule out`, `refute`, `exclude`, `would be
inconsistent with`, numerals adjacent to `±`, `>`, `<`, `M_sun`, `sigma`. Rank entries by hit
density. **Purpose: find CONSISTENCY-ONLY entries that contain an author-stated number and
threshold** — a live test we have been ignoring.

**Step 2 — blind re-classification.** Delegate in batches. Each seat gets: the paper, the tier
definitions, and **NOT our current tier**. It states what the paper supports, and only then is
the comparison made. Any seat that knows the prior answer cannot find an underclaim, because the
prior answer is what an underclaim looks like.

**Step 3 — the control, which is the part that makes the screen honest.** Include in every batch
a random sample of entries the screen did **not** flag. If blind re-classification promotes one
of those, the screen has a false-negative rate and its silence proves nothing. Without this the
sweep can only confirm what the screen already suspected — the same defect as the `abs()` check
that could not see the sign change, and the `nan` that hid behind a reported dipole.

**Step 4 — gate.** Two seats per proposed re-tier, as with 54/31/7. I do not apply any tier
change; that is Blanc's, and I am the interested party on the twenty I classed on 2026-08-23.

---

## Cost, honestly

Steps 0, 2 and 3 are seat work — agy, gpt, kimi. Step 1 is mine and cheap. My context goes on
designing briefs and adjudicating returns, not on reading papers. Estimated ~20 sweepable
entries in 4 batches of 5, plus controls.

---

## What I will report as unverifiable, not swept

Every classified entry with no pinned text, listed by number, with the reason (paywalled, no
eprint, never obtained). Four entries are already tiered UNREAD and are honest about it. The
larger group is entries carrying a **READ marker whose source I cannot now locate** — those are
the uncomfortable ones, because the record asserts a read that cannot be re-verified. I will
name them individually rather than in aggregate.

---

## Disclosure

I classed twenty of these on 2026-08-23, in the same batches, by the same method that produced
three-for-three overclaims. The blind step exists because my judgement is the thing under test,
and no amount of care from me substitutes for the seat not knowing what I concluded.

**Awaiting go/no-go before running Step 0.**
