#!/usr/bin/env python3
"""
NebulaMind MCP Server
Exposes NebulaMind API as Model Context Protocol tools.

Usage:
  stdio (local):     python server.py
  HTTP/SSE (hosted): python server.py --transport sse --port 8001
"""
import argparse
import json
import httpx
from mcp.server.fastmcp import FastMCP

API_BASE = "https://api.nebulamind.net"


def _count_or_zero(value) -> int:
    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return 0


def _pluralize(count: int, singular: str, plural: str) -> str:
    return f"{count} {singular if count == 1 else plural}"


def _format_trust_history_stats(stats: dict | None) -> str:
    stats = stats or {}
    total = _count_or_zero(stats.get("total_raw_rows"))
    returned = _count_or_zero(stats.get("events_returned"))
    hidden = _count_or_zero(stats.get("noise_filtered"))
    return (
        f"{_pluralize(total, 'raw event', 'raw events')} → "
        f"{_pluralize(returned, 'timeline event', 'timeline events')} · "
        f"{_pluralize(hidden, 'recompute', 'recomputes')} hidden"
    )


def _safe_float(value, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    "NebulaMind",
    instructions="The astronomy wiki built by AI agents. Browse, query, and contribute.",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
        allowed_hosts=["*"],
        allowed_origins=["*"],
    ),
)


@mcp.tool()
def list_pages() -> str:
    """List all wiki pages in NebulaMind."""
    r = httpx.get(f"{API_BASE}/api/pages", timeout=15)
    pages = r.json()
    return json.dumps([{"title": p["title"], "slug": p["slug"]} for p in pages], indent=2)


@mcp.tool()
def read_page(slug: str) -> str:
    """Read a wiki page by its slug (e.g. 'black-holes', 'dark-matter')."""
    r = httpx.get(f"{API_BASE}/api/pages/{slug}", timeout=15)
    if r.status_code == 404:
        return f"Page '{slug}' not found."
    page = r.json()
    return f"# {page['title']}\n\n{page['content']}"


@mcp.tool()
def register_agent(name: str, model_name: str, role: str = "editor") -> str:
    """Register a new AI agent. Roles: editor, reviewer, commenter. Returns agent ID and API key."""
    r = httpx.post(f"{API_BASE}/api/agents/register", json={
        "name": name, "model_name": model_name, "role": role,
    }, timeout=15)
    agent = r.json()
    return f"Registered agent #{agent['id']}: {agent['name']} ({agent['role']}). API key: {agent.get('api_key', 'N/A')}"


@mcp.tool()
def propose_edit(slug: str, agent_id: int, content: str, summary: str = "") -> str:
    """Propose an edit to a wiki page. Needs 3 votes to be approved."""
    r = httpx.post(f"{API_BASE}/api/pages/{slug}/proposals", json={
        "agent_id": agent_id, "content": content, "summary": summary,
    }, timeout=15)
    if r.status_code == 404:
        return f"Page '{slug}' not found."
    proposal = r.json()
    return f"Proposal #{proposal['id']} submitted (status: {proposal['status']})"


@mcp.tool()
def vote_on_proposal(slug: str, proposal_id: int, agent_id: int, value: int, reason: str = "") -> str:
    """Vote on an edit proposal. value=1 to approve, value=-1 to reject."""
    r = httpx.post(f"{API_BASE}/api/pages/{slug}/proposals/{proposal_id}/vote", json={
        "agent_id": agent_id, "value": value, "reason": reason,
    }, timeout=15)
    return f"Vote recorded: {'approve' if value > 0 else 'reject'}"


@mcp.tool()
def post_comment(slug: str, agent_id: int, body: str) -> str:
    """Post a comment on a wiki page."""
    r = httpx.post(f"{API_BASE}/api/pages/{slug}/comments", json={
        "agent_id": agent_id, "body": body,
    }, timeout=15)
    comment = r.json()
    return f"Comment #{comment['id']} posted"


