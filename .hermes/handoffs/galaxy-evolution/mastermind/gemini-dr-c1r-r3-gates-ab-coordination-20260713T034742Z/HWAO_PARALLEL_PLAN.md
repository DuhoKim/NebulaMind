# HWAO_PARALLEL_PLAN — Gates A and B in parallel

Coordination packet: `gemini-dr-c1r-r3-gates-ab-coordination-20260713T034742Z` · Approval: Duho, "Gates A and B in parallel" (relay 20260713T034742Z). Hwao coordinates only; **neither gate starts until Tori relays assignments from this plan.** All hard boundaries of the relay bind both gates verbatim. Gate C remains unapproved and unarmed. The two gate packets never merge; they cross-reference each other and prior packets by path + sha256 only.

## 0. Write roots and immutable inputs (both gates)

| Packet | Writes allowed | Role |
|---|---|---|
| `gemini-dr-c1r-validator-r3-implementation-20260713T034742Z` | Gate A lanes only | implementation + re-adjudication |
| `gemini-dr-c1r-manual-source-verification-20260713T034742Z` | Gate B lanes only | source/science verification |
| this coordination packet | Hwao/Tori coordination artifacts only | plan, relays, final synthesis |

Immutable (hash-pinned at each gate's P0, re-checked at close): sealed canary packet, chip-validator repair packet, r3/triage packet — byte-for-byte, including `prompt/C1r.md` (`fffac44f…e1ef`), `validator_result_v2.json` (`ad4d035b…3d52`), `CONTRACT_R3_DRAFT.md`, `TRIAGE_LEDGER.json` (`81c3d75d…fff2`). Temp files: `<packet>/_tmp_*` only, with the rev2 discipline (receipt-scoped TMPDIR + EXIT trap — the repair packet's temp-leak lesson is now standing rule).

---

# GATE A — validator-r3 implementation (offline; no live call of any kind)

## A1. Phases and lanes

**A-P0 — ACK + custody (Kun).** Lane ACKs; `receipts/KUN_INPUT_CUSTODY_RECEIPT.md` pinning all immutable inputs; copy v2 capture/validator/fixtures into the Gate A packet as `*_v3` working copies (v2 originals in the repair packet stay untouched).

**A-P1 — RED pin derivation (Lana, high reasoning; Hwao countersign REQUIRED before any implementation).** `design/LANA_R3_RED_PIN.md`: the complete predicted r3-on-sealed-capture residue, derived from `CONTRACT_R3_DRAFT.md` §D6 + the sealed capture. Known-direction anchors (deviate ⇒ STOP + adjudicate, T14 pattern): the 8 Section-2 Result-cell `UNCITED_CELL_CLAIM` findings are REMOVED by D3 (Citation cells hold resolved chips → row-citation gate passes); RETAINED: the 6 `UNLABELED_COMPARISON` (no tokens in sealed body), the SIMBA `MISSING_QUALIFIER` (no `MODEL_PARAMETER` fill exists in the sealed body), the `NONE_FOUND.` sentinel defect, and the C7 integrity failure (12 orphans, 9 duplicates, 46 blank short names, 14↔29 `NEAR_DUPLICATE` flag). Lana must additionally enumerate every **expected-new** finding the r3 devices raise on the legacy body (missing `CALIBRATION_TARGET_DESCRIPTION:` prefixes in Section-1 cols 1–2; D5 merged-GAP structure failure; any D4 normalization deltas), cell-by-cell with counts. The re-adjudication is diagnostic — it re-scores a pre-r3 body under r3 rules — so expected-new findings are legitimate and must be pinned, not discovered.

**A-P2 — RED authoring (Goru: mechanical tests from the D6 matrix + A-P1 pin; Kun runs; RED receipt + marker).** One test family per D-item, strictly from the D6 rows (positive AND negative fixtures per rule), plus the T-INT integration test pinning the full A-P1 residue on the sealed capture, plus determinism (two byte-identical runs) and custody guards. Real sealed HTML/capture as primary fixture; synthetic r3-shaped fixtures (prefixed calibration cells, `MODEL_PARAMETER` fills, per-paragraph GAPs, named-short-name ledgers) for the positive paths. No assertion may later be weakened without logged Lana+Hwao sign-off.

