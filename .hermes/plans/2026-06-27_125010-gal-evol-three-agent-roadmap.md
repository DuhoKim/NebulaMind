# Gal Evol Three-Agent Roadmap Plan

> **For Hermes:** Use this as a read-only roadmap until the user separately approves a mutation packet. Do not implement DB/prose/trust/threshold changes from this plan directly.

**Goal:** Move `/wiki/galaxy-evolution-v2` toward the original NebulaMind wiki idea: a research-grade Galaxy Evolution article with sentence/claim-level evidence, calibrated trust, review-ready provenance, and safe-to-publish gates.

**Architecture:** Separate review intake from mutation. First freeze the live page and label artifacts, diagnose calibration failure modes, build a representative human-audit queue, and only then prepare separate backup/rollback/exact-diff packets for any future DB vote, prose publish, trust badge, or threshold change.

**Tech Stack / Surfaces:** NebulaMind wiki page API, static report artifacts under `frontend/public/human-cal` and `frontend/public/agent-reports`, calibration labels JSON/CSV, Galaxy design docs, eventual backend trust/evidence tables only behind explicit approval packets.

---

## Current verified baseline

### Live/public page snapshot

Read-only public API probe on 2026-06-27 KST returned:

- Page id: `58`
- Slug: `galaxy-evolution-v2`
- Title: `Galaxy Evolution (Intro-Synthesis V2 Pilot)`
- Version: `4`
- Content length: `11855`
- Content SHA256: `af8a8c739c55a4a85b298ec0d62683f5b2f03b38fc5ecf3f14bdfcea176b0055`
- H2 count: `7`
- H2s:
  - `Trust-bearing claims`
  - `Cosmic foundations and halo assembly`
  - `Environmental quenching`
  - `Star formation and the baryon cycle`
  - `Feedback, black holes, and outflows`
  - `High-redshift frontier and survey tensions`
  - `Structure, morphology, and size growth`
- Claim marker count: `8`
- URLs in body: `0`

### Completed post-label readiness facts

Source report:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/human-cal/galaxy-post-label-readiness-analysis-20260627T121535Z.json`

Important fields:

- Status: `GO_FOR_READ_ONLY_REVIEW_INTAKE__NO_GO_FOR_AUTOMATED_RETUNE_OR_MUTATION`
- Labels reviewed: `28/28`
- Human decisions:
  - `nuance_only`: `16`
  - `drop_no_effect`: `10`
  - `count_as_support`: `1`
  - `count_as_weakening`: `1`
- Human-counted rows:
  - `c2929-e28074`: weakening, claim `2929`
  - `c2929-e28095`: support, claim `2929`
- Production machine counted rows in packet: `0`
- Assistant counted hints: `8`
- Same-sign matches among assistant counted hints: `0/8`
- DB writes executed by readiness work: `0`
- Galaxy prose edits executed: `0`
- Trust badge changes executed: `0`
- Threshold retunes executed: `0`
- Apply SQL generated: `false`

### Repo hygiene baseline

Active repo:
`/Users/duhokim/NebulaMind/NebulaMind`

Current branch:
`feat/surveys-atlas-ia-p1-20260627`

HEAD:
`ac0608c`

Tracked dirty files observed:

- `frontend/package.json`
- `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- `wiki_schema.md`

Many untracked report/static artifacts are present, including `.hermes/`, `docs/*page58*`, `docs/galaxy-post-label-readiness-*`, `frontend/public/agent-reports/`, `frontend/public/human-cal/`, and related report scripts/pages.

---

## Original goal anchors

### Galaxy Evolution research-grade article goal

Design file:
`/Users/duhokim/.openclaw/workspace/설계_GalaxyEvolution_Research_v1.md`

The locked v3 “Dissolution Model” says the target page should be a pure scientific review article, not a dataset/tooling portal. Key acceptance criteria:

- 12,000–15,000 chars.
- Exactly 8 content sections, plus See Also and References.
- No standalone `Open Questions / Active Debates` section.
- No standalone `Recent Advances / Research Frontiers` section.
- Debates woven into topical prose.
- 25–35 total claims.
- D1–D10 appear as woven prose in assigned topical sections.
- References list ≥20 entries.
- Zero URLs / dataset links in page body.
- No banned pop-science phrases.
- Provenance chip exactly reflects the intended synthesis tier.
- Independent senior-reader review recognizes contested ground from prose alone.

### Wiki V2 trust/evidence goal

Design file:
`/Users/duhokim/NebulaMind/NebulaMind/WIKI_V2_DESIGN.md`

The original wiki idea is not just better prose. It is sentence/claim-level trust and evidence:

