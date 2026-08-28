# REFEREE BRIEF — V29, SAME BYTES, second round. The tooling changed; the document did not.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V29_20260827.md`**, sha256
`542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343` — **byte-identical to the draft
you reviewed.** Verify and state the comparison.

## Why you are seeing the same bytes again

**No V30 was written, deliberately.** CODEX's single V29 blocker had **no document repair** — its
smallest sufficient repair named `_mut_repair_citation`, `CONTROLS` and a regression assertion, all
in `tools/prereg_lint.py`. V29 makes no claim about linter coverage anywhere. Issuing a V30 would
have been a version bump with no content delta.

**GPT56 returned CLEAR on these bytes.** CODEX's objection was to a tool. The tool is fixed:

1. **A sixth negative control** — `_mut_repair_citations` cites a finding whose report does not
   exist, so `check_repair_citations` must now prove it can fire like the other five.
2. **Coverage is computed, not asserted.** `CHECKS_RUN` lists what `main()` executes; the clean line
   reads `all 6 checks demonstrated they can fail`, and names any executed-but-uncontrolled check.
   Removing a control makes it report `5 of 6 … UNCONTROLLED: <name>` instead of claiming coverage.
3. **`--self-test`**, the regression assertion CODEX asked for: every control must fire and no
   executed check may be uncontrolled, exit 1 otherwise. A genuinely broken check exits **1**, not a
   printed warning.

**Run all of it yourself** — `prereg_lint.py`, `--self-test`, and `prereg_trace.py --check`. Report
what you get. My account of a tool result has been wrong twice today and both of you caught it; it
should carry no weight here.

## What is being asked

**Is there any remaining objection to the document?** Not to my tooling — that is now separately
testable and you should test it — but to the preregistration text itself.

If your V29 findings are addressed and the prose stands, say **CLEAR**. If something in the document
remains wrong, say what. **Do not clear it because the tooling was the only blocker last time** —
re-read the text, apply clause 10 in both directions, sweep the thresholds, read the neighbours.

## Standing state, unchanged

**BS-2a DESIGN/UNFILLED. One of fifteen class-P slots filled.** BS-2v UNRESOLVED; findings 1, 2, 2b
and 3 UNRESOLVED; rows C2 and E cannot run; **Stage P `SUPERSEDED / NON-APPLICABLE TO THE 49,211
MASK`, BS-5p unfillable pending rerun**; **BS-6 and the first image byte remain blocked.** No image
byte fetched or authorised. **§2.7 line 378 unchanged.**

A CLEAR here means *this is a correct preregistration that is honest about being an unfinished
programme* — not that the study may proceed. If that distinction is not what the document conveys,
that itself is a finding.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`V29_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.**
