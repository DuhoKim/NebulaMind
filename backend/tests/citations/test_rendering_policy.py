from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
WIKI_CLIENT = REPO_ROOT / "frontend" / "src" / "app" / "wiki" / "[slug]" / "WikiPageClient.tsx"
CITATION_POLICY = REPO_ROOT / "frontend" / "CITATION_POLICY.md"


def _render_citation_markers_like_frontend(content: str) -> str:
    """Small policy fixture mirroring the frontend citation display contract."""

    def parse_ids(raw: str) -> list[int]:
        return [
            int(part.strip())
            for part in raw.split(",")
            if part.strip().isdigit() and int(part.strip()) > 0
        ]

    def replace_cite(match: re.Match[str]) -> str:
        ids = parse_ids(match.group(1))
        return '<span data-cite-ids="{}"></span>'.format(",".join(map(str, ids))) if ids else ""

    rendered = re.sub(r"<!--cite:([\d,\s]+)-->", replace_cite, content)
    rendered = re.sub(
        r"<!--cite-unmatched:([^>]+?)-->",
        lambda m: '<span class="cite-unmatched" data-cite-unmatched="{}"></span>'.format(
            m.group(1).replace('"', "&quot;").replace("<", "&lt;")
        ),
        rendered,
    )
    rendered = re.sub(
        r"<!--\s*claim:([\d,\s]+?)\s*-->([\s\S]*?)<!--\s*/claim:([\d,\s]+?)\s*-->",
        lambda m: (
            '<span data-claim-id="{ids}" id="claim-{anchor}">{body}</span>'.format(
                ids=",".join(map(str, parse_ids(m.group(1)))),
                anchor=parse_ids(m.group(1))[0],
                body=m.group(2),
            )
            if parse_ids(m.group(1)) == parse_ids(m.group(3)) and parse_ids(m.group(1))
            else m.group(0)
        ),
        rendered,
    )
    return rendered


def test_citation_policy_doc_exists_and_states_durable_rule() -> None:
    text = CITATION_POLICY.read_text()

    assert "Inline evidence badges only" in text
    assert "Do not render numbered superscripts" in text
    assert "Do not render a bottom `References`, `Bibliography`" in text
    assert "2026-05-21" in text
    assert "2026-06-10" in text


def test_wiki_client_has_no_numbered_reference_renderer() -> None:
    source = WIKI_CLIENT.read_text()

    forbidden = [
        "assignCitationSeqs",
        "orderedCitations",
        "cite-num",
        "data-seqs",
        'id={`ref-',
        "<h2>References</h2>",
        ">References</h2>",
    ]
    for token in forbidden:
        assert token not in source


def test_citation_marker_rendering_policy_sample_has_no_superscripts_or_references() -> None:
    rendered = _render_citation_markers_like_frontend(
        "Claim text<!--cite:20823,20824--> and unresolved<!--cite-unmatched:Labbe 2023-->."
    )

    assert "<sup" not in rendered.lower()
    assert not re.search(r"\[\d+(?:,\d+)*\]", rendered)
    assert not re.search(r"<h[1-6][^>]*>\s*References\s*</h[1-6]>", rendered, flags=re.I)
    assert "data-cite-ids=\"20823,20824\"" in rendered
    assert "data-cite-unmatched=\"Labbe 2023\"" in rendered


def test_claim_marker_parser_does_not_escape_math_entities() -> None:
    rendered = _render_citation_markers_like_frontend(
        "<!--claim:1637-->Clean math $\\gt 700,000$ and $z \\lt 0.3$.<!--/claim:1637-->"
    )

    assert 'data-claim-id="1637"' in rendered
    assert "$\\gt 700,000$" in rendered
    assert "$z \\lt 0.3$" in rendered
    assert "&gt;" not in rendered
    assert "&lt;" not in rendered


def test_unmatched_and_unknown_comments_stay_invisible_by_policy_fixture() -> None:
    rendered = _render_citation_markers_like_frontend(
        "<!--claim:1-->Text <!--cite-unmatched:Dekel & Silk 1986--> <!--future-marker:x--><!--/claim:1-->"
    )

    visible_text = re.sub(r"<[^>]+>", "", rendered)
    visible_text = re.sub(r"<!--[\s\S]*?-->", "", visible_text)
    assert "Dekel" not in visible_text
    assert "future-marker" not in visible_text
    assert "<!--" not in visible_text


def test_wiki_client_uses_pure_renderer_without_normalizer_or_claim_escaper() -> None:
    source = WIKI_CLIENT.read_text()

    assert "normalizeMarkdown" not in source
    assert "wrapClaimComments" not in source
    assert "renderWikiMarkers" in source
    assert "Normalize existing entities" not in source
    assert "__CITE_SPAN_PLACEHOLDER_" not in source
    assert 'strict: "ignore"' in source
