# WIKI-EXPANSION — Area 1: Stellar Mass–Metallicity Relation (Deep Research brief, Tori / DR on Pro)

**Purpose (NEW pipeline):** we are rebuilding NebulaMind's galaxy-evolution wiki as a broad, well-cited, trust-scored evidence map — the instrument that later surfaces *optimum* research topics. This is the FIRST live area. Your DR output becomes real **wiki claims + verified evidence** written LIVE to the encyclopedia (Duho authorized live-direct writes). So rigor and verifiable citations are everything.

**Topic:** the **stellar mass–metallicity relation (MZR)** in galaxy evolution — BROAD, NOT AGN-framed. Cover gas-phase and stellar MZR, its shape/turnover, redshift evolution, the mass–metallicity–SFR "fundamental metallicity relation" (FMR), environmental and morphological dependencies, and the physical drivers (outflows, inflows, gas fraction, star-formation efficiency). Deliberately steer away from the AGN/feedback/BPT framing that over-dominates the current wiki.

## What to return (per the Gemini-web DR SIDECAR protocol — advisory source-discovery; every source verified before use)
Produce a structured packet with, for the MZR:
1. **Established findings** — the settled, textbook-level results, each with ≥1 REAL verified citation (DOI / arXiv / ADS bibcode that resolves to matching authors/title/year). Mark these `established`.
2. **Open debates / tensions** — where the literature genuinely disagrees (e.g. MZR normalization/slope across surveys, strength/existence of FMR redshift evolution, calibration-dependence of abundances). Each with the competing sources. Mark these `debate` and name the `debate_topic`.
3. **Key measurements & numbers** — with the survey/instrument and the citation, so claims can be grounded (not recomputed).
4. **What remains unknown** — genuine gaps (future-data motivation).
5. **DO_NOT_USE_UNVERIFIED list** — anything you couldn't resolve; do not let it into claims.

Format each source as: `Authors (year, journal) | DOI/arXiv/ADS | role=established|debate|caveat|future | one-line claim-boundary`.

## Hard rules
- Real astronomy literature only. No invented data, citations, identifiers, or findings. A citation is usable ONLY if its identifier resolves to matching authors/title/year — otherwise `UNCITED_NOT_USABLE`.
- Prefer 2020–2025 where it adds value; keep foundational older sources (Tremonti 2004, Mannucci 2010 FMR, etc.) where they're the strongest fit.
- Advisory only — you produce the researched packet; you do NOT edit the DB/wiki yourself (Hwao wires the verified packet into the live write path).

## ACCOUNT-SAFETY (gentle DR pace — the account is shared/one-account)
- A few DR runs, spaced ~human, not back-to-back. Poll each Deep Research to completion (async).
- Back off on the FIRST unaccepted/soft-throttled submit. STOP + hold for Duho on any `google.com/sorry`; never interact with a challenge.

## Output
Save the verified packet to `.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area1_mass_metallicity_DR_PACKET.md` and ping Hwao when done. Hwao then converts verified findings → live wiki claims+evidence and confirms topic-discovery re-fires, before we scale to Area 2 (chemical evolution) and Area 3 (gas depletion).
