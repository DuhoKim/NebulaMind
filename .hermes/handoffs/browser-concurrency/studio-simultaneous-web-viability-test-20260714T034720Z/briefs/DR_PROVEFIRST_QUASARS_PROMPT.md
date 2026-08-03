# DR PROVE-FIRST — Quasars-as-galaxy-evolution-driver debate

Prove-first Deep Research run to feed the NebulaMind wiki pipeline (Seam A). Target: Quasars page
(slug `quasars`, page_id 32, section "Open Debates"), debate_topic "Are Quasars the Primary
Drivers of Galaxy Evolution?", existing debate claims pro=1249 / con=1250 (both currently cite the
same papers all as "supports" — the exact problem this fixes).

## Task for Tori + Goru (ONE bounded DR run)
1. Submit the DR PROMPT below VERBATIM to Deep Research on the signed-in Pro Chrome (via the CDP
   forward), page-scoped preflight first.
2. POLL to a terminal state (research complete, result text stable) before judging.
3. SAVE the full sourced report to a receipt and VERIFY it saved.
4. THEN delete ONLY that run's own Gemini conversation (history hygiene), log the deletion.
5. Report to Hwao. Rails unchanged: real page challenge = STOP+freeze; serialized submit; no
   secrets; fail closed on target drift.

## DR PROMPT (submit verbatim)
Topic: Are quasars (luminous AGN) the primary drivers of galaxy evolution, or a secondary regulator relative to mergers and gas accretion?

Produce a rigorous, fully sourced literature review of the debate over the role of quasar / luminous-AGN feedback in galaxy evolution: whether energetic AGN feedback is the primary mechanism regulating star formation and galaxy growth (quenching, outflows, the M-sigma relation), versus the view that mergers, cold-gas accretion, and secular processes dominate while quasars play a secondary role.

Requirements:
1. Every factual assertion must be backed by a REAL, verifiable reference — give the arXiv ID (e.g. 2303.15506), DOI, and/or publisher URL, plus paper title, first author, and publication year. Do NOT invent, guess, or approximate identifiers; omit an identifier you cannot verify rather than fabricate it. Prefer peer-reviewed papers and prioritize 2023-2025 work (JWST, ALMA, MUSE, eROSITA, X-shooter era), while including foundational earlier references where needed for context.
2. Cover: (a) the current mainstream understanding and points of genuine consensus; (b) the contested findings, explicitly separating evidence/arguments that support "quasars are the primary driver" from those that challenge it (i.e., support the "mergers/accretion dominate, quasars secondary" position); (c) key open questions and what upcoming data could resolve them.
3. Address concrete sub-threads: observed AGN-driven outflows and their coupling efficiency; positive vs. negative feedback; correlation vs. causation in the M-sigma / M_BH-M_bulge relations; whether AGN feedback actually quenches star formation in situ; the role of major/minor mergers as triggers; cold accretion and secular gas supply; and cosmological-simulation evidence (e.g., IllustrisTNG, EAGLE, SIMBA) on feedback necessity.

Output structure (critical — the report will be machine-parsed): Organize the findings as a set of discrete claim units. For each distinct scientific claim, output a block with these fields:
- claim_text: one clear declarative sentence.
- claim_type: established (broad consensus) or debate (genuinely contested).
- debate_topic: for debate claims, a short shared label; for this review use "Are Quasars the Primary Drivers of Galaxy Evolution?" where applicable, or a precise sub-topic label.
- papers: a list of the supporting/relevant references, each as { arxiv_id | doi | url, title, year, stance } where stance is supports if the paper's findings back the claim_text, or refutes if they contradict it.

For contested points, provide both a pro claim and a con claim as separate units (mirroring a two-sided debate), each with its own correctly stance-labeled papers list. Ensure supporting and challenging literature are attributed to the correct side — do not attach the same paper as supports to opposing claims unless it genuinely supports both. Include a final plain-text bibliography of every reference cited with its verifiable identifier.
