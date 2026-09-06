# BLANC ORDER — fix the README pin, then write the decision brief (2026-09-06 21:53 KST)

Codex replayed nine commands from its own round-3 review using the original
synthetic inputs, output to a fresh temporary directory
(.hermes/CODEX_TORI_R4_CLOSURE_AND_BRIEF_20260906.md). Result: the honest
D1 validation, audit comparison and batch join still PASS; the
missing-candidate and unknown-claim cases now FAIL as they should; and
uppercase / non-hex seeds now emit structured failures. That is revision 4
doing what it claims.

TWO THINGS:

1. ONE PACKAGING DEFECT. All seven pins were checked, but the README
   changed AFTER the pin sheet was generated: README_STAGED_UNADOPTED.md
   no longer matches its recorded digest (expected 1333de06f5fc99dc…).
   Regenerate the pin sheet, or restore the README — whichever is correct —
   and say in the record which and why. A pin sheet that does not match its
   own files is the one thing in this package a reader can check in ten
   seconds, and it should not be the thing that fails.

2. WRITE THE DECISION BRIEF NOW. It is inside authorized preparation; do
   not wait to be told again. It should carry:
     - the exact recommended D1 clause and the exact recommended D7 clause;
     - the batch approach;
     - for each: what accepting it changes about what the census can
       conclude, in plain words;
     - the review history honestly — three rounds, and the readiness split
       (codex NO / kimi YES) which was recorded on the OLD revision. Say
       whether it survives revision 4 or not; do not present it as settled
       either way without evidence.

A CORRECTION OF MINE, for your records and because I told Duho the wrong
number: I described the round-3 findings as "five new defects across the
two reviewers". That is wrong — both reports share N1 and N2, and only
codex additionally found N3. THREE unique defects. I added 3 + 2 without
checking the overlap. Record the correct count.

Nothing adopted. D1, D7 and the batch choice remain Duho's.
