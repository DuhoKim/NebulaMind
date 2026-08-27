# REFEREE BRIEF — §6 fifth pass. One question decides this round.

Subject: **`SECTION6_DRAFT_AGY_R5.md`**, sha256 `63782432d816ef74581f5e9d9a181105b9926b7a16bee48acd0288d6593d6654`.
Author: the agy seat, fifth pass. You are not its author. Do not referee your own text.

## What changed, and why it is not another rename

Your R4 reports — `SECTION6_REVIEW_R4_GPT56.md` and `SECTION6_REVIEW_R4_CODEX.md` — both landed
on the same defect, in different words:

- GPT56 1: the acceptance-evidence projection is *declared* outcome-free, not *made* outcome-free.
- CODEX 1: it is not sign-blind by construction; row D still sees enough.

Duho's instruction on receiving those two reports was explicit: **make the projection outcome-free
BY CONSTRUCTION, not by declaration.** And: "if the honest construction is that some evidence
cannot be shown at all before unblinding, say that and lose the convenience."

R5's response is a structural change rather than a wording change. It **moved the writer.** A new
row **C2** (`verify_cutout_integrity`) runs pre-inference, reads only cutouts and fixed parent
lists, never invokes the classifier, and writes the projection. Confidence-based exclusion is
**removed from the pre-lock path entirely** and deferred to `run_production_verdict()` after
unblinding — with the cost stated in the draft rather than hidden: "we do not know until
post-unblinding if too many objects fall below the confidence threshold, potentially wasting a
run… We accept this cost for structural integrity."

## The question this round turns on

**Is row C2 actually incapable of seeing an outcome, or has the same capability simply been moved
earlier in the pipeline and given a new name?**

That is the whole round. R3 and R4 both failed by renaming, and the draft itself names this as its
characteristic defect (Part 4, D1). Treat the draft's own confession as a claim to test, not as
evidence of a cure. Specifically:

1. **Can C2's four output fields encode handedness?** They are attempt identity,
   expected/actual checksum, shape, and execution completion/non-finite status. For each, ask
   whether a value that varies with the galaxy's spin sign could reach it. Checksums are of bytes
   C2 read, not of anything it computed — verify that is actually true in the row's stated surface.
2. **Is "never invokes the classifier" enforced or asserted?** A row in a table is a promise. What
   would fail if C2 did invoke it? Is there a receipt, a pin, or only the sentence?
3. **Does anything downstream reintroduce the channel?** Row D writes χ-bearing receipts into the
   store. Rows C2 and D both touch the same store through row B. Check whether the ordering
   constraint (C2 before D) is enforceable or merely stated, and whether row B's mediation makes
   the separation real.
4. **Is the deferral honest?** Confidence now applies post-unblinding inside a pinned symbol. Does
   the text fix the threshold *before* unblinding? A post-unblinding cut whose threshold is also
   chosen post-unblinding is not a deferral, it is a free parameter.

## The three properties that must not regress

Confirmed held across four passes and two authors. If R5 breaks one, that is blocking regardless
of how well it solves the projection problem:

- the access ban is **universal**, not role-scoped, and bans access rather than disclosure;
- the **hand-check committee can complete** G→H→I without voiding the run it exists to enable;
- the **BS-5f → lock → unblinding** chain remains recordable through named producers.

## New surface R5 introduced — check it as new

R5 creates **BS-2k** (store mediator / log writer pin) and raises the class-P count from twelve to
fourteen. New slots are new prerequisites. Ask whether BS-2k is fillable as specified, whether
anything now depends on a slot that cannot be filled, and whether Part 2's conforming edits are
complete — a repair in §6 that leaves §7 asserting the old counts is the failure mode a linter
caught twice in this document already.

## Context you should have

- Current text: `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md`. §7 is the slot table.
- **BS-2a is REFUSED by all three seats** (`BS2A_REVIEW_{GPT56,CODEX,KIMI}.md`). The reason bears
  directly on this draft: the only confidence quantity that exists is `abs(chi_net)`, frozen at
  `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` line 82, and it **is** handedness amplitude.
  Mirror-evenness does not screen it out, because `abs(chi_net)` is itself mirror-even. R5's row
  C2 is pinned at BS-2a — a refused slot. Say whether that makes C2 unfillable as drafted.
- Prior passes: `SECTION6_DRAFT_{KIMI,KIMI_R2,AGY_R3,AGY_R4}.md` and the six reviews.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch; the 148 GB ceiling
is planning only.

## Verdict

Write `SECTION6_REVIEW_R5_<YOURSEAT>.md` here. Numbered findings, each with severity, the row or
sentence at issue, why it fails, and the smallest sufficient repair. Anything you assert but did
not verify against a file goes under `Testimony`. Final line exactly `**CLEAR**` or
`**NOT CLEAR**` with the blocking findings named.

**Renaming a finding counts as refusing it.** If R5 has renamed rather than repaired, say so in
those words — that judgement is the most useful thing you can return.
