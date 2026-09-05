# R3D — CHECK SHEET, one page, plain words (Tori, 2026-09-05)

**The question.** Do Dymnikova's "regular-core" black holes — black holes whose singularity is replaced by a small
de Sitter core — as printed in four pinned papers, fix a smallest possible black-hole mass? If they did, that number
would be a candidate counterexample to the lane's pattern (constructions of this kind never fix a magnitude).

**What happened.** Two blind seats on different engines (codex, kimi) ran the frozen protocol V30 (sha256 `a99aad15…`)
on the same four sources, unaware of each other. **Both found the same physics.** They split on a procedural point.

**The physics, in one paragraph.** The papers print a size–mass relation (the horizon radius `r_g = 2GM/c²`, and the
core-scale relation `r*³ = r0² r_g`) and one mass bound: the metric is a black hole only for `M ≥ M_crit`, where
`M_crit` is the mass at which the two horizons merge. No paper prints `M_crit`. Both seats, and I independently, solved
for it: **`M_crit = 0.8788 c² r0 / G`**, where `r0` is the core scale set by the interior vacuum density `ε0` through
`r0² = 3c⁴/(8πGε0)`. **Nothing in the four papers fixes `ε0` or `r0`** — the 1992 paper says "if" it is the GUT
density, or "if" Planckian, as worked examples. So the smallest black-hole mass is a *family*, one value per chosen
core density, and over the family its infimum is zero. **A positive floor was unreproduced from the stated inputs.**
That is the protocol's class 4 (V30 name `DYM_NO_POSITIVE_FLOOR`; V31 name `DYM_POSITIVE_FLOOR_UNREPRODUCED`).

**The split.** codex's own path-list control (C5b) failed: it opened two inspection tools (`rg`, `head`) that the
protocol's scope rule does not cover, and under §4 a scientific class may be filed only from a control-clean report,
so it filed `R3D_NO_CLASS`. kimi's report was control-clean and filed class 4 — but kimi used similar tools (`wc`,
`grep`, `awk`) and marked them in scope under the rule's general clause. §9 sends exactly that split to a third seat,
which also re-runs the failed control once (§4 class 6). **Third seat: agreed with kimi — `DYM_NO_POSITIVE_FLOOR`; its one C5b re-run for codex PASSED, so §4 class 6 files the common class.**

**FILED CLASS: DYM_NO_POSITIVE_FLOOR** (V30 name; V31 name `DYM_POSITIVE_FLOOR_UNREPRODUCED`).

**Controls (tokens as each seat printed them).**
| control | codex | kimi | what it certifies |
|---|---|---|---|
| C0 reachability | PASS (carried) | PASS (carried) | every outcome was reachable before the freeze |
| C1 source identity | PASS | PASS | the four files hash to the manifest |
| C2 census + ledger | PASS | PASS | every non-blank line assigned; 286/937(936)/753/1196 reconcile |
| C3 deletion probe | NOT_RUN | NOT_RUN | no floor to probe (class-4 clause) |
| C4 GR benchmark | PASS | PASS | the metric is Schwarzschild outside |
| C5 harness | PASS | PASS (cmd 2 from a file, not `-c`) | Python 3.9.6, sympy 1.14.0, interpreter digest |
| C5b path list | **FAIL ×2** | PASS (row 9 under the general rule) | nothing outside scope was opened |
| C6 breaker test | NOT_RUN | NOT_RUN | no positive floor to test against the pattern |

**What YOU should verify yourself (five minutes, source lines quoted).**
1. `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt`, lines 94–95: `rg = 2GM/c²` (eq 6);
   lines 126–127: `r0² = 3c⁴/(8πGε0)` (eq 9); line 148: `r*³ = r0² rg` (eq 13). These are the relations used.
2. Same file, lines 177–183 and 301–304: "For an object with the mass of several solar masses and ε0 corresponding
   to the GUT energy…", "If the final isotropic vacuum state … is achieved at the GUT energies … If this happens at
   the Planckian energy…" — **conditional examples, not a fixed density.**
3. `dymnikova_2019_universe_clean.txt`, lines 277–279: "Within the range of masses M ≥ Mcrit, where Mcrit
   corresponds to the double horizon…" — the only printed mass bound; search the file for a formula for Mcrit: none.
4. Same file, line 252: "ρ0 is the vacuum density at r = 0" — defined, never fixed.
5. `gr-qc_0611022_clean.txt`, lines 143–148: the inequality `q² < (16/27)M²` belongs to Bardeen's metric, a
   different branch. `2007.06664_clean.txt`, line 1099: "1 ≪ j ≪ Gm/ℓ_P" is a validity regime with a free `j`.
6. Reproduce the number: solve `f(x,a) = 1 − (a/x)(1 − e^{−x³/a}) = 0` and `∂f/∂x = 0`; you get `a = 1.7576`, so
   `M_crit = (a/2) c² r0/G = 0.8788 c² r0/G`. Three routes got `0.878794537877033…`.
7. Confirm the reports' first lines: `ACCESS_SHA=a99aad15f168290fa5afaaf957d478cedd4cf57cb967e97dd3ea8d6b2a25840b`.

**What this result is NOT.** Not a claim that the branch has no minimum mass — a claim that none was reproduced from
these four papers' stated inputs. Not a test of the lane's pattern: the breaker (C6) never ran because there was no
number to test. No tier, warrant, standing or stamp moves. The wording rule holds: "unreproduced", never "error".

**Receipts.** `R3D_RUN_REPORT_codex_20260905.md`, `R3D_RUN_REPORT_kimi_20260905.md`, `R3D_RUN_THIRD_SEAT_20260905.md`,
run directories `R3D_RUN_{codex,kimi}_20260905/`, `R3D_RUN_LOG_20260905.md`, Tori's blind route
`R3D_TORI_SECOND_ROUTE_BLIND_20260905.md` (committed before any report existed, sha256 `87af14ff…`).

**Addendum (2026-09-05 14:06:04 KST), on Duho's order "adjudicate row 9".** Ruled to the letter: kimi's row 9 utilities were OUT of scope and
its harness command 2 was not the printed form — so, like codex, kimi's original report was not control-clean. The
protocol's remedy is one fresh re-run of each failed control by the third seat; all three re-runs (codex C5b, kimi C5b,
kimi C5) passed. **Filed class unchanged: `DYM_NO_POSITIVE_FLOOR`.** Receipt: `R3D_RUN_THIRD_SEAT_ROW9_20260905.md`.
