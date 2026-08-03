# Deep Research Request: Method 1 RT Unresolved arXiv & Unbound Claims

**Request ID:** REQ_M1_RT_UNRESOLVED_ARXIV_20260707T144039Z
**Marker:** GORU_RUTHLESS_USAGE_SURGE_20260707T144039Z

**Method:** Method 1 (packet-gated-paper-to-wiki-reconciliation)

**Current RT artifact paths:**
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/autopilot/RESEARCH_TOPICS_GORU_M1_SEED_20260708T090359Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`

**Exact topic/cards to improve:**
1. **AGN Feedback as a Fast Quenching Channel (Claim 2929)** - 6 of the 8 distinct papers are unresolved arXiv IDs. We need their actual titles, main findings, and relevance to massive-galaxy AGN quenching.
2. **Halo Assembly History (Claims 2912, 2918, 2905)** - Completely unbound in the local M1 ledger. We need canonical review papers on assembly bias and low-mass stellar feedback.
3. **Ionizing Sources for Reionization (Claims 2925, 2926)** - Unbound. Need recent high-z Lyman-continuum escape fraction literature comparing faint galaxies vs proto-globular clusters.

**Existing source-basis links/claim IDs that must not be contradicted:**
- Claim 2929 (Internal AGN feedback can regulate or quench... but positive feedback can occur)
- Claim 2946 (Sustained AGN heating of hot gas reservoirs is reported as a maintenance mechanism)
- The 27 unbound claims must remain marked as needing evidence, but the Deep Research output can provide the missing sources for Hwao to verify.

**The question Gemini should answer:**
- What are the resolved titles and abstracts for the unresolved arXiv IDs currently supporting Claim 2929, and do they actually address massive-galaxy AGN quenching or are they unrelated (e.g. Milky Way superbubbles)?
- What are the 3 most highly-cited review papers or recent definitive studies for "dark matter halo assembly bias" and "globular clusters vs faint galaxies during reionization"?

**Expected output shape:**
A markdown report containing:
- Resolved bibliographic data (Title, Authors, Year, Abstract summary) for the requested arXiv IDs.
- A shortlist of recommended papers (with real DOIs/arXiv links) for the unbound topics, structured with: prior-study findings, what remains unknown, overclaim risks, and explicit decision criteria.
- A `DO_NOT_USE_UNVERIFIED` list for any spurious matches.

**Explicit safety locks (from protocol):**
- Verify every cited paper/source link before use.
- Do not import numeric results unless the source supports them.
- Do not use Gemini-generated DOI/ADS/arXiv IDs until checked.
- Output is advisory only; it is not accepted evidence, not product claim binding, and not permission to publish or mutate NebulaMind data.
