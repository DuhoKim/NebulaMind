# WIKI-EXPANSION — Area 3: Gas Depletion & Star-Formation Efficiency (Deep Research brief, Tori / DR on Pro)

**Purpose (same pipeline as Areas 1-2):** rebuild NebulaMind's galaxy-evolution wiki as a broad, well-cited, trust-scored evidence map. THIRD live area. Your DR output becomes real wiki claims + verified evidence (ADS-verify + Groq-jury pipeline confirmed working). Rigor + verifiable citations are everything.

**Topic:** **gas depletion and star-formation efficiency** in galaxy evolution — BROAD, NOT AGN-framed, and distinct from Areas 1-2 (which cover the mass-metallicity scaling relation and metal-enrichment history). Cover:
- cold gas content (HI atomic, H2 molecular) and gas fractions vs stellar mass and vs redshift;
- molecular-gas depletion time (t_dep = M_H2 / SFR): typical values, and dependence on mass, redshift, and environment;
- star-formation efficiency (SFE) and the Kennicutt-Schmidt star-formation law (Sigma_SFR vs Sigma_gas; molecular vs total gas);
- the role of gas supply vs gas exhaustion vs efficiency drop in QUENCHING (gas-regulator / equilibrium models; "starvation"/strangulation vs rapid removal);
- how gas fraction and depletion time relate to position on the star-forming main sequence;
- cosmic evolution of the molecular-gas density (rho_H2) and gas fractions with redshift (e.g. ASPECS/PHIBSS-type results).

## What to return (per the Gemini-web DR SIDECAR protocol — advisory source-discovery; every source verified before use)
1. **Established findings** — settled results, each with >=1 REAL verified citation (DOI / arXiv / ADS bibcode that resolves to matching authors/title/year). Mark `established`.
2. **Open debates / tensions** — genuine disagreements (e.g. quenching by gas-exhaustion vs efficiency-suppression vs removal; whether t_dep is roughly constant or varies with environment/redshift; molecular vs total-gas SF law slope). Each with competing sources; mark `debate` + name the `debate_topic`.
3. **Key measurements & numbers** — with survey/instrument (ALMA, IRAM, xCOLD GASS, ASPECS, PHIBSS, etc.) + citation.
4. **What remains unknown** — genuine gaps (future-data motivation).
5. **DO_NOT_USE_UNVERIFIED list** — anything unresolved; keep out of claims.
Format each source: `Authors (year, journal) | DOI/arXiv/ADS | role=established|debate|caveat|future | one-line claim-boundary`.

## Hard rules
- Real astronomy literature only. No invented data, citations, identifiers, or findings. A citation is usable ONLY if its identifier resolves to matching authors/title/year — else `UNCITED_NOT_USABLE`.
- Prefer 2020-2025 where it adds value; keep foundational sources (Kennicutt, Bigiel, Leroy, Tacconi, Genzel, Saintonge, etc.) where strongest.
- Advisory only — you produce the packet; Hwao wires verified findings into the live wiki.

## ACCOUNT-SAFETY (gentle DR pace — one shared account; you just completed Area-2, so SPACE this one)
- You just finished Area-2. Give a human-like gap before submitting Area-3 (do not fire back-to-back). A few DR runs per session, spaced.
- Poll each Deep Research to completion. Back off on the FIRST unaccepted/soft-throttled submit. STOP + hold for Duho on any `google.com/sorry`; never interact with a challenge.
- DR runs on the Pro via the signed-in DR Chrome (CDP 127.0.0.1:19223). Flow runs on the Studio (Yui) — different IP, so parallel is fine; stay gentle.

## Output
Save the verified packet to `.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area3_gas_depletion_DR_PACKET.md` and ping Hwao when done.
