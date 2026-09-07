# BOUNDED CODEX TASK — observational-test candidate evidence (Tori, 2026-09-07)

You are gathering EVIDENCE ONLY for a shortlist Tori will rank. You do not rank, recommend, or decide anything.

## Boundaries (hard)
- You MAY create or edit files ONLY under `bhu_observational_test/`. Touch nothing else in the lane: two reviewer seats are
  running right now against pinned inputs, and mutating any pinned file is the incident we are still writing up.
- Do NOT read, list or copy anything under any Hwao lane or any directory named for unopened evaluation data.
- Published, peer-reviewed sources only for physics claims; a preprint may be cited ONLY as context and must be labelled as such.
- Where you state that data is available, PROVE it: give the archive/service, the exact query or file, and what you actually
  observed (an HTTP status, a row count, a file size, a digest). "It is public" without a check is not evidence.
- Do not start any census/framework work. Do not run the R3C2 kit.

## Inputs you may read (lane-local)
`BHU_CORPUS_SYNTHESIS_20260902.md`, `BHU_PROGRAMME_SYNTHESIS_20260906.md`, `WARRANT_TABLE_20260903.md`,
`NS_MASS_WATCH_HITS.md`, `DESI_CURVATURE_WATCH_HITS.md` (lane copy), `K5_RESULT*`/`K5_LISA_FORECAST_PREREG_20260904.md`,
`PROGRAM_A_FREEDOM_MAP_20260902.md`, `RESOURCE_CATALOG.md` (parent dir, read-only), and the pinned corpus texts.

## Produce exactly one file: `bhu_observational_test/EVIDENCE_20260907.md`
For EACH of these five candidate claims, one section with the headings below. If a fact is not in the record, write
NOT IN RECORD rather than inferring it.

1. Entry 31's neutron-star maximum-mass bar (the author's own stated refutation threshold).
2. The Gaztañaga causal-horizon large-angle CMB correlation cutoff (entries 23–27, 54, 56).
3. Entry 54's spatial-curvature sign (closed universe).
4. The signed spin-axis/parity successor pre-registration in this lane (what it predicts observationally).
5. Entry 21's de Sitter-core ringdown (K5), including the class K5 actually filed.

Headings per section:
- **CITED PREDICTION** — the claim in the author's own words, with file and line, and whether it fixes a DIRECTION, a SCALE, or a
  MAGNITUDE. Quote; do not paraphrase.
- **IS IT A PREDICTION OR A LABEL?** — state explicitly whether the claim predicts a cosmological observable, or merely agrees with
  a classification/label applied to images or catalogue entries.
- **OBSERVABLE + DATA** — the measurable quantity, and the specific public dataset that carries it, with your access evidence.
- **COMPETING EXPLANATION** — what standard cosmology (or standard astrophysics) predicts for the same observable, cited.
- **FREE PARAMETERS** — every quantity the model may adjust after seeing data, from the lane's freedom map where it exists.
- **WHAT WOULD COUNT AGAINST THE MODEL** — the specific outcome, stated so it could actually occur.
- **SMALLEST USEFUL PILOT** — the least work that yields a real discriminating result: data volume, compute, wall-clock, and the
  main confounders that could fake either answer.

End the file with a table: claim | direction/scale/magnitude | data reachable now (YES/NO + evidence) | free parameters | pilot size.
Then print the file's sha256 and line count as your final answer.
