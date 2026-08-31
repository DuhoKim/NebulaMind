#!/usr/bin/env python3
"""Prove denial outside and success inside the three-store mediator boundary."""
import json
import stat
import sys

import bs2k_stage_v2 as stage


def main() -> int:
    receipt = {"model": "0700 directory roots plus mediator capability process path",
               "residual": "owner/root can bypass POSIX modes on a single-user machine",
               "stores": {}}
    for root in stage.store_roots():
        mode = stat.S_IMODE(root.stat().st_mode)
        if mode != 0o700:
            raise AssertionError(f"{root}: mode {mode:o}, expected 700")
        try:
            stage.direct_store_read(root)
        except stage.Refusal as exc:
            outside = exc.code
        else:
            raise AssertionError(f"raw read unexpectedly succeeded: {root}")
        inside = stage.mediator_read(root).decode().strip()
        if outside != stage.REFUSAL_DIRECT or inside != "mediator-boundary-green":
            raise AssertionError(root)
        receipt["stores"][root.name] = {"outside": outside, "mediator": "SUCCEEDED",
                                              "root_mode": "0700"}
    print(json.dumps(receipt, sort_keys=True))
    print("boundary fixtures: 6/6 green (3 refusal, 3 mediator success)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
