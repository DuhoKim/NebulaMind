# WEB_OPERATOR_PACKET — Supervised Gemini Web (AI Ultra) run: r2 six-card M3 prompt
Packet ID: `WEB_OPERATOR_PACKET_pilot-gemini-resume-20260711T050514Z` · Issued by Hwao · **ADVISORY-ONLY OUTPUT**

## 1. Authorization
- Scope: `DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`.
- **Fresh explicit approval: granted by Duho at 20260711T050514Z** (pilot-resume direction) for **exactly one** supervised browser run of this REQ. This is the run's P1 approval reference. No second run, no retry, without a fresh Duho-approved brief.
- Contract of record: hard-burn H2 packet
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z/h2-gemini-req-contract/GEMINI_SIDECAR_REQ_CONTRACT_PACKET.md`
  (its §B scorecard, §C checklist, §E failure playbook all apply). Two pilot amendments in §3 below.

## 2. Consumer-quota preflight (fresh — do this first, fail closed)
1. Log into the consumer Google account with the **Gemini AI Ultra** plan at `gemini.google.com`. Do not switch accounts, plans, or extensions.
2. Open the plan/usage surface (Google One → Gemini / app-compute usage). Duho's snapshot at 20260711T050514Z: **~1% app compute used** — confirm it is still low.
3. **Abort thresholds (STOP, write VOID marker per §6):** app compute ≥80%; any billing/upsell/upgrade interstitial demanding action; any account-verification demand beyond normal login.
4. Record: screenshot to `web/screenshots/quota_preflight_<UTC>.png` and one line (UTC, % used, verdict PROCEED/ABORT) — this line goes into `meta.md` at capture time. Repeat the check after the run (`quota_postrun_<UTC>.png`).
5. No purchases, no /credits, no quota-affecting account changes — per-step Duho approval would be required and is NOT granted here.

## 3. Pilot amendments to the H2 checklist (everything else in H2 §C applies verbatim)
- **(i) Capture location override (H2 C/P4):** capture dir lives under THIS handoff root:
  `web/answers/REQ_M3_RT_20260711T091128Z-r2-<UTCSTART>/` (contents unchanged: `body.md`, `meta.md`, `CAPTURE_RECEIPT.md`). All operator writes stay under `pilot-gemini-resume-20260711T050514Z/web/`.
- **(ii) Paste-source variant (H2 C/P2):** the live REQ file is NOT being adopted/modified in this pilot resume. You paste the r2 text embedded in §5 below, which Hwao copied verbatim from H2 §A **minus the OPERATOR-SIDE adjudication-reference block** (exactly what H2 step R2 prescribes for pasting). Before pasting, spot-verify against H2 §A: the `**Revision:** r2` line, the six-card mapping table, contract items C1–C8, and the C8 marker string `GEMINI_WEB_M3_RT_OUTPUT_DONE_REQ_M3_RT_20260711T091128Z` must all be present and identical. Any mismatch ⇒ STOP, VOID marker, escalate to Hwao/Duho (running a non-r2 text re-creates the cycle-7 failure surface). Record in `meta.md`: `paste_source: WEB_OPERATOR_PACKET.md §5 (verbatim from H2 §A minus OPERATOR-SIDE block)`.

## 4. Operator checklist (single supervised conversation)
1. ☐ P1: record UTC start, operator name, approval ref (= Duho direction 20260711T050514Z + this packet path).
2. ☐ §2 quota preflight → PROCEED.
3. ☐ P3: baseline custody — `shasum -a 256` of `M3_ACCEPTANCE_BASELINE.md` (in `fable-weekly-burn-20260711T010503Z/p3-m3-rt-baseline/`) must equal `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433`; mismatch ⇒ STOP.
4. ☐ P5: check for STOP/HOLD coordination files in the mastermind dir and this handoff root; SPRINT_STATUS may be glanced at read-only; runner PID 45665 is untouched no matter what.
5. ☐ Create the capture dir (§3.i) and `web/screenshots/` captures as you go (paste moment, mid-run, completion).
6. ☐ R1/R2: new conversation; Deep Research per the prior successful operator precedent (`TORI_GEMINI_WEB_OPERATOR_RETRY_SUCCESS_20260707T140944Z.md`); paste EXACTLY the §5 block between the BEGIN/END sentinel lines (sentinels excluded); no other instructions, no follow-up steering; human watches the full generation.
7. ☐ R3: if visibly truncated, at most ONE neutral "continue", logged in `meta.md`. If Gemini asks to browse/act beyond producing text: decline and log. R4: no mid-run edits to any local file.
8. ☐ E1: save answer body EXACTLY as produced to `body.md` (answer only, no prompt echo — the C8 marker check applies to `body.md`).
9. ☐ E2: `meta.md` — model/product label as displayed, conversation URL, UTC start/end, operator, approval ref, paste_source line, quota preflight/postrun lines, continue events, anomalies.
10. ☐ E3: confirm `## Links ledger` exists in `body.md`; if omitted, that is a contract failure — do NOT reconstruct it inside `body.md`.
11. ☐ E4/E5: `CAPTURE_RECEIPT.md` with `wc -c` + `shasum -a 256` for every captured file; all captured files immutable afterward. No adjudication on un-hashed text.
12. ☐ §6 marker (fail-closed), then hand off to adjudication (§7). Operator does not adjudicate mid-run.

