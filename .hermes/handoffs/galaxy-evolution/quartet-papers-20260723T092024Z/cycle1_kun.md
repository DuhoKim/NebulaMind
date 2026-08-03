# Cycle 1 — Kun (gate / adversarial referee): ranking + Cycle-2 target

Read: both lane triages (Tori motivation, Goru rigor); manuscript bodies for #1 and #4 (PDF); review-loop + history logs for #1/#2/#4/#5. Posture: assume each paper is NOT publishable; find the single thing that keeps it out. Bar = (1) lit-grounded motivation, (2) non-circular result, (3) defensible conclusion.

## 1. Ranking by distance-to-publishable (closest first)

1. **#1 z9–10 deficit** — closest. Clears all three axes on the merits (grounded MZR-evolution dispute; genuine differential vs local anchor, robustness-tested across two anchors + two samples; refuses a detection claim). **Blocking gap: the headline result is a systematic-limited non-detection on N=6** — effective ~4.5σ, magnitude floored by the 0.15 dex Te zero-point. This is a *data-ceiling* gap, not a writing gap: ~6 strictly-unlensed z9–10 direct-Te galaxies is roughly all the literature has. Nearly done, but a Cycle-2 analysis push cannot move the ceiling.

2. **#4 TNG massive-galaxy abundance** — a hair behind, and the better *investment*. Clean non-circularity (TNG masses are predictions, JWST counts independent, massive-end at z5–6 not a TNG tuning target); honest bounded null that carves out the z>6 quiescent excess as unresolved. **Blocking gap: the null is cheap** — consistency is bought by a 0.28 dex shift against a ~1 dex budget that is *asserted from a DR literature summary, not committed to or made falsifiable.* If a referee rejects "~1 dex," the null collapses. This gap is closable by writing + one tiny numeric check.

3. **#2 f_esc landscape** — rigor-clean, strongest motivation (names both camps of a live dispute), no overclaim. **Blocking gap: no new discriminating datum** — it re-quantifies a known ξion/SFRD degeneracy and maps the envelope rather than narrowing it. Passes rigor + motivation, thin on originality. Not fixable in one cycle without a new anchor constraint.

4. **#6 TNG validation (calibration≠validation)** — real strength (two-level differencing genuinely defuses the tuned-on-what-you-test trap). **Blocking gap: the load-bearing SFR-over-evolution gap (+1.3–1.6 vs +0.8–1.0 dex) is quoted against an unmatched stellar-mass definition (TNG 2R½ aperture vs SED masses) and the same selection-biased observed anchor as #3** — an uncorrected systematic of magnitude comparable to the signal.

5. **#3 scaling relations** — **Blocking gap: the SFMS "elevation" (+0.8→+1.9 dex) is largely a product of the emission-line selection that biases high-z samples to high sSFR (input selection ≈ output signal), and the paper overclaims a "rapid early enrichment toward evolving equilibrium" scenario off a flat offset with ~0.5 dex scatter and n=46.** Selection artifact drives the headline.

6. **#5 MZR aperture/calibration framework** — **Blocking gap: no result at all.** Self-admitted G4 novelty FAIL; it synthesizes known, settled systematics and makes no measurement. Cannot satisfy the "non-circular *result*" axis because there is no result to be circular about.

## 2. Cycle-2 deep-dive target: **#4 (TNG massive-galaxy abundance)**

Not a rubber-stamp of #4 over #1 — the opposite reasoning. **#1 is closest to the bar, so it is the wrong place to spend the deep-dive:** its one remaining gap (N=6, Te-floor-limited) is a physical data ceiling a writing/analysis hour cannot move, and it has already been hammered across 6 referee cycles + two continuations. Marginal return on #1 ≈ a light reframe (below). **#4 is where a focused hour has the most headroom and the gap is actually closable:** its blocking defect is that the null is cheap/asserted, and the fix (commit to an itemized budget, state the falsification threshold, benchmark against the ΛCDM stress-test that made this a frontier) is exactly writing + one small numeric check. Closing it converts "consistency is cheap when 0.28 dex buys it" into a *falsifiable, benchmarked* null on the single most-cited JWST-vs-ΛCDM frontier — a genuine publishable result. Highest lift-per-hour, and it clears all three axes with margin rather than by a hair.

