# K3 step 2 — one-page check sheet

**Tori, 2026-09-04 10:25 KST.** For a human who wants to check this without re-deriving it. Every line carries either a
source line or an executed-output line. Run any script below with `python3` from this directory.

## The question
K3 step 1 found the unpolarized spin-density square linear in `n`, so neither printed closure followed. The one route by
which a real `n²` could return was a Fermi-statistics exchange term. **Does it return?**

## The answer in one line
**Yes — and it comes out negative**, with a coefficient that is not a single number.

## The five numbers

| what | value | where to see it |
|---|---|---|
| direct (Hartree) term, unpolarized | `0` | `K3S2_claude_exchange.out` L47; `_tmp_k3s2_codex_rerun.out` "HARTREE_DIRECT= 0" |
| exchange (Fock) term | `−3(A² + B²)` | `K3S2_claude_exchange.out` L48 |
| `A`, fixed by `Tr ρ_med = n` | `n/(4N_f)` | `K3S2_claude_exchange.out` L44; `K3S2_route2_agy.py` run output |
| exchange, non-relativistic | `−(3/8) n²/N_f` | `K3S2_tori_verify.out` "NR ... : -3*n**2/(8*N_f)" |
| exchange, ultrarelativistic | `−(3/16) n²/N_f` | `K3S2_tori_verify.out` "UR ... : -3*n**2/(16*N_f)" |

## The two printed relations it is tested against

| printed | source line | verdict |
|---|---|---|
| `s² = ½ s_ik s^ik = ⅛ n²` | entry 10 **L121** (`1111.4595v2_poplawski_prd85_clean.txt`) | contradicted: opposite sign, magnitude 3/16 ≠ 1/8 |
| `⟨s²⟩ = ¾ n²` | entry 10 **L113** | contradicted: opposite sign, magnitude 3/8 ≠ 3/4 |

Both are the same quantity: `½ s_ij s^ij = |s⃗|²` exactly, re-derived in three independent scripts and unchanged under
the opposite Levi-Civita sign convention (`K3S2_claude_exchange.out`, C6 section).

## The one thing that could change the answer
There are **two objects** both called `⟨s²⟩`, and they give different answers:

| object | what it is | result |
|---|---|---|
| **L** — square, then coarse-grain | `⟨Σ_a s_a(x)s_a(x)⟩` at coincident `x` | `n²`, negative, regime-dependent |
| **C** — coarse-grain, then square | `⟨S_aS_a⟩/V²`, `S_a = ∫_V s_a` | everything `∝ n/V`, vanishes as `V → ∞` |

**Object L is the one the field equations need**, because `U^ik` (entry 10 Eq. (6), **L84–86**) is a local algebraic
function of the spin tensor and Einstein–Cartan is a local theory. Also, on Object C the unpolarized mean spin is zero,
so the term would vanish outright — which the paper plainly does not intend, since it asserts a nonzero `⟨s²⟩`.
**The paper never says which.** L108–110 says only "can be macroscopically averaged at cosmological scales as a perfect
fluid"; L113 then states the number. The physics fixes it; the text does not.

Either way the printed closures fail — on Object L by sign and magnitude, on Object C because no `n²` survives at all.

## Who computed what, and the split

| seat | blind? | method | class |
|---|---|---|---|
| claude | yes | momentum-space Wick | `EXCHANGE_N2_RESTORED` |
| codex | yes | equal-momentum projection (Object C) | `EXCHANGE_NEGLIGIBLE` |
| agy route 2 | yes | position-space Slater determinant, **both objects** | `EXCHANGE_N2_RESTORED` |
| agy third seat | no (full sight) | re-ran both scripts | `EXCHANGE_N2_RESTORED` |

**The split was about which object, not about the algebra.** codex additionally made an arithmetic error: it treated
the per-momentum spinor trace as a constant. It is not — Tori verified independently:
`Σ_a Tr(Σ_a P₊ Σ_a P₊) = 2 + 4m²/E²`, equal to **6** at `p = 0` and **2** at `m = 0`
(`K3S2_tori_verify.out`, `CLAIM_A_VERIFIED = True`). So codex's Object-C coefficient is wrong; its `1/V` scaling is
right and route 2 reproduces it.

## Controls (all eight, by name, in every seat that ran a script)
`C1_DIRECT_ZERO` · `C2_POLARIZED_N2_QUARTER` · `C3_CLASSICAL_LINEAR_IN_N` · `C4_EXCHANGE_DELETED` ·
`C5_UNITS_RESTORED` · `C6_MAP_DERIVED` · `C7_ANTIPARTICLE_SECTOR_LIVE` · `C8_NO_PRINTED_COEFF_INPUT`
— all `PASS`, `MISSING_CODES=none`. `C4`'s prediction (deleting antisymmetrisation must delete the exchange term
identically) was written into each script header **before** running. `C3` recovers K3 step 1's `(3/4) n/V` contact term,
so this step contains step 1 rather than replacing it.

## One correction Tori's own seat needed
Route 2 carried `N_f` where Tori's seat set it to 1. Route 2 is right; the reconciled numbers above carry `1/N_f` and
Tori's figures are the `N_f = 1` case (`K3S2_tori_verify.out`, last block).

## Receipts (sha256)
```
K3S2_EXCHANGE_PREREG_20260904.md  ca2344a04938f2351ff3b8a13c0549cdcc58382f8f0bef9fe09793c9bfe6e76d
K3S2_claude_exchange.py           9c9592cec6dbb7ea6a5faec96e52d9a28683b6bbbc1f23fb93abaef1afd5f18e
K3S2_claude_exchange.out          a3e614973336e6a0745316d5f915cb77322c8a0f796c03cd7527df92e78ebb1a
K3S2_codex_exchange.py            c411414f9f411f2e52fb5f64c2070a2c10a0822e7f6391e662893f0f5d62aacf
K3S2_route2_agy.py                10e41d2a07770db5b1bb4e4a784f73a96412085c3dc449b10988d46cd44c7938
K3S2_tori_verify.py               fdde76412a5dc52174f4f61f6f785b3e50b5eb9048c34c31cc5d6f3a9ea0a98b
K3S2_tori_verify.out              79c86a08ca369e2aeef412289191d1a2b11bae1e6564fefa8205e5d5f19bbbee
```
Gate: `K3S2_PREREG_GATE_20260904_agy.md` (ACCESS PROVEN, 3 repairs applied, 1 declined);
adjudication of the declined repair: `K3S2_PREREG_GATE_ADJUDICATION_20260904_agy.md`, `ADJUDICATION=LANE_RIGHT`.

K3S2_CHECK_SHEET_COMPLETE
