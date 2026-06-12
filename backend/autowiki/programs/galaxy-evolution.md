# AutoWiki Program — galaxy-evolution

## Reader persona (what we are optimizing for — Papa's directive)
A professional astronomer (postdoc-level or above) opens this page. We want them to:
  1. Walk away knowing what has been established in the field, with the right citations to follow up.
  2. Walk away with concrete ideas for what to research next — specific open questions, contested findings, frontier directions.
The Rakon judge will score the page on exactly this rubric. Every proposal should be evaluated by the drafter against this lens before submission.

## Goal
Push composite quality from t=0 to ≥0.78 (~ structural ≥90 AND utility ≥7.5/10) while preserving the "research review article" voice (no roadmap cards, no compass widgets).

## Priorities (what to try first, in order)
1. Surface debated/contested findings as first-class `claim_type='debate'` claims — these directly drive utility points on the "what to research next" axis of the rubric.
   - Priority debates: SMBH-host coevolution causality at high-z, AGN vs environmental quenching, MZR non-universality at low metallicity
2. Cover missing subtopics: dark_matter_halo, scaling_relations, color_bimodality, size_growth
3. Inject 2024-2025 evidence (JWST CEERS/COSMOS-Web, DESI Y3, Euclid Q1, IllustrisTNG/FIRE-3 papers)
4. Hero-fact upgrade: replace generic "stars in Milky Way ~100B" type facts with debate-tagged or range-typed astronomy facts with specific numbers

## Hard rules
- Every new claim needs ≥1 evidence row at quality≥0.40 in the SAME experiment, or the experiment is rejected before the judge ever sees it.
- Never lower any structural component by more than 0.05.
- Open questions live as `claim_type='debate'` claims, NOT as prose paragraphs in other sections.

## Banned moves (these will be penalized by the judge)
- Adding marketing/roadmap language ("we will explore...", "future work here will...") — judge rubric §11 deducts under "noise penalty."
- Inserting did_you_know cards into the article body.
- Vague claims without specific findings, numbers, or paper references.
- Rewriting sections that scored full marks on depth in the last 7 days.
- Generating paper citations the loop didn't actually retrieve (the evidence verifier will catch these, but the judge punishes them too).

## Rakon Deep Pass Targets (priority order)
1. SMBH-host coevolution at high redshift (z>2)
2. AGN feedback vs environmental quenching — which dominates?
3. Size growth mechanisms (inside-out vs mergers)
4. Color bimodality origin — quenching or initial conditions?

## Model assignments
AstroSage-70B (drafting), Atom-7B (alignment gate ≥0.55), Rakon deepseek-r1:671b (deep synthesis + judge)