## 5. PASTE TEXT — r2, six-card M3 (copy everything BETWEEN the sentinel lines; sentinels and code fence excluded)

-----BEGIN PASTE r2 REQ_M3_RT_20260711T091128Z-----
```markdown
# Gemini-Web Deep Research Request for Method 3 RT Quality

Marker: `RT_GEMINI_WEB_DEEP_RESEARCH_SIDECAR_PROTOCOL_V1`

**Request ID:** `REQ_M3_RT_20260711T091128Z`
**Revision:** r2 — contract-hardened candidate (drafted offline by hard-burn H2, 2026-07-11).
Adoption and the run itself are gated on separate Duho approval under
`DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`.
**Method:** Method 3 (Debate-map-to-wiki rebuild)
**Current RT artifact paths:**
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- Byte-identical snapshot copies exist under
  `.hermes/handoffs/galaxy-evolution/static-publish-20260709T124353Z/live-root-before/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/`
  (md sha256 `4f8e7fb0f272837b9b075f028cfb20ee89849e83383de104353fd529289abb56`).

**Exact topic/cards to improve:**
All 6 canonical research topic cards targeting Galaxy Evolution open questions. The artifact
at the paths above holds 3 consolidated proposals; the six canonical cards are the six-card
prospectus version (order marker
`AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z`). Answer
card-by-card against this mapping:

| Card | Canonical title | In current artifact |
|---|---|---|
| 1 | Isolating the causal contribution of AGN feedback to central-galaxy quenching | absorbed into P1/P3 (no standalone proposal) |
| 2 | A tracer-resolved, common-denominator census of AGN-driven outflows | Proposal P1 |
| 3 | Distinguishing reservoir removal from inefficient star formation | Proposal P2 |
| 4 | An observational determination of the maintenance-heating duty cycle | dropped in consolidation (still canonical) |
| 5 | Forward-modeled validation of simulation feedback predictions | Proposal P3 |
| 6 | Rebalancing the multi-channel evidence base: chemical, structural, high-redshift | downgraded to "Methodological note" |

All six cards MUST be addressed. A card with nothing to add still gets its full section
skeleton (contract C2) with `NONE_FOUND` fields (contract C3). Cards 1 and 4 being absorbed/
dropped in the current artifact is an editorial consolidation, not a scientific resolution;
answer them as first-class cards.

**Existing source-basis links/claim IDs that must not be contradicted:**
Local evidence anchors from `evidence-basis-20260708T014205Z.md#s2` to `#s8`. A cited external
study that disagrees may be reported as that study's claim — linked and flagged for local
verification — but the answer must not assert the contradiction as settled fact in its own
voice.

**The question Gemini should answer:**
What major recent (2020+) literature reviews or high-impact studies are missing from these
cards? Are the proposed decision criteria realistic given current JWST and ALMA survey
capabilities?
Note on question 2: cards 1 and 4 are primarily optical/X-ray/radio territory. For those
cards, "JWST/ALMA marginal here — the relevant capability is <instrument family>" is a
first-class, complete realism answer when justified. Do not force-fit JWST/ALMA relevance.

**Expected output shape — BINDING OUTPUT CONTRACT (new in r2):**

- C1 (meta header). The answer is ONE self-contained markdown report body. Its first lines
  are a meta block:

      # M3 RT sidecar answer — REQ_M3_RT_20260711T091128Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ, operator-verified>
      Model: <model/product self-identification>
      Cards addressed: <N> of 6

