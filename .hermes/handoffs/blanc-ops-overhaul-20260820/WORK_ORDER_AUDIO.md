# Work order — audio report system (from P0 survey, 01:4x KST)

Executor: Blanc (these are my live scripts; small, high-blast-radius — not
delegating the queue semantics). Review: one gpt-seat adversarial pass.

## Core (must ship tonight)

A1. **Transcript regression fix** — `nm_status_say.sh` has `$text` in hand;
    write `<stem>.txt` + `latest_transcript.txt`. Re-enables transcripts,
    alignment, sentence highlighting for all future readings. Also invoke
    `nm_audio_align.py` backgrounded (it needs the .txt).
A2. **Kill the single-slot race** — replace latest latch with `queue.json`:
    monotonic seq, ordered entries {seq, file, slug, speaker, voice, stamp_kst,
    duration_s, transcript, quiet}. Written via temp-file + atomic `mv`.
    Consumers (listen.html, nm_listen_daemon.sh) track last-played seq and play
    ALL unplayed entries in order — a 3-report burst delivers 3 readings, not 1.
    Keep latest.mp3/latest.txt as legacy mirrors (written after queue).
A3. **voices.json** — single registry (seat → voice, display name, color,
    gender). Consumed by nm_fable_say.sh, nm_say_cast.py, nm_audio_index.py,
    listen page. Ends the three-way table drift (cast table disagrees with
    fable table today).
A4. **Quiet hours** — in nm_status_say.sh: between 22:30–08:00 KST (override
    NM_QUIET_OFF=1), render + archive + queue with `quiet: true`, no afplay;
    daemons/pages skip quiet entries for playback but list them. Ends the
    "remember NM_SAY_NO_PLAY" honor system.
A5. **listen.html v2** — regenerate with speaker identity (name + voice + color
    from queue.json), live transcript of the current reading, queue-aware
    playback (plays every missed reading in order), still one-click arm.
A8. **Morning digest** — `nm_morning_digest.sh`: collects overnight quiet
    entries + a summary text argument, renders one onyx reading, queues it
    non-quiet at/after 08:00. Used by this campaign's 08:02 handover.

## Stretch (if the night allows)

A6. Index performance: duration manifest cache (stop 192 ffprobe spawns per
    reading), background the index call, log to status-audio/index.log.
A7. Retention: `_tests/` subfolder for test-slug artifacts (testA/B/C, canary,
    castdemo, tickB…) excluded from archive counts; note 296 MB/10 days growth
    in handover for Duho's retention decision (no deletion tonight).
A9. edge-tts fallback in nm_say.py (lift the engine from nm_paper_tts.py) so a
    $0 Nous balance degrades instead of muting the whole system.
A10. Mirror ALL audio components into tools/audio-reports/ + add plist
    StandardOut/ErrPaths + daemon logging.

## Update daemon deployment

nm_listen_daemon.sh changes (queue-aware) must be redeployed to the MacBook via
SSH (duhokim@100.75.47.116) — authorized install path from 08-19. Studio side
is served files only. Mac Pro stays excluded.
