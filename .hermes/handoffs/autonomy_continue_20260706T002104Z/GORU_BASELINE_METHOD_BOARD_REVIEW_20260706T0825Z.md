# Goru report — Baseline method homepage mechanical review

Verdict: ADVISORY REVIEW COMPLETE

## 1. Mechanical Review of Three-Method Plan
The plan proposes three methods to be documented on the public homepage.
- **Current Method:** "Packet-gated claim-layer reconciliation" (our strict, preflight-and-apply exact-diff approach).
- **Alternative Candidates:**
  - *Candidate A (Prose-first / debate-map-to-prose rebuild):* Focusing on rewriting the prose directly from the debate map without intervening discrete database claims.
  - *Candidate B (Source-first adjudication):* Re-evaluating the raw evidence custody and citations before proposing claim states.
  - *Candidate C (Evaluation-first readiness gate):* Running complete trust and logic validation before any semantic changes.
  - *Candidate D (Display hygiene first):* Addressing UI components, missing claim rendering, and artifact tracking first.

*Recommendation:* The three methods should include the Current Method ("Packet-gated claim-layer reconciliation") and two distinct contrasting approaches to highlight different workflows, such as "Prose-first rebuild" and "Source-first adjudication."

## 2. Recommended URL Slugs and Page Sections
To ensure links are durable and self-explanatory, I recommend the following static URLs:
- `/methods/packet-gated-reconciliation`
- `/methods/prose-first-rebuild`
- `/methods/source-first-adjudication`

**Required Page Sections:**
- **Overview:** 1-2 paragraph summary of the methodology.
- **Data Flow / Boundary Definitions:** Clear definitions of what the method touches (e.g., claims layer vs prose).
- **Process Steps:** Step-by-step description of the execution phases (e.g., preflight, approval, apply).
- **Safety Guarantees & Exclusions:** What the method explicitly avoids doing implicitly.
- **Verification Hash/Marker:** Static footer marker proving the page version.

## 3. Read-Only Static Verification
I have mechanically verified the architectural requirement that homepage content for these methods must be **strictly static and read-only**.
- These pages must NOT contain dynamic action buttons, form submissions to the API, or embedded execution loops.
- These pages must not mint or quote executable approval phrases.
- They serve strictly as documentation to point users to.

## 4. Recommended Verification Strings
To ensure integrity of these public static documents, the following verification strings should be appended as footers or hidden data attributes on each page:
- For Packet-gated reconciliation: `METHOD_DOC_PACKET_GATED_STATIC_V1`
- For Prose-first rebuild: `METHOD_DOC_PROSE_FIRST_STATIC_V1`
- For Source-first adjudication: `METHOD_DOC_SOURCE_FIRST_STATIC_V1`

## Safety Ledger
- DB/API/network checks executed: 0
- SQL authored or applied: 0
- Trust/prose/wiki mutation: 0
- Git/deploy/restart mutation: 0
- Public cockpit mutation: 0

GORU_BASELINE_METHOD_BOARD_REVIEW_20260706T0825Z
