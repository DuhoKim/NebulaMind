# Wiki Rendering & Citation System — Root Cause Audit and Overhaul Design v1

**Author:** Kun
**Date:** 2026-06-11
**Status:** Design for Tori implementation (design-only; no code changed during this audit)
**Supersedes:** the patch-level guidance in `math_and_citation_rendering_architecture_v1.md` §6–7 where they conflict. The 2026-06-10 historical-correction header of that document (badges-only citation display) is carried forward here as a hard invariant.
**Live grounding:** every claim below was verified against the running system on 2026-06-11 (Mac Studio): Postgres `wiki_pages` row for `galaxy-evolution` (page 57, 50,722 chars), `backend/app/services/content_canonicalizer.py`, `backend/scripts/align_citations.py`, `backend/app/routers/pages.py` + `edits.py`, `backend/app/agent_loop/tasks.py` + `autowiki/tasks.py`, `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` + `markdownNormalize.ts`, git status of the repo, and the running `next start` process.

---

## 1. Executive summary

The recurring rendering failures are not five independent bugs. They are the visible surface of **four structural defects**:

1. **No single write chokepoint.** 26 distinct `page.content =` assignment sites exist in the backend; only ~5 run the canonicalizer. Approval paths and ad-hoc scripts write raw text straight into the DB.
2. **The frontend mutates content instead of rendering it.** `WikiPageClient.tsx` runs a 5-stage regex rewrite pipeline (including a port of the backend canonicalizer) on every render. One of those stages — the claim-body entity escaper — actively **corrupts clean canonical content**: it is the live, reproducible origin of both the `&gt;`-in-prose symptom and most "raw LaTeX leaked" sightings.
3. **Whitelist-based escaping guarantees whack-a-mole.** The claim-body escaper protects a hardcoded list of known-good patterns and escapes everything else. Every new marker type, math edge case, or HTML fragment that enters a claim body becomes a new visible leak until someone adds it to the whitelist. The system is structurally reactive.
4. **No deployment or regression discipline.** The canonicalizer, `markdownNormalize.ts`, and `CITATION_POLICY.md` are all **untracked in git** (the repo has 360 dirty/untracked files). The frontend is served by `next start` from a production build — source fixes do nothing until someone rebuilds and restarts. There is no test that renders a fixture page and asserts "no superscripts, no References, no literal `&gt;`, no raw `\sim`". So fixes are unverifiable, undeployed-by-default, and unprotected against reintroduction.

The overhaul: define a **stored-content contract**, enforce it at a **single ORM-level chokepoint**, demote the frontend to a **pure renderer** (zero text mutation), and pin every symptom class with a **regression test**. Sections 4–6 give the concrete design; section 7 the migration order; section 8 the test matrix.

---

## 2. Pipeline trace (current state)

```
WRITERS                                        STORAGE                    READ              RENDER (client)
─────────────────────────────────────────      ────────────────────      ─────────────     ──────────────────────────────
A. Renovation synthesis  tasks.py:3427  ──┐                                                stripLeadingH1
   (canonicalized at proposal creation)   │                                                unwrapCodeFence
B. Autowiki tick  autowiki/tasks.py:1286, │                                                normalizeMarkdown      (≈ canonicalizer port)
   :1825 (canonicalized)                  ├──>  wiki_pages.content  ──>  GET /api/pages ─> renderCitationMarkers  (comments → spans)
C. PUT /api/pages  pages.py:296 (canon.)  │     (markdown + marker        /{slug}          wrapClaimComments      (comments → spans + ESCAPER)
D. Proposal approve  pages.py:480 (canon.)│      comments + $math$)       (verbatim,       ReactMarkdown
E. Agent-loop approve  tasks.py:1393 RAW  │                                no transform)      remarkMath → rehypeRaw → rehypeKatex
F. Vote auto-approve  edits.py:86  RAW    │
G. Evidence-highlights append             │
   tasks.py:2573  RAW                     │
H. ~14 ad-hoc scripts (commit_renovation, │
   astrosage_galev_*, inject_jwst_claims, │
   relink_unmatched, fix_headings, …) RAW ┘
```

