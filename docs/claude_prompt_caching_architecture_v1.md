# Claude Prompt Caching Architecture — NebulaMind
**v1.1 | 2026-06-09 20:02 KST | Author: Kun**

> **v1.1 changelog:** Audit table widened from 6 to 11 call sites after re-grep
> caught `arxiv_fetch.py`, `auto_improvement.py`, and
> `research_ideas/auto_improvement.py`. F-1 (`temperature` bug) reclassified
> from "judge-only" to "system-wide" — 5 Opus call sites are silently
> 400-failing, not 1. Step 1 of the Tori plan now covers all 5 sites.

---

## 0. Corrections to the Original Task Brief

The brief from HwaO contained three factual errors that would have produced a
non-functional design. Corrected values are used throughout this document.

| Error in brief | Correct value | Source |
|---|---|---|
| "Claude 3.5 Sonnet" | `claude-sonnet-4-6` | tasks.py, judge_panel.py |
| "Claude 3 Opus" | `claude-opus-4-7` | tasks.py, judge_panel.py |
| "Opus threshold 2,048 tokens" | **4,096 tokens** | Anthropic API docs |
| "Sonnet threshold 1,024 tokens" | **1,024 tokens** for `claude-sonnet-4-6` | Anthropic API docs / live audit correction |
| "saves up to 90%" | Up to ~90% on reads; **writes cost 1.25×** | Anthropic pricing |

The "Claude 3" names are retired and return 404. Using them in API calls fails
silently (the SDK raises an error, caught by the `except Exception` wrappers,
and the function returns `None`).

---

## 1. Cache Mechanics Reference

### 1.1 Minimum token thresholds

| Model | Min tokens to qualify |
|---|---|
| `claude-opus-4-7` | **4,096 tokens** |
| `claude-sonnet-4-6` | **1,024 tokens** |
| `claude-haiku-4-5` | Verify before implementation. Used at `arxiv_fetch.py:112` but with a ~30-tok system prompt, so caching is moot regardless of threshold. |

A `cache_control` marker on a block below threshold is silently accepted but
never cached. The API does not warn. This is the "silent no-op" pattern.

### 1.2 Cache TTLs

| Type | TTL | Write cost multiplier | Read cost multiplier |
|---|---|---|---|
| Ephemeral (default) | 5 minutes | 1.25× base input | 0.10× base input |
| Extended | 1 hour | 2.00× base input | 0.10× base input |

Use `"cache_control": {"type": "ephemeral"}` unless the job period exceeds
5 minutes and the same prefix will be reused within an hour.

### 1.3 Prefix-match invariant

The cache key is the **exact byte sequence** of all content before the
`cache_control` breakpoint. Block render order: `tools → system → messages`.
Any byte change anywhere in the prefix invalidates every breakpoint after it.

**Maximum breakpoints per request: 4.**

### 1.4 Silent invalidators — must eliminate before adding `cache_control`

| Pattern | Why it breaks caching |
|---|---|
| `f"... {datetime.now()} ..."` in system | Different bytes every call |
| `uuid.uuid4()` in system prefix | Same |
| `json.dumps(dict)` without `sort_keys=True` | Key order not guaranteed |
| Conditional system sections (`if flag: system += "..."`) | Variable byte sequence |
| Different tool sets per call | Render before system; invalidate everything |

---

## 2. Current State Audit

### 2.1 All Anthropic API call sites

