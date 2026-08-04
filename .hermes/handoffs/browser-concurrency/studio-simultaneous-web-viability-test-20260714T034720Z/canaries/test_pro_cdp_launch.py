import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pro_cdp_launch import (
    build_chrome_args,
    is_dedicated_root,
    listener_is_loopback,
    sanitize_targets,
)


def test_dedicated_root_requires_real_chrome_root_and_exact_profile():
    profile = "/tmp/packet/dr-live-cdp-20260714"
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    command = f"{chrome} --user-data-dir={profile} --remote-debugging-port=9223"
    assert is_dedicated_root(1, command, profile)
    assert not is_dedicated_root(9, command, profile)
    assert not is_dedicated_root(1, f"sh -c {command!r}", profile)
    assert not is_dedicated_root(1, command.replace(profile, profile + "-other"), profile)


def test_launch_args_are_visible_loopback_only_and_use_exact_profile():
    args = build_chrome_args("/tmp/fresh-profile", 9223, "https://accounts.google.com/")
    assert args[:4] == ["open", "-na", "Google Chrome", "--args"]
    assert "--user-data-dir=/tmp/fresh-profile" in args
    assert "--remote-debugging-address=127.0.0.1" in args
    assert "--remote-debugging-port=9223" in args
    assert not any("headless" in arg for arg in args)
    assert args[-1] == "https://accounts.google.com/"


def test_listener_must_be_loopback_only():
    good = "Google 123 user 45u IPv4 0x0 TCP 127.0.0.1:9223 (LISTEN)"
    assert listener_is_loopback(good, 9223)
    assert not listener_is_loopback("Google 123 user TCP *:9223 (LISTEN)", 9223)
    assert not listener_is_loopback("Google 123 user TCP 0.0.0.0:9223 (LISTEN)", 9223)
    assert not listener_is_loopback("", 9223)


def test_target_metadata_drops_queries_and_websocket_urls():
    targets = [
        {
            "id": "page-1",
            "type": "page",
            "title": "Sign in",
            "url": "https://accounts.google.com/v3/signin?secret=redact",
            "webSocketDebuggerUrl": "ws://127.0.0.1:9223/devtools/page/page-1",
        }
    ]
    assert sanitize_targets(targets) == [
        {
            "id": "page-1",
            "type": "page",
            "title": "Sign in",
            "url": "https://accounts.google.com/v3/signin",
        }
    ]
