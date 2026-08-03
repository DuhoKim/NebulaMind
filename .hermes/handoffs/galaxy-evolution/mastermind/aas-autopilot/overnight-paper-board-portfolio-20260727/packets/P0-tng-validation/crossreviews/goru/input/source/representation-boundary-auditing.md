---
name: representation-boundary-auditing
description: Audit whether rendered UI or document semantics survive capture into text/structured representations, and separate capture-, validator-, and model-caused failures.
version: 1.2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [audit, capture, representation, rendered-dom, validation, citations]
    related_skills: [systematic-debugging]
---

# Representation Boundary Auditing

## When to use

Use when a model or application renders content into a UI and downstream validation operates on captured `innerText`, HTML, accessibility data, Markdown, or normalized JSON. Typical symptoms include missing citations, empty cells, stripped heading syntax, flattened tables, duplicate blocks, or validator failures that may not reflect the rendered answer.

## Core rule

Never score the model from one lossy representation. Establish what existed at each boundary before assigning cause.

## Evidence layers

Audit these independently:

1. **Rendered source** — DOM/HTML or equivalent semantic tree.
2. **Plain-text capture** — usually `innerText`, not raw Markdown.
3. **Structured capture** — blocks, headings, rows/cells, links, citations/source IDs, sections.
4. **Validator output and implementation** — exact condition that emitted each finding.
5. **Tests** — whether fixtures exercise the native rendering constructs involved.

Preserve the distinction between literal anchors and native citation widgets. A citation component may be semantically present while exposing no `href` or visible text.

## Procedure

### 1. Inventory without modification

Locate the rendered artifact, plain-text artifact, structured representation, capture implementation, validator, fixtures/tests, and run receipt. Record schemas and custody hashes when available. Do not regenerate artifacts unless explicitly authorized.

### 2. Build deterministic comparisons

Measure and compare:

- heading tag sequence versus structured heading blocks;
- table count, row count, row widths, cell ownership, and normalized cell text;
- literal anchor order, duplicates, and destinations versus structured links;
- native citation/source components, their identifiers, and nearest logical unit;
- structured empty cells whose rendered cell contains a citation-only component;
- block duplication caused by nested semantic selectors;
- source-line references against the actual captured lines.

Normalize whitespace only for text-fidelity comparison. Report math/subscript whitespace fragmentation separately from missing content.

### 3. Trace capture code

Check for these recurrent defects:

- link extraction limited to `a[href]`;
- custom citation widgets ignored;
- parent and child semantic nodes both emitted, such as `li` plus `li > p`;
- text-only emptiness checks on citation-only cells;
- line matching in which an empty line matches every needle;
- newline-delimited logical units collapsed into one block;
- component state or citation targets omitted when serializing HTML.

### 4. Classify each failure

Use four labels:

- **Capture-caused:** required evidence exists in the rendered logical unit but is absent, flattened, or duplicated downstream.
- **Model-caused:** the rendered logical unit itself lacks required evidence, or malformed content is faithfully retained.
- **Validator-caused:** capture is adequate but validator control flow, scope, or clause interpretation emits the wrong finding.
- **Unresolved:** identifiers survive, but target metadata or correspondence was not captured. Do not infer mappings merely because counts match.

For same-cell contracts, inspect the exact cell. A citation in a dedicated citation column does not establish compliance for a neighboring claim cell.

### 5. Audit test coverage

Require fixtures for the native constructs involved, not only simplified anchors. Include citation widgets without anchors, citation-only cells, nested list paragraphs, math markup, duplicate links, and blank-line source mapping.

### 6. Run a counterfactual normalized replay when possible

Without modifying sealed artifacts, build an in-memory representation that restores recoverable native semantics such as citation-chip identifiers and their source mappings. Re-run the unchanged validator and compare:

- original findings;
- findings removed by faithful representation;
- findings that remain genuine under the literal contract;
- new false negatives exposed by correcting the representation.

Treat this replay as diagnosis, not acceptance: it does not establish source fidelity or scientific correctness. A clause finding can be **mixed** when its verdict remains genuine but its evidence set was inflated by capture loss.

### 7. Report evidence and confidence

For each requested feature, state: preserved/not preserved/partially preserved; direct evidence and counts; causal classification; and confidence. Explain which validator findings are false representations and which survive perfect capture. Explicitly identify what cannot be reconstructed from saved artifacts. Separate the acceptance decision from the causal diagnosis: fail-closed may remain correct even when most original failure reasons were wrong.

If a first-pass diagnosis confused zero anchors with zero citations, mark that draft superseded, name the missed native construct, and publish corrected counts rather than silently rewriting history.

### 8. Repair with custody-aware TDD when authorized

Keep the failed run immutable and implement capture/validator v2 in a separate packet. Pin RED behavior against the real rendered HTML, including a corrupted index→URL fixture that must fail closed. Treat helper done markers as claims: preserve incorrect helper artifacts as invalid, obtain coordinator adjudication before supersession, and require an independent lane to reproduce fixture hashes and counts twice. The final GREEN gate must inspect filesystem residue and write scope—not only test exit codes—because a passing harness can still leave temp or bytecode files outside its allowed area.