| File | Line | Model | `cache_control`? | System prompt size | Effective? |
|---|---|---|---|---|---|
| `autowiki/judge_panel.py` | 72 | `claude-sonnet-4-6` | YES — ephemeral | ~6,453 chars ≈ **1,600–2,150 tok** | **YES** — clears 1,024 |
| `autowiki/judge_panel.py` | 72 | `claude-opus-4-7` | YES — ephemeral | same | **NO — silent no-op** (below 4,096) |
| `autowiki/tasks.py` | 1675 | `claude-sonnet-4-6` | NO | `_SONNET_SECTION_SYSTEM` ≈ **313–418 tok** | No |
| `autowiki/tasks.py` | 217 | `claude-opus-4-7` | NO | `_COHERENCE_SYSTEM_PROMPT` ≈ **225–333 tok** | No |
| `marker_embed/aligner.py` | 80, 288 | `claude-sonnet-4-6` | NO | `_SYSTEM` ≈ **63–83 tok** | No |
| `marker_embed/judge.py` | 58 | `claude-sonnet-4-6` | NO | `_SYSTEM` ≈ **50–67 tok** | No |
| `arxiv_fetch.py` | 112 | `claude-haiku-4-5-20251001` | NO | `ARXIV_SUMMARY_SYSTEM` ≈ **30 tok** | No |
| `auto_improvement.py` | 1955 | `claude-opus-4-7` | NO | **none** (prompt in user msg) | No |
| `auto_improvement.py` | 2160 | `claude-opus-4-7` | NO | **none** (prompt in user msg) | No |
| `research_ideas/auto_improvement.py` | 2019 | `claude-opus-4-7` | NO | **none** (prompt in user msg) | No |
| `research_ideas/auto_improvement.py` | 2237 | `claude-opus-4-7` | NO | **none** (prompt in user msg) | No |

### 2.2 Key findings

**F-1 (Critical, system-wide bug):** `claude-opus-4-7` returns HTTP 400 when
`temperature` is set. **Every Opus call site in the backend passes `temperature`**,
so all of them silently fail today. The `except Exception:` wrappers around each
call swallow the 400 and return a fallback — zero-utility audit results,
`opus_failed_open` verdicts, or `{"error": str(exc)}` — so the bug is invisible
in dashboards.

Affected sites (5 total):

| File:line | Job | `temperature` | Fallback when it fails |
|---|---|---|---|
| `judge_panel.py:72` | `opus_judge_tick` | 0.2 | `_make_zero_result(...)` |
| `auto_improvement.py:1955` | `judge_idea_pool` | 0.2 | `opus_failed_open` (promotes anyway) |
| `auto_improvement.py:2160` | `opus_hero_refresh` | 0.3 | `return {"error": str(exc)}` |
| `research_ideas/auto_improvement.py:2019` | `research_ideas.opus_judge_pool` | 0.2 | `opus_failed_open` (promotes anyway) |
| `research_ideas/auto_improvement.py:2237` | `research_ideas.opus_hero_refresh` | 0.3 | `return {"error": str(exc)}` |

Sonnet 4.6 supports `temperature`; the bug is Opus-only. Fix: remove the
`temperature=...` argument from every Opus call. The judge/promotion rubrics
are deterministic by design — `temperature` was a redundant knob even on Sonnet.

The two `opus_hero_refresh` definitions (in `auto_improvement.py` and
`research_ideas/auto_improvement.py`) appear to be duplicates; consolidation is
out of scope for this design but worth flagging for a follow-up clean-up task.

**F-2 (Silent no-op):** The `cache_control: ephemeral` on the Opus judge
system prompt has never cached anything. The judge system prompt is
~1,600–2,150 tokens; Opus requires ≥ 4,096.

**F-3 (No cache metrics):** `log_llm_spend()` does not record
`cache_creation_input_tokens` or `cache_read_input_tokens`. Cache effectiveness
cannot be measured.

**F-4 (Largest uncached prompt):** `_call_opus_coherence` builds a user
message that contains the full page content (~62,000 chars ≈ 15,500 tokens)
every call. No `cache_control`. This is the single highest-ROI caching target
in the codebase.

**F-5 (Below-threshold system prompts):** `_SONNET_SECTION_SYSTEM` (~285–418
tokens) and the `marker_embed` `_SYSTEM` strings (50–83 tokens) are far below
the Sonnet 1,024-token minimum. Adding `cache_control` to them today does
nothing.

---

## 3. ROI Ranking

