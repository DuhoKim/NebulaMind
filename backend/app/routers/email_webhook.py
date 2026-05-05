from fastapi import APIRouter, Request
import subprocess
import os

router = APIRouter(prefix="/webhook", tags=["webhook"])

OPENCLAW_BIN = "/Users/duhokim/.nvm/versions/node/v24.13.0/bin/openclaw"
NODE_BIN = "/Users/duhokim/.nvm/versions/node/v24.13.0/bin"
GATEWAY_TOKEN = "e9eb45dac8ed04b86af638622ad10d8b0374d0b994cdc32c"

@router.post("/email")
async def receive_email(request: Request):
    data = await request.json()

    from_addr = data.get("from", "")
    subject = data.get("subject", "(no subject)")
    body = data.get("body", "")
    timestamp = data.get("timestamp", "")

    message = f"""📧 새 메일 도착!
From: {from_addr}
Subject: {subject}
Time: {timestamp}

{body[:1000]}"""

    env = {
        **os.environ,
        "PATH": f"{NODE_BIN}:/usr/local/bin:/usr/bin:/bin",
        "HOME": "/Users/duhokim",
    }

    result = subprocess.run(
        [
            OPENCLAW_BIN, "system", "event",
            "--text", message,
            "--mode", "now",
            "--token", GATEWAY_TOKEN,
        ],
        capture_output=True,
        text=True,
        env=env,
        timeout=10
    )

    return {
        "status": "ok",
        "stdout": result.stdout[-200:] if result.stdout else "",
        "stderr": result.stderr[-200:] if result.stderr else "",
        "returncode": result.returncode
    }
