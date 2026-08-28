# Seat availability — recorded honestly, 2026-08-08 13:20 KST

Per Duho: *"Record any unavailable seat honestly; do not fake the Sextet packet."*

| Seat | Session | Route | State |
|---|---|---|---|
| **Hwao** | this session | Fable 5 | ACTIVE (coordinator) |
| **Yui** (sole writer) | `yui-overhaul-integrator` | `~/.local/bin/yui`, openai-codex | **ACTIVE** — brief dispatched |
| **Lana** | `lana-overhaul` | `claude --model opus` | **ACTIVE** — brief dispatched |
| **Goru** | `goru-agy` | Antigravity / Gemini 3.1 Pro | **ACTIVE** — `GORU_OVERHAUL.md` already landed |
| **Kun** | `kun-codex-overhaul` | `~/.local/bin/kun-codex`, gpt-5.5 | **ACTIVE** — brief dispatched |
| **Tori** | `tori-overhaul` | `tori2`, Hermes | **ACTIVE** — brief dispatched; raised the DELEGATION blocker |

## Seats retired this pass — preserved, read-only, no authority

- **`yui-video-integration`** (Fable) — exhausted its Fable 5 limit before starting the overhaul
  build. Write authority **revoked** and recorded in `integrator/DELEGATION.md`. Verified idle; it
  produced no overhaul candidate. Its earlier work (the nine spin method canaries and the two
  sibling baselines) is preserved.
- **`lana-claude`** (Fable) — same limit. Preserved read-only.
- **`kun-overhaul`** (Kimi K3) — replaced rather than configured. It opened a provider-setup prompt,
  which is a closed gate, so it was **declined** and the session retired in favour of `kun-codex`.

No credits were bought. No provider or model configuration was changed. Every replacement used an
already-authenticated existing profile.

## Blocker caught and closed before the build

**Tori's preflight** found `integrator/DELEGATION.md` still forbidding *"TTS of any kind — canaries
are silent"*, which contradicted `HWAO_OVERHAUL_ORDER.md` §2 and `lanes/spin/STATUS.json`, both of
which now authorize Alloy narration for this method-only cut. My transfer banner had made it worse
by saying "everything below applies unchanged".

Reconciled: the blanket silent rule is superseded **for the spin method-only overhaul only**;
narration on any other lane's canary and narration of any blocked claim remain forbidden; audio
authorization does not touch reportability (`video_reportable_now` is still `false`). The original
02:02 KST quote is annotated as historical rather than edited. Verified across all three files.

That was my error to fix, and Tori was right to stop the build over it.
