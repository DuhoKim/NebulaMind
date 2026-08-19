# listen.html v2 spec (codex exec lane — Blanc overhaul 2026-08-20)

Rewrite /Users/duhokim/HermesOps/reports/status-audio/listen.html IN PLACE.
You may ONLY write that one file. Read first for reference: the current
listen.html (keep its visual language: dark #0f1115 bg, the pulsing dot,
centered column, the one-button arm flow), queue.json, voices.json, and
archive.html (for how transcripts render).

## Data contract
queue.json (same dir, poll every 8s, cache-bust with ?t=):
{ "version":1, "seq":N, "updated_utc":"...", "entries":[
  {"seq":n, "file":"<mp3 name>", "slug":"...", "speaker":"blanc",
   "name":"Blanc", "voice":"onyx", "color":"#ffd98e",
   "stamp_utc":"...", "stamp_kst":"2026-08-20 01:35:39 KST",
   "quiet":true|false, "transcript":"<txt name>"|null, "duration_s":5.6|null} ] }
Entries are oldest→newest, last 50. voices.json maps seat→{voice,name,color,role}.

## Behavior
1. One-click "Start listening" arm (browser autoplay gesture), exactly like now.
   On arm: record the CURRENT max seq as the baseline — do NOT replay history.
2. Every poll: play ALL entries with seq > lastPlayed AND quiet==false, in seq
   order, one after another — never cut off a playing reading; queue the rest.
   (The old page dropped all but the newest of a burst.)
3. While playing: show a colored speaker dot (entry.color), "Name — voice"
   (e.g. "Blanc — onyx"), the stamp_kst, duration, and the transcript: fetch
   entry.transcript from the same dir and render the text below the player
   (plain paragraphs, muted color, max-height with scroll).
4. Below: "Recent readings" list of the last 8 entries, newest first: colored
   dot, name, slug, stamp_kst, duration; quiet entries get a small "quiet ·
   queued overnight" badge and a click-to-play button (click IS a gesture, so
   playing on demand is fine even for quiet ones).
5. If queue.json fetch fails, fall back to the old latest.txt+latest.mp3 latch
   behavior (poll latest.txt, play on change).
6. Keep: the 12-line event log, the archive.html link, viewport meta,
   self-contained single file (no external scripts/fonts), works over plain
   http.server. Respect prefers-color-scheme light like the current page does.

## Verify
After writing, syntax-sanity: the file must be valid standalone HTML, all JS in
one <script>, no template literals containing "</script>". State what you
changed in 5 lines to stdout.
