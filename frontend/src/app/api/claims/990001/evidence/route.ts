import { NextResponse } from "next/server";

export const dynamic = "force-static";

const fixtureEvidence = {
  evidence: [
    {
      id: 990101,
      title: "Deterministic source-trace fixture for stacked Escape browser smoke",
      arxiv_id: "2606.990101",
      url: "https://example.org/nebulamind/source-trace-fixture",
      authors: "NebulaMind Fixture Harness; Hermes QA",
      year: 2026,
      summary: "Deterministic source-trace fixture evidence used by the browser smoke to keep an evidence panel open while Escape closes only the citation hover card.",
      stance: "supporting",
      status: "accepted",
      votes_agree: 3,
      votes_disagree: 0,
      comments_count: 0,
      element_links: [
        {
          element_id: "source-trace-fixture-sentence",
          element_text_snapshot: "A browser smoke can keep an evidence panel open while closing only the top source trace hover card.",
        },
      ],
      link_count: 1,
      relevance: 0.98,
      entailment: 0.96,
      rigor: 0.94,
      confidence: 0.97,
      quality_v2: 0.96,
    },
    {
      id: 990102,
      title: "Nullable source-trace fixture citation",
      arxiv_id: null,
      url: null,
      authors: null,
      year: null,
      summary: null,
      stance: "contradicting",
      status: "accepted",
      votes_agree: 2,
      votes_disagree: 0,
      comments_count: 0,
      element_links: [],
      link_count: 0,
      relevance: 0.82,
      entailment: 0.78,
      rigor: 0.76,
      confidence: 0.8,
      quality_v2: 0.79,
    },
  ],
  total_elements: 2,
};

export async function GET() {
  return NextResponse.json(fixtureEvidence);
}
