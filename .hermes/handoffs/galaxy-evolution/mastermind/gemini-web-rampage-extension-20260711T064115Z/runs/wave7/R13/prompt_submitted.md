# R13 — High-z quiescent frontier census (z ≥ 3)

Run ID: `RAMPAGE_R13` · REQ: `REQ_RAMPAGE_R13_20260711T064115Z` · Wave 7
Non-duplication: base run R2 Q8 touched the z>10 abundance tension; R8 (this packet) covers
ensemble evolution with matched estimands. R13 is the *object-level* frontier census: confirmed
massive quiescent galaxies at z≥3, their gas constraints, and inferred quenching timescales —
card-6 high-redshift territory with no prior depth run. Ensemble quenched fractions are OUT of
scope here (R8's job). Output is raw/advisory.

Paste everything BETWEEN the sentinel lines (sentinels and code fence excluded). No steering.
Single neutral "continue" ONLY on visible mid-generation truncation (packet-authorized, logged);
otherwise no follow-ups of any kind.

-----BEGIN PASTE REQ_RAMPAGE_R13_20260711T064115Z-----
```markdown
# Deep Research request — Census of spectroscopically confirmed massive quiescent galaxies at z ≥ 3

**Request ID:** `REQ_RAMPAGE_R13_20260711T064115Z`
**Role:** Literature analyst for a galaxy-evolution research journal. Published work only; no
access to the project's internal results.

**Required deliverables (markdown sections, in order):**
1. `## Confirmed-object census` — one row per spectroscopically confirmed quiescent galaxy or
   published sample at z ≥ 3:
   `Object/sample (citation) | z_spec ± unc | Confirmation instrument/mode | M* ± unc (IMF & SPS model stated) | SFR or limit ± unc (tracer, timescale) | Quiescence criterion used | Notes/caveats named by the source`
   JWST-era confirmations (e.g. NIRSpec) and pre-JWST anchors both belong here, labeled by era.
2. `## Number densities` — published number-density estimates of massive quiescents per z bin
   (z≈3–4, 4–5, >5), each with volume, selection, mass limit, uncertainty, citation; paired (where
   the sources themselves make the comparison) with simulation/SAM predictions as attributed
   comparisons with the sources' stated caveats.
3. `## Gas and dust constraints` — published CO/[C II]/dust-continuum detections or upper limits in
   z ≥ 3 quiescents: instrument, depth, inferred gas-fraction limit ± unc (conversion stated), citation.
4. `## Formation and quenching timescales` — the formation-epoch and quenching-timescale inferences
   each study derives (attributed, with the SFH model named); disagreements between SFH methods on
   the same objects.
5. `## Selection and systematics register` — published critiques: photometric preselection biases,
   emission-line contamination, M* systematics (IMF/SPS), quiescence-criterion sensitivity — each
   cited.
6. `## Tension ledger` — where the observed frontier is claimed to strain models and where it is
   claimed compatible: both positions, attributed, with the estimand each side actually uses.
7. `## Gaps` — `GAP:` lines (e.g. z ranges with no confirmations, missing gas constraints), cited
   or `NONE_FOUND`.

**Binding output contract:**
- C1 (meta header). ONE self-contained markdown report body starting with:

      # Rampage R13 answer — REQ_RAMPAGE_R13_20260711T064115Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
      Model: <model/product self-identification>
      Census rows: <N>

- C2 (structure). Exactly the seven numbered sections above, in order; empty fields say
  `NONE_FOUND`, never silently omitted, never padded.
- C3 (uncertainty). Every number carries the source's uncertainty or
  `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars.
- C4 (citation labeling). Every object/number carries a checkable citation (arXiv ID, DOI, ADS
  bibcode, or URL) on the same line, or `UNCITED_NOT_USABLE`.
- C5 (wording contract). Own-voice settled/causal register banned (case-insensitive):
  establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the
  debate, definitively, conclusively, is now known, "demonstrates that … causes". Model tension
  claims stay attributed; never adjudicate the tension in your own voice.
- C6 (estimand labels). Stellar masses under different IMF/SPS assumptions, SFRs on different
  timescales, and densities under different mass limits are non-commensurable: label them; no
  cross-estimand "consistent with" claims.
- C7 (links ledger). Final content section `## Links ledger`, one line per cited item:
  `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- C8 (completion marker). The exact string

      GEMINI_WEB_RAMPAGE_R13_OUTPUT_DONE_20260711T064115Z

  must appear exactly once, as the standalone FINAL non-empty line of the report body. Nothing may
  follow it — no "End of Report", no sign-off. A marker only in a chat-UI element counts as ABSENT
  and the run is rejected.

**Safety locks:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

Final reminder: the last non-empty line of your report must be exactly
`GEMINI_WEB_RAMPAGE_R13_OUTPUT_DONE_20260711T064115Z` with no text after it.
```
-----END PASTE REQ_RAMPAGE_R13_20260711T064115Z-----
