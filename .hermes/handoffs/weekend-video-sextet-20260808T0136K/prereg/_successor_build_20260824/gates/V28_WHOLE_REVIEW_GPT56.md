# V28 WHOLE-DOCUMENT REVIEW — GPT56

## Verdict

**CLEAR.** The exact V28 subject bytes match the dispatched SHA-256; the required live trace check exits 0 with 27 computed transitions and 0 problems; §10 describes the checker contract and does not assert that this V28 run passed; all 26 in-band table rows exactly match an independent regeneration of every mechanical column and the findings map; and the V27→V28 sidecar cites only the four V27 findings this delta answers. The held Clause 10, threshold/phase/effect, Stage-P, VOID, catalogue-quality, and line-378 states remain intact.

## Digest first — exact comparison

I computed SHA-256 directly over the current bytes of `../PREREG_SUCCESSOR_DRAFT_V28_20260827.md` and compared all 64 hexadecimal digits with the subject pin in `BRIEF_V28_WHOLE_REVIEW.md` lines 3–5.

- brief pin: `82cd8ac3690fb87b9cf123719cf29f8af37af70e93652ee7e8a2da2b3ee8b587`
- independently recomputed V28: `82cd8ac3690fb87b9cf123719cf29f8af37af70e93652ee7e8a2da2b3ee8b587`
- comparison: **MATCH — exact 64-hex equality**

## Required checker execution

From the repository root I ran the real checker against the pinned V28 subject:

`python3 tools/prereg_trace.py .hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824 --check .hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V28_20260827.md`

It returned exit code **0** and exactly:

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V28_20260827.md
  27 computed transition(s); 0 problem(s)
```

I did not accept the drafting account of this result.

## Numbered findings

**No blocking or non-blocking findings.**

## Required adjudications and failed attacks

### 1. §10 result-claim attack — FAILED

V28 §10 lines 815–820 states a contract: table-scoped in-band coverage through the subject's predecessor, current-transition ownership in `gates/FINDINGS_MAP.md`, a named V1→V15 exemption, and a row-local result-digest requirement. It does **not** say the V28 check passed, is clean, returned zero problems, or equivalent. A programmatic search confined to §10 found no `pass`, `passed`, `passes`, `passing`, `clean`, `zero problems`, or `0 problems` result token. Line 851 describes what the tool enforces; it is contract/capability language, not an assertion of this run's outcome.

### 2. Regenerated-table honesty attack — FAILED

I independently called the current `prereg_trace.py` build/render path over the draft directory, retained only transitions through V26→V27 (the subject's predecessor), and compared complete markdown rows rather than merely checking transition names or endpoint fragments.

- computed transitions available: 27, including current V27→V28
- expected in-band rows through V26→V27: 26
- actual §10 transition rows: 26
- exact complete-row matches: 26/26

Thus every displayed predecessor digest, result digest, changed-section list, added/removed line count, §7 row-count change, and findings column matches the independent regeneration/current sidecar. This is stronger than the checker’s exit alone.

### 3. Checker regression/canary attack — FAILED

In an automatically deleted `_tmp_v28_trace_*` mirror under this gate directory, I exercised the corrected checker rather than trusting its comments:

- baseline: exit 0, `27 computed transition(s); 0 problem(s)`;
- deleting only current `V27→V28` from the sidecar: exit 1 with `SIDECAR MISSING: V27 → V28`;
- deleting only the V24→V25 row from the §10 table while leaving §6.3's prose mention intact: exit 1 with `MISSING: no §10 table row for V24 → V25`;
- replacing only the V26→V27 row's result digest: exit 1 with `UNPINNED: V26 → V27 row does not carry its result digest`.

The three V27 failure mechanisms therefore no longer survive: the current transition is checked in the sidecar, presence is scoped to the §10 table, and a row must carry its own result digest.

### 4. V27→V28 findings-map overreach attack — FAILED

`gates/FINDINGS_MAP.md` line 21 maps the current transition only to `GPT56-V27-1`, `GPT56-V27-2`, `GPT56-V27-3`, and `CODEX-V27-1`. I opened both V27 reports and compared those findings with the actual V27→V28 draft diff and corrected checker behavior.

Those IDs are exactly the findings about: the failed asserted enforcement, the skipped/absent current-transition sidecar mapping, document-wide rather than table-scoped presence, and row-local digest masking. The V27→V28 draft delta changes only the version heading and §10: it replaces the result assertion with contract language, regenerates omitted/truncated table content, and adds rows through V26→V27. The sidecar does not cite unrelated science, custody, threshold, or standing-state findings.

### 5. Clause 10 forward/reverse and threshold-neighbour attack — FAILED

I reread the lifecycle table, its neighboring clauses, §5 outcome registry, §6.3 admissibility/void rules, and §7.1 antecedent registry. The V27→V28 diff makes no change to these normative surfaces.

- **Forward termination:** Rows A–S retain stated surfaces, phases, authorizations, emissions, and failure effects. Row P retains the closed precedence tree for missing, duplicate, orphan, malformed, absent, non-finite, low-confidence, and accepted-finite states. Row J retains calibration and Stage-C terminal consequences.
- **Reverse reachability:** Clause 10 line 580 does not overclaim closure. It says `VOID` reverse reachability is unresolved, Clause 10 is not executable, and BS-6 plus the first image byte remain blocked until every enumerated void antecedent has a pinned producer/conversion. BS-2v remains DESIGN/UNRESOLVED, so the open reverse direction is represented as a block rather than silently treated as passing.
- **Catalogue quality:** exact thresholds remain `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, and `nobs_r >= 3`; the phase is pre-BS-2f/P2–P3 and the effect is ordinary nonfatal catalogue-quality exclusion into the 49,211 mask. It is not reintroduced as a post-unblinding Row-P removal.
- **Calibration:** `a_LB_b < 0.85` remains a pre-unblinding `INCONCLUSIVE-BY-CALIBRATION` halt; its complement `a_LB_b >= 0.85` is required before Stage C. Spread `<= 0.03` selects scalar, while spread-only failure selects profile rather than terminating.
- **Power:** the planning boundary remains x ≥ 962/1,000; the historical 995/1,000 result is marked `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK` at both live surfaces, and BS-5p remains unfillable pending rerun. Stage-C failure, including fewer than 962/1,000 or self-verification failure, yields `INCONCLUSIVE-BY-POWER` before unblinding.
- **Post-unblinding adequacy:** any Row-P removal remains `INCONCLUSIVE-BY-CALIBRATION`, with no Stage-C rerun. Numeric p/amplitude/floor thresholds remain confined to the post-unblinding numeric verdict phase.