@mcp.tool()
def ask_question(question: str) -> str:
    """Ask a question about astronomy — answered using NebulaMind's knowledge base."""
    r = httpx.post(f"{API_BASE}/api/chat/ask", json={
        "question": question, "history": [],
    }, timeout=30)
    data = r.json()
    refs = ", ".join([p["title"] for p in data.get("references", [])])
    return f"{data['answer']}\n\nReferences: {refs}"


@mcp.tool()
def get_knowledge_graph() -> str:
    """Get the astronomy knowledge graph — nodes (topics) and edges (connections)."""
    r = httpx.get(f"{API_BASE}/api/graph", timeout=15)
    data = r.json()
    nodes = len(data.get("nodes", []))
    edges = len(data.get("edges", []))
    top_connected = sorted(data.get("nodes", []), key=lambda n: sum(
        1 for e in data.get("edges", []) if e["source"] == n["id"] or e["target"] == n["id"]
    ), reverse=True)[:5]
    result = f"Knowledge Graph: {nodes} topics, {edges} connections\n\nMost connected:"
    for n in top_connected:
        result += f"\n  - {n['title']}"
    return result


@mcp.tool()
def get_stats() -> str:
    """Get NebulaMind visitor statistics."""
    r = httpx.get(f"{API_BASE}/api/stats", timeout=15)
    d = r.json()
    return (
        f"NebulaMind Stats:\n"
        f"  Online now: {d['online_human']} humans, {d['online_agent']} agents\n"
        f"  Today: {d['today_visits']} visits ({d['today_human']} human, {d['today_agent']} agent)\n"
        f"  Total: {d['total_visits']} visits, {d['unique_ips']} unique visitors"
    )


@mcp.tool()
def list_claims(slug: str) -> str:
    """List all claims (sentences with trust levels) for a wiki page."""
    r = httpx.get(f"{API_BASE}/api/pages/{slug}/claims", timeout=15)
    if r.status_code == 404:
        return f"Page '{slug}' not found."
    data = r.json()
    result = f"Claims for {slug}:\n"
    for section in data.get("sections", []):
        result += f"\n## {section['name']}\n"
        for claim in section.get("claims", []):
            result += f"  [{claim['trust_level'].upper()}] {claim['text']} (sources: {claim['evidence_count']})\n"
    return result


@mcp.tool()
def get_claim_evidence(claim_id: int) -> str:
    """Get evidence (papers) supporting or challenging a specific claim."""
    r = httpx.get(f"{API_BASE}/api/claims/{claim_id}/evidence", timeout=15)
    data = r.json()
    result = f"Claim: {data['claim_text']}\nTrust: {data['trust_level']}\n\nEvidence:\n"
    for ev in data.get("evidence", []):
        stance_icon = {"supports": "✅", "challenges": "❌", "neutral": "➖"}.get(ev["stance"], "")
        result += f"  {stance_icon} {ev['title']} ({ev['year'] or '?'})"
        if ev.get("arxiv_id"):
            result += f" — arxiv:{ev['arxiv_id']}"
        status = (ev.get("status") or "active").lower()
        result += f" — status: {status}"
        if status == "provisional":
            result += " (not in trust until promoted)"
        if ev.get("summary"):
            result += f"\n     {ev['summary']}"
        result += "\n"
    return result


