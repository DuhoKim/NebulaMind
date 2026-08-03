# R3 — Tracer-denominator outflow census (Card-2 depth run)

Run ID: `RAMPAGE_R3` · REQ: `REQ_RAMPAGE_R3_20260711T052300Z` · Wave 1
Non-duplication: R1 asks what literature the six cards are missing; R2 collects headline numbers.
R3 is the actual *census methodology* deep-dive for AGN-driven outflows: who measured what, with
which numerator/denominator, and how much of the spread the literature itself attributes to method.
Output is raw/advisory; no local integration during the rampage.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No other
instructions, no follow-up steering; at most ONE neutral "continue" if visibly truncated, logged.

-----BEGIN PASTE REQ_RAMPAGE_R3_20260711T052300Z-----
```markdown
# Deep Research request — Tracer-resolved, common-denominator census of AGN-driven outflow measurements

**Request ID:** `REQ_RAMPAGE_R3_20260711T052300Z`
**Role:** Literature analyst for a galaxy-evolution research journal. Report only published work;
you have no access to the project's internal results.

**Question:** Across the AGN-driven-outflow literature (favor 2018+, seminal earlier anchors
labeled), what has actually been measured per gas phase — hot X-ray wind, warm ionized ([O III],
Hα, UV absorption), neutral atomic (Na I D, H I 21cm/absorption), molecular (CO, OH, HCN) — and how
far does any pair of published incidence or mass-loading numbers share a common denominator?

**Required deliverables (markdown sections, in order):**
1. `## Census table` — one row per study/sample:
   `Study (citation) | Phase/tracer | Sample + selection | N | Incidence or η ± unc | Numerator assumptions (geometry, v-cut, n_e, αCO, r_out) | Denominator (SFR calib/timescale/IMF or M*) | z range | Non-commensurability notes`
2. `## Denominator families` — group the rows into families whose numbers ARE mutually comparable;
   name each family's shared conventions; state explicitly which famous cross-family comparisons in
   the literature are non-commensurable and why.
3. `## Method-vs-physics spread` — what published comparisons/reviews themselves say about how much
   of the order-of-magnitude spread in η is attributable to tracer/assumption choices vs intrinsic
   variation; quote ranges with attribution, never adjudicate in your own voice.
4. `## Proposed common-denominator practice` — practices the literature itself proposes
   (attributed), e.g. matched apertures, uniform SFR tracers, standard velocity cuts.
5. `## What no study provides` — explicit gaps (e.g. a single sample with all four phases at
   matched depth), each line `GAP:` + why current data fall short, with citations or `NONE_FOUND`.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R3 answer — REQ_RAMPAGE_R3_20260711T052300Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Census rows: <N>

- C2 (structure). Exactly the five numbered sections above, in order; an empty field/section says
  `NONE_FOUND`, never silently omitted, never padded.
- C3 (uncertainty). Every number carries the source's uncertainty or
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars.
- C4 (citation labeling). Every study/number carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL) on the same line, or `UNCITED_NOT_USABLE`.
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes". Attributed quotes
  in that register require a checkable citation.
- C6 (estimand labels). Incidence/prevalence numbers carry all four qualifiers (tracer + selection +
  denominator + redshift range); unlike estimands are labeled non-commensurable; no "consistent
  with" claims across unlike estimands. Do not combine tracer-specific fractions (e.g. an ionized
  fraction and a neutral fraction) into any merged population statement.
- C7 (links ledger). Final content section `## Links ledger`:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R3_OUTPUT_DONE_20260711T052300Z

  must appear exactly once, as the standalone final non-empty line of the report body. A marker
  only in a chat-UI element counts as ABSENT and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.
```
-----END PASTE REQ_RAMPAGE_R3_20260711T052300Z-----
