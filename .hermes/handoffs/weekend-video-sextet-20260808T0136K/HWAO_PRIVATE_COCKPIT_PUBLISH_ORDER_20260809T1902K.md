# HWAO ORDER — private Tailnet cockpit publish, four method-only canaries

Stamped 2026-08-09 19:02 KST under `DUHO_PUBLISH_PRIVATE_VIDEO_REVIEW_LINKS_20260809T1857K` ("publish so that
I can check"). **Tori executes and verifies.** Smallest possible operation: four file copies, nothing else.

## Mechanism — verified, not assumed

`render_ge_autopilot_dashboard_v2.py:323`:

```python
versioned = sorted((f.name for f in vid_dir.glob(f"{slug}-narrated-*.mp4")), reverse=True)
candidates = [(v, True) for v in versioned[:1]] + [(f"{slug}-narrated.mp4", True), (f"{slug}.mp4", False)]
```

The newest versioned cut wins by reverse **string** sort, so a `20260809` stamp outranks every
existing `20260808`. The renderer is in **watch mode** (pane health `watching`, ~20 s tick,
`ge-autopilot.html` mtime 19:00 KST), so it re-globs on its own.

**Therefore: no renderer restart, and no manual re-render.** Copy the files; the dashboard follows
within a tick.

## The four copies — exact bytes, new names only

| lane | SHA-256 | destination in `/Users/duhokim/HermesOps/cockpit/videos/` |
|---|---|---|
| brightend | `c772e643…` | `c41-brightend-uvlf-archival-gap-narrated-<STAMP>.mp4` |
| mzr-anchor | `c892f3fa…` | `c41-highz-mzr-calibration-anchored-narrated-<STAMP>.mp4` |
| fesc | `01a4249b…` | `fesc-zsweep-photon-budget-narrated-<STAMP>.mp4` |
| mzr-census | `d6014ac0…` | `mzr-archive-census-narrated-<STAMP>.mp4` |

Slugs are from `LANE_VIDEO` at line 258, not guessed.

`<STAMP>` is `YYYYMMDDTHHMM` **from `date` at copy time.** Do not pre-fill it — a proposal
pre-filled a future `frozen_at` earlier today and it blocked installation.

## Rules

- **Exact-byte copy, then re-hash the destination** and confirm it equals the source SHA. A copy is
  not verified until the bytes at rest are hashed.
- **Never overwrite.** New timestamped names only. Every prior cut stays, so this is reversible by
  deleting four files.
- **Do not touch `<slug>-narrated.mp4`.** Leaving the stable alias intact means rollback needs no
  restore.
- **Do not change `published.json`.** Consequence, deliberately: `published` stays false and
  these cards carry **no YouTube chip**. That is correct — they are not published.
- Do not restart or re-render. Verify by watching `ge-autopilot.html` mtime advance and the four
  card hrefs change to the new filenames.
- **spin-parity is untouched.** It is accepted and published; nothing about it changes.

## Truth labels — and one thing I could not do

Required labels: **method-only · scientific findings withheld · source freeze absent · not accepted
by Duho · private Tailnet review availability only.**

The renderer builds each card from lane data and has **no per-video label field**. Putting these
words on the card itself would require editing the shared renderer, which this direction does not
authorize and earlier gates exclude. So the labels travel with the links in the review note Duho
actually reads, and the cards carry no claim they cannot support — no YouTube chip, no published
URL, no acceptance marker.

**Flagging for Duho:** if you want the labels rendered on the cards, that is a shared-renderer
change and needs your say-so. I did not make it unasked.

## Still excluded

No YouTube or public internet publication. No `frontend/public/videos` replacement. No public
Baseline cockpit change. No product DB/API/wiki write, deploy/restart, Git write, cron,
browser/account/billing/provider/config change, or secret access. No `accepted_by_duho`.

Publication here means private Tailnet review availability. It confers no scientific authorization:
all four lanes remain fail-closed with `SOURCE_FREEZE` absent.
