# Platoon Roster v3

Date: 2026-06-11 KST
Source: `docs/platoon_overhaul_v2.md` section 4 and section 6.

## Canonical Nicknames

| Nickname | Model | Machine | Role |
|---|---|---|---|
| Rakon | deepseek-r1:671b | Mac Pro | On-demand deep synthesis |
| Buddle | gpt-oss:120b | Mac Studio | Heavy general reasoning / synthesis backup |
| Vera | astrosage-70b | Mac Studio | Astronomy drafting and synthesis |
| Blanc | llama3.3:70b | Mac Studio | Non-astronomy prose |
| Mima | qwen3.6:35b-a3b | Mac Studio | Jury juror #1 / general scoring |
| Tera | qwen3.6:27b | Mac Studio | General mid + vision |
| Nutty | gpt-oss:20b | Mac Studio | Jury juror #2 / fast reasoning + JSON |
| Pico | vanta-research/atom-astronomy-7b | Mac Studio | Jury juror #3 / astro fast screen |
| Embeddings | qwen3-embedding:4b | Mac Studio | Primary embeddings |
| Legacy embeddings | nomic-embed-text:v1.5 | Mac Pro tunnel | Legacy vectors |
| Gemini Flash | gemini-2.5-flash | API | Jury juror #4 / batch default |
| Sonnet / Opus | Anthropic API | API | Judge ticks, rewrite, coherence |

## Job Assignments

| Job | Owner |
|---|---|
| Stance jury | Mima + Nutty + Pico local, Gemini Flash cloud |
| arXiv fast screen KEEP/DISCARD | Pico |
| Evidence stance pre-judge | Nutty |
| Adversarial query generation | Tera |
| Adversarial skeptic | Nutty |
| Autowiki section proposer | Vera |
| Autowiki section rewrite final | Sonnet |
| Coherence rewrite | Sonnet |
| Deep synthesis / multi-doc analysis | Rakon for batched depth, Buddle for interactive turnaround |
| Non-astro long-form | Blanc, pilot against Buddle |
| Embeddings | qwen3-embedding:4b primary, nomic for legacy vectors |
| High-volume batch default | Gemini Flash |
| Judge ticks | Sonnet / Opus |

## Co-Residency

Pin Pico + Mima + Nutty as the local jury set. Vera, Blanc, and Buddle load on demand. Rakon remains exclusive to the Mac Pro.
