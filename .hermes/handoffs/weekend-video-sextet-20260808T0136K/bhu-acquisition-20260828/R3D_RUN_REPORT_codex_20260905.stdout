ACCESS_SHA=a99aad15f168290fa5afaaf957d478cedd4cf57cb967e97dd3ea8d6b2a25840b
R3D_CLASS=R3D_NO_CLASS
C0_REACHABILITY=PASS
C1_SOURCE_IDENTITY=PASS
C2_COMPLETION_LEDGER=PASS
C3_DELETION_PROBE=NOT_RUN
C4_GR_BENCHMARK=PASS
C5_HARNESS_PINNED=PASS
C5B_PATH_LIST=FAIL
C6_BREAKER_TEST=NOT_RUN

LIMB REACHED: A and B

## Execution result

The frozen scientific partition, before the persistent C5b control failure is applied, selects class 4: `DYM_NO_POSITIVE_FLOOR`. Under §4 class 6, however, a scientific class may be filed only from a control-clean report. C5b failed on its first complete path table and on the required second attempt because two inspection utilities were outside the §9 allowlist. No source evidence was unread or unresolved, so §4 routes the terminal filing to `R3D_NO_CLASS`, not `DYM_SOURCE_BLOCKED`.

## Limb-A result and supporting census rows

Limb A reproduced a size–mass relation and a mass-bounding relation, so its exit was not taken.

- C2 L07; `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt`, L00149-L00154: “Ra(r)=r a 1 - e x p ... (12)” / “and” / “r ,3 =   ro2ra.                     (13)” / “This is the exact spherically symmetric solution of the Einstein equations which for r >> r, practically coincides with the Schwarzschild solution and for r << r, behaves like the de Sitter solution.” With C2 L01, `r_g=2GM/c²`, this gives the printed relation `r_*³=r₀²r_g=2GMr₀²/c²`.
- C2 L10; `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt`, L00280-L00283: “Within the range of masses M ≥ Mcrit , where Mcrit corresponds to the double horizon, the de Sitter–Schwarzschild geometry (2) describes a regular black hole with the de Sitter interior [14,24], called a Λ black hole (ΛBH) in [26]. For M > Mcrit spacetime has two horizons, an event horizon r = r+ and an internal Cauchy horizon r = r− .”

## Limb-B readings and partition

The finite admissible reading set contains only the completion-free reading. All four completion kinds are BOUND: Euclidean volume by C2 L04; the interior profile by L06; operative coefficients by L01 and L03-L08; and the GR exterior by L01, L02, and L15.

| reading | completion | allowed mass set | P/Z/I | floor/family |
|---|---|---|---|---|
| R0 | none | `⋃_{r₀>0}[0.878794537877033...c²r₀/G,∞)=(0,∞)` | Z | For fixed `r₀`, `Mcrit(r₀)=0.878794537877033...c²r₀/G`; across the printed free core scale, the infimum is 0 kg. |

Derivation: with `x=r/r₀`, `a=r_g/r₀`, the pinned metric gives `f=1-(a/x)[1-exp(-x³/a)]`. The double-horizon equations `f=0`, `∂f/∂x=0` give `xcrit=1.4957095399086404...`, `acrit=1.7575890757540665...`, and therefore `Mcrit=(acrit/2)c²r₀/G`. Entry 18's printed de Sitter relation makes this equivalently

`Mcrit(ε₀)=0.878794537877033... (c²/G)sqrt(3c⁴/(8πGε₀))`.

The manifest defines but does not fix `ε₀`/`ρ₀`; hence `ε₀→∞` permits `Mcrit→0+`. Thus `P=∅`, `Z={R0}`, `I=∅`. A positive floor was unreproduced from the stated inputs. No completion was chosen. The scientific family is the one-parameter family above; it has no positive global lower bound and therefore no positive floor interval or value in kg to file.

C3 was NOT_RUN under §4 class 4's direct-reach clause: no positive floor survives, so the probe has no candidate. The probe script was not opened and `_c3_relations.json` was not written.

## C4 GR benchmark

