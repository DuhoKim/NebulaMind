# R11 — Literature contradiction map for the six-card domain

Run ID: `RAMPAGE_R11` · REQ: `REQ_RAMPAGE_R11_20260711T064115Z` · Wave 6
Non-duplication: base runs collected censuses and envelopes with "Disagreements" subsections. R11
is a dedicated, structured contradiction map across the whole domain — the direct input format for
Method-3 debate-map work. Output is raw/advisory.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No steering.
Single neutral "continue" ONLY on visible mid-generation truncation (packet-authorized, logged);
otherwise no follow-ups of any kind.

-----BEGIN PASTE REQ_RAMPAGE_R11_20260711T064115Z-----
```markdown
# Deep Research request — Contradiction map: published head-to-head tensions in AGN feedback and quenching

**Request ID:** `REQ_RAMPAGE_R11_20260711T064115Z`
**Role:** Literature analyst building a debate map for a galaxy-evolution research journal.
Published work only; no access to the project's internal results. Your job is to catalogue
tensions, never to resolve them.

**Domains (D1–D6):** D1 AGN-feedback role in central-galaxy quenching; D2 AGN-outflow incidence
and mass loading; D3 reservoir depletion vs suppressed star-formation efficiency; D4 maintenance
(radio-mode) heating; D5 simulation-vs-observation feedback tests; D6 chemical/structural/high-z
channels (incl. MZR/FMR behavior and the z>10 abundance/mass debate).

**Entry format — one `### CONTRA-<n>` block per contradiction, grouped by domain:**

    ### CONTRA-<n> [D<k>] <short handle>
    - Position A: <finding, value ± unc where numeric, estimand spelled out> — <Author (year), citation>
    - Position B: <finding, value ± unc where numeric, estimand spelled out> — <Author (year), citation>
    - Tension type: SAME_ESTIMAND_NUMERIC | INTERPRETIVE | SCOPE/SELECTION | METHODOLOGICAL
    - Each side's stated reason for the discrepancy (attributed)
    - Proposed reconciliations in the literature (attributed, cited) or NONE_FOUND
    - Status per the most recent citing literature: OPEN | PARTIALLY_RECONCILED | LARGELY_SUPERSEDED (attributed)

**Coverage requirements:**
- ≥2 entries per domain D1–D6 where they exist (state `NONE_FOUND` for a domain otherwise);
  target 12–24 entries total, quality over quantity.
- SAME_ESTIMAND_NUMERIC entries are the most valuable: both sides must genuinely measure the same
  quantity (if estimands differ, the entry is SCOPE/SELECTION or METHODOLOGICAL and must say so).
- Include at least the well-documented tension families where published head-to-heads exist, e.g.
  positive-vs-negative feedback claims in the same object classes, gas-rich vs gas-poor quenched
  hosts, cavity heating sufficiency, sim quenched-fraction mismatches, z>10 tension-vs-no-tension —
  each ONLY as reflected in actual citable exchanges.

**Required sections, in order:** `## D1` … `## D6` (entries), then `## Cross-domain notes`
(contradictions whose sides live in different domains), then `## Links ledger`.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R11 answer — REQ_RAMPAGE_R11_20260711T064115Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Contradiction entries: <N>

- C2 (structure). Sections exactly as specified; every entry uses the CONTRA block template in
  full; empty fields say `NONE_FOUND`, never silently omitted, never padded.
- C3 (uncertainty). Every number carries the source's uncertainty or
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars.
- C4 (citation labeling). Every position/claim carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL) on the same line, or `UNCITED_NOT_USABLE` (an uncited position cannot anchor an
  entry — drop or mark the entry accordingly).
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes". Status labels
  must be attributed to citing literature, not asserted as your verdict.
- C6 (estimand labels). Tension type discipline above IS the estimand contract; every fraction
  carries tracer + selection + denominator + redshift range.
- C7 (links ledger). Final content section `## Links ledger`, one line per cited item:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R11_OUTPUT_DONE_20260711T064115Z

  must appear exactly once, as the standalone FINAL non-empty line of the report body. Nothing may
  follow it — no "End of Report", no sign-off. A marker only in a chat-UI element counts as ABSENT
  and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

Final reminder: the last non-empty line of your report must be exactly
`GEMINI_WEB_RAMPAGE_R11_OUTPUT_DONE_20260711T064115Z` with no text after it.
```
-----END PASTE REQ_RAMPAGE_R11_20260711T064115Z-----
