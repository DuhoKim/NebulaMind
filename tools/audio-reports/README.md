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

## Listening

Both machines auto-play natively — no browser needed:

- **Studio**: `nm_status_say.sh` afplays each reading directly.
- **MacBook**: `nm_listen_daemon.sh` runs as LaunchAgent
  `net.nebulamind.status-listener` (RunAtLoad + KeepAlive; installed via SSH,
  Duho-authorized 2026-08-19). It polls `latest.txt` every 8 s and afplays new
  readings; first poll after start only arms, so old readings never replay.
  Live copies: `~/.local/bin/nm_listen_daemon.sh` +
  `~/Library/LaunchAgents/net.nebulamind.status-listener.plist` on the MacBook,
  both also served from `HermesOps/reports/status-audio/` on the Studio.
  Reinstall/update: `curl -fsS https://duho-macstudio.taila27502.ts.net/reports/i | zsh`
  (that installer is `install-listener.sh` here, served as `HermesOps/reports/i`).
- **Stop**: `killall afplay` mutes the current reading;
  `launchctl bootout gui/$UID/net.nebulamind.status-listener` disables the MacBook daemon.

The listen.html / archive.html pages remain as browsable history (browser
autoplay needs one click per tab — that limitation is why the native daemons exist).
