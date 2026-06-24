# Page-58 Paper-Driven Vote Accumulation Dry Run

Slice 1 only. No Alembic migration was applied and no production DB/page data was written.

## Headline Ratios

- Intros that staked: 47/168 (28.0%); no-op intros: 121/168 (72.0%).
- No-match intros routed to emergent pool: 113/168 (67.3%).
- Finding-class sentences kept: 3553/11120 (32.0%); filtered: 7567/11120 (68.0%).
- Provenance coverage after new stakes: 10/10 (100.0%).
- Settled share after rollup: 240/272 (88.2%).

## Calibration Warning

The pro/con sign is UNCALIBRATED. This run uses placeholder tau_rel=0.55 and tau_vote=0.70, plus the existing tone gate as a proxy. Pairwise stance gold is required before any write path.

## Sensitivity

- Trust tier changes if con-votes are dropped: 0/10.
- Trust tier changes if tau_vote shifts -0.10: 0/10.
- Trust tier changes if tau_vote shifts +0.10: 0/10.

## Per-Base-Sentence Rollup

### Sentence 0

Internal AGN feedback processes drive powerful outflows that eject gas or heat circumgalactic gas, quenching star formation via starvation.

- New votes: +27 / -0; refine tally 4; no-op tally 0.
- Would-be trust: consensus (baseline consensus); settled share 1.000.

### Sentence 1

Gas removal and depletion, including disrupted accretion and stripping of circumgalactic reservoirs, suppress star formation by reducing cold gas supply.

- New votes: +15 / -0; refine tally 0; no-op tally 0.
- Would-be trust: consensus (baseline consensus); settled share 1.000.

### Sentence 2

Satellite galaxies experience environmental quenching after infall into groups or clusters, distinct from mass-driven quenching in centrals.

- New votes: +7 / -0; refine tally 0; no-op tally 0.
- Would-be trust: consensus (baseline consensus); settled share 1.000.

### Sentence 3

Dense cluster and group environments accelerate galaxy transformation through hydrodynamical interactions with the intracluster medium and gravitational effects.

- New votes: +4 / -0; refine tally 0; no-op tally 0.
- Would-be trust: accepted (baseline debated); settled share 0.913.

### Sentence 4

Key questions remain unresolved regarding the mechanisms driving environmental quenching, including the role of AGN feedback and observational biases.

- New votes: +2 / -0; refine tally 1; no-op tally 0.
- Would-be trust: challenged (baseline debated); settled share 0.286.

### Sentence 5

Environmental quenching signatures, including ram-pressure stripping, are observed at high redshift, linking environment to rapid quenching in the early Universe.

- New votes: +9 / -1; refine tally 1; no-op tally 0.
- Would-be trust: debated (baseline debated); settled share 0.821.

### Sentence 6

Ram-pressure stripping removes gas from galaxies via hydrodynamical interactions with the intracluster medium in dense environments.

- New votes: +5 / -0; refine tally 0; no-op tally 0.
- Would-be trust: accepted (baseline consensus); settled share 0.957.

### Sentence 7

Cosmic-web environments like filaments and sheets shape galaxy evolution through tidal fields that influence gas accretion and stripping.

- New votes: +2 / -0; refine tally 0; no-op tally 0.
- Would-be trust: debated (baseline debated); settled share 0.889.

### Sentence 8

Galaxy quenching is jointly regulated by stellar mass as the primary driver and environment as a secondary modulator, with separable effects.

- New votes: +15 / -0; refine tally 2; no-op tally 0.
- Would-be trust: debated (baseline debated); settled share 0.871.

### Sentence 9

Galaxy environment correlates with morphological transformation and color evolution, with dense regions hosting predominantly quenched early-type systems.

- New votes: +17 / -1; refine tally 2; no-op tally 0.
- Would-be trust: accepted (baseline consensus); settled share 0.912.

## Timing

- base_embedding_seconds: 0.483s
- claim_filter_seconds: 4317.876s
- embedding_match_seconds: 181.944s
- load_seconds: 0.085s
- tone_gate_seconds: 244.417s
- total_seconds: 4744.844s

## Containment

- db_write_count=0
- no_apply=True
- local_only=True
- paid_lane_touched=False
- claude_p_used=False
