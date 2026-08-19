# Resume after reboot — stopped deliberately 2026-08-18 16:17 KST

Stopped with SIGTERM before a macOS update, not crashed. Clean: 0 unparseable receipt lines.

    receipts at stop   27280 / 60308
    last brick         0951m457
    block event        none

## heartbeat.json is STALE — do not trust it

It still reads `state: RUNNING` because the process was killed between heartbeat writes. **The state
is `receipts.jsonl`, not the heartbeat.** On start the script re-reads it and never re-requests an
already-receipted brick, so resuming is safe and idempotent.

## To resume

From this directory:

    cd /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_harvest_20260817
    nohup /usr/bin/python3 nm_checksum_harvest.py >> harvest_stdout.log 2>&1 &

It will print `harvest start <utc>: N/60308 already receipted` — check that N matches the count
above before walking away. It respects the frozen §5.4 windows on its own (20:00–08:00 US/Pacific
weekdays, any hour at weekends) and will pause itself outside them.

## Do NOT

- do not delete or rewrite `receipts.jsonl` — it is the only state
- do not resume if `BLOCK_EVENT.json` appears; that needs Duho's decision per §5.4.6
- do not raise the pacing to catch up. The rate is frozen and a reboot is not a reason to hurry.