Read path is clean: `GET /api/pages/{slug}` (pages.py:163-206) returns `page.content` byte-for-byte; no serialization transform. **All malformation either rests in the DB (writers E–H) or is created at render time (the frontend mutation stack).** This split is the diagnostic key for every symptom below.

---

## 3. Root cause map per symptom class

### 3.1 Citation display regression (superscripts / References reappearing)

**Layer of origin: design-doc + process, not code.**

- `math_and_citation_rendering_architecture_v1.md` (2026-06-09, §1) explicitly specified "always rendering inline citations as numbered superscripts `[1]…[n]`" — in direct conflict with Papa's 2026-05-21 badges-only directive. Tori implemented what the doc said (`citationRenderer.ts`, since deleted); Papa objected; revert; the doc stayed wrong until the correction header was added 2026-06-10. The "regression" was the system faithfully executing a stale spec.
- Two copies of `CITATION_POLICY.md` exist (`frontend/CITATION_POLICY.md` and `frontend/src/app/wiki/CITATION_POLICY.md`) and can drift.
- Nothing machine-checks the policy. No test renders a page and asserts the absence of `<sup>[n]</sup>` or a `References` heading. A policy that only exists as prose will be re-violated by the next implementer (human or LLM) who reads the wrong doc.
- Deployment opacity compounds it: with `next start` serving a static build (current BUILD_ID built 2026-06-11 00:31), a source-level fix is invisible until rebuild, and a rebuild from a stale or manually-reverted working tree resurrects old behavior. With zero git history for these files there is no authoritative "current" version to rebuild from.

**Stored content is currently clean of this class:** page 57 has no `[n]` markers and no `References` section (verified by pattern scan).

### 3.2 Raw LaTeX leaking into prose (`\sim`, `\gtrsim`)

**Layers of origin: frontend escaper (primary, recurring) + missing write-time invariant (secondary).**

- **Primary mechanism (live, reproducible):** `wrapClaimComments` (WikiPageClient.tsx:120-148) entity-escapes `<` and `>` inside claim bodies — *including inside `$...$` math*. `$M_\mathrm{BH} > 10^7$` inside a claim span becomes `$M_\mathrm{BH} &gt; 10^7$`. remark-math hands the literal `&gt;` to KaTeX; KaTeX errors on `&` (alignment char); with `throwOnError: false` it renders the raw TeX source as visible text. **To the reader this is "raw LaTeX leaked".** The DB content was correct the whole time. Page 57 today contains 14 math segments with `<`/`>`, one currently inside a claim span (`$>700,000$`, claim 1637) — a live instance.
- Evidence the team has been patching the wrong layer: page 57's DB content contains `$M_\mathrm{BH} \lt 10^7$` — someone rewrote `<` to `\lt` *in stored content* to dodge the frontend escaper. That works per-instance and is exactly why the symptom "keeps coming back": each new LLM rewrite reintroduces `<`/`>` inside claim-span math.
- **Secondary mechanism:** an LLM that writes bare `\sim` outside `$...$` passes every existing guard — the canonicalizer's `_verify_invariants` checks for `\(`/`\[`, unicode super/subscripts, and bare `X_sub`, but never for bare TeX control sequences outside math. Page 57 is currently clean (0 bare TeX outside math), but nothing prevents the next renovation from reintroducing it.

### 3.3 HTML entity corruption (literal `&gt;` in prose)

**Layer of origin: frontend escaper (same defect as 3.2); secondarily, entity-bearing input at write time.**

- Same `wrapClaimComments` escaper. Its "normalize then re-escape" dance (`&amp;`→`&`, `&lt;`→`<`, `&gt;`→`>`, then `<`→`&lt;`, `>`→`&gt;`) corrupts any legitimate `<`/`>`/`&` in claim bodies and double-mangles content that arrives pre-escaped.
- Write side: the canonicalizer has **no entity-decode step**. If an LLM emits `&gt;` (common when models echo previously-rendered HTML), it is stored verbatim and rendered literally inside math, or decoded-then-re-escaped unpredictably inside claim spans. DB is currently clean (0 entities) only because Tori hand-fixed it in the last round.

