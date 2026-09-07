# STARTUP RECOVERY RECEIPT (2026-09-07 20:11 KST) — cause found, nothing frozen changed
## ACTUAL CAUSE: MY INVOCATION, NOT A CORE DEFECT
`RUNTIME_PINS_A1_CORE.json["invocation"]` requires **`PYTHONDONTWRITEBYTECODE=1`** with the pinned interpreter, PYTHONPATH and thread variables. **My failing run set the interpreter and PYTHONPATH and omitted the rest.** macOS therefore wrote `bytecode_correspondence.cpython-39.pyc` at **11:05:58Z — the exact minute of my run** — and the correspondence gate refused it, correctly, as unregistered.
**Proof it was the invocation:** re-running the real read-only preflight under the EXACT pinned invocation → **PREFLIGHT PASS**, CORE and runtime accepted, readiness True, 38 entries, and **0 new caches written**. No CORE change is needed and none was made.
## EVIDENCE PRESERVED, NOTHING DELETED
| item | state |
|---|---|
| incidental cache | archived byte-for-byte with metadata: `evidence_incidental_cache_20260907/` (sha256 `14fe54a012f6c658…`, mtime 11:05:58.212Z), suffixed `.evidence` **outside every import and cache search location** so it can never be imported; the cache location itself restored to its pre-run state |
| aborted designation | `OUT_A1/designation.abort.json` and `OUT_A1/input-anchor.json` untouched; **there is no `designation.started.json`** |
| my superseded declaration of 6444945 | retained in `INPUT_ANCHOR_RECORD_20260907.md`, marked superseded |
| round 6444942 (11:08:00Z) | **passed unused. Not collected, not substituted, not backdated, no re-anchor performed.** |
## BYTE-IDENTITY OF THE FROZEN SET — all unchanged
A1 `6b9ecc79…` · run_path `1c4f96fb…` · CORE `e9222abf…` · C `bbc08cd6…`
## A CORRECTION TO MY OWN BLOCKED REPORT
I listed **ANCHOR-DIGEST as a second executed gate failure. It was not.** The run aborted at `MISSING-CORE-ENTRY`; ANCHOR-DIGEST was my *inspection* of the code afterwards. `OUT_A1` containing no `designation.started.json` confirms only one gate ever ran. Recorded as an inspection, not an execution.
**And the related claim was too strong.** I wrote that the published anchor "does not bind the artefact the code checks". In fact the published C at commit `f7486ed5…` — fetched from GitHub by Codex — **states `core_manifest.sha256 = e9222abf13485a36017d09dbd5be4c50597478882acc773626102416f9a26710` inside its own bytes.** So the CORE digest *was* publicly stated at anchor time. What is missing is only the **machine-readable representation**: `published_sha256` must name the CORE digest, with the external source identified as the publicly committed C that states it.
## NEXT-RUN TEMPLATE — timing fields genuinely pending
```json
{"stage":"input-anchor","verdict":"PASS","mechanism":"public-push",
 "published_sha256":"e9222abf13485a36017d09dbd5be4c50597478882acc773626102416f9a26710",
 "published_sha256_refers_to":"the CORE input manifest, as stated inside the publicly committed INPUT_FREEZE_C_20260907.json",
 "input_freeze_sha256":"bbc08cd696150f9a077b32a644f0f39b18dc777e8627576c55b6dada8d3269f8",
 "external_reference":"PENDING — GitHub PushEvent id and head for the NEW push",
 "third_party":"github.com","lane_owner":"hwao-lane",
 "third_party_utc":"PENDING — GitHub server-side created_at of that push",
 "adopted_a1_sha256":"6b9ecc79210046fa4c6611953184ece75818214bf4e962e4ac2e308243616e9f"}
```
Invocation for the next run, verbatim: `env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<venv site-packages> OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /Library/Developer/CommandLineTools/usr/bin/python3`.
## AUTHORITY STILL NEEDED — reconciled against A1, not assumed
- **Attempt limit:** A1/V15's "one further validation attempt" attaches to **validation attempts**. No draw, no scoring and no validation occurred, so **no attempt was consumed.**
- **Missed deadline:** `designate()` refuses once `now ≥ scheduled`; there is **no automatic restart**, so a **new anchor** is required — a mechanical consequence, not a new scientific decision.
- **A1 §125** counts external anchoring among the events after which a run "has begun" **for the precedence rule** — i.e. which document governs. It does not make a fresh anchor a new adoption, and I am not treating an incidental cache as grounds to rewrite the method or repeat its reviews.
**Precise remaining authority: the decision to perform a SECOND anchor push** — the first having expired unused. Everything else is covered. That is Codex's to confirm, and I have not done it.
