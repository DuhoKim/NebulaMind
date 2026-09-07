# WORKER LAUNCH RECORD — profiles stated, as the efficiency update requires (2026-09-07 16:28 KST)
Profiles verified present as separate config files and RESOLUTION PROBED, not assumed: `/Users/duhokim/.codex/trio-routine.config.toml` (model gpt-6-astra, reasoning medium, `fast_mode = false`) and `trio-research.config.toml`. A probe run under `--profile trio-routine` returned rc 0 and reported **model gpt-6-astra, reasoning effort medium** — the profile's values, not the global xhigh/Fast default, so the flag resolves rather than silently falling back.

| worker | task | profile | state |
|---|---|---|---|
| pid 65824 (v44) | the REAL MEDIUM producer — bit-11 pixel perturbation, sign-flip rate, synthetic rasters | launched BEFORE this policy; settings preserved until safe completion | ACTIVE at 2026-09-07 16:28 KST (verified by process state, not by an absent output file) |
| pid 65827 (v45) | right-size the input manifest and runtime pins to the core registers | launched BEFORE this policy; settings preserved until safe completion | ACTIVE at 2026-09-07 16:28 KST |
| next (v43) | fold the implementation and manifest delta into A1 + refresh the sheet | **`--profile trio-routine`** — document upkeep and straightforward assembly, not scientifically difficult | STAGED, dispatches when v44 and v45 land |
| final review | focused review of the changed bytes only | **agy / Gemini via `nm_referee_dispatch.sh`** — a different engine that authored none of it; profile routing does not touch reviewer independence | pending the fold |
Job state is read from the process table AND the output, since an absent file alone cannot distinguish queued, active, failed and never-launched.

## 2026-09-07 17:08 KST — closed jobs and the launch fix, verified
| worker | profile | delivery | result |
|---|---|---|---|
| v44 MEDIUM producer | pre-policy settings | detached (old way) | `medium_perturbation.py` 10,439 B, sha256 `ea46478e…`, 32 tests + kit pass |
| v45 CORE registers | pre-policy settings | detached (old way) | CORE 27 real + 5 future groups, runtime 3 pins, readiness correctly FALSE at authoring |
| v46 consumer gap | **`--profile trio-research`** (it changes what the run path REFUSES — consequential, not clerical) | **harness-tracked background job `bo6u4ayxi`** | 122 tests + kit pass; CONSUMER-COMPLETE |
**THE LAUNCH FIX WORKS.** v46's completion notification woke me on exit. v44/v45 were detached and their panes described finished work as active for ~15 minutes; that is the failure this replaces. Every new launch uses the tracked mechanism.
**READINESS, and what it does NOT mean.** `ready_for_input_freeze` is now TRUE, and I checked it is a real gate rather than a label: `run_path.py:301` refuses unless it is True AND every pin check passes, with a test that a FALSE reading blocks. All 28 CORE real entries exist on disk; the 5 placeholders are genuinely later-stage. It means THE INPUT-STAGE FILES ARE READY TO FREEZE — not that the package is adopted, not that a run may start, and not that later-stage evidence exists.