As `r→∞`, the printed mass integral gives `M(r)→M`, hence `R_g(r)=2GM(r)/c²→2GM/c²=r_g`. Therefore `g_tt=1-R_g(r)/r→1-2GM/(c²r)` and `g_rr→-[1-2GM/(c²r)]⁻¹`, with angular term `-r²dΩ²`: exactly the Schwarzschild exterior form. Premises were only the printed mass integral, asymptotic finite mass, metric, and distant-observer mass identity. No interior premise (`r₀`, `ρ₀`, de Sitter limit, pressure, or regularity condition) entered. `C4_benchmark.md` contains the full algebra and premise list.

## C6

C6 was never engaged under §5 C6 and §5a because the scientific partition produced no positive-floor quantity. `C6_BREAKER_TEST=NOT_RUN`; no per-condition result or four-row comparison table is applicable on this path. Artefact: `C6_breaker.md`.

## Artefacts and SHA-256

| artefact | sha256 |
|---|---|
| `R3D_RUN_codex_20260905/C1_digests.txt` | `9ea143b7d851bb973016f7d4be8ee318aedb491ac71d0d207ddf3a9587d0ea5a` |
| `R3D_RUN_codex_20260905/C2_census_entry18.txt` | `15acfa441b59018b217edaba140dab5c1b462e319ae12278e96b75560b4484e0` |
| `R3D_RUN_codex_20260905/C2_census_entry19.txt` | `74c37abd9d815e13bad5bb586b287c8d0a5a9f24f7c87232aef35f556553445b` |
| `R3D_RUN_codex_20260905/C2_census_entry20.txt` | `b57f3416cea43a9353f42a53d889862d8eaee7185009cc114c473764246aaa88` |
| `R3D_RUN_codex_20260905/C2_census_entry55.txt` | `a203f29a982e05b7f7d2f0408fccdbd303b4542ef454a6ee6c6d9bab97c5c631` |
| `R3D_RUN_codex_20260905/C2_ledger.md` | `0cc528e311da7f2242dc3d4b6fcd8a716e8ebc40c503c6ef45eeb5664c6d34cb` |
| `R3D_RUN_codex_20260905/C3_probe.txt` | `c94331eb8ad7f671e5c7f9579d9ea444ba50b484432f73451b121f451945ce78` |
| `R3D_RUN_codex_20260905/C4_benchmark.md` | `decae07b4510ea2ae4b0fa24dbde59aa737f08f07c24320711599999a8039805` |
| `R3D_RUN_codex_20260905/C5_harness.txt` | `c4b7e64429c2544724f1e6fc808a434c893a17a7e620bcfc93b154074c182d6a` |
| `R3D_RUN_codex_20260905/C5b_paths.txt` | `7f093dfe75d2f1af8fc7d5a606a7706fd18f7042ac047fa17f7365be1f0a22da` |
| `R3D_RUN_codex_20260905/C6_breaker.md` | `b4a2d8c66d14176e488e72566404c98682596ba09334f1c0c194a21776a305ed` |
| `R3D_RUN_codex_20260905/build_census.py` | `25d5ed62433003fd754533ef07b3ef1e9bc0c7be4fc1593eb5952b6aa21abf41` |
| `R3D_RUN_codex_20260905/limbA.md` | `277c15a282fc3fb7244ab03b03e32efbec3d1e909e678bc2a73636de12023210` |
| `R3D_RUN_codex_20260905/limbB.md` | `70b43e046aab81bec05e811f4679bdfd9186c2aab7795c1789ed5c73469029e6` |

## OBSERVATIONS ON THE PROTOCOL

Nothing in the protocol was changed.

1. The brief says the four sources contain 3,171 non-blank lines, but applying the protocol's stated non-blank rule to the pinned bytes gives 286 + 937 + 753 + 1,196 = 3,172. Each source reconciles independently; the brief/protocol discrepancy did not change the census or result.
2. Section 9's path scope is unusually brittle for ordinary inspection: the sources and own artifacts are allowed, but utility executables chosen to inspect those artifacts are not covered unless they are a necessary consequence of a specifically mandated command. I would state an explicit allowlist of inspection utilities or require all inspection through `/usr/bin/python3`. The frozen rule was applied as written, producing the terminal `R3D_NO_CLASS`.
3. The source prints a positive critical mass only conditionally on a freely specified core density/scale. The protocol's reading-set construction correctly exposes that conditional floor as a zero-infimum family rather than silently choosing a density.

R3D_RUN_CODEX_COMPLETE
