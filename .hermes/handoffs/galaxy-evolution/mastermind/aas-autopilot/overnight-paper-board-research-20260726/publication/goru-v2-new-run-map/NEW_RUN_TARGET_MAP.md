# C2 V2 New-Run Target Mapping

AI_DRAFT_NOT_HUMAN_GOLD

*ATTESTATION: This is a read-only mapping. No public byte was touched, no browser or live-HTTP requests were made, no candidate copy occurred, and the baseline run was NOT edited.*

## 1. Exact ABSENT/Create Paths
The following target paths for a create-only promotion of the new run `gated-e2e-demo-c2-v2` have been verified as currently **ABSENT**:
* `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2.json` (ABSENT — create)
* `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2/draft.pdf` (ABSENT — create)
* `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2/draft.tex` (ABSENT — create)
* `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2/result.png` (ABSENT — create)

## 2. Source-Code Route Coupling
According to `lab_runner.py`, a new run is discovered and served purely additively by creating `<id>.json` (with `"status": "done"` and a populated `"summary"`) and the accompanying `lab-runs/<id>/` artifacts directory. 
This will automatically couple the new artifacts to the dynamic API route: `/api/lab/runs/gated-e2e-demo-c2-v2/artifact/<name>`.
**NO** existing run or JSON needs editing. This is a safe, strictly additive create-only operation.

## 3. Candidate V2 Hashes (Source of Promotion)
The following V2 candidate bytes will be copied into the new run directory:
* `candidate.pdf`: `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d`
* `candidate.tex`: `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6`
* `result.png`: `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`

## 4. Preview/Manifest Field Requirements
To successfully appear in the UI and serve the PDF, the new `gated-e2e-demo-c2-v2.json` must carry at least the following fields:
* `id`
* `status` (must equal `"done"`)
* `result.summary`
* `result.pdf_url` (must equal `/api/lab/runs/gated-e2e-demo-c2-v2/artifact/draft.pdf`)
* `created_utc`

The required visible labels (`AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration`) must be explicitly surfaced in the `result.summary` text so they survive into the final served representation. (They should also be added to a preview/draft flag if the schema formally supports it).

## 5. Create-Only Backup/Rollback Plan
* **Backup Requirement**: None. There is nothing to back up since this is a create-only pathway and no existing bytes are being overwritten.
* **Rollback Command Plan (DO NOT EXECUTE)**:
  ```bash
  rm -rf .hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2
  rm -f .hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2.json
  ```
  *(Explicit confirmation: the baseline `gated-e2e-demo` run is never touched.)*

## 6. HTTP / SHA / Visible-Label Verification Plan
This is a plan for the future publish packet (**DO NOT EXECUTE**):
1. **SHA Check**: `shasum -a 256 .hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo-c2-v2/draft.pdf` should return `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d`.
2. **HTTP Check**: Run `curl -I http://localhost:8000/api/lab/runs/gated-e2e-demo-c2-v2/artifact/draft.pdf` and verify a `200 OK` response with the correct `Content-Length`.
3. **Label Check**: Verify that the text in the served `summary`/manifest and the text of the PDF itself carry the labels: `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration`.

## 7. Blockers
None encountered. The mapping was successfully resolved entirely by static read-only inspection.
