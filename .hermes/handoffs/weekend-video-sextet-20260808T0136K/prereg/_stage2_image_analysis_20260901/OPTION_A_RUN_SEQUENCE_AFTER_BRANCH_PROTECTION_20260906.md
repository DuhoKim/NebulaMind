# OPTION A — EXACT RUN SEQUENCE once branch protection lands (written NOW, executed only after Blanc relays Duho's confirmation)

Written 2026-09-06 09:36 KST. Nothing below has been run. Every path is relative to the lane `_stage2_image_analysis_20260901/`; `$RULE` = `fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1`; `$STMT` = `SIGNATURE_RECORD_SELRULE_V15_20260906.md` (contains the rule digest and `2026-09-06T00:04:07Z` verbatim — the binding `collect` checks); T_sign = `2026-09-06T00:04:07Z`; T_pulse = `2026-09-06T00:15:00Z`; fallback instant = `2026-09-07T00:15:00Z`.

**Decision 4 as ruled (Duho "a", relayed 09:33 KST):** the rule stays as signed. The NIST pulse for T_pulse is fetched; if it does not authenticate (the observed 2048-bit certificate against a 512-byte signature), it is REFUSED and the outcome is RETRY — never a seed; from T_pulse + 24 h the drand fallback applies under the signed formula. No V16, no amendment, no acceptance check relaxed, signature untouched.

## Step 0 — branch-protection witness (Duho, then Hwao; V15 §7 "Freeze witness", line 56)
Duho enables "Do not allow force pushes" + "Do not allow deletions" on `feat/paper-workflow-v2` and says so in chat. Then Hwao, in a THROWAWAY clone (never the shared worktree):
```
git clone --branch feat/paper-workflow-v2 https://github.com/DuhoKim/NebulaMind.git /Users/duhokim/.claude/jobs/5b2f0371/tmp/bp_probe
cd /Users/duhokim/.claude/jobs/5b2f0371/tmp/bp_probe && git log --oneline -2
git commit --amend --no-edit --allow-empty            # rewrites the tip locally → non-fast-forward by construction
git log --oneline -2; git push --force-with-lease origin feat/paper-workflow-v2   # MUST be refused by the server
```
Receipt: `BRANCH_PROTECTION_WITNESS_RECEIPT_20260906.md` = verbatim server rejection text + exit code, the two `git log` graphs (before/after the amend) proving non-fast-forward, Duho's confirmation verbatim, KST stamp. If the push is ACCEPTED, STOP: the remote tip is now rewritten, Hwao immediately pushes the original tip back with `git push origin <original sha>:feat/paper-workflow-v2` from the shared worktree, files the failure, nothing else runs.

## Step 1 — beacon read (V15 §3b order (3)–(4)); the point at which the beacon is read
Earliest useful time: **2026-09-07T00:15:00Z (09:15 KST Monday)** — before that, NIST is refused (per the observed limit) and the result is RETRY with no seed. Running it earlier is allowed by the text and would only file a RETRY record. Command (from the lane root):
```
python3 _optionA_dev/beacon_v2/beacon_record.py collect --t-sign 2026-09-06T00:04:07Z --rule-sha256 $RULE --signature-statement $STMT --out _optionA_dev/beacon_record_T_pulse_20260906T0015Z.json
```
Exit 0 = ACCEPT-NIST or ACCEPT-DRAND; 4 = RETRY (record filed, re-run after the fallback instant); 2 = anything else (STOP, file). Then the independent re-verification with live re-fetch:
```
python3 _optionA_dev/beacon_v2/beacon_record.py verify --record _optionA_dev/beacon_record_T_pulse_20260906T0015Z.json --rule-sha256 $RULE --signature-statement $STMT
```
Receipt: `BEACON_READ_RECEIPT_20260906.md` = both commands' stdout verbatim (outcome, seed_hex, source), the record's SHA-256, the drand relay agreement count, KST stamps. The record is committed and pushed. Expected outcome under decision 4: `ACCEPT-DRAND`, source drand round ⌊(T_pulse − 1595431050)/30⌋ + 1.

