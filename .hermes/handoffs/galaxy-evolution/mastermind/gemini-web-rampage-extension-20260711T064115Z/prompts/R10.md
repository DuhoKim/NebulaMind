# R10 — Tracer/aperture harmonization: methods and before/after numbers

Run ID: `RAMPAGE_R10` · REQ: `REQ_RAMPAGE_R10_20260711T064115Z` · Wave 6
Non-duplication: base run R3 censused the heterogeneous outflow literature and its denominator
families. R10 collects the *fixes*: published cross-calibration and harmonization work, and — the
key deliverable — the numeric before/after shifts when heterogeneous measurements are put on a
common system. Output is raw/advisory.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No steering.
Single neutral "continue" ONLY on visible mid-generation truncation (packet-authorized, logged);
otherwise no follow-ups of any kind.

-----BEGIN PASTE REQ_RAMPAGE_R10_20260711T064115Z-----
```markdown
# Deep Research request — Harmonization of outflow/gas measurements: cross-calibrations, aperture corrections, and before/after shifts

**Request ID:** `REQ_RAMPAGE_R10_20260711T064115Z`
**Role:** Literature analyst for a galaxy-evolution research journal. Published work only; no
access to the project's internal results.

**Question:** What published work re-derives or cross-calibrates AGN-outflow and cold-gas
measurements onto common assumptions — and by how much do the numbers move when it does?

**Required deliverables (markdown sections, in order):**
1. `## Harmonization attempts table` — one row per meta-analysis/re-reduction (favor 2018+):
   `Study (citation) | What was harmonized (velocity cut / n_e diagnostic / geometry / aperture / αCO / SFR calibration) | Input heterogeneity | Common system adopted | BEFORE value(s) ± unc | AFTER value(s) ± unc | Shift magnitude as stated by the source`
   The BEFORE/AFTER columns are the point of this request: cases where the source itself quotes how
   a rate, loading factor, incidence, or gas mass changed under re-derivation.
2. `## Aperture and beam corrections` — published methods for matching IFU/fiber/slit apertures and
   radio/mm beams across samples; the correction sizes each source quotes.
3. `## Density and conversion diagnostics` — published comparisons of electron-density diagnostics
   ([S II] vs auroral vs trans-auroral vs IR) and αCO choices, with the factor-level impact each
   source assigns to outflow masses/rates.
4. `## Velocity-cut and decomposition conventions` — published sensitivity analyses of
   outflow-definition choices (fixed velocity cut vs kinematic decomposition), with quoted impacts.
5. `## Residual irreducibles` — after harmonization, what spread the sources say remains and what
   they attribute it to (attributed only).
6. `## Recipes the literature converges on` — explicitly proposed common-reporting standards
   (attributed, cited); `NONE_FOUND` if none.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R10 answer — REQ_RAMPAGE_R10_20260711T064115Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Harmonization rows: <N>

- C2 (structure). Exactly the six numbered sections above, in order; empty fields say `NONE_FOUND`,
  never silently omitted, never padded.
- C3 (uncertainty). Every number carries the source's uncertainty or
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars; never compute your own before/after
  shifts — only quote shifts the sources themselves state.
- C4 (citation labeling). Every study/number carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL) on the same line, or `UNCITED_NOT_USABLE`.
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes".
- C6 (estimand labels). Before/after pairs are commensurable only within one study's stated
  re-derivation; cross-study shifts are non-commensurable and must be labeled so; four qualifiers
  on every incidence/prevalence number.
- C7 (links ledger). Final content section `## Links ledger`, one line per cited item:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R10_OUTPUT_DONE_20260711T064115Z

  must appear exactly once, as the standalone FINAL non-empty line of the report body. Nothing may
  follow it — no "End of Report", no sign-off. A marker only in a chat-UI element counts as ABSENT
  and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

Final reminder: the last non-empty line of your report must be exactly
`GEMINI_WEB_RAMPAGE_R10_OUTPUT_DONE_20260711T064115Z` with no text after it.
```
-----END PASTE REQ_RAMPAGE_R10_20260711T064115Z-----
