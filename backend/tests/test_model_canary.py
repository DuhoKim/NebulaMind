from app.services import model_canary


class _FakeOpenAICompatResponse:
    status_code = 200
    text = "{}"

    def __init__(self, payload):
        self.payload = payload

    def json(self):
        max_tokens = self.payload.get("max_tokens") or 0
        if max_tokens < 64:
            return {
                "choices": [
                    {
                        "message": {
                            "role": "assistant",
                            "content": "",
                            "reasoning": "The canary answer is still in hidden reasoning.",
                        },
                        "finish_reason": "length",
                    }
                ]
            }
        return {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": "ok",
                        "reasoning": "The canary answer can now reach visible content.",
                    },
                    "finish_reason": "stop",
                }
            ]
        }


def test_gpt_oss_canary_allows_reasoning_tokens_before_visible_content(monkeypatch):
    calls = []

    def fake_post(url, *, headers, json, timeout):
        calls.append({"url": url, "headers": headers, "json": json, "timeout": timeout})
        return _FakeOpenAICompatResponse(json)

    monkeypatch.setattr(model_canary.httpx, "post", fake_post)
    monkeypatch.setattr(model_canary, "log_llm_call", lambda *args, **kwargs: None)

    result = model_canary._check_seat(
        model_canary.CanarySeat("Nutty", "http://127.0.0.1:11434", "gpt-oss:20b"),
        notify=False,
    )

    assert result["status"] == "pass"
    assert result["content_preview"] == "ok"
    assert calls[0]["json"]["max_tokens"] >= 64
