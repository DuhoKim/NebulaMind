# Autonomous spin — closing report (14:06 KST, 2026-08-12)

Window: ~12:00–14:06. **The boundary held.** No empirical sky run, no real-galaxy handedness, no sky
statistic, no catalogue query, no bulk acquisition, no publication, no commit. Tori's receipt records
`sky statistic computed: false` and `EMPIRICAL STATUS: BLOCKED`. The one grep hit in the boundary audit
was that line itself — a declaration, not a breach. Five seats alive and idle at close.

The window was **productive, not stalled**: twelve artifacts, one design narrowing, one measured
instrument, one bound survey route, and two independent audits that each caught a real defect.

---

## (a) Did Kun pass V2, and is preregistration drafting authorized?

**Yes to both.** `reviews/KUN_SPIN_V2_REGATE_20260812.md` — `PASS FOR PREREGISTRATION DRAFTING`.
No sky run, no result, no publication, nothing accepted. One repair required and made: V2 §0 claimed its
boundary sentence appeared "verbatim" in §6; it was equivalent wording, not verbatim. Lana corrected it
and carried the correction openly as a provenance note. Kun's naming ruling — any later artifact must
read **"Longo-amplitude test"**, not "spin anisotropy test" — is satisfied by the draft's title.

## (b) Does a frozen preregistration exist, and are all values frozen?

**A draft exists; it is NOT frozen, by Kun's explicit hold.**
`prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md` (20,420 B).
`prereg/KUN_PREREG_DRAFT_GATE_20260812.md`: `PASS AS A PREREGISTRATION DRAFT STRUCTURE; HOLD FREEZE`.

On the specific question — he checked and found **"no major value silently frozen ahead of its
evidence."** The draft separates frozen rules from an explicit binding-slot register, so the freeze gate
can audit each slot. My own suspicion that only one `BINDING SLOT` marker appeared was wrong: it uses a
register, not repeated markers.

## (c) Is a route bound, and does it supply 100,000 accepted?

**Route bound. Yield NOT closed — and the two seats contradict each other, which is the window's most
valuable outcome.**

`prereg/TORI_SURVEY_ROUTE_BINDING_20260812.md` (32,888 B, SHA-256 `3f41b6d9…3d3a87`, verified
independently). Bound: **DESI Legacy DR10.1 South only** — `ls-dr10-south` generated FITS, pixscale
0.262, bands grz, size 256; DR10.1 sweeps row-matched to 10.1 photo-z; current
`survey-bricks-dr10-south`; Gaia DR3 external TAP. Distortion branch: **fail-closed** on
SIP/PV/CPDIS/DET2IM, no local-Jacobian branch.

**The contradiction she raised, and it stands:** Goru's ~175,000 was never an accepted-yield receipt.
Its 2,000,000 parent was an *uncited assumed count*; the 25% / 70% / 50% were multiplied assumptions.
DR10 actually holds **~2.8 billion sources**, so the question was never data volume — it is which frozen
cuts produce an arm-resolving parent, and **nobody has counted that**. She grades the fractions
`ASSUMED, NOT COUNTED` and names losses Goru omitted entirely: all-band/shape/WCS/covariate losses and
footprint variance.

Goru rewrote (`df08a525…`) and fixed four real defects Tori found — south-only footprint, `maskbits=0`,
`r<17.7`, the **−99 photo-z sentinel** that a bare `z_phot_median < 0.15` would have admitted, and
`FLUX_R>0` to exclude zero-flux DUP rows. That sentinel bug would have selected every photo-z failure
into the parent sample invisibly. Every surviving count in his receipt is now honestly marked
`[UNKNOWN — requires catalog query]`.

**Retention, however, is now measured and it is good.** `prereg/YUI_PRODUCTION_ESTIMATOR_RECEIPT`:
central **96.44%**, one-sided lower 95% bound **96.15%** (n=12,000 held-out synthetics), verified against
`train_results.json`. At the lower bound, 100,000 accepted needs a parent of only **~104,000** spirals.
**No S/N inversion** — retention rises with signal (89.1% → 99.1% → 99.7% → 99.4%) with **100% sign
accuracy in every bin**. The pathology found earlier was specific to the crude deterministic tracer,
whose properly-recalibrated retention collapsed to **0.089%** lower bound and was *inverted* in S/N,
revealing its acceptances as noise excursions and the spike's 7.8% as an artifact of a 240-null
calibration. Yui's caveat, unprompted and load-bearing: these are **synthetic** S/N bins; the real
DR10.1-south r<17.7 distribution must be mapped onto them, and PSF, blends and artifacts are not
simulated.

## (d) Kun's seven freeze conditions

| # | condition | status | artifact needed to close |
|---|---|---|---|
| 1 | exact covariate battery | PARTLY CLOSED | survey-bound spec: exact products, versions, maps, model implementations, hyperparameters, missing-data rules |
| 2 | survey route and scale | **PARTLY CLOSED** | route bound ✓; **accepted-yield receipt still open** — needs the parent row count |
| 3 | production estimator freeze | **CLOSED in substance** | weights hashed `83008c1c…`, τ=4.4006 calibrated on 8,000 nulls pre-measurement, retention measured, R1/R2/R3 receipts pass on the production raster |
| 4 | hand-check attenuation protocol | PARTLY CLOSED | exact strata, sample size, adjudication, uncertainty propagation into decision regions |
| 5 | no-resampling mirror rule | CLOSED at design level | unit-test receipt vs exact analysis raster — **now supplied** (mirror∘mirror byte-exact 200/200) |
| 6 | signed-zero rule | CLOSED at design level | code test receipt — **now supplied** (R3, value-equal, ordered comparison in acceptance path) |
| 7 | distortion policy | CLOSED at design level | route declares its branch — **now supplied**: fail-closed on SIP/PV/CPDIS/DET2IM |

## (e) What needs a decision from Duho

**One item, and everything else waits on it: the DR10.1 parent row count.**
It computes no handedness, no statistic and no positions, but it queries the real catalogue, which is the
line he set. Tori stopped there deliberately. Without it, condition 2 cannot close and the
preregistration cannot freeze.

Secondary, not blocking: 2 MCP servers need authentication in Yui's session (surfaced after his restart).

## Operational notes
- Yui hit 100% context with unsent text in his pane; restarted with `/clear` (not Ctrl+C, which is how
  Tori's session was killed at 00:11). All his artifacts are on disk and survived — weights 11.2 MB.
- Tori superseded her own binding receipt to remove an incorrect claim that Lana's §0/§6 repair was her
  prerequisite, and declined to assert Kun's gate covered Goru's newest hash since it predates it.
