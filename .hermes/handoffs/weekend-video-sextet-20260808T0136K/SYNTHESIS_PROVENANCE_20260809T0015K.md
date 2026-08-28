# v3 synthesis — who actually ran it, and the interpreter the record omits

Filed 2026-08-09 00:15 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"run synthesize_v3.py"*.

This corrects a provenance gap in
`integrator/canaries/spin-method-overhaul-canary-20260808T1959K/BLOCKER.json`, which records
`RESOLVED_STUDIO_AUTH_STORE_RESTORED` with `execution_proof.fresh_sentence_syntheses: 27` but does
not say who executed them or under which interpreter. Both matter for Kun's reproducibility row.

## Two independent faults, not one

Auth restoration at **23:58 KST was necessary but not sufficient.**

1. **Auth (fixed 23:58 by Duho).** Login had been done on `Duhoui-MacBookPro-6`; the work runs on
   `Duhoui-MacStudio`, and the two keep separate `~/.hermes/auth.json`. Correctly recorded.
2. **Interpreter (never recorded).** At **00:02:19 KST** the integrator ran `python3
   synthesize_v3.py` and it died in **0.1 s** — too fast for a network call. `/usr/bin/python3` is
   **3.9.6**; `tools/managed_tool_gateway` uses PEP 604 `X | Y` annotations needing **3.10+**, so it
   fails at *import*, before any gateway logic. `audio_v3/` was never created.

The second fault mimics the first: both surface as "synthesis doesn't work" immediately after a
gateway problem, which invites the conclusion that the gateway is still down. It is not.

## What was actually run

    /Users/duhokim/.hermes/hermes-agent/venv/bin/python3 synthesize_v3.py   # Python 3.11.15

Executed by this seat at **00:02–00:04 KST**. All 27 sentences synthesized on the first attempt,
Alloy 1.18, `gpt-4o-mini-tts`, one exact sentence per call. Gateway verified resolving beforehand
(`https://openai-audio-gateway.nousresearch.com`) with a no-synthesis probe, so no credit was spent
testing. Receipt: `audio_v3/synthesis_receipt.json`.

Nothing else was run by this seat. `assemble_audio_v3.py`, `build.py --render`, and `qa_encoded.py`
were all executed by the integrator, which switched to the venv interpreter itself for the render.

## Correction to the recorded resume command

`BLOCKER.json.next_command_after_restore` reads `python3 synthesize_v3.py`. **That command cannot
succeed on this host.** Anyone replaying it will reproduce the 0.1 s failure and mis-diagnose it as
an auth problem. The reproducible command is the venv-interpreter form above.

Only synthesis needs 3.11 — `assemble_audio_v3.py`, `build.py`, and `qa_encoded.py` carry no Hermes
imports and compile cleanly under 3.9.

## Collision check performed before running

No `synthesize_v3.py`, `assemble_audio_v3.py`, or `build.py` process was running; `audio_v3/` did
not exist; the integrator pane had just failed and was deliberating. The script is per-file
idempotent (`if not output.exists()`), so a concurrent integrator retry would have skipped completed
sentences rather than double-spending.

## Gates

Nothing outside the candidate directory was written by the synthesis run. No upload, no publication,
no cockpit or `frontend/public` write, no Git write, no provider or billing change — the restored
entitlement was used, not modified, and no fallback voice was substituted.
