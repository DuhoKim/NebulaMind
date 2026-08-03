# R8 — Matched-estimand redshift-evolution tables

Run ID: `RAMPAGE_R8` · REQ: `REQ_RAMPAGE_R8_20260711T064115Z` · Wave 5
Non-duplication: base run R2 built a static published-values envelope. R8 builds *evolution with
redshift* series — but ONLY where the literature keeps the estimand fixed along the series. It is a
matching-discipline exercise, not another envelope. Output is raw/advisory.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No steering.
Single neutral "continue" ONLY on visible mid-generation truncation (packet-authorized, logged);
otherwise no follow-ups of any kind.

-----BEGIN PASTE REQ_RAMPAGE_R8_20260711T064115Z-----
```markdown
# Deep Research request — Matched-estimand redshift evolution of feedback/quenching quantities

**Request ID:** `REQ_RAMPAGE_R8_20260711T064115Z`
**Role:** Literature analyst for a galaxy-evolution research journal. Published work only; no
access to the project's internal results.

**Core rule of this request:** an "evolution" claim is admissible ONLY if every point in the series
uses the same estimand: same definition (e.g. same quiescence criterion), same tracer, same
denominator, comparable selection. Series that mix definitions must be either excluded or reported
in the violations section — never merged.

**Quantities (E1–E6):**
- E1: Quenched/quiescent fraction at fixed stellar mass vs z (state the quiescence definition per series).
- E2: Molecular gas fraction and depletion time of the QUIESCENT population vs z (tracer and
  conversion stated per series).
- E3: Molecular gas fraction / t_dep scaling relations of the STAR-FORMING population vs z (as the
  comparison baseline; name the compilation).
- E4: AGN-driven outflow incidence at matched selection vs z (per tracer; only same-survey or
  explicitly harmonized series).
- E5: Radio-AGN fraction at fixed stellar/halo mass vs z.
- E6: Metallicity-relation (MZR/FMR) normalization and scatter vs z up to z≈2.3; results claimed
  beyond z≈2.3 are reportable ONLY as labeled leads, flagged as beyond the project's locally
  anchored scope.

**Required deliverables (markdown sections, in order):**
1. `## E<k> series tables` (one subsection per quantity E1–E6) — one row per series point:
   `Series ID | z | Value ± uncertainty | Estimand definition (criterion/tracer/denominator) | Sample + selection | Citation`
   Group rows by Series ID; a series = one internally consistent estimand.
2. `## Definition drift register` — for each quantity, where the literature's common narrative
   stitches together points with different definitions; name the papers on each side.
3. `## Violations gallery` — published examples of mixed-estimand evolution claims that later
   papers criticized, with both citations and the critic's stated reason.
4. `## Commensurable envelope summaries` — per quantity, the evolution range supported by
   single-estimand series only; `NONE_FOUND` where no clean series exists.
5. `## Gaps` — `GAP:` lines for quantities/z-ranges with no single-estimand series, cited or `NONE_FOUND`.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R8 answer — REQ_RAMPAGE_R8_20260711T064115Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Series count: <N>

- C2 (structure). Exactly the five numbered sections above, in order; empty fields say `NONE_FOUND`,
  never silently omitted, never padded.
- C3 (uncertainty). Every value carries the source's uncertainty or
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars.
- C4 (citation labeling). Every value/study carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL) on the same line, or `UNCITED_NOT_USABLE`.
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes". Evolution trends
  are reported as what specific series show, attributed, never as settled population facts.
- C6 (estimand labels). The core rule above IS the estimand contract: cross-series comparisons are
  non-commensurable unless a cited harmonization exists; every fraction carries tracer + selection +
  denominator + redshift range.
- C7 (links ledger). Final content section `## Links ledger`, one line per cited item:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R8_OUTPUT_DONE_20260711T064115Z

  must appear exactly once, as the standalone FINAL non-empty line of the report body. Nothing may
  follow it — no "End of Report", no sign-off. A marker only in a chat-UI element counts as ABSENT
  and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

Final reminder: the last non-empty line of your report must be exactly
`GEMINI_WEB_RAMPAGE_R8_OUTPUT_DONE_20260711T064115Z` with no text after it.
```
-----END PASTE REQ_RAMPAGE_R8_20260711T064115Z-----
