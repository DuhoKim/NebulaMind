# STEP 2 pre-registration — a standing watch on entry 31 (Smolin's 2.5 M☉ neutron-star bar)

**Ordered by Duho (relay via Blanc 2026-09-02 17:23 KST, "a → b → c", STEP 2): "a weekly check for new
neutron-star mass measurements (pulsars, mergers) against the 2.5 M☉ bar, modelled on the DESI curvature
watch; fire/clear criteria written down first; cheap to run."** Criteria below are written BEFORE the
watch code. The watch never interprets; every hit is read by a human; any FIRED/LIVE change is Duho's.

## 1. What is watched, exactly (from the record, bibliography entry 31 and §0 standing table)
- **The bar:** Smolin 2004, §4 — a neutron star above **2.5 M☉** is "certain refutation" of cosmological
  natural selection as he states it (1.5 M☉ only if one trusts Bethe–Brown). The bar is the author's.
- **Standing today:** LIVE. Best measurement PSR J0952−0607, **2.35 ± 0.11 M☉** (Romani et al. 2025,
  arXiv:2512.05099), 1.36σ below the bar, posterior above the bar 8.6%. PSR J0740+6620 2.08 ± 0.07
  (Fonseca 2021), 6.00σ below. GW190814's secondary 2.50–2.67 M☉ (90%) is **conditional**: its identity
  (neutron star or black hole) is unresolved, so it does not test the bar as stated.
- **Trend stamped in the record:** drifting AWAY from firing as errors tighten (the J0952 error fell from
  ±0.17 to ±0.11 while the central value held).

## 2. Fire / re-gate / clear criteria — declared now
Let a candidate measurement have mass M ± σ (1σ, symmetric approximation; asymmetric errors use the
lower error), from a source with a **resolved neutron-star identity** (radio/optical pulsar timing or
light-curve mass; NOT a gravitational-wave secondary of unresolved nature).
- **FIRE_CANDIDATE:** (M − 2.5)/σ ≥ 3, in a **peer-reviewed** publication (preprints raise a
  RE_GATE, never a FIRE_CANDIDATE — the lane's published-papers-only rule). A FIRE_CANDIDATE is a
  two-seat gate + packet to Duho; the standing changes only on his stamp.
- **RE_GATE:** (M − 2.5)/σ ≥ 2 in any source, OR any peer-reviewed M > 2.5 central value at ≥ 1σ, OR a
  GW secondary with a resolved NS identity at M > 2.5 — a human reads and a two-seat gate decides
  whether the ledger changes.
- **HINT (log only):** a new measurement with posterior P(M > 2.5) ≥ 5% that does not meet RE_GATE.
- **CLEAR (no action, logged):** anything else, including tighter errors on known stars below the bar.
- **Battery rule (existing, §4): a secure central mass ≥ 2.5 M☉ added to the ledger FAILS the
  battery.** The bands above are for reading hits; the ledger is edited only after a two-seat gate.

## 3. The weekly watch (human-facing twin, modelled on `nm_desi_curvature_watch.py`)
- arXiv API query (title/abstract): neutron star AND (mass measurement OR Shapiro delay OR "most massive"
  OR "maximum mass" OR "black widow" OR "redback" OR "mass gap") — pulsars and mergers both surface;
  max 25 per run, sorted by submission date; seen-ids in `ns_mass_watch_state.json`; hits appended to
  `NS_MASS_WATCH_HITS.md`; one event per run with news to the autopilot feed; **silent when nothing is
  new; always stamps last_run** so a dead watch is detectable.
- Schedule: **Tuesdays 10:00 KST** (the curvature watch holds Mondays), hermes cron `--no-agent --script`,
  named "BHU neutron-star mass watch". Absolute lane paths (register §1av).
- The watch text states the criteria of §2 verbatim so the human reader tests the right thing.

## 4. The standing tripwire — ALREADY EXISTS; not duplicated
Found while building this: `b68_entry31_massbar_tripwire.py` + `entry31_massbar_ledger.json` (RQ-E,
BHU Lane 2) already recompute entry 31's standing on every battery run (`check.py` runs every
`[ab]N*.py`). Its rule is the record's: **FAIL the moment a SECURE (resolved-identity) central mass
reaches 2.5 M☉**; GW190814's secondary is tracked `secure=false` and never counted; a binding check
asserts the computed gap equals the record's 1.36σ. Run today: 3/3 PASS. **That rule governs the
battery.** The RE_GATE / HINT bands in §2 are reading criteria for the human who opens a watch hit —
they decide whether a two-seat gate is convened to change the ledger; they do not add a second trip
rule. No `b64` is created.

## 5. What would make this watch wrong, stated in advance
- A measurement with asymmetric or non-Gaussian posteriors: the ledger records the published lower
  bound and the human reader uses the paper's own P(M > 2.5) where given.
- Systematics (inclination, light-curve modelling) are the paper's to state; the watch does not re-derive.
- The bar itself is Smolin's; if a future ruling moves the operative bar (e.g. to the 1.5 M☉ conditional
  limb), the ledger's `bar` field changes under that ruling, not silently.
