# Independent source-backed scientific review — final v4

## Frozen target

- Storyboard SHA-256: `49db67e9c565eef6c8ec0f53bf348e8ecf1f581168507ce6eb2fa24c4a44c182`
- Visual manifest SHA-256: `683460640960402716741303b38d833e1edece2a95806f912ba4c640f5f38622`
- Numeric source SHA-256: `8df9f25b5f8acaf22825d6ece958867562c7e37a73fe69aa8e8175fe0b7aa242`
- Reviewer: isolated read-only leaf subagent with frozen JSON/manuscript/code access and full-resolution v4 frames.

## Verbatim compact result

`V=PASS;N=zc=8.045 lower-Δ16 crossing, zm=6.328 median crossing, no-tail zc=7.615, 66/83/93%@z=7/8/9 correct;S=separate/unpaired no-tail;B=finite-MC/model/no-measurement/non-exhaustive explicit;P=audience paths no;R=none`

## Independent computation evidence

The reviewer independently compared `TREND_RESULTS.json` with `TREND_DATA.json` and reported maximum absolute deviation `2.220446049250313e-16`. An expanded v4 pass also replayed `make_trend_figure.py` and reported agreement to `4.44e-16` while recovering the exact fiducial, median, no-tail, bootstrap, and keyed-shortfall values. Its exact result is preserved at `archive/LATE_EXPANDED_SCIENTIFIC_V4.json`.

## Verdict

`PASS`; required fixes: none for the worker v4 static/storyboard proposal.

This does not promote v4 to an official candidate. Hwao's shared integration and encoded silent-canary QA gates remain closed.
