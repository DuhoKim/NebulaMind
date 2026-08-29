# GATE BRIEF — verify the question-1 answer

Fresh context, adversarial. **Not re-arguing whether to screen** — Duho returned question 1 to Tori
with "answer question 1" and it is answered. Check the reasoning and whether anything broke.

Files: `b26_answer_q1.py` (2/2), `OPEN_QUESTIONS_FOR_DUHO.md` (CLOSED question 1),
`../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md`,
`../bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md`.

## THE ANSWER

1. **The question is malformed for 18 of 51 papers** — entries 1–5, 13–16, 18–20, 28, 42, 47, 48,
   50, 56 have no pinned source, and hand-reading needs the text as much as the screen does. For
   those, acquisition is the queue.
2. **For the 33 readable: screen, then hand-check every flag.**
3. **The precision debate was largely beside the point** — if every flag is read, the screen cannot
   misfile anything; its accuracy determines only wasted reading. What it buys is the 30 it did not
   flag.
4. **The real risk is recall and it cannot be measured** — one known obstruction, caught; 1-of-1 at
   n=1 is not a measurement.
5. **It is already done** — 3 flagged, 3 read, 1 correct, no tier moved.

## ATTACK

1. **Is the 18-unpinned count right?** Tori's parser accepts a map row as "has a source" if the row
   contains a backticked `.txt`/`.pdf`. **A previous version of this same parser miscounted by
   missing cross-directory rows** — check it hasn't miscounted again, in either direction. Are any
   of the 18 actually pinned somewhere the map doesn't record?
2. **Is claim 3 sound, or too clever?** "A verified screen is safe at any precision" — is that true?
   Consider: a screen with terrible precision floods the reviewer, and reviewer fatigue is a real
   failure mode. At what precision does "check every flag" stop being affordable? Tori treats 1-in-3
   as obviously fine on 3 flags — does the argument survive if the screen flagged 30?
3. **Does claim 4 understate what CAN be measured?** Recall against known obstructions is n=1, but
   could recall be estimated another way — e.g. by hand-reading a random sample of unflagged
   readable papers and seeing whether any is an obstruction? **If that is cheap, "cannot be
   measured" is wrong and the answer should say so.**
4. **Is claim 5 true?** Verify all three flagged papers really have been read, and that no tier
   moved. Tori's own check initially reported entry 25 unread — a false absence he caught.
5. **Is the reframe legitimate or an evasion?** Tori answers a question Duho did not ask (acquisition
   is the bottleneck) alongside the one he did. Is that the useful reading, or dodging?
6. Predicate audit.

## VERDICT

First line one token: `Q1_ANSWER_CONFIRMED` / `Q1_ANSWER_REFUTED_<what>` / `Q1_ANSWER_NARROWED_<what>`.
Write to `<C or A>GATE_Q1_VERDICT.md` here.
