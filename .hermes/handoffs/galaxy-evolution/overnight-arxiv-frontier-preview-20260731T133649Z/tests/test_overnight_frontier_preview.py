import datetime as dt
import json
from email.message import Message
from io import BytesIO
from urllib.error import HTTPError

import numpy as np
import pytest

from scripts.overnight_frontier_preview import (
    assign_records,
    build_shadow_delta,
    ensure_within_run,
    canonical_arxiv_id,
    classify_candidate,
    load_base_arxiv_ids,
    parse_atom_page,
    request_bytes_with_retries,
    reached_date_boundary,
    validate_and_explain_rerank,
    verify_protected_hashes,
)


def test_canonical_arxiv_id_preserves_old_style_and_strips_source_and_version():
    assert canonical_arxiv_id("https://arxiv.org/abs/2607.19428v4") == ("2607.19428", "2607.19428v4")
    assert canonical_arxiv_id("oai:arXiv.org:2607.19428v2") == ("2607.19428", "2607.19428v2")
    assert canonical_arxiv_id("arXiv:astro-ph/0601001v2") == ("astro-ph/0601001", "astro-ph/0601001v2")


def _paper(**overrides):
    row = {
        "arxiv_id": "2607.30000",
        "observed_version": "2607.30000v1",
        "title": "A valid galaxy evolution paper",
        "abstract": " ".join(["science"] * 45),
        "published": "2026-07-30",
        "categories": ["astro-ph.GA"],
    }
    row.update(overrides)
    return row


def test_load_base_arxiv_ids_reads_identifier_lists(tmp_path):
    path = tmp_path / "base.jsonl"
    path.write_text(
        json.dumps({"identifier": ["2026ApJ...", "arXiv:2607.11111"]}) + "\n"
        + json.dumps({"identifier": ["arXiv:astro-ph/0601001"]}) + "\n"
    )
    assert load_base_arxiv_ids(path) == {"2607.11111", "astro-ph/0601001"}


def test_classify_candidate_routes_dedup_and_version_updates():
    today = dt.date(2026, 7, 31)
    assert classify_candidate(_paper(), set(), {}, set(), today) == "accepted_new"
    assert classify_candidate(_paper(), {"2607.30000"}, {}, set(), today) == "duplicate_base"
    assert classify_candidate(_paper(), set(), {"2607.30000": "2607.30000v1"}, set(), today) == "duplicate_delta"
    assert classify_candidate(_paper(observed_version="2607.30000v2"), set(), {"2607.30000": "2607.30000v1"}, set(), today) == "version_update_only"
    assert classify_candidate(_paper(), set(), {}, {"2607.30000"}, today) == "duplicate_fetch"


def test_classify_candidate_quarantines_invalid_scientific_rows():
    today = dt.date(2026, 7, 31)
    assert classify_candidate(_paper(title="Withdrawn: invalid result"), set(), {}, set(), today) == "quarantine_withdrawn"
    assert classify_candidate(_paper(abstract="This paper has been retracted."), set(), {}, set(), today) == "quarantine_retracted"
    assert classify_candidate(_paper(published="2026-08-01"), set(), {}, set(), today) == "quarantine_bad_date"
    assert classify_candidate(_paper(abstract=""), set(), {}, set(), today) == "quarantine_missing_abstract"
    assert classify_candidate(_paper(abstract="too short"), set(), {}, set(), today) == "quarantine_short_abstract"
    assert classify_candidate(_paper(categories=["cs.AI"]), set(), {}, set(), today) == "quarantine_out_of_scope"


def test_parse_atom_page_preserves_version_and_all_categories():
    xml = b'''<?xml version="1.0"?>
    <feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
      <entry>
        <id>https://arxiv.org/abs/2607.40000v2</id>
        <updated>2026-07-31T01:02:03Z</updated><published>2026-07-30T01:02:03Z</published>
        <title> A fresh galaxy paper </title><summary>''' + b' '.join([b'science'] * 45) + b'''</summary>
        <author><name>Ada Example</name></author>
        <arxiv:primary_category term="astro-ph.HE"/>
        <category term="astro-ph.HE"/><category term="astro-ph.GA"/>
      </entry>
    </feed>'''
    rows = parse_atom_page(xml)
    assert rows[0]["arxiv_id"] == "2607.40000"
    assert rows[0]["observed_version"] == "2607.40000v2"
    assert rows[0]["primary_category"] == "astro-ph.HE"
    assert rows[0]["categories"] == ["astro-ph.HE", "astro-ph.GA"]
    assert rows[0]["authors"] == ["Ada Example"]


def test_request_bytes_with_retries_honors_retry_after():
    headers = Message()
    headers["Retry-After"] = "7"
    attempts = [
        HTTPError("https://example.test", 429, "rate", headers, None),
        BytesIO(b"ok"),
    ]
    sleeps = []

    def opener(_request, timeout):
        result = attempts.pop(0)
        if isinstance(result, Exception):
            raise result
        return result

    body, ledger = request_bytes_with_retries(
        "https://example.test", opener=opener, sleeper=sleeps.append, timeout=3
    )
    assert body == b"ok"
    assert sleeps == [7.0]
    assert [row["status"] for row in ledger] == [429, 200]


