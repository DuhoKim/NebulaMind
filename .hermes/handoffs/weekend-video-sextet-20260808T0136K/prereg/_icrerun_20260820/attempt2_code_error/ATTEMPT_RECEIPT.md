# Attempt 2 custody — pre-receipt code error

The unchanged deterministic run completed all 1,000 identity rows and then stopped before any aggregate receipt because the R3 fixture referenced `synth_disk` through the old R4/R5 runner, which imports only `synth_spiral`. The traceback is preserved. No scientific predicate failed, no verdict was emitted, and the complete partial rows are retained unchanged.

Root cause: wrong module namespace for an existing hash-pinned generator symbol. Minimal repair: import the already-pinned frozen BS-3 generator module directly and call its `synth_disk`; no formula, probe, slot, seed, model, threshold, or production input function changed.

The next execution repeats the full fixed sequence. No failed probe is dropped or replaced.
