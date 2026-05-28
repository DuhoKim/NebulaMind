"use client";

import { useEffect, useMemo, useState } from "react";
import { useParams } from "next/navigation";
import ReactMarkdown from "react-markdown";
import rehypeRaw from "rehype-raw";
import Link from "next/link";
import ClaimBlock from "./ClaimBlock";
import TOCSidebar from "./TOCSidebar";
import ProvenanceChip from "./ProvenanceChip";

interface WikiPage {
  id: number;
  title: string;
  slug: string;
  content: string;
  hero_tagline?: string | null;
  hero_facts?: string | null;
  editor_agent_tier?: string | null;
  synthesized_date?: string | null;
  version_num?: number | null;
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

const TRUST_COLORS: Record<string, string> = {
  consensus: "#22c55e",
  accepted: "#6366f1",
  debated: "#f97316",
  challenged: "#ef4444",
  unverified: "#64748b",
};

const SPECIALTY_COLORS: Record<string, string> = {
  observational: "#3b82f6",
  theoretical: "#a855f7",
  computational: "#22c55e",
  cosmology: "#6366f1",
  stellar: "#eab308",
  galactic: "#ec4899",
};

const GAP_TYPE_COLORS: Record<string, { bg: string; text: string }> = {
  gap:      { bg: "rgba(239,68,68,0.15)",   text: "#f87171" },
  tension:  { bg: "rgba(245,158,11,0.15)",  text: "#fbbf24" },
  bridge:   { bg: "rgba(16,185,129,0.15)",  text: "#34d399" },
  frontier: { bg: "rgba(99,102,241,0.15)",  text: "#818cf8" },
  synergy:  { bg: "rgba(14,165,233,0.15)",  text: "#38bdf8" },
};

function slugify(text: string): string {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

function unwrapCodeFence(content: string): string {
  const trimmed = content.trim();
  const m = trimmed.match(/^```(?:markdown|md)?\s*\n([\s\S]*?)\n```\s*$/);
  return m ? m[1].trim() : trimmed;
}

function wrapClaimComments(content: string): string {
  return content.replace(
    /<!--\s*claim:(\d+)\s*-->([\s\S]*?)<!--\s*\/claim:\1\s*-->/g,
    (_, id, body) => {
      const safe = body.replace(/</g, '&lt;').replace(/>/g, '&gt;');
      return `<span data-claim-id="${id}" id="claim-${id}">${safe}</span>`;
    }
  );
}

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
        id: slugify(text),
      });
    }
  }
  return headings;
}

