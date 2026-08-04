import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import dr_submit_one as driver


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self):
        return json.dumps(self.payload).encode()


def patch_targets(monkeypatch, targets):
    monkeypatch.setattr(driver.urllib.request, "urlopen", lambda *_args, **_kwargs: FakeResponse(targets))


def target(url, target_id=driver.TARGET_ID):
    return {"id": target_id, "type": "page", "url": url}


def test_exact_initial_target_accepts_only_bare_gemini_app(monkeypatch):
    patch_targets(monkeypatch, [target("https://gemini.google.com/app")])
    assert driver.exact_target(require_initial=True)["id"] == driver.TARGET_ID

    patch_targets(monkeypatch, [target("https://gemini.google.com/app/abc")])
    assert driver.exact_target(require_initial=True) is None


def test_conversation_target_requires_exact_id_and_origin(monkeypatch):
    patch_targets(monkeypatch, [target("https://gemini.google.com/app/abc")])
    assert driver.exact_target(require_initial=False)["url"].endswith("/abc")

    patch_targets(monkeypatch, [target("https://evil.example/app/abc")])
    assert driver.exact_target(require_initial=False) is None

    patch_targets(monkeypatch, [target("https://gemini.google.com/app/abc", "wrong")])
    assert driver.exact_target(require_initial=False) is None


def test_duplicate_exact_target_fails_closed(monkeypatch):
    t = target("https://gemini.google.com/app")
    patch_targets(monkeypatch, [t, dict(t)])
    assert driver.exact_target(require_initial=True) is None


def test_need_rejects_broker_denial():
    with pytest.raises(RuntimeError, match="denied"):
        driver.need({"ok": False, "deny": "held"}, "denied")