| Priority | Target | Estimated monthly saving (KRW) | Complexity |
|---|---|---|---|
| P0 | Strip `temperature` from all 5 Opus call sites (F-1) | Restores `opus_judge_tick`, `judge_idea_pool`, and both `opus_hero_refresh` pipelines — a correctness fix, not a savings | Low |
| P1 | `opus_coherence` — cache user-msg page content | Very high — 15,500 tok cached at 0.10× vs 1.00× on Opus | Medium |
| P2 | `judge_panel.py` Sonnet — keep current breakpoint; add metrics | Low–Medium | Low |
| P3 | `judge_panel.py` Opus — grow system prompt to ≥4,096 tokens | Low–Medium once F-1 fixed | Low |
| P4 | Add cache token tracking to `log_llm_spend` | Enables measurement | Low |
| Backlog | `sonnet_section_rewrite`, `marker_embed/*` | Requires prompt restructure | High |

---

## 4. Layered Prefix Architecture

Every cacheable call site should use this three-layer model:

```
┌──────────────────────────────────────────────────────────────┐
│  Layer 1 — Static                                            │
│  Model persona, invariant rules, rubric definitions          │
│  NEVER changes between calls.                                │
│  → cache_control: ephemeral (or extended if period > 5 min)  │
├──────────────────────────────────────────────────────────────┤
│  Layer 2 — Stable                                            │
│  Page content, section context, knowledge base snapshot      │
│  Changes per page (not per call). Same page → same bytes.    │
│  → cache_control: ephemeral                                  │
├──────────────────────────────────────────────────────────────┤
│  Layer 3 — Dynamic                                           │
│  Claim text, run-specific parameters, per-call metadata      │
│  Changes every call. Never cached.                           │
│  → no cache_control                                          │
└──────────────────────────────────────────────────────────────┘
```

Rules:
1. Place `cache_control` on the LAST block of each stable layer, not every block.
2. Dynamic content must always come AFTER all cached blocks.
3. No timestamps, UUIDs, or non-deterministic values inside any cached layer.
4. Maximum 4 breakpoints per request; use ≤ 2 for safety in most cases.

---

## 5. Per-Call-Site Architecture

### 5.1 `_call_opus_coherence` — HIGHEST ROI

**Current code (tasks.py:217–222):**
```python
with client.messages.stream(
    model="claude-opus-4-7",
    max_tokens=32000,
    system=_COHERENCE_SYSTEM_PROMPT,          # Layer 1: static, ~333 tok — TOO SMALL
    messages=[{"role": "user", "content": prompt}],  # Layer 2+3 mixed, ~15,500 tok — UNCACHED
) as stream:
```

**Problem:** System prompt is too small to cache on Opus (needs ≥ 4,096 tokens).
The 15,500-token page content is in the user message with no breakpoint.

**Architecture after fix:**

```
system=[
    {"type": "text", "text": _COHERENCE_SYSTEM_PROMPT}  # Layer 1 — keep as-is
    # (too small to cache; expand or accept no system caching on this call)
]

messages=[
    # Layer 2: stable page content block → cached
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": f"===PAGE CONTENT===\n{content}",
                "cache_control": {"type": "ephemeral"}    # ← BREAKPOINT
            }
        ]
    },
    # Layer 3: dynamic per-run parameters → NOT cached
    {
        "role": "assistant",
        "content": "Understood. I will now rewrite this page."
    },
    {
        "role": "user",
        "content": f"===CLAIMS===\n{claims_text}\n\n===CITATIONS===\n{citation_context}\n\nProceed."
    }
]
```

**Why this works:** For a page that is rewritten multiple times in a session,
the full page content (~15,500 tokens) is only charged at 0.10× on the second
and subsequent calls within 5 minutes. On Opus 4.7 pricing (~₩75,000/1M output
tokens, ₩15,000/1M input tokens), caching 15,500 tokens per re-call saves
~₩209 per hit (15,500 × 15,000 × (1.0 - 0.1) / 1,000,000).

**Note on system prompt:** `_COHERENCE_SYSTEM_PROMPT` is ~333 tokens — below
Opus's 4,096 threshold. Adding `cache_control` to it would be a silent no-op.
Options: (a) expand it to ≥ 4,096 tokens by appending detailed style rules and
rubric, or (b) accept no system caching and rely entirely on user-message
caching. Option (b) is simpler and sufficient.

### 5.2 `judge_panel.py` — FIX TEMPERATURE FIRST

