# PROPOSAL for Blanc → Duho — the pre-block citation corpus is 94 citations, not ~30 reports

**Written 2026-08-29 10:35 KST. Duho ruled option C ("fix it so checker actually read it") but did
NOT rule on the existing corpus. This is the proposal he asked for, with the size measured rather
than estimated.**

## The checker is built and works

`tools/citation_block_check.py` reads `FINDINGS-BLOCK v1` and nothing else. 12 controls, 0 failures;
all four outcomes pinned by at least one control; **the deletion probe detects removal of all four,
including `VERIFIED`** — the branch the previous check could never detect losing. Verified live: it
returns `VERIFIED` for `GPT56-V38 F1` against this morning's real report.

**Not yet wired into `prereg_lint.py`**, deliberately — the V38 round was live and the brief told both
seats exactly how the lint behaves, so changing it mid-round would have been modifying a subject
under review.

## The measured size

I classified every citation in V38 against its report on disk:

    citations in V38:  94
    NO_BLOCK:          94   (100%)

**Every citation in the document points at a report that predates the block.** The corpus is not ~30
reports to be spot-checked; it is 94 individual claims, none of which the new checker can verify and
none of which it will call fabricated. It reports them as `NO_BLOCK` — a fourth outcome kept separate
from `UNVERIFIABLE` precisely so a pending human decision cannot hide inside a parse failure.

## The options

**A. Hand-verify all 94 at freeze.** *My reading, and still is.* It is bounded, one-time, and happens
at the only moment correctness matters. *Cost:* real human minutes, and no regression protection
between now and freeze.

**B. Retrofit blocks onto the ~30 historical reports.** Machine-verifiable forever after. *Cost:*
somebody must decide, for each old report, which numbered items were findings — **the exact unencoded
judgement that sank three versions of the old checker.** Retrofitting means making that judgement now,
for reports whose authors are gone, and freezing it as fact. I would not trust my own retrofit.

**C. Accept `NO_BLOCK` permanently as an honest gap.** Cheapest and truthful. *Cost:* 94 citations
stay unverified forever, and the document's most dangerous sentence — one announcing a repair — is
exactly the kind the check existed to guard.

**D. Verify only citations that carry a repair announcement**, not every mention. Narrows the 94 to
the load-bearing subset. *Cost:* requires agreeing which sentences are load-bearing, which is a
smaller version of B's problem — but a much smaller one, and it is mine to draft rather than guess.

## Recommendation

**A, with D as the way to scope it.** Hand-verify at freeze, and use D to order the work so the
repair-announcing citations are verified first and the incidental mentions last. **I am not choosing
between them** — the corpus disposition was explicitly not ruled on, and 94 is large enough that the
cost of A is a real call about someone's time, not a detail.

**Not in doubt:** no draft defect is implied by any of this. The failure was always in the tool.

---

# UPDATE 2026-08-29 12:15 KST — the hand-verification burden is 11 citations, not 94

**Option D said the 94 could be narrowed to the load-bearing subset, and that the scoping was mine to
draft rather than guess. Drafted, and it changes the decision materially.**

## Structure, not vocabulary

My first attempt classified citations by whether the sentence carried repair language
(`CORRECTION`, `repaired`, `corrected`). **It returned 2, and that number was wrong** — a narrow
pattern used in the *absence* direction, which is the unsound move this whole tool exists to stop
making. I did not ship it. There is exactly **one** `CORRECTION` construction in the document, so the
risk was never concentrated in a keyword.

The honest split is structural. Of **104** citations in V41:

| where | count | what the citation does |
|---|---|---|
| **§10's changelog table** | **88** | one column of a transition row — *"this revision answered these findings"*. A uniform, bulk-checkable record. |
| **prose** | **16** | embedded inside an argument, where a reader stops checking because a finding is named. |

## Five of the sixteen are already machine-verified

Their reports carry `FINDINGS-BLOCK v1`, so I ran them rather than asserting it:

    CODEX-V38 F1  VERIFIED     CODEX-V38 F3  VERIFIED     GPT56-V40 F6  VERIFIED
    CODEX-V38 F2  VERIFIED     CODEX-V38 F4  VERIFIED

**That leaves 11 pre-format prose citations** — at lines 31 (x2), 66, 67 (x2), 120, 276, 277,
358 (x2) and 520 — pointing at V11, V24 and V34 reports.

## What that does to the options

**Option A costs 11 careful reads, not 94.** At the outside an hour, at the one moment it matters,
covering every citation embedded in an argument.

**The 88 changelog rows are a smaller and different problem.** A wrong row misrecords history; a
wrong prose citation misleads a reader mid-argument. They are uniform enough to verify in bulk later,
or to leave as `repair-citation-legacy` advisories permanently without much risk.

**Revised recommendation: A, scoped to the 11.** Everything new is machine-verified going forward,
five of the sixteen verified themselves the moment the format landed, and the residue is small enough
that the honest answer is to read it rather than build anything further.

**Still not my decision.** The corpus was explicitly not ruled on, and eleven careful reads is still
someone's time.