- C2 (per-card section contract). For EACH card 1–6, in ascending order, exactly these seven
  headings, echoing the canonical titles verbatim:

      ## Card <N> — <canonical title from the mapping table>
      ### <N>.1 Prior-study findings (with source links)
      ### <N>.2 What remains unknown
      ### <N>.3 Recommended data/survey families
      ### <N>.4 Test/decision-criteria realism (JWST/ALMA or stated alternative)
      ### <N>.5 Overclaim risks
      ### <N>.6 Key papers to verify

- C3 (empty-field device). A field with genuinely nothing to report contains exactly
  `NONE_FOUND` — never silently omitted, never padded with filler.

- C4 (citation labeling). Every named study, review, survey, catalogue, or number carries a
  checkable citation (arXiv ID, DOI, ADS bibcode, or URL) on the same line, or the same-line
  label `UNCITED_NOT_USABLE`.

- C5 (wording contract). In the answer's own voice, settled/causal register about what
  evidence or statistics show is banned (case-insensitive): establish / establishes /
  established / establishing, proves, proven, confirms that, settles, settled question,
  resolves the debate, definitively, conclusively, is now known, "demonstrates that … causes".
  Association-only results stay association-only. A source's own claim in that register may be
  quoted only as explicit attribution with a checkable citation ("Author (year) claim: …").

- C6 (estimand labels). Any absolute quantity (absolute SFR/sSFR medians, simulation medians,
  single-object outflow rates) set beside a differently defined statistic (matched-control
  differences, per-tracer fractions with different denominators) must be explicitly labeled
  non-commensurable; no "remarkably close" / "consistent with" claims across unlike estimands.
  Every incidence/prevalence number carries all four qualifiers: tracer + selection +
  denominator + redshift range.

- C7 (links ledger). After Card 6, a section `## Links ledger` lists every cited item, one per
  line: `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.

- C8 (completion marker). The exact string

      GEMINI_WEB_M3_RT_OUTPUT_DONE_REQ_M3_RT_20260711T091128Z

  must appear exactly once in the report body, as the standalone final non-empty line of the
  body file. A marker present only in a chat-UI completion element and not in the body counts
  as ABSENT and the run is rejected.

**Explicit safety locks copied from protocol:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not use Gemini-generated DOI/ADS/arXiv IDs until checked locally.
- Do not import numeric results unless supported.
```
-----END PASTE r2 REQ_M3_RT_20260711T091128Z-----

(Per H2 step R2 the OPERATOR-SIDE adjudication-reference block is deliberately excluded from the paste; adjudication rules live in H2 §B and §7 below.)

## 6. Fail-closed markers + metadata (orchestrator watches for these)
- **Complete capture** (all of: `body.md`, `meta.md`, `CAPTURE_RECEIPT.md` with hashes, quota preflight+postrun screenshots): write `web/WEB_RUN_CAPTURED_20260711T050514Z` containing the capture dir path and `body.md` sha256.
- **Anything missing, aborted preflight, paste-verification mismatch, or any doubt:** write `web/WEB_RUN_VOID_20260711T050514Z` with a one-line reason. A VOID run yields nothing — no leads may be harvested from un-hashed or partial text.
- Exactly one of the two markers must exist at the end. Never both, never neither.

## 7. Adjudication (separate step, required before ANY use)
- Adjudicator: a Claude lane or Hwao under quintet review — never the operator mid-run; requires a second quintet sign-off before any content influences any writer slot.
- Procedure: H2 §B fail-closed order — global gates G1–G8 (stop at first failure ⇒ wholesale `REJECT_RETAIN_VERIFIED_SOURCE_LEADS_ONLY`), floors F1–F5, per-card CHKs, B.4 summary + wholesale verdict — scored against `M3_ACCEPTANCE_BASELINE.md` (sha256 pinned in §4.3). Mechanical checks A1–A3 (marker grep/awk, banned-register grep, heading counts) are mandatory and quoted in the adjudication file.
- Output: `web/ADJUDICATION_REQ_M3_RT_20260711T091128Z-r2.md`, citing `body.md` line numbers; captured files are never edited.
- Disposition regardless of verdict (H2 A6): every ID `QUARANTINED_PENDING_LOCAL_CHECK`; cited leads → Tori local-verification queue; NOTHING imported into wiki/candidates/runner artifacts; no claim/cite binding; the answer text is never evidence. Even a full pass is **advisory leads only**.
