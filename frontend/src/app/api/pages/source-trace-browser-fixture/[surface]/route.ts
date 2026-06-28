import { NextResponse } from "next/server";

export const dynamic = "force-static";

const fixtureCitations = [{
  evidence_id: 990101,
  author_year_key: "Fixture2026",
  title: "Deterministic source-trace fixture for stacked Escape browser smoke",
  authors: ["NebulaMind Fixture Harness", "Hermes QA"],
  year: 2026,
  doi: "10.0000/nebulamind.fixture.source-trace",
  arxiv_id: "2606.990101",
  url: "https://example.org/nebulamind/source-trace-fixture",
  summary: "A deterministic source-trace fixture citation used to verify that Escape closes only the top citation hover card while the evidence panel remains open.",
  abstract: "This fixture is static frontend data for browser-level regression coverage.",
  journal_ref: "NebulaMind Fixtures 1, 1",
},
  {
    evidence_id: 990102,
    author_year_key: "FixtureNull2026",
    title: "Nullable source-trace fixture citation",
    authors: [],
    year: null,
    doi: null,
    arxiv_id: null,
    url: null,
    summary: null,
    abstract: null,
    journal_ref: null,
  },
];

const fixtureClaims = {
  sections: [
    {
      title: "Fixture",
      claims: [
        {
          id: 990001,
          text: "A browser smoke can keep an evidence panel open while closing only the top source trace hover card.",
          connector: null,
          trust_level: "debated",
          evidence_count: 2,
          con_count: 0,
          section: "Fixture",
          has_escalation: false,
        },
      ],
    },
  ],
  debates: [],
};

const fixtureContributors = {
  contributors: [],
  edit_history: [],
};

const fixtureHealth = {
  score: 100,
  band: "fixture",
  emoji: "🧪",
};

type RouteContext = { params: Promise<{ surface: string }> };

export async function GET(_request: Request, { params }: RouteContext) {
  const { surface } = await params;

  if (surface === "citations") return NextResponse.json({ citations: fixtureCitations });
  if (surface === "claims") return NextResponse.json(fixtureClaims);
  if (surface === "contributors") return NextResponse.json(fixtureContributors);
  if (surface === "health") return NextResponse.json(fixtureHealth);
  if (surface === "ideas") return NextResponse.json({ ideas: [] });

  return NextResponse.json({ error: `Unknown source-trace fixture surface: ${surface}` }, { status: 404 });
}