- Trust visualization by consensus level.
- Evidence links for individual claims/sentences.
- Evidence-level voting/comments.
- Trust recalculation based on evidence and votes.
- A readable “clean view” that does not make the article visually noisy.

### Updated evidence-generation direction

Persistent direction from prior work: prefer distillation from multiple paper introductions. Treat older prose-to-matching-evidence / keyword-excerpt paths as legacy unless explicitly requested.

---

## Three-agent inputs

### Hermes view

The safe path is: freeze baseline, use exported labels as review input only, diagnose why assistant triage over-called counted votes, expand human audit coverage, and only then prepare separate exact-diff packets for any mutation class.

### Lana view

Lana’s max-effort Opus lane concluded:

- HOLD on all mutation.
- Read-only audit and packet preparation are GO.
- Do not couple future mutation to the current dirty branch.
- Define falsifiable gates: calibration understood, sufficient human sample, packet completeness, scope isolation, branch hygiene.
- Suggested sample floors before trust/threshold claims:
  - single-claim conclusion: at least `N >= 20` human-counted/relevant examples.
  - page-wide trust signal: at least `N >= 50` representative examples.
- Immediate focus: dump the 8 unsafe counted hints, cross-reference the 2 human-counted rows, publish calibration definitions, expand the audit queue, and triage repo dirtiness.

### Goru view, corrected for safety

Goru correctly emphasized machine-checkable inventories:

- calibration registry,
- claim 2929 candidate registry,
- blocked triage hints log,
- dirty-tree inventory,
- audit queue schema/manifest,
- acceptance checks around page SHA, label counts, and blocked automated integration.

However, Goru also suggested generating SQL inserts and verification scripts. This plan rejects those as premature. Any SQL/apply script belongs only in a separate backup/rollback/exact-diff approval packet.

---

## Phase plan

### Phase 0: Freeze and name the baseline

**Objective:** Prevent page/version confusion before more work.

**Read-only steps:**

1. Record the live page invariant:
   - id `58`
   - slug `galaxy-evolution-v2`
   - version `4`
   - SHA `af8a8c739c55a4a85b298ec0d62683f5b2f03b38fc5ecf3f14bdfcea176b0055`
2. Record the label artifact and readiness report paths.
3. Record the dirty branch and dirty files.
4. State explicitly: “No DB/prose/badge/threshold mutation is authorized.”

**Output artifact:**

- `docs/galaxy_v2_baseline_lock_YYYYMMDDTHHMMSSZ.md`
- `docs/galaxy_v2_baseline_lock_YYYYMMDDTHHMMSSZ.json`

**Validation:**

- Public API content hash still equals the frozen SHA.
- Report metadata says `db_writes_executed: 0`.

---

### Phase 1: Define calibration vocabulary before adding data

**Objective:** Make “support”, “weakening”, “nuance”, and “drop” operational and consistent across agents/humans.

**Tasks:**

1. Write a calibration-definition report that defines:
   - `count_as_support`
   - `count_as_weakening`
   - `nuance_only`
   - `drop_no_effect`
   - `same-sign match`
   - `counted hint`
   - `human-counted row`
   - `claim-level conclusion`
   - `page-wide trust conclusion`
2. Explain why assistant triage is not trusted as a write diff:
   - `8` assistant counted hints.
   - `0` same-sign matches.
3. Set minimum sample gates before mutation discussion reopens:
   - single-claim conclusion: provisional `N >= 20` relevant human-audited rows.
   - page-wide trust/threshold conclusion: provisional `N >= 50` representative human-audited rows.
4. Mark these as policy/gate definitions, not DB state.

**Output artifact:**

- `docs/galaxy_v2_calibration_definitions_YYYYMMDDTHHMMSSZ.md`
- `docs/galaxy_v2_calibration_definitions_YYYYMMDDTHHMMSSZ.json`

**Validation:**

- The artifact has no SQL/apply script.
- It cites the two human-counted rows and the 8 unsafe assistant counted hints.

---

### Phase 2: Build the diagnostic inventory and audit queue

**Objective:** Convert current labels into review work, not writes.

**Tasks:**

1. Produce `claim_2929_candidate_registry`:
   - `c2929-e28074`: human weakening.
   - `c2929-e28095`: human support.
2. Produce `blocked_assistant_hints_log`:
   - all 8 assistant counted hints,
   - assistant sign,
   - human final decision,
   - why not writeable.
3. Produce `targeted_audit_queue_v2` with row categories:
   - human-counted rows,
   - assistant-counted but human-noncount rows,
   - assistant/human disagreement rows,
   - consensus weakening drivers,
   - same-source repeated rows,
   - metadata cleanup rows,
   - control rows from obvious `drop_no_effect` examples.
