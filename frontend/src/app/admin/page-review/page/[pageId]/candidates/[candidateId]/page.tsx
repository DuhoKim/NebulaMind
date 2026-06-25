"use client";

import { useEffect, useMemo, useState } from "react";
import { useParams, useSearchParams } from "next/navigation";
import Link from "next/link";
import ReactMarkdown from "react-markdown";
import rehypeRaw from "rehype-raw";
import rehypeKatex from "rehype-katex";
import remarkMath from "remark-math";
import "katex/dist/katex.min.css";

type CheckStatus = "PASS" | "FAIL" | "CURRENT" | "STALE_PREIMAGE" | "NOT_REVIEWABLE" | string;

interface EvidenceRow {
  id: number;
  title: string;
  arxiv_id?: string | null;
  url?: string | null;
  summary?: string | null;
  stance?: string | null;
  relevance?: number | null;
  entailment?: number | null;
  rigor?: number | null;
  confidence?: number | null;
  quality_v2?: number | null;
}

interface EvidencePanel {
  claim_id: number;
  missing?: boolean;
  text?: string;
  trust_level?: string;
  trust_score?: number;
  section?: string;
  evidence: EvidenceRow[];
  total_elements?: number;
}

interface ReviewData {
  read_only: boolean;
  write_paths_reachable: boolean;
  route_guarantee: string;
  review_status: string;
  candidate: {
    id: string;
    page_id: number;
    label: string;
    artifact_ref: string;
    markdown: string;
    sha256: string;
    bytes: number;
    chars: number;
  };
  registry: Record<string, any>;
  checks: {
    missing_files: string[];
    candidate_hash: { status: CheckStatus; computed_sha256: string; expected_sha256: string };
    marker_bijection: { status: CheckStatus; ids?: number[]; open_ids?: number[]; expected_ids: number[]; extra_ids: number[]; missing_ids: number[] };
    forbidden_tokens: { status: CheckStatus; hits: Record<string, boolean> };
    canonicalizer: Record<string, any>;
    live_drift: Record<string, any>;
    apply_gate: { status: string; allowed_to_apply: boolean };
  };
  packet: {
    validation: Record<string, any>;
    traceability: { entries?: Array<Record<string, any>> };
    integration: { counts?: Record<string, number>; row_dispositions?: Array<Record<string, any>> };
    section_claim_map: Array<Record<string, string>>;
    coherence_guard_decisions: string;
  };
  traceability_summary: Record<string, number | null>;
  evidence_panels: EvidencePanel[];
}

const TRUST_COLORS: Record<string, string> = {
  consensus: "#22c55e",
  accepted: "#3b82f6",
  debated: "#f59e0b",
  challenged: "#ef4444",
  reported: "#14b8a6",
  unverified: "#64748b",
};

function statusColor(status: CheckStatus) {
  if (status === "PASS" || status === "CURRENT" || status === "REVIEWABLE" || status === "APPLIED" || status === "ALREADY_APPLIED") return "#22c55e";
  if (status === "STALE_PREIMAGE" || status === "NOT_FULLY_HARD_GATED") return "#f59e0b";
  return "#ef4444";
}

function Badge({ label, status }: { label: string; status: CheckStatus }) {
  const color = statusColor(status);
  return (
    <span style={{
      display: "inline-flex",
      alignItems: "center",
      gap: "0.35rem",
      border: `1px solid ${color}55`,
      background: `${color}18`,
      color,
      borderRadius: "999px",
      padding: "0.18rem 0.55rem",
      fontSize: "0.72rem",
      fontWeight: 700,
      whiteSpace: "nowrap",
    }}>
      {label}: {status}
    </span>
  );
}

function renderReviewMarkers(content: string) {
  return content.replace(
    /<!--\s*claim:(\d+)\s*-->([\s\S]*?)<!--\s*\/claim:\1\s*-->/g,
    (_match, id, body) => `<span data-claim-id="${id}">${body}</span>`
  );
}

function ClaimSpan({
  claimId,
  evidenceByClaim,
  children,
}: {
  claimId: number;
  evidenceByClaim: Record<number, EvidencePanel>;
  children: React.ReactNode;
}) {
  const panel = evidenceByClaim[claimId];
  const trust = panel?.trust_level || "unverified";
  const color = TRUST_COLORS[trust] || TRUST_COLORS.unverified;
  return (
    <span
      id={`claim-${claimId}`}
      title={`${claimId} · ${trust} · ${panel?.evidence?.length ?? 0} evidence rows`}
      style={{
        borderBottom: `2px solid ${color}`,
        background: `${color}18`,
        padding: "0 0.12rem",
        borderRadius: "2px",
      }}
    >
      {children}
      <a href={`#evidence-${claimId}`} style={{ color, fontWeight: 800, marginLeft: "0.25rem", textDecoration: "none" }}>
        [{claimId}]
      </a>
    </span>
  );
}

