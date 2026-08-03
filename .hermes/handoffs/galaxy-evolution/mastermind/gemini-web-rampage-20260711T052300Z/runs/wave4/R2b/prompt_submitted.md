# R2 — Cycle-9 quantitative prior-work comparison envelope

Run ID: `RAMPAGE_R2` · REQ: `REQ_RAMPAGE_R2_20260711T052300Z` · Wave 1
Purpose (operator side, not pasted as extra steering): the pilot's cycle-9 audit rejects partly on
a missing **prior-work comparison** gate. This run builds the published-values envelope the
journal's comparison section can later be checked against. Non-duplication: R1 critiques the six
cards; R2 collects *numbers only*. Output is raw/advisory; no local integration during the rampage.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No other
instructions, no follow-up steering; at most ONE neutral "continue" if visibly truncated, logged.

-----BEGIN PASTE REQ_RAMPAGE_R2_20260711T052300Z-----
```markdown
# Deep Research request — Quantitative prior-work envelope for galaxy-evolution feedback/quenching quantities

**Request ID:** `REQ_RAMPAGE_R2_20260711T052300Z`
**Role:** You are compiling a literature-values table ("prior-work envelope") for a research-journal
project on galaxy evolution (AGN feedback, quenching, gas cycling). You have NO access to the
project's own results and must not guess or invent them: report ONLY published values.

**Task:** For EACH quantity Q1–Q8 below, tabulate at least 3 independent published measurements or
estimates (prefer 2020+; seminal earlier anchors allowed and labeled as such), so a later reader can
judge whether any new value sits inside or outside the published envelope.

- Q1: Incidence/prevalence of ionized AGN-driven outflows (survey samples, e.g. IFU/long-slit),
  per tracer and selection.
- Q2: Incidence/prevalence of neutral (e.g. Na I D, H I) AGN-driven outflows, per tracer and selection.
- Q3: Mass-loading factors (η = outflow rate / SFR) by gas phase (ionized, neutral, molecular),
  including the assumptions that set the numerator (geometry, velocity cut, electron density) and
  denominator (SFR calibration, timescale, IMF).
- Q4: Molecular gas fractions and depletion times of quenched/quiescent vs star-forming galaxies at
  z≈0 and z≈0.5–2 (state αCO or dust-based assumptions).
- Q5: X-ray cavity power vs cooling luminosity balance (P_cav/L_cool) in groups/clusters, and the
  fraction of cool-core systems with detected cavities.
- Q6: Radio-AGN / maintenance-mode duty-cycle estimates as a function of stellar or halo mass.
- Q7: Mass–metallicity / fundamental-metallicity-relation scatter and evolution to z≈2.3 (and, as
  labeled leads only, claims beyond z≈2.3).
- Q8: z>10 galaxy abundance / stellar-mass tension figures (UV luminosity density, quoted masses)
  as presented by both "tension" and "no-tension" analyses.

**Table columns (one table per quantity, markdown):**
`Value ± uncertainty | Definition/estimand | Tracer | Selection/sample | Denominator (if ratio) | Redshift range | Instrument/survey | Citation`

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R2 answer — REQ_RAMPAGE_R2_20260711T052300Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Quantities addressed: <N> of 8

- C2 (structure). One `## Q<n> — <short title>` section per quantity, ascending, each containing the
  table plus `### Q<n>.a Definition conflicts` and `### Q<n>.b Envelope summary` (min–max of
  commensurable values only). A quantity with nothing found gets its skeleton with `NONE_FOUND`.
- C3 (uncertainty). Every value carries the source's uncertainty, or the explicit label
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars.
- C4 (citation labeling). Every value/study carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL) on the same line, or the same-line label `UNCITED_NOT_USABLE`.
- C5 (wording contract). In your own voice, settled/causal register is banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes". Disagreements
  between sources are reported as attributed claims, never adjudicated in your own voice.
- C6 (estimand labels). Values with different definitions/denominators/selections are
  non-commensurable: label them so, and exclude them from envelope min–max summaries. Every
  incidence/prevalence number carries all four qualifiers: tracer + selection + denominator +
  redshift range.
- C7 (links ledger). Final content section `## Links ledger`, one line per cited item:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R2_OUTPUT_DONE_20260711T052300Z

  must appear exactly once, as the standalone final non-empty line of the report body. A marker
  only in a chat-UI completion element counts as ABSENT and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.
```
-----END PASTE REQ_RAMPAGE_R2_20260711T052300Z-----