See `references/citation-capture-repair-tdd-and-custody.md` for the full repair and rev2-gate pattern.

### 9. Verify document-format conversions structurally before visual QA

For Markdown-to-HTML and similar report rendering, do not feed line-number-annotated tool output directly into the parser. A prefix such as `12|## Heading` can preserve the words while silently eliminating heading tags, anchors, and TOC structure. Acquire raw source text or remove only a confirmed reader-added `^\d+\|` prefix, then assert expected heading counts/order, TOC target integrity, marker counts/final position, exact critical tokens, closed HTML, and promised dependency boundaries. Only after these pass should browser QA check console/page errors, desktop/mobile overflow, and screenshots. If a managed browser rejects `file://`, use installed local headless tooling rather than publishing or starting a persistent server solely for preview. See `references/markdown-to-html-semantic-fidelity.md`.

### 10. Preserve machine-oriented CLI semantics and audit the checker

For fixed-width or porcelain CLI output, treat whitespace and record ordering as schema. Never apply whole-output `.strip()` to `git status --porcelain`; strip scalar command results only, prefer NUL-safe records, and compare ordered status/path pairs unless the contract explicitly permits set comparison.

When a verifier fails, inspect the predicate before editing the artifact. Distinguish literal wording from semantic requirements, list order from set identity, raw diff operations from logical changed regions, and schema-location assumptions from actual schema. If the artifact is valid and the assertion is over-literal, correct and rerun the checker while leaving the artifact untouched. Preflight helper-generated classifiers before approval so broad filename rules cannot mark real tests or source as debris.

See `references/fixed-width-cli-and-verifier-fidelity.md` for parsing rules, checker-failure triage, generated-script preflight, and an independent verification recipe.

### 11. Audit interactive UI contracts across data, semantics, and tests

For filtered charts and disclosures, reconcile the full predicate lineage behind every rendered set, count, description, and empty state. A deliberate omission such as “no band filter so out-of-band points dim” must not accidentally omit search or another global filter. Treat empty-state wording as a factual claim about why the set is empty.

Review the accessibility topology, not isolated ARIA tokens: image-role containers must not flatten focusable descendants; an `aria-controls` IDREF must resolve whenever present; inline disclosures should normally keep targets mounted+hidden, while conditionally mounted dialogs should conditionally omit `aria-controls` while closed; and links/buttons must not be nested. Source-text regex tests are supplemental because they can lock in the exact defect under review. Prefer behavioral fixtures, TypeScript AST structure checks, or an existing DOM/accessibility-tree harness, with one observed RED per production correction. Before freezing the writable file list, census custom child components directly rendered by the modified surface for the same defect classes; a new hit outside scope is a STOP/rescope, not a reason to ignore the child.

When review and implementation run concurrently, compare against an immutable base/mirror rather than treating the changing worktree as the baseline. Freeze edits before hashing the final review artifact and require independent hash reproduction.

See `references/interactive-ui-contract-review.md` for predicate-lineage checks, truthful empty states, interactive SVG/disclosure rules, stronger test patterns, and custody-safe review.

## Pitfalls

- Treating `innerText` as raw Markdown.
- Calling a citation cell empty because its widget has no text node.
- Assuming every native citation can be resolved to a URL from serialized HTML.
- Conflating a secondary `BAD_STRUCTURE` finding with missing headings when it was triggered by another flag.
- Reporting matching unique counts as proof of one-to-one identity.
- Ignoring faithfully preserved model defects while focusing on capture bugs.

## Verification checklist

- [ ] Every available representation was compared.
- [ ] Heading order and table topology were checked structurally.
- [ ] Literal links and native citations were counted separately.
- [ ] Validator findings were traced to exact logical units.
- [ ] Capture-, model-, validator-caused, and unresolved findings were separated.
- [ ] Test coverage was exercised or inspected.
- [ ] No files were modified when the task was read-only.

## References

- See `references/rendered-dom-citation-audit.md` for a compact probe recipe and evidence table derived from a real citation-preservation audit.
- See `references/deep-research-citation-chip-adjudication.md` for native `source-footnote` mapping, chip-aware counterfactual replay, mixed-finding adjudication, false-negative reconciliation, and correction protocol.
- See `references/citation-capture-repair-tdd-and-custody.md` for immutable repair packets, real-HTML RED fixtures, two-pass chip mapping, helper-artifact supersession, deviation adjudication, and residue-aware independent GREEN gates.
- See `references/markdown-to-html-semantic-fidelity.md` for raw-source acquisition, line-prefix hazards, heading/TOC/marker assertions, and desktop/mobile headless-browser verification of standalone reports.
- See `references/fixed-width-cli-and-verifier-fidelity.md` for whitespace-sensitive CLI parsing, semantic-versus-literal checker triage, path set/order rules, and generated-script preflight.