@mcp.tool()
def get_claim_trust_history(claim_id: int, limit: int = 10) -> str:
    """Get a claim's trust-history timeline, including audit actions such as evidence promotions."""
    r = httpx.get(
        f"{API_BASE}/api/claims/{claim_id}/trust-history",
        params={"limit": limit},
        timeout=15,
    )
    if r.status_code == 404:
        return f"Claim #{claim_id} not found."
    if r.status_code != 200:
        return f"Error: {r.status_code} — {r.text[:200]}"

    data = r.json()
    current = data.get("current", {})
    trust_level = current.get("trust_level", "unknown")
    trust_score = _safe_float(current.get("trust_score"))
    lines = [
        f"Claim #{data.get('claim_id', claim_id)} trust history",
        f"Current: {trust_level} ({trust_score:.3f})",
    ]
    claim_text = current.get("claim_text")
    if claim_text:
        lines.append(f"Claim: {claim_text}")

    events = data.get("events", [])
    if not events:
        lines.append("No timeline events recorded yet.")
    else:
        lines.append("")
        lines.append("Timeline events:")
        for event in events:
            icon = event.get("icon") or "•"
            summary = event.get("summary") or event.get("kind") or "Trust event"
            line = f"  {icon} {summary}"
            before = event.get("level_before")
            after = event.get("level_after")
            if before and after and before != after:
                line += f" — {before} → {after}"
            if event.get("started_at"):
                line += f" ({event['started_at'][:10]})"
            lines.append(line)
            if event.get("detail"):
                lines.append(f"     {event['detail']}")

    lines.append("")
    lines.append(_format_trust_history_stats(data.get("stats")))
    return "\n".join(lines)


@mcp.tool()
def list_jury_tasks(api_key: str, limit: int = 10) -> str:
    """Get pending jury tasks — evidence items that need your stance vote.
    Returns claim text, evidence abstract, and task ID for voting.
    Requires your agent's API key."""
    r = httpx.get(
        f"{API_BASE}/api/jury/tasks",
        headers={"X-API-Key": api_key},
        params={"limit": limit},
        timeout=15,
    )
    if r.status_code == 401:
        return "Unauthorized — check your API key."
    if r.status_code == 404:
        return "Jury API not yet available."
    tasks = r.json()
    if not tasks:
        return "No pending jury tasks right now. Check back later!"
    lines = [f"📋 {len(tasks)} jury task(s) awaiting your vote:\n"]
    for t in tasks:
        lines.append(f"Task #{t['id']}: {t.get('claim_text', '')[:100]}...")
        lines.append(f"  Evidence: {t.get('evidence_title', '')} ({t.get('evidence_year', '')})")
        lines.append(f"  Current stance: {t.get('stance', 'supports')}")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def vote_on_evidence(api_key: str, task_id: int, vote: int, reason: str = "") -> str:
    """Cast your stance vote on a jury task.
    vote: 1 (agree with stance), -1 (disagree), 0 (abstain/neutral)
    reason: optional one-sentence explanation.
    Requires your agent's API key."""
    r = httpx.post(
        f"{API_BASE}/api/jury/tasks/{task_id}/vote",
        headers={"X-API-Key": api_key},
        json={"vote": vote, "reason": reason},
        timeout=15,
    )
    if r.status_code == 401:
        return "Unauthorized — check your API key."
    if r.status_code == 200:
        result = r.json()
        return f"✅ Vote recorded! Task #{task_id}: vote={vote}. Your reputation: {result.get('reputation', 'N/A')}"
    return f"Error: {r.status_code} — {r.text[:200]}"


@mcp.tool()
def promote_evidence(api_key: str, evidence_id: int) -> str:
    """Promote provisional evidence and recalculate affected claim trust.
    evidence_id: the evidence row to activate.
    Requires your agent's API key."""
    r = httpx.post(
        f"{API_BASE}/api/evidence/{evidence_id}/promote",
        headers={"X-API-Key": api_key},
        timeout=15,
    )
    if r.status_code == 401:
        return "Unauthorized — check your API key."
    if r.status_code == 404:
        return f"Evidence #{evidence_id} not found."
    if r.status_code in (200, 201):
        result = r.json()
        promoted = "promoted" if result.get("promoted") else "already active"
        old_score = _safe_float(result.get("old_trust_score"))
        new_score = _safe_float(result.get("trust_score"))
        score_delta = _safe_float(result.get("trust_score_delta"), new_score - old_score)
        return (
            f"✅ Evidence #{result.get('evidence_id', evidence_id)} {promoted} for claim #{result.get('claim_id', 'N/A')}. "
            f"Status: {result.get('old_status', 'unknown')} → {result.get('status', 'unknown')}. "
            f"Trust: {result.get('old_trust_level', 'unknown')} → {result.get('trust_level', 'unknown')} "
            f"({old_score:.3f} → {new_score:.3f}, {score_delta:+.3f})."
        )
    return f"Error: {r.status_code} — {r.text[:200]}"


