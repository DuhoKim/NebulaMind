FABLE_HARD_BURN_H3_INTEGRATION_PACKET_20260711T035354Z

# Runner/manuscript integration change-packet — rollup follow-up item 3

Burn `fable-weekly-hard-burn-20260711T035354Z`, lane H3. Written 2026-07-11 ≈04:30Z. **Proposal only — nothing here is applied.** Every referenced live file was read read-only; the running sprint (PID 45665, checked alive `Ss+` at 04:05Z) was not touched.

Live targets (read-only, hashes at read time 04:05–04:30Z):
- Runner/audit/prompt file: `<S>/run_weekend_journal_sprint.py` — 50,295 bytes, sha256 `b6795c05f3b790cc22644addcf2c42f7da33387d986f683c7193ccf94450efa2`, where `<S> = /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z`
- Canon base package: `<S>/candidates/cycle_05_package/` (flagship + supplement TeX; snapshot copies hash-pinned in P1 receipt: flagship `63b3920e…`, supplement `a4e3d66c…`)
- Manifest: prior burn `p1-rp1-invariants/INVARIANT_MANIFEST.json`, sha256 `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` (verified before use)

**Live status update discovered during preparation (read-only greps, 04:17–04:30Z), strengthening urgency:** the livelock is still active and has *widened* beyond the RCA's two cycles:
- `cycle_08` (results phase): flagship carries `[-1.334,-1.282]` ×4 and supplement `2.831` — the same re-derivation signature; `CYCLE_08_results_AUDIT.json` fails with `numeric_invariants_missing: ["[-1.334,-1.283]"]`.
- `cycle_09` (discussion phase, rebuilt from clean base): canon strings restored (`-1.283` ×4, `2.830`), but `CYCLE_09_discussion_AUDIT.json` fails with `numeric_invariants_missing: ["249,917", "24.0"]` — grep confirms both strings are **gone entirely** from the cycle-9 flagship. This is a third failure mode: outright deletion/rewording of canon numerals (carry-rule §5.5 class), not re-rounding.

Three distinct drift classes have now each caused a cycle failure: re-rounding (6,7,8), aggregate/referent rewrite (6), deletion (9). Sections (a) and (b) close all three.

---

## (a) Proposed extension of the runner audit `numeric_invariants` list

**Current live list** (`run_weekend_journal_sprint.py` line 109, verbatim):

```python
NUMERIC_INVARIANTS = ["8,146", "-1.309", "[-1.334,-1.283]", "249,917", "60,000", "24.0"]
```

**Check mechanism** (line 281): `"numeric_invariants_missing": [x for x in NUMERIC_INVARIANTS if x not in flagship_text]` — presence-only substring test against the **flagship text only**; any hit becomes integrity blocker `numeric invariants missing` (line 319). Two consequences the extension must respect: (1) supplement entries are dead weight unless the metrics line also tests `supplement_text`; (2) the audit is presence-level, weaker than the manifest's occurrence counts — the manifest pre-audit gate (RCA §5.6) remains the count-level check; this list is the runner-side backstop.

### (a.1) Coverage stats (mechanically derived by `tools/derive_audit_extension.py`; cross-validated 105/105 against the hash-pinned cycle-5 snapshot, 0 problems)

