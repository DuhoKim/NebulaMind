```

**Required mechanism change (one line, same blocker key)** — without it the supplement list is never evaluated. In `journal_metrics()` (live line 281), replace:

```python
        "numeric_invariants_missing": [x for x in NUMERIC_INVARIANTS if x not in flagship_text],
```

with:

```python
        "numeric_invariants_missing": [x for x in NUMERIC_INVARIANTS if x not in flagship_text]
        + [x for x in SUPPLEMENT_NUMERIC_INVARIANTS if x not in supplement_text],
```

`classify_integrity_blockers()` needs no change (it already fires on a non-empty list). Note for the integrator: the running process loaded these constants at start; editing the script does **not** affect PID 45665 mid-run. Apply at sprint end or as the seed config of the next sprint (see section d).

### (a.3) Mapping table — manifest entry → audit entry (all 105 entries)

Legend: "covered" = already caught presence-level by the live 6-entry list (flagship only); "NEW" = added by this proposal; `numeric_token` rows are manifest-gate-only. Cycle-5 check = exact occurrence count against the hash-pinned snapshot (token rows: presence).

