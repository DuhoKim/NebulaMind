# Hermes / Nous amount-first credit card activation receipt

Marker: `HERMES_NOUS_AMOUNT_FIRST_CARD_ACTIVATED_V1`
Completed at: `2026-07-22T10:40:04Z`

## Operator direction and approval

- User requested the usable credit amount instead of a percentage as the primary value.
- `restart usage monitor` authorized replacement of provider monitor PID 4900 only.

## Display contract

- Primary headline: `$43.12`
- Main card percentage: absent because total usable purchased credit has no fixed denominator.
- Monthly-plan sub-gauge: `100% used · $0.00 / $22.00 left`.
- Top-up sub-gauge: `$43.12 remaining · purchased balance`, with no percentage.
- Total-usable sub-gauge: `$43.12 available`, with no percentage.

## Runtime receipt

- Old provider monitor PID 4900: gone.
- Active provider monitor PID 14154: one process, tmux `ge-provider-usage-monitor`, cadence `60s` local / `300s` slash.
- Private renderer PID 9602: unchanged and still running at its `20s` cadence.
- No duplicate monitor or renderer process was present.

## Repeated-cycle verification

- Initial amount-first observation: `2026-07-22T10:38:02Z`.
- Next full monitor cycle: public advanced to `2026-07-22T10:39:17Z`.
- Private renderer mirrored the same observation at `2026-07-22T10:39:25Z`.
- Public status: HTTP 200; `big` is `$43.12`; top-level `fill_pct` is null; monthly sub-gauge remains `100.0`.
- Private status: HTTP 200; `big` is `$43.12`; top-level `percent` is null; monthly sub-gauge remains `100.0`.
- Public HTML: HTTP 200; amount appears in the main card; the main meter has no `aria-valuenow`; the monthly sub-gauge retains the 100% used label.
- Latest monitor record: `rendered: true`, lock status `PASS`, no stale writer.
- Final stable cockpit guard: `PASS`; local and public rich checks pass, public HTTP 200, and every protected file remains `uchg`.

## Tests

- Changed-path suite: `91 passed`.
- Python compile checks: passed.
- `git diff --check`: passed.

## Backup

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/provider-usage-monitor-restart-20260722T103746Z`

- 17 current artifacts copied before restart.
- `all_hashes_match: true`.
- Backup is outside the served roots.

## Explicit negatives

No renderer restart, purchase, top-up, billing/payment mutation, browser/account-page automation, DB write, SQL/apply, product deploy, public route redesign, Git action, cron job, cloud/GCP change, or unrelated process restart occurred.
