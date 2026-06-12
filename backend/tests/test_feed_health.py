"""Feed-health probe: assert all configured RSS feeds return HTTP 200 and at least 1 item.

Run in CI:
    pytest tests/test_feed_health.py -v

Run standalone:
    python3 -m app.agent_loop.news_curator --probe-feeds
"""
import pytest
from app.agent_loop.news_curator import probe_feeds


def test_general_feeds_healthy():
    """All 6 GENERAL_FEEDS must return HTTP 200 with at least 1 item."""
    from app.agent_loop.news_curator import GENERAL_FEEDS
    general_pubs = {f["source_publication"] for f in GENERAL_FEEDS}
    results = probe_feeds()
    general_results = [r for r in results if r["source"] in general_pubs]
    assert general_results, "No probe results for GENERAL_FEEDS"
    failed = [r for r in general_results if not r["ok"]]
    if failed:
        msgs = "\n".join(f"  {r['source']}: {r['url']} — {r['error']}" for r in failed)
        pytest.fail(f"{len(failed)} general feed(s) dead or empty:\n{msgs}")


@pytest.mark.parametrize("pub", [
    "AAS Nova",
    "Nature Astronomy",
    "Sky & Telescope",
    "ESO",
    "NOIRLab",
    "ESA Science",
])
def test_general_feed_individually(pub):
    from app.agent_loop.news_curator import GENERAL_FEEDS
    src = next((f for f in GENERAL_FEEDS if f["source_publication"] == pub), None)
    assert src is not None, f"{pub} not found in GENERAL_FEEDS"
    results = probe_feeds()
    row = next((r for r in results if r["source"] == pub), None)
    assert row is not None, f"No probe result for {pub}"
    assert row["ok"], f"{pub} feed unhealthy: {row['error']} ({row['url']})"
    assert row["items"] > 0, f"{pub} returned 0 items"