**Current code (judge_panel.py:62–86):**
```python
def _call_claude(model: str, system: str, user_msg: str) -> dict | None:
    ...
    response = client.messages.create(
        model=model,
        max_tokens=512,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
        temperature=0.2,    # ← BUG: returns HTTP 400 on claude-opus-4-7
    )
```

**Fix:** Remove `temperature` from the call entirely. Opus 4.7 returns 400 when
temperature is set. Sonnet 4.6 supports it, but the judge rubric is deterministic
by design — `temperature=0.2` provides no benefit over the default.

**Post-fix architecture — Sonnet judge:**
- System prompt ≈ 1,600–2,150 tokens, which clears the Sonnet 1,024-token
  minimum. The existing `cache_control` breakpoint is correctly placed on the
  static system block.
- Recommendation: keep the current breakpoint, add usage metrics, then check
  `usage.cache_read_input_tokens` over 24 hours to verify actual hit rate.

**Post-fix architecture — Opus judge:**
- System prompt is a silent no-op at ≤ 2,150 tokens vs. 4,096 threshold.
- To enable system-prompt caching on Opus judge: expand `_load_prompt()` to
  return at least 4,096 tokens by adding detailed scoring rubric definitions,
  domain vocabulary reference, or example judge outputs.
- Alternatively, cache the user message: the page content portion of `user_msg`
  is stable per page within a 20-minute window (judge runs every 60 min, so
  caching adds minimal value unless the same page is judged twice within 5 min).
- Near-term recommendation: just fix the `temperature` bug (P0) and skip Opus
  system caching until prompt expansion is prioritized.

### 5.3 `sonnet_section_rewrite` (tasks.py:1675)

`_SONNET_SECTION_SYSTEM` is ~285–418 tokens — far below Sonnet's 1,024 minimum.
Adding `cache_control` today would be a silent no-op.

The user message varies per section per call (different section content, claims,
evidence map). There is no stable large prefix to cache in the user message.

**Recommendation:** Defer. Only worth investing when `_SONNET_SECTION_SYSTEM`
is expanded with detailed writing rubric, banned-phrase lists, and style
examples to push past 1,024 tokens. At that point, add `cache_control` to the
system block.

### 5.4 `marker_embed/aligner.py` and `marker_embed/judge.py`

Both use tiny `_SYSTEM` strings (50–83 tokens). User messages are fully variable
per claim pair. No caching opportunity without a full prompt restructure.

**Recommendation:** Defer indefinitely. These calls are fast (max_tokens=80–
1024) and the variable content dominates. Caching would require putting a large
stable reference corpus in a preceding user turn — over-engineering for small
models.

---

## 6. `log_llm_spend` Extension — Cache Token Tracking

Add `cache_creation_input_tokens` and `cache_read_input_tokens` to the spend
log so cache effectiveness can be measured.

**File:** `app/utils/premium_dispatch.py`

**Current signature (line 270):**
```python
def log_llm_spend(
    job_name: str,
    model: str,
    *,
    prompt_tokens: int | None = None,
    completion_tokens: int | None = None,
    estimated_tokens: int | None = None,
    status: str = "executed",
    metadata: dict[str, Any] | None = None,
    db=None,
) -> None:
```

**Add two parameters:**
```python
def log_llm_spend(
    job_name: str,
    model: str,
    *,
    prompt_tokens: int | None = None,
    completion_tokens: int | None = None,
    cache_creation_tokens: int | None = None,   # ← new
    cache_read_tokens: int | None = None,        # ← new
    estimated_tokens: int | None = None,
    status: str = "executed",
    metadata: dict[str, Any] | None = None,
    db=None,
) -> None:
```

**In the body, add to metadata:**
```python
    # Merge cache stats into metadata for log visibility
    cache_stats: dict[str, Any] = {}
    if cache_creation_tokens is not None:
        cache_stats["cache_creation_tokens"] = cache_creation_tokens
    if cache_read_tokens is not None:
        cache_stats["cache_read_tokens"] = cache_read_tokens
    if cache_stats:
        metadata = {**(metadata or {}), **cache_stats}
```

