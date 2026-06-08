import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.config import settings
from app.services import paper_search


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


def test_ads_citing_papers_query_shape(monkeypatch):
    captured = {}

    def fake_urlopen(req, timeout):
        captured["url"] = req.full_url
        captured["headers"] = dict(req.header_items())
        captured["timeout"] = timeout
        return FakeResponse(
            {
                "response": {
                    "docs": [
                        {
                            "bibcode": "2025ApJ...1....1A",
                            "title": ["Modern citer"],
                            "abstract": "Uses a standard framework.",
                            "author": ["Ada A."],
                            "year": "2025",
                            "doi": ["10.1000/citer"],
                            "identifier": ["arXiv:2501.00001"],
                            "citation_count": 3,
                            "pub": "ApJ",
                        }
                    ]
                }
            }
        )

    monkeypatch.setattr(settings, "ADS_API_KEY", "token")
    monkeypatch.setattr(paper_search.urllib.request, "urlopen", fake_urlopen)

    records = paper_search.ads_citing_papers("1978MNRAS.183..341W", rows=25, start=5, min_year=2024)

    assert len(records) == 1
    assert records[0].bibcode == "2025ApJ...1....1A"
    assert "citations%28bibcode%3A%221978MNRAS.183..341W%22%29+year%3A2024-" in captured["url"]
    assert "rows=25" in captured["url"]
    assert "start=5" in captured["url"]
    assert captured["headers"]["Authorization"] == "Bearer token"


def test_s2_citation_contexts(monkeypatch):
    captured = {}

    def fake_urlopen(url, timeout):
        captured["url"] = url
        captured["timeout"] = timeout
        return FakeResponse({"data": [{"contexts": ["Following White and Rees..."], "intents": ["background"]}]})

    monkeypatch.setattr(paper_search.urllib.request, "urlopen", fake_urlopen)

    rows = paper_search.s2_citation_contexts("DOI:10.1093/mnras/183.3.341")

    assert rows[0]["contexts"] == ["Following White and Rees..."]
    assert "fields=contexts" in captured["url"]
    assert "DOI:10.1093%2Fmnras%2F183.3.341" in captured["url"]


def test_ads_reference_bibcodes_query_shape(monkeypatch):
    captured = {}

    def fake_urlopen(req, timeout):
        captured["url"] = req.full_url
        captured["headers"] = dict(req.header_items())
        return FakeResponse(
            {
                "response": {
                    "docs": [
                        {
                            "bibcode": "1978MNRAS.183..341W",
                            "title": ["Seed paper"],
                            "abstract": "Foundational result.",
                            "author": ["White S."],
                            "year": "1978",
                            "doi": ["10.1093/mnras/183.3.341"],
                            "identifier": [],
                            "citation_count": 3979,
                            "pub": "MNRAS",
                        }
                    ]
                }
            }
        )

    monkeypatch.setattr(settings, "ADS_API_KEY", "token")
    monkeypatch.setattr(paper_search.urllib.request, "urlopen", fake_urlopen)

    records = paper_search.ads_reference_bibcodes("2026MNRAS.548ag650S", rows=30)

    assert records[0].bibcode == "1978MNRAS.183..341W"
    assert "references%28bibcode%3A%222026MNRAS.548ag650S%22%29" in captured["url"]
    assert "rows=30" in captured["url"]
    assert captured["headers"]["Authorization"] == "Bearer token"


def test_s2_references(monkeypatch):
    captured = {}

    def fake_urlopen(url, timeout):
        captured["url"] = url
        return FakeResponse({"data": [{"contexts": ["We follow the cited work."], "citedPaper": {"title": "Seed"}}]})

    monkeypatch.setattr(paper_search.urllib.request, "urlopen", fake_urlopen)

    rows = paper_search.s2_references("arXiv:2501.00001")

    assert rows[0]["contexts"] == ["We follow the cited work."]
    assert "/references?" in captured["url"]
    assert "citedPaper.externalIds" in captured["url"]
