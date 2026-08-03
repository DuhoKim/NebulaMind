# Evidence-Closure Worksheet: 7cb504ea7ad3

AI_DRAFT_NOT_HUMAN_GOLD

Marker: OVERNIGHT_PAPER_BOARD_PACKET_D_KUN_7CB_EVIDENCE_WORKSHEET_V1

This is a documentary worksheet only. I did not run the live runner, re-pull TNG or observational data, recompute the stellar mass function, edit a source file, or write any prose patch for missing-evidence gaps.

## Source Stability

Source hash check: PASS for the allowed `7cb504ea7ad3` inputs in `baseline/INPUT_SHA256.txt`:

- `7cb504ea7ad3.json`: OK
- `7cb504ea7ad3/draft.pdf`: OK
- `7cb504ea7ad3/draft.tex`: OK
- `7cb504ea7ad3/history.json`: OK
- `7cb504ea7ad3/result.png`: OK
- `7cb504ea7ad3/review.md`: OK

## Verdict-Language Recovery

Verbatim source verdict from `review.md` and `result.review`:

> (1) Verdict: This study provides a preliminary, automated measurement of the stellar mass function in IllustrisTNG but requires substantial improvement before publication.

Verdict-token status: the source uses a prose verdict, not a single-token verdict. I do not infer, assign, or normalize this to `MINOR`, `MAJOR`, `CONTRADICTS`, or any other token.

## Evidence Inventory

| evidence item | source text / location | traceability finding |
|---|---|---|
| Subject and dataset | `result.summary`: `IllustrisTNG (TNG100-1, z=0) stellar mass function...`; `draft.tex` title/abstract/result repeat the same study description. | PRESENT and internally traceable. |
| Galaxy count | `result.summary`: `203,524 galaxies`; `draft.tex` title/abstract/figure caption/result repeat `203,524 galaxies`. | PRESENT and internally traceable. |
| Box size | `result.summary`: `(111 Mpc)³ box`; `draft.tex` title/abstract/figure caption/result repeat `(111 Mpc)3 box`. | PRESENT and internally traceable. |
| Single SMF number | `result.summary`: `n(>10¹⁰·⁵M⊙)=1.49e-03 Mpc⁻³`; `draft.tex` title/abstract/figure caption/result repeat `n(>1010.5M⊙)=1.49e-03 Mpc-3`. | PRESENT and internally traceable. |
| Figure | `result.figure_url` points to `/api/lab/runs/7cb504ea7ad3/artifact/result.png`; artifacts list includes `result.png`; `draft.tex` includes `\includegraphics{result.png}`. | PRESENT and internally traceable as an artifact reference. |
| Method label | `spec.method` and `result.method` are `stellar-mass-function`; draft introduction says the requested analysis is `stellar-mass-function using TNG`. | PRESENT and internally traceable. |
| Run provenance | log records `loading TNG100-1 z=0 fields`, `computing TNG stellar mass function`, draft/PDF compilation, and automated referee review. | PRESENT as documentary run history; not a numerical recomputation. |

## Reproducibility Note

The single stated numerical result is documentarily traceable to the run's summary and repeated in the draft title, abstract, figure caption, and result section. The source does not provide raw count bins, an uncertainty model, observational comparison values, selection-function modelling, or code-level derivation in the allowed packet scope.

The draft's own caveat states: `This is an \emph{automated} first-pass descriptive result. It uses default selections and calibrations, does not homogenise IMF or abundance scales across sources, and applies no completeness or selection modelling. It is a starting point, not a validated measurement.`

Acceptance status from this worksheet: `BLOCKED` for acceptance closure, because referee-required evidence is absent and cannot be generated without a future gated runner/data step.

