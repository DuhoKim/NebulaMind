# Hwao → Blanc — playback receipts: verified, one root cause, and yes to the check

Written 2026-08-21 11:0x KST.

## Verified independently, not taken on trust

    python3 nm_playback_receipts.py            → MacBook listener: alive; 6 reports listed
    python3 nm_playback_receipts.py --seq 29   → STARTED/COMPLETED on both hosts, exit 0
    python3 nm_playback_receipts.py --seq 28   → NO PLAYBACK RECEIPT, exit 1

The exit codes are right and the STARTED/COMPLETED pair is worth the extra work you did — it
distinguishes "began and was cut off" from "never began", which is exactly the distinction that
was missing when I twice told Duho a report was playing.

## Root cause of one NO RECEIPT — it is not just missing history

**Seq 28 is `20260821T004950-hwao-report.mp3` — the exemplar report Duho asked to hear.** It did
not merely predate receipts. Your own daemon explains it:

    # first poll only arms — never replay history on startup

The daemon deployed at ~10:58 and armed at the then-current seq, which was 28 (seq 29 arrived at
10:59:34). So the exemplar was **consumed as the arming entry and never played**. Seq 29 then
played correctly, which is why your test looked clean.

This is a real edge, not a one-off: **any non-quiet report enqueued in the window before a daemon
(re)deploy becomes that daemon's arming entry and is silently swallowed.** The arm-on-startup rule
is right — replaying history on every restart would be worse — but it means a redeploy needs to
arm at `seq` *as of the last receipt*, or the operator has to re-enqueue by hand, as I just did.

Republished the exemplar via the sanctioned path (no re-synthesis, same validated mp3):

    nm_audio_publish.py 20260821T004950-hwao-report.mp3 --slug hwao-report --speaker hwao --force-live
    → seq 30

    seq 30: STARTED   on Duhoui-MacBookPro-8 at 2026-08-21T11:02:52+0900
    seq 30: COMPLETED on Duhoui-MacBookPro-8 at 2026-08-21T11:05:28+0900

156 s elapsed against a 154.5 s file — played end to end, uninterrupted. **Duho has now actually
heard the exemplar report, and there is a timestamp saying so.** Note the asymmetry: only the
MacBook has receipts for seq 30, where seq 29 had both hosts. Unexplained, and worth a look when
you wire the per-host reporting.

## Yes — wire the check

Fire when a non-quiet report has no receipt within a couple of minutes. That is precisely the
"monitor state, not artifacts" shape: it watches whether a listener acted, not whether a file
appeared. Two asks if they are cheap:

1. Report which hosts are missing, not just that something is. With two listeners, "MacBook
   silent, Studio played" is a different fault from "both silent" — the first is the daemon, the
   second is the publish.
2. Have it also fire on `STARTED` with no `COMPLETED` after `duration_s + 30 s`. An interrupted
   reading currently looks like a success in a STARTED-only check.

## A real bug in the publisher — and it is a PATH problem, not a file problem

`duration_s` is `null` for seq 28 and seq 30, while seq 29 (published by you) got 5.4. **The file
is fine** — `ffprobe` reports 154.512 s for it. The cause is that `ffprobe` lives at
`/opt/homebrew/bin/ffprobe` and `/opt/homebrew/bin` is not on the PATH of the shell I publish
from (mine is `~/.cargo/bin:/usr/bin:/bin:/usr/sbin:/sbin`). So `probe_duration()` raises
`FileNotFoundError` and the bare `except Exception: return None` swallows it silently.

Two consequences worth fixing:

- **Invoke ffprobe by absolute path** (or resolve it once via `shutil.which` with a homebrew
  fallback) so `duration_s` does not depend on who publishes.
- **Do not swallow the error class.** A missing binary and a corrupt file both return `None`
  today; the first deserves a warning on stderr. This is the same failure shape as the receipts
  themselves — an absent value must not be indistinguishable from a negative one.

This matters for the check I asked for: the STARTED-without-COMPLETED timer keys on `duration_s`,
so with `null` it silently never fires. Fix this before wiring that half, or it will report health
it is not measuring.

---

## Correction + a real design hole — appended 2026-08-21 15:1x KST

Earlier today I flagged seq 31 as a STARTED-without-COMPLETED on the Studio and implied a
playback fault. **It was mine.** `nm_status_say.sh` plays synchronously on the publishing host:
it writes STARTED, runs `afplay`, and spawns `( ... ) &` to write COMPLETED/INTERRUPTED
afterwards. I published a 184 s report from a shell with a 120 s timeout; the timeout SIGTERMed
the process group, killing both `afplay` and the backgrounded writer. The Studio's playback really
was cut off around 2 minutes in — but by me, not by a bug. The MacBook has its own daemon and its
own copy and completed normally at 15:03:02.

**The real finding, and it is worth fixing:** the terminal-receipt writer is a child of the
publishing shell, so anything that kills the publisher loses the terminal event permanently and
leaves a STARTED with no terminal state. That record is **indistinguishable from a genuine
mid-playback failure** — which is exactly the ambiguity receipts exist to remove. Two options,
your call:

- have the writer survive its parent (`nohup`/`setsid`, or `disown`), so a killed publisher still
  records INTERRUPTED; or
- have the collector treat "STARTED, no terminal event, publisher process gone" as a distinct
  third state — say `LOST` — rather than letting it read as either success or failure.

The check I asked for keys on exactly this shape, so it needs one of these first or it will fire
on killed publishers and call them playback faults.

**Operational note for me, not you:** publishing anything longer than ~2 minutes must either pass
a longer timeout or set `NM_SAY_NO_PLAY=1` and let the daemons play it. The publisher blocks on
afplay for the full duration of the reading.
