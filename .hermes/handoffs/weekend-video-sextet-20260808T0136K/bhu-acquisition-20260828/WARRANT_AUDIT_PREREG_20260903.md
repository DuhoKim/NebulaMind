# Corpus-wide WARRANT audit — pre-registration (Tori, 2026-09-03 00:5x KST)

**Ordered by Duho (relay via Blanc 00:47 KST, verbatim "Hwao a, Tori b"): extend the warrant column from the 5
calibrated rows across the corpus, receipted, blind-doubled where a warrant is contested.** Written BEFORE the first
draw. In-lane; paper HOLD; no tier or standing moves; packets to `OPEN_QUESTIONS_FOR_DUHO.md`; audio hold, text only.

## 1. What the warrant axis is (from the record, §0, 2026-08-29)
The TIER describes a claim's shape; STANDING whether it fired; **WARRANT whether the theory actually produces the
claim it is tiered on, or borrows/asserts it.** The record's own correction: "a directional claim can fail to follow
in the asserted direction, a PROSPECT can fail to connect theory to instrument, a THEORETICAL-OBSTRUCTION can rest on
a disputed no-go." This audit implements exactly that, one cell per base-layer paper.

## 2. Scope
The 51 base-layer papers (entries 1–28, 31, 36–44, 46–57, 59). Entries 18 and 56 have no clean text: their cells are
`NO_TEXT` and they remain acquisition targets. The five existing calibrated cells (7, 31, 51, 44, 1) are re-verified
against today's deep-audit receipts, not re-derived.

## 3. The warrant question, per tier, and the vocabulary (one token per cell; fixed now)
- **CALIBRATED-FALSIFIER** — does the theory derive the number AND the threshold?
  `W_EXPLICIT` (both derived in the paper) · `W_BORROWED` (number or threshold from an instrument chain or an
  external result) · `W_DISPUTED` (a pinned published challenge to the derivation) · `W_UNDERIVED` (stated, not derived).
- **QUALITATIVE-DIRECTIONAL** — does the sign/direction FOLLOW from the model?
  `W_DIRECTION_DERIVED` (follows with stated assumptions) · `W_DIRECTION_CONDITIONAL` (follows only for a free
  parameter choice) · `W_DIRECTION_ASSUMED` (the sign is an input or ansatz — note: A(a) already excludes such entries
  from the tier, so this token is a contradiction flag → packet).
- **PROSPECT** — does the paper connect theory to the named instrument/observable?
  `W_ROUTE_CONNECTED` (a derived link, amplitude-free) · `W_ROUTE_NAMED_ONLY` (named, not connected).
- **THEORETICAL-OBSTRUCTION** — is the no-go proved here with its stated hypotheses?
  `W_PROOF_OWNED` · `W_PROOF_CITED` (ownership-of-proof rule violated → packet) · `W_PROOF_CONTESTED` (a seat split or a
  pinned challenge; domain as stamped or narrower).
- **CONSISTENCY-ONLY** — is the consistency shown by equations, or asserted?
  `W_CONSTRUCTION_DERIVED` · `W_CONSTRUCTION_ASSERTED` (by ansatz or citation at the load-bearing step) ·
  `W_MIXED` (derived background, asserted link to cosmology — the common case).
- Uniform second field, every cell: **borrowed inputs** — the load-bearing imports (closures, data used as inputs,
  cited theorems), listed with line receipts, or `none`.

## 4. Evidence standard
- Each cell cites line receipts from the pinned source (or page receipts for image-only PDFs).
- **Extraction, not re-audit:** today's 31 deep-audit reconciliations (+ the Programs for 23–27, the standing
  files for 1, the b-series for 7/31/44/51/54) already answered "is it derived?". One seat (codex) drafts each cell
  from those receipts + the source; **Tori verifies at least one receipt per cell against the source before filing.**
- **Blind double mandated where contested:** (i) the deep-audit seats disagreed on derivation; (ii) a pinned
  published challenge exists (31; 5/4 vs 1); (iii) the drafted cell contradicts the record's prose or a stamped
  tier/standing; (iv) the token is a packet-class token (`W_DIRECTION_ASSUMED`, `W_PROOF_CITED`). Then codex + kimi
  (≤ 600 lines) or codex + claude-seat, results written only when complete; third seat on a split.
- A warrant cell NEVER changes a tier or standing. A packet-class token files a packet and the audit continues.

## 5. Queue and outputs
- Order: the depth rule's density ranking (`b70_warrant_queue.py`, same frame/mapping as `b69`), receipts
  `WARRANT_<n>_*.md`; the five calibrated rows first (re-verification), then by density.
- Output: `WARRANT_TABLE_20260903.md` in this lane (entry | tier | warrant token | borrowed inputs | receipts),
  plus a one-line `Warrant (2026-09-03):` annotation per entry in the bibliography and, at the end, a §0 pointer.
  Tier words untouched.

**Dated amendment, 2026-09-03 00:58 KST (first split, entry 31):** when a calibrated cell is both borrowed/underived AND the subject of a pinned challenge, the cell token records the DERIVATION status (`W_EXPLICIT` / `W_BORROWED` / `W_UNDERIVED`) and the pinned challenge is recorded in the notes field as `pinned challenge: …` — "disputed" describes the literature, not the derivation. `W_DISPUTED` is reserved for cells where the derivation itself is contested and no derivation-status token can be assigned. Entry 31 is therefore `W_BORROWED` with the challenge noted (codex `W_DISPUTED`, claude-seat `W_BORROWED`; both contents preserved).
