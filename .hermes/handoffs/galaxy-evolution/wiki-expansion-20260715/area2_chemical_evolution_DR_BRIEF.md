# WIKI-EXPANSION — Area 2: Galaxy Chemical Evolution (Deep Research brief, Tori / DR on Pro)

**Purpose (same pipeline as Area 1 MZR):** we are rebuilding NebulaMind's galaxy-evolution wiki as a broad, well-cited, trust-scored evidence map — the instrument that later surfaces optimum research topics. This is the SECOND live area. Your DR output becomes real **wiki claims + verified evidence** written live (the ADS-verify + Groq-jury pipeline is now confirmed working — real trust lands). Rigor + verifiable citations are everything.

**Topic:** galaxy **chemical evolution** — BROAD, NOT AGN-framed, and distinct from Area 1's mass–metallicity *scaling relation*. Cover the *process/history* of metal enrichment:
- chemical enrichment history over cosmic time; metallicity evolution with redshift;
- nucleosynthetic sources and their timescales (core-collapse SNe vs Type Ia vs AGB stars) and how they shape abundance ratios;
- key abundance-ratio diagnostics: [alpha/Fe] vs [Fe/H], [N/O], [C/O], and what they trace (star-formation timescale, IMF, delayed enrichment);
- radial metallicity gradients in disks and their evolution;
- chemical evolution models: closed-box, leaky-box, inflow/outflow (accretion of pristine gas, galactic winds), and the classic **G-dwarf problem**;
- the fundamental metallicity relation (note overlap with Area 1; keep the enrichment-process framing here).

## What to return (per the Gemini-web DR SIDECAR protocol — advisory source-discovery; every source verified before use)
1. **Established findings** — settled, textbook-level results, each with >=1 REAL verified citation (DOI / arXiv / ADS bibcode that resolves to matching authors/title/year). Mark `established`.
2. **Open debates / tensions** — genuine disagreements (e.g. IMF-dependence of yields, inflow vs outflow dominance, gradient-evolution direction, alpha-enhancement interpretation). Each with competing sources; mark `debate` + name the `debate_topic`.
3. **Key measurements & numbers** — with survey/instrument + citation.
4. **What remains unknown** — genuine gaps (future-data motivation).
5. **DO_NOT_USE_UNVERIFIED list** — anything unresolved; keep out of claims.
Format each source: `Authors (year, journal) | DOI/arXiv/ADS | role=established|debate|caveat|future | one-line claim-boundary`.

## Hard rules
- Real astronomy literature only. No invented data, citations, identifiers, or findings. A citation is usable ONLY if its identifier resolves to matching authors/title/year — else `UNCITED_NOT_USABLE`.
- Prefer 2020-2025 where it adds value; keep foundational sources (Tinsley, Matteucci, Pagel, etc.) where strongest.
- Advisory only — you produce the packet; Hwao wires verified findings into the live wiki.

## ACCOUNT-SAFETY (gentle DR pace — shared one-account, and Flow is running in parallel on the Studio)
- A few DR runs, spaced ~human, not back-to-back. Poll each Deep Research to completion (async).
- Back off on the FIRST unaccepted/soft-throttled submit. STOP + hold for Duho on any `google.com/sorry`; never interact with a challenge.
- DR runs on the Pro via the existing signed-in DR Chrome (CDP at 127.0.0.1:19223). Flow runs on the Studio (Yui) — different machine/IP, so parallel is fine, but stay gentle.

## Output
Save the verified packet to `.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area2_chemical_evolution_DR_PACKET.md` and ping Hwao when done. Hwao then converts verified findings -> live wiki claims+evidence (ADS-verify + jury), same as Area 1.