**In `judge_panel.py` — after reading usage:**
```python
usage = getattr(response, "usage", None)
log_llm_spend(
    job_name,
    model,
    prompt_tokens=getattr(usage, "input_tokens", None),
    completion_tokens=getattr(usage, "output_tokens", None),
    cache_creation_tokens=getattr(usage, "cache_creation_input_tokens", None),
    cache_read_tokens=getattr(usage, "cache_read_input_tokens", None),
    estimated_tokens=est_tokens["input"],
)
```

With this in place, a simple SQL query reveals cache effectiveness:
```sql
SELECT
    model_name,
    COUNT(*) as calls,
    SUM((metadata_json::jsonb ->> 'cache_read_tokens')::int) as total_cache_read,
    SUM((metadata_json::jsonb ->> 'cache_creation_tokens')::int) as total_cache_write
FROM llm_spend_log
WHERE status = 'executed'
  AND created_at >= NOW() - INTERVAL '24 hours'
GROUP BY model_name;
```

---

## 7. Platoon Assignment — Tori Implementation Plan

All implementation work goes to Tori (executor). Steps are ordered by priority.
No Kun, Blanc, or Rakon involvement needed — these are mechanical code changes.

### Step 1 — Remove `temperature` from ALL Opus 4.7 call sites [P0, ~25 min]

Opus 4.7 returns HTTP 400 when `temperature` is set. Five call sites are
affected; remove the `temperature=...` line from each. No other arguments
change.

| # | File | Line | Current | Required |
|---|---|---|---|---|
| 1 | `app/agent_loop/autowiki/judge_panel.py` | 76 | `temperature=0.2,` | delete line |
| 2 | `app/agent_loop/auto_improvement.py` | 1959 | `temperature=0.2,` | delete line |
| 3 | `app/agent_loop/auto_improvement.py` | 2164 | `temperature=0.3,` | delete line |
| 4 | `app/agent_loop/research_ideas/auto_improvement.py` | 2023 | `temperature=0.2,` | delete line |
| 5 | `app/agent_loop/research_ideas/auto_improvement.py` | 2241 | `temperature=0.3,` | delete line |

For `judge_panel.py:_call_claude()` (sites 1) the function is called with
**both** `claude-sonnet-4-6` and `claude-opus-4-7`; Sonnet still accepts
`temperature`, but the judge rubric is deterministic, so removing
`temperature=0.2` for both models is safe and avoids a model-aware branch.

Example (site 1):
```python
# BEFORE
response = client.messages.create(
    model=model,
    max_tokens=512,
    system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
    messages=[{"role": "user", "content": user_msg}],
    temperature=0.2,
)

# AFTER
response = client.messages.create(
    model=model,
    max_tokens=512,
    system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
    messages=[{"role": "user", "content": user_msg}],
)
```

**Verification:**
1. After restart, run `opus_judge_tick` manually on page 57. Check that
   `AutowikiRun` rows for `model_judge='claude-opus-4-7'` now have
   `u1_median > 0.0`.
2. Trigger `judge_idea_pool` on a page with ≥ 5 polished candidates; confirm
   `opus_verdicts` in the job log no longer report `"opus_failed_open"` for
   every entry.
3. Trigger `opus_hero_refresh` on a page with new accepted claims; confirm the
   `wiki_pages.hero_tagline` row is updated rather than the job returning
   `{"error": ...}`.

---

### Step 2 — Add cache token tracking to `log_llm_spend` [P1, ~20 min]

**File:** `app/utils/premium_dispatch.py`

Implement the extension described in §6. No DB schema change needed; the two
new fields go into the existing `metadata_json` JSONB column.

After implementing, update all callers that pass `usage` from Anthropic:
- `judge_panel.py:77–83` — add `cache_creation_tokens` and `cache_read_tokens`
- `tasks.py:1683–1688` (`sonnet_section_rewrite`) — same
- `tasks.py:227–231` (`opus_coherence`) — same; currently uses only
  `estimated_tokens`, so swap to actual when tokens are available from
  `stream.get_final_message().usage`

---

### Step 3 — Cache page content in `_call_opus_coherence` [P1, ~30 min]

**File:** `app/agent_loop/autowiki/tasks.py`
**Function:** `_call_opus_coherence` (line 188)

