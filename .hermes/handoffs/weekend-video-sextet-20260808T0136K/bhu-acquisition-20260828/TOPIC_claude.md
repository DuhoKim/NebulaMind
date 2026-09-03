# TOPIC_claude — three study topics from the BHU corpus audit (claude seat, blind; written 2026-09-03 16:16 KST)

Reading set: exactly the six files named in `_TOPIC_SEARCH_BRIEF.md`. Citation keys: S = `BHU_CORPUS_SYNTHESIS_20260902.md`,
WT = `WARRANT_TABLE_20260903.md`, WDR = `WARRANT_DOUBLE_RECONCILIATION_20260903.md`, FM = `PROGRAM_A_FREEDOM_MAP_20260902.md`,
PC = `PROGRAM_C_FLUX_RESULT_20260902.md`, WIL = `WHAT_IS_LEFT_20260903.md`; "Lnn" = line number in that file. Every number
below is quoted from one of these six files at the cited line; where a study needs a published value the record does not
carry, the value is named, not quoted. Nothing here moves a tier, a standing, or a warrant token.

## Topic 1

1. TITLE: Is our universe at a local maximum of black-hole production? A one-parameter computation of Rothman & Ellis's
   "primary requirement". Grows from entries 31 and 6 (and the challenge papers pinned under 31: Rothman & Ellis 1993,
   Harrison 1995, Silk 1997 — S L66-70, WT L8).
2. CLAIM: Cosmological natural selection (entry 31; its direction stated in entry 6) requires that every small change of a
   parameter reduces the number of black holes produced per comoving volume (S L67-68); the study computes the sign of
   dN_BH/dA_s at the measured primordial scalar amplitude A_s, counting both primordial and stellar-collapse black holes,
   and tests whether the local-maximum premise survives for this one parameter.
3. FALSIFIER: The premise is falsified for A_s if the computed N_BH(A_s) is monotone increasing through the Planck 2018
   value (dN_BH/dA_s > 0 at the measured amplitude, with the primordial term included). It survives only if the sum of the
   primordial and stellar terms has a maximum at the measured A_s, or if the study derives — rather than assumes — a reason
   to exclude the primordial term, which is what Rothman & Ellis call "the primary requirement" and the record says is
   unanswered (S L68-69). Measurement met: the Planck 2018 A_s (published value; not quoted here because the record carries
   none). Theorem met: the CNS optimality claim as the record states it — the selection argument "needs every parameter
   change to reduce black holes" (S L67-68); entry 6's sign is currently `W_DIRECTION_ASSUMED` because "the direction
   follows only definitionally from the assumed peaking plus a typicality assumption" (WT L47). Secondary confrontation:
   the stellar-collapse term must either reproduce the maximum-mass dependence entry 31 borrows (Bethe–Brown
   kaon-condensation calculations [52–54], WT L8) or state where it departs from it.
4. COST: 4–5 seat-days. Data: Planck 2018 A_s and n_s (the record quotes only n_s = 0.9649 ± 0.0042, S L46). Compute: a
   semi-analytic halo/collapse count and a primordial-black-hole abundance integral over a declared small-scale extrapolation
   of the primordial spectrum; a laptop. Otherwise pure theory.
5. GAPS CLOSED: entry 6 `W_DIRECTION_ASSUMED` (WT L47; packet-class token, WDR L49) → derived-or-refuted for one named
   parameter; entry 31's `W_BORROWED` cell with the pinned "DISPUTED" challenge (WT L8; S L66-70) gains the first in-corpus
   computed answer to the Rothman & Ellis requirement (S L68-69). Sharpens the live falsifier: today the record's only
   direct kill route is entry 31's 2.5 M☉ bar, "drifting away from firing as the error tightens" (S L60-66, L158-159); if
   the maximum premise fails for A_s, the premise itself becomes a second, observation-independent route.
6. SCORES: CONTESTED 5 — the only calibrated row whose warrant is "DISPUTED and pinned" against three published
   challenges (S L66-70; WT L8), with the central objection recorded as "unanswered" (S L69). TRACTABLE 4 — semi-analytic,
   no new data, standard methods; one declared choice (the small-scale spectral extrapolation) must be pre-registered and
   varied. Circularity: none — the measured A_s is not an input of the CNS premise. FRONTIER = 5 × 4 = 20.
7. RISKS: A proponent restricts "parameters" to low-energy constants and excludes primordial black holes by definition —
   Rothman & Ellis's exact point (S L68) — so the computed sign is conceded as true and declared out of scope; the study
   then returns a result nobody disputes and nobody accepts as bearing.

