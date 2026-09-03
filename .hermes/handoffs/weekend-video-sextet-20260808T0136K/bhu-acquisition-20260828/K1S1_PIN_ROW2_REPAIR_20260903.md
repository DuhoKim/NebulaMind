# K1 stage-1 pin sheet — row 2 repair (Tori, 2026-09-03 16:55 KST), answering `K1S1_PIN_GATE_codex.md` PIN_GATE=FAIL

**Row 2 (the scaling of σ(M) with the primordial amplitude), now with quoted receipts:**
- Zentner 2007, arXiv:astro-ph/0611454, pinned `../bhu-reading-20260823/sources/astro-ph_0611454_clean.txt`
  (sha256 c14f95336af9ad14…): L194 "Δ²(k) ≡ k³P(k)/2π²" (Eq. 5); L277–278 "σ²(R) = ⟨δ²(x;R)⟩ = ∫ d ln k Δ²(k)|W(k;R)|²" (Eq. 14).
  So σ²(M) is LINEAR in P(k) at fixed window and fixed spectral shape.
- Planck 2018, `1807.06209_clean.txt` L3047–L3050: 𝒫_ℛ(k) = A_s (k/k₀)^{n(k)}; L1780: power ∝ A_s (as the first gate accepted).
- Therefore, at fixed transfer function and shape, σ²(M) ∝ A_s and σ(M) ∝ A_s^{1/2}; the exponent 1/2 is the square root of a
  receipted linear relation, not a quoted numeral. No other row changes. The master sheet in `K1S1_PIN_GATE_codex.md`
  stands for rows 1 and 3–7 (with the Fryer line numbers as repaired there; `1110.1726_clean.txt` sha256 8f49418708594992…
  is now the frozen extraction).

**Clerical amendment (Tori, 17:03 KST, answering the Kimi pin audit `K1S1_PIN_AUDIT_kimi.md`):** full hashes —
`astro-ph_0611454_clean.txt` sha256 c14f95336af9ad140997abb925002c66a2cdcbff71bc993553def72e26b922c3; `1110.1726_clean.txt` (frozen extraction) sha256 8f49418708594992cc8f9da284fb8f5fb5b2ce074c3b1932fa8b1fa58b1340f2. Row 6 units: the
Sicilia 2022 mass-function fits log N are per Mpc³ per dex of black-hole mass; the relic density is in M☉ Mpc⁻³. Kimi's
issue 2 (the row-2 receipt is a derivation) restates the first gate's objection; the codex re-gate (`K1S1_PIN_GATE2_codex.md`,
PIN_GATE=PASS) accepted the quoted-linearity receipts; the dissent is recorded here, not adjudicated by Tori. Issue 3
(metallicity corners without pinned values) is answered below once the Fryer text is checked.
**Issue 3 answered — row 4 metallicity corners pinned:** Fryer et al. 2012 evaluate their prescriptions "at solar and zero
metallicity" (`1110.1726_clean.txt` L436–437) and state solar as Z = 0.02 (L1786); the remnant fits are "fairly insensitive
to the metallicity" (L638). Nuisance range for phase 2: Z ∈ [0, Z☉] with Z☉ = 0.02; a seat sampling 0.01 Z☉ and 1.00 Z☉ as
corners is inside this range.
