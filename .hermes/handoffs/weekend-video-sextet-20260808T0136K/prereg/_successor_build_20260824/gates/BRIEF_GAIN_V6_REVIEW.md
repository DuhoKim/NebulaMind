# GAIN v6 — SCOPED. Your finding 1 is parked on a human; do not re-litigate it.

**Read this scope line first.** Your v5 finding that production `p` is not a function of `|A|`
**stands, is accepted, and is parked** on a human decision recorded in
`OPEN_QUESTION_T_COMPLETENESS.md`. The p-to-A reduction is dead; the refutation is at the top of
`verdict_breakpoints.py` and §4 of the design is marked REFUTED and OPEN. **Do not spend this round
re-deriving it.** If you find the parking itself dishonest, say so in one finding and move on.

**This round asks one thing: do the repairs to your OTHER v5 findings hold, and did they break
anything?** Those repairs survive whichever way the parked fork is decided, so clearing them now is
not wasted work.

## Subjects

- `../ref/gain_gradient_estimator.py` — `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd`
- `verify_mu_gamma.py` — `e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04`
- `../ref/verdict_breakpoints.py` — `712b535d43890f327a1da3c7de183cf1ef839ed3b17f86ba6c06b3411d67e707`
- `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` — `1c3ced94086be0f1995a71435ee59dff8a0d84633c44593adcc73d6c434b1f20`

**Verify all four and state the comparisons.** Write to `GAIN_V6_REVIEW_<YOURSEAT>.md`.

## What was repaired

1. **Not every `numpy.linalg` call was wrapped** (GPT56). `eigvalsh(S)` and `matrix_rank(X)` sat
   outside the `try`, so the result-or-refusal contract was literally false. Both are now inside.
2. **`recipe_gamma()` was never repaired** (CODEX) — v4's finding was about that function, and v5
   found `simulate()` had gained guards while it had not. All three of your exact attacks now
   refuse: `gamma=0.251` → per-object accuracy reaches `1.000396`; `gamma=0.30` → `1.019995`;
   `gamma=nan` → non-finite parameter. **I had fixed the guard one function away and reported the
   class closed. Check I have not done it again.**
3. **The design still described the v4 contract** (GPT56) — G08 unreachable, eight codes, `T`
   deferred. Now 9 codes, nothing exempt, `G09` documented, and §4 marked REFUTED/OPEN.
4. **The transcription check was vacuous** (GPT56) — it compared `verdict_at()` against another
   local restatement of the same `if/elif`. It now calls **`v9._decide_from()`** and takes
   `sigma_comb`, `sigma_ours_band` and `evaluated_floor` out of the returned record rather than
   supplying my own. 48 `(A, p)` points. **This is the repair I am least sure of — attack it.**
   Building it surfaced that `adjudicate_path` raises `InconclusiveByCalibration` below
   `A_FLOOR = 0.85`; the fixture now clears it.

## Attack

- **Is the transcription check real now, or merely differently circular?** It is a scalar-path
  fixture with a stub mask. Does that fixture exercise the branch production would take?
- **Did wrapping every linalg call change any refusal code**, or mask a case that used to refuse
  distinctly?
- **Is `recipe_gamma`'s guard the same guard as `simulate`'s**, or a third variant that will drift?
- **Does the design now match the code exactly?** It has been wrong in this way twice.
- Run both self-tests: estimator (9/9 codes, 0 failures), verifier (10 in-domain, 5 domain
  controls, 0 failures), breakpoints (0 failures). **Do not take those from me.**

## Standing

`γ̂` unmeasured; control **DESIGN, defined, UNFILLED**. BS-2a's quality-predicate component cleared
at round 6 and is pinned in V34 with its limit; the slot stays UNFILLED. **BS-6 and the first image
byte remain blocked.** Do not read `/Users/duhokim/NebulaMindData/`.

Final line exactly `**CLEAR**` or `**NOT CLEAR**`, where CLEAR means *these repairs hold* — not that
the control is freezeable, which the parked fork decides. Budget iterations so the report is written.
