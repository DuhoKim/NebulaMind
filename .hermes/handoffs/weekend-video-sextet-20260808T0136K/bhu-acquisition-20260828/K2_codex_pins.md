# K2 codex pin sheet

Conventions: signature `(-,+,+,+)`, outward normal from FRW (`-`) to Kottler (`+`), `[Q]=Q_+-Q_-`, and geometrized units except where `G` is displayed. The source paths below are frozen local text receipts.

## Geometry and junction inputs

- FRW: `ds_-^2=-dτ^2+a(τ)^2[dχ^2/(1-kχ^2)+χ^2dΩ^2]`, `k=0,±1`: entry 22, `../bhu-reading-20260823/sources/2606.25023_clean.txt` L316–320. Equivalently for the closed chart, `χ=sin ψ` gives `ds^2=-c^2dt^2+a^2dψ^2+a^2sin^2ψ dΩ^2`: entry 4, `knutsen_2009_gravcosmol15_273_clean.txt` L1093–1103. The original FRW curvature-coordinate form and the meanings of `k` are also printed at entry 4 L43–66.
- Schwarzschild–de Sitter/Kottler: `ds_+^2=-F(R)dT^2+F(R)^(-1)dR^2+R^2dΩ^2`, `F=1-2GM/R-ΛR^2/3`. Entry 4 prints this form at L238–279 (its `m=GM/c^2` convention is stated at L280–283); entry 5 prints the regular retarded-coordinate form and `f=1-2M/r-Λr^2/3` at L83–92. Entry 22 independently prints the one-function curvature-coordinate metric at L310–320.
- Timelike Darmois/Israel input: continuity of the first fundamental form is stated and evaluated at entry 4 L603–642; equality of second fundamental forms is the smooth condition at L695–700. Entry 22 calls these the Darmois–Israel no-shell conditions at L289–297 and prints the induced-metric and angular-extrinsic-curvature equations at L335–368. With the convention above, the shell formula used here is the standard Israel relation `S_ab=-(8πG)^(-1)([K_ab]-h_ab[K])`; the pinned papers supply its no-shell specialization, while entry 5 explicitly defines jumps at L56–60.
- Null Barrabès–Israel input: entry 5 says it uses that formalism at L49–55, defines the transverse curvature `K_ab=e_a^μe_b^ν∇_μN_ν` at L137–140, gives its two sides at L141–168, and gives `p=-(8π)^(-1)[K_uu]` at L169–179. Its induced degenerate metric and pseudo-inverse are at L132–136.

## Boundary and mass inputs

- Pathria's closed model selects positive curvature: entry 1, `pathria_1972_universe_black_hole_nature240_298_clean.txt` L67–71 and L394–409. Its largest sphere has area approaching `4πR_max^2`: L419–424. In the curvature coordinate this equator is `r_b=1`: entry 4 explicitly attributes that choice to Pathria at L1063–1072 and relates it to `r=sin ψ`, `ψ=π/2` at L1093–1119. (The entry-1 OCR drops the displayed radial factor in its metric, so the explicit coordinate value is receipted through entry 4's direct audit of Pathria.)
- Pathria's exterior mass is the interior dust integral: entry 1 L308–329 gives `μ=(4πG/3c^2)ρR^3`; entry 5 gives `M=∫_0^r4πρr^2dr=(4π/3)ρr^3|_Σ` at L88–92. Pathria identifies the horizon radius with maximum expansion at entry 1 L394–406.
- Entry 56: `M=(4/3)πχ^3ρ_0` is printed in `gaztanaga_mass_mnras_clean.txt` L141–144; the same source prints uniform-density `M=(4/3)πr^3ρ`, `r=aχ`, and the flat FRW metric at L130–136. Its finite top-hat and empty exterior are L147–160.
- The allowed Pathria range `0≤Λ≤Λ_c` and the horizon/maximum-expansion identification are printed at entry 5 L29–41.

