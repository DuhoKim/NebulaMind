# Overnight spin-parity — tick 1 status (01:23 KST, 2026-08-12)

**The chain completed before this tick fired.** All four artifacts landed between 00:13 and 00:55;
Kun's gate was dispatched at 00:20 rather than waiting for 01:23. Nothing was pending at tick time.
All four seats idle, no permission prompts stuck, no seat dead.

| artifact | bytes | landed |
|---|---:|---|
| `reviews/LANA_SPIN_DESIGN_BRIEF_20260812.md` | 20,778 | 00:13 |
| `reviews/GORU_SPIN_DATA_SURVEY_20260812.md` | 5,890 | 00:13 |
| `reviews/KUN_SPIN_DESIGN_BRIEF_GATE_20260812.md` | 9,385 | 00:22 |
| `reviews/TORI_SPIN_DATA_ACCESS_CUSTODY_20260812.md` | 21,926 | 00:55 (corrected rewrite) |

## Kun's gate (item 2 of this tick — already answered)
`PASS AS A DESIGN BRIEF; NOT A PREREGISTRATION FREEZE; NO EMPIRICAL SKY RUN YET.`
Three-tier verdict respected: label-table reanalysis `NOT_WORTH_DOING_YET`; image-level
custody-audited mirror-controlled preregistered fixed-axis test `WORTH_SCOPING`; immediate
empirical run `BLOCKED` until a separate preregistration artifact freezes every open value.
Acceptance/rejection regions are present and pre-declared at both published axes — Longo
`(l,b)=(52°,68.5°)`, Shamir `(RA,Dec)=(132°,32°)` — with `REPRODUCED` / `REJECTED-AT-CLASS` /
`INCONCLUSIVE` / `INCONCLUSIVE-BY-POWER` branches, so ambiguity is forced to INCONCLUSIVE rather
than narrated into support. Kun records the kill switches as "real switches, not decorative
caveats". Exact numeric thresholds are still proposals pending the §7 power estimate — which is
precisely why he passed it as a design and not as a freeze.

## Orientation custody (item 3 — the fact that decides buildability)
**Goru: `ALL CANDIDATES FAIL`. Kun ruled that standard over-strict, and Tori settled it empirically.**
Kun's correct standard: the archive must provide public calibrated pixel data with intact per-image
WCS *sufficient for us to compute pixel-to-sky parity ourselves* — we run the mirrored control, so a
survey publishing its own is not required. "Only rendered images with no WCS or unverifiable
orientation" is the real failure condition.

Tori then live-tested rather than citing documentation: **DESI Legacy DR10 returns an anonymous FITS
cutout** — 5,760 bytes, float32, TAN WCS, hash recorded, file retained at
`reviews/_tori_spin_access_evidence/legacy_dr10_one_test_cutout_r_16px.fits`.
Her own corrected grade, and it is narrower than Hwao first reported: this **passes the exact
FITS/WCS delivery gate only — not end-to-end parity/injection custody**, which remains a separate
future gate. HSC PDR3 registration-gated, exact delivery UNDOCUMENTED. SDSS SkyServer returns
rendered JPEG (SAS corrected frames do carry WCS). PS1 anonymous FITS documented but UNTESTED, with
obsolete PC WCS, RADESYS and polar caveats. Verifier: 22/22 sources quote-backed, 61% coverage.

## Incidents (all Hwao's, all disclosed and repaired)
1. Killed `tori-overhaul` at 00:11 by sending Ctrl+C to an **idle** hermes pane — that exits the CLI.
   Rebuilt as `hermes -p tori2 --yolo` inside a zsh shell. (`-Q -q` from memory is not a valid flag.)
2. The scratchpad dispatcher reported `DISPATCHED` against the dead pane, because an empty pane reads
   as "static". A session-existence guard is now installed; it refuses rather than reporting success.
3. Rebuilt her in the repo root instead of the lane, so lane-relative paths — including her output
   path — resolved to nothing. She disclosed the missing prerequisite rather than fabricating it.
   Her root-written artifacts were moved into the lane at 00:38 (hash verified across the move) and
   the disclosure reached her at 01:00.

## State
Nothing published, accepted, acquired, or run. Next valid step per Kun: a non-sky-statistic
feasibility/custody spike, then a preregistration freezing every open number before measurement.
Awaiting Duho.
