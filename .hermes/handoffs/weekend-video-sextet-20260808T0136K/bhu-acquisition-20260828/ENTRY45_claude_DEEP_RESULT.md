AUDIT_FLAG_MEMBERSHIP

# Entry 45 deep audit — claude-seat (blind, independent), 2026-09-02 19:42 KST

Brief: `ENTRY45_AUDIT_BRIEF_20260902.md`. Source read in full: `../bhu-reading-20260823/sources/2210.15186_clean.txt` (lines 1–1137; body ends line 899, references 901–1124). No ENTRY45_*RESULT* file and no codex/kimi-named file was opened. Line receipts are line numbers of the pinned source. Equation numbers are the paper's.

Verdict in one line: the derivation is a standard, essentially correct near-horizon Bogoliubov calculation with the stated approximations asserted rather than shown; the "departure from Planck" is a free function, not a geometric prediction; and the paper, in its own words, puts *us* in the black-hole EXTERIOR (line 657) and disclaims relevance to the observable Universe twice (lines 40–41, 97). It neither makes nor tests "our universe is the inside of a black hole". Tier CONSISTENCY-ONLY is the ceiling if it stays; whether it stays is the flag.

---

## 1. The setup — derived vs. cited vs. asserted

**Geometry (derived, checked).** Schwarzschild in Kruskal light-cone form (1)–(6), lines 52–93. WH region U,V<0 bounded by the past singularity (line 97). Tortoise/conformal time τ = −r_* (7)–(8), lines 100–123; WH metric in Kantowski–Sachs form (9)–(10), lines 125–137, with a(τ) = (2GM/r − 1)^{1/2} contracting along x ≡ t and r(τ) expanding on the S². I re-derived: near r→0, τ ≃ r²/4GM gives (11) (line 146–148) ✓; cosmic time (15) (line 181) integrates dt̂ = dr/√(2GM/r − 1) correctly and gives 0 < t̂ < πGM (line 185) ✓; Kasner exponents p = (−1/3, 2/3, 2/3) (lines 218–219) satisfy Σp = Σp² = 1 ✓; H₁H₂ = −GM/r³ (23) ✓. Two cosmetic slips: (12) drops a constant e^{−1} inside the exponential prefactor (line 156; harmless), and Eq. (4) T/R = tanh(t/4GM) (line 74) is the exterior relation only — inside the WH it is coth, which is what (48) at line 458 actually uses, so nothing downstream is affected.

**Field equation (derived, checked).** Massless test scalar, no backreaction (lines 249–250, asserted as a limit, standard). Spherical decomposition (24)–(26), canonical action (27), master equation (28), Regge–Wheeler form (29)–(30), lines 253–299. I checked the 2GM/r³ term: it is r''/r with dr/dτ = 2GM/r − 1, giving (2GM/r³)(1−2GM/r) ✓. Spin generalisation (31) is stated, not derived (line 301–310; standard RW, cited [26] at line 289).

**Near-singularity solution (derived, checked).** With r² ≃ 4GMτ the potential becomes −(1−s²)/4τ², Eq. (33) (line 335) ✓; Hankel solution (34) with order ν = s/2 (line 341) ✓; Wronskian normalisation |C₂|² − |C₁|² = π/4 (38) (line 377) ✓ — I recomputed it from W(H⁽¹⁾,H⁽²⁾) = −4i/πz.

**Horizon matching and Bogoliubov coefficients (derived, checked).** Asymptotic (40) (line 393) ✓; plane-wave limit (41)–(44) (lines 399–422); Kruskal map (48) with κ = 1/4GM (line 458–462) ✓ (I checked UV = G²M² e^{−τ/2GM} and U/V = e^{−x/2GM}); the integral (55) → Γ(−iω̃/κ)(ω/4κ)^{iω̃/κ} e^{πω̃/2κ} (lines 522–529) ✓ and its β partner (57) ✓; |α|² = e^{2πω̃/κ}|β|² (61) ✓; (62) ✓; the d = b_{−ω̃} identification (65) (line 602) follows because U(u) has the same functional form on both sides of V = 0 (lines 597–600) ✓; Planck spectrum (68) at T_H = 1/8πGM (69) ✓. Appendix A (lines 857–899) re-derives (50) by the Klein–Gordon inner product — a genuine internal cross-check. The left-ℐ⁻ sector (70)–(84) (lines 651–753) is the mirror computation, ᾱ = α*, β̄ = β* (83) ✓.

