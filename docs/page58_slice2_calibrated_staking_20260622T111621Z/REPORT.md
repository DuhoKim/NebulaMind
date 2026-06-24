# Page-58 Slice-2 Calibrated Vote Dry Run

Status: DRY-RUN ONLY. Stance gold is a draft for Papa spot-check; stance classifier is PROVISIONAL / NOT LOCKED.

## Headline Ratios
- Intros staked: 31/168 (18.5%).
- Base sentence coverage: 9/10 (90.0%).
- Settled share: 192/227 (84.6%).

## Golds
- Stance draft rows: 90 (Papa spot-check required before lock).
- Relevance gold rows: 120; tau_rel=0.53 validate_F1=0.8182.
- Tone transfer gate rows: 60; provisional macro-F1 qwen=0.6117, gpt=0.6127, gate_passed=False (gate-only; not tuned).

## Sensitivity
- Drop con votes: 2/10.
- tau_vote -0.10: 0/10.
- tau_vote +0.10: 0/10.

## Per-Sentence Projection
### Sentence 0
Internal AGN feedback processes drive powerful outflows that eject gas or heat circumgalactic gas, quenching star formation via starvation.
- New votes: +21 / -2; seed duplicate stakes skipped 2.
- Would-be trust: debated (settled share 0.953488).

### Sentence 1
Gas removal and depletion, including disrupted accretion and stripping of circumgalactic reservoirs, suppress star formation by reducing cold gas supply.
- New votes: +10 / -1; seed duplicate stakes skipped 2.
- Would-be trust: consensus (settled share 0.962963).

### Sentence 2
Satellite galaxies experience environmental quenching after infall into groups or clusters, distinct from mass-driven quenching in centrals.
- New votes: +3 / -0; seed duplicate stakes skipped 1.
- Would-be trust: consensus (settled share 1.0).

### Sentence 3
Dense cluster and group environments accelerate galaxy transformation through hydrodynamical interactions with the intracluster medium and gravitational effects.
- New votes: +2 / -0; seed duplicate stakes skipped 0.
- Would-be trust: consensus (settled share 0.904762).

### Sentence 4
Key questions remain unresolved regarding the mechanisms driving environmental quenching, including the role of AGN feedback and observational biases.
- New votes: +2 / -0; seed duplicate stakes skipped 0.
- Would-be trust: challenged (settled share 0.285714).

### Sentence 5
Environmental quenching signatures, including ram-pressure stripping, are observed at high redshift, linking environment to rapid quenching in the early Universe.
- New votes: +5 / -0; seed duplicate stakes skipped 0.
- Would-be trust: debated (settled share 0.826087).

### Sentence 6
Ram-pressure stripping removes gas from galaxies via hydrodynamical interactions with the intracluster medium in dense environments.
- New votes: +2 / -0; seed duplicate stakes skipped 0.
- Would-be trust: consensus (settled share 0.95).

### Sentence 7
Cosmic-web environments like filaments and sheets shape galaxy evolution through tidal fields that influence gas accretion and stripping.
- New votes: +0 / -0; seed duplicate stakes skipped 1.
- Would-be trust: consensus (settled share 0.875).

### Sentence 8
Galaxy quenching is jointly regulated by stellar mass as the primary driver and environment as a secondary modulator, with separable effects.
- New votes: +7 / -1; seed duplicate stakes skipped 0.
- Would-be trust: debated (settled share 0.791667).

### Sentence 9
Galaxy environment correlates with morphological transformation and color evolution, with dense regions hosting predominantly quenched early-type systems.
- New votes: +3 / -1; seed duplicate stakes skipped 1.
- Would-be trust: debated (settled share 0.85).

## Containment
- db_write_count=0
- paid_lane_touched=False
- local_only=True
- claude_p_invocations=15
