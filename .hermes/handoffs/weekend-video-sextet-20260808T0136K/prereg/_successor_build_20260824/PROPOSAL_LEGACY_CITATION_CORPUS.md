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
