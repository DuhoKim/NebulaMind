# Gemini-Web Deep Research Request for Method 3 RT Quality

Marker: `RT_GEMINI_WEB_DEEP_RESEARCH_SIDECAR_PROTOCOL_V1`

**Request ID:** `REQ_M3_RT_20260711T091128Z`
**Method:** Method 3 (Debate-map-to-wiki rebuild)
**Current RT artifact paths:**
- `.../research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md`
- `.../research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`

**Exact topic/cards to improve:**
All 6 extracted research topic cards targeting Galaxy Evolution open questions.

**Existing source-basis links/claim IDs that must not be contradicted:**
Local evidence anchors from `evidence-basis-20260708T014205Z.md#s2` to `#s8`.

**The question Gemini should answer:**
What major recent (2020+) literature reviews or high-impact studies are missing from these cards? Are the proposed decision criteria realistic given current JWST and ALMA survey capabilities?

**Expected output shape:**
A markdown file containing for each card: prior-study findings with source links, what remains unknown, recommended data/survey families, test/decision criteria, overclaim risks, and key papers to verify.

**Explicit safety locks copied from protocol:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not use Gemini-generated DOI/ADS/arXiv IDs until checked locally.
- Do not import numeric results unless supported.
