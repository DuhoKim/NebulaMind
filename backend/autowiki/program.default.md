# AutoWiki Default Program

## Reader persona
A professional astronomer (postdoc-level or above). They want:
  1. Clear, accurate, well-evidenced findings with the right citations.
  2. Specific open questions, active debates, and frontier directions.

## Goal
Improve composite quality (structural + astronomer utility) through small, targeted edits.
Commits only when Δq ≥ 0.02.

## Priorities
1. Surface actively debated findings as `claim_type='debate'` claims
2. Cover any missing required subtopics
3. Add 2023-2025 evidence to claims with thin or stale support
4. Upgrade hero facts with specific quantitative findings

## Hard rules
- Every new claim needs ≥1 evidence row (arxiv, quality ≥ 0.40) in the same experiment
- No structural component may drop by more than 0.05
- Debate claims go as structured claims, not prose paragraphs

## Banned moves (judge penalizes these)
- Roadmap/marketing language ("future work will...", "this page covers...")
- Vague claims without specific numbers or paper references
- Hallucinated citations

## Model assignments
AstroSage-70B (drafting), Atom-7B (alignment gate ≥0.55), Rakon deepseek-r1:671b (judge)
