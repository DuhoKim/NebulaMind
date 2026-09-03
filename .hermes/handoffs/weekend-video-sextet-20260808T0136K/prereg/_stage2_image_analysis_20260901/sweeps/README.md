# DR10-south local-sweep fallback

This is the measurement-only inventory for the completeness gate’s named local-sweep fallback. No sweep payloads were downloaded, and the fallback is not implemented or activated in this round.

A later, separately authorized implementation would download only the `710` manifest entries, verify each against NERSC’s published SHA-256 and recorded byte size, route each target position to its 5° × 5° sweep box, read matching Tractor rows locally, and reproduce the gate’s match radius, column selection, ordering, null handling, and receipt semantics. Before any use, the route must be pinned and refereed via `nm_referee_dispatch.sh`; the running TAP crossmatch and `completeness_gate/artifacts_full` remain authoritative and untouched.

Footprint (a) uses `scratch/gz1_parsed.csv.gz` with the assigned-brick rectangle rule from `completeness_gate/prior_unresolved_13725.json`; footprint (b) uses the 65,060-row `../_successor_build_20260824/acquire/positions_selected.csv`. Remote metadata: [DR10 south sweep 10.0](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/) and [published SHA-256 manifest](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/legacysurvey_dr10_south_sweep_10.0.sha256sum).
