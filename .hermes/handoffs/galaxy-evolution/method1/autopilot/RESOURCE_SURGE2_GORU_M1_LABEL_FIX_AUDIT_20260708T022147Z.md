# Goru — M1 Label-Fix Feasibility Audit

**Marker:** RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z_SECOND_WAVE

## Audit Findings

I inspected the static candidate `evidence-trust-preview-20260708T014205Z.html` to identify strings that falsely imply positive trust or provenance for the 27 unbound chips, which contradicts the "unbound-local" designation.

**1. On-Chip Text**
- **Exact String:** `· provenance`
- **Occurrences:** 27
- **Context:** Rendered inside the `<span class="cid">...</span>` for every unbound chip (e.g., `<span class="cid">2930 · provenance</span>`).
- **Proposed Safe Replacement:** `· unbound-local`

**2. Summary Paragraph Text**
- **Exact String:** `genuine provenance chips`
- **Occurrences:** 1
- **Context:** In the `<p class="muted">` summary section ("The 27 baseline chips are genuine provenance chips...").
- **Proposed Safe Replacement:** `unbound-local claims`

**3. CSS Class Name (Optional but recommended)**
- **Exact String:** `t-baseline`
- **Occurrences:** 27
- **Context:** Used to style the unbound chips (`<span class="claim t-baseline">`). While technically a CSS class, it implies a "baseline" trust level.
- **Proposed Safe Replacement:** `t-unbound-local`

**4. Legend Text**
- **Exact String:** `baseline / unbound-local`
- **Occurrences:** 1
- **Context:** In the legend explaining the dot colors.
- **Proposed Safe Replacement:** `unbound-local`

## Feasibility Verdict
**PASS (Feasible).** The affected strings are purely static text within the HTML output. They can be safely replaced via standard string substitution or static templating updates without touching any live product databases, API endpoints, or external network requests. 

**No edits were made during this audit.**
