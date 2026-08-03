# R14 — Quenching-predictor head-to-head census (structural vs BH vs halo)

Run ID: `RAMPAGE_R14` · REQ: `REQ_RAMPAGE_R14_20260711T064115Z` · Wave 7
Non-duplication: base R1/R1b critique card 1 (isolating AGN's causal contribution) at the
review level. R14 censuses the actual head-to-head *predictor-comparison studies* — the
"which variable best predicts quiescence" literature that the pilot's open predictor debate
(halo vs central properties) rests on. Output is raw/advisory.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No steering.
Single neutral "continue" ONLY on visible mid-generation truncation (packet-authorized, logged);
otherwise no follow-ups of any kind.

-----BEGIN PASTE REQ_RAMPAGE_R14_20260711T064115Z-----
```markdown
# Deep Research request — Head-to-head comparisons of quenching predictors: central structure, black-hole proxies, halo mass, environment

**Request ID:** `REQ_RAMPAGE_R14_20260711T064115Z`
**Role:** Literature analyst for a galaxy-evolution research journal. Published work only; no
access to the project's internal results. The predictor question is OPEN for this program: your
job is the census of comparisons, not a winner.

**Required deliverables (markdown sections, in order):**
1. `## Comparison-study table` — one row per published head-to-head (favor 2018+, seminal anchors
   labeled):
   `Study (citation) | Dataset | Population (centrals/satellites/all; z range) | Predictors compared (e.g. σ_c, Σ1, M_BH or proxy, B/T, M*, M_halo, environment) | Method (random forest / partial correlation / conditional demographics / other) | Reported ranking or effect sizes ± unc | Quiescence definition | Caveats named by the study`
2. `## Method critiques` — published methodological objections: correlated-predictor degeneracy,
   halo-mass estimation circularity (group catalogs built from the same photometry), M_BH proxy
   indirectness, ML feature-importance instability — each attributed and cited.
3. `## Simulation-based predictor tests` — studies running the same predictor comparisons inside
   simulations (where the true cause is known by construction): what they report about method
   reliability, explicitly labeled model-scope.
4. `## Centrals vs satellites split` — where rankings differ by population, per the sources.
5. `## Convergences and reversals` — predictor rankings that replicate across ≥2 independent
   datasets/methods vs published reversals (A beats B in one study, B beats A in another), all
   attributed, with each study's estimand differences spelled out.
6. `## Discriminating data needs` — what the comparison papers themselves say would break the
   remaining degeneracies (e.g. direct M_BH samples, weak-lensing halo masses at scale), cited.
7. `## Gaps` — `GAP:` lines, cited or `NONE_FOUND`.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R14 answer — REQ_RAMPAGE_R14_20260711T064115Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Comparison rows: <N>

- C2 (structure). Exactly the seven numbered sections above, in order; empty fields say
  `NONE_FOUND`, never silently omitted, never padded.
- C3 (uncertainty). Every effect size/number carries the source's uncertainty or
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars.
- C4 (citation labeling). Every study/number carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL) on the same line, or `UNCITED_NOT_USABLE`.
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes". Predictive
  ranking is not causal ordering: any causal reading stays attributed to its source. Do not declare
  a winning predictor in your own voice.
- C6 (estimand labels). Rankings under different quiescence definitions, populations, or z ranges
  are non-commensurable: label them; four qualifiers on every quoted fraction.
- C7 (links ledger). Final content section `## Links ledger`, one line per cited item:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R14_OUTPUT_DONE_20260711T064115Z

  must appear exactly once, as the standalone FINAL non-empty line of the report body. Nothing may
  follow it — no "End of Report", no sign-off. A marker only in a chat-UI element counts as ABSENT
  and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

Final reminder: the last non-empty line of your report must be exactly
`GEMINI_WEB_RAMPAGE_R14_OUTPUT_DONE_20260711T064115Z` with no text after it.
```
-----END PASTE REQ_RAMPAGE_R14_20260711T064115Z-----
