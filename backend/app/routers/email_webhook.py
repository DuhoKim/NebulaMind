from fastapi import APIRouter, Request
import subprocess
import os
import base64
import json
import httpx
import email
from email import policy as email_policy
from datetime import datetime
from pathlib import Path

EMAIL_LOG_DIR = Path("/Users/duhokim/NebulaMind/logs/emails")
EMAIL_LOG_DIR.mkdir(parents=True, exist_ok=True)

router = APIRouter(prefix="/webhook", tags=["webhook"])


def _parse_full_email(raw_bytes: bytes) -> tuple[str, list[dict]]:
    """Parse a complete raw RFC 2822 email.

    Returns (body_text, attachments) where each attachment is:
    {"filename": str, "content_type": str, "size": int, "data_b64": str}
    """
    try:
        msg = email.message_from_bytes(raw_bytes, policy=email_policy.default)
    except Exception:
        return raw_bytes.decode("utf-8", errors="replace"), []

    plain_text = None
    html_text = None
    attachments = []

    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            disposition = str(part.get("Content-Disposition") or "")

            if "attachment" in disposition or part.get_filename():
                filename = part.get_filename() or "attachment"
                payload = part.get_payload(decode=True) or b""
                attachments.append({
                    "filename": filename,
                    "content_type": ct,
                    "size": len(payload),
                    "data_b64": base64.b64encode(payload).decode("ascii"),
                })
            elif ct == "text/plain" and plain_text is None:
                payload = part.get_payload(decode=True)
                if payload:
                    plain_text = payload.decode(
                        part.get_content_charset() or "utf-8", errors="replace"
                    )
            elif ct == "text/html" and html_text is None:
                payload = part.get_payload(decode=True)
                if payload:
                    import re
                    html_text = re.sub(
                        r"<[^>]+>",
                        "",
                        payload.decode("utf-8", errors="replace"),
                    )
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            plain_text = payload.decode(
                msg.get_content_charset() or "utf-8", errors="replace"
            )

    body = (plain_text or html_text or "").strip()
    return body, attachments


def _extract_plain_text(raw: str) -> str:
    """Fallback plain-text extractor for legacy body-only payloads."""
    if not raw:
        return ""
    if "Content-Type:" not in raw and "--" not in raw:
        return raw.strip()
    try:
        wrapped = (
            f"MIME-Version: 1.0\nContent-Type: multipart/alternative; boundary=\"boundary\"\n\n{raw}"
            if "MIME-Version" not in raw
            else raw
        )
        msg = email.message_from_string(wrapped, policy=email_policy.default)
        plain = html = None
        if msg.is_multipart():
            for part in msg.walk():
                ct = part.get_content_type()
                if ct == "text/plain" and plain is None:
                    p = part.get_payload(decode=True)
                    if p:
                        plain = p.decode(part.get_content_charset() or "utf-8", errors="replace")
                elif ct == "text/html" and html is None:
                    p = part.get_payload(decode=True)
                    if p:
                        import re
                        html = re.sub(r"<[^>]+>", "", p.decode("utf-8", errors="replace"))
        else:
            p = msg.get_payload(decode=True)
            if p:
                plain = p.decode(msg.get_content_charset() or "utf-8", errors="replace")
        return (plain or html or raw).strip()
    except Exception:
        import re
        clean = re.sub(r"--[\w]+[\r\n]+", "", raw)
        clean = re.sub(r"Content-Type:.*?[\r\n]+", "", clean)
        clean = re.sub(r"Content-Transfer-Encoding:.*?[\r\n]+", "", clean)
        clean = re.sub(r"<[^>]+>", "", clean)
        return clean.strip()


OPENCLAW_BIN = "/Users/duhokim/.nvm/versions/node/v24.13.0/bin/openclaw"
NODE_BIN = "/Users/duhokim/.nvm/versions/node/v24.13.0/bin"
GATEWAY_TOKEN = "e9eb45dac8ed04b86af638622ad10d8b0374d0b994cdc32c"

# Telegram direct delivery
TELEGRAM_BOT_TOKEN = "8592251480:AAFNZjd52cLhnVRqxkeZAjg_AlTqE76D6i0"
TELEGRAM_CHAT_ID = "8572067151"  # Papa's Telegram ID


@router.post("/email")
async def receive_email(request: Request):
    data = await request.json()

    from_addr = data.get("from", "")
    subject = data.get("subject", "(no subject)")
    timestamp = data.get("timestamp", "")

    # Prefer full base64 raw email (new Worker format); fall back to legacy body field
    raw_email_b64 = data.get("raw_email_b64", "")
    attachments: list[dict] = []

    if raw_email_b64:
        try:
            raw_bytes = base64.b64decode(raw_email_b64)
            body, attachments = _parse_full_email(raw_bytes)
        except Exception as exc:
            body = f"(raw email decode error: {exc})"
    else:
        body = _extract_plain_text(data.get("body", ""))

    # Persist email to disk
    email_record = {
        "from": from_addr,
        "subject": subject,
        "body": body,
        "timestamp": timestamp,
        "received_at": datetime.utcnow().isoformat(),
        "attachments": [
            {k: v for k, v in a.items() if k != "data_b64"}
            for a in attachments
        ],
    }
    log_filename = (
        EMAIL_LOG_DIR
        / f"{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{from_addr.split('@')[0][:20]}.json"
    )
    try:
        with open(log_filename, "w") as f:
            json.dump(email_record, f, indent=2, ensure_ascii=False)
    except Exception:
        pass

    attachment_summary = ""
    if attachments:
        lines = [
            f"  • {a['filename']} ({a['content_type']}, {a['size']:,}B)"
            for a in attachments
        ]
        attachment_summary = "\n\nAttachments:\n" + "\n".join(lines)

    message = (
        f"📧 새 메일 도착!\n"
        f"From: {from_addr}\n"
        f"Subject: {subject}\n"
        f"Time: {timestamp}\n"
        f"\n{body[:1000]}"
        f"{attachment_summary}"
    )

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
        timeout=10,
    )

    # Also push directly to Telegram so HwaO receives it regardless of active session
    try:
        tg_text = (
            f"📧 *New mail to hwao@nebulamind.net*\n\n"
            f"*From:* {from_addr}\n"
            f"*Subject:* {subject}\n"
            f"*Time:* {timestamp}\n\n"
            f"{body[:800]}"
        )
        if attachments:
            tg_text += "\n\n📎 " + ", ".join(
                f"{a['filename']} ({a['size']:,}B)" for a in attachments
            )
        async with httpx.AsyncClient(timeout=8) as client:
            await client.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                json={
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": tg_text,
                    "parse_mode": "Markdown",
                },
            )
    except Exception:
        pass

    return {
        "status": "ok",
        "attachments": len(attachments),
        "stdout": result.stdout[-200:] if result.stdout else "",
        "stderr": result.stderr[-200:] if result.stderr else "",
        "returncode": result.returncode,
    }
