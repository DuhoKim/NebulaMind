# Entry-31 watch — machine pre-read of arXiv:2609.03157 (2026-09-07 04:03 KST; Tori, on Blanc's order of 03:52 KST)

**Hit:** 2026-09-04T18:04:47Z · arXiv:2609.03157 (submitted 2026-09-02) — "Observational selection effects on radio pulsars are minimal
for masses, but significant for orbits and spins". Surfaced by Hwao's disclosed by-hand positive-control run of `nm_ns_mass_watch.py`
(`HWAO_LANE_STATE_20260905.md`), which persisted `seen` and so consumed the new-flag; the scheduled cron (Tuesdays 10:00 KST, next
2026-09-08) will not report it again. Recovered from the hits row and the autopilot feed line the script wrote before the flag was consumed.

**Criteria applied (NS_MASS_WATCH_PREREG_20260902.md §2, verbatim in force):** FIRE_CANDIDATE = (M − 2.5)/σ ≥ 3 in a peer-reviewed
publication; RE_GATE = (M − 2.5)/σ ≥ 2 in any source, or any peer-reviewed M > 2.5 central at ≥ 1σ, or a GW secondary with resolved NS
identity at M > 2.5; HINT = P(M > 2.5) ≥ 5%; CLEAR = anything else. Identity must be resolved (radio/optical pulsar timing or light-curve
mass; not an unresolved GW secondary).

**What the abstract says (arXiv abstract page, read-only fetch):** a population study — simulated radio-pulsar timing observations,
detectability and measurability selection folded into hierarchical inference to extract the intrinsic distributions of pulsar mass,
companion mass, eccentricity, orbital period and spin period. Result: "Selection effects have minimal impact on the mass distributions,
but more significantly affect other parameters"; the observed mass distribution is bimodal (~1.3, ~1.6 M☉) with a cutoff above ~2 M☉.

**Band by the criteria: CLEAR (log only).** No new neutron-star mass measurement is reported — no M ± σ for any object — so none of
FIRE_CANDIDATE, RE_GATE or HINT can be tested. Preprint, no journal reference seen; under the lane's published-papers-only rule it could
at most raise a RE_GATE if it carried a mass, and it carries none.

**Bearing on the bar, stated plainly.** The bar turns on the maximum SECURE measured mass against 2.5 M☉. This paper says the observed
radio-timing mass distribution is close to the intrinsic one — selection does not hide heavier pulsars behind detectability or
measurability — so the observed maximum in that population is a fair proxy for the true maximum. It therefore LEAVES THE CRITERIA
UNTOUCHED (no number changes, no band moves), and it removes a loosening argument (that the true maximum might be systematically higher
than observed), which makes the recorded LIVE standing and its "drifting away from firing" trend slightly more robust, not less. Scope
limit: Galactic binary radio pulsars timed in radio; it says nothing about GW190814's secondary, which stays conditional.

**Not an adjudication.** No FIRED/LIVE set, no tier moved, no ledger change; the stamp is Duho's and a committee poll is his call (Blanc has
put the options to him). The hits row's bytes are unchanged; this pre-read is a sub-row beneath it and this file.

**Sweep ordered with it.** (1) Other hits lacking both a pre-read and an adjudication: NS_MASS_WATCH_HITS.md — none besides this one
(2609.02395 carries a pre-read and a committee CLEAR ruling). DESI_CURVATURE_WATCH_HITS.md — the 2026-08-31 hit arXiv:2608.24433 has neither;
the 25 rows of the 2026-08-23 first run are the seeding batch, of which one (2512.09486) carries a READ — that watch is Hwao's, reported
here as a fact, not acted on. (2) Watch `seen` state consumed by a manual run: NS watch — two manual runs, both disclosed (Hwao
2026-09-04T18:04:47Z in HWAO_LANE_STATE_20260905.md; Tori 2026-09-05T15:18:29Z in WATCH_POSITIVE_CONTROLS_20260906.md §2, a silent
control run that consumed nothing new); DESI watch — last run 2026-08-31T01:01:07Z is the scheduled Monday cron, no manual run found.