Restructure the `messages.stream()` call to split page content into a separate
cached user block. The system prompt stays as a plain string (too small to cache
on Opus; no `cache_control` on system).

```python
# BEFORE (tasks.py:217–222)
with client.messages.stream(
    model="claude-opus-4-7",
    max_tokens=32000,
    system=_COHERENCE_SYSTEM_PROMPT,
    messages=[{"role": "user", "content": prompt}],
) as stream:

# AFTER
# Split prompt into stable page block + dynamic instructions
page_block = f"===PAGE CONTENT===\n{content}"
dynamic_block = (
    f"===CLAIMS===\n{claims_text}\n\n"
    f"===CITATIONS===\n{citation_context}\n\n"
    "Now rewrite the page following all system instructions."
)

with client.messages.stream(
    model="claude-opus-4-7",
    max_tokens=32000,
    system=_COHERENCE_SYSTEM_PROMPT,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": page_block,
                    "cache_control": {"type": "ephemeral"},  # cache page content
                },
                {
                    "type": "text",
                    "text": dynamic_block,                   # dynamic, not cached
                },
            ],
        }
    ],
) as stream:
```

**Important:** `prompt` was previously built with
`_COHERENCE_USER_TEMPLATE.format(full_page_content=content, claims_text=…,
citation_context=…)`. After this change, that template is replaced by the two
explicit blocks. Delete the old `prompt =` line. Update the `est_tokens`
estimate to use `len(page_block) + len(dynamic_block)` instead.

Also update the `log_llm_spend` call to capture actual usage from
`stream.get_final_message().usage` instead of estimating:

```python
final_msg = stream.get_final_message()
usage = getattr(final_msg, "usage", None)
log_llm_spend(
    "autowiki.opus_coherence",
    "claude-opus-4-7",
    prompt_tokens=getattr(usage, "input_tokens", None),
    completion_tokens=getattr(usage, "output_tokens", None),
    cache_creation_tokens=getattr(usage, "cache_creation_input_tokens", None),
    cache_read_tokens=getattr(usage, "cache_read_input_tokens", None),
    estimated_tokens=est_tokens["input"],
)
```

---

### Step 4 — Verify Sonnet judge cache hit rate [P2, ~10 min after Step 2]

After Step 2 lands, wait 24 hours and run the SQL from §6. If
`total_cache_read = 0` for `claude-sonnet-4-6` on judge ticks despite repeated
calls within the TTL, treat it as a breakpoint/rendering bug, not a likely
token-floor miss. The system prompt clears the 1,024-token Sonnet floor in the
live audit.

Only if Anthropic usage confirms a threshold miss should Tori pad the prompt:

**File:** `app/agent_loop/autowiki/judge.py` (where `_load_prompt()` is defined)