### 6. Held-state preservation attacks — FAILED

- V26, V27, and V28 line 378 are byte-for-byte identical. The sentence claims only outcome-blind chronology and explicitly says conditional independence from handedness is **not established**.
- `VOID-6.1C2-ATTESTATION-FAIL` has zero occurrences; it was not recreated with a fabricated antecedent.
- The exact `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK` Stage-P label occurs twice.
- `prereg_counts.py` returns 15 class-P rows, 8 class-E rows, and prose matching the table; only BS-2m is claimed filled.
- `prereg_lint.py` returns 23 §7 data rows, 15 class P, 8 class E, and `no inconsistencies found`.
- The standing state remains explicit: BS-2a DESIGN/UNFILLED; one of fifteen class-P slots filled; BS-2v UNRESOLVED; findings 1, 2, 2b, and 3 UNRESOLVED; Rows C2 and E cannot run; Stage P superseded pending rerun; BS-6 and the first image byte blocked.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`, as prohibited.
- I did not fetch or authorize any image byte, execute Stage P, run inference, unblind data, mutate git, or alter the subject, predecessors, checker, or permanent sidecar.
- Survey provenance, scientific-source authenticity, and the factual claim that no image byte has been fetched are Testimony in this pass. I checked document-level values, phase/effect consistency, trace bytes, and executable checker behavior.
- The mutation tests used only a temporary mirror inside the assigned gate directory; it was deleted automatically. The only durable write is this report.

## Evidence ledger

Files read for content: `BRIEF_V28_WHOLE_REVIEW.md`; pinned V28 subject; V27 subject for the exact delta; both V27 whole-review reports; `gates/FINDINGS_MAP.md`; and complete `tools/prereg_trace.py` source. V26 was read only for exact line-378 preservation and trace recomputation.

Independent executions: V28 SHA-256; exact V27→V28 diff; required V28 `prereg_trace.py --check`; exact 26-row render/table comparison; three mutation canaries plus baseline; V26/V27/V28 line-378 byte comparison; §10 result-token search; orphan-ID and Stage-P-label counts; `prereg_counts.py`; and `prereg_lint.py`.

**CLEAR**