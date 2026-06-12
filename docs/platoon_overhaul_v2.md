# Platoon Overhaul v2 — Local LLM Roster Decision Doc

**Date:** 2026-06-11 (KST)
**Author:** Kun (claude-fable-5)
**For:** Papa, via HwaO. Tori executes approved pulls/retires.
**Method:** Live `/api/tags` + `/api/ps` probes on both Ollama hosts; backend config read (`config.py`, `routing.py`, `agent_loop/tasks.py`); Ollama library pages fetched 2026-06-11 for candidate sizes (external info marked ⚠ where unverified). Builds on `Audit_ModelPlatoonSelection_2026_v1.md` (2026-06-03).

---

## 1. Actual installed inventory (probed 2026-06-11)

### Mac Studio (512GB, `localhost:11434`)

| Model | Disk | Params | Quant | Nickname (HwaO table) |
|---|---:|---|---|---|
| llama3.1:405b | 243.1 GB | 405.9B | Q4_K_M | "Buddle" (per dispatch table) |
| llama3.3:70b | 42.5 GB | 70.6B | Q4_K_M | Blanc |
| astrosage-70b | 42.5 GB | 70.6B | Q4_K_M | Vera |
| deepseek-r1:70b | 42.5 GB | 70.6B | Q4_K_M | Nutty-Heavy |
| deepseek-r1:32b | 19.9 GB | 32.8B | Q4_K_M | — (unassigned) |
| qwen3:30b | 18.6 GB | 30.5B | Q4_K_M | Mima |
| qwen3:30b-a3b-instruct-2507-q4_K_M | 18.6 GB | 30.5B MoE | Q4_K_M | — (unassigned; **doing jury duty**) |
| gemma3:27b | 17.4 GB | 27.4B | Q4_K_M | Tera |
| phi4:14b | 9.1 GB | 14.7B | Q4_K_M | Takji |
| deepseek-r1:14b | 9.0 GB | 14.8B | Q4_K_M | Nutty |
| llama3.1:8b | 4.9 GB | 8.0B | Q4_K_M | — (cloud-parity fallback) |
| vanta-research/atom-astronomy-7b | 4.5 GB | 7.3B | Q4_K_M | Pico |
| qwen3-embedding:4b / 0.6b, nomic-embed-text:v1.5 | 3.4 GB | — | — | — (embeddings, load-bearing) |

Total ≈ **415 GB** on disk.

### Mac Pro (`169.254.100.1:11435`)

| Model | Disk | Params | Nickname |
|---|---:|---|---|
| deepseek-r1:671b | 404.4 GB | 671B MoE | Rakon |
| deepseek-r1:32b | 19.9 GB | 32.8B | (roster v2 called THIS one "Buddle") |
| nomic-embed-text:v1.5 | 0.3 GB | — | — |

### Resident right now (`/api/ps`, Studio)

atom-7b (9.2GB) + **deepseek-r1:70b (45.8GB)** + **qwen3:30b dense (19.5GB)** — all correctly ctx-capped at 8192 (June-3 audit P0-1 fix landed ✓). Mac Pro: nothing loaded.

---

## 2. Gap analysis

**G1 — "Buddle" means three different models depending on the source.** Dispatch table: llama3.1:405b (Studio). `platoon-roster.md` v2: deepseek-r1:32b (Mac Pro). `routing.py` T3: qwen3:30b. `config.py` `BUDDLE_MODEL`: llama3.3:70b. Four sources, four answers. Any scheduler or human trusting a nickname is routing blind.

**G2 — The dispatch's jury table is stale.** It says jury = Mima + Nutty-Heavy + Pico. Code truth (`agent_loop/tasks.py` `STANCE_JURY_MODELS`): **gemini-2.5-flash + qwen3:30b-a3b-instruct-2507 + deepseek-r1:14b + atom-7b**. Nutty-Heavy (r1:70b) is in NO jury — yet it is sitting resident at 45.8GB.

