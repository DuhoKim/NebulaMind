# HWAO CORRECTION ORDER — spin-parity private cockpit copy

Stamped 2026-08-09 19:14 KST under `DUHO_PRIVATE_COCKPIT_SPIN_LINK_CORRECTION_20260809T1913K`
("why spin parity video not updated?"). **Parent Tori executes. No second writer is dispatched.**

## My error

My 19:02 publish order said, in its own words, *"spin-parity is untouched. It is accepted and
published; nothing about it changes."* I wrote that as a safety rail — spin was the one finished
lane and I did not want it disturbed. But Duho asked to publish so he could **check**, and I
narrowed a review scope using a rule about *modification*. Being accepted is a reason not to
overwrite spin's bytes; it is not a reason to withhold it from review. The result is that the
dashboard has been serving `02fe11f0` (the 08-08 01:49 cut) while the accepted overhaul sat
unlinked.

Same shape as the day's other misses: a correct rule applied where its precondition did not hold.

## The one copy

| source | SHA-256 | destination |
|---|---|---|
| `integrator/canaries/spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4` | `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240` | `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-<STAMP>.mp4` |

Verified at source: 16,065,978 bytes, 187.695 s — matching the direction exactly. Durable verdict
`HWAO_FINAL_VERDICT_c5e7deed.md`, **ACCEPTED by Duho 2026-08-09**.

`<STAMP>` is `YYYYMMDDTHHMM` **from `date` at copy time**; do not pre-fill. A `20260809T19xx` stamp
outranks the current `20260808T0149` under the renderer's reverse string sort
(`render_ge_autopilot_dashboard_v2.py:323`), and the renderer is in watch mode, so it selects the
new cut on its own — no restart, no manual render.

## Rules

- Exact-byte copy, then **re-hash the destination and the served bytes** over HTTP.
- **Never overwrite.** New timestamped name only; `20260807T1901`, `20260807T1903` and
  `20260808T0149` all remain. Reversible by deleting one file.
- **Do not touch `spin-parity-census-narrated.mp4`**, the stable alias.
- **Do not change `published.json`.**

## The consequence to expect, and to leave alone

`published.json` records spin's published cut as `spin-parity-census-narrated-20260807T1903.mp4`
(`af47d95a…`, unlisted, `youtu.be/uch2gFhtd3g`). After this copy the card will show a **private
watch link two generations newer than its YouTube chip.**

That is truthful and must not be "fixed". The chip describes what was uploaded; the watch link
describes what is available for review. Replacing the YouTube video or editing the registry to
make them agree would be a public action nobody authorized — and the honest display is the one
where a stale published cut looks stale.

## Excluded

No YouTube replacement or upload, no `published.json` change, no renderer restart or manual render,
no `frontend/public/videos`, no public Baseline change, no product/DB/deploy/Git/browser/account/
billing/config/secret action. Spin's acceptance is unchanged; the four sibling lanes remain
fail-closed with `SOURCE_FREEZE` absent and unaffected by this correction.
