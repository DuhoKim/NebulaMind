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

Also mirrored since the 2026-08-20 overhaul: `nm_audio_publish.py` (queue.json
publisher — monotonic seq, atomic writes, quiet hours 22:30-08:00 KST,
transcript sidecars, speaker identity), `nm_morning_digest.sh` (force-live
first-sound-of-the-day), `voices.json` (single voice registry: Hwao=shimmer,
Tori=nova, Blanc=onyx), `nm_say.py`, `nm_audio_index.py`, `nm_audio_align.py`.
Not mirrored: `nm_audio_route.sh` (orphaned pre-overhaul router, no callers).

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

## Slides (default since 2026-08-20)

Per FEATURE_SPEC_AUDIO_SLIDES_20260820 (Duho: "let's make it as a default
feature for audio report"). Every reading gets a deck without the speaker doing
anything:

`nm_audio_publish.py` spawns `nm_report_postprocess.sh`, which runs
**align → derive deck → rebuild index** in that order, off the critical path:

- `nm_audio_align.py` (MUST use the hermes venv python — system python3 has no
  faster_whisper) writes `<stem>.times.json` with per-sentence end times.
- `nm_deck_derive.py` turns transcript + times into `<stem>.deck.json` in Tori's
  podcast DECK schema. Two rules are enforced mechanically, not trusted: every
  slide time must equal a real sentence start, and **every number in the deck
  must already appear in the transcript** — invented numbers are rejected and a
  deck with under 3 surviving slides is discarded entirely.
- Decks are cached: an existing `.deck.json` is never re-rolled or re-billed.
- Failure is always non-fatal — the reading archives audio-only, as before.

`listen.html` and `archive.html` render decks with Tori's podcast look (cyan
kicker, amber numbers, clickable time chips that seek the audio).

Captions recovered by `nm_audio_backfill.py` (machine transcription of old
readings whose text was never saved) carry an `.asr.json` marker and show an
"auto-transcribed" badge — a guess at what was said is never presented as the
written record.
