# Manifest Validation — NM-C2V2-20260727-A (read-only)

`PREVIEW_MANIFEST.json` SHA-256: `fa4c815578aef3f01a7e18985f83725fefab052d4735987577f77f76f4d6b0ba` (2,566 bytes). All checks below were run **locally and read-only** (no `lab-runs`/public write, no live HTTP).

## Results (all PASS)
| check | result | detail |
|---|---|---|
| valid JSON parse | PASS | parses with `json.load` |
| id alphanumeric | PASS | `c2v2e2e0726a` — `isalnum()` True |
| id length ≤ 32 | PASS | length 12 |
| `status == "done"` | PASS | list-visibility gate |
| `result.summary` non-empty | PASS | list-visibility gate |
| four required labels in `result.summary` | PASS | `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration` all present |
| summary states not submitted / not peer-reviewed | PASS | verbatim in summary |
| summary states no fresh data run | PASS | "no fresh data run" |
| summary states not a physical interpretation | PASS | "NOT a physical interpretation … cannot be interpreted as physical" |
| `result.figure_url` matches id | PASS | `/api/lab/runs/c2v2e2e0726a/artifact/result.png` |
| `result.pdf_url` matches id | PASS | `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` |
| optional review fields absent | PASS | no `review_url` / `review_verdict` / `review_cycles` (no review artifact will be served) |
| `lit_grounded`/`lit_papers` absent | PASS | run will honestly read as "not grounded" |
| `spec.force == true` | PASS | forced-demo lineage disclosed |
| all four target paths + run dir ABSENT | PASS | create-only |
| candidate V2 hashes match frozen | PASS | pdf `ac59ac60…`, tex `bb77d38d…`, png `ed83a825…` |
| source baseline `gated-e2e-demo` unchanged | PASS | `draft.pdf 0d863bff…`, `draft.tex f1aeadd8…`, `.json 46ddd75d…` |

## Route validators (cited accurately from `backend/app/routers/lab_runner.py`)
- **`get_run` (l.181–191):** rejects with `400` unless `rid.isalnum()` **AND** `len(rid) ≤ 32` (maximum length 32). → `c2v2e2e0726a` passes (alphanumeric, length 12).
- **`get_artifact` (l.194–201):** rejects with `400` unless `rid.isalnum()` **AND** the artifact `name` contains neither `/` nor `..` (safe artifact name). **This handler has NO run-id length check.** → `c2v2e2e0726a` + `draft.pdf`/`result.png` passes.
- **`list_runs` (l.148–178):** a run is visible only if top-level `status == "done"` **AND** `result.summary` is non-empty.

> Correction of record: `NEW_RUN_TARGET_MAP_V2.md:18` mis-attributed a `len(rid) > 32` check to `get_artifact`. Per `TORI_NEW_RUN_MAP_V2_VALIDATION_V1`, `get_artifact` checks only alphanumeric + safe artifact name; the length bound (≤ 32) is in `get_run` only. The route-validity conclusion is unchanged: `c2v2e2e0726a` passes both handlers.
