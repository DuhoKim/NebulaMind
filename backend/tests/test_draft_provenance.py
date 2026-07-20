"""Tests for draft provenance capture (structured revision history)."""
import json

from app.services.draft_provenance import (
    parse_review_loop,
    build_history,
    append_event,
    write_history_json,
    backfill,
)

LOOP_2CYCLE = (
    "# Automated review-revise loop\n\n"
    "Model: astrosage-70b:latest. Converged to **MINOR** after 2 cycle(s).\n\n"
    "## Cycle 1 — VERDICT: MAJOR\nVERDICT: MAJOR\n"
    "The draft overclaims and misses caveats.\n\n"
    "<details><summary>draft reviewed in cycle 1</summary>\nAlpha beta gamma one two.\n</details>\n\n"
    "## Cycle 2 — VERDICT: MINOR\nVERDICT: MINOR\n"
    "Much improved; minor calibration note.\n\n"
    "<details><summary>draft reviewed in cycle 2</summary>\nAlpha beta gamma delta epsilon three four five.\n</details>\n\n"
    "## Final manuscript body\nAlpha beta gamma delta epsilon three four five.\n"
)


def _write_run(tmp_path, rid="r1", loop=LOOP_2CYCLE):
    (tmp_path / rid).mkdir()
    (tmp_path / rid / "review_loop.md").write_text(loop, encoding="utf-8")
    (tmp_path / f"{rid}.json").write_text(
        json.dumps({
            "id": rid,
            "created_utc": "2026-07-20T00:00:00Z",
            "spec": {"topic": "cosmic-chemical-evolution", "topic_source": "frontier-map"},
            "result": {"review_model": "astrosage-70b:latest", "review_verdict": "MINOR"},
        }),
        encoding="utf-8",
    )
    return rid


def test_parse_review_loop_multi_cycle():
    p = parse_review_loop(LOOP_2CYCLE)
    assert p["model"] == "astrosage-70b:latest"
    assert p["convergedVerdict"] == "MINOR"
    assert [c["n"] for c in p["cycles"]] == [1, 2]
    assert [c["verdict"] for c in p["cycles"]] == ["MAJOR", "MINOR"]
    # the duplicated "VERDICT: X" line is stripped from the feedback body
    assert not p["cycles"][0]["feedback"].startswith("VERDICT")
    assert "overclaims" in p["cycles"][0]["feedback"]
    # the <details> draft is separated out
    assert "Alpha beta gamma one two" in p["cycles"][0]["draft"]
    # the final body never leaks into the last cycle draft
    assert "epsilon three four five" in p["final"]


def test_parse_empty_and_single_cycle():
    assert parse_review_loop("garbage")["cycles"] == []
    single = (
        "Model: astrosage-70b:latest. Converged to **ACCEPT** after 1 cycle(s).\n\n"
        "## Cycle 1 — VERDICT: ACCEPT\nVERDICT: ACCEPT\nLooks good.\n"
    )
    p = parse_review_loop(single)
    assert len(p["cycles"]) == 1 and p["cycles"][0]["verdict"] == "ACCEPT"


def test_build_history_referee_and_lineage(tmp_path):
    rid = _write_run(tmp_path)
    meta = json.loads((tmp_path / f"{rid}.json").read_text())
    h = build_history(rid, tmp_path / rid, meta)
    assert h["runId"] == rid
    assert h["model"] == "astrosage-70b:latest"
    assert h["converged"] == "MINOR"
    # real lineage from metadata
    assert h["lineage"]["topicSource"] == "frontier-map"
    assert h["lineage"]["topic"] == "cosmic-chemical-evolution"
    # two referee revisions, categorised, first pass has no diff, second has a diff
    refs = [r for r in h["revisions"] if r["feedbackSource"] == "referee-model"]
    assert len(refs) == 2
    assert refs[0]["changed"]["diffStat"] is None
    assert refs[1]["changed"]["diffStat"]["added"] > 0
    assert "overclaim" in refs[0]["feedbackKind"]["categories"]
    # honest absences by default
    assert h["humanFeedback"]["captured"] is False
    assert h["gates"]["captured"] is False


def test_capture_human_feedback_flips_absence(tmp_path):
    rid = _write_run(tmp_path)
    append_event(tmp_path / rid, {
        "feedbackSource": "human",
        "feedbackBy": "duho",
        "verdict": "REJECT",
        "categories": ["novelty", "motivation"],
        "feedbackText": "Not publishable — needs wiki-grounded motivation.",
        "timestamp": "2026-07-20T01:00:00Z",
    })
    meta = json.loads((tmp_path / f"{rid}.json").read_text())
    h = build_history(rid, tmp_path / rid, meta)
    assert h["humanFeedback"]["captured"] is True
    human = [r for r in h["revisions"] if r["feedbackSource"] == "human"]
    assert len(human) == 1 and human[0]["feedbackBy"] == "duho"
    assert human[0]["feedbackKind"]["verdict"] == "REJECT"


def test_write_and_backfill(tmp_path):
    rid = _write_run(tmp_path)
    out = write_history_json(rid, tmp_path)
    assert out is not None and out.exists()
    # history.json added to the metadata artifact list
    meta = json.loads((tmp_path / f"{rid}.json").read_text())
    assert "history.json" in meta["artifacts"]
    # backfill picks it up
    ids = backfill(tmp_path)
    assert rid in ids
