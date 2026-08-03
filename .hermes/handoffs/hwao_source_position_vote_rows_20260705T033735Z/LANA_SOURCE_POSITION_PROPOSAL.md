# Lana — source-position + adjudication proposal for the six vote-dependent 2929 rows

Coordinator: Hwao/Fable · Relay: Tori/Hermes · Lane: Lana (semantic/source-grounded), read-only proposal.
Written: 2026-07-05, repo `/Users/duhokim/NebulaMind/NebulaMind`.
**Docs-only. No SQL/DB, no apply/rollback files, no queue edits, no prose/runtime/git/public-cockpit mutation. Two output files only. Hard lock respected: no SQL until all 36 rows are decided — these six do not unlock SQL.**

Companion machine-readable file: `lana_source_position_proposal.jsonl` (one row per evidence id, same marker).

## Method

I read the six queue-context snippets and fetched each source's public arXiv abstract to verify the paper and the rhetorical zone of the cited span. All three papers are real and on-topic. A recurring, important finding: **most of the six snippets are introduction/background review sentences of their source papers (citing prior work), not the papers' own results** — so source-position honesty requires flagging zone, and I mapped each row to the successor claim it genuinely supports while preserving every human-gold vote.

## Source verification (abstracts fetched)

- **arXiv 2604.15438 — SWAN M51 IV** ("Extent of AGN feedback on the ISM"): studies AGN feedback on M51's ISM; its *own* result is a two-stage jet-ISM/X-ray molecular-excitation mechanism. The positive-feedback, outflow-turbulence, and "models need AGN feedback" sentences (rows 28060/28091/28155) are **introduction/background**, confirmed by the abstract.
- **arXiv 2009.11175 — "AGN-driven outflows... in young radio galaxies"**: own finding is that warm ionised outflows track radio-source extents, consistent with **jet-mode feedback being the dominant driver**. Rows 28095/28111 are intro/background but on-mechanism for **kinetic/radio-mode** feedback, consistent with the paper's own finding.
- **arXiv 1706.08987 — "AGN feedback on molecular gas reservoirs in quasars at z~2.4"**: own ALMA finding is CO(3-2) **spatially anti-correlated with the ionised outflow** (molecular gas dispersed/heated in the outflow-swept region). Row 28141's span is the prior SINFONI review, but the paper's own finding directly supports ejective gas removal.

## Proposed adjudications

| Row / ev | Vote | Successor | Role | Docs position | Decision | Conf |
|---|---|---|---|---|---|---|
| 28060 | 5048 **−1** | 2942 | limitation_or_caution | accepted_limited | **leave_archival** | high |
| 28091 | 5049 +1 | 2943 | support | accepted_limited | relink | medium |
| 28155 | 5053 +1 | 2942 | support | accepted_limited | relink | medium |
| 28095 | 5050 +1 | **2947** | support | accepted | **route_kinetic_radio** | high |
| 28111 | 5051 +1 | **2947** | support | accepted_limited | **route_kinetic_radio** | high |
| 28141 | 5052 +1 | 2943 | support | accepted | relink | high |

### Special handling — 28060 (the only −1)

The span is about **positive AGN feedback** (gas compression triggering star formation) — the *opposite sign* to the quenching narrative of 2942–2947 — and it is a background-review sentence, not SWAN's own finding. Positive feedback is exactly the nuance old 2929 carried that **no successor claim covers**. Human vote 5048 (−1, `confirm_weakening`, "about positive AGN feedback in general") is honored: I classify it `limitation_or_caution` and `leave_archival` on the retired 2929 parent, **not** relinked as support. A plain support+relink would contradict the gold vote and put a positive-feedback source under a quenching claim.

### The two kinetic routings — 28095, 28111 (→ 2947)

Both concern **relativistic jets**. The prior matrix mapped them to 2943/2946 because it predates 2947; the correct successor is the new kinetic/radio-mode claim **2947**. 28095 is accepted (jet-mode is the paper's own finding); 28111 is accepted_limited (the jet-bubble result is simulation-based → model-bounded). Both preserve their +1 votes via `route_kinetic_radio`.

### Background-zone caveats — 28091, 28155

Both are SWAN introduction sentences: 28091 (outflow-turbulence regulates SF → supports 2943, but the mechanism is turbulent prevention, not literal removal) and 28155 (models require AGN feedback → supports 2942, but it is theoretical/model background). Both are `accepted_limited` supports honoring their +1 votes, flagged for zone/mechanism scope.

## Dependency handling (votes)

Every row's `dependency_handling_action` names its vote id and states how it is honored: the five +1 votes (5049/5050/5051/5052/5053) are relinked/routed as support onto the correct visible successor; the one −1 vote (5048) is preserved as a weakening/limitation and left archival, never overridden.

## Anti-duplicate

Marked `resolved_no_duplicate` for all six (distinct evidence ids / distinct source spans). For the two kinetic routings (28095/28111 → 2947) I recorded 2947's existing kinetic evidence ids `[26681–26685]` (the relinked old-2915 rows) as the duplicate-check set; these six are different evidence ids from different papers, so no duplicate — **but a DB-level dedup against 2947's live evidence should be confirmed at SQL time (no DB access in this lane).**

## Limitations of this pass

- Source access was **abstract-level** (`abstract_only_verified` on all six): I verified each paper and the zone of each span via the abstract, but did not fetch full-text PDFs to pin exact page/paragraph, so `pdf_page`/`figure_or_table` are null and the locators are section-level. A later full-text pass should pin exact spans — and for 28141 should prefer the paper's own ALMA anti-correlation sentence over the quoted prior-work review.
- These are **proposals for human/source decision**, not executed changes; the queue files are untouched.

## Confirmation

No SQL, no DB connection, no apply/rollback file, no queue edit, no prose/wiki publish, no runtime/deploy, no git, no public-cockpit change. Two files written: this report + `lana_source_position_proposal.jsonl` (6 rows, all carrying the marker).

LANA_SOURCE_POSITION_VOTE_ROWS_PROPOSAL_20260705T033735Z
