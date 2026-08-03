# Publication Target Map

AI_DRAFT_NOT_HUMAN_GOLD

*ATTESTATION: This is a read-only mapping. No public byte was touched, no browser was launched, and no HTTP requests were made to a live server.*

## 1. Current Served Target
* **Target Type**: Dynamic API serving from the `lab-runs` directory.
* **Serving Mechanism**: The Next.js frontend calls the backend API endpoint (`/api/lab/runs`). The backend (via `backend/app/routers/lab_runner.py`) globs `*.json` from the `lab-runs` directory and dynamically serves the files located at `lab-runs/<id>/<filename>` through the `/api/lab/runs/{rid}/artifact/{name}` route.
* **Promotion Impact**: A C2 promotion would **replace** the existing draft artifacts in the `lab-runs/gated-e2e-demo/` directory.
* **Status**: **OCCUPIED (replace → needs backup)**. The target path currently hosts a `draft.pdf` and `draft.tex`.

## 2. Route / Manifest / Index Coupling
* **Discoverability**: Published items are discovered dynamically. There is no central JSON board or manifest file to edit. The "manifest" for a specific run is its individual JSON file (e.g., `lab-runs/gated-e2e-demo.json`).
* **Addition Mechanism**: An entry is coupled simply by the existence of a valid JSON file in the `lab-runs` directory with `"status": "done"` and a populated `"summary"`. The JSON file itself contains the explicit route mappings (e.g., `"pdf_url": "/api/lab/runs/gated-e2e-demo/artifact/draft.pdf"`). To add labels or change routes, the JSON file is regenerated or edited in place (replace).
* **Host Mapping**: Front-end requests to the Next.js app on `lab.nebulamind.net` (or similar subdomains) proxy to the FastAPI backend which serves the bytes.

## 3. Current Bytes + Hashes
### Target Files (To be replaced)
| File | Size (bytes) | SHA-256 |
|---|---|---|
| `lab-runs/gated-e2e-demo/draft.pdf` | 76,488 | `0d863bff4d4d260fe32e56617ca6f920f2943574aaff2a5faeee3f7460575933` |
| `lab-runs/gated-e2e-demo/draft.tex` | 3,836 | `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a` |

### Source of Promotion (C2 Candidate Hashes)
| File | SHA-256 |
|---|---|
| `candidate.pdf` | `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` |
| `candidate.tex` | `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` |

## 4. Backup / Rollback Requirements
* **Backup Requirement**: Before the C2 promotion, a backup must be made of the current `lab-runs/gated-e2e-demo/draft.pdf`, `lab-runs/gated-e2e-demo/draft.tex`, and `lab-runs/gated-e2e-demo.json`.
* **Rollback Command Plan (DO NOT EXECUTE)**:
  ```bash
  cp backups/gated-e2e-demo/draft.pdf .hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo/draft.pdf
  cp backups/gated-e2e-demo/draft.tex .hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo/draft.tex
  cp backups/gated-e2e-demo.json .hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo.json
  ```
* **Required Visible Labels**: `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration`. These must survive into the updated JSON/served form.
* **Smoke-Test Plan (DO NOT EXECUTE)**:
  1. **SHA check**: Run `shasum -a 256` on the newly replaced `lab-runs/gated-e2e-demo/draft.pdf` and assert it matches `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e`.
  2. **HTTP check**: `curl -s -I http://localhost:8000/api/lab/runs/gated-e2e-demo/artifact/draft.pdf` (or the equivalent local port) and assert a `200 OK` response with the expected `Content-Length`.

## 5. Gaps / Blockers
* **None encountered during static read-only analysis.** The serving target and dynamic mapping were fully determinable by inspecting the local repository configuration (`lab_runner.py` and `lab-runs/*.json`).
