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
is not committed here. This paragraph said "Δγ stands whatever the ratified endpoints are" —
**false** (GPT56-V89 F5: a fixed spacing cannot produce an exact endpoint-inclusive uniform grid
for arbitrary endpoints), repaired by AMENDMENT 2 below, which re-expresses the commitment as a
step count.

**Every value above is now frozen by commitment: a later change is a post-hoc edit and says so.**

---

**AMENDMENT — 2026-08-30 11:2x KST, logged per this file's own rule ("a later change is a post-hoc
edit and says so").** CODEX-V86 F10: the addressing rule as first committed read one-based —
`spawn(n_draws)[i]` for draw `i ∈ [1, n_draws]` — which addresses `spawn(99)[99]`, out of range,
and leaves child 0 unused. **The rule is corrected to ZERO-BASED: draw `i ∈ [0, n_draws−1]` uses
`SeedSequence(master_seed).spawn(n_draws)[i]`.** The amendment touches the ADDRESSING RULE only;
`master_seed`, the generator, `Δγ` and `n_draws` stand exactly as first committed, and this
amendment is itself part of the committed record.


---

## AMENDMENT 2 — the spacing commitment RE-EXPRESSED as a step count (2026-08-30, logged under this file's own amendment rule)

**Why (GPT56-V89 F3 + F5, relayed by the principal's coordinator):** `delta_gamma_max = 0.01` was
committed as a SPACING and claimed to stand for any ratified endpoints. That claim is false — for
endpoints such as ±0.253 no integer number of 0.01 steps reaches the far endpoint, so "exactly the
uniform grid" and "contains both endpoints" cannot both hold. And the matrix rule compared every
cell `(i, j)` to `(i, 0)`, an address outside its own declared `j ∈ [1, n_perturbations]` domain,
while γ=0 is an interior manifest entry.

**The commitment, re-expressed — values unchanged at the proposed endpoints:**

| quantity | committed value | status |
|---|---|---|
| `n_steps` | **50** (EVEN) | COMMITTED here, replacing the spacing as the frozen quantity |
| ratified endpoints | **symmetric ±Γ** | the ratification is CONSTRAINED to the symmetric form; asymmetric endpoints would need a new commitment |
| `delta_gamma` (Δγ) | **DERIVED: 2Γ / n_steps** | no longer independently committed — at the proposed Γ = 0.25 it derives to **0.01, the previously committed value unchanged** |
| grid | **γ_j = −Γ + j·Δγ, j ∈ [0, n_steps]**, zero-based | endpoint-inclusive BY CONSTRUCTION for every symmetric ratification |
| `n_perturbations` | **n_steps + 1 = 51** | the baseline is IN the matrix |
| baseline index | **j₀ = n_steps/2 = 25**, with **γ_{j₀} = 0 exactly** | derived, and the receipt verifier VERIFIES γ_{j₀} = 0 |
| `HELD` | every cell `(i, j)` equals its own draw's `(i, j₀)` cell | the `(i, 0)` comparisons die with the one-based addressing |

**What is untouched:** `n_draws = 99`, `draw_master_seed = 20260830`, the committed generator, the
zero-based draw indexing of Amendment 1, and COMMON RANDOM variates. **What died:** the independent
Δγ commitment, the one-based `j` domain, and the out-of-domain `(i, 0)` baseline address.