def test_reached_date_boundary_uses_oldest_published_date():
    assert reached_date_boundary([_paper(published="2026-07-24")], dt.date(2026, 7, 24)) is True
    assert reached_date_boundary([_paper(published="2026-07-25")], dt.date(2026, 7, 24)) is False


def test_build_shadow_delta_preserves_historical_prefix_and_alignment(tmp_path):
    source = tmp_path / "source"
    target = tmp_path / "shadow"
    source.mkdir()
    historical = {"arxiv_id": "2607.10000", "version": "2607.10000v1", "cluster": 1}
    historical_line = json.dumps(historical) + "\n"
    (source / "new_papers.jsonl").write_text(historical_line)
    (source / "new_labels.json").write_text(json.dumps({"2607.10000": 1}))
    old_vector = np.asarray([[1, 2, 3, 4]], dtype=np.float32)
    (source / "new_emb.f32").write_bytes(old_vector.tobytes())
    source_bytes = (source / "new_emb.f32").read_bytes()

    new_record = {"arxiv_id": "2607.20000", "version": "2607.20000v1", "cluster": 2}
    summary = build_shadow_delta(
        source,
        target,
        [new_record],
        np.asarray([[5, 6, 7, 8]], dtype=np.float32),
        dim=4,
    )

    assert summary == {"before": 1, "added": 1, "after": 2, "embedding_bytes": 32}
    assert (source / "new_papers.jsonl").read_text() == historical_line
    assert (target / "new_papers.jsonl").read_text().startswith(historical_line)
    assert (target / "new_emb.f32").read_bytes().startswith(source_bytes)
    assert json.loads((target / "new_labels.json").read_text()) == {"2607.10000": 1, "2607.20000": 2}


def test_build_shadow_delta_rejects_dimension_mismatch(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    (source / "new_papers.jsonl").write_text("")
    (source / "new_labels.json").write_text("{}")
    (source / "new_emb.f32").write_bytes(b"")
    with pytest.raises(ValueError, match="embedding shape"):
        build_shadow_delta(source, tmp_path / "shadow", [{"arxiv_id": "x", "cluster": -1}], np.ones((1, 3), np.float32), dim=4)


def test_ensure_within_run_rejects_protected_output_path(tmp_path):
    run = tmp_path / "run"
    run.mkdir()
    assert ensure_within_run(run, run / "ranking/preview.json") == (run / "ranking/preview.json").resolve()
    with pytest.raises(ValueError, match="outside approved run root"):
        ensure_within_run(run, tmp_path / "frontend/frontiersData.ts")


def test_validate_and_explain_rerank_enforces_constants_and_rank_arithmetic():
    constants = {"a_half": 12.16, "tension_min": 0.026, "tension_max": 0.434, "growth_min": 0.074, "growth_max": 0.458}
    previous = {
        "v1_constants": constants,
        "clusters": [
            {"cluster": 1, "tractable": 1, "score_v1": 0.8, "size": 10, "strict_tension": 0.2, "recent_frac": 0.3},
            {"cluster": 2, "tractable": 1, "score_v1": 0.7, "size": 10, "strict_tension": 0.2, "recent_frac": 0.3},
        ],
    }
    current = {
        "v1_constants": constants,
        "constants_frozen": True,
        "clusters": [
            {"cluster": 1, "tractable": 1, "score_v1": 0.6, "size": 11, "strict_tension": 0.19, "recent_frac": 0.35},
            {"cluster": 2, "tractable": 1, "score_v1": 0.9, "size": 11, "strict_tension": 0.25, "recent_frac": 0.35},
        ],
    }
    result = validate_and_explain_rerank(previous, current, [{"arxiv_id": "new", "cluster": 2}])
    by_cluster = {row["cluster"]: row for row in result["explanations"]}
    assert by_cluster[1]["previous_rank"] == 1 and by_cluster[1]["current_rank"] == 2
    assert by_cluster[1]["rank_delta"] == -1
    assert by_cluster[2]["new_paper_ids"] == ["new"]
    assert sorted(row["current_rank"] for row in result["explanations"]) == [1, 2]

    changed = {**current, "v1_constants": {**constants, "a_half": 99}}
    with pytest.raises(ValueError, match="frozen v1 constants changed"):
        validate_and_explain_rerank(previous, changed, [])


def test_assign_records_uses_frozen_thresholds_and_retains_novel_rows():
    papers = [_paper(arxiv_id="a", observed_version="av1"), _paper(arxiv_id="b", observed_version="bv1")]
    vectors = np.asarray([[1.0, 0.0], [1.0, 1.0]], dtype=np.float32)
    centroids = np.asarray([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32)
    records, report = assign_records(
        papers,
        vectors,
        centroids,
        {"order": [10, 20], "tau_assign": 0.8, "tau_drift": 0.75},
    )
    assert [row["cluster"] for row in records] == [10, -1]
    assert records[1]["drift_far"] is True
    assert report["assigned"] == 1 and report["novel_or_noise"] == 1 and report["drift_far"] == 1


def test_verify_protected_hashes_detects_input_drift(tmp_path):
    protected = tmp_path / "protected.txt"
    protected.write_text("before")
    import hashlib
    lock = {"protected_files": {str(protected): {"sha256": hashlib.sha256(b"before").hexdigest(), "bytes": 6}}}
    assert verify_protected_hashes(lock) == []
    protected.write_text("after")
    assert verify_protected_hashes(lock)[0]["path"] == str(protected)
