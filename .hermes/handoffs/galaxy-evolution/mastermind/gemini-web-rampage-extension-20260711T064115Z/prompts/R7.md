# R7 — Survey-feasibility dossier for the six-card decision criteria

Run ID: `RAMPAGE_R7` · REQ: `REQ_RAMPAGE_R7_20260711T064115Z` · Wave 5
Non-duplication: base runs R1/R1b asked per-card realism *judgments*; R7 compiles the underlying
PUBLISHED instrument/survey specifications and completed-program statistics those judgments depend
on. No science-result censuses here (that is R3/R4/R5 territory). Output is raw/advisory.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No steering.
Single neutral "continue" ONLY on visible mid-generation truncation (packet-authorized, logged);
otherwise no follow-ups of any kind.

-----BEGIN PASTE REQ_RAMPAGE_R7_20260711T064115Z-----
```markdown
# Deep Research request — Instrument/survey feasibility dossier for galaxy-evolution feedback tests

**Request ID:** `REQ_RAMPAGE_R7_20260711T064115Z`
**Role:** Technical literature analyst for a galaxy-evolution research program. Report only
published specifications, documentation, and completed-program statistics; you have no access to
the program's internal results.

**Context (self-contained):** The program's open questions need these measurement families:
(a) a multi-phase AGN-outflow census at matched depth (ionized/neutral/molecular tracers) at
z≈0–2; (b) resolved molecular gas in quenched/quiescent hosts; (c) X-ray cavity and hot-halo
detection toward low halo masses; (d) radio-AGN population monitoring; (e) high-z (z>3) quiescent
confirmation spectroscopy.

**Task:** Compile the feasibility evidence base, strictly from published sources.

**Required deliverables (markdown sections, in order):**
1. `## Capability table` — one row per instrument/mode relevant to (a)–(e) (e.g. JWST NIRSpec IFU
   & MSA, NIRCam WFSS, ALMA bands vs CO transition & z, VLT/MUSE & ERIS, Keck/KCWI, MaNGA-class
   IFU surveys, DESI/4MOST/WEAVE, eROSITA, Chandra/XMM, XRISM, LOFAR/MeerKAT/uGMRT/VLA and funded
   successors, Euclid/Roman grism):
   `Instrument/mode | Measurement family (a–e) | Sensitivity/depth figure (with units) | Spatial/spectral resolution | FoV/multiplex | Redshift window for the relevant lines | Citation (docs or paper)`
2. `## Matched-depth census feasibility` — published exposure-time analyses, sensitivity
   calculations, or completed-survey detection statistics for outflow tracers at matched depth:
   what sample size at what depth has actually been achieved or credibly proposed (cited).
3. `## Resolved gas in quenched hosts` — published ALMA (or NOEMA) detection rates, integration
   times, and stacking limits for CO/dust in quiescent galaxies, per mass/z bin.
4. `## Hot-phase limits vs halo mass` — published cavity/corona detection limits as a function of
   halo mass (Chandra/XMM/eROSITA), including stacking analyses.
5. `## Program-allocation reality` — published statistics on awarded time/program sizes for
   comparable programs (observatory reports, accepted-program abstracts), as attributed facts.
6. `## Feasibility verdicts` — one row per measurement family (a)–(e):
   `Family | Verdict: FEASIBLE_NOW / FEASIBLE_WITH_STATED_PROGRAM / NO_PUBLISHED_PATH | Enabling or blocking spec (cited) | What a decisive program would minimally require (as stated by sources, or NONE_FOUND)`
   Every verdict line must cite the spec(s) it rests on; verdicts are conditional summaries of the
   cited specs, not new claims.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R7 answer — REQ_RAMPAGE_R7_20260711T064115Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Capability rows: <N>

- C2 (structure). Exactly the six numbered sections above, in order; empty fields say `NONE_FOUND`,
  never silently omitted, never padded.
- C3 (uncertainty). Every quantitative figure carries the source's stated uncertainty/conditions,
  or `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent numbers.
- C4 (citation labeling). Every spec/statistic carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL — official instrument documentation URLs count) on the same line, or
  `UNCITED_NOT_USABLE`.
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes".
- C6 (estimand labels). Depth/sensitivity figures quoted under different conditions (point vs
  extended source, line vs continuum, on-axis vs survey average) are non-commensurable: label them.
- C7 (links ledger). Final content section `## Links ledger`, one line per cited item:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R7_OUTPUT_DONE_20260711T064115Z

  must appear exactly once, as the standalone FINAL non-empty line of the report body. Nothing may
  follow it — no "End of Report", no sign-off, no blank-line-then-text. A marker only in a chat-UI
  element counts as ABSENT and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

Final reminder: the last non-empty line of your report must be exactly
`GEMINI_WEB_RAMPAGE_R7_OUTPUT_DONE_20260711T064115Z` with no text after it.
```
-----END PASTE REQ_RAMPAGE_R7_20260711T064115Z-----
