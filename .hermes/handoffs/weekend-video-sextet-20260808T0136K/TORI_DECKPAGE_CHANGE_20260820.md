# Tori → Blanc: I changed a shared script — nm_status_say.sh (Duho-authorised)

Disclosing as I act, not after. Duho, verbatim: *"yes, fold it into nm_fable_say.sh"*.

**What happened first (the reason).** Duho asked me to play a queued reading. I played
`latest.mp3` and **Hwao's** reading came out instead of mine — Hwao published at 23:24:55 KST,
48 seconds after my file was routed at 23:24:07, and `latest.mp3`/`latest.txt` point at whoever
wrote last. I caught it only because the fetched byte count disagreed with the file I had routed.
With three of us publishing into one `status-audio/`, that is now the normal case.

**The change — two files, both additive.**

1. **NEW** `reports/status-audio/deck.html` — a generic player. `deck.html?f=<stem>` loads that
   reading's `<stem>.mp3` and its built `<stem>.deck.json` and renders your slides against it.
   - It consumes **your** pipeline's output, not the authored deck: it uses the
     alignment-snapped `t` values and the pre-rendered `svg` your `nm_deck_build.py` emits.
     Verified on `20260820T230754-tori-report`: times came through as 0 / 6.68 / 20.5 / 33.82
     (my authored 9 / 21 / 33, snapped by your aligner) and the badge SVG rendered at 778×83.
   - It polls for the `.deck.json` for ~12s, because post-processing is async and the page can
     open before the deck exists. No deck → it says "audio only" and still plays.
   - It plays via `decodeAudioData`, **not** an `<audio>` element, because that element does not
     decode in Duho's MacBook Chrome. `listen.html` line 72 uses one — worth your knowing.
2. **EDITED** `scripts/nm_status_say.sh` — one added `echo` (plus a comment explaining the race).
   It now prints the stable `deck.html?f=<stem>` URL **in addition to** the `latest.mp3` line,
   which I left untouched. `latest.mp3` is right for your self-polling `listen.html` — that page
   is *meant* to track the newest — and wrong for "play that reading".
   - backup: `scripts/nm_status_say.sh.pre-deckpage` (sha256 b85f8b85c9eb6935…)
   - `zsh -n` clean; all three assets serve 200 over the tailnet.

**Nothing removed, nothing renamed, no behaviour changed for you or Hwao** — same mp3, same
publish path, same queue, same quiet hours, one extra line of stdout. If you would rather own
`deck.html` and fold it into the archive index, take it; I built it because Duho was looking at a
bare directory listing while a reading played.

One loose end I left rather than cleaned: `reports/status-audio/play-20260820T232407.html`, a
one-off page I generated before finding your deck pipeline. `deck.html` supersedes it. I did not
delete it because Duho may still have it open — bin it whenever.

Also note `reports/status-audio/play.html` is stale: 19 lines, hardcoded to
`status-20260810T1049.mp3`. Not mine, not touched.

— Tori, 2026-08-20 23:5x KST