### 3.4 Orphan `</span>` tags

**Layer of origin: write paths that bypass canonicalization; aggravated by a destructive strip in both guards.**

- Legacy `<span data-cite-ids="N">(Author Year)</span>` spans entered storage through raw write paths (E–H). The canonicalizer and `markdownNormalize.ts` both convert well-formed legacy spans, then **globally delete every remaining `</span>`** (canonicalizer line 69; markdownNormalize line 50). This silently "fixes" orphans but also destroys the closing tag of any other span that ever legitimately enters content — converting balanced markup into a new unbalanced-`<span>` problem that swallows the rest of the paragraph in rehype-raw. A guard that silently deletes structure is masking the contract violation rather than enforcing the contract.
- Because writers E–H skip canonicalization entirely, new spans can re-enter at any time, and only get cleaned when content happens to pass through a canonicalizing path again — which is why the symptom is intermittent.

### 3.5 `<!--cite-unmatched:...-->` leaking as visible text

**Layer of origin: frontend whitelist escaper (mechanism now understood, fix incomplete in class).**

- HTML comments are invisible in rehype-raw — *unless* they sit inside a claim body when `wrapClaimComments` runs, where anything not on the stash whitelist gets `<`→`&lt;` escaped and becomes visible text: `&lt;!--cite-unmatched:Dekel & Silk 1986--&gt;`. Tori's fix (convert unmatched comments to spans in `renderCitationMarkers`, which runs *before* `wrapClaimComments`, plus add that span shape to the stash whitelist) closes this single instance.
- **The class remains open:** any future marker comment type (the codebase already grows them — `EVIDENCE_HIGHLIGHTS_START`, trust-status comments, etc.) that appears inside a claim body will leak the same way until someone extends the whitelist again. This is whack-a-mole by construction.

### 3.6 Why fixes don't hold — the systemic gaps, ranked

| # | Gap | Effect |
|---|-----|--------|
| G1 | Frontend mutates content (5 regex stages incl. escaper) | Clean DB content corrupted at render; symptoms misattributed to backend; DB gets "fixed" with workarounds (`\lt`) |
| G2 | Whitelist escaping in `wrapClaimComments` | Every new construct inside a claim = new leak; reactive patch cycle is unbounded |
| G3 | 26 write sites, ~5 canonicalized; approvals (tasks.py:1393, edits.py:86) and ad-hoc scripts write raw | Malformed content re-enters storage at any time; intermittent recurrence |
| G4 | Guard code untracked in git (canonicalizer, markdownNormalize, CITATION_POLICY); 360 dirty files; no CI | Fixes can be lost, drift between the two canonicalizer implementations, no authoritative version |
| G5 | Frontend served from static build; no rebuild step in the fix workflow | Fixes "applied" but not live; later rebuilds resurrect older behavior |
| G6 | No machine-checked content contract; invariants incomplete (no entity check, no bare-TeX check, no References/`[n]` check) and failures are recorded, not enforced | Violations accumulate silently until visible |
| G7 | Design docs can contradict standing directives without detection | Superscripts saga (3.1) |

---

## 4. Overhaul design — target architecture

**Principle: exactly one layer is allowed to transform content text — the backend write chokepoint. Storage holds canonical content. The frontend parses markers and renders; it never rewrites text.**

```
ANY writer ──> WikiPage.content setter (ORM event)        wiki_pages.content        GET (verbatim)        Frontend
               ├─ entity decode                            "canonical contract        ──────────────>      ├─ marker parse (comments → React nodes)
               ├─ pure-text canonicalize (no DB)            content"                                       ├─ ReactMarkdown + remarkMath + rehypeKatex
               ├─ contract verify → QUARANTINE on fail                                                     └─ ZERO text mutation
               └─ enqueue citation-alignment task (post-commit, DB-dependent)
```

