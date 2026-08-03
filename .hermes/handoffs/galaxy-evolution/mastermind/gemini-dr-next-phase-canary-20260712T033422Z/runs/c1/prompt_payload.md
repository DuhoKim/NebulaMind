# Deep Research request — Calibration targets vs out-of-sample validations for major galaxy-formation simulations

**Request ID:** `REQ_JOINT_C1_20260711T100139Z`
**Role:** Literature analyst for a galaxy-evolution research journal. Published work only; no
access to the journal's internal results.

**Question:** For each major galaxy-formation simulation project (IllustrisTNG, EAGLE, SIMBA,
FIRE, ROMULUS, ASTRID, FLAMINGO, and comparable published suites), what do the METHOD papers state
was used to calibrate the feedback/subgrid model — and which later observation comparisons are
genuinely out-of-sample (not calibration targets, per the papers themselves)?

**Required deliverables (markdown sections, in order):**
1. `## Calibration ledger` — one row per simulation:
   `Simulation (method-paper citation) | Stated calibration targets (observable + dataset, faithful to the source wording) | Feedback parameters tuned (as stated) | Explicitly emergent (stated NOT calibrated) | Notes`
   Only what method papers/official documentation state; where ambiguous, write
   `AMBIGUOUS_IN_SOURCE` and quote the sentence.
2. `## Out-of-sample validation ledger` — published comparisons the authors or independent groups
   explicitly frame as predictions/out-of-sample tests: simulation, observable, result
   (agreement/tension, magnitude ± uncertainty), overlap with any section-1 calibration target,
   citation.
3. `## Double-counting warnings` — published critiques warning against counting calibration
   targets as evidence of feedback-model correctness (attributed, cited).
4. `## Feedback-relevant observables map` — for observables central to AGN-feedback/quenching
   debates (quenched fractions, gas fractions of passive galaxies, outflow demographics,
   hot-halo/cavity properties, radio-AGN incidence): per simulation, mark
   `CALIBRATED / EMERGENT / NOT_REPORTED`, each cell backed by a section-1/2 citation or `NONE_FOUND`.
5. `## Gaps` — `GAP:` lines (simulations without public calibration statements; observables with
   no published out-of-sample test), cited or `NONE_FOUND`.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Joint C1 answer — REQ_JOINT_C1_20260711T100139Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Simulations covered: <N>

- C2 (structure). Exactly the five numbered sections above, in order; empty fields say
  `NONE_FOUND`, never silently omitted, never padded.
- C3 (uncertainty). Every number carries the source's uncertainty or
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars.
- C4 (citation labeling). Every statement about a simulation's calibration or validation carries a
  checkable citation (arXiv ID, DOI, ADS bibcode, or URL — official simulation documentation URLs
  count) on the same line, or `UNCITED_NOT_USABLE`.
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes". "Simulation X
  validated / ruled out" is banned in your own voice; agreement/tension statements stay
  per-observable and attributed. Simulation-only results are model-scope, never observed prevalence.
- C6 (estimand labels). Simulation medians vs observed selection-shaped statistics are
  non-commensurable unless the cited work matched selections; label every such pairing; every
  quoted fraction carries tracer/selection/denominator/redshift qualifiers where applicable.
- C7 (links ledger). Final content section `## Links ledger`, one line per cited item:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_JOINT_C1_OUTPUT_DONE_20260711T100139Z

  must appear exactly once, as the standalone FINAL non-empty line of the report body. Nothing may
  follow it — no "End of Report", no sign-off, no blank-line-then-text. A marker only in a chat-UI
  element counts as ABSENT and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

Final reminder: the last non-empty line of your report must be exactly
`GEMINI_WEB_JOINT_C1_OUTPUT_DONE_20260711T100139Z` with no text after it.