function Metric({ label, value }: { label: string; value: React.ReactNode }) {
  return (
    <div style={{ border: "1px solid #1e293b", background: "#0f172a", borderRadius: "6px", padding: "0.7rem 0.85rem" }}>
      <div style={{ fontSize: "0.68rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: "0.25rem" }}>{label}</div>
      <div style={{ color: "#e2e8f0", fontWeight: 700, fontSize: "0.9rem", overflowWrap: "anywhere" }}>{value}</div>
    </div>
  );
}

function EvidenceCard({ panel }: { panel: EvidencePanel }) {
  const color = TRUST_COLORS[panel.trust_level || ""] || TRUST_COLORS.unverified;
  return (
    <section id={`evidence-${panel.claim_id}`} style={{ border: "1px solid #1e293b", borderLeft: `3px solid ${color}`, borderRadius: "6px", background: "#0f172a", padding: "1rem", scrollMarginTop: "1rem" }}>
      <div style={{ display: "flex", justifyContent: "space-between", gap: "1rem", flexWrap: "wrap", marginBottom: "0.55rem" }}>
        <h3 style={{ color: "#f8fafc", margin: 0, fontSize: "0.95rem" }}>Claim {panel.claim_id}</h3>
        <span style={{ color, fontSize: "0.78rem", fontWeight: 800 }}>{panel.trust_level || "missing"}</span>
      </div>
      <p style={{ color: "#cbd5e1", margin: "0 0 0.8rem", lineHeight: 1.5 }}>{panel.text || "Claim row not found."}</p>
      {panel.evidence.length === 0 ? (
        <p style={{ color: "#64748b", margin: 0 }}>No evidence rows returned.</p>
      ) : (
        <div style={{ display: "grid", gap: "0.65rem" }}>
          {panel.evidence.map((row) => (
            <div key={row.id} style={{ borderTop: "1px solid #1e293b", paddingTop: "0.65rem" }}>
              <div style={{ display: "flex", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap" }}>
                {row.url ? (
                  <a href={row.url} target="_blank" rel="noopener noreferrer" style={{ color: "#93c5fd", fontWeight: 700, textDecoration: "none" }}>{row.title}</a>
                ) : (
                  <strong style={{ color: "#e2e8f0" }}>{row.title}</strong>
                )}
                <span style={{ color: "#94a3b8", fontSize: "0.75rem" }}>{row.stance || "stance unknown"} · evidence {row.id}</span>
              </div>
              {row.summary && <p style={{ color: "#94a3b8", margin: "0.35rem 0 0", fontSize: "0.84rem", lineHeight: 1.45 }}>{row.summary}</p>}
              <div style={{ color: "#64748b", fontSize: "0.72rem", marginTop: "0.35rem" }}>
                {row.arxiv_id ? `arXiv ${row.arxiv_id}` : "no arXiv id"}
                {row.quality_v2 != null ? ` · quality ${row.quality_v2.toFixed(3)}` : ""}
              </div>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

export default function PageReviewCandidatePage() {
  const params = useParams();
  const searchParams = useSearchParams();
  const pageId = params?.pageId as string;
  const candidateId = params?.candidateId as string;
  const [data, setData] = useState<ReviewData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<"candidate" | "evidence" | "traceability">("candidate");

  useEffect(() => {
    if (!pageId || !candidateId) return;
    setLoading(true);
    const token = searchParams?.get("review_token") || "";
    const headers = new Headers();
    // Preview fallback only: URL tokens can leak via browser history, logs, and referrers.
    // Prefer server-side header forwarding or reverse-proxy auth for managed/public exposure.
    if (token) headers.set("X-Page-Review-Token", token);
    fetch(`/api/admin/page-review/page/${pageId}/candidates/${candidateId}`, { cache: "no-store", headers })
      .then((res) => res.ok ? res.json() : Promise.reject(new Error(`HTTP ${res.status}`)))
      .then((payload) => {
        setData(payload);
        setError(null);
        setLoading(false);
      })
      .catch((err) => {
        setError(err instanceof Error ? err.message : "Failed to load review candidate");
        setLoading(false);
      });
  }, [pageId, candidateId, searchParams]);

  const evidenceByClaim = useMemo(() => {
    const map: Record<number, EvidencePanel> = {};
    for (const panel of data?.evidence_panels || []) map[panel.claim_id] = panel;
    return map;
  }, [data?.evidence_panels]);

  const processedMarkdown = useMemo(() => {
    if (!data?.candidate.markdown) return "";
    return renderReviewMarkers(data.candidate.markdown);
  }, [data?.candidate.markdown]);

  const forbiddenHits = useMemo(() => {
    if (!data?.checks.forbidden_tokens?.hits) return [];
    return Object.entries(data.checks.forbidden_tokens.hits).filter(([, hit]) => hit).map(([token]) => token);
  }, [data?.checks.forbidden_tokens]);

  if (loading) return <main style={{ padding: "2rem", color: "#94a3b8" }}>Loading review candidate...</main>;
  if (error) return <main style={{ padding: "2rem", color: "#ef4444" }}>Review candidate failed to load: {error}</main>;
  if (!data) return <main style={{ padding: "2rem", color: "#94a3b8" }}>No review data returned.</main>;

  const counts = data.packet.integration?.counts || {};
  const drift = data.checks.live_drift;

  return (
    <main style={{ maxWidth: "76rem", margin: "0 auto", padding: "2rem 1rem 4rem" }}>
      <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.75rem" }}>
        <Link href="/" style={{ color: "#818cf8", textDecoration: "none" }}>Home</Link>
        <span> / Admin / Page review / Page {data.candidate.page_id}</span>
      </div>

      <header style={{ marginBottom: "1.25rem" }}>
        <div style={{ color: "#94a3b8", fontSize: "0.82rem", marginBottom: "0.35rem" }}>Read-only candidate review</div>
        <h1 style={{ color: "#f8fafc", fontSize: "1.8rem", margin: 0 }}>{data.candidate.label}</h1>
        <p style={{ color: "#64748b", margin: "0.45rem 0 0", lineHeight: 1.5 }}>
          This route serves local packet artifacts and live read checks only. It exposes no write handler, proposal vote flow, hidden form, or apply control.
        </p>
      </header>

      <section style={{ display: "flex", gap: "0.45rem", flexWrap: "wrap", marginBottom: "1rem" }}>
        <Badge label="Review" status={data.review_status} />
        <Badge label="Hash" status={data.checks.candidate_hash.status} />
        <Badge label="Markers" status={data.checks.marker_bijection.status} />
        <Badge label="Forbidden" status={data.checks.forbidden_tokens.status} />
        <Badge label="Canonicalizer" status={data.checks.canonicalizer.status} />
        <Badge label="Preimage" status={drift.status} />
        <Badge label="Gate" status={data.checks.apply_gate.status || "UNKNOWN"} />
      </section>

      <section style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(13rem,1fr))", gap: "0.75rem", marginBottom: "1.25rem" }}>
        <Metric label="Candidate SHA" value={data.candidate.sha256} />
        <Metric label="Packet validation" value={data.packet.validation?.status || "unknown"} />
        <Metric label="Apply allowed" value={String(data.checks.apply_gate.allowed_to_apply)} />
        <Metric label="Integrated rows" value={`${counts.integrated_total_v3 ?? "?"}/${counts.total_original_survivor_rows_considered ?? "?"}`} />
        <Metric label="New over v2" value={counts.newly_integrated_v3 ?? "?"} />
        <Metric label="Excluded or held" value={counts.excluded_or_held_total ?? "?"} />
      </section>

      {drift.status !== "CURRENT" && (
        <section style={{ border: "1px solid rgba(245,158,11,0.45)", background: "rgba(245,158,11,0.12)", color: "#fbbf24", borderRadius: "6px", padding: "0.85rem 1rem", marginBottom: "1.25rem" }}>
          Live baseline drift detected. This is displayed as a stale-preimage signal only; it does not enable mutation.
        </section>
      )}

      {forbiddenHits.length > 0 && (
        <section style={{ border: "1px solid rgba(239,68,68,0.45)", background: "rgba(239,68,68,0.12)", color: "#fca5a5", borderRadius: "6px", padding: "0.85rem 1rem", marginBottom: "1.25rem" }}>
          Forbidden token hits: {forbiddenHits.join(", ")}
        </section>
      )}

      <nav style={{ display: "flex", gap: "0.5rem", marginBottom: "1.25rem", flexWrap: "wrap" }}>
        {(["candidate", "evidence", "traceability"] as const).map((tab) => (
          <button
            key={tab}
            type="button"
            onClick={() => setActiveTab(tab)}
            style={{
              border: activeTab === tab ? "1px solid #818cf8" : "1px solid #334155",
              background: activeTab === tab ? "rgba(99,102,241,0.2)" : "transparent",
              color: activeTab === tab ? "#c7d2fe" : "#94a3b8",
              borderRadius: "5px",
              padding: "0.45rem 0.75rem",
              cursor: "pointer",
              textTransform: "capitalize",
            }}
          >
            {tab}
          </button>
        ))}
      </nav>

      {activeTab === "candidate" && (
        <article style={{ display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: "1rem" }}>
          <div className="prose max-w-none" style={{ color: "#94a3b8", lineHeight: 1.7 }}>
            <ReactMarkdown
              remarkPlugins={[remarkMath]}
              rehypePlugins={[rehypeRaw, [rehypeKatex, { throwOnError: false, output: "html", strict: "ignore" }]]}
              components={{
                h1: ({ children }) => <h1 style={{ color: "#f8fafc", fontSize: "1.5rem", marginTop: "1rem" }}>{children}</h1>,
                h2: ({ children }) => <h2 style={{ color: "#f8fafc", fontSize: "1.18rem", marginTop: "1.5rem", paddingTop: "1rem", borderTop: "1px solid #1e293b" }}>{children}</h2>,
                p: ({ children }) => <p style={{ marginBottom: "1rem", color: "#94a3b8" }}>{children}</p>,
                span: ({ children, ...props }: any) => {
                  const claimId = Number(props["data-claim-id"]);
                  if (Number.isFinite(claimId) && claimId > 0) {
                    return <ClaimSpan claimId={claimId} evidenceByClaim={evidenceByClaim}>{children}</ClaimSpan>;
                  }
                  return <span {...props}>{children}</span>;
                },
              }}
            >
              {processedMarkdown}
            </ReactMarkdown>
          </div>
        </article>
      )}

      {activeTab === "evidence" && (
        <div style={{ display: "grid", gap: "0.85rem" }}>
          {data.evidence_panels.map((panel) => <EvidenceCard key={panel.claim_id} panel={panel} />)}
        </div>
      )}

      {activeTab === "traceability" && (
        <div style={{ display: "grid", gap: "1rem" }}>
          <section style={{ border: "1px solid #1e293b", background: "#0f172a", borderRadius: "6px", padding: "1rem" }}>
            <h2 style={{ color: "#f8fafc", margin: "0 0 0.75rem", fontSize: "1rem" }}>Traceability Summary</h2>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(12rem,1fr))", gap: "0.65rem" }}>
              <Metric label="Paragraphs" value={data.traceability_summary.paragraph_count ?? "?"} />
              <Metric label="Original context paragraphs" value={data.traceability_summary.entries_with_original_context ?? "?"} />
              <Metric label="Newly integrated" value={data.traceability_summary.newly_integrated ?? "?"} />
              <Metric label="Held/excluded" value={data.traceability_summary.excluded_or_held ?? "?"} />
            </div>
          </section>

          <section style={{ border: "1px solid #1e293b", background: "#0f172a", borderRadius: "6px", padding: "1rem" }}>
            <h2 style={{ color: "#f8fafc", margin: "0 0 0.75rem", fontSize: "1rem" }}>Coherence Guards</h2>
            <pre style={{ color: "#94a3b8", whiteSpace: "pre-wrap", fontFamily: "inherit", margin: 0 }}>{data.packet.coherence_guard_decisions}</pre>
          </section>

          <section style={{ border: "1px solid #1e293b", background: "#0f172a", borderRadius: "6px", padding: "1rem", overflowX: "auto" }}>
            <h2 style={{ color: "#f8fafc", margin: "0 0 0.75rem", fontSize: "1rem" }}>Row Dispositions</h2>
            <table style={{ width: "100%", borderCollapse: "collapse", fontSize: "0.8rem" }}>
              <thead>
                <tr style={{ color: "#64748b", textAlign: "left" }}>
                  <th style={{ padding: "0.45rem", borderBottom: "1px solid #1e293b" }}>ID</th>
                  <th style={{ padding: "0.45rem", borderBottom: "1px solid #1e293b" }}>Priority</th>
                  <th style={{ padding: "0.45rem", borderBottom: "1px solid #1e293b" }}>Disposition</th>
                  <th style={{ padding: "0.45rem", borderBottom: "1px solid #1e293b" }}>Reason</th>
                </tr>
              </thead>
              <tbody>
                {(data.packet.integration.row_dispositions || []).map((row) => (
                  <tr key={row.omitted_survivor_claim_id} style={{ color: "#94a3b8" }}>
                    <td style={{ padding: "0.45rem", borderBottom: "1px solid #1e293b", fontFamily: "monospace" }}>{row.omitted_survivor_claim_id}</td>
                    <td style={{ padding: "0.45rem", borderBottom: "1px solid #1e293b" }}>{row.priority}</td>
                    <td style={{ padding: "0.45rem", borderBottom: "1px solid #1e293b" }}>{row.disposition}</td>
                    <td style={{ padding: "0.45rem", borderBottom: "1px solid #1e293b" }}>{row.reason}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
        </div>
      )}
    </main>
  );
}
