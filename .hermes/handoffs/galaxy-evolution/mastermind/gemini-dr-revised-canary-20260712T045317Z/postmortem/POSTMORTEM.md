# POSTMORTEM — closed C1 body audit (offline; Phase A, Hwao)
Packet: `gemini-dr-revised-canary-20260712T045317Z` · 2026-07-12 · **offline, read-only, no browser/network**
Input (immutable): closed C1 body
`../gemini-dr-next-phase-canary-20260712T033422Z/runs/c1/body.md`
sha256 `9933638616c9fc4dfb8306849f1ed91bf2d008f819c2623b831aec672da347d3` (untouched).
Contract of record: C1 "calibration provenance" prompt, clauses C1–C8.

## 0. Framing (decisive) — the captured body is RENDERED innerText, not raw markdown
Evidence: no `#`/`##` on any heading (L1, L7, L78, L121, L143, L169, L181); MathJax
subscripts/superscripts split onto their own lines with zero-width chars (χ₀/β L9–L13; ε_SN/ε_f
L17–L25; f_gas,500c/f_SN/Δv_SN/β_BH/ΔT_AGN/v_jet L27–L51; ΔT_heat/v_w L52–L60; 10^51 L64–L66;
H_I/H_2 L83–L115; R_500 L163–L167; k^−1 L131–L133; Ω_m/σ_8 L133–L141); tables rendered as
tab-separated text de-aligned by those fragments (L8–L60, L82–L103, L147–L159).
**Consequence:** a naive validator run on THIS text would emit many false failures (no `##`, broken
tables, numbers split from their tokens). Every finding below is tagged **[MODEL]** (genuine, would
persist under perfect capture) or **[REPR]** (representation artifact of innerText capture).

## 1. Clause verdict table
| Clause | Verdict | Line refs | Note |
|---|---|---|---|
| C1 meta header | **PASS** (content) | L1–L5 | all four fields present (title/Run date/Model=Gemini 1.5 Pro/Simulations covered: 8). `#` stripped = [REPR]. |
| C2 structure + `NONE_FOUND` | **FAIL** | sections L7/78/121/143/169/181 (PASS order); NONE_FOUND device OK L16; **Gaps "cited or NONE_FOUND" FAIL L175, L177, L179** | 5 sections present & ordered; three GAP lines are neither cited nor `NONE_FOUND` [MODEL]. |
| C3 uncertainty token | **FAIL / MANUAL** | token applied L91–L103 (ledger); MISSING on prose/params L9 (0.002, 2), L64–66 (10^51 ergs), L97 (0.3 dex), L117 (1σ; z=7–8), L131–141 (k∼1–10; Ω_m; σ_8) | token used in validation-ledger cells but not in prose/parameters [MODEL]; whether parameter settings/physical constants require it = MANUAL. |
| C4 citation labeling | **FAIL** | **L129** (confirmed) + **L96** ASTRID-UVLF row citation cell EMPTY; MANUAL L161 | uncited calibration/validation statements [MODEL]. |
| C5 wording | **FAIL** | **L117** own-voice "firmly established" (confirmed); MANUAL L131 | one own-voice banned-register hit [MODEL]; L131 "demonstrated that" is an attributed quote WITH citation `[1603.02702]` ⇒ acceptable, not a fail. |
| C6 estimand/commensurability | **MANUAL_REVIEW_REQUIRED** | labels present L91–L103, L105 | "simulation median vs observed selection-shaped stat: matched/unmatched" applied structurally; per-source correctness is semantic; four-qualifier rule largely N/A for calibration content. |
| C7 links ledger | **FAIL** | in-text URLs absent from ledger: **2501.16602 (L72)**, **2605.13843 (L105)** | original C7 is **one-way** (every cited item must be in the ledger) — these two violate it [MODEL]. Orphan ledger rows (534:957 L215; ASTRID-RG L200; TNG-RG L208; FIRE-Movies L212; Siegel-Critique L206) are **advisory quality findings, NOT original-contract failures**. |
| C8 marker | **PASS** | L217 marker; L218 blank | exactly once and the final non-blank line. |

## 2. Confirmation of the two known failures
- **C5 L117 [MODEL]:** "…before dynamic and virial equilibrium is **firmly established**." Own-voice
  use of a banned settled-register verb. CONFIRMED.
