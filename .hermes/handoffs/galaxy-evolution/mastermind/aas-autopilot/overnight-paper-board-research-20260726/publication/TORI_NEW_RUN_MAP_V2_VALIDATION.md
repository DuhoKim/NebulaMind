# Tori Validation — Corrected New-Run Map V2

Marker: `OVERNIGHT_PAPER_BOARD_TORI_NEW_RUN_MAP_V2_VALIDATION_V1`

Status: `PASS_WITH_SOURCE_CITATION_CORRECTION`

## Pass

- Legal run id: `c2v2e2e0726a`.
- Length 12; `isalnum()` true.
- Target JSON and directory are absent.
- Candidate V2 hashes match the frozen accepted candidate.
- The first failed map and receipt remain preserved unchanged.
- Create-only publication avoids overwriting the baseline `gated-e2e-demo` run.

## Required source citation correction for the publish packet

`NEW_RUN_TARGET_MAP_V2.md:18` says `get_artifact` also checks `len(rid) > 32`. The current source does not:

- `get_run` at `backend/app/routers/lab_runner.py:181-191` checks alphanumeric and maximum length 32.
- `get_artifact` at `backend/app/routers/lab_runner.py:194-201` checks only that the run id is alphanumeric and the artifact name contains neither `/` nor `..`.

This does not change the route-validity conclusion: `c2v2e2e0726a` passes both handlers. The exact publish packet must cite the validators accurately and must not repeat the extra length check for `get_artifact`.

## Publication status

No live/public/source byte changed. Publication remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL` pending a candidate-specific exact packet and its exact approval phrase.
