import type { WikiPageClientTestOnlyFixtureData } from "../[slug]/WikiPageClient";

export const sourceTraceBrowserFixtureData = {
  page: {
    id: 990000,
    title: "Source Trace Browser Fixture",
    slug: "source-trace-browser-fixture",
    hero_tagline: "Deterministic no-auth fixture for source-trace browser smoke coverage.",
    hero_facts: null,
    editor_agent_tier: "browser-fixture",
    synthesized_date: "2026-06-28",
    version_num: 1,
    content: `# Source Trace Browser Fixture

This deterministic wiki fixture exists only to keep browser-level source trace Escape sequencing covered without depending on live article content.

<!--claim:990001-->A browser smoke can keep an evidence panel open while closing only the top source trace hover card<!--cite:990101,990102-->.<!--/claim:990001-->

The fixture intentionally combines one claim badge, one evidence panel, and two linked citation markers on the same route.`,
  },
  claims: {
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
            con_count: 1,
            section: "Fixture",
            has_escalation: false,
          },
        ],
      },
    ],
    debates: [],
  },
  citations: [
    {
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
  ],
  health: {
    score: 100,
    band: "fixture",
    emoji: "🧪",
  },
  contributorsData: {
    contributors: [],
    edit_history: [],
  },
  claimIdeasMap: {},
} satisfies WikiPageClientTestOnlyFixtureData;
