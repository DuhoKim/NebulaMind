# Per-Fable audio reports — versioned mirror

The LIVE copies run from `/Users/duhokim/HermesOps/scripts/` (not a git repo);
this directory is the version-controlled source of truth for the pieces the
OPS session owns. Deploy = copy the file back to HermesOps/scripts.

- `nm_fable_say.sh` — one report voice per Fable coordinator (2026-08-19):
  Hwao=shimmer (F), Tori=nova (F), Blanc=onyx (M). Usage:
  `nm_fable_say.sh <hwao|tori|blanc> "report text"`.
- `nm_status_say.sh` — the underlying pipeline (OpenAI TTS via the Nous-covered
  hermes gateway → timestamped mp3 in `HermesOps/reports/status-audio/` →
  `latest.mp3`/`latest.txt` refresh → afplay on the Studio → archive.html
  rebuild). Extended 2026-08-19 with `NM_SAY_VOICE` / `NM_SAY_NO_PLAY` and the
  archive-index rebuild (the archive had silently rotted 08-16→08-19 because
  nothing regenerated it).

Not mirrored (unchanged, pre-existing): `nm_say.py` (gateway TTS shim),
`nm_audio_index.py` (archive builder), `nm_audio_route.sh` (machine detector).

Listening: leave https://duho-macstudio.taila27502.ts.net/reports/status-audio/listen.html
open and press "Start listening" once — every new reading then auto-plays,
queueing behind one already in progress. The Studio speakers always play.
