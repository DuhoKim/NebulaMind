# BHU cosmology — receipted numbers for the video

**Tori, 2026-09-04 17:23 KST.** For Blanc, who writes the narration and builds the video. Duho's order via Blanc,
17:16 KST: the actual numbers behind the headline coincidence, and the honest framing.

**Blanc: use only what this note certifies.** §7 marks the receipt status of every number. Anything marked NOT
COMPUTED must not appear in the video, and anything marked QUOTED is the paper's number, not ours.

**Blind-doubled.** Two seats computed everything independently from the same pinned inputs and **agree on every
quantity to the precision quoted** (`bhu_video_numbers_claude.py` / `.out`, `bhu_video_numbers_codex.py`,
`BHU_NUMBERS_codex_RESULT.md`). No disagreement to report. The only difference is rounding: 7.7% vs 7.671% for the
same H₀ spread.

---

## 1. Inputs, with status

| input | value | status |
|---|---|---|
| `G` | `6.67430 × 10⁻¹¹ m³ kg⁻¹ s⁻²` | CODATA 2018, cited |
| `c` | `2.99792458 × 10⁸ m/s` | **exact by definition** |
| `H₀` | `67.4 ± 0.5 km/s/Mpc` | Planck 2018 (TT,TE,EE+lowE+lensing) |
| `Ω_Λ` | `0.6889` | Planck 2018 |
| `M☉` | `1.98892 × 10³⁰ kg` | cited |
| 1 Mpc | `3.0856775814913673 × 10²² m` | IAU definition |
| 1 light year | `9.4607304725808 × 10¹⁵ m` | IAU definition |

`H₀ = 2.184285 × 10⁻¹⁸ s⁻¹`.

**On the H₀ tension, plainly:** the CMB value (67.4) and the local distance-ladder value (~73) differ by about 8%,
and that **moves the mass by 7.7%** — it changes the last digit of the quoted mass. **It does not touch the ratio in
§4, which stays exactly 1 at every H₀ we tested, from 50 to 500.** The tension is real and it is irrelevant to the
point of this video.

## 2. Mass-energy inside the Hubble radius

| quantity | formula | value |
|---|---|---|
| critical density | `ρ_c = 3H₀²/8πG` | `8.5329 × 10⁻²⁷ kg m⁻³` |
| Hubble radius | `R_H = c/H₀` | `1.3725 × 10²⁶ m` = **14.51 billion light years** |
| enclosed mass | `M = (4/3)π ρ_c R_H³` | `9.2410 × 10⁵² kg` |
| the same, in suns | | **`4.65 × 10²² M☉`** |

Closed form, computed independently and agreeing to floating-point: `M = c³/(2GH₀)`.

## 3. Schwarzschild radius of that mass

`R_s = 2GM/c² = 1.3725 × 10²⁶ m` = **14.51 billion light years**.

## 4. The ratio

**`R_s / R_H = 1.000000000000`**

Not "close to 1". Exactly 1, to every digit either seat carried.

## 5. THE HONEST PART — why it is exactly 1, and what that costs the claim

**This is the part that matters more than the numbers, and the video should not skip it.**

Substitute the definitions into each other:

```
M   = (4/3)π ρ_c R_H³
    = (4/3)π · [3H₀²/(8πG)] · [c/H₀]³
    = c³ / (2GH₀)

R_s = 2GM/c²
    = (2G/c²) · c³/(2GH₀)
    = c/H₀
    = R_H
```

The `G`s cancel, the `c`s cancel, the 2 cancels. **`R_s = R_H` is an algebraic identity for any spatially flat
universe at critical density** — it is the Friedmann equation rearranged. Both seats derived this independently and
reached the same conclusion.

We tested it numerically as well, at `H₀` = 50, 67.4, 73, 100 and 500 km/s/Mpc. **The mass changes — inversely with
`H₀`. The ratio is 1.000000000000 every time.**

### What that means for "the numbers match, so we are inside a black hole"

**The match is not evidence for the claim.** Saying "the Schwarzschild radius of the universe's mass equals the Hubble
radius" is the same statement as "the universe is spatially flat at the critical density" — which is measured
independently, and which every standard cosmology already says. Any flat critical-density universe reproduces the
match exactly, whether or not it is inside anything at all.

**One sentence for the narration:** *the numbers match perfectly, and that is exactly why the match proves nothing —
it is a restatement of flatness, not a discovery on top of it.*