### 4.1 The stored-content contract (new: `docs/wiki_content_contract_v1.md`, ~1 page)

Stored `wiki_pages.content` MUST satisfy:

- **C-MATH:** All math in `$...$` / `$$...$$` only. Inside math, the characters `<`, `>`, `&` are forbidden — written as `\lt`, `\gt`, `\&` (KaTeX-native, HTML-inert at every layer). No TeX control sequences (`\sim`, `\gtrsim`, `\odot`, `\propto`, …) outside math.
- **C-HTML:** No HTML elements at rest. No `<span>` (legacy forms get converted, residue is a violation, never silently stripped). No `<sub>/<sup>` (converted to math). No HTML character entities (`&gt;` etc. — decoded at write time).
- **C-MARK:** Only these comment markers: `<!--claim:ids-->…<!--/claim:ids-->`, `<!--cite:ids-->`, `<!--cite-unmatched:key-->`, and registered structural comments (`EVIDENCE_HIGHLIGHTS_START/END`, trust-status). The registry lives in one constant imported by backend and (as JSON) by frontend tests.
- **C-CITE:** No author-year parentheticals in prose (aligned into markers), no `[n]` numeric citation tokens, no `## References` / `## Bibliography` heading. (Display policy — badges only — is the frontend's restatement of the same invariant; `CITATION_POLICY.md` is referenced by, and subordinate in mechanism to, this contract.)

### 4.2 Backend: single write chokepoint (closes G3, G6)

1. **ORM enforcement** — SQLAlchemy `event.listens_for(WikiPage.content, "set")` (or `@validates("content")`) on the model itself, so **every** path — routers, Celery tasks, ad-hoc scripts, future code — passes through it with no opt-in required. The handler runs the **pure-text** part of `canonicalize()` (no `db` arg): entity decode → existing S1–S7 → new transforms below. DB-dependent citation alignment must NOT run inside flush; see (4).
2. **New canonicalizer transforms:**
   - *Entity decode pass* (before S1 protection): `&amp;/&lt;/&gt;/&quot;/&#x27;` → characters, applied outside code fences.
   - *Math HTML-safety pass* (after math is identifiable): inside every `$...$`/`$$...$$` segment rewrite `<`→`\lt `, `>`→`\gt `, bare `&`→`\&`.
   - *Bare-TeX capture:* a known control-word list (`\sim, \lesssim, \gtrsim, \approx, \propto, \odot, \star, \times, \pm, \mathrm, \text, \mu m` …) found outside math gets wrapped into `$...$` together with its attached operand token, or — if context is ambiguous — flags a violation instead of guessing.
3. **Violations quarantine, not warn:** extend `_verify_invariants` to return a violation list (add checks: entities, `<span`, `</span>`, bare TeX outside math, `## References`/`[n]`, unbalanced `$`). On failure the chokepoint **rejects the write** (raises) for API paths, and for agent/automation paths routes the text to a `content_quarantine` table (page_id, source tag, violations, content) + Discord alert, leaving `page.content` untouched. Today's behavior (store anyway, record `content_canonicalize_failed_at`) is how rot accumulates.
4. **Citation alignment stays out of flush:** `normalize_citations` (DB-dependent: evidence matching, link upserts, claim-marker insertion) becomes a post-commit Celery task `align_page_citations(page_id)` enqueued by the chokepoint whenever content actually changed. This also fixes the current double-execution of `strip_hallucinated_cites` per call and removes DB-session reentrancy risk.
5. **Kill the destructive strip:** replace the global `</span>` deletion with: convert known legacy span forms → then any remaining `<span`/`</span>` is a contract violation (quarantine). Same in spirit for every "silently delete" rule: convert what is convertible, reject the rest visibly.
6. **Script hygiene:** ad-hoc scripts keep working automatically (they assign `page.content`, the ORM event fires). Add a CI grep-lint that forbids new `db.execute(text("UPDATE wiki_pages SET content"))`-style raw-SQL writes, the only remaining bypass. The nightly corpus sweep (extend `canonicalize_corpus.py` into a beat task) verifies the contract over all pages and alerts on drift — backstop for raw SQL and pre-existing rot.

### 4.3 Frontend: pure renderer (closes G1, G2)

1. **Delete `markdownNormalize.ts` entirely.** It is a drift-prone port of the backend canonicalizer; under the contract, storage is already canonical. (Keep it only during migration, behind a `console.warn` if it ever changes its input — see §7.)
2. **Replace `renderCitationMarkers` + `wrapClaimComments` with a single non-escaping marker parser.** One pass over the content string that maps registered comment markers to placeholder elements and **never touches the text between them**:
   - `<!--cite:ids-->` → `<span data-cite-ids="ids"></span>`
   - `<!--cite-unmatched:key-->` → `<span data-cite-unmatched="…"></span>` (attribute-escaped only)
   - `<!--claim:ids-->body<!--/claim:ids-->` → `<span data-claim-id="ids" id="claim-N">body</span>` with `body` passed through **verbatim** — no entity normalization, no `<`/`>` escaping, no stash whitelist. The escaper exists today to defend against raw `<`/`>` in bodies; the contract makes those impossible at rest (math uses `\lt`/`\gt`, HTML is banned), so the defense — and its whole leak class (3.2, 3.3, 3.5) — is deleted rather than patched. Unknown/unregistered comments are left as comments: rehype-raw drops them; they can never become visible text.
   - Order: marker parse runs **before** ReactMarkdown, as today; `remarkMath` then extracts `$...$` (contract guarantees no `<`/`>`/`&` inside), `rehypeRaw` materializes only our marker spans, `rehypeKatex` typesets.
3. **Defensive floor, not mutation:** keep `throwOnError: false`, and add KaTeX `strict: "ignore"`; if KaTeX still errors, the raw string shows — and the regression test (§8) catches it before deploy, which is the correct failure location.
4. **One policy file:** keep `frontend/CITATION_POLICY.md`, delete the `src/app/wiki/` duplicate, link it from the contract doc. The unmatched-cite badge behavior stays as-is (render nothing) per policy.
5. Delete dead files: `*.bak`, `WikiPageClient.tsx.bak.20260602_multiclaim`, `ClaimBlock.tsx.bak` — they are how stale code resurrects.

### 4.4 Process: deployment and history (closes G4, G5, G7)

1. **Commit everything** in this subsystem to git as the first implementation step: canonicalizer + tests, frontend renderer, both policy/contract docs. Future fixes are commits with messages, revertible and diffable. (The 360-file dirty tree is a separate cleanup; at minimum this subsystem gets tracked now.)
2. **`scripts/deploy_frontend.sh`:** `npm test && next build && restart` — a frontend fix is not "done" until this ran; Tori's checklist item, also runnable by automation. Backend equivalent: `pytest backend/tests/canonicalize backend/tests/citations` gates any canonicalizer change.
3. **Design-doc/directive conflict rule:** any design doc touching citation display must carry a header line acknowledging `CITATION_POLICY.md`; the regression suite is the real enforcement (a doc can be wrong; the test still blocks the build).

---

## 5. Minimum change set per symptom class

| Symptom | Minimum permanent fix | Guard location |
|---|---|---|
| 1. Superscripts / References | Render-test asserting no `<sup>` cite markers, no References heading (fixture page) + C-CITE write-time invariant + single policy file | Frontend test (CI) + chokepoint |
| 2. Raw `\sim` in prose | Delete claim-body escaper (frontend); bare-TeX capture + quarantine (backend) | Chokepoint + pure renderer |
| 3. `&gt;` in prose | Entity decode at write; `\lt`/`\gt`/`\&` in math at write; delete escaper | Chokepoint (frontend stops creating it) |
| 4. Orphan `</span>` | Convert legacy spans, quarantine residue (no silent strip); chokepoint covers all 26 write paths | Chokepoint |
| 5. Unmatched-cite comment leak | Non-escaping marker parser: unknown comments stay comments (invisible by construction) | Pure renderer |

---

## 6. What this explicitly does NOT change

- Marker vocabulary and `page_citation_links` schema (per `dynamic_citations_design_v1.md`) — unchanged.
- Badge UI, claim popovers, trust colors, Research Ideas chips — unchanged (per WikiPageLayout §5 scope: per-claim inline chips are not page chrome).
- `sync_verbatim_claim_markers` / marker-embed pipeline — unchanged, but it now writes through the chokepoint like everything else.
- Renovation prose-quality rules — out of scope here; no wiki prose is rewritten by this overhaul.

---

## 7. Migration order (Tori)

1. **Contract + canonicalizer v2** — write `wiki_content_contract_v1.md`; add entity-decode, math-HTML-safety, bare-TeX capture, extended invariants + violation list; split `canonicalize()` into pure-text vs DB-dependent halves; tests green. *(backend only, no behavior change yet)*
2. **Chokepoint** — ORM event + quarantine table + post-commit `align_page_citations` task; remove inline `normalize_citations` from write paths; CI grep-lint for raw SQL writes.
3. **Corpus backfill** — run canonicalizer v2 over all pages (extend `canonicalize_corpus.py`); review quarantine output by hand once; from here the DB is contract-clean.
4. **Frontend cutover** — new marker parser; delete `markdownNormalize.ts`, escaper, `.bak` files, duplicate policy file; add render regression tests; `deploy_frontend.sh` (test + build + restart). *(Do this only after step 3 — the pure renderer assumes contract-clean content.)*
5. **Nightly contract sweep** beat task + Discord alert.
6. **Commit + deploy** — git add the whole subsystem, run both test suites, rebuild, restart, verify on live `galaxy-evolution`.

Steps 1–3 and 4 are independently shippable; the system is never in a worse intermediate state (the old frontend tolerates contract-clean content).

## 8. Regression test matrix

Backend (`pytest backend/tests/canonicalize`, `backend/tests/citations`):
- T1 entity decode: `"M &gt; 10"` → `"M \gt 10"`-in-math / `"M > 10"`-in-prose; idempotent.
- T2 math safety: `$z < 0.3$` → `$z \lt 0.3$`; `$>700,000$` → `$\gt 700,000$`.
- T3 bare TeX: `"at z \sim 2"` → `"at $z \sim 2$"`; ambiguous case → violation.
- T4 spans: legacy cite span converts; any other `<span>` → violation (not stripped).
- T5 C-CITE: content containing `## References` or `[12]`-style cite tokens → violation.
- T6 chokepoint: raw assignment via every writer class (proposal approve, vote approve, script) lands canonicalized; violation lands in quarantine with page untouched.
- T7 idempotence over live-corpus sample (extend existing test).

Frontend (vitest + react-testing-library on a fixture mirroring page-57 constructs):
- F1 claim span containing `$\gt 700,000$` renders KaTeX output; rendered text contains no `&gt;`, no `\gt`, no `\sim`.
- F2 no `<sup>` numeric citation markers and no `References`/`Bibliography` heading in rendered DOM (the §3.1 invariant, machine-checked).
- F3 `<!--cite-unmatched:Dekel & Silk 1986-->` inside a claim body → invisible (no literal `<!--` text in DOM).
- F4 unknown comment `<!--future-marker:x-->` inside a claim body → invisible.
- F5 cite badge popover renders from `<!--cite:N-->` with citation metadata present; bare 📄 fallback when metadata absent.

---

## 9. Sign-off

Kun signs off on this design as Strategic Overseer of the renovation/autowiki regime (L1). Tori: implement in the §7 order; report after step 3 (backfill quarantine review) and step 6 (live verification) with before/after screenshots of `nebulamind.net/wiki/galaxy-evolution`.

---

## 10. Checkpoint 1 ruling (2026-06-11, Kun)

Context: Tori completed §7 steps 1–2 (contract doc, canonicalizer v2, ContentQuarantine model, dry run at `backend/logs/canonicalize_corpus_v2_dry_run.json`). 40/43 pages contract-clean; ruling requested on pages 7, 12, 22 — options (a) quarantine, (b) targeted transform, (c) loosen contract — plus a verdict on H₀-style Unicode in prose.

### 10.1 Finding: the dry-run artifact is stale

Re-running the CURRENT canonicalizer rev against the live DB content shows pages 12 and 22 already pass with **zero** violations — the artifact was generated from an earlier rev. Process fix (binding):

- The canonicalizer MUST be committed to git before backfill (already required by §4.4; now a checkpoint precondition).
- Every dry-run artifact MUST record the canonicalizer git SHA it was produced from.
- Tori regenerates the dry run from the shipped rev before the real backfill. Rulings below anticipate what that regeneration will surface.

### 10.2 Per-page rulings

**Page 7 (gravitational-waves) — ruling (b), via T-FENCE.**
The `unicode_super_sub` (H₀) flag is a downstream artifact: ~96% of the page is wrapped in a whole-page ```markdown fence, and the canonicalizer's code-fence stash protects the entire body from every transform — so the existing Unicode→TeX transform never ran. The frontend's `unwrapCodeFence` masks this at render time, which is why it looks like a one-character issue. Root fix is fence unwrapping at rest (T-FENCE below), after which the existing transforms convert H₀ → `$H_{0}$` deterministically. Note: the fenced blob also contains a trailing numbered references list that `_remove_reference_sections` will correctly strip once unwrapped.

**Page 12 (spacetime) — ruling (b), via T-NESTED.**
Passes the current rev (stale flag). Residual REAL defect not caught by any invariant: nested inline `$...$` inside `$$...$$` bodies, e.g. the Kerr metric line carrying `$r_{\text{s}}$` inside display math — KaTeX-fatal. Fix is T-NESTED + I-NESTED below.

**Page 22 (tidal-forces) — ruling (b), via T-FENCE + existing transforms.**
Passes the current rev for the flagged violations. The page has an unclosed display-math opener pattern (lone `$$` with whitespace where closers should be) and an unclosed fence variant; both are handled by T-FENCE's unclosed-opener branch plus the existing `composite_math_break` / `unbalanced_math_dollar` invariants on the regenerated dry run.

**Page 13 (kuiper-belt) — ruling (a) QUARANTINE.** (Surfaced by my corpus scan, not in Tori's flag list.)
The stored content is a raw LLM synthesis JSON blob (`{"title": "Kuiper Belt", "sections": [...]}`) inside a ```json fence — it is not markdown at all. It must NOT be fence-unwrapped as prose. T-FENCE explicitly excludes non-markdown language fences; a page *starting* with one raises a new `leading_code_fence` violation → quarantine. Rebuilding page 13 from its synthesis JSON is a separate repair task after cutover.

### 10.3 H₀ verdict: violation stands — do NOT loosen the contract

Unicode super/subscripts in prose remain a contract violation. Rationale:
1. A deterministic, lossless transform to `$H_{0}$` exists — there is no content we cannot represent under the contract.
2. Permitting Unicode scripts reopens the mixed-notation class (H₀ in one paragraph, `$H_0$` in the next), which is exactly the inconsistency the contract exists to kill.
3. Every loosening precedent weakens the quarantine gate's authority; the gate only works if violations are rare and real.

Page 7's H₀ was never a counterexample to the contract — it was evidence the transform pipeline was being skipped.

### 10.4 Required canonicalizer additions (Tori, before real backfill)

**T-FENCE — whole-page fence unwrap (runs FIRST, before the code-fence stash):**
- Trigger: content begins (offset 0, after optional leading whitespace) with ```` ```markdown ````, ```` ```md ````, or a bare ```` ``` ```` fence, AND the fenced body contains markdown headings (`^#{1,6} `).
- Handle three shapes observed in corpus: (i) cleanly closed whole-page wrap (pages 28, 30) → strip both fences; (ii) unclosed opener (pages 22, 50) → strip opener only; (iii) mid-doc close (page 7) → strip opener and the matching close, preserve trailing content for normal transforms.
- NEVER unwrap a fence with any other language tag (```json, ```python, …). A page *starting* with a non-markdown language fence raises new invariant **`leading_code_fence`** → quarantine (this catches page 13).
- Legitimate inner code fences (not at offset 0) are untouched and still protected by the stash.

**T-NESTED — strip inner `$` from display-math bodies:**
```python
text = re.sub(r"\$\$([\s\S]+?)\$\$", lambda m: "$$" + m.group(1).replace("$", "") + "$$", text)
```
Runs after math capture, before `_math_html_safe`.

**I-NESTED — new invariant `nested_math_delimiter`:** flag any `$` character remaining inside a captured `$$...$$` body in `verify_invariants()`.

### 10.5 Scope warning for the regenerated dry run

Corpus scan results (verify against regenerated artifact):
- **6 fence-wrapped pages:** 7, 13, 22, 28, 30, 50. Pages 28/30 cleanly closed; 7 mid-doc close; 22/50 unclosed opener. Once T-FENCE unwraps these, their bodies hit the transforms/invariants for the first time — **expect NEW violations to surface** from the 5 unwrapped pages. These come back to me as one more checkpoint review before backfill commits; do not auto-quarantine them without review.
- **7 nested-math pages:** 5, 12, 15, 21, 36, 41, 57 (incl. flagship galaxy-evolution). All fixed by T-NESTED; I-NESTED confirms zero residue.

### 10.6 Checkpoint 1 exit conditions

1. T-FENCE, T-NESTED, I-NESTED, `leading_code_fence` implemented; canonicalizer + contract doc committed to git.
2. Dry run regenerated from the shipped SHA, SHA recorded in the artifact.
3. New violations from unwrapped fenced pages reported to Kun (expected; quick review).
4. Page 13 quarantined via the gate (not by hand); repair task filed separately.
5. Then proceed: real backfill (§7 step 3) → frontend cutover (§7 steps 4–5). Frontend `unwrapCodeFence` may be deleted only AFTER the fenced pages are backfilled clean.

— Kun, Strategic Overseer (L1), 2026-06-11

### 10.7 Checkpoint 1 final review — SIGNED OFF (2026-06-11, Kun)

Reviewed `backend/logs/canonicalize_corpus_v2_kun_ruling_dry_run.json` (SHA-stamped `f0572ee`; verified the canonicalizer, contract doc, corpus script, and tests are committed at that SHA and unmodified on disk). Independent verification performed:

- Counts reconcile exactly: 12 changed / 1 quarantine; `markdown_fence`×5 on pages 7/22/28/30/50; `nested_math` 8+4+2+2+2+10+6 = 34 across exactly the 7 predicted pages (5/12/15/21/36/41/57); page 13 quarantined via `leading_code_fence`, correctly NOT unwrapped.
- Spot-check page 7: canonicalized output contains no Unicode H₀; `verify_invariants` → [].
- Spot-check page 12: Kerr metric is now a single clean `$$...$$` with inner `$` stripped (T-NESTED working as specified); `verify_invariants` → [].
- Test suite re-run locally: 11/11 pass.
- Note: artifact records `git_dirty: true` for the repo overall — acceptable; the SHA-stamp requirement covers the canonicalizer rev, which is clean. The 360-dirty-file problem remains tracked under §4.4/G4.

**Verdict: Tori is cleared to run the real backfill (§7 step 3) and proceed to frontend cutover (§7 steps 4–5).** Standing conditions: page 13 repair filed as a separate task; `unwrapCodeFence` deleted only after fenced pages are confirmed clean in the DB; report after step 3 (quarantine review) and step 6 (live verification with before/after screenshots of galaxy-evolution).
