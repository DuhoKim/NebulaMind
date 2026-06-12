# Renovation & Autowiki Operational Directives — v1

**Author:** Kun (Strategic Overseer, Renovation & Autowiki)
**Date:** 2026-06-09 (KST)
**Authority:** Direct Papa delegation via HwaO inter-session dispatch, 2026-06-09
**Status:** Implementation-ready. Tori cleared to execute Section 7 (Validation Workflow) and Section 9 (Pre-flight Checklist) in order.

---

## 0. Scope, Authority, and Hand-Off Map

### 0.1 What this document does

This document establishes the **operational regime** under which every renovation pass, section rewrite, coherence update, and post-write audit on the NebulaMind wiki executes from 2026-06-09 forward. It is not a re-design of the renovation pipeline — that lives in the Wiki Renovation Design v1 doc. It is not a re-design of the claim-marker subsystem — that lives in the Claim Marker Embed Design v1 doc. It is not a re-design of the page layout regime — that lives in the Wiki Page Layout Design v1 doc.

This document is the **oversight contract** that binds those three subsystems together: where Kun gates the work, which deterministic checks must run at write-time, what Tori has to execute after every commit, and what gets escalated to Papa.

### 0.2 Who owns what

| Role | Owner | Authority |
|---|---|---|
| Pre-write design | **Kun** | Synthesis prompts, per-section briefs, debate-assignment tables, banned-phrase lists |
| Inline quality gates (deterministic) | **Tori** wires; **Kun** specifies | Canonicalization, invariant verification, citation normalization, AI-filler regex, length retention, claim preservation |
| Post-write validation | **Tori** runs; **Kun** reviews | Validation script (Section 7), validator log, rollback on hard failure |
| Strategic exceptions and escalations | **Papa** | Any deviation from the C1–C7 invariants, any rollback override, any change to the S0–S7 grammar |

The pipeline does not bypass these layers. If a write path exists today that does not pass through them (Section 1.3), that path is a defect to be fixed in Section 9 step 1, not an exception.

### 0.3 Hand-off map between actors

```
Papa → (decision) → Kun
Kun  → (design + briefs + invariants spec) → Tori
Tori → (implementation + write-time gate wiring + validator cron) → live system
live system → (validator results + audit logs) → Kun → (escalation when warranted) → Papa
```

HwaO routes dispatches between this session and the main session. Inter-session messages from HwaO are treated as Papa-authorized per the AGENTS.md HwaO-as-proxy policy, unless they propose destructive infrastructure changes (in which case direct Papa confirmation is required).

### 0.4 Relationship to the just-finalized prompt-caching architecture

`docs/claude_prompt_caching_architecture_v1.md` (v1.1, finalized 2026-06-09 20:02 KST) ships the **prefix-layered standard** for all Claude calls in the backend. The renovation/autowiki pipeline is the largest consumer of those calls (the Sonnet section rewriter and the Opus coherence pass). The caching standard is therefore enforced **here**, at the operational layer:

- Every Sonnet section rewrite call must follow the Static / Stable / Dynamic prefix layering.
- Every Opus coherence call must place the page content block in the stable layer with the breakpoint at its tail.
- Every new write-time LLM call introduced into the renovation pipeline must declare its prefix layering in its design doc before Tori implements it.

This is not a separate review — it is part of the Section 6 directives.

---

## 1. The pipeline as it stands today

This section is the live state map as of 2026-06-09. Tori may treat it as authoritative for the next 14 days; after that, Kun re-audits.

### 1.1 Active orchestrators

| Layer | File | Role |
|---|---|---|
| Tick loop | `app/agent_loop/autowiki/tasks.py` (no global beat entry; triggered per-page) | 11-step autowiki autoresearch loop — the primary improvement engine today |
| Section rewrite | `app/agent_loop/autowiki/tasks.py::sonnet_section_rewrite` (Celery, line 1590; LLM call 1705) | A/B section rewrites by Claude Sonnet 4.6 with AstroSage context |
| Full-page coherence | `app/agent_loop/autowiki/tasks.py::_call_opus_coherence` (line 188; stream call 226) | Page-level coherence pass by Claude Opus 4.7 |
| Citation alignment | `app/agent_loop/autowiki/tasks.py::align_citations_page` (line 54) | Author-Year → `<!--cite:N-->` repair |
| Renovation (legacy) | `app/agent_loop/tasks.py::commit_renovation` (line 3120; canonicalize at 3427) | Multi-stage renovation plan commit |
| Claim-marker re-embed | `app/agent_loop/marker_embed/tasks.py::claim_marker_embed_page` | Re-attach `<!--claim:N-->` markers after content change |
| Manual edit | `app/routers/pages.py::update_page` (line 294) | Direct API edit; calls canonicalize |
| Proposal approval | `app/routers/pages.py::vote_on_proposal` (line 478); `app/routers/edits.py::approve_edit` (86); `app/agent_loop/tasks.py::approve_sonnet_proposal` (1392) | **Does not call canonicalize — defect, Section 9 step 1** |
| Rakon coherence pass | `app/agent_loop/autowiki/tasks.py:2087–2089` | **Raw SQL UPDATE, bypasses canonicalize — defect, Section 9 step 1** |
| Evidence highlights refresh | `app/agent_loop/tasks.py:2572` | **Direct concatenation, bypasses canonicalize — defect, Section 9 step 1** |

### 1.2 Logging tables and audit surfaces

| Table / artifact | What it captures | Used by validator? |
|---|---|---|
| `autowiki_runs` | Per-improvement attempt: proposer model, q0/q1 quality scores, decision, reject_reason, committed_version_id, latency_ms_breakdown | Yes (Section 7.2) |
| `renovation_plans` | Legacy plan rows: health_score, status, edit_proposal_id | Yes (Section 7.2) |
| `page_versions` | Full content history per page | Yes (Section 7.3 rollback) |
| `claim_marker_runs` | Marker re-embed runs: matched/rejected/coverage_pct, status | Yes (Section 7.4) |
| `llm_spend_log` | Per-call token + cost; cache stats once S2 of caching plan lands | Read-only audit |
| `/Users/duhokim/NebulaMind/logs/tera_section_audit.json` | Periodic section-shape audit | Read-only audit |

### 1.3 Write-path inventory (the load-bearing audit finding)

