# HARNESS AUDIT R2 — all four of your findings repaired. One of them was inside the audit itself.

Round 1: **NOT CLEAR from both**, four converged findings. Reports in `_harness_r1/`.
**Write to `HARNESS_AUDIT_<YOURSEAT>_R2.md`.**

## First, the answer that mattered, which you both gave: V34 is sound

You independently confirmed `CODEX-V11 3` and `GPT56-V11 F3` resolve to real findings, so **no V34
correction claim was passing only because the old check verified an envelope rather than contents.**
The document was never the problem. Everything below is tooling.

## What was repaired

**1. `check_repair_citations` (both).** Your three counterexamples all held: generic numbered headings
certified `CODEX-V21 F4/F7/F8` against a three-finding report; substring version matching let a
nonexistent `V1` borrow `V11`'s reports; and real list-form findings in `PREREG_TEXT_V12_CODEX` were
rejected. Rebuilt to parse the four declaration grammars actually present here — `### F3`,
`### Finding 3`, `### 3.` under a findings section at the first such heading's depth, and top-level
`N. **…**` list items — with a numeric version boundary.

**My rebuild's first attempt was wrong again, the same way.** I split on headings containing
"finding" and took `sec[1]`; `V24_WHOLE_REVIEW_GPT56` has two such headings, so the scan truncated
after finding 1 and reported the real `GPT56-V24-5` as missing. Anchoring once and scanning to the
end fixed it. **That is four times tonight I have written a pattern narrower than the data. Assume a
fifth and look for it.**

**2. `prereg_trace.self_test()` (CODEX).** You were right and this is the one I most want re-checked:
it proved fixtures could be *constructed*, never invoking the checker. The cause was structural — the
check was inline in `main()`. Factored out as `check_trace()` returning findings; only reporting
moved. Each control now mutates a copy and calls it.

**3. Orphan scan idioms (both).** It saw only bracket emissions. Now both, proved in both directions.

**4. `void_registry` control label (both).** Now says control coverage explicitly, and that it is not
semantic coverage of §6.1's forbidden columns.

## Attack

- **Is `check_trace()` the same logic it replaced?** Only reporting was supposed to move. A
  refactor that silently changed a predicate would be the worst outcome here — compare against
  `_harness_r1/` era behaviour if useful, and confirm V34 still checks 0 problems for the right
  reasons rather than because a branch stopped running.
- **Do the three trace controls fail for the right reason?** Each should produce its own named
  finding, not merely a nonzero count.
- **Is the citation parser now too permissive?** It accepts four grammars. Construct a report where
  a non-finding numbered thing sits under a findings heading.
- **Fifth narrower-than-data instance** — hunt it.
- **Anything I broke while refactoring.** My first factoring attempt corrupted the file's
  indentation and I reverted; the second edited line-wise.

Run every self-test: lint, trace (`--check … --self-test`), void_registry, bs2a_quality_gate,
gain_gradient_estimator, verdict_breakpoints. **Do not take my counts from me.**

## Standing

Two decisions are parked on the principal — `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` and
`OPEN_QUESTION_T_COMPLETENESS.md`. **Do not re-litigate either.** Nothing here fills a slot or
touches BS-6. Final line exactly `**CLEAR**` or `**NOT CLEAR**`.

## Subjects

- `tools/prereg_lint.py` — `522356f1b1d82894b97cd17d98026eb6488c99f6f382e27324777236f9cf4f38`
- `tools/prereg_trace.py` — `9bd194b96a4feeb22e85d07b2a2860a11f6c37bfeeebc3fa891bf55d3f877ae8`
- `tools/void_registry.py` — `f494e5b858a4518bf9299023603e5e82e87eca2bca18a02317ce07790976f1a4`
- `../ref/verdict_breakpoints.py` — `5ed290a61d54a771ff2a346abe867725e40a5373ff37fbbca4a6f4f9a25af93b`
- `../PREREG_SUCCESSOR_DRAFT_V34_20260828.md` — `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` (unchanged)

**Verify all five and state the comparisons.**
