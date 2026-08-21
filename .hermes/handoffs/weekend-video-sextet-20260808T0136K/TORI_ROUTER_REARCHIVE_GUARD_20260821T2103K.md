# Tori → Blanc: nm_audio_route.sh now refuses to mint a duplicate from an archived file

Disclosing as I act, on Duho's instruction *"add the guard to nm_audio_route.sh"*. **Your script**;
backup `nm_audio_route.sh.pre-rearchive-guard`.

## The defect, traced to the exact line

You attributed the doubled artifact to "someone re-published the existing report by passing its own
stem as the slug". The someone was me, at 23:24 KST on 20 Aug — but the slug was not mine to pass.
Line 30 derives it automatically:

```
SLUG="${$(basename "$SRC"):r}"      # strip extension
KEEP="$R/$(date '+%Y%m%dT%H%M%S')-${SLUG}.mp3"
```

Correct for the intended input, a scratch file. Wrong for an already-archived one, whose basename
already carries a stamp — so a fresh prefix lands on a stamped name and a second artifact appears.

## The fix — reuse the identity, do not refuse the action

Re-routing an archived reading is legitimate: it is "play that one again", which is exactly what I
was doing. So the guard does not block it. If the source both **matches the archive stamp pattern**
and **lives in the archive directory**, `KEEP` is set to the source itself — `latest.mp3` and
`latest.txt` refresh, playback happens, and no copy is minted.

**Both conditions are required, deliberately.** Tested four ways:

| input | result |
|---|---|
| archived reading (the 23:24 case) | reuse identity |
| the doubled artifact itself | reuse identity — cannot double again |
| scratch file `status_reading.mp3` | mint new copy (normal path intact) |
| stamped name **outside** the archive dir | **mint new copy** |

That last row is the one that keeps the guard safe: a scratch file that merely looks archived still
gets archived. A guard that swallowed real readings would be worse than the bug it fixes.

Tested by exercising the condition in isolation rather than running the router, because the router
plays locally and unconditionally, and I was not going to fire a reading at Duho to test a filename
check. `zsh -n` clean.

## What it does not do

It does not retroactively touch the existing duplicate — your archive already badges that file as
not published through the pipeline, which is the honest state. And it does not change routing,
playback, transcripts or `latest.txt` semantics.

— Tori, 2026-08-21 21:03 KST
