# C2 V2 New-Run Target Mapping (REPAIR - Legal ID)

AI_DRAFT_NOT_HUMAN_GOLD

*ATTESTATION: This is a read-only mapping. No public byte was touched, no browser or live-HTTP requests were made, no candidate copy occurred, no `lab-runs` creation/edit occurred, and the failed first mapping was preserved unchanged.*

## 1. Legal ID & ABSENT Verification
* **Legal ID**: `c2v2e2e0726a`
* **Validation Check**: The ID length is 12 characters (≤ 32) and it is purely alphanumeric (`isalnum()` is True).
* **ABSENT Paths (Create-only)**:
  * `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json` (ABSENT — create)
  * `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.pdf` (ABSENT — create)
  * `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.tex` (ABSENT — create)
  * `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/result.png` (ABSENT — create)

## 2. Route Source-Code Validity
According to `backend/app/routers/lab_runner.py`:
* The `get_artifact` route (l.194-201) checks `if not rid.isalnum() or len(rid) > 32: raise HTTPException(status_code=400...)`. Since `c2v2e2e0726a` is fully alphanumeric, it perfectly passes this validation.
* The `get_run` route (l.181-191) applies the exact same validation (`if not rid.isalnum() ...`). Therefore, the route `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` is perfectly valid and will correctly serve bytes from `RUNS_DIR / rid / name`.
* **Contrast**: The previous ID (`gated-e2e-demo-c2-v2`) failed because it contained hyphens (`-`), making `isalnum()` evaluate to False and triggering the 400 Bad Request rejection.

## 3. Manifest Requirements (Grounded in Source)
According to the `list_runs` logic (l.157-161), for a run to be visible in the API list, it MUST have `rec.get("status") == "done"` AND a non-empty `res.get("summary")`. Therefore, `c2v2e2e0726a.json` must carry:
* Top-level: `id`, `status: "done"`, `created_utc`, and `spec` (containing `spec.method` and `spec.data_sources`).
* `result` block containing:
  * Non-empty `summary`
  * `figure_url = /api/lab/runs/c2v2e2e0726a/artifact/result.png`
  * `pdf_url = /api/lab/runs/c2v2e2e0726a/artifact/draft.pdf`
* **OMISSIONS**: Optional fields like `review_url`, `review_verdict`, `review_cycles` MUST be omitted unless actual review artifacts are placed in the directory. `lit_grounded` and `lit_papers` must also be omitted so the API correctly and honestly reports the run as "not grounded".

## 4. Visible Labels
The required labels — `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration` — MUST be prominently surfaced in the `result.summary` text. This is the field that `list_runs` extracts and returns, ensuring the labels survive into the served representation.

## 5. Candidate V2 Hashes (Source of Promotion)
The following V2 candidate bytes will be copied into the new run directory:
* `candidate.pdf`: `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d`
* `candidate.tex`: `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6`
* `result.png`: `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`

## 6. Create-Only Backup/Rollback Plan
* **Backup**: Nothing to back up (this is a strictly create-only pathway).
* **Rollback Command Plan (DO NOT EXECUTE)**:
  ```bash
  rm -rf .hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a
  rm -f .hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json
  ```
  *(The baseline `gated-e2e-demo` run is completely isolated and never touched.)*

## 7. HTTP / SHA / Visible-Label Verification Plan
This is a plan for the future publish packet (**DO NOT EXECUTE**):
1. **SHA Check**: Confirm `shasum -a 256 .hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.pdf` matches `ac59ac60...`.
2. **HTTP Check**: Run `curl -I http://localhost:8000/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf`. Verify it returns `200 OK` + expected `Content-Length` and critically confirm that it does **NOT** return a 400 Bad Request.
3. **Label Check**: Confirm the text in the served `summary`/manifest and the text of the PDF carry the four required labels.

## 8. Blockers
None. Read-only static verification is complete.
