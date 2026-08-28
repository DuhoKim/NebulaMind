# HARNESS AUDIT — three of my checks claimed more than they tested. Verify the repairs.

Prompted by a finding in a sister lane: both its seats found a check whose NAME asserted more than
its PREDICATE evaluated. I audited my six harnesses for the same shape and found three. **All three
are in tools I built to catch exactly this class in documents**, which is why I want them checked
rather than taken on my word.

## Subjects

- `/Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py` — `5090a694690446ade672bcc8d35e523425bac2660514d7a5ed586524b5a99d48`
- `/Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py` — `b8ef412e3df842068a5105d8f0f72a4e01bacef3aa82f6a11b1e717b60aaa658`
- `../ref/verdict_breakpoints.py` — `2fcd43a121ced22a34262dafd3020d90989ea8e36fa240b1589ddd3a2505ed1f`
- `../PREREG_SUCCESSOR_DRAFT_V34_20260828.md` — `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` (unchanged; the certification subject)

**Verify all four and state the comparisons.** Write to `HARNESS_AUDIT_<YOURSEAT>.md`.

## The three, and why the first is the one that matters

**1. `check_repair_citations` verified the envelope, not the contents.** Its docstring claimed a
`V## CORRECTION (SEAT-Vn Fk)` claim "must cite a finding that exists on disk". The predicate only
checked that a **report file** for that seat and version existed; `fid` was parsed and used solely
in the error message. **A citation to `CODEX-V27 F9` passed against a report with four findings.**

The check's own docstring argues a sentence announcing a repair is the document's most dangerous,
because a reader stops checking there. **This check certified V29 through V34 under that weakness.**
It now requires the cited finding number to be present in that seat's report.

**This is the question I most want answered: does V34 still certify honestly under the stronger
check, and were any of its correction claims passing only because the old check was weak?**

**2. `void_registry.py` V05/V06 were named for coverage and tested a naming convention.** They match
the `VOID-6.1<ROW>-` prefix, which proves a row is *named*, not that the antecedent covers that
row's forbidden column. Renamed to "no antecedent ID names it"; the module now says **NAME-complete**
and states that semantic coverage is not computable and not claimed.

**3. `verdict_breakpoints.py` declared `T03` and no runtime path emitted it.** Removed, and
`self_test()` now computes its own orphan set and fails if any declared code is unemitted. I proved
that check can fail by reintroducing a synthetic code.

## Attack

- **Is the strengthened citation check correct, or is it now too strict?** My first attempt accepted
  only `### 3.` headings and reported a **real** citation as missing, because the V11 reports use
  `### F3 — BLOCKER`. **I have made a pattern narrower than the data three times tonight.** Assume
  I have done it again and look for the case.
- **Does it still catch a fabrication?** `GPT56-V11 F97` should be rejected naming the real numbers.
- **Are the renames honest, or did I merely relabel a weak check to sound acceptable?** A rename that
  makes a check sound smaller without making the claim true is its own defect.
- **Does the orphan check hold across both emission idioms** — `refuse("X01", ...)` and direct
  bracket append? My first audit pass used one and produced a false positive.
- **Are there instances I missed?** Six harnesses: `prereg_lint`, `prereg_trace`, `void_registry`,
  `bs2a_quality_gate`, `gain_gradient_estimator`, `verdict_breakpoints`.

Run: lint on V34 with `--gates .` and `--self-test`; `prereg_trace --check`; `void_registry`
and its `--self-test`; `verdict_breakpoints --self-test`. **Do not take my counts from me.**

## Standing

Nothing here fills a slot or touches BS-6. Two decisions are parked on the principal in
`OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` and `OPEN_QUESTION_T_COMPLETENESS.md`; do not
re-litigate either. Final line exactly `**CLEAR**` or `**NOT CLEAR**`.