- **C4 L129 [MODEL]:** the FLAMINGO-critique paragraph ("…a sophisticated ΛCDM-based modeling
  apparatus, not an assumption-free measurement of cosmic reality") carries **no same-line citation
  and no `UNCITED_NOT_USABLE`** (its source, the "Siegel Critique" medium link, sits in the ledger
  L206 but is not cited inline). CONFIRMED.

## 3. Latent issues explicitly tested (Duho's list)
1. **Widespread C3 numbers lacking uncertainty/token — CONFIRMED [MODEL].** The model applied `±
   UNCERTAINTY_NOT_QUOTED_BY_SOURCE` diligently in the validation-ledger cells (L91–L103) but omitted
   it for numbers in prose and in the calibration ledger: 0.002 & 2 (L9), 10^51 ergs (L64–66), "1σ"
   and z=7–8 (L117), "0.3 dex" (L97), k∼1–10 / Ω_m / σ_8 (L131–141). Inconsistent application.
2. **C2 Gaps uncited / non-`NONE_FOUND` lines 175/177/179 — CONFIRMED [MODEL].** L173 GAP is cited
   `[512/3703, 548/stag375]`; L175 (radio-AGN), L177 (passive-galaxy cold-gas), L179 (selection-
   function matching) are assertions of absence with neither citation nor `NONE_FOUND`. Note the
   semantic tension (a claim of "no published test" is hard to cite) → contract likely needs a
   dedicated asserted-absence token; flagged MANUAL for the contract fix, FAIL against the literal rule.
3. **C7 cited URLs absent from ledger — CONFIRMED [MODEL].** `arxiv.org/html/2501.16602v1` (L72,
   FIRE/STARBURST99) and `arxiv.org/html/2605.13843v1` (L105, forward-modeling) are cited in-text but
   missing from the Links ledger; both are the "html/25xx" inline-only form. This IS the C7 FAIL: the
   original contract is **one-way** (every cited item must appear in the ledger). Orphan ledger rows
   (ledger entries not cited in-text, §1 C7) are **advisory quality findings only, not
   original-contract failures**.
4. **Rendered-innerText MathJax/table fragmentation — CONFIRMED [REPR], NOT a model defect.** See §0;
   these break table parsing and split numbers from tokens but originate in the capture, not the
   model. This is the dominant source of *apparent* structural failure and must not be scored against
   the model.
5. **C6 commensurability/qualifier semantics — [MANUAL].** Labels are structurally present and the
   report devotes L105 to commensurability; correctness of each "matched/unmatched" verdict per source
   requires human judgment. No deterministic FAIL.

## 4. Model-output defects vs representation artifacts (required separation)
- **[MODEL] genuine (persist under faithful capture):** C5 L117; C4 L129 + L96; C2/Gaps L175/177/179;
  C3 prose/parameter numbers; C7 one-way FAIL (cited 2501.16602 & 2605.13843 missing from ledger).
  Orphan ledger rows are advisory quality findings, not contract failures.
- **[REPR] representation artifacts (capture, not model):** stripped `#`/`##` headings; MathJax
  sub/superscript fragmentation; table de-alignment (§0 line ranges). These are why the validator must
  operate on a **normalized structured representation** of the rendered DOM (§5), not on raw innerText.
- **[MANUAL] ambiguous:** C3 exemption for parameter settings / physical constants / scale refs; C6
  per-source label correctness; citability of asserted-absence GAP lines; C5 attributed-quote triage
  (L131 acceptable).

## 5. Implications for the revised packet (Phase B inputs — advisory, not applied here)
1. **Dual capture** (top priority — raw Markdown is NOT available on the validated Gemini surface, and
   a raw-Markdown assumption would contradict this packet's rendered-body validator): (a) preserve the
   **exact immutable answer-body innerText**, AND (b) capture the **structured rendered DOM** (heading
   roles, paragraphs, table rows/cells, links, logical block IDs) into a **canonical normalized
   representation with source mapping** back to the innerText. The Phase-B validator runs on that
   normalized structured representation (which restores the headings/tables/links that innerText
   loses), while the **C8 completion marker is additionally checked against the exact innerText**
   (marker exactly once + final non-blank line).
2. **C1r prompt tightening:** (a) C3 token on EVERY number or a stated exemption convention for
   parameter settings / physical constants; (b) every GAP line carries a citation OR an explicit
   asserted-absence token (not silent); (c) Links-ledger rule — the original **one-way** rule (every
   in-text citation appears in the ledger) is binding; C1r **MAY** explicitly tighten to bidirectional
   (also require every ledger row be cited in-text), which would additionally catch the orphan rows;
   (d) no empty citation cell in any
   ledger row (citation or `UNCITED_NOT_USABLE`); (e) reinforce C5 banned register incl.
   `establish(es|ed|ing)`.
3. **Validator (deterministic on the normalized structured representation; C8 marker also vs exact
   innerText):** flag C3 bare numbers, C4 empty/absent citations, C2/Gaps uncited lines, C5
   banned-register, C7 **one-way** ledger check (every cited item in the ledger; bidirectional only if
   C1r adopts it), C8 marker-once-final; emit `MANUAL_REVIEW_REQUIRED` for the [MANUAL] classes.
   Because it runs on the normalized representation, [REPR] artifacts do not surface as failures. Its
   RED fixture = this body (must FAIL C5 L117 + flag C4 L129 + the two C7 misses); GREEN on a clean fixture.

## 6. Attestation
Offline, read-only audit; no browser/network; **only this file written**; no marker, no ledger row,
no edit to the closed packet or its immutable body. Path + sha256 returned for Tori review.
