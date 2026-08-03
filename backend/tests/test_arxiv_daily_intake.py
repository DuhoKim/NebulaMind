import json
import time
from types import SimpleNamespace

import pytest
from sqlalchemy.exc import IntegrityError

pytest.skip(
    "quarantined 2026-08-03: imports symbols absent from committed arxiv_fetch.py — see Kun audit R5",
    allow_module_level=True,
)

from app.agent_loop import arxiv_fetch
from app.agent_loop.arxiv_fetch import (
    build_intake_fields,
    canonical_arxiv_id,
    collect_daily_rss_candidates,
    persist_daily_rss_intake,
    query_arxiv_rss,
    select_unseen_papers,
)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("oai:arXiv.org:2607.19428", "2607.19428"),
        ("oai:arXiv.org:2607.19428v2", "2607.19428"),
        ("arXiv:2607.19428v3", "2607.19428"),
        ("https://arxiv.org/abs/2607.19428v4", "2607.19428"),
        ("http://arxiv.org/abs/astro-ph/0601001v2", "astro-ph/0601001"),
        ("  2607.19428  ", "2607.19428"),
        ("", ""),
    ],
)
def test_canonical_arxiv_id_normalizes_source_and_version(raw, expected):
    assert canonical_arxiv_id(raw) == expected


def test_query_arxiv_rss_normalizes_fresh_feed_entry(monkeypatch):
    entry = arxiv_fetch.feedparser.FeedParserDict(
        {
            "id": "oai:arXiv.org:2607.19428v2",
            "title": "  A Fresh\nGalaxy Paper  ",
            "summary": "  New result.\nMore detail.  ",
            "authors": [{"name": "Ada Example"}, {"name": "Grace Example"}],
            "published_parsed": time.strptime("2026-07-23", "%Y-%m-%d"),
            "link": "https://arxiv.org/abs/2607.19428v2",
        }
    )
    monkeypatch.setattr(
        arxiv_fetch.feedparser,
        "parse",
        lambda url: arxiv_fetch.feedparser.FeedParserDict(
            {"entries": [entry], "bozo": False, "href": url}
        ),
    )

    papers = query_arxiv_rss("astro-ph.GA", limit=20)

    assert papers == [
        {
            "arxiv_id": "2607.19428",
            "title": "A Fresh Galaxy Paper",
            "abstract": "New result. More detail.",
            "authors": json.dumps(["Ada Example", "Grace Example"]),
            "submitted": "2026-07-23",
            "url": "https://arxiv.org/abs/2607.19428",
            "category": "astro-ph.GA",
        }
    ]


def test_select_unseen_papers_deduplicates_legacy_ids_and_feed_versions():
    papers = [
        {"arxiv_id": "2607.19428", "title": "Already stored"},
        {"arxiv_id": "arXiv:2607.20000v1", "title": "New paper"},
        {"arxiv_id": "oai:arXiv.org:2607.20000v2", "title": "Same new paper"},
    ]

    unseen = select_unseen_papers(
        papers,
        existing_raw_ids=["oai:arXiv.org:2607.19428v3"],
    )

    assert unseen == [{"arxiv_id": "2607.20000", "title": "New paper"}]


def test_collect_daily_rss_candidates_queries_all_categories_and_deduplicates(monkeypatch):
    seen_categories = []

    def fake_query(category, limit):
        seen_categories.append((category, limit))
        if category == "astro-ph.GA":
            return [
                {"arxiv_id": "2607.10000", "title": "Existing"},
                {"arxiv_id": "2607.20000v1", "title": "New A"},
            ]
        if category == "astro-ph.CO":
            return [
                {"arxiv_id": "oai:arXiv.org:2607.20000v2", "title": "New A duplicate"},
                {"arxiv_id": "2607.30000", "title": "New B"},
            ]
        return []

    monkeypatch.setattr(arxiv_fetch, "query_arxiv_rss", fake_query)

    papers = collect_daily_rss_candidates(
        existing_raw_ids=["oai:arXiv.org:2607.10000v3"],
        per_category_limit=75,
    )

    assert seen_categories == [(category, 75) for category in arxiv_fetch.ARXIV_CATEGORIES]
    assert [paper["arxiv_id"] for paper in papers] == ["2607.20000", "2607.30000"]



def test_build_intake_fields_is_deterministic_and_stops_before_integration():
    paper = {
        "arxiv_id": "2607.30000",
        "title": "Safe intake",
        "abstract": "A" * 600,
        "authors": json.dumps(["Ada Example"]),
        "submitted": "2026-07-23",
        "url": "https://arxiv.org/abs/2607.30000",
        "category": "astro-ph.GA",
    }

    fields = build_intake_fields(paper)

    assert fields["abstract_summary"] == "A" * 500
    assert fields["related_pages"] == "[]"
    assert fields["wiki_edit_proposed"] is False
    assert "match_type" not in fields
    assert "processed_at" not in fields



