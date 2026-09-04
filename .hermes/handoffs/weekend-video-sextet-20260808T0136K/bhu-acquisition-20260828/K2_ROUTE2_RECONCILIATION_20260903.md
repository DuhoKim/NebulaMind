# K2 — second route vs first route (Tori, 2026-09-03 17:32 KST; Duho's order "both", 17:22 KST)

**Route 1:** extrinsic-curvature jumps (Israel; Barrabès–Israel for the null case) in comoving FRW coordinates — codex and the
Claude seat blind, third seat agy on two placement splits (`K2_RESULT_20260903.md`).
**Route 2:** a fresh agy seat via `nm_referee_dispatch.sh` (ACCESS PROVEN), blind to every route-1 file, gave a manual Darmois/
Misner–Sharp derivation in LTB/Painlevé–Gullstrand-type slicing with areal radius R(τ) (`K2_ROUTE2_agy.md`). A 2026-09-04 support
audit found that its named companion `K2_route2_agy.py` is a preserved six-line no-output stub, not an executable receipt. Tori
therefore added `K2_route2_tori_repair.py`, `K2_route2_tori_repair.out`, and `test_K2_route2_agy.py`; the test passed and the output
independently prints the mass-continuity identity, the nondegenerate and equator B3 derivatives, and controls C1–C4.

| question | route 1 | route 2 | agreement |
|---|---|---|---|
| entry 56's cell (B1, k=0, Λ=0) | J_SMOOTH_EXPANDING | J_SMOOTH_EXPANDING | yes |
| Pathria's cell (B2, k=+1, 0≤Λ≤Λ_c) | J_SHELL_UNPHYSICAL (μ=0, p=ρa/4, DEC fails) | J_SHELL_UNPHYSICAL (σ=0, p=ρa/4, DEC fails) | yes |
| must a no-shell B3 boundary be comoving? | yes (Birkhoff constancy of M) | yes: M_T = M₀ S_k(r*)³ constant ⇒ r*(τ) comoving | yes |
| controls C1–C4 | pass | pass (C1: M_T = M₀ sin³χ*, expanding into the F<0 region; C3: F(R_b) = −ȧ² ⇒ ȧ = 0 under F>0; C4 flips B2 to J_SHELL_EXPANDING) | yes |

**Point of divergence:** none in any class or control. Route 2 states the B3 result more directly: Misner–Sharp continuity gives
`dM/dτ = 3M₀ sin²χ cosχ χ̇`; away from the equator fixed exterior M forces χ̇=0, while at χ=π/2 the first nondegenerate condition is
`d²M/dτ² = −3M₀χ̇²`, again forcing χ̇=0 (`K2_route2_tori_repair.out` L4–5). Route 2's C1 phrase "expanding into the F(R)<0 exterior
region" is the same white-hole region route 1's extra row records. The theorem has two distinct derivations; only the repaired Tori
companion, not the original agy stub, is an executable route-2 receipt.
