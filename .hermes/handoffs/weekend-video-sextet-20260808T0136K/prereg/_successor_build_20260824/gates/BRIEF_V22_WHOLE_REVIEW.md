# REFEREE BRIEF — V22, whole document. Seventh assembled round.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V22_20260827.md`**, sha256
`9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3`. **Verify before opening; state
what you compared and what it returned.** 25 lines changed from V21.

## A defect that survived five drafts and two of your reviews

§7's prose claimed **8 class-E slots** over a table holding **7**. It entered at **V17** and V18–V21
inherited it.

**It was not caught by either of you, and it was not caught by me.** GPT56 correctly found that the
V16→V17 trace row overstated a class-P repair that never happened — but its proposed replacement,
*"Repaired the Class E count in §7 from 7 to 8"*, described the **introduction** of the error as its
repair, and I wrote that wording into V20's trace. A byte check confirmed the 7→8 edit had occurred.
**Nobody counted the rows.**

**The standing lesson, which applies to your reports as much as to the draft: when a finding says a
value was changed, check whether the new value is correct — not merely that the change happened.**

A `prereg_lint.py` check now compares §7's prose counts against its parsed table. Its own first
version reported clean, because §7 states its live count inside a blockquote and the history
predicate treated every blockquote as a quotation — **a guard that could not fire, reporting
"clean."** Fixed; history is now marked only by explicit version citation.

## What V22 changes

1. **The count is corrected and the table grew.** The `VOID` converter now has a real slot, **BS-2v**,
   class-P DESIGN, unfilled — so class-P is **15**, class-E is **7**, and the prose now says so.
   **Count the rows yourself.**
2. **The trace row states the truth**: *"V17 changed the class-E prose from 7 to 8 while the table
   held 7, introducing a count error that V18–V21 inherited, and V22 corrects the prose to 7."*
3. **`BS-2v` is receiptable** — producer, inputs, schema, and what it blocks — rather than a sentence.
4. **"Branch-complete" is now decidable**: a canonical closed antecedent registry with stable IDs and
   exact source/phase/failure-effect per `VOID` branch, a **set-equality coverage requirement**, and a
   defined failure effect for missing, duplicate or non-`VOID` coverage.
5. GPT56's third missing unresolved-inventory item added; V21→V22 trace entry added.

## What to judge

1. **Digest first**, with the comparison stated.
2. **Count both classes of §7 row yourself** and compare to the prose. Do not take 15 and 7 from me.
3. **Is `BS-2v` genuinely enforceable?** Can a gate fail an incomplete antecedent manifest using only
   what the document specifies? Set equality against *what*, exactly — is the reference set closed and
   named?
4. **Adding a class-P slot changes what BS-6 waits on.** Check every count, inventory, dependency and
   lint assertion that mentions class-P still agrees. **A row insertion broke the count last time.**
5. **Read the neighbours** of every change.
6. **Clause 10 across §§0–11, both directions**, still expecting it explicitly unresolved at `VOID`.
7. **Every threshold: value, phase, failure effect.** **All six §10 trace entries accurate?** State
   what you compared.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked** for two separately named reasons, now including unfilled `BS-2v`.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`V22_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

**Judge independently; do not converge.** If V22 is a correct preregistration that is honest about
being an unfinished programme, say so in those words — CODEX came within one count and one
enforceability gap of that verdict last round.