4. Include claim id, evidence id, sample id, source title/arXiv if available, current claim text, human label, assistant recommendation, and audit reason.

**Output artifacts:**

- `docs/galaxy_v2_claim_2929_candidate_registry_YYYYMMDDTHHMMSSZ.csv`
- `docs/galaxy_v2_blocked_assistant_hints_YYYYMMDDTHHMMSSZ.csv`
- `docs/galaxy_v2_targeted_audit_queue_YYYYMMDDTHHMMSSZ.csv`
- `docs/galaxy_v2_targeted_audit_queue_YYYYMMDDTHHMMSSZ.json`

**Validation:**

- Counted human candidates exactly `2`.
- Assistant counted hints exactly `8`.
- Queue references the original sample ids.
- Queue is explicitly `review_only: true` and `no_apply: true`.

---

### Phase 3: Audit page architecture against the research-grade article target

**Objective:** Separate “content quality gaps” from “trust calibration gaps”.

**Current known architecture gaps to evaluate:**

- Current page has `7` h2 sections, while the locked v3 target expects `8` content sections plus See Also and References.
- Current page has `8` claim markers in the live API snapshot, while the target says `25–35` total claims.
- Current page has no URLs in body, which matches the target.
- Current h2 `High-redshift frontier and survey tensions` should be checked against the design ban on standalone “Recent Advances / Research Frontiers” and “Open Questions / Active Debates” style sections.

**Tasks:**

1. Produce a `section_conformance_matrix`:
   - locked v3 section,
   - live v4 section nearest match,
   - missing/merged/renamed status,
   - whether debates/highlights are dissolved into prose.
2. Produce a `claim_marker_inventory`:
   - marker count,
   - claim ids,
   - section placement,
   - open/close marker correctness.
3. Produce a `prose_quality_checklist`:
   - banned phrase grep,
   - no standalone debates/recent-advances section,
   - reference count,
   - no URLs,
   - no code fences,
   - senior-review readability notes.
4. Do not edit prose in this phase.

**Output artifacts:**

- `docs/galaxy_v2_section_conformance_YYYYMMDDTHHMMSSZ.md`
- `docs/galaxy_v2_claim_marker_inventory_YYYYMMDDTHHMMSSZ.csv`
- `docs/galaxy_v2_prose_quality_checklist_YYYYMMDDTHHMMSSZ.md`

**Validation:**

- Public page SHA remains unchanged after report creation.
- Any proposed prose change is described as a future diff, not applied.

---

### Phase 4: Expand human audit before any trust or threshold decision

**Objective:** Get enough representative review input to support a decision.

**Tasks:**

1. Expand beyond claim 2929 to all live v4 claim markers and all locked design debate topics that are represented in the page.
2. Include both likely-support and likely-weakening evidence rows per claim.
3. Ensure sample is representative, not only priority/stress rows.
4. Require explicit labeling of:
   - support / weakening / nuance / drop,
   - confidence,
   - whether the row should affect claim trust,
   - whether it should affect prose wording,
   - whether it is a source-family duplicate.
5. Keep AI/Hermes-assisted labels clearly marked as assisted, not independent human gold.

**Output artifacts:**

- `frontend/public/human-cal/galaxy-v2-human-audit-workspace-YYYYMMDDTHHMMSSZ.html`
- `frontend/public/human-cal/galaxy-v2-human-audit-queue-YYYYMMDDTHHMMSSZ.json`
- `frontend/public/human-cal/galaxy-v2-human-audit-queue-YYYYMMDDTHHMMSSZ.csv`

**Validation:**

- Static HTML/JSON/CSV serve with HTTP 200 locally before sharing.
- Queue declares `db_writes_executed: 0`.
- Queue has stable IDs and can be re-imported for analysis.

---

### Phase 5: Prepare optional preview-only content work

**Objective:** Let us improve quality safely without touching the live page.

**Allowed before mutation approval:**

- Offline prose gap report.
- Offline proposed section outline.
- Offline draft snippets for missing/weak sections.
- Offline citation/evidence mapping.
- HTML preview/report under static report directories.

**Not allowed before separate approval packet:**

- Writing a new `PageVersion`.
- Editing `wiki_pages.content`.
- Changing trust badges.
- Changing claim rows.
- Changing evidence votes.
- Retuning thresholds.

**Output artifacts:**

- `docs/galaxy_v2_preview_outline_YYYYMMDDTHHMMSSZ.md`
- `docs/galaxy_v2_proposed_prose_diff_packet_DRAFT_YYYYMMDDTHHMMSSZ.md`

**Validation:**

- Files are clearly labeled preview/draft.
- The live public SHA is unchanged.

