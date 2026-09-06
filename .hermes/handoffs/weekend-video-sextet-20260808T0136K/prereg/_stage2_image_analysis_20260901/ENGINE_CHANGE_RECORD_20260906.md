# ENGINE CHANGE RECORD — codex seat moves to gpt-6-astra — 2026-09-06 09:47 KST

**Ruling (Duho via Blanc, 09:46 KST), verbatim:** "seems gpt 6 astra is available now, update codex cli and use the new version" / "update now" / "use astra for both". Blanc updated codex-cli in place at /Users/duhokim/.local: 0.146.0 → 0.153.4 (one installation), probed `gpt-6-astra` live (ASTRA_OK) before reporting it.

**What this does NOT do (recorded in Blanc's terms):** it does not retroactively touch V15. The selection rule is SIGNED (fdd9eedd…, 2026-09-06T00:04:07Z) and its gate history — 15 drafts, 30 seat reports — was produced under codex-cli 0.146.0 with the previous model. Those verdicts stand as verdicts about what they read, under the tooling they ran on. They are not re-labelled, not re-run to "match", and the signed rule is not described as cleared by astra.

**What it DOES do:** every referee run from now on uses codex-cli 0.153.4 with model gpt-6-astra, and every dispatch record carries the engine beside the ACCESS_SHA.

## Check requested: does the signed V15 name an engine or version this breaks?
No. The signed text contains no CLI version, no model name and no `-m`/`--model` flag. "codex" appears 8 times, every one an attribution in the gate-history annotations (e.g. "V4 added (codex, V3 gate)", "codex V13: a signed rule must not carry two selection algorithms") or in the authorship disclosure ("AUTHORED BY THE CODEX SEAT 2026-09-06 00:13–00:18"). Those statements describe what happened and remain true. No amendment question arises.

## Mechanics changed (lane-side; the HermesOps wrapper `nm_referee_dispatch.sh` is untouched)
- `_tmp_codex_as_agy_shim.sh`: SHA-256 before 9c981c12c3f91edc5bb268ed2e20df20a63e41e67a822cf2a34490b4ce999806 → after cf22663e85b54b8480d8a6d52cc9b40ea4fdb0b1f45835589becc694afa79378. Adds `-m gpt-6-astra`; writes `<report>.engine` = "ENGINE: codex-cli <version> model gpt-6-astra dispatched <UTC>" (report path parsed from the wrapper's own prompt) and prints the same line to stderr. Access-proof control unchanged.
- Agy dispatches: the dispatching command writes `<report>.engine` = "ENGINE: agy <`agy --version`> model <as configured> dispatched <UTC>" before invoking the wrapper (agy 1.1.27 today).
- `scripts/build_attempts_register.py`: new column "engines A / B (CLI, model)" per seat report — the `.engine` stamp when present; for the 30 historical reports, codex = "codex-cli 0.146.0, pre-astra model (not stamped at run time; Blanc relay 09-06 09:46)", agy = "agy (Gemini), version/model not stamped at run time". Register regenerated.

No referee run was dispatched by this change. Standing blockers unchanged: server-side branch protection with a refused force push; no beacon fetch, no draw, no fetch, no pixel.
