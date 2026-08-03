# Gemini-web Deep Research prompt

Marker to require in Gemini output: `GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE`

## Task
You are assisting a supervised NebulaMind research-topic quality pass.
Topic: The impact of active galactic nuclei on the interstellar medium of their host galaxies

Please provide a comprehensive, systematic deep research literature review of the last 10 years of observational and theoretical data regarding this topic. 

## Required output format
1. `Topic Overview`
2. `Prior studies/reviews to verify locally` (bullet list of 10-15 high leverage papers with DOI/arXiv links)
3. `What the literature appears to establish`
4. `What remains unknown or heavily debated`
5. `Data/survey plan or Observational Constraints`
6. `Overclaim risks and wording guardrails`

Finish with the exact standalone marker:
`GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE`
