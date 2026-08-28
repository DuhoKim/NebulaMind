# Adversarial scientific review scope

Review only; do not write files or mutate the repository.

## Proposal under test

- `STORYBOARD_PROPOSAL.json`
- `visual_proposal_v4/manifest.json`
- `visual_proposal_v4/states/*.png`

All are under:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lane-fesc-zsweep/worker-yui/`

## Frozen sources

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/TREND_RESULTS.json`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/MERGED_FESC_ZSWEEP.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/fesc_zsweep_trend.png`

## Required attacks

1. Independently verify the exact meanings and values of `z_c=8.045`, `z_m=6.328`, `z_c=7.615`, both bootstrap intervals, and 66/83/93% at z=7/8/9.
2. Look for any conflation of median-curve crossing with closure-envelope crossing.
3. Look for any expansion of the no-SFRD-tail test into an all-assumptions or worst-case claim.
4. Check that bands and percentages are described as conditional model/systematic quantities, not observational confidence or real-world probability.
5. Check that every visual geometry is recoverable from the frozen numeric source.
6. Check that the proxy-transport limitation and no-measurement status are prominent enough.
7. Check for omitted conditions that would materially change a paper-naive interpretation.
8. Return `PASS`, `MINOR`, or `BLOCK`, with exact source-backed findings.

Do not judge an encoded MP4 or audio: neither exists in this worker packet.