**Non-vacuum sector (derived, checked, one normalisation slip).** (85)–(92), lines 763–830. I re-did the contraction: with P, Q the right/left-mover Killing-mode operators (88)–(89), ⟨0_K|b†b|0_K⟩ = |C₂|²·n + |C₁|²·(1+n), n = (e^{2πω̃/κ}−1)^{−1}, which is the first line of (92) ✓. The second line, n + |C₁|² coth(πω̃/κ), requires |C₂|² − |C₁|² = 1, i.e. the unit normalisation stated at line 758 ("C₁ = 0 and C₂ = 1"), which contradicts (38)'s π/4 and (39)'s C₂ = √π/2 (lines 377–386). This is a convention inconsistency, not an error in the physics: rescale the C's by 2/√π and the coth form is exact.

**Cited, not derived:** Hawking effect framework [27–34] (line 316); Kantowski–Sachs [20] (line 35); WH instability [22] (line 40); the tunnelling comparisons [23,24] (line 44, 646–647).

**Asserted rather than shown (the honest list):**
- (a) Dropping ℓ(ℓ+1) "with reasonable accuracies" and working at ℓ = 0 (lines 312–313) — argued by the two asymptotic limits only.
- (b) Taking the τ→0 Hankel solution (34) as "qualitatively valid for the entire region 0 < τ < ∞" (line 347; admitted unsolvable at line 332). This is the load-bearing one: the potential in (32) is non-zero between the two asymptotic regions, so a mode that is pure H⁽²⁾ at the singularity is not pure e^{−iωτ} at the horizon for ω ≲ κ; the singularity-vacuum ↔ horizon-vacuum identification (C₁ = 0 ⇔ "vacuum initial condition", lines 349–351, 758) is therefore only a high-frequency statement, and the paper does not bound the induced C₁.
- (c) Exterior Regge–Wheeler bump neglected "for large enough ω" (lines 427, 649, 852) — greybody factor acknowledged, not computed.
- (d) C₁ = 0 called "the natural choice… may be compared to the standard Bunch-Davies vacuum… which carries the lowest energy" (lines 381–383) — an analogy; no energy minimisation is performed on this time-dependent background.
- (e) δ(0) "replaced by the physical length" (line 513) — the x ≡ t direction is infinite in the eternal manifold.

**Adversarial point on the physics (not a computational error, a framing one).** The state in which every expectation value is taken is the Kruskal vacuum |0⟩_K (lines 612–614, 618, 815). The "initial condition generated near the past singularity" (lines 315, 349–351) is instead used to define the *operator basis* b (which mode counts as a particle), not the state. In |0⟩_WH itself — the state the singularity-observer would prepare — the far observer, who by (65) shares that vacuum (line 609), sees nothing. So "Hawking radiation from quantum white-hole perturbations" is: *assume the Unruh/Kruskal state on the past horizon; then Killing-frequency observers count a thermal spectrum* — the textbook eternal-Schwarzschild result, here re-derived from inside the WH. The novel Section 5 quantity is the number of C-rotated (α-vacuum-like) quanta in |0⟩_K; a far detector using the ordinary Boulware/Killing modes (C₁ = 0) would still register Planck. The "non-vacuum initial condition… interpreted as an initial state which contains particles" (line 848) is not the state used anywhere in the calculation.

## 2. The result — what departs from thermal, and what fixes it

Vacuum case: n(ω̃) = 1/(e^{2πω̃/κ} − 1), T_H = κ/2π = 1/8πGM (68)–(69), lines 635–641; identical to the ordinary BH Hawking temperature, as measured at ℐ⁺ from right-movers that crossed the past horizon (lines 645–646). Left-ℐ⁻ modes give the same (84), line 749.

Non-vacuum case (92), line 828: n(ω̃) + |C₁(ω̃)|² coth(πω̃/κ).

- **Sign:** fixed — an *excess* over Planck for every ω̃ (|C₁|² ≥ 0, coth > 0). Equivalent form: |C₁|²(1 + 2n), i.e. stimulated-plus-spontaneous counting of the rotated mode.
- **Magnitude:** not fixed by geometry. C₁(ω̃) is an arbitrary function (line 774: "the coefficients Cᵢ depend on ω"), constrained only by |C₂|² − |C₁|² = const (38). The high-frequency limit of the excess is |C₁(ω̃)|² itself; the low-frequency limit is |C₁|² κ/πω̃ (divergent). The statement "The deviation from a Planck distribution is significant" (line 830) has no support — it is as large or as small as C₁ is chosen.
- **Dependence on other choices:** test-field mass — massless assumed throughout (line 249); spin s enters only the Hankel order and the phase π(1+s)/4 in (40), and drops out of T_H; mode range — ℓ = 0 and ω ≫ κ only (items (a)–(c) above); vacuum state — this is the whole content of the departure, and it is also entangled with the un-quantified intermediate-region scattering (item (b)): the paper cannot separate "the singularity vacuum" from "an effective C₁ generated by the potential".

