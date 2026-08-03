# GORU BRIEF — REAL-NLI B1 mechanical verification

Role: Goru / mechanical verifier.
Read the master brief: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/quintet-real-nli-b1-20260703/QUINTET_REAL_NLI_B1_MASTER_BRIEF.md`

Task:
- Verify exact file presence, JSON validity, row counts, model count, done markers, and safety ledger fields.
- Confirm each model-specific validation has rows_loaded=45 and b1_real_nli_run_complete=true.
- Confirm no artifact claims Step 8 prose was written or automatically unlocked.
- Write report to `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/quintet-real-nli-b1-20260703/GORU_REAL_NLI_B1_MECHANICAL_REPORT.md`.

Verdict format: PASS | PASS_WITH_PATCHES | BLOCKED.
Required marker: `GORU_REAL_NLI_B1_MECH_DONE_20260703`

Allowed scope only: the master brief, comparison packet, Step 7a artifacts/reports/validation/scripts, claim ledger JSONL. No unrelated brain/scratch files.