This does not make the black-hole-universe idea wrong. It means **this particular coincidence cannot be the argument
for it**, and a video that presents it as the argument would be overselling. The corpus's real arguments have to be
found elsewhere — and this lane's audit of where they stand is a separate story.

## 6. What the corpus's own papers print

**Entry 56 — Gaztañaga (MNRAS), abstract L29 and Eq. (21) L259: "a mass M ≃ 6 × 10²² M☉".**

Ours is `4.65 × 10²²`. **These are not in conflict — they are different quantities.** He does not use the Hubble
radius: he sets `Λ ≡ 3/r_S²` (L28, L252), so his radius is the Λ (de Sitter) radius,
`r_S = √(3/Λ) = c/(H₀√Ω_Λ) = 1.2048 R_H`, and his mass is correspondingly larger by the same factor. Recomputing his
definition from Planck inputs gives **`5.60 × 10²² M☉`**, which is his `≃ 6 × 10²²` — agreement, once you use his
radius rather than ours.

- ours: the mass whose Schwarzschild radius equals the **Hubble** radius → `4.65 × 10²² M☉`
- his: the mass whose gravitational radius equals the **Λ** radius → `5.60 × 10²² M☉` (he prints `≃ 6 × 10²²`)

**Entry 1 — Pathria (1972), L399–L405** prints a *third* identity: `R_s = R_max`, the Schwarzschild radius equal to
the maximum expansion radius of a **closed (k=+1)** universe — "the fact that the two, whenever they exist, are
identically equal can hardly be a coincidence". That is **not** the flat-universe identity computed here; it is a
different geometry, and Pathria states no mass value at that point. Our numbers neither confirm nor contradict it.

**If the video quotes a mass, it should say which of the three quantities it means.** They differ by ~20% and they are
not the same statement.

## 7. Receipt status of every number

| quantity | status | basis |
|---|---|---|
| `ρ_c`, `R_H`, `M`, `R_s`, `R_s/R_H` | **RECEIPTED** | equations in §2–§4 + the §1 inputs; blind-doubled |
| `M` in solar masses | **RECEIPTED** | `M / M☉` |
| `R_H`, `R_s` in light years | **RECEIPTED** | IAU light year |
| the 7.7% H₀ spread | **RECEIPTED** | computed from 67.4 vs 73.0 |
| Gaztañaga's `r_S`, `M_T` recomputed | **RECEIPTED** | his `Λ = 3/r_S²` (L28, L252) + Planck `Ω_Λ` |
| Gaztañaga's "≃ 6 × 10²² M☉" | **QUOTED FROM SOURCE** | abstract L29, Eq. (21) L259 — his number, not ours |
| Pathria's `R_s = R_max` | **QUOTED FROM SOURCE** | L399–L405; no mass value printed there |
| age of the universe | **NOT COMPUTED** | do not quote from this note |
| number of atoms, stars, galaxies | **NOT COMPUTED** | do not quote from this note |
| anything about entropy, information, holography | **NOT COMPUTED** | not in scope; do not quote |

## 8. Receipts

```
bhu_video_numbers_claude.py    3927fdcc658a3cd078fc3dfb1e5c832762e30d7e3c694029e0a76e00bb095d8e
bhu_video_numbers_claude.out   ab3f127b2d78d98b199646be56b425e7ebde10cb66fd4c63e94c2dabe6a736d2
bhu_video_numbers_codex.py     0b225025071fc15103faa702baea23e5fcaa1afc9f5a1e227b6f167fe989baee
BHU_NUMBERS_codex_RESULT.md    c7b64e5c483940100469c7230e83a0c78dea4a35c1434b4f30ccdcf2aa7917fd
bhu_video_numbers_codex.out    5acba86a4d50ba2bc5d203287d1eb26e6d6cb42a6891ea86bd40eba57db67208
```
Both scripts run under `python3`; Tori executed both. Two seats, independent, **no disagreement on any quantity** —
the comparison table is in the commit message and reproducible by running the two scripts.

## 9. Boundaries

This is a receipted numbers note for a public explainer. **It is not a study**, moves no tier, warrant token, standing
or stamp, and needs no ruling. Paper HOLD stands; nothing outward from this lane. The scientific verdicts on the
corpus live in the K-series results, not here.

BHU_NUMBERS_FOR_VIDEO_COMPLETE
