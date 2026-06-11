You are evaluating an astronomy reference text against a strict research-utility rubric. The text is presented without provenance — do not assume it is high quality, professionally curated, or already vetted. Many texts you will judge are mediocre or generic, and you must say so.

The rubric measures only two things:
  1. ESTABLISHED FINDINGS — what has been settled in the field, stated with specific numbers, mechanisms, and authoritative citations.
  2. RESEARCH FRONTIER — specific open questions, active debates with named opposing positions, and explicit pointers to ongoing instruments / surveys / datasets.

Be strict. Score SUBSTANCE, not style. Well-written prose with no specific findings must score LOW, not high. Generic "future work" language must trigger noise_penalty. A page that "covers the topic" without quantitative anchors or named debates is a 2/3 on findings_clarity at best, not a 3 — top scores require exceptional evidence and are not given by default.

The top tier of each dimension (3, 3, 2, 1, 0) is meant to be hard. A page that earns a top score on every dimension is in the top ~5% of astronomy reference texts. If you are tempted to give all top scores, re-check against the harder bars below before doing so.

===

RUBRIC (top tiers are intentionally hard — read the bars before assigning):

findings_clarity (0-3):
  Are established findings stated cleanly, accurately, and with specific quantitative anchors and authoritative citations?
  0 = vague or absent findings, or descriptive prose without specifics
  1 = some findings present but lacking specifics (no numbers, no citations)
  2 = clear findings with numbers or mechanisms, partial citation coverage
  3 = ≥3 distinct quantitative findings (numbers with units / specific mechanisms / dated detections)
      AND ≥3 author+year (or arXiv) citations attached to those findings
      AND those citations are appropriate (not tangential, not generic review papers used as a catch-all)

open_questions_q (0-3):
  Are open questions specific, currently active in the field, and researchable?
  0 = no open questions, or only vague gestures at uncertainty
  1 = open questions mentioned but unspecific or stale (pre-2020 framing)
  2 = real open questions named, but at most one has named competing positions
  3 = ≥3 active debates explicitly identified
      AND each has named competing positions or camps (e.g., "Group A claims X, Group B claims Y")
      AND ≥2 of those debates cite work from 2023 or later on at least one side

evidence_depth (0-2):
  Do the page's key claims have strong cited support — not just any reference, but the right ones, with recency?
  0 = claims lack citations, or citations are tangential
  1 = some claims well-supported, others thin; mix of recent and old references
  2 = ≥75% of substantive claims have specific paper citations
      AND ≥5 distinct cited works are from 2020 or later
      AND ≥2 distinct cited works are from 2023 or later

frontier_signal (0-1):
  Does the page point to where the field is going — current-instrument findings, hot debates, planned surveys?
  0 = no frontier content, only pre-2020 perspective, or only generic "future work" claims
  1 = ≥1 explicit named-instrument finding from 2023+ (JWST, Euclid, DESI, Roman, Rubin/LSST, ALMA, IceCube, LIGO O4/O5, etc.)
      AND ≥1 explicit pointer to an ongoing or near-future survey/mission with a concrete deliverable

noise_penalty (-2 to 0):
  Subtract for problems present in the page. Each of the following is at least -1 when present (cap total at -2):
  a) vague claims without specific numbers / mechanisms / paper refs
  b) prescriptive / roadmap / marketing voice ("we will explore...", "future work will...", "this page covers...", "in this article we...")
  c) hallucinated or unverified citations (author+year that doesn't match the claim, or fabricated arXiv IDs)
  d) irrelevant evidence (paper doesn't support the claim it's attached to)
  e) repetition / filler prose / "in conclusion" / "in summary" / "overall" / "various aspects" / "plays a crucial role"
  Voice drift (b) is an automatic -1 when present anywhere in the text.

NORMALIZATION (do not output this — for reference):
  raw = findings_clarity + open_questions_q + evidence_depth + frontier_signal + noise_penalty
  utility_0_10 = max(0, min(10, (raw + 2) * 10 / 11))

  A normalized utility of 9.5+ requires raw ≥ 8.45, which in practice means top-tier on at
  least three of the four positive dimensions AND zero noise_penalty. If the text does not
  meet the explicit numeric bars above, do not award the top tier.

===

The text follows after ===PAGE===. Its claims (consensus / debate / accepted) follow after ===CLAIMS===.

Score the absolute current state of the text. Do not score what it could become. Do not score the author's intent or what subsections "promise" to cover.

Output JSON only — no preamble, no explanation outside the JSON:
{
  "findings_clarity": <int 0-3>,
  "open_questions_q": <int 0-3>,
  "evidence_depth": <int 0-2>,
  "frontier_signal": <int 0-1>,
  "noise_penalty": <int -2 to 0>,
  "rationale": "<exactly 3 sentences tying the score to specific content on the page>"
}
