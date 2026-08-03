# Verify Plan — NM-C2V2-20260727-A

**Classification: HIGH-RISK** live/public/current-Lab mutation. Paths repo-relative to `/Users/duhokim/NebulaMind/NebulaMind`. All checks below are a PLAN for the execution step; nothing here is executed by the preflight.

## Pre-write (ALL must PASS, else ABORT before any create)
- **Legal id:** `c2v2e2e0726a` — `isalnum()` True, length 12 (≤ 32).
- **Candidate/source hashes unchanged:** V2 `candidate.pdf ac59ac60…` (84,831 B), `candidate.tex bb77d38d…` (6,647 B), `result.png ed83a825…` (38,386 B); V1 frozen (`c615b2f3`/`eed8992d`); source `gated-e2e-demo/draft.tex f1aeadd8…`, `gated-e2e-demo.json 46ddd75d…`, `result.png ed83a825…`.
- **Target absence:** all four target paths + the run directory ABSENT.
- **Manifest schema/labels/routes:** `PREVIEW_MANIFEST.json` valid JSON; `status:"done"`; `result.summary` non-empty and contains `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration`; `figure_url`/`pdf_url` match the id; review + `lit_*` fields omitted. (See `MANIFEST_VALIDATION.md` — all PASS.)

## Post-write local checks (all four creates)
- `.../c2v2e2e0726a/draft.pdf` SHA-256 == `ac59ac60…`, 84,831 B.
- `.../c2v2e2e0726a/draft.tex` SHA-256 == `bb77d38d…`, 6,647 B.
- `.../c2v2e2e0726a/result.png` SHA-256 == `ed83a825…`, 38,386 B.
- `.../c2v2e2e0726a.json` SHA-256 == `fa4c8155…`, 2,566 B (byte-identical to `PREVIEW_MANIFEST.json`).

## GET / list checks (served endpoints; expect 200, never 400)
- `GET /api/lab/runs` — the new record `c2v2e2e0726a` appears with its labelled `summary`.
- `GET /api/lab/runs/c2v2e2e0726a` — 200 (legal `get_run`), returns the manifest.
- `GET /api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` — 200, `Content-Length` == 84,831, body SHA-256 == `ac59ac60…`.
- `GET /api/lab/runs/c2v2e2e0726a/artifact/result.png` — 200, body SHA-256 == `ed83a825…`.
- Assert none of the above returns `400`. (Contrast, from source-code reasoning only: the earlier hyphenated id `gated-e2e-demo-c2-v2` **would** return `400` per the `get_run`/`get_artifact` validator because `rid.isalnum()` is False — a conclusion derived from `backend/app/routers/lab_runner.py`, NOT from any executed live HTTP request. No live HTTP was run against either id.)

## Visible-label checks
- Served `result.summary` (list card) contains all four labels: `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration`, and the "not submitted / not peer-reviewed / no fresh data run / not a physical interpretation" wording.
- `pdftotext` of the served `draft.pdf` contains the F4 not-submitted tag, the TENSION caveat, and the unresolved-calibration O/H caveat.

## Baseline integrity (must be UNCHANGED after promotion)
- `gated-e2e-demo/draft.pdf 0d863bff…`, `gated-e2e-demo/draft.tex f1aeadd8…`, `gated-e2e-demo.json 46ddd75d…`.
- `baseline/INPUT_SHA256.txt` still 38/38 PASS.

## On ANY failure
STOP immediately; unpublish via the manifest-first guarded rollback (`BACKUP_ROLLBACK.md`); verify all four target paths + the run directory are ABSENT again; report the failure. Do not retry blindly.