So: the thermal part is geometry-fixed and standard; the departure's sign is fixed and its magnitude is a free function of frequency chosen by hand.

## 3. Our universe — every sentence bearing on it

Verbatim, with receipts:

- L19 (abstract): "The spacetime inside the white hole is **like** an anisotropic cosmological background with the past singularity **playing the role of** a big bang singularity." "We consider an eternal Schwarzschild manifold…"
- L26: "This phenomena suggests that the interior of a BH is **like** a cosmological background bounded by the event horizon."
- L26–28: "There have been works in the past to treat the interior of a BH as a cosmological background. For example the idea that the interior of BH may be replaced by a non-singular dS space-time was studied in [4–12]" — the BHU/dS-interior family (Sakharov, Poisson–Israel, Frolov–Markov–Mukhanov, Firouzjahi 2016 [8], Brandenberger et al., Gaztañaga [11],[12]; lines 929–981) is cited as *prior context*, not adopted.
- L33: "the white hole (WH) background is **more akin to** a cosmological spacetime in which the global structure of spacetime suggests that the past singularity r=0 **behaves as** the onset of big bang singularity".
- L35: "it is believed that all structures in observable Universe are generated from tiny quantum fluctuations generated during primordial inflation. It is therefore a natural question to study perturbations inside the WH **as a particular cosmological background**."
- **L40–42 (disclaimer 1):** "It is believed that the WHs are not stable and have disappeared in early universe [22] so **the current analysis may not be directly relevant to observable Universe**. However, we treat WH as part of an eternal BH manifold which exists along with BH as required by the time reversal symmetry of general relativity. We find interesting properties of WH cosmology as an anisotropic cosmological background while studying quantum field theory in WH background can provide **a non-trivial example of quantum field theory in curved backgrounds**."
- **L97 (disclaimer 2):** "the singularity of the WH is in the past, i.e. it represents a big bang singularity. As mentioned before, **the WH is unstable and may not exist in current observable Universe**. However, in our treatment we consider an eternal BH in which a WH is an integral part of the full manifold."
- L140–141: "At the **“big bang”** singularity" — scare quotes in the original; "the space along the x direction starts off very large and contracts as time pass by".
- L179: "Choosing the onset of big bang singularity to be at t̂ = 0".
- L287: "may be interpreted as the extension of the Sasaki-Mukhanov equation to an anisotropic cosmological background such as the Bianchi I universe."
- L315: "quantum fluctuations generated at the point of past singularity r=0 (i.e. Big Bang) inside the WH".
- L329: "This is the hallmark of a contracting universe".
- L350: "This interpretation is **quite similar to** the case of FLRW cosmology, in which the observed large scale perturbations are generated from quantum fluctuations in early universe".
- **L657 (the decisive one):** "The region enclosed by the left ℐ⁻ and the part of future horizon with V=0, U>0 (which is usually referred to as part of the 'other universe') is similar to the exterior of BH **in our part of the universe**." — "our part of the universe" is the black-hole **exterior**, where the ℐ⁺ observer who measures the flux lives (lines 37, 420, 633).
- L834 (summary): "The past singularity inside the WH is **like** a big bang singularity such that the WH background represents an anisotropic cosmological setup."

Is "plays the role of a big bang" more than an analogy? No. Every occurrence is hedged ("like", "akin to", "behaves as", "playing the role of", "may be interpreted", "quite similar to", scare-quoted "big bang"), the authors twice say the object may not exist in the observable Universe, and the only place they locate "our" universe is outside the horizon. The paper's interior is moreover the honest classical Schwarzschild interior — a Kasner/Kantowski–Sachs anisotropic patch with one *contracting* direction of infinite extent (lines 141, 218–220, 329) — not an FLRW big bang; a BHU model wanting an isotropic expanding interior has to *replace* this geometry, which is precisely what the cited family [4–12] does and this paper does not.

## 4. Base-layer membership (reported, not decided)

The corpus rule: "papers that make or test the identification 'our universe is the inside of a black hole'."

