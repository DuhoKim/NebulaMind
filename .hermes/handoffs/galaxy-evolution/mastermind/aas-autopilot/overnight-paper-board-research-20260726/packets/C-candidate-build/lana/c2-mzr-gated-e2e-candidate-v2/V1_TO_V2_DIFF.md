# C2 V1 → V2 Change Log (F1–F4 red-team fixes)

AI_DRAFT_NOT_HUMAN_GOLD

V2 is a NEW versioned candidate. **V1 is frozen and untouched** (`candidate.tex` `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9`). A unified `diff -u` of V1 → V2 shows only the four fixes below plus the non-rendered header-comment update; every other line (Introduction split, Data-and-method, the three caveats, References) is unchanged context. Each fix is representation/wording only — **no new scientific number, relation, O/H offset, or claim was introduced.**

## F1 — soften the Result interpretive sentence (rendered; §Result)
- **Before (V1):** "This comparison provides insights into the relationship between galaxy mass and gas-phase metallicity in these two distinct datasets."
- **After (V2):** "We present the two median relations (TNG100 and SDSS); their direct comparison is bounded by the unresolved O/H-scale systematic (see Caveats) and is not interpreted as physical here."
- Effect: drops the interpretive-insight claim; keeps the source numbers (23,722 / 120,000) in the preceding sentence; cross-references the Caveats. Old phrase confirmed absent from the V2 PDF.

## F2 — remove the unsubstantiated "reproducible" (rendered; §Abstract)
- **Before:** "…via the NebulaMind Lab runner: a bounded, reproducible, descriptive study."
- **After:** "…via the NebulaMind Lab runner: a bounded, descriptive study."
- Effect: the forced (`spec.force=true`) demo lineage does not substantiate reproducibility; "reproducible" confirmed absent from the V2 PDF.

## F3 — surface the bounding status at Abstract + figure-caption level (rendered)
- **Abstract (added sentence):** "This is a scale-limited, TENSION-flagged anchor comparison on un-reconciled O/H scales — see Caveats."
- **Figure caption — before:** "Mass-metallicity relation"
- **Figure caption — after:** "Mass-metallicity relation. Median relations on un-reconciled O/H scales; the TNG--SDSS comparison is scale-limited (see Caveats)."
- Effect: the scale-limited/TENSION/anchor status now appears on the excerptable surface (abstract + figure caption), not only in the Caveats. **Caption text only — the source figure image `result.png` is byte-identical and unmodified.**

## F4 — visible not-submitted / not-peer-reviewed tag near Title/Abstract (rendered; §Abstract, first line)
- **Added:** "AI-assembled draft — not submitted, not peer-reviewed (AI\_DRAFT\_NOT\_HUMAN\_GOLD)."
- Effect: the AASTeX typesetting can no longer read as a formatted/submitted note; the tag renders at the top of the abstract.

## Non-rendered
- The five `%` header-comment lines before `\documentclass` were updated from the V1 build note to a V2 note describing F1–F4. LaTeX comments; not rendered in the PDF.

## Retained verbatim from V1 / source (unchanged or strengthened, never weakened)
- Source numbers: TNG100 `23,722`, SDSS `120,000`, `z=0`, SF-weighted gas metallicity → O/H (solar-scaled). No number invented; no O/H offset.
- All 5 references: Qi2025, Torrey2019, Garcia2023, Guo2016, **LaraLopez2013** (reference block textually identical to V1/source).
- Introduction citation **split** (four single-citation sentences).
- The original source **Caveats paragraph** (intact) and the three appended caveats — **O/H-scale** (bounded "…confounded … cannot be interpreted as physical until a common calibration is established"), **TENSION** (carried, not upgraded), **Provenance** (forced-demo lineage) — unchanged.
- `AI_DRAFT_NOT_HUMAN_GOLD` header comment + rendered provenance disclosure (now also reinforced by the F4 visible tag).
