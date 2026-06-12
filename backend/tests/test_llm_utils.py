from app.services.llm_utils import clean_llm_response, strip_think_blocks


def test_strip_closed_think_block():
    raw = "<think>chain of thought</think>###VERDICT: SUPPORTS"
    assert strip_think_blocks(raw) == "###VERDICT: SUPPORTS"


def test_strip_thinking_variant():
    raw = "<thinking>...</thinking>final answer"
    assert strip_think_blocks(raw) == "final answer"


def test_strip_unclosed_think_block():
    raw = "<think>I am thinking but ran out of tokens"
    assert strip_think_blocks(raw) == ""


def test_strip_multiple_think_blocks():
    raw = "<think>a</think>middle<think>b</think>end"
    assert strip_think_blocks(raw) == "middleend"


def test_strip_decoy_verdict_inside_think_does_not_survive():
    raw = (
        "<think>tentatively ###VERDICT: REFUTES, but reconsidering</think>"
        "###VERDICT: SUPPORTS\n###SENTENCE: NONE\n###CONFIDENCE: HIGH"
    )
    out = strip_think_blocks(raw)
    assert "REFUTES" not in out
    assert "###VERDICT: SUPPORTS" in out


def test_clean_llm_response_unwraps_json_fence():
    raw = '<think>x</think>```json\n{"a": 1}\n```'
    assert clean_llm_response(raw) == '{"a": 1}'