**This paper does neither.** In its own words: it studies "quantum field theory in WH background" as "a non-trivial example of quantum field theory in curved backgrounds" (line 42); its subject is "an eternal Schwarzschild manifold" (line 19) in which "the WH exists along with BH as required by the time reversal symmetry" (line 98); the measured quantity is "the spectrum of Hawking radiation as measured by this observer" "far outside the BH" (lines 37–38); and "our part of the universe" is the BH exterior (line 657). Its bearing on the identification is limited to (i) the cosmological *reading* of the Schwarzschild interior (KS form, Kasner exponents, two Hubble rates, "superhorizon" modes) and (ii) a citation of the dS-interior/BHU family as prior context (lines 26–28).

Classification, with the paper's words: **a white-hole QFT paper adjacent to the family** ("may not be directly relevant to observable Universe", line 41), not a universe-origin claimant. If the base layer is strictly "make or test", it does not qualify; it is a natural *support/method* reference (the classical anisotropic-interior baseline that any BHU model must either accept or replace). Membership is Duho's call; this seat reports that the 08-23 flag ("family-adjacent, not a universe-origin claim") is confirmed at full text.

## 5. Tier consequence, argued

- **CALIBRATED-FALSIFIER — no.** The only universe-facing prediction would be Hawking flux from a white-hole horizon at T_H = 1/8πGM (69) with an excess |C₁|² coth(πω̃/κ) (92). T_H is the standard value (nothing white-hole-specific to calibrate against), and the excess amplitude is an unconstrained function (section 2). Nothing is calibrated.
- **PROSPECT — no.** No observation, instrument, or test is proposed; the outlook items are the information-loss problem (lines 830, 850) and including greybody scattering (line 852).
- **QUALITATIVE-DIRECTIONAL — no.** The one fixed-sign statement (excess over Planck) concerns a WH horizon's Hawking flux, depends on a free C₁ ≠ 0, is detector-basis-dependent (section 1, adversarial point), and is made about an object the authors say "may not exist in current observable Universe" (line 97). It gives no direction for any observable of *our* universe (no curvature sign, no anisotropy amplitude, no spectrum tilt, no parity).
- **Falsifiability leg.** A null cannot contradict it: non-detection is already explained by the authors (WHs "have disappeared in early universe [22]", line 40). Even a *positive* detection of a non-thermal WH flux could not be checked against the paper, since |C₁(ω̃)|² is free; and a perfectly thermal flux is the C₁ = 0 case. There is no observation on either side that the paper forbids.
- **CONSISTENCY-ONLY — holds, as the ceiling**, conditional on membership. The paper is internally consistent (standard Bogoliubov machinery, an appendix cross-check, correct Kasner/KS bookkeeping, one normalisation-convention slip at (38) vs (92)/line 758, and approximations (a)–(e) asserted at high frequency). It shows that the classical BH/WH interior *can be written* as an anisotropic cosmology and that QFT on it reproduces the ordinary Hawking temperature — consistent with, and mildly cautionary for, the BHU family (the honest interior is Kasner, not FLRW).

Token therefore: **AUDIT_FLAG_MEMBERSHIP** — the tier holds if the entry stays, but the entry may not belong in the base layer. No tier changed; this is a packet for Duho.

---

## Plain language

This paper asks what happens if you treat the inside of a white hole — the time-reverse of a black hole, which the authors themselves say probably does not exist in today's universe — as a tiny anisotropic universe, let quantum ripples start at its "big bang" singularity, and ask what someone standing far outside the black hole would see. The answer, worked out carefully and correctly with the standard Hawking-radiation toolkit, is: ordinary Hawking radiation at the ordinary temperature, plus an extra non-thermal piece whose size is whatever you choose for a free function the calculation never pins down. The derivation is sound at high frequencies with the usual simplifications assumed rather than proven, and the one honest subtlety is that the "extra piece" comes from redefining what counts as a particle, not from a different physical state. Nothing here is a claim that our universe sits inside a black hole; the paper puts "our part of the universe" outside the horizon and says so twice that the whole thing may not be relevant to what we can observe. It is a good quantum-field-theory-in-curved-space exercise that shares a family resemblance with the black-hole-universe idea and cites that family as background. Nothing we could measure would contradict it. If it stays in the corpus, CONSISTENCY-ONLY is right; the real question, which is Duho's, is whether a paper that neither makes nor tests the identification should be in the base layer at all rather than filed as a supporting reference.
