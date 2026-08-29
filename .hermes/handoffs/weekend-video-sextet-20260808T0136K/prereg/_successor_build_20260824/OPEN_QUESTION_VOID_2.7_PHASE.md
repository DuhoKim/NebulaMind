# OPEN QUESTION — when does "inference exist"? The §2.7 phase, deliberately unresolved in V37.

**Raised 2026-08-29 09:4x KST by Hwao. The principal's 09:20 authorisation covered decision 1
option A and decision 4 option (a). Blanc's relay was explicit that it did NOT cover this, and that
I must not pick the cheap answer because the surrounding work is authorised. I have not.**

## What was done, and what was not

`VOID-2.7-THRESHOLD-MOVED` → **`VOID-2.7-THRESHOLD-CHOSEN-OR-MOVED`**. Coverage extended to a
threshold *chosen*, as authorised. **The phase cell is unchanged at `Post-first-real-χ`**, inherited
from the predecessor ID. Nothing about the instant was decided.

§2.7 line 388, byte-identical since V30: *"A threshold **chosen or moved after inference exists**
voids the run."* The registry says `Post-first-real-χ`. **Those are not obviously the same instant**,
and the document itself shows they are not.

## The ordering is established from the document, not assumed

Row P (§6.1, line 558) is **"post-unblinding only: reads the real χ vector"**. So the first real χ is
read *after* unblinding. **`Post-unblinding` is strictly earlier and strictly broader than
`Post-first-real-χ`, and there is a real window between them.**

**That window is the whole question.** A threshold chosen or moved after unblinding but before the
first real χ is read: §2.7's prose plausibly voids it; the registry's current phase does not.

## The candidates, in the document's own closed phase vocabulary

| candidate | reads "inference exists" as | what it costs |
|---|---|---|
| **`Post-first-real-χ`** (current) | inference exists once a real χ has actually been computed | **Narrowest. Leaves the unblinding→first-χ window uncovered.** If a threshold can be chosen in that window on the strength of anything unblinding revealed, the prose voids it and the registry does not. |
| **`Post-unblinding`** | inference exists as soon as the data are unblinded and the analysis *could* be run | Closes the window. Cost: it voids threshold-setting the study may legitimately intend to allow after unblinding but before χ — and §2.7 line 388 explicitly says *"Post-unblinding instrument-confidence handling is kept separate"*, so post-unblinding activity is contemplated and not uniformly forbidden. |
| **`Any`** | any threshold chosen or moved at all voids | Maximally safe and almost certainly wrong: thresholds must be chosen at *some* point, and §2.7 line 386 says these were *"fixed before any image byte, which makes the predicate preregistered rather than chosen."* `Any` would void the study's own act of preregistering them. |

## One interaction worth knowing before deciding

§6.3's Void rule (line 614) already reads: *"Any **post-first-real-χ** change to ANY binding rule,
parameter, algorithm, slot…"* So a threshold change after the first real χ **may already be caught by
that broader rule**, which would make the §2.7 antecedent's distinctive value precisely its coverage
of the *earlier* window — an argument for `Post-unblinding`. I am flagging the interaction; I have not
verified that §6.3's rule subsumes the §2.7 case, and that verification should happen before the
choice is locked.

## What I recommend, and why I distrust myself here

**My reading is `Post-unblinding`** — it is the only candidate that closes the window §2.7's prose
appears to describe, and the interaction above suggests the earlier window is where this antecedent
earns its place.

**Treat that lightly.** `Post-first-real-χ` is the zero-work answer: it is already in the cell, it
already passes every checker, and V37 is otherwise complete. That is exactly the shape of the
temptation I flagged on the T fork — the cheap option arriving dressed as the finished one. **The
choice determines which acts void a real run, so it is a claim about the study, not a cell value.**

## Status

- **V37 is written and does not depend on this.** All four checkers were run; the registry digest
  (`a4d1d745…`) will change if the phase changes, so **the registry must not be pinned as final until
  this is answered.** §7.1 says so in the document.
- BS-6 and the first image byte remain blocked. Nothing here touches them.