(Runner-up if #4 stalls: #1 — promote with the light reframe in §4, do not deep-dive.)

## 3. MUST-FIX list for #4 (each: defect → fix → verify)

M1. **The ~1 dex budget is asserted, not committed — the whole null rests on it.** → Replace the hand-wave with a single itemized budget table: name each component with a central dex value and sign (SED-code prior spread, IMF, nebular/AGN-LRD contamination, Eddington bias) and give one committed *central* budget (e.g. ~0.5 dex conservative / ~1 dex generous), not just "near ∼1 dex." → Verify: budget table sums transparently to the stated central value; every entry has a citation already in DR2. *(Writing; numbers already in the DR2 summary — no new analysis.)*

M2. **The null is not stated as falsifiable — Goru's core rigor gap.** → Add one explicit sentence + Table 1 annotation: "the z≃5–6 consistency revives as a tension if the true mass-systematic budget is below **0.28 dex**; the z≃7–9 point revives below **0.44 dex**." State the threshold *as the falsification condition*. → Verify: threshold values equal the Δ already in Table 1 (0.27–0.28 at s≈−1.6; 0.44 for z7–9) — cross-check they match the table cells. *(Writing + trivial arithmetic against existing Table 1.)*

M3. **No benchmark against the ΛCDM stress-test that made this a frontier (Tori's fix).** → Add the halo-mass-function / extreme-value ceiling (Boylan-Kolchin 2023 "Stress testing ΛCDM"; Lovell 2023) so the "erased by 0.28 dex" result is judged against the actual ΛCDM cumulative-SFE ceiling, not only against TNG's own SMF. Report the implied ε=M⋆/(f_b M_halo) post-shift and show it lands in the ΛCDM-allowed ε≈0.2–0.4 the paper already cites. → Verify: the post-0.28-dex ε at z5–6 falls below the BK23/Lovell extreme-value ceiling. *(Small numeric check — one ε computation from M⋆, halo mass, f_b≈0.157; flag for the worker if halo mass isn't already in hand.)*

M4. **TNG stellar-mass definition is unspecified and may not match the observed SED-mass basis** (the same mass-definition mismatch that is load-bearing in #6). → State which TNG mass is used (total subhalo vs 2R½ aperture) and add one line either matching it to the SED-mass convention or folding the definition offset explicitly into the M1 budget as a named component. → Verify: the chosen TNG mass aperture is named in §2 and its offset appears as a line in the M1 budget table. *(Writing; if a re-extraction of TNG aperture mass is wanted, that is a worker numeric task — otherwise fold into budget as a cited term.)*

M5. **Single-anchor fragility / TNG box statistics unstated.** The z5–6 null hangs on one observed point (Weibel 2024) vs one TNG value at z=5, and TNG100-1's 110 Mpc box gives limited massive-end counts at these z. → Add a one-line robustness note: n(>10^10.5) implies ~10–15 TNG objects in-box (state the count), and cite/add a second observed anchor if available so the null isn't a two-point comparison. → Verify: the in-box object count is quoted; if a second anchor is added, Δ is recomputed for it. *(Numeric: object count = n×V_box, V≈1.4e6 Mpc³ — trivial; second anchor is optional and only if a clean one exists.)*

M6 (light). **Redshift mismatch in the comparison** — TNG value quoted at z=5 vs observed "z≃5–6." → State the TNG value at the observed bin's median z (or bracket z=5 and z=6) so the like-for-like claim is exact. → Verify: TNG n quoted at matched z. *(Numeric lookup from the same TNG catalog the worker already used.)*

Priority: **M1 + M2 are the gate items** (they convert the cheap null into a falsifiable one — do these even if nothing else). M3 supplies the frontier benchmark. M4–M6 harden against the obvious referee shots.

## 4. Honest-disposition calls (shelve / reframe over polish)

- **#5 MZR framework → SHELVE as a research paper.** Not a polish problem, not fixable this cycle: it has no original result, so it structurally cannot clear the non-circular-*result* axis. Keep it only as a methods/review companion; never resubmit it as a frontier paper. Reframing has already been done once (SHELVE→review-cleared) and that is its ceiling. Do not spend Quartet cycles on it.

- **#3 scaling relations → REFRAME, do not polish.** The SFMS-elevation headline is a selection artifact and the enrichment-scenario language is unearned — polishing the current draft would produce exactly the kind of "polished reject" the lead dislikes. Honest options: (a) forward-model the emission-line selection onto the SDSS anchor *before* quoting any elevation (a real analysis task, not a Cycle-2 polish), and demote to a bounded offset; or (b) strip the SFMS-elevation claim and the scenario language entirely, keep only the metallicity offset as a bounded differential feeding #6. Given project memory ("z≈0 SDSS relations are anchors, not standalone papers"), option (b) folds #3 into #6 rather than shipping it standalone. Recommend: **reframe #3 as an input to #6, not a standalone submission.**

- **#1 → PROMOTE with a light reframe, not a deep-dive.** Its only real gap is a data ceiling. The cheap win is Tori's reframe: lead with the *contested claim it adjudicates* (rapid-early-enrichment outliers vs a metal-poor floor) instead of "we measured a deficit," so the N=6 bounded-consistency result reads as settling debate Y rather than as an underpowered measurement of X. That is a ~15-min intro/abstract rewrite, not a cycle.

- **#2 → hold.** Rigor- and motivation-clean but originality-thin; not shelve-worthy, but it needs a genuinely new constraint (a direct high-z ξion anchor) to become more than an envelope map — out of scope for a one-hour push.

---
**Gate verdict:** deep-dive **#4** (M1+M2 mandatory, M3 for the frontier benchmark, M4–M6 to harden). Promote **#1** with a light reframe in parallel. **Shelve #5**, **reframe #3 into #6**, hold #2. The portfolio's single highest-value cross-paper analysis remains Goru's: forward-model the emission-line selection — it simultaneously repairs #3 and de-risks #6, but it is an analysis task for a later cycle, not this hour's push.