---

### Phase 6: If mutation is requested, create separate approval packets

**Objective:** Keep every mutation reversible and reviewable.

Create one packet per mutation class. Do not bundle them.

#### Packet A: Evidence/vote DB write packet

Required:

- target tables and rows,
- current backup JSON,
- exact row-level diff,
- transaction apply script with drift guards,
- rollback script,
- verification queries,
- approval phrase `APPROVE EXECUTE <packet_id>`.

#### Packet B: Claim trust / trust badge publish packet

Required:

- backup of visible trust rows or rendering source,
- before/after UI preview,
- exact badge/tier diffs,
- rollback,
- browser/DOM verification steps,
- approval phrase `APPROVE PUBLISH <packet_id>`.

#### Packet C: Galaxy prose publish packet

Required:

- backup of current live content and page version metadata,
- exact markdown diff,
- preview render,
- source/evidence citation map,
- rollback to prior version,
- approval phrase `APPROVE PUBLISH <packet_id>`.

#### Packet D: Threshold retune packet

Required:

- representative calibration set,
- stability split by human-only vs assisted labels,
- threshold sweep with numeric features available,
- before/after confusion matrices,
- rollback and verification,
- approval phrase `APPROVE EXECUTE <packet_id>`.

**Current status:** No packet is authorized for execution.

---

## Agent roles

### Hermes

- Owns artifact generation, reproducible scripts, static reports, and final synthesis.
- Runs read-only API/state checks.
- Drafts approval packets when requested.
- Must not self-approve mutation.

### Lana

- Safety/calibration lead.
- Reviews gate definitions, sample sufficiency, and packet completeness.
- Blocks threshold/trust/prose mutation if evidence is insufficient.
- Best used on Opus max-effort lane for high-stakes reasoning.

### Goru

- Mechanical verifier.
- Checks counts, manifests, CSV schemas, marker inventories, dirty-tree inventories, and acceptance checklist outputs.
- Should not generate SQL/apply scripts until a packet is explicitly requested.
- Should stay out of Antigravity brain/scratch and unrelated paths.

---

## Immediate next 48 hours

1. Create the baseline-lock artifact from Phase 0.
2. Create the calibration-definition artifact from Phase 1.
3. Create the claim 2929 registry and blocked assistant hints log from Phase 2.
4. Create the section conformance matrix from Phase 3.
5. Have Lana review the baseline/calibration/section reports for gate correctness.
6. Have Goru mechanically verify row counts, CSV schema, marker counts, and artifact paths.
7. Decide whether to ask the human for more audit labels before any write packet.
8. Do not touch DB/prose/badges/thresholds.

---

## Stop conditions

Stop immediately if any of these occur:

- Public page SHA changes unexpectedly.
- Any agent proposes DB write, SQL apply, migration, service restart, deploy, git push, or live page publish without a packet.
- Assistant-triage rows are treated as writes rather than review hints.
- Threshold retune is proposed without numeric features and representative labels.
- Claim 2929 weakening row is ignored in a consensus/trust decision.
- Work proceeds on dirty repo state without explicitly separating report artifacts from code changes.
- Prose + DB + badge + threshold changes are bundled into one approval.
- Goru attempts to inspect Antigravity brain/scratch files or write scripts outside scope.

---

## Verification commands for future read-only checks

Run from `/Users/duhokim/NebulaMind/NebulaMind` unless noted.

```bash
# Git hygiene snapshot
git status --short
git branch --show-current
git rev-parse --short HEAD
```

```bash
# Public page invariant check
python3 - <<'PY'
import json, urllib.request, hashlib, re
url='https://nebulamind.net/api/pages/galaxy-evolution-v2'
req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=20) as r:
    data=json.loads(r.read().decode())
content=data.get('content','')
print(data.get('id'), data.get('slug'), data.get('version_num'))
print(len(content))
print(hashlib.sha256(content.encode()).hexdigest())
print(len(re.findall(r'^##\\s+', content, flags=re.M)))
print(len(re.findall(r'<!--\\s*claim:', content)))
print(len(re.findall(r'https?://', content)))
PY
```

Expected current values:

- id/slug/version: `58 galaxy-evolution-v2 4`
- length: `11855`
- SHA: `af8a8c739c55a4a85b298ec0d62683f5b2f03b38fc5ecf3f14bdfcea176b0055`
- h2 count: `7`
- claim markers: `8`
- URLs: `0`

---

## Final planning status

- Planning artifact only.
- DB writes executed: `0`.
- Galaxy prose edits executed: `0`.
- Trust badge changes executed: `0`.
- Threshold retunes executed: `0`.
- Apply SQL generated: `false`.