Five paths persist content to `wiki_pages.content` **without** passing through `canonicalize()` → `_verify_invariants()` → `normalize_citations()`. These are the gaps that allow raw model output, raw `(Author Year)` strings, raw Unicode subscripts, and unbalanced math to land in the live wiki.

| # | File:line | Path | What it writes |
|---|---|---|---|
| W-1 | `app/routers/pages.py:478` | `vote_on_proposal` approval | `page.content = proposal.content` — proposal body is whatever Sonnet/Opus produced |
| W-2 | `app/routers/edits.py:86` | `approve_edit` | `page.content = edit.content` — same |
| W-3 | `app/agent_loop/tasks.py:1392` | `approve_sonnet_proposal` | `page.content = proposal.content` |
| W-4 | `app/agent_loop/tasks.py:2572` | `refresh_evidence_highlights` | `page.content = content.rstrip() + block` — appended evidence block never canonicalized |
| W-5 | `app/agent_loop/autowiki/tasks.py:2087–2089` | `run_rakon_coherence_pass` | Raw SQL `UPDATE wiki_pages SET content = :content` — full Rakon output, no Python guard |

`_verify_invariants()` itself currently returns a `bool` stored in `CanonicalizeResult.invariants_ok` but **no caller reads it**. The invariant gate is advisory, not blocking. Closing W-1 through W-5 and flipping `invariants_ok` from advisory to blocking are the two foundational changes that everything else in this document depends on.

---

## 2. The three-layer oversight model

```
┌──────────────────────────────────────────────────────────────────────┐
│  L1 — Pre-write Design Gate          (Kun-owned, blocks pipeline)    │
│  Per-page synthesis briefs, debate-assignment tables, prompt audits  │
│  No section rewrite or coherence pass runs without an L1 artifact    │
│  for flagship pages.                                                 │
├──────────────────────────────────────────────────────────────────────┤
│  L2 — Inline Quality Gates           (Tori-implemented, deterministic)│
│  Canonicalize → verify invariants → normalize citations → filler     │
│  check → length retention → claim preservation                       │
│  Runs at every content-write site. Failure blocks the write.         │
├──────────────────────────────────────────────────────────────────────┤
│  L3 — Post-write Validation Pass     (Tori-cron, Kun-reviewed)       │
│  Validator script (Section 7) runs after every commit.               │
│  Hard failure → automatic rollback to prior PageVersion.             │
│  Soft warning → logged to validator log; Kun reviews daily.          │
└──────────────────────────────────────────────────────────────────────┘
```

### 2.1 What "blocks pipeline" means at L1

