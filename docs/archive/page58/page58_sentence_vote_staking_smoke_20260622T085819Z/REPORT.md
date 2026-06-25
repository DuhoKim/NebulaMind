# Page-58 Paper-Driven Vote Accumulation Dry Run

Slice 1 only. No Alembic migration was applied and no production DB/page data was written.

## Headline Ratios

- Intros that staked: 1/5 (20.0%); no-op intros: 4/5 (80.0%).
- Finding-class sentences kept: 58/293 (19.8%); filtered: 235/293 (80.2%).
- Provenance coverage after new stakes: 1/10 (10.0%).
- Settled share after rollup: 138/168 (82.1%).

## Calibration Warning

The pro/con sign is UNCALIBRATED. This run uses placeholder tau_rel=0.55 and tau_vote=0.70, plus the existing tone gate as a proxy. Pairwise stance gold is required before any write path.

## Sensitivity

- Trust tier changes if con-votes are dropped: 0/10.
- Trust tier changes if tau_vote shifts -0.10: 0/10.
- Trust tier changes if tau_vote shifts +0.10: 0/10.

## Per-Base-Sentence Rollup

### Sentence 0

Internal AGN feedback processes drive powerful outflows that eject gas or heat circumgalactic gas, quenching star formation via starvation.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: consensus (baseline consensus); settled share 1.000.

### Sentence 1

Gas removal and depletion, including disrupted accretion and stripping of circumgalactic reservoirs, suppress star formation by reducing cold gas supply.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: consensus (baseline consensus); settled share 1.000.

### Sentence 2

Satellite galaxies experience environmental quenching after infall into groups or clusters, distinct from mass-driven quenching in centrals.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: consensus (baseline consensus); settled share 1.000.

### Sentence 3

Dense cluster and group environments accelerate galaxy transformation through hydrodynamical interactions with the intracluster medium and gravitational effects.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: debated (baseline debated); settled share 0.895.

### Sentence 4

Key questions remain unresolved regarding the mechanisms driving environmental quenching, including the role of AGN feedback and observational biases.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: challenged (baseline debated); settled share 0.211.

### Sentence 5

Environmental quenching signatures, including ram-pressure stripping, are observed at high redshift, linking environment to rapid quenching in the early Universe.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: debated (baseline debated); settled share 0.778.

### Sentence 6

Ram-pressure stripping removes gas from galaxies via hydrodynamical interactions with the intracluster medium in dense environments.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: accepted (baseline consensus); settled share 0.944.

### Sentence 7

Cosmic-web environments like filaments and sheets shape galaxy evolution through tidal fields that influence gas accretion and stripping.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: debated (baseline debated); settled share 0.875.

### Sentence 8

Galaxy quenching is jointly regulated by stellar mass as the primary driver and environment as a secondary modulator, with separable effects.

- New votes: +1 / -0; refine tally 0; no-op tally 0.
- Would-be trust: debated (baseline debated); settled share 0.765.

### Sentence 9

Galaxy environment correlates with morphological transformation and color evolution, with dense regions hosting predominantly quenched early-type systems.

- New votes: +0 / -0; refine tally 0; no-op tally 0.
- Would-be trust: debated (baseline consensus); settled share 0.875.

## Timing

- load_seconds: 0.063s
- base_embedding_seconds: 0.487s
- claim_filter_seconds: 110.252s
- embedding_match_seconds: 4.166s
- tone_gate_seconds: 1.741s
- total_seconds: 116.748s

## Containment

- db_write_count=0
- no_apply=True
- local_only=True
- paid_lane_touched=False
- claude_p_used=False