## Step 2 — corpus identity, sealed FIRST (V15 §7 line 51; E3(i))
```
python3 _optionA_dev/corpus_identity/build_corpus_identity.py --beacon-record _optionA_dev/beacon_record_T_pulse_20260906T0015Z.json --rule-sha256 $RULE --signature-statement $STMT --exclude _optionA_dev/corpus_identity/dryrun_identities_to_exclude_20260905.txt --out _optionA_dev/corpus_identity/run_20260907
```
Produces `corpus_identity.json` (tuning 400 / holdout 200 / fresh 2,000 ordered objids, skipped ranks, seed, beacon-record digest, exclusion digest, pool digest) + `corpus_identity_receipt.json`. The builder itself re-runs `beacon_record.verdict` with live re-fetch and refuses `BEACON-NOT-ACCEPTED (<token>)`.
Seal: append to `seal_journal_tierc.jsonl` one chained record `{"timestamp","operation":"corpus-identity-freeze","relative_path","observed_digest":<sha256 of corpus_identity.json>,"status":"SEALED","predecessor_receipt_digest":<previous record's receipt_digest>,"receipt_digest":sha256(canonical_bytes(record))}` — the exact shape `scripts/stage2_gate_validation.py` lines 78–79 write via `seal_gate.canonical_bytes`/`_seal_predecessor`. **GAP, stated:** no dedicated append command exists yet for this operation; a ≤20-line `_optionA_dev/seal_append.py` reusing those two functions must be written, tested against `check_chain.py`, and its digest filed BEFORE step 2 — it is the only new code in this sequence and Blanc decides whether it needs a seat. Then:
```
git add <journal> <identity dir>; git commit; git push origin feat/paper-workflow-v2
python3 - <<'PY'   # witness pointer the driver requires (run_configurations.verify_witness)
import json,subprocess; c=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(); json.dump({"commit":c},open("seal_journal_tierc.jsonl.witness.corpus-identity-freeze.json","w"))
PY
```
The driver later checks: record in the journal, journal blob at that commit contains it, `origin` URL == pinned, `git fetch`, commit is an ancestor of `origin/feat/paper-workflow-v2`, and the identity file bytes equal the blob at that commit. Receipt: `CORPUS_IDENTITY_FREEZE_RECEIPT_20260907.md` (identity digest, journal record, commit sha, push confirmation, Duho's chat statement of the digest + commit hash — the second witness, V15 line 56).

## Step 3 — development bricks: checksum manifest → seal → fetch → render (E5(a)–(b), §9B.2a–c discipline)
**PREREQUISITE (finding 2026-09-06 ~11:15 KST, `FINDING_PIPELINE_AMENDMENT_REQUIRED_BEFORE_STEP3_20260906.md`): the §6 pipeline identity has no implementing code — the pinned `pixel_rejection.py` rejects MEDIUM and the render path refuses whole rasters on nexp ≤ 0. The PIPELINE AMENDMENT (new module + fixture + text, two-seat gate, Duho's signature) must exist before any development pixel is rendered. Step 3 is BLOCKED until then.**
For the 600 tuning+holdout objids only (never the 2,000): resolve bricks from `corpus_identity.json` (the builder's `resolve_brick` against `scratch/survey-bricks-dr9-north.fits.gz`), fetch each brick's PUBLISHED `.sha256sum` at the pinned DR9-north URL pattern (`scripts/fetch_one_checksum.sh <brick>`), build the sealed checksum manifest, seal it (same append), commit+push; then fetch the three planes per brick verified ONLY against that sealed manifest (`scripts/fetch_validation_bricks.sh <bricks.txt> <out_dir> <journal.jsonl>` semantics), then render 128×128 float32 tensors (`<objid>.ic6`, 65,536 bytes) under the §6 pipeline identity with `study_renderer.renderer_v3` (the `scripts/stage2_render_validation.py` path), writing `TUNING.csv` and `HOLDOUT.csv` with columns exactly `objid,g,tensor_sha256` in the identity's order. **GAP 2 CLOSED IN CODE (12:35 KST), NOT YET GATED:** `_optionA_dev/dev_corpus/dev_corpus_pipeline.py` SHA-256 a947a609f5acd68a65b47c2a540cf96b7172c2a8597b4d9111d237e370d67cf8 with fixture `test_dev_corpus_pipeline.py` 5b5fed0470e5fc9e125201d810cf4d0e75f10567b3eab71eb4b5df0a9d391935 (3 tests, synthetic brick, mocked network): modes `manifest` (published checksum files at the pinned URL pattern → sealed dev manifest + brick list + receipt), `fetch` (verified ONLY against that manifest; quarantine; resumable; locked; journalled), `render` (render_chain_v3 under r_T = 23 per V15 §6; SCORED → tensor, REFUSED → the V18 sentinel, journalled; driver manifests in identity order; read manifest per E5(b)). Development groups only — the fresh set is refused by name. To be gated with V18/V38 before use. Labels `g` come from the development label source named in §7 for the TUNING set; the holdout labels are read by `holdout` only. Receipts: fetch journal, render journal, manifest digests, KST stamps; first fetch timestamp must post-date the corpus-identity-freeze witness.

## Step 4 — tune (V15 §7 "Search"; all 96 configurations, journalled)
```
python3 _optionA_dev/fourier_chirality/run_configurations.py tune --manifest <TUNING.csv> --tensors <tensor dir> --out _optionA_dev/runs/tune_20260907 --identity _optionA_dev/corpus_identity/run_20260907/corpus_identity.json
```
Refuses on any integrity failure (`DATA-INTEGRITY-FAIL …`, exit 2). Output: `tuning_journal.jsonl`, `tuning_receipts.jsonl`, `selection_summary.json`, run-root digest. Floor: m ≥ 380 on the scored denominator, else `CLOSED`. Seal `tuning-freeze` (run-root digest) → commit → push → witness pointer `seal_journal_tierc.jsonl.witness.tuning-freeze.json` → Duho's chat statement of the digest + commit. Receipt: `TUNING_FREEZE_RECEIPT_20260907.md`.

## Step 5 — holdout, ONCE (V15 §7 "Holdout, once"; §4 N_max = 1)
```
python3 _optionA_dev/fourier_chirality/run_configurations.py holdout --tuning-receipt _optionA_dev/runs/tune_20260907/selection_summary.json --manifest <HOLDOUT.csv> --tensors <tensor dir> --out _optionA_dev/runs/holdout_20260907 --identity _optionA_dev/corpus_identity/run_20260907/corpus_identity.json
```
Reconstructs the winner from the 96 receipts (summary never trusted), refuses overlap with tuning, floor m ≥ 190, Wilson lower bound > 0.70 at z = 1.96. Output line: `{"mode","n_eligible","winner_config_id","verdict","m_scored","k_eff","wilson_lower"}`. PASS → E3(ii) candidate identity (family hash a026fe5f…, reconstructed config_id, env-lock hash 4e2c851f…) receipted and SEALED; FAIL/CLOSED → option A closes (§4), filed, no second attempt. Receipt: `HOLDOUT_RECEIPT_20260907.md` + `CANDIDATE_IDENTITY_FREEZE_RECEIPT_20260907.md`.

## Step 6 — only on a holdout PASS: the fresh set (E5(a),(d); §3a)
Hwao posts the E3(ii) and §6 freeze receipts' digests. Duho, logged in as `nmcustody`, fetches the 2,000 fresh-validation bricks into `/Users/nmcustody/fresh_validation_bricks/` against the sealed manifest; post-fetch receipt per the custody addendum; then Duho lifts the boundary ONCE in chat. Only then the frozen validation run (out of scope of this file; governed by the signed pipeline amendment and V36).

## Stop conditions, standing
Any refusal token, any integrity failure, any seat or gate FATAL, a server-accepted force push, a beacon outcome that is not ACCEPT-*, a manifest/tensor mismatch: STOP, file, wait. No step is re-run "with a fix" without a filed change record and Duho's ruling.