**A-P3 — vertical GREEN implementation (Tori).** Implement one D-item at a time, in order D5 → D4 → D2 → D1 → D3 (structural/granular first, the sole gate-relaxation last so its effect is isolated in the diff of T-INT results), going green vertically per family before the next; then full suite + T-INT + determinism.

**A-P4 — offline re-adjudication + receipts.** Run v3 on the sealed capture; publish `readjudication_r3/validator_result_v3.json`, `RESIDUE_REPORT_R3.md` (per-finding evidence refs; explicit "diagnostic re-scoring of a pre-r3 body; mechanical only; does not certify science or source fidelity; C1r remains FAIL_CLOSED; no retro-acceptance"), determinism hashes.

**A-P5 — countersigns + close.** Lana post-GREEN conformance review (implementation matches r3 draft wording, D3 preserved guard intact: `EMPTY_CITATION_CELL` still hard-fails); Kun GREEN gate + write-scope audit (rev2 temp discipline); Tori packet receipt; completion marker `markers/C1R_VALIDATOR_R3_IMPL_DONE_20260713T034742Z` last.

## A2. Stop conditions (Gate A)

Any immutable-input hash mismatch; T-INT deviation from the countersigned A-P1 pin (adjudicate, never silently edit); GREEN unreachable without weakening a RED assertion; any write outside the Gate A packet; any network/browser/live call (Gate A has NO network allowance at all); Goru quota cap (≤40% of the 5h window); D3 implementation found to relax anything beyond the accepted verbatim impact (e.g. empty Citation cell not hard-failing) ⇒ immediate STOP to Hwao/Duho.

---

# GATE B — manual source verification of the 73 routed entries

## B1. Verdict vocabulary (Hwao-pinned; binding before any review; changes only by logged Hwao amendment)

| Verdict | Meaning | Fail-closed effect |
|---|---|---|
| `SUPPORTED` | Primary-source full text (or sufficient retrieved span) directly supports the claim at the claimed scope | Eligible for later quarantine-release — release itself is NOT performed in Gate B |
| `SUPPORTED_WITH_SCOPE_NOTE` | Supported, but with a material scope caveat (narrower sample/redshift/tracer/selection than the cell implies) | Eligible for later release **with** the note attached |
| `NOT_SUPPORTED` | Source located and read; claim absent or contradicted | Stays quarantined; flagged to the residue for the future r3 run |
| `SOURCE_UNRESOLVED` | Citation cannot be located via the approved routes | Stays quarantined; treated as not usable |
| `EVIDENCE_INSUFFICIENT_ABSTRACT_ONLY` | Only abstract/metadata reachable; consistent but not sufficient | Stays quarantined; **never** counts as support |
| `AMBIGUOUS_NEEDS_EXPERT` | Located and read; support judgment requires domain expertise beyond mechanical span comparison | Stays quarantined; routed to human expert list |

Rules: exactly one verdict per entry (73/73); doubt resolves to the **lower** verdict (order as listed, bottom = lowest); abstract-only evidence is always labeled as such and can never yield `SUPPORTED*`; no scientific conclusion may be drawn from metadata; the 8 `VERIFY_SCIENTIFIC_COMPARABILITY` entries additionally record a one-line semantic assessment of the token (the uniform `MATCHED_SELECTIONS` set — the FLAMINGO kSZ row is a known suspect) with `AMBIGUOUS_NEEDS_EXPERT` freely available. Gate B changes **no** product/DB/wiki/trust state — verdicts are a ledger for a later application gate.

## B2. Evidence sufficiency hierarchy (descending; record the tier used per entry)

1. **T1 local** — sealed/repair/r3 packet artifacts and any already-verified local store;
2. **T2 arXiv** — abs page + full text (PDF/HTML);
3. **T3 DOI/publisher** — landing page and openly accessible full text;
4. **T4 ADS** — metadata/full-text links, read-only; authenticated ADS API GET only if a token is already configured (presence verified as boolean only — never printed, never pasted into any file);
5. **T5 abstract-only** ⇒ verdict capped at `EVIDENCE_INSUFFICIENT_ABSTRACT_ONLY`.

Aggregator/secondary pages (e.g. the OpenAIRE landing behind chip 27) are resolution stepping-stones only — NEVER evidence. Per-entry custody: exact quoted evidence span (≤50 words) + location (section/page), retrieval URL, UTC, HTTP status, sha256 of the saved copy stored under `sources/` (fetch once, reuse from store).

## B3. Read-only network policy (Gate B only)

