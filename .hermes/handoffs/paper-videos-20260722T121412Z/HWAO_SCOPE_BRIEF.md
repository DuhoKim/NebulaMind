# Hwao scope brief — one public video per durable Nebula manuscript

Marker: `HWAO_PAPER_VIDEO_SCOPE_BRIEF_20260722T121412Z`

## User direction

User asks: “can you also make videos about each papers and publish and add also on Nebula?”

## Proposed scope for Hwao ratification

Interpret “each paper” as the five durable PDF manuscripts currently curated in the clean live Paper stage, not transient pipeline measurements:

### Flagship

1. `An Independent, Unlensed Gas-Phase Metallicity Deficit at z≈9–10`
   - Live PDF: `https://nebulamind.net/studies/z9-10-unlensed-metallicity-deficit.pdf`
   - Catalog source: `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/FlagshipStudies.tsx`
   - Current status: `REVIEW-READY`; descriptive, not validated, not published as a scientific paper.

### Frontier drafts

2. `Galaxy scaling relations from z≈0 to the JWST frontier`
   - Live PDF: `https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf`
   - Current status: descriptive draft; no human clearance.

3. `The z≈4–6 massive-galaxy abundance is consistent with IllustrisTNG once stellar-mass systematics are budgeted`
   - Live PDF: `https://nebulamind.net/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf`
   - Current status: `REVIEW-READY`; descriptive, not validated.

4. `Disentangling aperture and calibration systematics in the gas-phase MZR: a practitioner’s framework`
   - Live PDF: `https://nebulamind.net/agent-reports/research-frontiers/mzr-aperture-calibration-framework.pdf`
   - Current status: `REVIEW-CLEARED` by automated workflow; methods synthesis, not a new measurement and not human/journal validated.

5. `Calibration is not validation: confronting IllustrisTNG with observed scaling-relation evolution`
   - Live PDF: `https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf`
   - Current status: descriptive draft; no human clearance.

Catalog source for 2–5: `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/FrontierDrafts.tsx`.

## Excluded scope

The live `/api/lab/runs` currently exposes five non-demo pipeline measurements plus two demos. Three non-demo runs have no PDF and all are transient runtime records. Exclude them from “each paper” unless Hwao finds contrary evidence.

## Proposed media contract

- Five distinct narrated explainers, approximately 60–75 seconds each.
- Clearly female `en-US-EmmaNeural` narration.
- Manual SRT and burned-in captions from exact narration.
- Approved synthetic Flow astronomer identity only; no robot/mascot substitution.
- If the presenter is visible while speaking, use exact-audio lip-sync; otherwise use silent opening/outro portrait only.
- Deterministic local fact rendering; no invented charts or geometry.
- Every video repeats its status boundary: descriptive/machine-generated; not validated; automated review is not journal/human peer review.
- Public YouTube publication requested by the user, but upload must occur once per exact QA-locked artifact, with exact-title duplicate inventory, processing verification, manual captions serving, public settlement, and receipt.

## Proposed Nebula placement

Preserve current Paper-stage layout. Add a typed `video?: string` or centralized `paperVideos.ts` map keyed by exact PDF path and render a responsive YouTube embed inside each manuscript card near the existing PDF link. Do not add a new Paper subview or redesign the page.

Recommended source shape:

- New: `frontend/src/app/lab/paperVideos.ts` mapping each PDF path to a YouTube ID.
- Modify: `frontend/src/app/lab/FlagshipStudies.tsx` and `frontend/src/app/lab/FrontierDrafts.tsx` to render the corresponding embed only when an ID exists.
- Add/update focused source test for exact five-key coverage and correct embed/title/status semantics.

The existing `watch_subnav_videos.py` is out of scope and unsafe here because it auto-builds and restarts the live frontend after delivery-file changes. Do not use it.

## Gate boundaries

- Hwao scope/story ratification: requested now, read-only.
- Local rendering/QA: permitted by user request after scope ratification.
- YouTube upload/public visibility: user requested publication, but exact artifacts/titles must be frozen before mutation.
- Nebula source edit/test: user requested integration; exact patch and review still required.
- Git commit/push/merge: separate explicit approval.
- Runtime build/restart/deploy: separate explicit approval after source/video IDs verify.
- No DB/SQL/migration action.

## Hwao task

1. Approve/correct the five-paper scope and exclusions.
2. Approve/correct card-level video placement.
3. For each paper return:
   - one-sentence scope headline;
   - three exact, source-supported facts or numbers;
   - the main caveat/status wording;
   - any title/description wording that is unsafe for public YouTube.
4. Give the safest batch sequence across render, review, public YouTube, local source integration, Git, and runtime deployment.
5. Do not write project files or perform external mutations.

End with standalone marker:

`HWAO_PAPER_VIDEO_SCOPE_COMPLETE_20260722`