## Topic 2

1. TITLE: Does the Gaztañaga finite-mass top-hat join its empty exterior without a shell? An Israel / Barrabès–Israel
   junction computation confronted with Easson's Proposition 2. Grows from entries 56 (with the 23–27 series), 22, 5 and 4.
2. CLAIM: The entry-56 universe — a finite FRW top-hat with an empty exterior and Λ = 3/r_S² (WT L59; S L110) — admits a
   shell-free junction to its exterior, as the series assumes when it treats the exterior as empty; if so it is a
   nondegenerate comoving no-shell closed-FRW daughter and must satisfy Easson's Proposition 2 bound (S L123-124) on the
   closed-daughter limb Duho kept on 2026-09-03 (WT L48).
3. FALSIFIER: Two computations, each meeting an existing theorem. (a) The junction jump: compute [K] (timelike boundary,
   Israel) or [K_uu] (null boundary, Barrabès–Israel) at the top-hat boundary for the entry-56 construction (finite top-hat
   and empty-exterior boundary closure, SOURCE lines 147–160; GHY boundary evaluation, SOURCE lines 206–218 — WT L59). The
   claim is wrong if the jump is nonzero — the outcome entry 5 proved for the sibling Pathria case (pressureless closed-FRW
   interior with 0 ≤ Λ ≤ Λ_c joined at χ = π/2 to a Schwarzschild–de Sitter exterior with the same Λ: [K_uu] ≠ 0, a
   pressure-only null shell p = ρa/4; S L117-121) — in which case the "empty exterior" carries a shell whose surface
   stress-energy the study writes down and checks against the energy conditions. (b) If the jump vanishes, Easson's
   Proposition 2 applies (entry 22 "bounds nondegenerate comoving no-shell closed-FRW daughters of static, asymptotically
   flat, finite-ADM parents", S L123-124; domain narrowed to the closed-daughter limb, WT L48); the claim is wrong if the
   entry-56 daughter violates that bound. Either branch is decided by the algebra the record already holds receipts for
   (entry 5's method, WT L34; entry 4's junction assumptions, WT L38). Consistency check: entry 24's in-paper bound
   χ_§ ≲ χ_O (WDR L29) must be recovered by the same geometry.
4. COST: 3–4 seat-days. Data: none (pure theory). Compute: symbolic algebra only, against the lane's pinned texts for
   entries 56, 22, 5, 4 (56 pinned 2026-09-03 15:53 KST, WIL L16).
5. GAPS CLOSED: entry 56 `W_DIRECTION_ASSUMED` with its borrowed "empty-exterior boundary closure" (WT L59) → the closure
   becomes derived or refuted; entry 22 `W_PROOF_CITED` (WT L48; WDR L35) → the proposition is applied, in-corpus, to the
   one published construction it was written against, turning "restricts, does not kill" (S L126-128) into a decided
   yes/no for entry 56; entry 5's open clause "other FRW/black-hole junction classes are not excluded" (S L121) closes for
   one more class; entry 4's `W_PROOF_CONTESTED` (WT L38) gains a second junction case with Λ ≠ 0. Bears on the packet
   (6, 22, 23, 25, 27 — WDR L49): a forced shell is a physical ingredient the 23–27 cutoff sentence never mentions.
6. SCORES: CONTESTED 4 — a 2026 published no-go (entry 22) against the 2020–23 series, adjudicated 2026-08-31 as
   restricting rather than killing and re-ruled 2026-09-03 (S L126-128; WT L48); its own warrant cell split codex/claude
   and needed a third seat (WDR L35). TRACTABLE 4 — the same junction algebra entry 5 completed for the sibling case
   (S L117-121), no data; the one point of care is the exterior branch for Λ = 3/r_S² with a finite interior mass, which is
   not the 0 ≤ Λ ≤ Λ_c dust case entry 5 treated (S L117-118). Circularity: none — the boundary is fixed by the series'
   own geometry, not by any CMB statistic. FRONTIER = 4 × 4 = 16.
7. RISKS: The entry-56 construction is under-specified at its boundary (the GHY evaluation is cited from Gaztañaga 2022c,
   WT L59), so no unique junction exists to compute and the study returns "the paper does not fix its own boundary" — a
   licensing statement of the FM L156-159 kind, not a yes/no.

## Topic 3

1. TITLE: A causal boundary that changes the transfer physics: linear perturbations of the finite top-hat with junction
   conditions at χ_§, confronted with the pre-registered Planck S₁/₂ test. Grows from entries 23–27 and 56, on top of PC
   and FM; takes Topic 2's junction as input.
2. CLAIM: Replacing the infrared spectral window used by every row of FM §6 (FM L140-147) with a genuine boundary — linear
   scalar perturbations on the finite FRW patch of comoving radius χ_§ = (3.149 ± 0.006) c/H₀ = 14,015 Mpc (FM L33), with
   the top-hat's junction conditions imposed at χ_§ and a ΛCDM primordial amplitude fixed by high-ℓ data with low-ℓ held
   out (FM L84-85) — predicts the observed large-angle correlation deficit at a percentile above the best existing
   refinement.
3. FALSIFIER: The prediction is pushed through the Phase (b) pre-registered estimator (one uniform-weight pixel-pair
   estimator on the masked SMICA map, 3° bins, monopole+dipole removed, 5 × 2,000 masked skies; FM L196-207), whose
   control C2 reproduces the literature's cut-sky value on the real map: 1,223 μK⁴ (FM L203). The claim is wrong if
   P(S₁/₂ ≤ observed) under the boundary model is ≤ 2.2–2.8% — the best existing refinement, Reading A at 2π/χ_§
   (FM L212) — and a fortiori if it is ≤ ΛCDM's 0.15–0.20% (FM L211). Two theorems it must clear before any sky is drawn:
   (i) if the boundary condition reduces to a compactly supported convolution W ⋆ δ = 0, Program (C)'s F2 result applies —
   Paley–Wiener leaves no continuous power spectrum except P ≡ 0 (PC L19-22; top-hat transform zeros at kR = 4.4934,
   7.7253, PC L37-38) — and the model is dead; (ii) if it reduces to a spherically symmetric functional about the
   observer, F1 applies and every C_ℓ for ℓ ≥ 1 is exactly unchanged (PC L15-18, L60-62). The study's first deliverable is
   therefore a proof that the junction-condition problem is of neither form. A second falsifier: the boundary model must
   not carry the ~5% excess at first-acoustic-peak scales the no-splice Reading B construction carried (FM L130-132),
   which measured high-ℓ data would notice.
4. COST: 10–14 seat-days. Data: the Planck SMICA map and mask already in the lane (S L96-97; FM L203). Compute: the lane's
   `phaseB_pipeline.py` / `phaseB_production.py` and the validated S₁/₂ operator `cutoffA_s12_machinery.py` (FM L229-236),
   plus a new mode-function/Boltzmann solve on the bounded patch (CAMB is the reference solver at FM L84); one workstation.
5. GAPS CLOSED: the freedom map's declared structural caveat — "a genuine causal boundary could alter the mode structure,
   projection, or evolution themselves, and no receipt here constrains that" (FM L174-177) — becomes a receipt; open flag
   (i), that causal disconnection does not imply zero correlation under common initial conditions (FM L56-59), is answered
   constructively, since the boundary state is declared and the correlation beyond θ_§ = 57.4° (FM L33) is computed rather
   than asserted; entries 23, 25, 27 `W_DIRECTION_ASSUMED` ("the sign is the causal premise restated", WT L49, L51) and 56
   (WT L59) → derived-or-refuted for one declared boundary model. It does not overturn the 23–27 ruling (S L106-109): the
   amplitude would belong to the study's declared completion, not to the papers — exactly the licence FM L156-159 words.
6. SCORES: CONTESTED 4 — the corpus's sharpest observational claim (S L82-83); the observed deficit sits at 0.15–0.20% under
   ΛCDM (FM L211); the author concedes the amplitude cannot be quantified without an initial-conditions model (FM L42-44)
   while four seats found no licensed perturbation condition at all (FM L48-52). TRACTABLE 3 — pipeline and data exist and
   are validated (FM L198-207), but the bounded-patch perturbation problem with a junction is new work, and Topic 2 may
   find the boundary shell-bearing (S L121), adding a shell degree of freedom. Circularity: none — χ_§ comes from
   Ω_Λ = 0.69 ± 0.01 measured by supernovae/BAO (FM L31-33) and the amplitude from high-ℓ with low-ℓ held out (FM L84-85).
   FRONTIER = 4 × 3 = 12.
7. RISKS: The boundary alters mode functions only at wavelengths comparable to the patch, and their projection through
   ΛCDM transfer physics lands where every prior refinement landed — at or below the ~3% ceiling (FM L219-220; Reading B
   rows 0.60–1.6%, FM L214-215) — so the study returns one more completion under the same ceiling.

ranking: 1, 2, 3
