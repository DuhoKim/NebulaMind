# BS-2a round 3 — reports

- `BS2A_CODE_GATE_CODEX.md` — CODEX, **NOT CLEAR**. One HIGH finding (crash instead of refusal).
  All 276 pairwise deletion probes caught; all five frozen constants independently recomputed
  without importing the module; could not make the verifier accept a bad receipt.
- **GPT56 produced no report.** It ran 38 minutes and exhausted its iteration budget mid-review,
  writing its findings only to the runner log, preserved here as `GPT56_UNFINISHED_runner.log`.
  `gates/BS2A_CODE_GATE_GPT56.md` was therefore never overwritten and still holds the **round-2**
  report — do not mistake it for a round-3 verdict.
  Its unwritten findings (all reproduced independently by Hwao before repair):
  1. `OverflowError` escapes the caught tuple — `float(10**400)` crashes instead of refusing.
  2. Missing evidence field crashes past its own refusal (same class as CODEX's finding).
  3. A lying `__eq__` in `schema_version` / `thresholds` / `evidence_sha256` was **ACCEPTED**.
  Its stated working assessment was NOT CLEAR. It completed 150/276 pair probes with none silent.
