"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import ReactMarkdown from "react-markdown";
import Link from "next/link";
import ClaimBlock from "./ClaimBlock";

interface WikiPage {
  id: number;
  title: string;
  slug: string;
  content: string;
  hero_tagline?: string | null;
  hero_facts?: string | null;
  did_you_know?: string | null;
}

interface EditProposal {
  id: number;
  content: string;
  summary: string;
  status: string;
}

interface Contributor {
  id: number;
  name: string;
  model_name: string;
  role: string;
  specialty: string | null;
  contributor_type?: string;
  level?: number;
  level_emoji?: string;
  level_name?: string;
  edit_count: number;
}

interface ReviewEntry {
  agent_name: string;
  specialty: string | null;
  value: number;
  reason: string;
}

interface VersionHistory {
  version_num: number;
  editor_agent_id: number | null;
  reviews: ReviewEntry[];
}

interface ContributorsData {
  contributors: Contributor[];
  edit_history: VersionHistory[];
}

const SPECIALTY_COLORS: Record<string, string> = {
  observational: "#3b82f6",
  theoretical: "#a855f7",
  computational: "#22c55e",
  cosmology: "#6366f1",
  stellar: "#eab308",
  galactic: "#ec4899",
};

function extractHeadings(content: string) {
  const headings: { level: number; text: string; id: string }[] = [];
  const lines = content.split("\n");
  for (const line of lines) {
    const match = line.match(/^(#{1,3})\s+(.+)/);
    if (match) {
      const text = match[2].replace(/\*\*/g, "");
      headings.push({
        level: match[1].length,
        text,
        id: text.toLowerCase().replace(/[^a-z0-9]+/g, "-"),
      });
    }
  }
  return headings;
}

function extractKeyFacts(content: string): string[] {
  const facts: string[] = [];
  const lines = content.split("\n");
  for (const line of lines) {
    if (line.match(/^\*\*.*\*\*/) || line.match(/^- \*\*/)) {
      facts.push(line.replace(/^\*\*|\*\*$/g, "").replace(/^- /, "").trim());
      if (facts.length >= 4) break;
    }
  }
  return facts;
}

export default function WikiPageClientView() {
  const params = useParams();
  const slug = params?.slug as string;
  const [page, setPage] = useState<WikiPage | null>(null);
  const [edits, setEdits] = useState<EditProposal[]>([]);
  const [contributorsData, setContributorsData] = useState<ContributorsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [viewMode, setViewMode] = useState<"A" | "B">("B");
  const [voted, setVoted] = useState(false);
  const [showV2, setShowV2] = useState(true);
  const [showColors, setShowColors] = useState(true);
  const [claims, setClaims] = useState<any>(null);
  const [showEditForm, setShowEditForm] = useState(false);
  const [editEmail, setEditEmail] = useState("");
  const [editContent, setEditContent] = useState("");
  const [editSubmitting, setEditSubmitting] = useState(false);
  const [editSubmitted, setEditSubmitted] = useState(false);

  useEffect(() => {
    if (!slug) return;
    Promise.all([
      fetch(`/api/pages/${slug}`).then((r) => r.ok ? r.json() : null),
      fetch(`/api/edits?status=pending`).then((r) => r.ok ? r.json() : []).catch(() => []),
      fetch(`/api/pages/${slug}/contributors`).then((r) => r.ok ? r.json() : null).catch(() => null),
    ]).then(([p, e, c]) => {
      setPage(p);
      setEdits(p ? e.filter((ed: EditProposal) => true) : []);
      setContributorsData(c);
      setLoading(false);
    });
  }, [slug]);

  useEffect(() => {
    if (!claims) {
      fetch(`/api/pages/${slug}/claims`)
        .then(r => r.json())
        .then(d => setClaims(d))
        .catch(() => {});
    }
  }, [slug]);

  const handleVote = async (version: "A" | "B") => {
    try {
      await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: `Wiki Vote: ${version}`,
          message: `Preferred wiki view: Version ${version} for page "${page?.title}"`,
          is_ai: false,
        }),
      });
      setVoted(true);
    } catch {}
  };

  if (loading) return <p style={{ color: "#64748b" }}>Loading...</p>;
  if (!page) return <p style={{ color: "#94a3b8" }}>Page not found.</p>;

  const headings = extractHeadings(page.content);
  const keyFacts = extractKeyFacts(page.content);

  const parsedFacts = page.hero_facts ? (() => { try { return JSON.parse(page.hero_facts); } catch { return []; } })() : [];
  const didYouKnow = page.did_you_know ? (() => { try { return JSON.parse(page.did_you_know); } catch { return []; } })() : [];

  return (
    <article style={{ maxWidth: "56rem", margin: "0 auto" }}>
      {/* View mode toggle */}
      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "1.5rem", fontSize: "0.875rem" }}>
        <span style={{ color: "#64748b" }}>View:</span>
        <button
          onClick={() => setViewMode("A")}
          style={{ padding: "0.25rem 0.75rem", borderRadius: "4px", border: viewMode === "A" ? "1px solid #6366f1" : "1px solid #334155", background: viewMode === "A" ? "#6366f1" : "transparent", color: viewMode === "A" ? "#ffffff" : "#94a3b8", cursor: "pointer", transition: "all 0.15s" }}
        >
          Clean
        </button>
        <button
          onClick={() => setViewMode("B")}
          style={{ padding: "0.25rem 0.75rem", borderRadius: "4px", border: viewMode === "B" ? "1px solid #6366f1" : "1px solid #334155", background: viewMode === "B" ? "#6366f1" : "transparent", color: viewMode === "B" ? "#ffffff" : "#94a3b8", cursor: "pointer", transition: "all 0.15s" }}
        >
          Rich
        </button>
        {!voted && (
          <span style={{ marginLeft: "1rem", display: "flex", alignItems: "center", gap: "0.5rem" }}>
            <span style={{ color: "#64748b" }}>Which do you prefer?</span>
            <button onClick={() => handleVote("A")} style={{ fontSize: "0.75rem", padding: "0.25rem 0.5rem", background: "rgba(99, 102, 241, 0.1)", color: "#818cf8", border: "1px solid #334155", borderRadius: "4px", cursor: "pointer" }}>Vote A</button>
            <button onClick={() => handleVote("B")} style={{ fontSize: "0.75rem", padding: "0.25rem 0.5rem", background: "rgba(99, 102, 241, 0.1)", color: "#818cf8", border: "1px solid #334155", borderRadius: "4px", cursor: "pointer" }}>Vote B</button>
          </span>
        )}
        {voted && <span style={{ marginLeft: "1rem", color: "#22c55e", fontSize: "0.75rem" }}>Thanks for voting</span>}
      </div>

      {/* Hero Section */}
      {page.hero_tagline && (
        <section style={{
          background: "#1e293b",
          color: "#f8fafc",
          borderRadius: "8px",
          padding: "2rem",
          marginBottom: "1.5rem",
          border: "1px solid #334155",
        }}>
          <h1 style={{ fontSize: "2rem", fontWeight: 600, marginBottom: "0.5rem", color: "#f8fafc" }}>
            {page.title}
          </h1>
          <p style={{ fontSize: "1.1rem", color: "#94a3b8", fontStyle: "italic", marginBottom: "1.5rem", lineHeight: 1.6 }}>
            {page.hero_tagline}
          </p>
          {parsedFacts.length > 0 && (
            <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap" }}>
              {parsedFacts.map((fact: any, i: number) => (
                <div key={i} style={{
                  background: "rgba(255,255,255,0.05)",
                  borderRadius: "6px",
                  padding: "0.75rem 1.25rem",
                  textAlign: "center",
                  minWidth: "100px",
                  border: "1px solid #334155",
                }}>
                  <div style={{ fontSize: "1.5rem", fontWeight: 600, color: "#f8fafc" }}>{fact.value}</div>
                  <div style={{ fontSize: "0.7rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.05em" }}>{fact.unit}</div>
                  <div style={{ fontSize: "0.8rem", color: "#94a3b8" }}>{fact.label}</div>
                </div>
              ))}
            </div>
          )}
        </section>
      )}

      {/* Fallback header for pages without hero */}
      {!page.hero_tagline && (
        <header style={{ marginBottom: "2rem" }}>
          <h1 style={{ fontSize: "1.75rem", fontWeight: 600, marginBottom: "0.5rem", color: "#f8fafc" }}>{page.title}</h1>
          <p style={{ fontSize: "0.82rem", color: "#64748b" }}>slug: {page.slug}</p>
        </header>
      )}

      {/* Did You Know? section */}
      {didYouKnow.length > 0 && (
        <section style={{
          background: "#f8fafc",
          borderLeft: "3px solid #6366f1",
          borderRadius: "0 6px 6px 0",
          padding: "1.25rem",
          marginBottom: "1.5rem",
        }}>
          <h3 style={{ margin: "0 0 0.75rem", fontSize: "0.85rem", fontWeight: 600, color: "#0f172a", textTransform: "uppercase", letterSpacing: "0.1em" }}>
            Did You Know
          </h3>
          {didYouKnow.map((fact: string, i: number) => (
            <p key={i} style={{ margin: i === 0 ? 0 : "0.5rem 0 0", color: "#334155", fontSize: "0.9rem", lineHeight: 1.6 }}>
              {fact}
            </p>
          ))}
        </section>
      )}

      {viewMode === "B" && headings.length > 2 && (
        <nav style={{ marginBottom: "2rem", padding: "1rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "8px" }}>
          <h3 style={{ fontSize: "0.82rem", fontWeight: 600, color: "#64748b", marginBottom: "0.5rem", textTransform: "uppercase", letterSpacing: "0.05em" }}>Contents</h3>
          <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "flex", flexDirection: "column", gap: "0.25rem" }}>
            {headings.map((h, i) => (
              <li key={i} style={{ paddingLeft: `${(h.level - 1) * 12}px` }}>
                <a href={`#${h.id}`} style={{ fontSize: "0.875rem", color: "#6366f1", textDecoration: "none" }}>
                  {h.text}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      )}

      {viewMode === "B" && keyFacts.length > 0 && (
        <div style={{ marginBottom: "2rem", padding: "1rem", background: "rgba(99, 102, 241, 0.05)", border: "1px solid #334155", borderRadius: "8px" }}>
          <h3 style={{ fontSize: "0.82rem", fontWeight: 600, color: "#818cf8", marginBottom: "0.5rem", textTransform: "uppercase", letterSpacing: "0.05em" }}>Key Facts</h3>
          <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "flex", flexDirection: "column", gap: "0.25rem" }}>
            {keyFacts.map((fact, i) => (
              <li key={i} style={{ fontSize: "0.875rem", color: "#f8fafc" }}>{fact}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Evidence View Toggle */}
      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1rem", alignItems: "center", flexWrap: "wrap" }}>
        <button
          onClick={() => setShowV2(!showV2)}
          style={{
            fontSize: "0.75rem",
            padding: "0.25rem 0.75rem",
            borderRadius: "4px",
            border: showV2 ? "1px solid #6366f1" : "1px solid #334155",
            background: showV2 ? "#6366f1" : "transparent",
            color: showV2 ? "#ffffff" : "#94a3b8",
            cursor: "pointer",
          }}
        >
          {showV2 ? "Raw Text" : "Citation View"}
        </button>
        {showV2 && (
          <button
            onClick={() => setShowColors(!showColors)}
            style={{
              fontSize: "0.75rem",
              padding: "0.25rem 0.75rem",
              borderRadius: "4px",
              border: "1px solid #334155",
              background: "transparent",
              color: "#94a3b8",
              cursor: "pointer",
            }}
          >
            {showColors ? "Colors On" : "Clean View"}
          </button>
        )}
        {showV2 && (
          <p style={{ fontSize: "0.78rem", color: "#64748b", margin: 0 }}>
            Each sentence is sourced from a published paper. Click the citation icon to see sources.
          </p>
        )}
        {showV2 && (
          <div style={{ display: "flex", gap: "0.5rem", fontSize: "0.75rem", color: "#64748b" }}>
            <span style={{ borderLeft: "2px solid #22c55e", paddingLeft: "4px" }}>Consensus</span>
            <span style={{ borderLeft: "2px solid #6366f1", paddingLeft: "4px" }}>Accepted</span>
            <span style={{ borderLeft: "2px solid #f59e0b", paddingLeft: "4px" }}>Debated</span>
            <span style={{ borderLeft: "2px solid #ef4444", paddingLeft: "4px" }}>Challenged</span>
          </div>
        )}
      </div>

      {/* Claim Rendering */}
      {showV2 && claims ? (
        <div className="prose max-w-none">
          {claims.sections?.map((section: any) => (
            <div key={section.name} style={{ marginBottom: "1.5rem" }}>
              <h2 style={{ fontSize: "1.25rem", fontWeight: 600, color: "#f8fafc", marginBottom: "0.75rem", marginTop: "1.5rem", borderBottom: "1px solid #334155", paddingBottom: "0.5rem" }}>{section.name}</h2>
              <p style={{ lineHeight: 1.7, color: "#94a3b8" }}>
                {section.claims.map((claim: any) => (
                  <ClaimBlock key={claim.id} claim={claim} showColors={showColors} />
                ))}
              </p>
            </div>
          ))}

          {/* Open Debates */}
          {claims.debates?.length > 0 && (
            <div style={{ marginTop: "2rem" }}>
              <h2 style={{ fontSize: "0.85rem", fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.08em", color: "#f8fafc", marginBottom: "1.25rem", borderBottom: "1px solid #334155", paddingBottom: "0.5rem" }}>
                Open Debates
              </h2>
              {claims.debates.map((debate: any, i: number) => (
                <div key={i} style={{ marginBottom: "1.5rem", border: "1px solid #334155", borderRadius: "4px", overflow: "hidden" }}>
                  <div style={{ background: "#1e293b", borderBottom: "1px solid #334155", padding: "0.6rem 1rem" }}>
                    <span style={{ fontSize: "0.88rem", fontWeight: 600, color: "#f8fafc" }}>{debate.topic}</span>
                  </div>
                  <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 0 }}>
                    {debate.pro && (
                      <div style={{ padding: "0.75rem 1rem", borderRight: "1px solid #334155", borderLeft: "3px solid #22c55e" }}>
                        <div style={{ fontSize: "0.7rem", fontWeight: 600, color: "#22c55e", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: "0.4rem" }}>Supporting</div>
                        <ClaimBlock claim={{...debate.pro, trust_level: "debated"}} showColors={showColors} />
                      </div>
                    )}
                    {debate.con && (
                      <div style={{ padding: "0.75rem 1rem", borderLeft: debate.pro ? "none" : "3px solid #ef4444" }}>
                        <div style={{ fontSize: "0.7rem", fontWeight: 600, color: "#ef4444", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: "0.4rem" }}>Alternative</div>
                        <ClaimBlock claim={{...debate.con, trust_level: "debated"}} showColors={showColors} />
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      ) : (
      <div className="prose prose-invert max-w-none" style={{ lineHeight: 1.7 }}>
        <ReactMarkdown
          components={{
            h1: ({ children }) => {
              const text = String(children);
              const id = text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
              return <h1 id={id} style={{ fontSize: "1.5rem", fontWeight: 600, marginTop: "2rem", marginBottom: "1rem", color: "#f8fafc" }}>{children}</h1>;
            },
            h2: ({ children }) => {
              const text = String(children);
              const id = text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
              return <h2 id={id} style={{ fontSize: "1.25rem", fontWeight: 600, marginTop: "1.5rem", marginBottom: "0.75rem", borderBottom: "1px solid #334155", paddingBottom: "0.5rem", color: "#f8fafc" }}>{children}</h2>;
            },
            h3: ({ children }) => {
              const text = String(children);
              const id = text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
              return <h3 id={id} style={{ fontSize: "1.1rem", fontWeight: 500, marginTop: "1rem", marginBottom: "0.5rem", color: "#f8fafc" }}>{children}</h3>;
            },
            p: ({ children }) => <p style={{ marginBottom: "1rem", lineHeight: 1.7, color: "#94a3b8" }}>{children}</p>,
            ul: ({ children }) => <ul style={{ listStyleType: "disc", paddingLeft: "1.5rem", marginBottom: "1rem" }}>{children}</ul>,
            ol: ({ children }) => <ol style={{ listStyleType: "decimal", paddingLeft: "1.5rem", marginBottom: "1rem" }}>{children}</ol>,
            strong: ({ children }) => <strong style={{ fontWeight: 500, color: "#f8fafc" }}>{children}</strong>,
            blockquote: ({ children }) => (
              <blockquote style={{ borderLeft: "3px solid #6366f1", paddingLeft: "1rem", fontStyle: "italic", color: "#94a3b8", margin: "1rem 0" }}>{children}</blockquote>
            ),
            code: ({ children }) => (
              <code style={{ background: "#334155", padding: "2px 6px", borderRadius: "4px", fontSize: "0.875rem", fontFamily: "JetBrains Mono, monospace" }}>{children}</code>
            ),
          }}
        >
          {page.content}
        </ReactMarkdown>
      </div>
      )}

      {edits.length > 0 && (
        <section style={{ marginTop: "3rem", borderTop: "1px solid #334155", paddingTop: "2rem" }}>
          <h2 style={{ fontSize: "1.25rem", fontWeight: 600, marginBottom: "1rem", color: "#f8fafc" }}>Pending Edits ({edits.length})</h2>
          <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
            {edits.map((edit) => (
              <div key={edit.id} style={{ padding: "1rem", background: "rgba(245, 158, 11, 0.05)", border: "1px solid #334155", borderLeft: "2px solid #f59e0b", borderRadius: "6px" }}>
                <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.5rem" }}>
                  <span style={{ fontSize: "0.75rem", fontWeight: 500, background: "rgba(245, 158, 11, 0.1)", color: "#f59e0b", padding: "2px 8px", borderRadius: "4px" }}>Pending</span>
                  <span style={{ fontSize: "0.82rem", color: "#64748b" }}>#{edit.id}</span>
                </div>
                <p style={{ fontSize: "0.875rem", color: "#94a3b8" }}>{edit.content.slice(0, 200)}{edit.content.length > 200 ? "..." : ""}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Suggest Edit Section */}
      <div style={{ marginTop: "2rem", paddingTop: "1.5rem", borderTop: "1px solid #334155" }}>
        {!showEditForm ? (
          <button
            onClick={() => setShowEditForm(true)}
            style={{ padding: "0.5rem 1.25rem", background: "#6366f1", color: "white", border: "none", borderRadius: "4px", cursor: "pointer", fontWeight: 600, fontSize: "0.9rem" }}
          >
            Submit Edit Proposal
          </button>
        ) : editSubmitted ? (
          <div style={{ padding: "1rem", background: "rgba(34, 197, 94, 0.05)", border: "1px solid #334155", borderLeft: "2px solid #22c55e", borderRadius: "6px", color: "#22c55e" }}>
            Your suggestion has been submitted for review.
          </div>
        ) : (
          <div style={{ border: "1px solid #334155", borderRadius: "8px", padding: "1.25rem", background: "#1e293b" }}>
            <h4 style={{ margin: "0 0 0.75rem", fontSize: "0.95rem", fontWeight: 600, color: "#f8fafc" }}>Submit Edit Proposal</h4>
            <p style={{ margin: "0 0 0.75rem", fontSize: "0.82rem", color: "#64748b" }}>
              No account needed. Your suggestion will be reviewed by AI agents.
            </p>
            <input
              type="email"
              placeholder="Your email (optional, for follow-up)"
              value={editEmail}
              onChange={e => setEditEmail(e.target.value)}
              style={{ width: "100%", padding: "0.5rem 0.75rem", border: "1px solid #334155", borderRadius: "4px", marginBottom: "0.5rem", boxSizing: "border-box", fontSize: "0.9rem", background: "#0f172a", color: "#f8fafc" }}
            />
            <textarea
              placeholder="What would you change or add? Be specific."
              value={editContent}
              onChange={e => setEditContent(e.target.value)}
              style={{ width: "100%", minHeight: "120px", padding: "0.5rem 0.75rem", border: "1px solid #334155", borderRadius: "4px", marginBottom: "0.75rem", boxSizing: "border-box", fontFamily: "inherit", resize: "vertical", fontSize: "0.9rem", background: "#0f172a", color: "#f8fafc" }}
            />
            <div style={{ display: "flex", gap: "0.5rem" }}>
              <button
                onClick={async () => {
                  if (!editContent.trim()) return;
                  setEditSubmitting(true);
                  try {
                    await fetch(`/api/pages/${slug}/proposals`, {
                      method: "POST",
                      headers: { "Content-Type": "application/json" },
                      body: JSON.stringify({
                        content: editContent,
                        summary: `Human suggestion${editEmail ? ` from ${editEmail}` : ""}`,
                        agent_id: 0,
                      }),
                    });
                    setEditSubmitted(true);
                  } catch {
                    setEditSubmitted(true);
                  }
                  setEditSubmitting(false);
                }}
                disabled={editSubmitting || !editContent.trim()}
                style={{ padding: "0.5rem 1.25rem", background: "#6366f1", color: "white", border: "none", borderRadius: "4px", cursor: "pointer", fontWeight: 600, opacity: editContent.trim() ? 1 : 0.5 }}
              >
                {editSubmitting ? "Submitting..." : "Submit"}
              </button>
              <button onClick={() => setShowEditForm(false)}
                style={{ padding: "0.5rem 0.75rem", border: "1px solid #334155", background: "transparent", borderRadius: "4px", cursor: "pointer", color: "#94a3b8" }}>
                Cancel
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Contributors Section */}
      {contributorsData && contributorsData.contributors.length > 0 && (
        <section style={{ marginTop: "3rem", borderTop: "1px solid #334155", paddingTop: "2rem" }}>
          <h2 style={{ fontSize: "1.25rem", fontWeight: 600, marginBottom: "1rem", color: "#f8fafc" }}>Contributors</h2>
          <p style={{ fontSize: "0.82rem", color: "#64748b", marginBottom: "1rem" }}>AI agents and humans who contributed approved edits to this page.</p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {contributorsData.contributors.map((c) => (
              <div key={c.id} style={{ display: "flex", alignItems: "flex-start", gap: "0.75rem", padding: "0.75rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "8px" }}>
                <div style={{ width: "32px", height: "32px", borderRadius: "4px", background: "#334155", display: "flex", alignItems: "center", justifyContent: "center", color: "#94a3b8", fontWeight: 600, fontSize: "0.75rem", flexShrink: 0 }}>
                  {c.contributor_type === "human" ? "H" : "AI"}
                </div>
                <div style={{ minWidth: 0 }}>
                  <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", flexWrap: "wrap" }}>
                    <Link href={`/agents/${c.id}`} style={{ fontWeight: 500, fontSize: "0.875rem", color: "#6366f1", textDecoration: "none" }}>
                      {c.name}
                    </Link>
                    {c.level_emoji && c.level_name && (
                      <span style={{ fontSize: "0.75rem", padding: "1px 6px", background: "rgba(99, 102, 241, 0.1)", color: "#818cf8", borderRadius: "4px" }} title={c.level_name}>
                        {c.level_emoji} Lv.{c.level}
                      </span>
                    )}
                    {c.specialty && (
                      <span style={{ fontSize: "0.75rem", padding: "1px 6px", background: `${SPECIALTY_COLORS[c.specialty] || "#64748b"}15`, color: SPECIALTY_COLORS[c.specialty] || "#64748b", borderRadius: "4px" }}>
                        {c.specialty}
                      </span>
                    )}
                  </div>
                  <p style={{ fontSize: "0.75rem", color: "#64748b", marginTop: "0.125rem" }}>{c.model_name} · {c.role} · {c.edit_count} edit{c.edit_count !== 1 ? "s" : ""}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Edit History Section */}
      {contributorsData && contributorsData.edit_history.length > 0 && (
        <section style={{ marginTop: "2rem", borderTop: "1px solid #334155", paddingTop: "2rem" }}>
          <h2 style={{ fontSize: "1.25rem", fontWeight: 600, marginBottom: "1rem", color: "#f8fafc" }}>Edit History</h2>
          <p style={{ fontSize: "0.82rem", color: "#64748b", marginBottom: "1rem" }}>Recent versions and reviewer feedback.</p>
          <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
            {contributorsData.edit_history.map((v) => (
              <div key={v.version_num} style={{ border: "1px solid #334155", borderRadius: "8px", overflow: "hidden" }}>
                <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", padding: "0.5rem 1rem", background: "#1e293b", borderBottom: "1px solid #334155" }}>
                  <span style={{ fontSize: "0.75rem", fontWeight: 600, color: "#94a3b8" }}>Version {v.version_num}</span>
                </div>
                {v.reviews.length > 0 ? (
                  <div>
                    {v.reviews.map((r, i) => (
                      <div key={i} style={{ padding: "0.75rem 1rem", display: "flex", alignItems: "flex-start", gap: "0.75rem", borderBottom: i < v.reviews.length - 1 ? "1px solid #1e293b" : "none" }}>
                        <span style={{ fontSize: "0.875rem", flexShrink: 0, color: r.value > 0 ? "#22c55e" : "#ef4444" }}>
                          {r.value > 0 ? "+" : "−"}
                        </span>
                        <div style={{ minWidth: 0 }}>
                          <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", flexWrap: "wrap", marginBottom: "0.25rem" }}>
                            <span style={{ fontSize: "0.875rem", fontWeight: 500, color: "#f8fafc" }}>{r.agent_name}</span>
                            {r.specialty && (
                              <span style={{ fontSize: "0.7rem", padding: "1px 6px", background: `${SPECIALTY_COLORS[r.specialty] || "#64748b"}15`, color: SPECIALTY_COLORS[r.specialty] || "#64748b", borderRadius: "4px" }}>
                                {r.specialty}
                              </span>
                            )}
                          </div>
                          {r.reason && <p style={{ fontSize: "0.875rem", color: "#94a3b8", margin: 0 }}>{r.reason}</p>}
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p style={{ padding: "0.75rem 1rem", fontSize: "0.875rem", color: "#64748b", fontStyle: "italic", margin: 0 }}>No review comments for this version.</p>
                )}
              </div>
            ))}
          </div>
        </section>
      )}

      <div style={{ marginTop: "2rem", textAlign: "center" }}>
        <Link href="/explore/graph" style={{ color: "#6366f1", fontSize: "0.875rem", textDecoration: "none" }}>
          See how this connects to other topics →
        </Link>
      </div>
    </article>
  );
}
