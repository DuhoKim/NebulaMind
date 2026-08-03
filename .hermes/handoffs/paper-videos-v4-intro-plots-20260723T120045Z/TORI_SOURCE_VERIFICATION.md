# TORI VERIFICATION — V4 direction requires source refresh and plot-map corrections

Verdict: `PASS_WITH_MANDATORY_AMENDMENT`

The Hwao direction has the correct structural response to the user's feedback, but it must not be used for a canary until these verifier findings are incorporated.

## 1. Renderer root cause — verified

`paper-videos-v2-20260723T034035Z/build_paper_videos_v2.py:273-289` hard-wires `first_page_path` into the first narrated teaching scene. V3 reuses the V2 layouts. The user's critique therefore maps to a concrete shared-renderer defect: the introduction's dominant visual is a shrunken manuscript cover rather than an explanatory visual.

## 2. Current public sources do not match the V3 freeze

Fresh downloads from the five canonical `source_url` values were SHA-256 compared with the frozen V2/V3 PDF inputs:

| key | frozen sha256 | current live sha256 | match |
|---|---|---|---|
| z9-metallicity | `7b12f8af4a5b173d1c09d4190df145cfdafa2c628cca8c6262858c9f1f76c3f9` | `37c7795175ead264403a68c882c15b4d39e2c203836e9c829a13e67110fc24e8` | NO |
| scaling-relations | `8a45fe2ae8aa38e4e8a329c3622f34b65ce3b90ba10a6ee23198197b0131b23d` | `e878fff31192d3bfa1677e6784d3bf3901aa9bb95522d3dd801ea0ed6a145f0b` | NO |
| massive-abundance | `1b2de6f74ec6ef8606e88d1b9049ccc6cf3ac5416a53240e07d8100ccc1d61d6` | `189a2764a0b8e310802fb31bd53db3a64be49ac6411fe5f5b38af62cefa23f5d` | NO |
| mzr-framework | `bb0869aa02afd311d91605d60e3613e88bead425a088dd1bea844c6ff9b0e59e` | `bb0869aa02afd311d91605d60e3613e88bead425a088dd1bea844c6ff9b0e59e` | YES |
| tng-validation | `f037d89d210130d464e3ddbc2390b020aa3ffeebabab272357102691190f75d6` | `086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef` | NO |

At least two are plainly substantive, not PDF metadata churn:

- Current scaling-relations says the apparent SFMS elevation below redshift six is consistent with pure selection and makes no physical-evolution claim there; the frozen extract instead retains the older "rapid early enrichment" interpretation.
- Current massive-abundance uses the like-for-like total-mass footing: factor `2.04`, required shift `0.20 dex`, committed budget `0.46–0.55 dex`. The frozen narration/figure uses factor `2.7`, `0.28 dex`, and an undifferentiated `~1 dex` budget.

Therefore the next gate is not figure inventory against the old freeze. It is:

1. freeze and hash the current live PDFs;
2. extract current text/figures;
3. claim-level diff current manuscripts against V3 narration/cards/captions;
4. rewrite affected V4 narration before any audio/lip-sync/layout build;
5. then perform plot inventory and crop/redraw decisions against the new freeze.

## 3. Hwao plot-map corrections

Independent extraction of the current public PDFs shows:

- `scaling-relations`: both Figure 1 and Figure 2 exist. Figure 1 shows JWST points against local SFMS/MZR relations. Figure 2 shows offsets versus redshift and carries the selection-aware interpretation. Both should be inventoried; the allowed claim must reflect the current no-SFMS-evolution-below-z~6 boundary.
- `massive-abundance` Figure 1 has x-axis **redshift**, not stellar mass; y-axis is cumulative number density above the fixed mass threshold. Its current claim uses factor `2.04` and a `0.20 dex` shift.
- `z9-metallicity` Figure 1 is the gas-phase mass–metallicity plane: stellar mass versus oxygen abundance.
- `tng-validation` Figure 1 is relation versus stellar mass; Figure 2 is offsets versus redshift.
- `mzr-framework` has no paper figure; use a source-quoted procedure diagram explicitly labeled non-data unless a current source inventory finds a legitimate table/figure.

## 4. Safe state

No V4 media has been rendered. No YouTube, visibility, website, DB, Git, runtime, deploy, restart, or V3 artifact mutation has occurred. Existing public V3 videos remain unchanged while the corrected V4 source contract is prepared.

TORI_V4_DIRECTION_VERIFICATION_PASS_WITH_MANDATORY_SOURCE_REFRESH