**G3 — deepseek-r1 family is structurally wrong for jury duty.** Verified 2026-05-20 (TOOLS.md): all r1 sizes put reasoning in `<think>` and return **empty `content`** on synchronous `/v1/chat/completions` — they cannot emit the required `{"vote": …}` JSON reliably. The r1:14b juror seat is a silent-failure seat; "Nutty-Heavy as heavy juror" was never viable. Within the 90s/juror timeout, a 42.5GB thinking model is also a latency bust.

**G4 — 305GB of weights appeared with no documented purpose.** llama3.1:405b (243GB), deepseek-r1:70b, deepseek-r1:32b were all pulled onto the Studio after my 2026-06-03 audit (none were in that day's `/api/tags`). llama3.1:405b is a July-2024 dense model: at Q4 on M3 Ultra it is slow (dense 405B decode), eats half the disk budget, and is beaten on quality-per-GB by gpt-oss:120b (65GB) by every mid-2026 report. No backend code references it for any scheduled job (`inference_scheduler.py` only lists it as a known model).

**G5 — Resident set still drifts from workload.** The jury's fast model (qwen3-a3b-instruct) is NOT resident while qwen3:30b dense (no scheduled role) and r1:70b (no role at all) ARE. Every jury tick pays a ~20s cold load it shouldn't.

**G6 — Unassigned-but-load-bearing models have no nicknames/roster entries:** qwen3-a3b-instruct (jury primary!), llama3.1:8b, and all three embedding models.

---

## 3. Recommended changes

### Keep (no change)
- **astrosage-70b (Vera)** and **atom-7b (Pico)** — the astronomy domain edge; still no open-weight equal. Pico stays pinned resident.
- **deepseek-r1:671b (Rakon, Mac Pro)** — on-demand deep reasoning only. Note: DeepSeek-V4-Flash on Ollama is **cloud-only** (`:cloud` tag, no local weights) ⚠ — so there is currently no local successor to pull; the V4 path is provider/cloud if we want it. Keep Rakon until that changes.
- **llama3.3:70b (Blanc)** — non-astronomy prose. Re-evaluate after gpt-oss:120b arrives.
- **Embeddings** (qwen3-embedding:4b primary, nomic for legacy) — document them in the roster.

### Pull (new, all sizes verified on ollama.com 2026-06-11)
- **qwen3.6:35b-a3b** (24GB, 256K ctx, MoE A3B, vision+tools) — jury/scoring workhorse; successor to qwen3:30b-a3b-2507. ⚠ Validate JSON reliability + thinking-toggle behavior before promoting (same trap that bit qwen3:30b). **RESOLVED 2026-06-11 — see validation note below; requires top-level `"think": false` in `/api/chat`.**
- **gpt-oss:20b** (14GB, 128K ctx) — fast reasoning WITH clean structured output; replaces deepseek-r1:14b everywhere r1's empty-content defect bites (jury seat, stance pre-judge, skeptic).
- **gpt-oss:120b** (65GB, 128K ctx) — heavy general reasoner at 1/4 the footprint of llama3.1:405b; reported ≈o4-mini reasoning ⚠. Takes the "general heavy" role.
- **qwen3.6:27b** (17GB, 256K ctx, **vision**) — general mid-size; successor to gemma3:27b and qwen3:30b dense. Vision input is a new capability (plot/figure reading for arXiv triage).

### Validation note — qwen3.6:35b-a3b empty-content failure (2026-06-11, RESOLVED)

Tori's harness reported 0/20 non-empty content on qwen3.6:35b-a3b. Live-probed on Studio: **the model is fine; the harness flag was wrong.**

- **Root cause:** qwen3.6 is a hybrid-thinking model. Ollama defaults thinking ON; all tokens stream into `message.thinking`, exhausting `num_predict` before `content` receives anything (`done_reason: length`, `content: ""`). Same *symptom* as the r1 defect, different *mechanism* — and unlike r1, it is fixable.
- **Wrong fixes (both confirmed ineffective):** `"thinking": false` (not an Ollama API field — silently ignored) and `/no_think` prompt prefix (soft switch removed in Qwen3-2507+ generations).
- **Correct fix:** top-level `"think": false` in the `/api/chat` request body (`think=False` in ollama-python). Probe result: clean `{"stance":"KEEP"}` in `content`, 6 tokens, 0.36s.
- **Re-validation:** 5/5 jury-style calls with `think:false` + `format:"json"` → all parsed, correct stance, 0.95 confidence, 18–45s warm latency (within the 90s juror budget).
- **Endpoint switches (both verified 5/5 on jury-style prompts, 2026-06-11):**
  - Native `/api/chat`: top-level `"think": false` (+ `format:"json"`)
  - OpenAI-compat `/v1/chat/completions`: `"reasoning_effort": "none"` (+ `response_format:{"type":"json_object"}`). Note `"think": false` is IGNORED on this endpoint (confirmed: 2148 reasoning chars, empty content).
- **Do NOT use the prompt-hack path** ("Do not think step by step" / `/no_think` prefixes). It is template-fragile and unnecessary — both endpoints expose a documented API-level switch.
- **Default mode is budget-roulette:** with thinking ON, short prompts may finish inside `max_tokens` and long jury prompts won't — explains intermittent/total empty-content results across harness runs.
- **Verdict:** Mima upgrade proceeds as designed. No replacement tag needed. Fallbacks if ever required: qwen3:30b-a3b-instruct-2507 (installed, non-thinking) or gpt-oss:20b.

### Retire (after replacements validated — Papa approval required; `ollama rm` is destructive)
| Model | Reclaims | Why |
|---|---:|---|
| llama3.1:405b | **243 GB** | No scheduled role, 2024-era, dominated by gpt-oss:120b at 27% of the size |
| deepseek-r1:70b (Studio) | 42.5 GB | No role; r1 JSON defect; was idling resident |
| deepseek-r1:32b (Studio) | 19.9 GB | Duplicate of Mac Pro copy; same r1 defect |
| qwen3:30b (dense) | 18.6 GB | Superseded by a3b variants; no scheduled role |
| deepseek-r1:14b | 9.0 GB | After gpt-oss:20b validated in its three seats |
| phi4:14b | 9.1 GB | Role fully absorbed by gpt-oss:20b / qwen3.6:27b |

Net: retire ~342GB, pull ~120GB → **Studio disk drops ~222GB** and every remaining model has a named role.

### Rename / canonicalize
- **One authoritative nickname table** (below) replaces all four divergent sources. Tori updates `config.py` constants (`BUDDLE_MODEL` etc.) and `routing.py` header comments to match; `platoon-roster.md` v3 mirrors it.
- **Buddle** is rebound to gpt-oss:120b (one meaning, forever). **Nutty** migrates to gpt-oss:20b. **Mima** migrates to qwen3.6:35b-a3b. **Tera** migrates to qwen3.6:27b. **Nutty-Heavy** and **Takji** retire as names with their models.

---

## 4. Updated platoon table (proposed)

| Nickname | Model | Machine | Role | Why |
|---|---|---|---|---|
| Rakon | deepseek-r1:671b | Mac Pro | On-demand deep synthesis | Largest local reasoner; cold-load minutes → batch-only, never real-time. No local V4 successor exists yet |
| Buddle | **gpt-oss:120b** (pull) | Mac Studio | Heavy general reasoning / synthesis backup | ≈o4-mini-class ⚠ at 65GB; replaces 405b at 27% footprint; clean tool/JSON output |
| Vera | astrosage-70b | Mac Studio | Astronomy drafting & synthesis | Domain-tuned 70B; no 2026 equal for astro idiom/citations |
| Blanc | llama3.3:70b | Mac Studio | Non-astronomy prose | Adequate; re-eval vs Buddle after pilot |
| Mima | **qwen3.6:35b-a3b** (pull) | Mac Studio | Jury juror #1 / general scoring | MoE A3B = fast decode for 90s jury budget; 256K ctx; gate on JSON validation |
| Tera | **qwen3.6:27b** (pull) | Mac Studio | General mid + **vision** | Dense 27B successor to gemma3; reads plots/figures — new triage capability |
| Nutty | **gpt-oss:20b** (pull) | Mac Studio | Jury juror #2 / fast reasoning + JSON | Fixes the r1 empty-content defect in every JSON seat; 14GB, co-resident friendly |
| Pico | vanta-research/atom-astronomy-7b | Mac Studio | Jury juror #3 / astro fast screen | Domain-tuned, 4.5GB, pinned resident; KEEP/DISCARD + astro entailment |
| — | qwen3-embedding:4b | Mac Studio | Embeddings (primary) | Marker aligner, arXiv classifier; document as platoon member |
| (cloud) | gemini-2.5-flash → 3.5-flash | API | Jury juror #4 / batch default | Cheap diversity vote; upgrade tick per June-3 audit |
| (cloud) | Sonnet / Opus | API | Judge ticks, rewrite, coherence | Unchanged — irreplaceable cognition only |

**Proposed jury: Mima + Nutty + Pico (local) + Gemini Flash (cloud).** All three local jurors are JSON-reliable, total ≈47GB resident, and fit comfortably alongside Vera. Resident pin set: **Pico + Mima + Nutty** (≈47GB @ 8k ctx), Vera/Blanc/Buddle load on demand.

Interim (before pulls validate): jury = qwen3:30b-a3b-2507 + Pico + Gemini Flash; drop the r1:14b seat now — it is a silent-failure seat.

---

## 5. Pull priority list

| # | Pull | Size | Impact |
|---|---|---:|---|
| 1 | `qwen3.6:35b-a3b` | 24 GB | Jury quality/speed upgrade on the highest-volume scored path |
| 2 | `gpt-oss:20b` | 14 GB | Kills the r1 empty-JSON defect in 3 live seats (jury, stance pre-judge, skeptic) |
| 3 | `gpt-oss:120b` | 65 GB | Unlocks retiring llama3.1:405b (net −178GB); heavy-general slot |
| 4 | `qwen3.6:27b` | 17 GB | Vision triage + general mid consolidation (retires gemma3 + qwen3:30b dense) |

Total new: **120 GB**. Each pull is followed by a validation gate (JSON-output test ×20 calls, latency under jury timeout, `/no_think`-equivalent behavior check) **before** any retire happens. Retires are Papa-approval-gated.

---

## 6. Platoon Assignment — periodic jobs (post-overhaul)

| Job (cadence) | Owner | Why this model |
|---|---|---|
| Stance jury (90s spacing, ~40/h enqueue) | **Mima + Nutty + Pico** local, Gemini Flash cloud | Speed: all ≤24GB, A3B/20B decode fits 60–90s timeout. Quality: Pico domain entailment, Mima/Nutty general reasoning, JSON-reliable all three |
| arXiv fast screen KEEP/DISCARD | **Pico** | 4.5GB pinned, domain-tuned, sub-second-class; unchanged |
| Evidence stance pre-judge (`paper_search.py`) | **Nutty** (gpt-oss:20b) | Replaces r1:14b — that seat needs sync JSON, r1 can't deliver it |
| Adversarial query gen | **Tera** (qwen3.6:27b) | Replaces gemma3:27b like-for-like, newer base |
| Adversarial skeptic | **Nutty** | Replaces r1:14b (same defect) |
| Autowiki section proposer (15-min tick) | **Vera** | Unchanged; pin Vera during autowiki windows or accept cold-load — reconcile with `ollama_model_policy_v1.md` resident set |
| Autowiki section rewrite (final) | Sonnet (cloud) | Unchanged — LaTeX + contract compliance quality bar |
| Coherence rewrite | Sonnet (cloud) | Unchanged |
| Deep synthesis / multi-doc analysis | **Rakon** (batched) or **Buddle** (interactive) | Rakon when depth is the bottleneck and minutes-scale latency is fine; Buddle for same-hour turnaround |
| Non-astro long-form (newsletter, news curation) | **Blanc**, pilot vs **Buddle** | Existing role; winner of a fixed drafting eval keeps it |
| Embeddings (marker aligner, classifier) | qwen3-embedding:4b | Standardize; nomic kept for legacy vectors only |
| High-volume batch default | gemini-2.5-flash → **gemini-3.5-flash** | Per June-3 audit; cheap, fast |
| Judge ticks (20m / 60m) | Sonnet / Opus | Unchanged |

**Co-residency rules (512GB Studio):** pin set Pico+Mima+Nutty ≈47GB; one 70B (Vera OR Blanc) on top ≈90GB total — comfortable. Buddle (65GB) + one 70B + pin set ≈155GB — fine. Never needed: two 70Bs + Buddle simultaneously. Rakon remains exclusive on Mac Pro; nothing changes there.

---

## 7. Decisions for Papa

1. **Approve the 4 pulls** (120GB, reversible, validation-gated)? — recommend yes.
2. **Retire llama3.1:405b** (243GB)? It was pulled recently — if it has a purpose I couldn't find in code or docs, say so; otherwise it's the single biggest win in the doc. **Was it intended as "Buddle"? If so, gpt-oss:120b fills that role at 27% the size.**
3. **Retire the three Studio deepseek-r1 models** after gpt-oss:20b validates? — recommend yes (JSON defect is structural).
4. **Drop the r1:14b jury seat immediately** (config one-liner, no pull needed)? — recommend yes, today.
5. **Rebind nicknames per §4** and make this table the single source of truth? — recommend yes; Tori syncs `config.py`/`routing.py`/roster in one commit.

---

## 8. Source links checked

Live local probes:
- Mac Studio inventory: `curl http://localhost:11434/api/tags` at 2026-06-11 08:54 KST.
- Mac Pro inventory: `curl http://169.254.100.1:11435/api/tags` at 2026-06-11 08:54 KST.

Ollama library pages checked 2026-06-11:
- Qwen3.6 family / tags: <https://ollama.com/library/qwen3.6>
- Qwen3.6 35B-A3B: <https://ollama.com/library/qwen3.6%3A35b-a3b>
- Qwen3.6 27B: <https://ollama.com/library/qwen3.6%3A27b>
- gpt-oss family / tags: <https://ollama.com/library/gpt-oss>
- gpt-oss 20B model blob: <https://ollama.com/library/gpt-oss%3A20b/blobs/e7b273f96360>
- gpt-oss 120B model blob: <https://ollama.com/library/gpt-oss%3A120b/blobs/90a618fe6ff2>
- DeepSeek-V4-Flash cloud tag: <https://ollama.com/library/deepseek-v4-flash%3Acloud>

---

## 9. Beyond Ollama — MLX, cloud burst, HF Transformers (added 2026-06-11, Papa request)

Scope expansion per Papa: non-Ollama options for the same hardware (Mac Studio M3 Ultra 512GB, Mac Pro). Additive to §1–8; does **not** block Tori's execution of decisions 1–5. External claims marked ⚠; local probes verified this session.

### 9.1 MLX / MLX-LM (Apple Silicon native)

**Verified local state:** Both hosts run **Ollama 0.24.0** (`/api/version`, 2026-06-11). Studio is macOS 26.5.1, M3 Ultra confirmed. Ollama ≥0.19 ships an MLX engine for Apple Silicon ⚠ — but our `server.log` shows the **ggml engine** loading every current model. Reason: our entire inventory is legacy **GGUF Q4_K_M** blobs; the MLX engine engages for MLX-format/NVFP4 model builds ⚠, not for existing GGUF pulls. So we are paying the llama.cpp tax today despite running an MLX-capable Ollama.

**What MLX buys on this hardware** (⚠ 2026 benchmarks, M3-Ultra-class):
- 15–30% higher decode throughput at equal quant vs llama.cpp GGUF; 20–87% for models <14B; **up to ~3× on MoE models** — exactly our jury profile (qwen3.6 A3B is MoE).
- ~10% lower memory from native unified-memory handling; tighter packing.
- Reference points ⚠: gpt-oss-20b ≈124 tok/s (MLX Q4); qwen3.5-35B-A3B NVFP4 58→112 tok/s switching ggml→MLX engine; gpt-oss-120b 8-bit batched ≈129 tok/s.
- Caveats ⚠: MLX's lead shrinks at long context (≳40K) and llama.cpp's server has more mature batched/concurrent scheduling — relevant if we ever run jury seats concurrently on one host.

**JSON reliability — MLX actually solves it structurally.** `mlx-lm` integrates with **Outlines** (and `llm-structured-output`) for *constrained decoding*: the sampler can only emit tokens that fit the JSON schema. That is a guarantee, not a prompt convention — stronger than anything Ollama's `format:"json"` gives us, and categorically immune to the r1-style empty-`content` defect (G3). LM Studio exposes the same via its OpenAI-compatible `/v1/chat/completions` with `response_format` (Outlines under the hood) ⚠.

**MLX candidates** (all on HuggingFace `mlx-community`/`unsloth` ⚠; sizes ≈, 4-bit unless noted):

| Candidate | (a) Platoon role | (b) JSON | (c) Disk/VRAM vs current | (d) vs Ollama equivalent |
|---|---|---|---|---|
| Qwen3.6-35B-A3B MLX 4-bit / NVFP4 | Mima (jury #1) | Guaranteed w/ Outlines | ≈19–20GB vs 24GB Ollama pull | Faster (MoE ≈3× ⚠), smaller, schema-guaranteed; cost = second runtime or NVFP4 re-pull |
| gpt-oss-20b MLX MXFP4 | Nutty (jury #2 / fast JSON) | Guaranteed w/ Outlines | ≈12GB vs 14GB | Already JSON-clean in Ollama; MLX adds ~speed only — weakest case for switching |
| gpt-oss-120b MLX MXFP4 | Buddle (heavy general) | Guaranteed w/ Outlines | ≈65GB (same) | Batched MLX throughput ⚠ attractive for synthesis runs; single-stream gain modest at this size (bandwidth-bound) |
| Qwen3.6-27B MLX 4-bit | Tera (general mid + vision) | Guaranteed w/ Outlines | ≈15GB vs 17GB | Vision via `mlx-vlm` is separate tooling — keep Ollama for vision path for now |

**Recommendation (MLX):** do *not* stand up a second runtime fleet-wide now. Two cheap moves instead:
1. **R1 — Engine check during Tori's validation gates (zero new infra):** when Tori pulls the §5 models, prefer **NVFP4/MLX-engine variants where the Ollama library offers them**, and verify in `server.log` which engine loads. If the MLX engine engages, we capture most of the speed win inside the runtime we already operate.
2. **R2 — One-seat pilot (after Tori finishes):** run `mlx-lm` + Outlines as a sidecar OpenAI-compatible server hosting **one** jury seat (Mima candidate, Qwen3.6-35B-A3B 4-bit). Measure: votes/hour, timeout rate, schema-violation rate (should be exactly 0). Promote only if it beats the Ollama seat on the same model. This is the only seat where MoE decode speed + guaranteed JSON both pay off.

### 9.2 Cloud burst — Groq, Together, Fireworks, OpenRouter

**Verified current state:** `tasks.py` already implements a burst chain — **Ollama(local) → Groq → Cerebras → SambaNova** (`tasks.py:461`), with a Groq jury label `JuryGroq` (`tasks.py:126`, default `llama-3.3-70b-versatile`). `.env` has keys for Groq (`NM_LLM_API_KEY`), Cerebras, SambaNova, Gemini, Anthropic. **No Together/Fireworks/OpenRouter integration exists.**

**Pricing snapshot** (⚠ fetched 2026-06-11, per 1M tokens in/out):

| Provider | gpt-oss-20b | gpt-oss-120b | Qwen mid (27–35B) | Latency class |
|---|---|---|---|---|
| Groq (have key) | ~$0.04 w/ cache | $0.15 / $0.60 | qwen3-32b $0.29 / $0.59 | TTFT <0.25s, 280–1000 tok/s — fastest |
| Together | $0.05 / $0.20 | $0.15 / $0.60 | qwen3-235b $0.20 / $0.60 | GPU-class, ~10× slower than Groq ⚠ |
| Fireworks | $0.07 / $0.30 | $0.15 / $0.60 | qwen3-VL-30b $0.15 / $0.60 | Fastest GPU provider ⚠ |
| OpenRouter | **free tier** | **free tier** | qwen3.5-27b $0.195 / $1.56 | Varies by routed provider; +5.5% fee on paid |

**Where cloud beats local (role analysis):**
- **Saturation relief — the strongest case.** Documented failure mode (TOOLS.md, 2026-05-20): when Celery keeps Studio Ollama hot, sync calls return empty/timeout. A cloud juror seat keeps voting when local is saturated. Groq gpt-oss-20b at jury volume (~960 calls/day × ~2.5K in / 400 out) ≈ **$6–12/month** ⚠ — noise.
- **Deadline ticks / interactive synthesis:** Groq gpt-oss-120b gives Buddle-class reasoning at sub-second TTFT for same-hour turnaround when Buddle is cold or the Studio is busy. $0.15/$0.60 is cheaper than Sonnet by ~20× for the non-final drafting passes.
- **Diversity juror:** a cloud seat (different weights, different failure modes) hardens the jury against correlated local errors — same logic as the existing Gemini Flash seat.
- **Where local stays right:** steady-state high-volume scoring (jury, arXiv screen, embeddings) — zero marginal cost on hardware we own, no rate limits, no data egress. Cloud is the relief valve, not the baseline.

**Recommendation (cloud):**
1. **R3 — Repoint the existing Groq seat** from `llama-3.3-70b-versatile` to **`gpt-oss-120b`** ($0.15/$0.60, better reasoning per dollar ⚠) for the burst chain, and **`gpt-oss-20b`** for the JuryGroq seat. Config-only change; keys already live.
2. **R4 — Add OpenRouter as an experiment gateway** (one env key): free gpt-oss-20b/120b tiers (~50 req/day ⚠) are perfect for A/B-ing candidate models before pulling weights locally. Not for production SLA paths.
3. **Skip Together and Fireworks for now** — they fill no role Groq+Cerebras+SambaNova don't already cover, and each new provider is another key, billing surface, and failure mode. Revisit if we need Qwen-VL serverless (Fireworks) or fine-tuned model hosting (Together).

### 9.3 HuggingFace Transformers + quantization

**When it beats Ollama on this hardware: almost never for inference.** PyTorch MPS runs fp16/bf16 but cannot CPU-offload via `device_map`, has operator fallbacks to CPU, and its quantization story (Quanto int4/int8; community `mps-bitsandbytes` since Feb 2026 ⚠) is strictly dominated by MLX-native 4/8-bit on speed and memory. Setup overhead (venv, weights in safetensors at 2× GGUF disk before quant, manual serving) buys nothing for our serving roles.

**The two legitimate uses:**
1. **Fine-tuning** — if we ever domain-tune a Pico successor (astro classifier) or LoRA Vera-class models on DESI/NebulaMind corpora, the training has to happen outside Ollama. Even then, **`mlx_lm.lora` is the better Apple Silicon path** (QLoRA-style, unified memory native); HF+`mps-bitsandbytes` is the fallback if an architecture lacks MLX training support.
2. **Unconverted models** — a niche model with no GGUF/MLX release (e.g., some science-tuned checkpoints). None of our current candidates qualify; astrosage and atom both have GGUF.

**Recommendation (HF):** **R5 — no platoon role for HF Transformers.** Revisit only when a fine-tuning project is approved; budget it as a training stack, not a serving stack.

### 9.4 Additional decisions for Papa (additive to §7)

6. **Approve R1** (prefer NVFP4/MLX-engine variants in Tori's §5 pulls + log the engine at validation)? — recommend yes; zero extra cost, folds into work already in flight.
7. **Approve R2** (post-Tori one-seat `mlx-lm`+Outlines jury pilot)? — recommend yes, gated on Tori finishing decisions 1–5.
8. **Approve R3** (repoint Groq burst chain to gpt-oss-120b / JuryGroq to gpt-oss-20b)? — recommend yes; config-only.
9. **Approve R4** (OpenRouter key for free-tier model A/B)? — optional, low value-at-risk; Papa's call.
10. **R5** (no HF Transformers adoption) — no action needed unless Papa objects.

### 9.5 §9 sources

Verified locally 2026-06-11: `/api/version` both hosts (0.24.0); `~/.ollama/logs/server.log` engine lines; `system_profiler` (M3 Ultra, 512GB); `tasks.py` burst chain + `JuryGroq`; `.env` key names.

External (⚠, fetched 2026-06-11): Ollama MLX engine — <https://ollama.com/blog/mlx>, <https://docs.ollama.com/faq>; MLX-LM — <https://github.com/ml-explore/mlx-lm>; Outlines MLX-LM structured generation — <https://dottxt-ai.github.io/outlines/latest/features/models/mlxlm/>; `llm-structured-output` — <https://pypi.org/project/llm-structured-output/>; OpenAI gpt-oss baseline — <https://openai.com/index/introducing-gpt-oss/>; MLX quants — <https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit>, <https://huggingface.co/unsloth/Qwen3.6-27B-MLX-8bit>, mlx-community on HF; pricing — <https://groq.com/blog/gpt-oss-improvements-prompt-caching-and-lower-pricing>, <https://groq.com/blog/groqcloud-tm-now-supports-qwen3-32b>, <https://fireworks.ai/pricing>, <https://openrouter.ai/pricing>, <https://openrouter.ai/collections/free-models>, <https://openrouter.ai/openai/gpt-oss-120b>; `mps-bitsandbytes` — <https://pypi.org/project/mps-bitsandbytes/>; HF MPS limits — <https://huggingface.co/docs/transformers/en/perf_train_special>.

---

*All Ollama-library size/capability claims fetched 2026-06-11 and marked ⚠ where they rest on vendor/third-party reporting. Local probe data (inventory, resident set, config) is live-verified this session. §9 added 2026-06-11 (Papa-requested scope expansion); §9 external benchmarks/pricing are ⚠ third-party.*

### 9.6 Ruling (Kun, 2026-06-11, delegated via HwaO)

HwaO relayed that R1–R5 await my call (Papa-proxy delegation). Rulings — all non-destructive; §7 retirements (#2, #3) remain Papa-gated and are NOT covered here:

- **R1 — APPROVED, effective immediately** (time-sensitive: Tori's §5 pulls are in flight). Prefer NVFP4/MLX-format variants where the Ollama library offers one; log the inference engine (`ggml` vs `mlx`) in each validation record. If no MLX-engine variant exists for a model, fall back to GGUF Q4_K_M — do not block the pull.
- **R2 — APPROVED, gated.** One-seat `mlx-lm`+Outlines jury pilot starts only after Tori completes §7 decisions 1–5 and validations pass. Pilot seat runs A/B against the seat it would replace; no wider rollout without a results review.
- **R3 — APPROVED.** Repoint Groq burst chain to `gpt-oss-120b`, JuryGroq to `gpt-oss-20b`. Config-only and reversible; require one successful live call per repointed endpoint before commit.
- **R4 — DEFERRED to Papa.** Requires provisioning an external OpenRouter account/key, which only Papa can do. Low value-at-risk, blocks nothing; revisit on Papa's convenience.
- **R5 — APPROVED.** No HF Transformers adoption. If fine-tuning ever becomes a need, `mlx_lm.lora` is the designated path.