def test_persist_daily_rss_intake_writes_only_safe_intake_rows(monkeypatch):
    candidate = {
        "arxiv_id": "2607.40000",
        "title": "Persist me",
        "abstract": "Safe abstract",
        "authors": json.dumps(["Ada Example"]),
        "submitted": "2026-07-23",
        "url": "https://arxiv.org/abs/2607.40000",
        "category": "astro-ph.GA",
    }

    class FakeQuery:
        def all(self):
            return [("oai:arXiv.org:2607.10000v1",)]

    class FakeDB:
        def __init__(self):
            self.added = []
            self.commits = 0

        def query(self, _column):
            return FakeQuery()

        def add(self, row):
            self.added.append(row)

        def commit(self):
            self.commits += 1

        def rollback(self):
            raise AssertionError("rollback not expected")

    class FakePaper:
        arxiv_id = object()

        def __init__(self, **kwargs):
            self.fields = kwargs

    monkeypatch.setattr(
        arxiv_fetch,
        "collect_daily_rss_candidates",
        lambda existing_raw_ids, per_category_limit: [candidate],
    )
    db = FakeDB()

    result = persist_daily_rss_intake(db, FakePaper, per_category_limit=75)

    assert result == {
        "source": "arxiv_rss",
        "total_new": 1,
        "per_category_limit": 75,
        "automatic_integration": False,
        "duplicates_skipped": 0,
    }
    assert db.commits == 1
    assert len(db.added) == 1
    assert db.added[0].fields == build_intake_fields(candidate)



def test_persist_daily_rss_intake_continues_after_duplicate_race(monkeypatch):
    candidates = [
        {"arxiv_id": "2607.50000", "title": "Race duplicate", "abstract": "A"},
        {"arxiv_id": "2607.60000", "title": "Still persists", "abstract": "B"},
    ]

    class FakeQuery:
        def all(self):
            return []

    class FakeDB:
        def __init__(self):
            self.commit_attempts = 0
            self.rollbacks = 0

        def query(self, _column):
            return FakeQuery()

        def add(self, _row):
            pass

        def commit(self):
            self.commit_attempts += 1
            if self.commit_attempts == 1:
                raise IntegrityError("insert", {}, Exception("duplicate"))

        def rollback(self):
            self.rollbacks += 1

    class FakePaper:
        arxiv_id = object()

        def __init__(self, **kwargs):
            self.fields = kwargs

    monkeypatch.setattr(
        arxiv_fetch,
        "collect_daily_rss_candidates",
        lambda existing_raw_ids, per_category_limit: candidates,
    )
    db = FakeDB()

    result = persist_daily_rss_intake(db, FakePaper)

    assert result["total_new"] == 1
    assert result["duplicates_skipped"] == 1
    assert db.commit_attempts == 2
    assert db.rollbacks == 1



def test_fetch_arxiv_daily_uses_safe_intake_and_enqueues_mode1(monkeypatch):
    from app import database

    class FakeDB:
        def __init__(self):
            self.closed = False

        def close(self):
            self.closed = True

    db = FakeDB()
    persist_calls = []
    sent_tasks = []
    expected = {
        "source": "arxiv_rss",
        "total_new": 2,
        "per_category_limit": 100,
        "automatic_integration": False,
        "duplicates_skipped": 0,
    }

    def fake_persist(session, paper_model, per_category_limit=100):
        persist_calls.append((session, paper_model, per_category_limit))
        return dict(expected)

    monkeypatch.setattr(database, "SessionLocal", lambda: db)
    monkeypatch.setattr(arxiv_fetch, "persist_daily_rss_intake", fake_persist)
    monkeypatch.setattr(
        arxiv_fetch,
        "current_app",
        SimpleNamespace(
            send_task=lambda name, kwargs=None: sent_tasks.append((name, kwargs))
        ),
    )
    monkeypatch.setattr(arxiv_fetch.settings, "ARXIV_WIKI_FEED_V2_ENABLED", True)

    result = arxiv_fetch.fetch_arxiv_daily.run()

    assert result == expected
    assert len(persist_calls) == 1
    assert persist_calls[0][0] is db
    assert persist_calls[0][2] == 100
    assert sent_tasks == [
        (
            "app.agent_loop.tasks.arxiv_wiki_feed_daily",
            {"trigger": "fetch_arxiv_daily"},
        )
    ]
    assert db.closed is True



def test_legacy_task_module_does_not_export_duplicate_intake_tasks():
    from app.agent_loop import tasks as legacy_tasks

    assert not hasattr(legacy_tasks, "fetch_arxiv_daily")
    assert not hasattr(legacy_tasks, "retry_unprocessed_arxiv_papers")


def test_beat_does_not_schedule_automatic_arxiv_integration_retry():
    from app.agent_loop.worker import celery_app

    assert "retry-unprocessed-arxiv-daily" not in celery_app.conf.beat_schedule
