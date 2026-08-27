# FOLD BRIEF — produce V16: V15 with §6 replaced and Part 2's conforming edits applied.

You are folding the refereed §6 replacement into the preregistration. **This is an assembly task, not
a drafting task.** Do not improve, rephrase or extend anything. Every substantive decision has been
refereed already; your job is to place it correctly and change nothing else.

## Inputs, pinned

- **Base:** `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md`, sha256
  `efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28`, 699 lines.
- **Section:** `SECTION6_DRAFT_AGY_R14.md` — its sha256 is pinned in `runner_s6r14_round.log`.
  **Verify it before you start and record what you read.**

## The fold

1. **Replace V15 lines 461–590** — from `## §6 Conduct` through the last line before
   `## §7 Binding slots` — with **Part 1 of R14**, the complete §6 replacement including §6.1, §6.2,
   §6.3, the lifecycle table and all ten clauses.
2. **Apply every conforming edit in R14's Part 2** to the sections it names — §2.7, §4, §5, §7 and
   the code-side inventory. Part 2 exists to enumerate exactly this; apply it literally.
3. **Do not carry Parts 3, 4 or 5 into the preregistration.** They are drafting apparatus — choices,
   residual risks and the finding map. They stay in the gates directory.

## The fold record — add this as a new subsection at the end of §6

A short, factual block. No advocacy.

- **Folded section:** `SECTION6_DRAFT_AGY_R14.md`, with its sha256 written out in full, folded on
  2026-08-27.
- **Referee state at fold:** GPT56 returned **CLEAR** on R12 and again on R13, with no blocking
  finding. CODEX returned NOT CLEAR on R13 with one blocking finding, which R14 addresses in Part 2.
  State whether R14 has been refereed at the time of folding; if it has not, say so plainly.
- **Clause 10 audited in both directions by GPT56 on R12 and R13** — forward termination and reverse
  reachability — and CODEX's independent clause-10 audit on R13 concurred that the partition is
  single-valued and correctly seated. **This is the strongest evidence §6 carries and it must travel
  with the section.**
- **Carried open, not closed by this fold:** findings 1, 2, 2b and 3 remain **UNRESOLVED** pending the
  refused BS-2a design; **BS-2a is REFUSED by all three seats**; rows C2 and E cannot run; **BS-6 and
  the first image byte remain blocked**. The `verify_lock()` calibration-PASS implementation named in
  Part 2 is required work and is **not** implemented.
- **Known design consequence, with the principal:** any single post-unblinding removal emits
  `INCONCLUSIVE-BY-CALIBRATION`. No attrition rate exists in the frozen record, so the probability is
  unknown; what is established is that one removal suffices.

## What must not happen

- **§6 must not stop being tracked as open.** This fold places a section that one seat has cleared
  twice and the other has an open objection against. The document must say that.
- Do not adjust any threshold, re-seat any decision, add or delete any branch, or alter the lifecycle
  table. All of it is refereed.
- Do not renumber §7's slot table or change its class assignments except exactly as Part 2 directs.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V16_20260827.md` — the complete document, single write.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch.

**If Part 2 names an edit you cannot apply because the target text is not what Part 2 expects, stop
and say so in your reply rather than improvising a placement.** A misplaced conforming edit is worse
than a reported mismatch.
