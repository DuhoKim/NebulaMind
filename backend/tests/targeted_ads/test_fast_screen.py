import pytest

from app.services.paper_search import PaperRecord
from scripts import targeted_ads_miner as miner


def make_candidate(claim_id: int, title: str) -> miner.Candidate:
    claim = miner.ClaimSnapshot(
        id=claim_id,
        text="AGN feedback quenches star formation in massive galaxies.",
        section="AGN Feedback & Quenching Debates",
        claim_type="debated",
    )
    record = PaperRecord(
        title=title,
        abstract="This abstract discusses AGN feedback, gas removal, and star formation quenching.",
        year=2024,
        arxiv_id=f"2401.{claim_id:05d}",
    )
    return miner.Candidate(claim=claim, record=record, terms=[], query="q")


def test_build_screen_batches_stable_refs_and_batch_size():
    candidates = [
        make_candidate(10, "Paper A"),
        make_candidate(10, "Paper B"),
        make_candidate(11, "Paper C"),
    ]

    batches = miner.build_screen_batches(candidates, batch_size=2)

    assert [item.ref for batch in batches for item in batch.items] == [0, 1, 2]
    assert [len(batch.items) for batch in batches] == [2, 1]
    assert batches[0].items[0].candidate.record.title == "Paper A"
    assert batches[1].items[0].candidate.record.title == "Paper C"


def test_screen_prompt_groups_by_claim_id_and_keeps_refs():
    batch = miner.ScreenBatch(
        items=[
            miner.ScreenItem(ref=0, candidate=make_candidate(10, "Paper A")),
            miner.ScreenItem(ref=1, candidate=make_candidate(10, "Paper B")),
            miner.ScreenItem(ref=2, candidate=make_candidate(11, "Paper C")),
        ]
    )

    prompt = miner.screen_prompt(batch)

    assert prompt.count("CLAIM 10:") == 1
    assert prompt.count("CLAIM 11:") == 1
    assert "[ref 0]" in prompt
    assert "[ref 1]" in prompt
    assert "[ref 2]" in prompt


def test_parse_screen_response_maps_refs_out_of_order():
    raw = """
    ```json
    [{"ref": 2, "pre_filter": "DISCARD"}, {"ref": 0, "pre_filter": "KEEP"}]
    ```
    """

    outcomes, fallback = miner.parse_screen_response(raw, {0, 2})

    assert fallback is False
    assert outcomes[0].pre_filter == "KEEP"
    assert outcomes[2].pre_filter == "DISCARD"
    assert outcomes[2].fail_open is False


def test_parse_screen_response_missing_ref_fails_open_to_keep():
    raw = '[{"ref": 0, "pre_filter": "DISCARD"}]'

    outcomes, fallback = miner.parse_screen_response(raw, {0, 1})

    assert fallback is True
    assert outcomes[0].pre_filter == "DISCARD"
    assert outcomes[1].pre_filter == "KEEP"
    assert outcomes[1].fail_open is True


@pytest.mark.parametrize("raw", ["not json", '{"ref": 0}', '[{"ref": 0, "pre_filter": "MAYBE"}]'])
def test_parse_screen_response_malformed_or_bad_value_fails_open(raw):
    outcomes, fallback = miner.parse_screen_response(raw, {0})

    assert fallback is True
    assert outcomes[0].pre_filter == "KEEP"
