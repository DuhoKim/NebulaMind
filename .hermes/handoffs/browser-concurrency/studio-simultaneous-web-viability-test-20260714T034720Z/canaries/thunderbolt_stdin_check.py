"""NO-BROWSER Thunderbolt stdin-fed exec check, both directions (Tori requirement).

Proves the repaired stdin-fed remote execution works over the direct Thunderbolt
link in each direction, reaching the intended host (verified by CPU arch):
  - Studio -> Pro           : expect machine == x86_64 (Mac Pro)
  - Studio -> Pro -> Studio : expect machine == arm64  (Mac Studio, via the Pro->Studio leg)
No browser, no account, no listener; HostKeyAlias-pinned, no Tailscale fallback.

EXECUTION-GATED: refuses without --armed <token>.
Usage: thunderbolt_stdin_check.py --armed <token> <root> <pro_user_host> <pro_alias> <studio_from_pro> <studio_alias> <marker>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from net import matches_pro, matches_studio, ssh_argv  # noqa: E402
from remote_exec import run_python_stdin  # noqa: E402


def marker_script(marker: str) -> str:
    return ("import platform\n"
            f"m = {json.dumps(marker)}\n"
            "print('MARKER ' + m + ' ' + platform.machine() + ' ' + platform.node())\n")


def main(argv):
    if len(argv) < 9 or argv[1] != "--armed":
        print(json.dumps({"check": "REFUSED",
              "reason": "usage: --armed <token> <root> <pro_user_host> <pro_alias> <studio_from_pro> <studio_alias> <marker>"}))
        return 4
    token, root = Path(argv[2]), Path(argv[3]).resolve()
    pro_user_host, pro_alias, studio_from_pro, studio_alias, marker = argv[4], argv[5], argv[6], argv[7], argv[8]
    if not token.exists():
        print(json.dumps({"check": "REFUSED", "reason": "approval token absent"})); return 4
    if not matches_pro(pro_user_host, pro_alias):
        print(json.dumps({"check": "REFUSED", "reason": "pro endpoint/alias != canonical Thunderbolt Pro"})); return 4
    if not matches_studio(studio_from_pro, studio_alias):
        print(json.dumps({"check": "REFUSED", "reason": "studio endpoint/alias != canonical Thunderbolt Studio"})); return 4

    outcome = {"check": "thunderbolt_stdin", "transport": "thunderbolt", "fallback": "none",
               "endpoints": {"pro": {"host": pro_user_host, "host_key_alias": pro_alias},
                             "studio_from_pro": {"host": studio_from_pro, "host_key_alias": studio_alias}},
               "directions": {}}
    try:
        # Direction 1: Studio -> Pro
        rc, out, err = run_python_stdin(ssh_argv(pro_user_host, pro_alias), marker_script(marker), timeout=25)
        d1 = {"rc": rc, "stdout": out.strip(), "stderr": err.strip()[:200]}
        d1["pass"] = (rc == 0 and out.strip().startswith(f"MARKER {marker} ") and " x86_64 " in f" {out.strip()} ")
        outcome["directions"]["studio_to_pro"] = d1

        # Direction 2: Studio -> Pro -> Studio (exercises the Pro->Studio leg)
        channel = [*ssh_argv(pro_user_host, pro_alias), *ssh_argv(studio_from_pro, studio_alias)]
        rc, out, err = run_python_stdin(channel, marker_script(marker), timeout=30)
        d2 = {"rc": rc, "stdout": out.strip(), "stderr": err.strip()[:200]}
        d2["pass"] = (rc == 0 and out.strip().startswith(f"MARKER {marker} ") and " arm64 " in f" {out.strip()} ")
        outcome["directions"]["pro_to_studio"] = d2
    except Exception as e:
        outcome["fatal"] = f"{type(e).__name__}: {e}"

    ok = (outcome["directions"].get("studio_to_pro", {}).get("pass")
          and outcome["directions"].get("pro_to_studio", {}).get("pass") and "fatal" not in outcome)
    outcome["pass"] = bool(ok)
    (root / "receipts/archeval/THUNDERBOLT_STDIN_CHECK_RECEIPT.json").write_text(json.dumps(outcome, indent=1))
    print(json.dumps({"pass": outcome["pass"],
                      "studio_to_pro": outcome["directions"].get("studio_to_pro", {}).get("pass"),
                      "pro_to_studio": outcome["directions"].get("pro_to_studio", {}).get("pass"),
                      "fatal": outcome.get("fatal")}))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
