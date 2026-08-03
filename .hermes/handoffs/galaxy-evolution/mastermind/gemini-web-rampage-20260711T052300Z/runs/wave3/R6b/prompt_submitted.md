# R6 — Simulation forward-modeling and selection effects (Card-5 depth run)

Run ID: `RAMPAGE_R6` · REQ: `REQ_RAMPAGE_R6_20260711T052300Z` · Wave 2
Non-duplication: R1 critiques the cards; R2 collects headline numbers. R6 maps how simulation
feedback predictions are (and are not) forward-modeled into observables, and what selection effects
published comparisons say they suffer. Output is raw/advisory; no local integration during the rampage.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No other
instructions, no follow-up steering; at most ONE neutral "continue" if visibly truncated, logged.

-----BEGIN PASTE REQ_RAMPAGE_R6_20260711T052300Z-----
```markdown
# Deep Research request — Forward-modeled simulation-vs-observation comparisons of feedback predictions: pipelines, selection effects, biases

**Request ID:** `REQ_RAMPAGE_R6_20260711T052300Z`
**Role:** Literature analyst for a galaxy-evolution research journal. Published work only; no
access to the project's internal results.

**Question:** For the major galaxy-formation simulations (e.g. IllustrisTNG, EAGLE, SIMBA, FIRE,
ROMULUS, and successors), which feedback-relevant predictions have been compared to observations
through genuine forward modeling (mock observables incl. selection functions), which only through
raw simulation statistics, and what biases do the forward-modeling papers themselves quantify?

**Required deliverables (markdown sections, in order):**
1. `## Observable-pipeline map` — one row per observable relevant to AGN feedback/quenching
   (outflow incidence & rates per phase, quenched fractions, molecular gas fractions & t_dep of
   passive galaxies, X-ray cavities/hot-halo properties, radio-AGN fractions, sSFR distributions):
   `Observable | Forward-model required (mock spectra/cubes, radiative transfer, CO modeling, X-ray/radio mocks) | Published mock-based comparisons (citations) | Raw-statistics-only comparisons (citations) | Biases quantified by the sources (with magnitudes ± unc where given)`
2. `## Selection-function ledger` — for each compared survey named by these papers, the concrete
   selection effects modeled vs ignored (flux/surface-brightness limits, aperture, resolution
   (beam/PSF), detection thresholds, sample matching), as stated by the sources.
3. `## Per-observable discrimination power` — which observables the literature says actually
   discriminate between feedback implementations, with the quoted residuals vs stated
   uncertainties; global "simulation X is validated/ruled out" rankings are banned in your own
   voice and reportable only as attributed claims.
4. `## Public data products` — which public simulation data releases expose the fields needed for
   the above mocks (with links); `NONE_FOUND` where a needed field is not public.
5. `## Known failure modes` — cases where a raw-statistics comparison and a forward-modeled
   comparison of the same quantity disagreed, with each paper's numbers and explanation, quoted
   with attribution.
6. `## Gaps` — `GAP:` lines for observables with no published forward-modeled comparison, with
   citations or `NONE_FOUND`.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R6 answer — REQ_RAMPAGE_R6_20260711T052300Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Observables mapped: <N>

- C2 (structure). Exactly the six numbered sections above, in order; empty fields say `NONE_FOUND`,
  never silently omitted, never padded.
- C3 (uncertainty). Every number carries the source's uncertainty or
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars.
- C4 (citation labeling). Every study/number carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL) on the same line, or `UNCITED_NOT_USABLE`.
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes". Simulation-only
  statements are model-scope demonstrations, never observed prevalence, in your own voice.
- C6 (estimand labels). Simulation absolute medians vs observed selection-shaped distributions are
  unlike estimands: label non-commensurable unless the source itself matched selections; no
  "remarkably close / consistent with" across unlike estimands; four qualifiers on every fraction.
- C7 (links ledger). Final content section `## Links ledger`:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R6_OUTPUT_DONE_20260711T052300Z

  must appear exactly once, as the standalone final non-empty line of the report body. A marker
  only in a chat-UI element counts as ABSENT and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.
```
-----END PASTE REQ_RAMPAGE_R6_20260711T052300Z-----
