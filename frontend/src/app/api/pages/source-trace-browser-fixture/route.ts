import { NextResponse } from "next/server";

export const dynamic = "force-static";

const fixturePage = {
  id: 990000,
  title: "Source Trace Browser Fixture",
  slug: "source-trace-browser-fixture",
  hero_tagline: "Deterministic no-auth fixture for source-trace browser smoke coverage.",
  hero_facts: null,
  editor_agent_tier: "browser-fixture",
  synthesized_date: "2026-06-28",
  version_num: 1,
  created_at: "2026-06-28T00:00:00Z",
  updated_at: "2026-06-28T00:00:00Z",
  content: `# Source Trace Browser Fixture

This deterministic wiki fixture exists only to keep browser-level source trace Escape sequencing covered without depending on live article content.

<!--claim:990001-->A browser smoke can keep an evidence panel open while closing only the top source trace hover card<!--cite:990101,990102-->.<!--/claim:990001-->

The fixture intentionally combines one claim badge, one evidence panel, and two linked citation markers on the same route.`,
};

export async function GET() {
  return NextResponse.json(fixturePage);
}
