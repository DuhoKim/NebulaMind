J_SMOOTH_EXPANDING — entry 56 cell (B1, k=0, Λ=0): the comoving dust top-hat has the standard Oppenheimer–Snyder/Darmois match.
J_SHELL_UNPHYSICAL — Pathria cell (B2, k=+1, 0≤Λ≤Λ_c): pressure-only null shell; WEC passes but DEC fails (the endpoint itself has ȧ=0, so “expanding” means the expanding branch reaching it).

| placement | k | Λ=0 | 0<Λ≤Λ_c |
|---|---:|---|---|
| B1 comoving timelike | +1 | J_SMOOTH_EXPANDING | J_SMOOTH_EXPANDING |
| B1 comoving timelike | 0 | J_SMOOTH_EXPANDING | J_SMOOTH_EXPANDING |
| B2 maximum/equator horizon | +1 | J_SHELL_UNPHYSICAL | J_SHELL_UNPHYSICAL |
| B2 maximum/equator horizon | 0 | J_NONE | J_NONE |
| B3 general noncomoving timelike | +1 | J_UNDETERMINED | J_UNDETERMINED |
| B3 general noncomoving timelike | 0 | J_UNDETERMINED | J_UNDETERMINED |

Controls (printed before the table by `K2_codex_junction.py`): C1 PASS, `M=4πρR³/3`, all jumps zero and `β_+²=1-S²`; C2 PASS, `[K_uu]=-2πρa`, angular jumps zero, `μ=0`, `p=ρa/4`; C3 PASS, `r_b=1`, `F=0`, smooth angular matching gives `Ṙ²=0`; C4 PASS, deleting the energy-condition test changes closed B2 from `J_SHELL_UNPHYSICAL` to `J_SHELL_EXPANDING`.

Key expressions (outward normal, `[K]=K_+-K_-`): for B1, `K^-_{ss}=K^+_{ss}=0`, `K^-_{θθ}=R C_k`, `K^+_{θθ}=R√(Ṙ²+F)=R C_k`, hence `S_ab=0`. For B3, write `v=dτ/ds`, `q=dχ/ds`, `v²-a²q²=1`, `R=aS_k(χ)`, `β_-=vC_k+a q ȧS_k`, `β_+=√(Ṙ²+F)`. Then `[K_{θθ}]=R(β_+-β_-)`, `[K_{φφ}]=sin²θ[K_{θθ}]`, `K^+_{ss}=-(R̈+F'/2)/β_+`, `K^-_{ss}=a q(ṽ+aȧq²)-av(q̇+2(ȧ/a)vq)`, `σ=-(β_+-β_-)/(4πGR)`, and `p=([K_{ss}]+(β_+-β_-)/R)/(8πG)`. WEC is `σ≥0, σ+p≥0`; DEC is `σ≥|p|`.

Derivation summary (154 words): The induced radius fixes `R=aS_k`. For a comoving dust edge, the Friedmann equation and `M=4πρR³/3` turn the exterior angular condition into `Ṙ²+F=C_k²`; both angular curvatures agree, and the boundary is geodesic on both sides, so the temporal curvatures also agree. Thus every B1 cell admits an expanding smooth branch. The closed `Λ=0` case is the standard OS matching and lies within entry 22 Proposition 2's asymptotically-flat, finite-mass domain, so it later turns around; this does not negate its expanding branch. At Pathria's equatorial horizon, Barrabès–Israel gives only `[K_uu]=-2πρa`, hence `μ=0`, `p=ρa/4`: WEC holds and DEC fails. Flat dust with nonnegative Λ has strictly positive `H²`, so the defining maximum-expansion B2 does not exist. A genuinely noncomoving B3 layer has two free trajectory derivatives in `σ,p`; the junction identities alone neither impose an equation of state nor fix WEC/DEC. Those cells are therefore `J_UNDETERMINED`, with the residual freedom displayed above.
