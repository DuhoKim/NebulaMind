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
        if ev.get("summary"):
            result += f"\n     {ev['summary']}"
        result += "\n"
    return result


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