function stripMarkdown(text: string): string {
  return text
    .replace(/\*\*(.+?)\*\*/g, "$1")   // bold
    .replace(/\*(.+?)\*/g, "$1")         // italic
    .replace(/`(.+?)`/g, "$1")           // inline code
    .replace(/\[(.+?)\]\(.+?\)/g, "$1") // links
    .replace(/^#+\s/gm, "")             // headings
    .replace(/^[-*]\s/gm, "")           // bullets
    .trim();
}


function renderSourceBadge(src: any): React.ReactNode {
  if (!src) return <span style={{fontSize:"0.58rem",color:"#475569"}}>⚠️ AI estimate</span>;
  if (src.tier === "authoritative") return (
    <a href={src.reference_url || "#"} target="_blank" rel="noopener noreferrer"
      style={{fontSize:"0.58rem",color:"#818cf8",textDecoration:"none"}} title={src.reference_title}>
      📐 {src.attribution}
    </a>
  );
  if (src.tier === "claim") {
    const tc = src.trust_level === "consensus" ? "#22c55e" : src.trust_level === "debated" ? "#f97316" : "#94a3b8";
    return <span style={{fontSize:"0.58rem",color:tc}} title={`${src.evidence_count} cited papers`}>📄 {src.evidence_count} sources · {src.trust_level}</span>;
  }
  if (src.flagged) return <span style={{fontSize:"0.58rem",color:"#ef4444"}}>🚩 {src.reason || "Flagged"}</span>;
  return <span style={{fontSize:"0.58rem",color:"#f59e0b"}}>⚠️ AI estimate</span>;
}

function superscript(n: number): string {
  const map: Record<string, string> = {
    "0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹","-":"⁻",
  };
  return String(n).split("").map(c => map[c] || c).join("");
}

function renderFactValue(fact: any): string {
  switch (fact?.kind ?? "scalar") {
    case "range": {
      if (fact.scale === "log" && fact.value_min != null && fact.value_max != null) {
        const lo = Math.log10(fact.value_min);
        const hi = Math.log10(fact.value_max);
        return `10${superscript(Math.round(lo))} – 10${superscript(Math.round(hi))}`;
      }
      return `${fact.value_min} – ${fact.value_max}`;
    }
    case "count":
      return `${fact.modifier === "approximately" ? "~" : ""}${Number(fact.value).toLocaleString()}`;
    case "date":
      return String(fact.year ?? fact.value ?? "");
    default:
      return String(fact.value ?? "");
  }
}

function ClaimAnnotatedSpan({
  claim,
  showColors,
  ideas,
  children,
}: {
  claim: any;
  showColors: boolean;
  ideas?: any[];
  children: React.ReactNode;
}) {
  const [open, setOpen] = useState(false);
  const [ideasOpen, setIdeasOpen] = useState(false);
  const trustLevel = claim?.trust_level ?? "unverified";
  const trustColor = TRUST_COLORS[trustLevel] ?? "#64748b";
  const evidenceCount = claim?.evidence_count ?? 0;
  const isContested = ["debated", "challenged"].includes(trustLevel) || (claim?.con_count ?? 0) >= 2;

  useEffect(() => {
    if (!open && !ideasOpen) return;
    const close = () => { setOpen(false); setIdeasOpen(false); };
    document.addEventListener("click", close);
    return () => document.removeEventListener("click", close);
  }, [open, ideasOpen]);

  if (!showColors) return <span>{children}</span>;

  return (
    <span style={{ position: "relative", display: "inline" }}>
      <span
        style={{ borderBottom: `1px dotted ${trustColor}`, cursor: "pointer" }}
        title={`${trustLevel} · ${evidenceCount} source${evidenceCount !== 1 ? "s" : ""}`}
        onClick={(e) => { e.stopPropagation(); setOpen((v) => !v); }}
      >{children}</span>
      {ideas && ideas.length > 0 && (
        <button
          onClick={(e) => { e.stopPropagation(); setIdeasOpen((v) => !v); }}
          style={{
            display: "inline",
            background: "none",
            border: "none",
            cursor: "pointer",
            fontSize: "0.72rem",
            padding: "0 2px",
            ...(isContested
              ? { color: "#fbbf24", fontWeight: 700 }
              : { color: "#818cf8", fontWeight: 400, opacity: 0.6 }),
          }}
          title={isContested
            ? `⚡ ${ideas.length} open research question${ideas.length > 1 ? "s" : ""} — this claim is actively debated`
            : `${ideas.length} research idea${ideas.length > 1 ? "s" : ""} linked to this claim`}
        >
          {isContested ? "⚡" : "💡"} {ideas.length}
        </button>
      )}
      {open && (
        <span
          onClick={(e) => e.stopPropagation()}
          style={{
            position: "absolute",
            top: "1.5em",
            left: 0,
            zIndex: 100,
            background: "#1e293b",
            border: "1px solid #334155",
            borderLeft: `3px solid ${trustColor}`,
            borderRadius: "6px",
            padding: "0.6rem 0.8rem",
            minWidth: "180px",
            maxWidth: "280px",
            fontSize: "0.78rem",
            color: "#94a3b8",
            boxShadow: "0 4px 16px rgba(0,0,0,0.5)",
            display: "block",
            whiteSpace: "normal",
          }}
        >
          <div style={{ fontWeight: 600, color: "#f8fafc", marginBottom: "0.3rem", textTransform: "capitalize" }}>
            {trustLevel}
          </div>
          {evidenceCount > 0 && (
            <div>📄 {evidenceCount} source{evidenceCount !== 1 ? "s" : ""}</div>
          )}
        </span>
      )}
      {ideasOpen && ideas && ideas.length > 0 && (
        <span
          onClick={(e) => e.stopPropagation()}
          style={{
            position: "absolute",
            left: 0,
            top: "1.5em",
            zIndex: 110,
            background: "#1e293b",
            border: "1px solid #4f46e5",
            borderRadius: "8px",
            boxShadow: "0 8px 24px rgba(0,0,0,0.4)",
            padding: "0.75rem",
            width: "min(28rem, 92vw)",
            display: "block",
            whiteSpace: "normal",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "0.5rem" }}>
            <span style={{ color: isContested ? "#fbbf24" : "#818cf8", fontWeight: 600, fontSize: "0.8rem" }}>
              {isContested ? "⚡ Open Research Questions" : "💡 Research Ideas"}
            </span>
            <button
              onClick={(e) => { e.stopPropagation(); setIdeasOpen(false); }}
              style={{ background: "none", border: "none", color: "#64748b", cursor: "pointer" }}
            >&#x2715;</button>
          </div>
          {ideas.map((idea: any) => (
            <div key={idea.id} style={{ border: "1px solid #334155", borderRadius: "6px", padding: "0.6rem 0.75rem", marginBottom: "0.4rem", background: "#0f172a" }}>
              {idea.gap_type && (
                <span style={{
                  display: "inline-block",
                  fontSize: "0.65rem",
                  fontWeight: 600,
                  textTransform: "uppercase",
                  letterSpacing: "0.06em",
                  padding: "1px 6px",
                  borderRadius: "99px",
                  marginBottom: "0.3rem",
                  background: GAP_TYPE_COLORS[idea.gap_type]?.bg ?? "rgba(100,116,139,0.15)",
                  color: GAP_TYPE_COLORS[idea.gap_type]?.text ?? "#94a3b8",
                }}>
                  {idea.gap_type}
                </span>
              )}
              <p style={{ margin: 0, fontSize: "0.82rem", color: "#f8fafc", lineHeight: 1.5 }}>{idea.question}</p>
            </div>
          ))}
        </span>
      )}
    </span>
  );
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
  const [isMobile, setIsMobile] = useState(false);

  const [health, setHealth] = useState<{score:number;band:string;emoji:string} | null>(null);
  const [claimIdeasMap, setClaimIdeasMap] = useState<Record<number, any[]>>({});
  const [ideasOpen, setIdeasOpen] = useState(false);

  useEffect(() => {
    const check = () => setIsMobile(window.innerWidth < 768);
    check();
    window.addEventListener("resize", check);
    return () => window.removeEventListener("resize", check);
  }, []);

  useEffect(() => {
    if (!slug) return;
    fetch(`/api/pages/${slug}/health`)
      .then(r => r.ok ? r.json() : null)
      .then(d => { if (d?.score != null) setHealth(d); })
      .catch(() => {});
  }, [slug]);

  useEffect(() => {
    if (!slug) return;
    fetch(`/api/pages/${slug}`)
      .then(r => r.ok ? r.json() : null)
      .then(p => {
        setPage(p);
        setLoading(false);
        if (p?.id) {
          fetch(`/api/edits?status=pending&page_id=${p.id}`)
            .then(r => r.ok ? r.json() : [])
            .then(setEdits)
            .catch(() => setEdits([]));
        }
        fetch(`/api/pages/${slug}/contributors`)
          .then(r => r.ok ? r.json() : null)
          .then(setContributorsData)
          .catch(() => setContributorsData(null));
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

  useEffect(() => {
    if (!slug) return;
    fetch(`/api/pages/${slug}/ideas?per_page=100`)
      .then(r => r.json())
      .then(data => {
        const map: Record<number, any[]> = {};
        for (const idea of data.ideas || []) {
          if (idea.claim_id) {
            if (!map[idea.claim_id]) map[idea.claim_id] = [];
            map[idea.claim_id].push(idea);
          }
        }
        setClaimIdeasMap(map);
      })
      .catch(() => {});
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

  const claimById = useMemo(() => {
    const map: Record<number, any> = {};
    for (const section of claims?.sections ?? []) {
      for (const claim of section.claims ?? []) {
        map[claim.id] = claim;
      }
    }
    return map;
  }, [claims]);

  if (loading) return <p style={{ color: "#64748b" }}>Loading...</p>;
  if (!page) return <p style={{ color: "#94a3b8" }}>Page not found.</p>;

  const headings = extractHeadings(page.content);
  const parsedFacts = page.hero_facts ? (() => { try { return JSON.parse(page.hero_facts); } catch { return []; } })() : [];
  // H6: filter out flagged AI-estimate facts (failed validation)
  const displayFacts = parsedFacts.filter((f: any) => !(f?.source?.tier === "ai_estimate" && f?.source?.flagged));
  const processedContent = wrapClaimComments(unwrapCodeFence(page.content));

  return (
    <article
      style={
        isMobile
          ? { maxWidth: "56rem", margin: "0 auto" }
          : {
              display: "grid",
              gridTemplateColumns: "minmax(0, 56rem) 240px",
              gap: "2rem",
              maxWidth: "64rem",
              margin: "0 auto",
              alignItems: "start",
            }
      }
    >
      <div>
      {/* View mode toggle */}
      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "1.5rem", fontSize: "0.875rem", flexWrap: "wrap" }}>
        {health && (
          <span
            title={`Health: ${health.score}/100 — ${health.band}`}
            style={{
              fontSize: "0.72rem", fontWeight: 600,
              padding: "0.15rem 0.5rem", borderRadius: "99px", cursor: "help",
              background: health.score >= 80 ? "rgba(34,197,94,0.15)"
                : health.score >= 60 ? "rgba(59,130,246,0.15)"
                : health.score >= 40 ? "rgba(234,179,8,0.15)"
                : health.score >= 20 ? "rgba(249,115,22,0.15)"
                : "rgba(239,68,68,0.15)",
              color: health.score >= 80 ? "#22c55e"
                : health.score >= 60 ? "#3b82f6"
                : health.score >= 40 ? "#ca8a04"
                : health.score >= 20 ? "#ea580c"
                : "#ef4444",
            }}
          >
            {health.emoji} {health.score}/100
          </span>
        )}
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
        <Link href={`/wiki/${slug}/history`}
          style={{ marginLeft: "auto", fontSize: "0.75rem", color: "#64748b", textDecoration: "none",
            padding: "0.25rem 0.5rem", border: "1px solid #334155", borderRadius: "4px" }}>
          📜 History
        </Link>
        <Link href={`/wiki/${slug}/sources`}
          style={{ fontSize: "0.75rem", color: "#64748b", textDecoration: "none",
            padding: "0.25rem 0.5rem", border: "1px solid #334155", borderRadius: "4px" }}>
          📚 Sources
        </Link>
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
          <h1 style={{ fontSize: "clamp(1.25rem, 4vw, 2rem)", fontWeight: 600, marginBottom: "0.5rem", color: "#f8fafc" }}>
            {page.title}
          </h1>
          <p style={{ fontSize: "1.1rem", color: "#94a3b8", fontStyle: "italic", marginBottom: "1.5rem", lineHeight: 1.6 }}>
            {page.hero_tagline}
          </p>
          {displayFacts.length > 0 && (
            <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap" }}>
              {displayFacts.map((fact: any, i: number) => (
                <div key={i} style={{
                  background: "rgba(255,255,255,0.05)",
                  borderRadius: "6px",
                  padding: "0.75rem 1.25rem",
                  textAlign: "center",
                  minWidth: "100px",
                  border: "1px solid #334155",
                  position: "relative",
                }}>
                  {/* H6 trust dot */}
                  {fact.trust_level && (
                    <span
                      title={`Source trust: ${fact.trust_level}`}
                      style={{
                        position: "absolute", top: "4px", right: "5px",
                        fontSize: "0.55rem",
                        color: fact.trust_level === "consensus" ? "#22c55e"
                          : fact.trust_level === "accepted" ? "#64748b"
                          : fact.trust_level === "debated" ? "#f97316"
                          : fact.trust_level === "challenged" ? "#ef4444"
                          : "#475569",
                      }}
                    >
                      {fact.trust_level === "consensus" ? "●" : fact.trust_level === "debated" ? "◖" : "◦"}
                    </span>
                  )}
                  <div style={{ fontSize: "1.5rem", fontWeight: 600, color: "#f8fafc" }}>{renderFactValue(fact)}</div>
                  <div style={{ fontSize: "0.7rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.05em" }}>{fact.unit}</div>
                  <div style={{ fontSize: "0.8rem", color: "#94a3b8" }}>{fact.label}</div>
                  <div style={{ marginTop: "0.3rem" }}>{renderSourceBadge(fact?.source)}</div>
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
          {/* ProvenanceChip for pages without hero */}
          <ProvenanceChip
            editorAgentTier={page.editor_agent_tier ?? undefined}
            synthesizedDate={page.synthesized_date ?? undefined}
            versionNum={page.version_num ?? undefined}
          />
        </header>
      )}

      {/* ProvenanceChip for pages with hero (placed after hero) */}
      {page.hero_tagline && (
        <ProvenanceChip
          editorAgentTier={page.editor_agent_tier ?? undefined}
          synthesizedDate={page.synthesized_date ?? undefined}
          versionNum={page.version_num ?? undefined}
        />
      )}

      {/* Mobile TOC: collapsed accordion above content */}
      {isMobile && (
        <TOCSidebar headings={headings} isMobile={true} />
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

      {/* Prose content — identical in both modes; Citation View adds inline claim badges */}
      <div className="prose max-w-none" style={{ lineHeight: 1.7, color: "#94a3b8" }}>
        <ReactMarkdown
          rehypePlugins={[rehypeRaw]}
          components={{
            h1: ({ children }) => {
              const text = String(children);
              const id = slugify(text);
              return <h1 id={id} style={{ fontSize: "1.5rem", fontWeight: 600, marginTop: "2rem", marginBottom: "1rem", color: "#f8fafc" }}>{children}</h1>;
            },
            h2: ({ children }) => {
              const text = String(children);
              const id = slugify(text);
              return <h2 id={id} style={{ fontSize: "1.25rem", fontWeight: 600, marginTop: "1.5rem", marginBottom: "0.75rem", borderBottom: "1px solid #334155", paddingBottom: "0.5rem", color: "#f8fafc" }}>{children}</h2>;
            },
            h3: ({ children }) => {
              const text = String(children);
              const id = slugify(text);
              return <h3 id={id} style={{ fontSize: "1.1rem", fontWeight: 500, marginTop: "1rem", marginBottom: "0.5rem", color: "#f8fafc" }}>{children}</h3>;
            },
            p: ({ children }) => <p style={{ marginBottom: "1rem", lineHeight: 1.7, color: "#94a3b8" }}>{children}</p>,
            ul: ({ children }) => <ul style={{ listStyleType: "disc", paddingLeft: "1.5rem", marginBottom: "1rem", color: "#94a3b8" }}>{children}</ul>,
            ol: ({ children }) => <ol style={{ listStyleType: "decimal", paddingLeft: "1.5rem", marginBottom: "1rem", color: "#94a3b8" }}>{children}</ol>,
            li: ({ children }) => <li style={{ marginBottom: "0.25rem", color: "#94a3b8" }}>{children}</li>,
            strong: ({ children }) => <strong style={{ fontWeight: 600, color: "#f8fafc" }}>{children}</strong>,
            blockquote: ({ children }) => (
              <blockquote style={{ borderLeft: "3px solid #6366f1", paddingLeft: "1rem", fontStyle: "italic", color: "#94a3b8", margin: "1rem 0" }}>{children}</blockquote>
            ),
            code: ({ children }) => (
              <code style={{ background: "#334155", padding: "2px 6px", borderRadius: "4px", fontSize: "0.875rem", fontFamily: "JetBrains Mono, monospace" }}>{children}</code>
            ),
            span: ({ node, children, ...props }: any) => {
              const claimId = props["data-claim-id"];
              if (claimId && showV2) {
                return (
                  <ClaimAnnotatedSpan
                    claim={claimById[Number(claimId)]}
                    showColors={showColors}
                    ideas={claimIdeasMap[Number(claimId)]}
                  >
                    {children}
                  </ClaimAnnotatedSpan>
                );
              }
              return <span {...props}>{children}</span>;
            },
          }}
        >
          {processedContent}
        </ReactMarkdown>
      </div>

      {/* Open Debates — only in Citation View; suppressed for flagship 671B pages (spec §5.3 / D12) */}
      {showV2 && !page.editor_agent_tier?.includes("671B") && claims?.debates?.length > 0 && (
        <div style={{ marginTop: "2rem" }}>
          <h2 style={{ fontSize: "0.85rem", fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.08em", color: "#f8fafc", marginBottom: "1.25rem", borderBottom: "1px solid #334155", paddingBottom: "0.5rem" }}>
            Open Debates
          </h2>
          {claims.debates.map((debate: any, i: number) => (
            <div key={i} style={{ marginBottom: "1.5rem", border: "1px solid #334155", borderRadius: "4px", overflow: "hidden" }}>
              <div style={{ background: "#1e293b", borderBottom: "1px solid #334155", padding: "0.6rem 1rem" }}>
                <span style={{ fontSize: "0.88rem", fontWeight: 600, color: "#f8fafc" }}>{debate.topic}</span>
              </div>
              <div style={{ display: "grid", gridTemplateColumns: isMobile ? "1fr" : "1fr 1fr", gap: 0 }}>
                {debate.pro && (
                  <div style={{ padding: "0.75rem 1rem", borderRight: "1px solid #334155", borderLeft: "3px solid #22c55e" }}>
                    <div style={{ fontSize: "0.7rem", fontWeight: 600, color: "#22c55e", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: "0.4rem" }}>Supporting</div>
                    <ClaimBlock claim={{...debate.pro, trust_level: "debated"}} showColors={showColors} ideas={claimIdeasMap[debate.pro?.id]} />
                  </div>
                )}
                {debate.con && (
                  <div style={{ padding: "0.75rem 1rem", borderLeft: debate.pro ? "none" : "3px solid #ef4444" }}>
                    <div style={{ fontSize: "0.7rem", fontWeight: 600, color: "#ef4444", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: "0.4rem" }}>Alternative</div>
                    <ClaimBlock claim={{...debate.con, trust_level: "debated"}} showColors={showColors} ideas={claimIdeasMap[debate.con?.id]} />
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Research Ideas — shown in both Citation View and Raw Text modes */}
      {(() => {
        const allIdeas = Object.values(claimIdeasMap).flat();
        if (allIdeas.length === 0) return null;
        const GAP_COLORS: Record<string, string> = {
          empirical: "#3b82f6",
          theoretical: "#a855f7",
          methodological: "#22c55e",
          observational: "#6366f1",
          computational: "#14b8a6",
        };
        return (
          <div style={{ marginTop: "2rem" }}>
            <button
              onClick={() => setIdeasOpen(v => !v)}
              style={{
                width: "100%",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                background: "transparent",
                border: "none",
                borderBottom: "1px solid #334155",
                paddingBottom: "0.5rem",
                marginBottom: ideasOpen ? "1rem" : 0,
                cursor: "pointer",
                textAlign: "left",
              }}
            >
              <span style={{ fontSize: "0.85rem", fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.08em", color: "#f8fafc" }}>
                Research Ideas ({allIdeas.length})
              </span>
              <span style={{ fontSize: "0.75rem", color: "#64748b" }}>{ideasOpen ? "▲" : "▼"}</span>
            </button>
            {ideasOpen && (
              <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
                {allIdeas.map((idea: any, i: number) => (
                  <div key={idea.id ?? i} style={{ padding: "0.85rem 1rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "6px", borderLeft: "3px solid #6366f1" }}>
                    {idea.gap_type && (
                      <span style={{
                        display: "inline-block",
                        fontSize: "0.65rem",
                        fontWeight: 600,
                        textTransform: "uppercase",
                        letterSpacing: "0.06em",
                        padding: "1px 7px",
                        borderRadius: "99px",
                        marginBottom: "0.45rem",
                        background: `${GAP_COLORS[idea.gap_type] ?? "#64748b"}22`,
                        color: GAP_COLORS[idea.gap_type] ?? "#94a3b8",
                        border: `1px solid ${GAP_COLORS[idea.gap_type] ?? "#334155"}55`,
                      }}>
                        {idea.gap_type}
                      </span>
                    )}
                    <p style={{ margin: 0, fontSize: "0.875rem", color: "#f8fafc", lineHeight: 1.6 }}>{idea.question}</p>
                    {idea.why_now && (
                      <p style={{ margin: "0.4rem 0 0", fontSize: "0.78rem", color: "#64748b", lineHeight: 1.5 }}>{idea.why_now}</p>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        );
      })()}

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
          <div style={{ display: "grid", gridTemplateColumns: isMobile ? "1fr" : "repeat(2, 1fr)", gap: "0.75rem" }}>
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
      </div>{/* end column 1 */}

      {/* Column 2: sticky TOC sidebar (desktop only) */}
      {!isMobile && (
        <TOCSidebar headings={headings} isMobile={false} />
      )}
    </article>
  );
}