Append a static rubric appendix to the prompt to push it past 1,024 tokens.
The appendix should be astronomically accurate content (no hallucination risk
since it's qualitative rubric language). Example:

```python
_PROMPT_PADDING = """
## Appendix: Scoring Rubric Definitions

### Completeness dimensions
- citation_density: Fraction of factual sentences carrying at least one
  <!--cite:N--> marker. Target ≥ 0.35 for a well-sourced section.
- recency_density_2020: Fraction of citations referencing work from 2020 or later.
  Threshold 0.25 for a live topic like galaxy evolution.
- recency_density_2023: Same, restricted to 2023–present. Threshold 0.10.
- instrument_breadth: Number of distinct survey/instrument acronyms mentioned
  (SDSS, JWST, ALMA, MaNGA, CANDELS, HSC, Euclid, DESI, VLA, Planck, Herschel,
  Chandra, XMM, Spitzer, 2dFGRS, GAMA, zCOSMOS, COSMOS, MUSE, SINFONI).
  Target ≥ 4 for a review-article section.

### Voice dimensions
- voice_purity: Absence of AI-erosion markers. Deduct for: "plays a crucial
  role", "complex and dynamic", "fundamental understanding", "key driver",
  "important implications", "remains to be seen", "future work will".
...
"""
```

Pad only enough to clear the reported floor with margin; 1,200 tokens is enough
for Sonnet 4.6 if Anthropic reports a floor miss. Add `_PROMPT_PADDING` at the
end of the string returned by `_load_prompt()`.

---

### Step 5 — Defer marker_embed and sonnet_section_rewrite [Backlog]

Do not add `cache_control` to:
- `marker_embed/aligner.py` `_SYSTEM` (50–83 tokens — silent no-op)
- `marker_embed/judge.py` `_SYSTEM` (50–67 tokens — silent no-op)
- `tasks.py` `_SONNET_SECTION_SYSTEM` (~285–418 tokens — silent no-op)

These require prompt expansion and restructuring that touches scoring invariants.
Schedule as a separate design task.

---

## 8. Invariant Checklist Before Going Live

Before any `cache_control` goes to production, verify:

- [ ] System prompt text is deterministic (no timestamps, no UUIDs, no random seeds)
- [ ] `json.dumps()` calls in system prefix use `sort_keys=True`
- [ ] Tool list for the call is static (same set every invocation)
- [ ] `cache_control` breakpoint is on the last block of the stable layer
- [ ] Dynamic content comes after ALL breakpoints
- [ ] `temperature` removed from all `claude-opus-4-7` calls
- [ ] `log_llm_spend` extended to capture `cache_creation_input_tokens` and
  `cache_read_input_tokens` before deploying Steps 3–4

---

## 9. Expected Economics

All figures assume current `claude-opus-4-7` pricing (₩15,000/1M input, ₩75,000/1M output).

### Step 3 — Opus coherence page-content caching

Opus coherence runs once per page per trigger cycle. Assume a page receives
3 triggers per day (section rewrite → coherence, research_ideas → coherence,
manual trigger).

| Item | Value |
|---|---|
| Page content size | ~15,500 tokens |
| Calls per day | ~3 |
| Without caching (3 × 15,500 × ₩15/1k) | ₩697 |
| With caching (1 write × 1.25 + 2 reads × 0.10) × 15,500 × ₩15/1k | ₩350 |
| Daily saving per page | ~₩347 |
| Monthly saving for 10 active pages | ~₩104,000 |

Write penalty on the first call (1.25× vs 1.00×) costs ~₩58 extra; recovered
after 1.2 subsequent hits.

### Step 1 (bug fix) — All Opus calls now actually run

The `temperature` bug means every Opus call across 5 sites silently 400s and
returns its fallback path (zero result / `opus_failed_open` / `{"error": ...}`).
Three pipelines are broken in production:
- `opus_judge_tick` — has produced zero-utility audit results every cycle
- `judge_idea_pool` / `research_ideas.opus_judge_pool` — every "Opus verdict"
  was actually `opus_failed_open`, i.e. blanket promotion with no Opus signal
- `opus_hero_refresh` (both copies) — has been returning `{"error": ...}` and
  never updating `wiki_pages.hero_tagline`

Fixing site 1 restores meaningful audit data. Fixing sites 2–5 restores Opus
input to idea promotion and hero refresh. Cost increases by the real Opus call
cost (currently paid for nothing); the system gains actual quality signal in
return.

---

## 10. Summary

| # | Action | File | Priority | Effort |
|---|---|---|---|---|
| S1 | Remove `temperature` from all 5 Opus call sites | judge_panel.py:76, auto_improvement.py:1959/2164, research_ideas/auto_improvement.py:2023/2241 | P0 | ~25 min |
| S2 | Extend `log_llm_spend` for cache token tracking | premium_dispatch.py | P1 | ~20 min |
| S3 | Cache page content in `_call_opus_coherence` | tasks.py:217 | P1 | ~30 min |
| S4 | Verify Sonnet judge cache hit rate; pad prompt if needed | judge.py | P2 | ~10 min + wait |
| S5 | Defer marker_embed and section_rewrite prompt caching | — | Backlog | — |
| Followup | Consolidate duplicate `opus_hero_refresh` definitions | auto_improvement.py vs research_ideas/auto_improvement.py | Backlog | TBD |

Steps S1 and S2 are prerequisites for S3 and S4. Deploy S1 first (P0 bug);
S2 can be batched with S3.