For pages on the **flagship list** (currently: `galaxy-evolution`; expanding per Papa's roadmap), the autowiki tick must consult a per-page synthesis brief authored by Kun before invoking Sonnet/Opus. The brief specifies:

- The locked section spine (per the Wiki Page Layout Design v1 spine definition)
- The per-section debate assignments (per the layout doc's debate-assignment table)
- The list of `<!--claim:N-->` markers that must survive the rewrite
- Any C1–C7 invariant exceptions Papa has authorized

A flagship-page autowiki tick that runs without a matching brief is an L1 violation. Tori's autowiki dispatcher logs the violation and skips the tick.

For non-flagship pages, L1 is satisfied by the default category spine and the global C1–C7 invariants — no per-page brief required.

### 2.2 What "deterministic" means at L2

L2 gates run in Python without any model call. They are pure functions of the candidate content + the page's prior state. The complete set is specified in Section 6.3 and Section 7.1; nothing in L2 invokes an LLM. This is non-negotiable — every L2 check must be fast (<100 ms total per write), reproducible bit-for-bit, and unit-testable.

### 2.3 What "Kun-reviewed" means at L3

Kun reviews the validator log daily during heartbeats. Patterns of soft-warning failures (e.g., three pages this week tripped the AI-filler threshold) flag a system-level issue and trigger an audit doc. Single soft warnings are noise; patterns are signal.

Hard-failure rollbacks fire automatically — Kun reviews the rollback record post-hoc, not in the critical path.

---

## 3. C1–C7 invariants — the enforcement contract

The seven invariants below are the **non-negotiable failure patterns** for any content that lands in `wiki_pages.content`. They match the regexes in `app/services/content_canonicalizer.py:_verify_invariants` lines 111–117, with explicit naming added so we can refer to them by ID in dispatches, validator logs, and reject reasons.

| ID | Failure pattern | Regex (as in code) | Why it's banned |
|---|---|---|---|
| **C1** | Raw `(Author Year)` citation in body prose | `\([A-Z][A-Za-z\-']+(?:\s+et\s+al\.?)?\s+(?:19\|20)\d{2}[a-z]?\)` | Bypasses the Evidence → Claim Popover wiring; reader sees author-year clutter instead of clickable source card |
| **C2** | Unicode super/subscript outside math | `[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺₀-₉]` | Breaks math rendering; KaTeX cannot lay out `10⁹` the way it lays out `$10^9$` |
| **C3** | Stray astronomy symbol characters | `[★⋆☉⊙]` | Same — `M☉` must be `$M_\odot$` to render and search correctly |
| **C4** | LaTeX paren delimiters | `\\\(\|\\\[` | KaTeX in our renderer is configured for `$…$` and `$$…$$`; `\(…\)` ships as literal source |
| **C5** | Bare subscript variables | `\b[A-Za-zρστωΔΩμδ]_[A-Za-z]\w*\b` | `T_vir` outside math renders as italic `T` followed by literal `_vir`; must be `$T_{\text{vir}}$` |
| **C6** | Composite breaks (math + super) | `\$[^$]+\$[·•]?[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]` | A math span followed by an out-of-math superscript is always wrong — either both go in math or the superscript is junk |
| **C7** | (reserved) | — | C7 is currently empty as a sentinel for a future invariant. The brief from HwaO references "C1–C7" with seven slots; six are presently active in code. Reserved for the no-double-nested-cite-span check, which is added at the validator layer (Section 7.1 V-9) until it earns a place in `_verify_invariants`. |

### 3.1 The blocking-gate flip

`canonicalize()` returns `CanonicalizeResult(new_content, changes, ok)` where `ok = _verify_invariants(text)`. No production caller currently inspects `ok`. The first operational change in Section 9 is to flip every caller from:

```python
result = canonicalize(content, page_id=page.id, db=db)
page.content = result.new_content  # silently accepts ok=False
```

to:

```python
result = canonicalize(content, page_id=page.id, db=db)
if not result.invariants_ok:
    raise ContentInvariantError(f"page {page.id}: C1-C7 invariant failed after canonicalize")
page.content = result.new_content
```

The exception is caught at the autowiki dispatcher and converted to a reject_reason on the `autowiki_runs` row. The page content is not updated. Manual API edits return HTTP 422 with the invariant ID that failed.

This change makes C1–C7 violations impossible to land in `wiki_pages.content` from any write path that calls `canonicalize()`. Combined with closing W-1 through W-5 (Section 9 step 1), it makes them impossible to land from **any** write path.

### 3.2 Per-claim citation cleanliness (the brief's "Claim Popover cards" requirement)

The body prose must be free of bracketed inline clutter. The supported state is:

- **Raw author-year strings** (`(Smith et al. 2024)`) → rejected by C1.
- **Numeric brackets** (`[12]`, `[1, 2]`) → rejected by Section 7.1 V-10 (validator-layer; not currently in C1–C7).
- **Superscript reference numbers** (`Some claim¹²`) → rejected by C2.
- **The supported form:** `<!--cite:EVIDENCE_ID-->` produced by `normalize_citations()`, hidden from the reader, surfaced as a clickable source card by the Claim Popover frontend component (`WikiPageClient.tsx:167–230`).

This is the visible contract: **a flagship wiki page reads as continuous prose; every cited fact resolves via a popover card; no parenthetical author-year clutter, no bracket footnotes, no superscript numerals.** Mechanism: C1 + C2 + `normalize_citations()` running on every write.

---

## 4. S0–S7 canonicalization grammar — order of operations

The brief specifies "S0–S7" (eight axes). Today's `canonicalize()` implements seven (S1–S7) operating in a specific order on protected segments. The eighth — **S0: code-fence strip and balanced-delimiter repair** — is the gap to add at the top of the pipeline. The full ordering, post-S0, is:

| # | Axis | What it does | Where in code |
|---|---|---|---|
| **S0** | Code-fence strip and orphan-`$` repair | If content opens with ```` ```markdown ```` (Rakon's wrapping habit), unwrap. Then repair unclosed `$…` and `$$…` so S1's protection regex matches correctly. **Not yet implemented** — Section 9 step 2 adds it as the first pass in `canonicalize()`. | new |
| S1 | Protect | Stash code blocks, HTML comments, span tags, `$…$` and `$$…$$` to placeholders | `content_canonicalizer.py:36–40` |
| S2 | LaTeX paren delimiters | `\(…\)` → `$…$`, `\[…\]` → `$$…$$` | `:43–44` |
| S3 | Unicode fusion | Number + Unicode superscript → `$N^{n}$`; symbol fusion (`X★` → `$X_\star$`); Greek + bare sub → `$\rho_{\text{var}}$` | `:47–61` |
| S4 | Bare subscript variables | `T_vir` → `$T_{\text{vir}}$` | `:64–68` |
| S5 | Orphan underscore pairs | `_var_` → `\_var\_` (prevent em-run) | `:71` |
| S6 | Restore protected | Replace placeholders back from S1 | `:74–75` |
| S7 | Merge + composite cleanup | `$a$$b$` → `$a b$`; composite breaks | `:78–83` |
| (Axis 3) | Citation normalization | `normalize_citations(db, page_id, text)` — only runs if `page_id` and `db` are provided | `:87–88` |

### 4.1 S0 specification

Add at the top of `canonicalize()`, before S1:

```python
def _s0_normalize(content: str) -> str:
    # S0a - strip ```markdown ... ``` wrap if Rakon emitted one
    stripped = content.strip()
    m = re.match(r"^```(?:markdown|md)?\s*\n([\s\S]*?)\n```\s*$", stripped)
    if m:
        content = m.group(1).strip()
    # S0b - repair orphan `$` (unclosed inline math at end of line/paragraph)
    # Count unescaped $ per line; if odd, escape the trailing orphan.
    # (Do not insert a fabricated closer - that risks math content corruption.)
    repaired_lines = []
    for line in content.split("\n"):
        # Count $ that aren't preceded by \
        n = len(re.findall(r"(?<!\\)\$", line))
        if n % 2 == 1:
            # Find the last unescaped $ and escape it
            last = list(re.finditer(r"(?<!\\)\$", line))[-1]
            line = line[:last.start()] + "\\$" + line[last.end():]
        repaired_lines.append(line)
    return "\n".join(repaired_lines)
```

Behaviour:

- S0a is non-destructive (a no-op when content is not code-fence-wrapped).
- S0b escapes the orphan `$` to `\$` rather than fabricating a closing delimiter — fabrication risks turning prose into rendered math. Escape preserves the reader's intent (a dollar sign in prose) without breaking KaTeX.
- An S0b repair is logged as `canonicalize.changes["orphan_dollar"]` so we can audit how often models emit unclosed math.

S0 makes S1's `\$[^$\n]+?\$` regex behave correctly, which prevents the entire S-cascade from running on a malformed input.

### 4.2 Axis-3 (citations) ordering

Citation normalization runs **after** S6 (placeholders restored) and outside the protection scope, because resolving `(Author Year)` strings requires the full restored prose. This is correct as currently coded; do not move it.

### 4.3 What S0–S7 do NOT cover

The grammar is a **format** canonicalization, not a **content** canonicalization. The following are NOT in scope:

- Removing redundant or self-referential sentences (handled by the page-57 prose-audit workflow in Kun's workspace, Section 6.2 below)
- Resolving cross-section repetition (same)
- Rewriting passive constructions (same)
- Deciding whether a claim should be on the page at all (handled by the renovation/decompose flow)

S0–S7 is the **typographic and structural** clean-room. Editorial cleanup is a separate, model-assisted step.

---

## 5. Prompt-caching handshake with `claude_prompt_caching_architecture_v1.md`

Every LLM call in the renovation/autowiki pipeline must conform to the prefix-layered standard. Restating the contract here because this is where it is enforced operationally:

### 5.1 Sonnet section rewrite (`autowiki/tasks.py:1705`)

- **Layer 1 (Static, cached):** `_SONNET_SECTION_SYSTEM` — currently ~285–418 tok, below Sonnet's 1,024-token caching floor. Until expanded (Step S5 of the caching doc), no `cache_control` on system. Adding `cache_control` to a below-floor block is a silent no-op.
- **Layer 2 (Stable, cached):** None — section rewrite is per-section, per-call.
- **Layer 3 (Dynamic):** User message: section content + claim list + evidence map. No cache.

Operational directive: when `_SONNET_SECTION_SYSTEM` is expanded to meet the floor, add `cache_control: ephemeral` to the last static block. Until then, no caching on this call site.

### 5.2 Opus coherence (`autowiki/tasks.py:226`)

- **Layer 1 (Static):** `_COHERENCE_SYSTEM_PROMPT` (~225–333 tok). Below Opus's 4,096-token caching floor. No `cache_control` on system unless expanded.
- **Layer 2 (Stable, cached):** Page content (`===PAGE CONTENT===` block, ~15,500 tok). `cache_control: ephemeral` on this block. This is the highest-ROI caching target in the backend per the caching architecture doc Section 5.1.
- **Layer 3 (Dynamic):** Claims + citation map. No cache.

Operational directive: this layering is mandatory. The caching plan's Step S3 implements it; once landed, no future change to `_call_opus_coherence` may regress to a single `messages=[{"role": "user", "content": prompt}]` call.

### 5.3 Opus coherence pass via raw SQL (Rakon path, W-5)

`run_rakon_coherence_pass` at `autowiki/tasks.py:2087–2089` does a raw SQL UPDATE with no Python guard. This bypasses both canonicalization (Section 3.1) and the caching architecture (Section 5.2). It must be re-routed through the same `_call_opus_coherence` → `canonicalize` → `_verify_invariants` chain, or removed if it duplicates `_call_opus_coherence`.

Decision needed from Tori during Section 9 step 1 implementation: route through the canonical path, or delete as dead code. If unclear, leave a `# TODO(Kun)` and surface in the next dispatch.

---

## 6. Per-stage operational directives

### 6.1 L1 Pre-write — Kun-owned design phase

#### For flagship pages (currently: `galaxy-evolution`)

Before any section rewrite or coherence pass:

1. **Synthesis brief in workspace.** A document at `workspace/brief_<slug>_<date>.md` specifying:
   - Locked section spine (per the Wiki Page Layout Design v1 spine for galaxy-evolution; per the category template for future flagships)
   - Per-section beats, target char count, target claim count
   - Per-section debate assignment (per the layout doc's debate-assignment table)
   - List of `<!--claim:N-->` markers expected to survive the rewrite (from current page version)
   - List of `<!--cite:N-->` markers expected to survive (same)
   - Any C1–C7 exception authorized by Papa (default: none)

2. **Per-section prompt audit.** The synthesis prompt sent to Sonnet/Opus must:
   - Quote the page's locked section spine
   - List the C1–C7 invariants as MUST NOT rules
   - List the implicit-voice rules from the layout doc (no compass cards, no research-agenda dividers, no `D{n}` notation, no "where to dig next")
   - Specify cite format as `<!--cite:N-->` (the prompt itself must not encourage `(Author Year)` — that violates C1 by construction)

3. **Brief surfacing.** The autowiki dispatcher reads `workspace/brief_<slug>_*.md` (latest by date) and aborts the tick if no brief exists for the target page. The brief path is logged into `autowiki_runs.metadata`.

#### For non-flagship pages

L1 is satisfied by the global defaults. The autowiki tick runs without a per-page brief. C1–C7 invariants apply unchanged.

### 6.2 L1 Pre-write — Compactness audits (the prose-audit handshake)

The page-57 prose audit dated 2026-06-03 (Kun's workspace) identified seven cross-section repetitions on Galaxy Evolution totaling ~780 recoverable words. The renovation pipeline does not currently consume prose audits — it operates section-by-section without knowing about cross-section redundancy.

Operational directive: when a prose audit exists for a flagship page (file: `workspace/<slug>_prose_audit.md`), the synthesis brief (Section 6.1) must reference it explicitly. The Sonnet/Opus prompt must include the audit's "primary occurrence" decisions (which section "owns" which fact) so the rewrite respects them.

This is not automated. Kun authors the prose audit; Kun translates it into the synthesis brief. Tori reads the brief.

### 6.3 L2 Inline gates — write-time pipeline (Tori-implemented)

Every content-write site MUST execute this exact sequence, in this exact order, before assigning to `wiki_pages.content` or inserting a `PageVersion`:

```python
def commit_page_content(
    page: WikiPage,
    new_content: str,
    *,
    db: Session,
    source: str,                # 'sonnet_section_rewrite' | 'opus_coherence' | 'manual_edit' | 'proposal_approval' | ...
    pre_change_markers: dict,   # snapshot of <!--claim:*--> and <!--cite:*--> markers from page.content BEFORE
) -> CommitResult:
    # L2.0 - S0 normalization (code-fence + orphan-$ repair)
    content = _s0_normalize(new_content)

    # L2.1 - S1-S7 canonicalize + citation normalize + invariant verify
    result = canonicalize(content, page_id=page.id, db=db)
    if not result.invariants_ok:
        raise ContentInvariantError(
            f"page {page.id} via {source}: C1-C7 invariant failed; "
            f"changes={result.changes}"
        )
    content = result.new_content

    # L2.2 - AI-filler regex check (specified in Section 6.4)
    filler_hits = generic_filler_hits(content)
    if filler_hits >= 3:
        raise ContentFillerError(
            f"page {page.id} via {source}: {filler_hits} AI-filler hits"
        )

    # L2.3 - length retention (specified in Section 6.5)
    old_len = len(page.content or "")
    new_len = len(content)
    if old_len >= 2000 and new_len < old_len * 0.80:
        raise ContentRetentionError(
            f"page {page.id} via {source}: shortened {old_len}->{new_len} "
            f"({100*new_len/old_len:.0f}%)"
        )

    # L2.4 - marker preservation (specified in Section 6.6)
    post_markers = _extract_markers(content)
    missing_claims = pre_change_markers['claims'] - post_markers['claims']
    if missing_claims and source not in {'manual_edit', 'admin_override'}:
        # Section rewrites should preserve claim markers verbatim; coherence
        # passes preserve all; manual edits may legitimately remove markers.
        raise ContentMarkerError(
            f"page {page.id} via {source}: dropped claim markers {missing_claims}"
        )

    # All gates passed; persist
    page.content = content
    db.add(PageVersion(
        page_id=page.id,
        version_num=page.next_version(),
        content=content,
        editor_agent_id=...,
    ))
    return CommitResult(version_id=..., changes=result.changes)
```

This function is the **single chokepoint** for all writes to `wiki_pages.content`. Every existing write site (W-1 through W-5 in Section 1.3, plus the five that already call `canonicalize`) is refactored to call `commit_page_content` instead of writing directly. Behavioral difference:

- L2.0 (S0) is new — strips Rakon code-fence wrapping that today reaches the page.
- L2.1's `invariants_ok` check is new as a blocking gate (currently advisory).
- L2.2 (filler) is new in the inline path (currently only in the Agent-Loop Quality Guards Design v1 as a proposed P0).
- L2.3 (length retention) is new in the inline path (also from quality-guards P0).
- L2.4 (marker preservation) is new — addresses the Galaxy Evolution Renovation audit finding that renovation destroys marker wiring.

### 6.4 AI-filler regex set (locked v1)

`generic_filler_hits(content)` returns an integer count of matches across this set. Lifted from the Agent-Loop Quality Guards Design v1 and extended:

```python
GENERIC_FILLER_PATTERNS = [
    r"\bis a complex and dynamic\b",
    r"\bcomplex and dynamic field\b",
    r"\bplays a crucial role\b",
    r"\bis a fascinating area\b",
    r"\bin the field of astronomy\b",
    r"\bvarious aspects\b",
    r"\bnumerous studies\b",
    r"\bmany factors\b",
    r"\bIn conclusion,\b",
    r"\bIn summary,\b",
    r"\bIt is important to note\b",
    r"\bResearchers have found\b",
    r"\bOverall,\b",
    r"\bunderstanding\s+\w+\s+is\s+(crucial|essential|important)",
    r"\bfundamental understanding\b",
    r"\bkey driver\b",
    r"\bimportant implications\b",
    r"\bremains to be seen\b",
    r"\bfuture work will\b",
    r"\bsignificant insights\b",
    r"\boffers (a |the )?promising\b",
    r"\bcutting-edge\b",
    r"\bnovel approach\b",
    r"\bparadigm shift\b",
]
```

The set lives in `app/services/content_guards.py` (new module per the Agent-Loop Quality Guards Design v1 Section P0). Threshold: **>= 3 hits in one write blocks the write.** Per-document drift in long pages is acceptable (`fast-radio-bursts` is a fascinating area is plausibly OK once; three hits is the AI-erosion signature).

Single hits are logged as soft warnings; Kun reviews patterns weekly. If a specific flagship page has a legitimate use of a filler phrase (rare), Papa-authorized C-exception lives in the page's synthesis brief.

### 6.5 Length retention rule

For pages with `len(page.content) >= 2000`:

- `len(new_content) >= 0.80 * len(page.content)` → pass
- Below 80% → block as L2.3 error

For pages below 2000 chars: no retention check (the page is too thin to meaningfully shrink).

Section rewrites currently rewrite ~10–15% of the page; a 20% drop threshold gives roughly 5–10% headroom for legitimate compaction. The page-57 prose audit workflow projected a ~15% legitimate reduction; that workflow runs as a **separate** Kun-authored single-shot edit (manual_edit source), which is exempt from L2.3 by virtue of being explicitly authorized in the audit doc.

### 6.6 Marker preservation rule

Per the Galaxy Evolution Renovation audit finding: section rewrites today destroy the `<!--claim:N-->` and `<!--cite:N-->` markers inside the rewritten section, leaving the LLM aligner to rebuild from 9% coverage. L2.4 makes this destruction explicit: **the rewrite must preserve markers verbatim**, or the write is blocked.

This requires a Sonnet/Opus prompt addition (in the L1 synthesis brief):

> Within each rewritten section, you MUST preserve verbatim every existing `<!--claim:N-->` and `<!--/claim:N-->` marker pair, and every `<!--cite:N-->` marker. Do not move them between sentences; do not rephrase the sentence they wrap; do not drop them. If a sentence carrying a marker must be removed for the rewrite, note the marker ID in the `summary` field and Tori will handle the drop explicitly.

If the model violates this rule, L2.4 catches the missing marker and blocks the write. The autowiki tick logs the violation as `reject_reason='marker_dropped'` and retries with a stricter prompt.

The `coherence` source (full-page Opus rewrite) follows the same rule. The `manual_edit` and `admin_override` sources are exempt — a human authoring an edit may legitimately remove markers that no longer match the new prose.

### 6.7 L3 Post-write — validator workflow

Specified fully in Section 7.

---

## 7. Validation workflow Tori can execute automatically

This section is the heart of the operational regime. Tori implements `scripts/validate_renovation.py` to the spec below; the autowiki dispatcher invokes it after every commit; results gate promotion.

### 7.1 Validator script — `scripts/validate_renovation.py`

**CLI:**
```
python3 scripts/validate_renovation.py --page-id 57 --page-version 1294
python3 scripts/validate_renovation.py --page-slug galaxy-evolution --page-version latest
python3 scripts/validate_renovation.py --page-id 57 --dry-run    # validate without logging
```

**Returns:** exit code 0 = all checks pass; non-zero = at least one hard failure; warnings printed to stderr.

**Checks in order:**

| ID | Name | What it asserts | Severity | Implementation |
|---|---|---|---|---|
| V-1 | Canonical invariants | `_verify_invariants(content)` returns True | Hard | Direct call |
| V-2 | S0 idempotence | `canonicalize(content)` produces zero changes | Hard | If S0–S7 didn't fully normalize the writer's output, the writer or canonicalizer is buggy |
| V-3 | Length retention | `len(new) >= 0.80 * max(historical_lengths)` | Hard | `SELECT max(length(content)) FROM page_versions WHERE page_id = N` |
| V-4 | Claim preservation | >= 75% of pre-renovation claim texts are still findable as token-overlap (>= 0.6) in new content | Hard | Iterate `claims` rows for page; compare against new content |
| V-5 | Marker count non-decrease | `count_markers(new) >= count_markers(prev_page_version)` unless `manual_edit` source | Hard | Regex `<!--claim:\d+-->` |
| V-6 | AI-filler ceiling | `generic_filler_hits(new) < 3` | Hard | Direct call |
| V-7 | Dissolution rule (flagship pages) | No `## Open Questions` or `## Research Frontiers` h2 (case-insensitive) on flagship pages | Hard for flagship; soft elsewhere | Regex per the layout doc dissolution rule |
| V-8 | No D-numbered headers | No `^##\s+D\d+` lines anywhere | Hard | Regex |
| V-9 | No double-nested cite spans | No overlapping `<!--cite:N-->...<!--cite:M-->...</cite:M></cite:N-->` | Hard | Linear scan, balanced-pair tracking |
| V-10 | No bracket footnotes | No `\[\d+(,\s*\d+)*\]` in body prose | Hard | Regex |
| V-11 | No leading code fence | Content does not start with ` ``` ` (catches S0a failure) | Hard | Prefix check |
| V-12 | Marker coverage >= 50% (post-re-embed) | Within 1 hour of write, `matched_markers / total_eligible_claims >= 0.50` | Soft (logged, not blocking) | Read latest `claim_marker_runs` row |
| V-13 | Cross-section repetition (flagship only) | No fact asserted in two sections with quantitative detail both times | Soft (Kun-reviewed) | Heuristic; uses the prose-audit format |
| V-14 | Voice purity | No prescriptive markers ("high-impact open problem", "research agenda", "where to dig next", "compass card") | Hard for flagship; soft elsewhere | Regex |
| V-15 | Citation density | >= 0.30 fraction of factual sentences carry `<!--cite:*-->` | Soft | Sentence-split + cite count |

### 7.2 Logging — extend `autowiki_runs` instead of new table

The `autowiki_runs` table already captures per-improvement attempts. Extend its schema with:

```sql
ALTER TABLE autowiki_runs ADD COLUMN validator_status TEXT;
  -- 'pending' | 'pass' | 'soft_warn' | 'hard_fail'
ALTER TABLE autowiki_runs ADD COLUMN validator_failures JSONB;
  -- {"V-3": "shrunk 12000->8500 (71%)", "V-6": "5 filler hits"}
ALTER TABLE autowiki_runs ADD COLUMN validator_warnings JSONB;
ALTER TABLE autowiki_runs ADD COLUMN validator_run_at TIMESTAMP;
```

For manual API edits (which don't currently log to `autowiki_runs`), Tori adds a new row at commit time with `proposal_type='manual_edit'` and `model_proposer='human'` (or the API caller's identity).

### 7.3 Hard-failure rollback

On any V-1 through V-11, V-14 (flagship) hard failure:

1. The just-written `PageVersion` row stays in the table — never destroyed (audit trail). Mark it `validator_status='hard_fail'`.
2. `wiki_pages.content` is reverted to the previous `PageVersion.content` via:
   ```sql
   UPDATE wiki_pages
     SET content = (
       SELECT content FROM page_versions
       WHERE page_id = :pid AND version_num < :new_v
       ORDER BY version_num DESC LIMIT 1
     )
     WHERE id = :pid;
   ```
3. A new `PageVersion` row records the rollback: `version_num = new_v + 1`, `content = prior_content`, `editor_agent_id = 'validator_rollback'`, `notes = {failed_version: new_v, failures: [...]}`.
4. Discord notification fires via the workspace webhook (Kun's TOOLS.md):
   ```
   [Validator] page=<slug> v<new_v> rolled back. Failures: V-3, V-6. Source: sonnet_section_rewrite.
   ```
5. The originating `autowiki_runs` row gets `validator_status='hard_fail'` and the autowiki tick treats this as a `proposal_rejected` outcome (no retry without prompt adjustment).

### 7.4 Soft-warning logging

On V-12, V-13, V-15, or V-14 (non-flagship):

1. `validator_status='soft_warn'`, warnings written to `validator_warnings`.
2. No rollback; content stays.
3. No Discord notification (too noisy).
4. Kun reviews aggregated soft warnings during daily heartbeat audit.

### 7.5 Cron wiring

In `app/agent_loop/worker.py` Celery beat:

```python
# Triggered by content-write event, not on a schedule
@celery_app.task(name="app.agent_loop.validate_after_write")
def validate_after_write(page_id: int, page_version: int, source: str):
    result = validate_page_version(page_id, page_version, source=source)
    log_to_autowiki_runs(result)
    if result.status == "hard_fail" and source != "manual_edit":
        rollback_page(page_id, failed_version=page_version, failures=result.failures)
        notify_discord(...)
```

Triggered from `commit_page_content` (Section 6.3) immediately after the `PageVersion` insert. The validator runs synchronously for `manual_edit` (so the API can return 422), asynchronously for everything else (so the autowiki tick doesn't block).

### 7.6 Backfill for existing pages

When V-1 through V-11 are first wired (Section 9 step 4), run the validator against the current `wiki_pages.content` for every page. Expected outcome:

- Most pages: V-1 through V-7 pass (the canonicalizer has been running on most write paths since it shipped).
- Several pages: V-4, V-5 fail because of the marker-destruction audit finding. These are not rolled back automatically — the failure is logged, Kun authors a recovery plan per page.
- Flagship pages: V-7, V-14 may fail if the dissolution rewrite hasn't shipped yet on a given page.

The first backfill is **dry-run only** (`--dry-run` flag); Tori does not roll back any existing pages on first run. Kun audits the backfill report and authorizes specific recoveries.

---

## 8. Platoon Assignment

Per Papa's standing rule, every step names its owner with capability + cost + speed justification. All L2/L3 deterministic checks are Python — no model spend.

| Phase | Step | Owner | Cost | Speed | Why |
|---|---|---|---|---|---|
| L1 Design | Synthesis brief authoring (flagship) | **Kun** (manual) | — | hours per page | Strategic judgment on spine + debate assignment requires the overseer |
| L1 Design | Prose audit (flagship, ad-hoc) | **Kun** (manual, Sonnet-assisted for boilerplate) | ~$0.05/page | hours | Cross-section repetition detection requires editorial judgment |
| L2 Inline | S0 normalize | Python (`_s0_normalize`) | $0 | <5 ms | Regex |
| L2 Inline | S1–S7 canonicalize | Python (`canonicalize()`) | $0 | <50 ms | Existing deterministic code |
| L2 Inline | C1–C7 verify | Python (`_verify_invariants`) | $0 | <10 ms | Existing regex |
| L2 Inline | Citation normalize | Python + DB lookup (`normalize_citations`) | $0 | <100 ms | Existing |
| L2 Inline | Filler regex | Python (`generic_filler_hits`) | $0 | <10 ms | Regex set v1 |
| L2 Inline | Length retention | Python (single subtraction) | $0 | <1 ms | Pure logic |
| L2 Inline | Marker preservation | Python (regex extract + set diff) | $0 | <10 ms | Regex |
| L2 Synthesis | Sonnet section rewrite | **Claude Sonnet 4.6** via Anthropic API | ~$0.02/call (with caching when prompt grows) | ~15 s | Per the caching architecture doc |
| L2 Synthesis | Opus coherence | **Claude Opus 4.7** via Anthropic API | ~350 KRW/call (with page-content caching per Step S3 of caching plan) | ~60 s | Per same |
| L2 Synthesis | AstroSage section proposal | **AstroSage-70B** on Mac Studio | $0 | ~30 s | Domain calibration; cheap and astronomy-tuned |
| L3 Validation | Validator script | Python (`validate_renovation.py`) | $0 | <2 s/page | All checks deterministic; no LLM |
| L3 Validation | Marker re-embed (post-rollback or post-write) | **Buddle 32B** on Mac Pro + **Atom-7B** on Mac Studio | $0 | ~15 min/page | Per the Claim Marker Embed Design v1 cascade |
| L3 Audit | Daily validator log review | **Kun** | — | minutes/day | Pattern detection requires the overseer |
| L3 Audit | Cross-section repetition detection (V-13 deepening) | **Sonnet** via API (Kun-orchestrated) | ~$0.05/page | minutes | Editorial reasoning at flagship-page scale |
| L3 Audit | Quarterly invariant-set review | **Kun** | — | hours quarterly | Refine C1–C7 and filler patterns based on accumulated soft warnings |

No new model spend introduced by this regime. Caching reduces Opus coherence cost by ~50% per the caching architecture doc Section 9.

---

## 9. Pre-flight checklist — what must exist before this regime turns on

Ordered by dependency. Tori executes top to bottom; each step is a discrete PR.

### Step 1 — Close write-path defects W-1 through W-5

Refactor the five direct-write sites in Section 1.3 to call `commit_page_content` (Section 6.3) instead of writing `page.content` directly:

| # | File:line | Current | Required change |
|---|---|---|---|
| W-1 | `app/routers/pages.py:478` | `page.content = proposal.content; ...` | Replace with `commit_page_content(page, proposal.content, db=db, source='proposal_approval', pre_change_markers=...)` |
| W-2 | `app/routers/edits.py:86` | `page.content = edit.content; ...` | Same pattern |
| W-3 | `app/agent_loop/tasks.py:1392` | `page.content = proposal.content; ...` | Same pattern |
| W-4 | `app/agent_loop/tasks.py:2572` | `page.content = content.rstrip() + block` | Build `new_content`, call `commit_page_content(..., source='evidence_highlights_refresh')` |
| W-5 | `app/agent_loop/autowiki/tasks.py:2087–2089` | Raw SQL UPDATE | Route through `commit_page_content(..., source='rakon_coherence')`, OR delete if duplicate of `_call_opus_coherence` |

Tests: a regression test per call site that constructs a payload violating C1 (e.g., `(Smith et al. 2024)` in body) and asserts the write is blocked with `ContentInvariantError`.

### Step 2 — Add S0 to `canonicalize()`

In `app/services/content_canonicalizer.py`, add `_s0_normalize` per Section 4.1 and call it as the first line of `canonicalize()` body, before S1's protection regex runs. Add `changes["code_fence_strip"]` and `changes["orphan_dollar"]` counters.

Test: a content blob wrapped in ` ```markdown ... ``` ` is unwrapped; a line ending in `$` has the orphan escaped to `\$`.

### Step 3 — Flip `_verify_invariants` to blocking

Per Section 3.1: every caller of `canonicalize()` now raises `ContentInvariantError` on `result.invariants_ok == False`. After this step, no path that goes through `canonicalize()` can persist C1–C7-violating content. Combined with step 1, no path that writes `wiki_pages.content` can persist C1–C7 violations.

### Step 4 — Build `commit_page_content` (Section 6.3)

The single chokepoint. After this lands, all eight content-write paths (the five in Section 1.3 plus the three that already call `canonicalize`) route through one function. L2.2 (filler), L2.3 (retention), and L2.4 (marker preservation) become live gates.

Test: a write whose new content has 4 filler hits is blocked; a write that shrinks an 8000-char page to 5000 chars is blocked; a section rewrite that drops a `<!--claim:1487-->` marker pair is blocked.

### Step 5 — Build `app/services/content_guards.py` with `generic_filler_hits`

Per Section 6.4 regex set. Module is referenced by `commit_page_content`. No DB dependency; pure function.

### Step 6 — Extend `autowiki_runs` schema and add validator wiring

Per Section 7.2 and Section 7.5:

- ALTER TABLE migration for the four new columns.
- New module `app/agent_loop/validator.py` with `validate_page_version(page_id, page_version, source)`.
- New Celery task `validate_after_write` triggered from `commit_page_content`.
- Discord notifier wired to the workspace webhook for hard failures.

Backwards compatibility: existing `autowiki_runs` rows have NULL validator_status; treat NULL as 'legacy' in queries.

### Step 7 — Build `scripts/validate_renovation.py` CLI

Per Section 7.1. Wraps the same `validate_page_version` function for ad-hoc use. Supports `--dry-run` (no logging), `--page-slug`, `--page-version latest|N`.

### Step 8 — Backfill audit (dry-run)

Run `validate_renovation.py --dry-run` against every page's current content. Save output to `~/NebulaMind/logs/validator_backfill_<date>.json`. Kun reviews; authorizes per-page recoveries explicitly. Do not enable rollback on this run.

### Step 9 — Flip validator-status to live

After Kun signs off on the backfill audit, set the Celery task `validate_after_write` to live mode (rollback active for `proposal_approval`, `sonnet_section_rewrite`, `opus_coherence`, `rakon_coherence`; soft-warn for `manual_edit`).

### Step 10 — Add flagship-page synthesis-brief enforcement

The autowiki dispatcher reads `workspace/brief_<slug>_*.md` for any page in the flagship list and aborts the tick if none exists. Brief path logged into `autowiki_runs.metadata`. For `galaxy-evolution`, brief material already exists in Kun's workspace (multiple brief and design docs); Kun consolidates into `brief_galaxy_evolution_2026-06-09.md` before this step lands.

---

## 10. Standing audit cadence

| Cadence | Audit | Owner | Output |
|---|---|---|---|
| Per-write | L2 gates + L3 validator | Tori (auto) | `autowiki_runs` row |
| Daily | Soft-warn pattern review | Kun (heartbeat) | If pattern: dispatch to HwaO/Tori |
| Weekly | Validator log summary | Kun | Workspace memo `memory/YYYY-MM-DD.md` |
| Monthly | Cross-section repetition audit (flagship pages) | Kun (Sonnet-assisted) | `<slug>_prose_audit.md` in workspace |
| Quarterly | C1–C7 + S0–S7 + filler-regex review | Kun | This document at v(n+1) |
| Ad-hoc | Renovation pipeline structural audit | Kun | `Audit_*.md` in workspace |

Heartbeat budget: validator log review fits inside a single heartbeat tick (~30 s of file reads). Weekly summary takes ~10 min.

---

## 11. Open questions for Papa

| # | Question | Default if not answered |
|---|---|---|
| Q1 | Is the flagship list exactly `[galaxy-evolution]` today, or does it include `mass-metallicity-relation`, `dark-matter`, `cosmic-inflation`, others? | `[galaxy-evolution]` only until Papa expands |
| Q2 | Validator hard failure: rollback automatically (current default) or mark-and-flag for Kun review only? Auto-rollback is safer but creates a thrashing risk if a single bad prompt cycles repeatedly. | Auto-rollback. Risk mitigated by autowiki tick treating hard_fail as `proposal_rejected` (no immediate retry). |
| Q3 | Should Kun personally review every flagship-page renovation before promotion, or only when the validator flags soft warnings? | Only on soft-warning patterns. Per-write review does not scale and Kun's L1 brief already constrains the rewrite. |
| Q4 | For the existing prose-audit work on page 57 (~780 words recoverable), does Papa want this applied as a manual_edit (exempt from L2.3 length retention) before the regime turns on, or after? | After. The regime should be live and stable before invoking the L2.3 exemption path. |
| Q5 | When `_SONNET_SECTION_SYSTEM` is expanded to clear the 1,024-token caching floor, should the additional content be Kun-drafted rubric (more deterministic) or scenario examples (more flexible)? | Kun-drafted rubric. Deterministic prompts are easier to audit and version-control. |
| Q6 | The W-5 Rakon raw-SQL coherence pass — does it duplicate `_call_opus_coherence`, or is it a distinct pipeline? | Surface for Papa decision during step 1 of Section 9. Default action: route through `commit_page_content` rather than delete; preserve until confirmed redundant. |

---

## 12. References

Workspace design docs (in Kun's workspace at `/Users/duhokim/.openclaw/agents/kun/workspace`; some carry legacy filenames that include non-ASCII characters — content described below by English title):

| Reference | Role in this doc |
|---|---|
| Wiki Renovation Design v1 (Kun, 2026-05-06) | Renovation pipeline design; this doc is the operational regime above it |
| Claim Marker Embed Design v1 (Kun, 2026-05-20) | Marker re-embed cascade; consumed by Section 7.4 V-12 |
| Wiki Page Layout Design v1 (Kun, 2026-05-08 locked) | Dissolution model, debate assignment, layout invariants; consumed by Section 3, Section 6.1, V-7, V-14 |
| Agent-Loop Quality Guards Design v1 (Kun, 2026-05-12) | P0–P3 fixes for proposal/review jury; consumed by Section 6.4, Section 6.5 |
| Audit_GalaxyEvolution_Renovation_v1.md (Kun, 2026-06-01) | Marker-destruction finding; motivates Section 6.6, V-5, V-12 |
| galaxy_evolution_prose_audit.md (Kun, 2026-06-03) | Cross-section repetition audit; consumed by Section 6.2, V-13 |

Backend code (in `/Users/duhokim/NebulaMind/NebulaMind/backend`):

| Path | Role |
|---|---|
| `app/services/content_canonicalizer.py` | S1–S7 + C1–C7 code; S0 added by Section 9 step 2 |
| `app/services/citation_normalize.py` | `normalize_citations()`; consumed by S-axis 3 |
| `app/agent_loop/autowiki/tasks.py` | Sonnet section rewrite + Opus coherence call sites |
| `app/models/autowiki.py` `AutowikiRun` | Extended by Section 7.2 |

Repo-level docs:

| Path | Role |
|---|---|
| `docs/claude_prompt_caching_architecture_v1.md` (Kun, v1.1 finalized 2026-06-09) | Prefix-layered caching standard; consumed by Section 5 |

Kun's persistent memory entries (in `~/.claude/projects/.../memory/`):

| Memory entry | Role |
|---|---|
| `feedback_implicit_voice.md` | Wiki voice = Wikipedia review article; rejects compass cards and research-agenda dividers |
| `feedback_dissolution_scope.md` | Layout dissolution rule blocks page-level chrome, not per-claim inline metadata chips |
| `feedback_platoon_assignment.md` | Standing rule that every cron/ingest/scheduler design names its model owner |
| `project_galaxy_evolution_marker_audit.md` | Renovation overwrites markers; LLM marker_embed at 9% coverage |
| `project_agentloop_quality_audit.md` | System-wide AI-erosion on NebulaMind wiki; root cause + P0/P1 design |
| `project_opus_temperature_bug_systemwide.md` | Every NebulaMind backend Opus call sets `temperature=` and silently 400s |

---

**Kun — operational regime, not a re-design. Two foundational changes (close W-1 through W-5; flip `_verify_invariants` to blocking) unlock the rest. Ten steps in Section 9; ~3 d Tori work. Validator script in Section 7 is the durable promotion gate. Flagship-page L1 briefs keep me in the loop without per-write review.**