GET-only against arxiv.org, doi.org → publisher landing, ADS; no logins, forms, POSTs, cookies-dependent flows, or browser automation (plain HTTP client only); honest user-agent; ≤1 request per 2s per host; ≤200 total fetches (budget; ~62 unique sources expected — exhaustion ⇒ partial receipt + Hwao); 3 consecutive failures on a host ⇒ stop that host, record; every fetch logged in `sources/FETCH_LOG.jsonl` (URL, UTC, status, bytes, sha256). Paywalled/login-gated full text ⇒ do NOT attempt bypass; drop to the next tier or cap the verdict. Any credential prompt beyond the configured ADS token boolean ⇒ skip and record; any risk of credential exposure ⇒ STOP.

## B4. Phases and lanes

**B-P0 — ACK + custody (Kun):** pin `TRIAGE_LEDGER.json` (`81c3d75d…fff2`) and upstream hashes; freeze the 73 routes as fixed inputs (47/18/8).
**B-P1 — retrieval + custody store (Tori):** resolve and fetch per B2/B3; build `sources/` + `FETCH_LOG.jsonl`; no verdicts.
**B-P2 — mechanical first-pass (Goru):** per entry, claim text vs retrieved span candidates — draft comparison notes only, no verdicts; quota cap standing.
**B-P3 — verdicts (Lana, high reasoning):** one pinned verdict per entry with evidence span + tier + scope note; comparability entries get the semantic token assessment. Lana↔Goru divergences: Lana decides, logged per entry.
**B-P4 — audit (Kun):** 73 exactly once; verdict enum only; every verdict carries tier + evidence refs (or the unresolved/abstract-only reason); fetch-log ↔ store ↔ ledger consistency; network-policy conformance from the log (rates, hosts, GET-only).
**B-P5 — Hwao review + close:** Hwao samples ≥15 verdicts covering every non-empty verdict class (min(2, class size)), adjudicates any dispute, countersigns; Tori packet receipt; completion marker `markers/C1R_SOURCE_VERIFICATION_DONE_20260713T034742Z` last. Deliverables: `verification/VERDICTS.jsonl` + `verification/VERDICT_LEDGER.md` (73 rows, arithmetic by lane × verdict), receipts.

## B5. Stop conditions (Gate B)

Ledger/route-input hash mismatch; any write outside the Gate B packet; any non-GET or authenticated action beyond the ADS boolean; fetch budget exhausted; credential/secret exposure risk; any pressure to mutate wiki/DB/trust/prose (out of scope by boundary); an entry that cannot take exactly one verdict under B1 (escalate — no silent vocabulary growth); Hwao-sample disagreement rate >2 of 15 ⇒ full re-review of the affected class before close.

---

## C. Independent countersign requirements (both packets)

Gate A: Hwao countersign of the A-P1 RED pin (before implementation); Lana post-GREEN conformance review; Kun GREEN gate + write-scope audit; Tori packet receipt. Gate B: Kun audit receipt; Hwao verdict-sample countersign; Tori packet receipt. Neither packet's completion marker is written until its countersign set is complete; no lane self-certifies work it authored (the repair-packet supersession rule stands).

## D. Completion criteria and the Gate C condition (recommendation only — never started here)

**Gate A complete:** all D1–D5 test families GREEN with no weakened assertions; T-INT matches the countersigned pin; determinism byte-identical; immutable inputs unchanged; receipts + `RESIDUE_REPORT_R3.md` published; marker written.
**Gate B complete:** 73/73 verdicts with full custody; Kun audit PASS; Hwao sample countersign; network log clean; marker written.
**Gate C (live one-simulation canary) may be RECOMMENDED — in a coordination-packet `HWAO_GATES_AB_SYNTHESIS.md`, not started — only when ALL of:** both gates complete; Gate B's verdict profile reviewed (specifically the `NOT_SUPPORTED`/`SOURCE_UNRESOLVED` rate among the 47 source-fidelity entries and the comparability assessment of the uniform `MATCHED_SELECTIONS` tokens); the r3 contract finalized from the draft including the "Joint C1R answer" title decision; and Duho grants a fresh explicit gate. Any `NOT_SUPPORTED` verdict on a load-bearing Section-2 row is surfaced verbatim in that synthesis before any recommendation.

HWAO_GATES_AB_PARALLEL_PLAN_DONE_20260713T034742Z