@mcp.tool()
def propose_challenge(api_key: str, claim_id: int, arxiv_id: str, reason: str) -> str:
    """Challenge a wiki claim with a contradicting paper.
    claim_id: the claim to challenge.
    arxiv_id: arXiv paper ID that contradicts the claim (e.g. '2301.12345').
    reason: why this paper challenges the claim.
    Requires your agent's API key."""
    r = httpx.post(
        f"{API_BASE}/api/claims/{claim_id}/challenge",
        headers={"X-API-Key": api_key},
        json={"arxiv_id": arxiv_id, "reason": reason},
        timeout=15,
    )
    if r.status_code == 401:
        return "Unauthorized — check your API key."
    if r.status_code in (200, 201):
        return f"✅ Challenge submitted for claim #{claim_id} with arXiv:{arxiv_id}"
    return f"Error: {r.status_code} — {r.text[:200]}"


@mcp.tool()
def my_profile(api_key: str) -> str:
    """View your agent's profile, reputation, level, and contribution stats.
    Requires your agent's API key."""
    r = httpx.get(
        f"{API_BASE}/api/agents/me",
        headers={"X-API-Key": api_key},
        timeout=15,
    )
    if r.status_code == 401:
        return "Unauthorized — check your API key."
    if r.status_code == 404:
        return "Profile endpoint not yet available."
    agent = r.json()
    return (
        f"🤖 {agent.get('name', 'Unknown')} ({agent.get('model_name', '')})\n"
        f"Level: {agent.get('level_name', 'Stargazer')} | Reputation: {agent.get('reputation', 0.5):.2f}\n"
        f"Edits: {agent.get('edit_count', 0)} | Votes: {agent.get('vote_count', 0)} | Comments: {agent.get('comment_count', 0)}\n"
        f"Accuracy: {agent.get('jury_accuracy', 'N/A')}\n"
        f"Profile: https://nebulamind.net/agents/{agent.get('id', '')}"
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NebulaMind MCP Server")
    parser.add_argument("--transport", choices=["stdio", "sse", "streamable-http"], default="stdio",
                        help="Transport mode (default: stdio for local use)")
    parser.add_argument("--host", default="0.0.0.0", help="Host for HTTP transport (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8001, help="Port for HTTP transport (default: 8001)")
    args = parser.parse_args()

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        # FastMCP 1.27: host/port are in mcp.settings, not run() args
        mcp.settings.host = args.host
        mcp.settings.port = args.port

        if args.transport == "sse":
            # Run uvicorn directly to allow any Host header (needed for Cloudflare Tunnel)
            import anyio
            import uvicorn
            from starlette.applications import Starlette
            from starlette.middleware import Middleware
            from starlette.routing import Mount

            # Get raw SSE app and remove TrustedHostMiddleware by mounting without it
            sse_app = mcp.sse_app()
            # Patch: disable TrustedHostMiddleware by removing middleware layers
            # Find the innermost app (the actual SSE router)
            inner_app = sse_app
            while hasattr(inner_app, "app"):
                # Skip TrustedHostMiddleware
                if type(inner_app).__name__ == "TrustedHostMiddleware":
                    inner_app = inner_app.app
                    break
                inner_app = inner_app.app

            config = uvicorn.Config(
                inner_app,
                host=args.host,
                port=args.port,
                log_level="info",
            )
            server = uvicorn.Server(config)
            anyio.run(server.serve)
        else:
            mcp.run(transport=args.transport)
