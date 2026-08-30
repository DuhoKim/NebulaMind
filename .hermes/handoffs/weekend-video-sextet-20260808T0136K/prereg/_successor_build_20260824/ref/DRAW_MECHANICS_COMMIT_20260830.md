**STATUS: COMMITTED — the delegated BS-3g mechanics, fixed in this artifact BEFORE any verdict is
seen (principal's delegation, 2026-08-30 10:46, relayed by Blanc; the pre-commitment requirement is
CODEX's replay finding — a receipt cannot prove its own values were chosen blind, so the values are
chosen HERE, in a committed file, with their rationales, and reported).**

# The delegated draw mechanics — chosen by rule, not by search

| parameter | value | rationale — why this value could not have been shopped |
|---|---|---|
| `n_draws` | **99** | RULED by the principal (the 99th-percentile worst case, the proposal he ratified) |
| `draw_master_seed` | **20260830** | the calendar date of this commitment — one value, derived from the clock, no search space |
| `draw_generator_id` | **`numpy-1.26.4-PCG64-default_rng`** | the frozen environment's own generator, version-pinned by `require_environment`; per-draw seed = `SeedSequence(master_seed).spawn(n_draws)[i]` |
| `delta_gamma_max` (Δγ) | **0.01** | 51 grid points across the proposed ±0.25 range; fine enough that a flip confined to one cell spans < 4 % of the swept range |
| draw variates | **COMMON RANDOM** | RULED: one uniform stream per draw across every γ — a flip is the gradient's doing |

**The γ range itself (±0.25) is a PROPOSAL awaiting ratification** (`PROPOSAL_GAMMA_RANGE.md`) and
is not committed here; Δγ stands whatever the ratified endpoints are, as the maximum adjacent
spacing.

**Every value above is now frozen by commitment: a later change is a post-hoc edit and says so.**
