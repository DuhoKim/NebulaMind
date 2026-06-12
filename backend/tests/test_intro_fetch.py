import datetime as dt

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import Base
from app.models.claim import PaperIntro
from app.services import intro_fetch


def _db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine, tables=[PaperIntro.__table__])
    return Session(engine)


def _payload(body: str) -> bytes:
    return (("<html><body><h1>Introduction</h1>" + body + "</body></html>") + (" " * 21_000)).encode()


def test_fetch_intro_cache_hit(monkeypatch):
    db = _db()
    db.add(PaperIntro(arxiv_id="2401.00001", intro_text="Introduction cached.", http_status=200, source="ar5iv"))
    db.commit()
    called = False

    def fake_fetch(url, timeout):
        nonlocal called
        called = True
        return 200, _payload("network")

    monkeypatch.setattr(intro_fetch, "_fetch_url", fake_fetch)
    assert intro_fetch.fetch_intro("2401.00001", db) == "Introduction cached."
    assert called is False


def test_fetch_intro_cache_miss_records_success(monkeypatch):
    db = _db()
    monkeypatch.setattr(
        intro_fetch,
        "_fetch_url",
        lambda url, timeout: (200, _payload("This introduction explains galaxies and redshift.")),
    )
    text = intro_fetch.fetch_intro("2401.00002", db)
    assert text and "galaxies and redshift" in text
    row = db.get(PaperIntro, "2401.00002")
    assert row and row.http_status == 200 and row.source == "ar5iv" and row.intro_text


def test_fetch_intro_stub_guard_and_failure_cache(monkeypatch):
    db = _db()
    calls = 0

    def fake_fetch(url, timeout):
        nonlocal calls
        calls += 1
        return 200, b"<html>short Introduction stub</html>"

    monkeypatch.setattr(intro_fetch, "_fetch_url", fake_fetch)
    assert intro_fetch.fetch_intro("2401.00003", db) is None
    assert intro_fetch.fetch_intro("2401.00003", db) is None
    assert calls == 2  # ar5iv + native arXiv fallback only once; failure cache blocks the second call
    assert db.get(PaperIntro, "2401.00003").intro_text is None


def test_fetch_intro_404_path(monkeypatch):
    db = _db()
    monkeypatch.setattr(intro_fetch, "_fetch_url", lambda url, timeout: (404, b""))
    assert intro_fetch.fetch_intro("2301.00004", db) is None
    row = db.get(PaperIntro, "2301.00004")
    assert row and row.http_status == 404 and row.intro_text is None


def test_old_failed_fetch_retries(monkeypatch):
    db = _db()
    db.add(
        PaperIntro(
            arxiv_id="2401.00005",
            intro_text=None,
            http_status=0,
            source="ar5iv",
            fetched_at=dt.datetime.utcnow() - dt.timedelta(days=31),
        )
    )
    db.commit()
    monkeypatch.setattr(
        intro_fetch,
        "_fetch_url",
        lambda url, timeout: (200, _payload("Fresh introduction about stellar mass functions.")),
    )
    assert "stellar mass" in intro_fetch.fetch_intro("2401.00005", db)


def test_select_excerpt_deterministic():
    intro = (
        "Introduction. First sentence discusses telescope calibration and sky maps. "
        "Second sentence describes galaxy redshift surveys and stellar mass. "
        "Third sentence covers dark matter halos in galaxy evolution. "
        "Fourth sentence is about unrelated instrument scheduling. "
        "Fifth sentence returns to redshift and stellar mass measurements."
    )
    claim = "Galaxy redshift surveys constrain stellar mass evolution."
    assert intro_fetch.select_excerpt(intro, claim) == intro_fetch.select_excerpt(intro, claim)
    excerpt = intro_fetch.select_excerpt(intro, claim)
    assert excerpt and "redshift" in excerpt and len(excerpt) <= 1200
