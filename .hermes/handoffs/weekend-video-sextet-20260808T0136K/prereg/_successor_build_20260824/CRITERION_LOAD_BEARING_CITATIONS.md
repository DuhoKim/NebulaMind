# CRITERION — which citations option D verifies. Written before classifying.

**Duho ruled option D (2026-08-29, relayed by Blanc): verify only the repair-announcing citations,
not all 94. Blanc's instruction was that the criterion is the deliverable, not the list, and that it
must be written before a single citation is classified — because a rule written afterwards is a
rationalisation of choices already made.**

## Disclosure first: I have already seen the corpus

**I cannot honestly claim this criterion was written before I looked.** Earlier today I measured the
corpus (104 citations), split it structurally (88 in §10's changelog table, 16 in prose), and
hand-verified 11 pre-format prose citations — finding one miscitation. So a criterion drafted now
could be shaped to fit what I already know.

**What I have instead is an anchor written before any of it.** `CITATION_CHECK_SPEC.md`, committed
**05:19 today**, hours before the corpus was measured, states the purpose:

> The document's most dangerous sentence is one announcing a repair, because a reader stops checking
> there. The check exists so that `V## CORRECTION (SEAT-Vn Fk)` cannot cite a finding nobody made.

The criterion below is derived from that sentence, not from the distribution I later observed. Where
the two could diverge I have followed the spec. **Readers should weight this accordingly**, and the
`UNCLASSIFIABLE` bucket exists so that my prior knowledge cannot quietly dispose of a hard case.

## The criterion

> **A citation is LOAD-BEARING if and only if a reader who accepts the surrounding sentence would
> stop checking the underlying issue — that is, the citation is offered as the warrant for a claim
> that something in this document was REPAIRED, FIXED, CLOSED, WITHDRAWN, RETRACTED or VERIFIED.**

Three consequences, stated before application:

1. **Warrant, not mention.** The test is whether the cited finding *does work* in the sentence. A
   citation that attributes a position or observation to a seat, without claiming the document
   changed in response, is not load-bearing.
2. **Independent evidence defeats load-bearing status.** If the same sentence or row carries evidence
   for its claim that does not depend on the citation — a from/to digest, a diff, a named changed
   section — then a reader is not relying on the citation to accept the claim, and the citation is
   provenance metadata. **A record whose accuracy is independently checkable is not the dangerous
   sentence the spec describes.**
3. **A citation the rule cannot decide is UNCLASSIFIABLE, never excluded.** This is the one
   non-negotiable. Using a pattern to establish that a citation is *not* load-bearing is the same
   unsound move — a narrow pattern in the absence direction — that got the citation check quarantined
   after three rounds. Anything the rule cannot decide is reported for a human to read.

## What this predicts, before I run it

Stated in advance so the result can embarrass the criterion rather than be fitted to it:

- **`V## CORRECTION (…)` blockquotes select.** They are the spec's named target.
- **Prose sentences saying a claim was narrowed, deleted, withdrawn or recorded at its real strength
  select.** The reader has nothing but the citation.
- **§10 changelog rows do NOT select**, by consequence 2: each row carries from/to digests and the
  changed-section list, so its claim is checkable against the bytes without trusting the finding ID.
  A changelog row with no digest WOULD select — the rule turns on the evidence, not the location.
- **Carried-open / status listings do NOT select.** They assert an item is still open, which is the
  opposite of announcing a repair; a wrong citation there misattributes an open item, it does not
  retire one.

**If this selects a large fraction of the 94, option D has collapsed back into option A and I will
say so plainly rather than let it happen quietly.** That is Blanc's test and I accept it as written.

## Boundaries carried from the ruling

- **No retrofitting blocks onto historical reports.** Option B is rejected; deciding which numbered
  items were findings for reports whose authors are gone, and freezing that as fact, is exactly the
  judgement nobody is in a position to make now.
- **Non-selected citations keep reporting `NO_BLOCK`.** They must not drift to `UNVERIFIABLE` or
  `VERIFIED`. Those outcomes were kept separate so that a pending human decision could not hide
  inside a parse failure; now that the decision has been made, the separation records *which* answer
  each citation got, and matters more rather than less.

---

# RESULTS — applied 2026-08-29 12:4x

**12 selected, 96 not selected, 0 unclassifiable** out of 108 citation instances (compounds
expanded). **Selected = 11% of the corpus. Option D has NOT collapsed back into option A** — Blanc's
test was whether it would select ~80 of 94; it selects 12.

**All four advance predictions held.** `V## CORRECTION` blockquotes selected. Prose announcing a
narrowing, deletion or settlement selected. §10 changelog rows did not, by consequence 2 — each
carries from/to digests. Carried-open status listings did not.

## Two things the run itself taught

**The first pass was line-based and split a wrapped sentence.** Line 66 selected and line 67 did not
— *the same sentence*, wrapped. Three citations landed in `UNCLASSIFIABLE` for a formatting reason
rather than a substantive one. **The bucket did exactly the job it was put there for**: it surfaced
a defect in the application instead of silently under-selecting. Fixed by classifying paragraphs.

**One case genuinely needed a human.** Line 748 reads *"RESOLVED at V40 by principal ruling"* — an
unambiguous repair announcement whose verb was simply missing from the warrant vocabulary.
Adjudicated **selected**, and the vocabulary extended. That is one hand-adjudication in 108, which is
what a `UNCLASSIFIABLE` bucket should cost.

## The result that matters most, and it is not the count

**The only wrong citation in the entire corpus is one option D does not select.**

The miscitation I found by hand this morning — `KIMI-V11 F4`, an access finding cited for a Stage-P
claim, corrected to `F7` — sits at line 276, inside *"STAGE P REMAINS DUAL-VALUED … LEFT OPEN
DELIBERATELY"*. The criterion classifies that **not load-bearing**, correctly and for the stated
reason: a wrong citation on an open item misattributes provenance, it does not retire a defect.

**This is not an argument against D**, and I am not making one. The harm model that justifies D is
intact: a wrong citation announcing a repair lets a real defect stand, which is categorically worse.

**But it should change how the result is read.** Empirically, the one error in 108 citations lay in
the class D does not verify. So when option D reports clean, that means *"every repair-announcing
citation is sound"* — it does **not** mean *"the citations are correct."* Anyone quoting this work
should quote the first sentence and not the second.

## Option D's work is already complete

All 12 selected citations are verified:

- **8 are pre-format** and were hand-verified this morning against their V11, V24 and V34 reports,
  checked for topical match and not merely for a finding number that exists.
- **4 resolve against declared `FINDINGS-BLOCK v1` blocks** and were machine-verified:
  `CODEX-V38 F2`, `CODEX-V38 F3`, `CODEX-V38 F4`, `GPT56-V40 F6` — all **VERIFIED**.

**No further verification work is outstanding under the ruling.** The 96 non-selected citations
continue to report `repair-citation-legacy` / `NO_BLOCK`, which is now their permanent and honest
answer rather than a deferral.
