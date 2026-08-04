#!/usr/bin/env python3
"""Deterministic generator for synthetic, browser-free test fixtures.

Emits generic chat-product DOM (NO Google assets, NO branding, NO network) plus targets.json.
Ground truth lives in the hand-authored EXPECTED_VERDICTS.json, NOT here. Deterministic: no
timestamps/random, so sha256 of outputs is stable across regenerations. Run:
    python3 tests/gen_fixtures.py
Outputs under tests/fixtures/.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FX = os.path.join(HERE, "fixtures")
MARKER = "SYNTHETIC_TESTFIXTURE_OUTPUT_DONE_FX20260711"


def page(testid, body):
    # Minimal generic chat-product shell; classifier keys on data-testid + visible text.
    return (
        "<!doctype html>\n<html><head><meta charset=\"utf-8\">"
        "<title>synthetic fixture</title></head>\n"
        f"<body data-app=\"generic-chat\" data-testid=\"{testid}\">\n{body}\n</body></html>\n"
    )


def report_body(lines):
    return "<article class=\"report-body\">\n" + "\n".join(
        f"<p>{ln}</p>" for ln in lines
    ) + "\n</article>"


FIXTURES = {
    "fx_composer_idle.html": page(
        "composer-idle",
        "<div class=\"composer\" data-mode=\"none\">"
        "<button data-testid=\"tool-deep-research\">Deep Research</button>"
        "<textarea data-testid=\"composer-input\"></textarea></div>",
    ),
    "fx_composer_dr_active.html": page(
        "composer-dr-active",
        "<div class=\"composer\" data-mode=\"deep-research\" data-mode-active=\"true\">"
        "<span class=\"chip active\">Deep Research</span>"
        "<textarea data-testid=\"composer-input\"></textarea></div>",
    ),
    "fx_plan_ready.html": page(
        "plan-ready",
        "<div class=\"plan\" data-testid=\"research-plan\"><h2>Research plan</h2>"
        "<ol><li>step</li></ol>"
        "<button data-testid=\"start-research\">Start research</button></div>",
    ),
    "fx_running.html": page(
        "running",
        "<div class=\"run\" data-state=\"running\">"
        "<div data-testid=\"stop-control\">Stop</div>"
        "<progress></progress><span>Researching…</span></div>",
    ),
    "fx_ack_no_control.html": page(
        "ack-no-control",
        "<div class=\"run\" data-state=\"acknowledged\">"
        "<span>Request received</span>"
        "<!-- no stop control, no streamed sections, no progress: R14 signature --></div>",
    ),
    "fx_complete_ok.html": page(
        "complete-ok",
        "<div class=\"run\" data-state=\"complete\">"
        + report_body(["Section 1.", "Section 2.", MARKER])
        + "</div>",
    ),
    "fx_complete_marker_missing.html": page(
        "complete-marker-missing",
        "<div class=\"run\" data-state=\"complete\">"
        + report_body(["Section 1.", "Section 2.", "End of Report"])
        + "</div>",
    ),
    "fx_complete_marker_dup.html": page(
        "complete-marker-dup",
        "<div class=\"run\" data-state=\"complete\">"
        + report_body([MARKER, "Section 2.", MARKER])
        + "</div>",
    ),
    "fx_verification_wall.html": page(
        "verification-wall",
        "<div data-testid=\"interstitial\" data-kind=\"verification\">"
        "<h1>Verify you are human</h1><p>Unusual traffic detected.</p></div>",
    ),
    "fx_billing_upsell.html": page(
        "billing-upsell",
        "<div data-testid=\"interstitial\" data-kind=\"billing\">"
        "<h1>Upgrade your plan</h1><button>Buy</button></div>",
    ),
    "fx_login_wall.html": page(
        "login-wall",
        "<div data-testid=\"interstitial\" data-kind=\"login\">"
        "<h1>Sign in</h1><input type=\"password\" data-testid=\"password\"></div>",
    ),
    "fx_stale_dom.html": page(
        "stale-dom",
        "<div class=\"run\" data-state=\"stale\" data-stale=\"true\">"
        "<span>Content may be out of date</span></div>",
    ),
}

TARGETS = {
    "note": "T2 exact-target custody: each conversation id maps to the fixture the shim must "
            "classify while echoing THIS id. Addressing any other id, or a default/first target, "
            "is a FAIL.",
    "targets": [
        {"conversation_id": "conv-alpha", "fixture": "fx_complete_ok.html"},
        {"conversation_id": "conv-bravo", "fixture": "fx_running.html"},
        {"conversation_id": "conv-charlie", "fixture": "fx_plan_ready.html"},
    ],
}


def main():
    os.makedirs(FX, exist_ok=True)
    for name, html in sorted(FIXTURES.items()):
        with open(os.path.join(FX, name), "w", encoding="utf-8") as fh:
            fh.write(html)
    with open(os.path.join(FX, "targets.json"), "w", encoding="utf-8") as fh:
        json.dump(TARGETS, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"wrote {len(FIXTURES)} html fixtures + targets.json to {FX}")


if __name__ == "__main__":
    main()
