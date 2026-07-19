"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import { ExternalLink, Search } from "lucide-react";

type WikiPage = {
  id: number;
  slug: string;
  title: string;
};

type Idea = {
  id: number;
  page_slug: string;
  page_title: string;
  survey_combo: string;
  question: string;
  why_now?: string;
  novelty: number;
  feasibility: number;
  status: string;
  coverage_status?: string | null;
  display_badge?: string | null;
  claim_id?: number | null;
  survey_slugs?: Record<string, string>;
  anchor_claims?: Array<{ id: number; text: string; trust_level?: string }>;
  created_at?: string | null;
};

const STATUS_OPTIONS = ["all", "draft", "active", "review-queue", "covered"];
const FOCUSED_PAGE_SLUG = "galaxy-evolution";
const FOCUSED_PAGE_TITLE = "Galaxy Evolution";
const MANUSCRIPT_PDFS = [
  {
    group: "Method 1",
    label: "Environment quenching",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp2_environment_quenching_aas.pdf",
  },
  {
    group: "Method 1",
    label: "Maintenance heating",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp3_maintenance_heating_aas.pdf",
  },
  {
    group: "Method 2",
    label: "Outflow escape/recycling",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p1_outflow_escape_recycling_aas.pdf",
  },
  {
    group: "Method 2",
    label: "Radio-jet environment",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p2_radio_jet_environment_aas.pdf",
  },
  {
    group: "Method 2",
    label: "Feedback transition mass",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p3_feedback_transition_mass_aas.pdf",
  },
  {
    group: "Method 3",
    label: "Multiphase census",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p1_multiphase_census_aas.pdf",
  },
  {
    group: "Method 3",
    label: "Gas depletion efficiency",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p2_gas_depletion_efficiency_aas.pdf",
  },
  {
    group: "Method 3",
    label: "Simulation validation",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p3_simulation_validation_aas.pdf",
  },
  {
    group: "Shared pilot",
    label: "SDSS AGN/SFR pilot",
    href: "/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf",
  },
  {
    group: "Public-data study",
    label: "SDSS mass–metallicity & FMR aperture",
    href: "/agent-reports/research-frontiers/galaxy-evolution-mzr-fmr-draft.pdf",
  },
  {
    group: "Frontier study",
    label: "Scaling relations from z≈0 to the JWST frontier",
    href: "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf",
  },
  {
    group: "Frontier study",
    label: "Calibration ≠ validation: IllustrisTNG vs SDSS + JWST",
    href: "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf",
  },
  {
    group: "Draft in progress",
    label: "Does IllustrisTNG make enough massive galaxies early enough?",
    href: "/agent-reports/research-frontiers/galaxy-evolution-massive-galaxies-draft.pdf",
  },
];

function statusLabel(status: string | null | undefined) {
  return (status || "unknown").replace(/-/g, " ");
}

function coverageLabel(idea: Idea) {
  if (idea.display_badge) return idea.display_badge;
  return statusLabel(idea.coverage_status || "unverified");
}

function score(value: number | null | undefined) {
  if (value === null || value === undefined || Number.isNaN(value)) return "—";
  return value.toFixed(2);
}

function coverageColor(label: string) {
  if (label === "screened pass") return "#22c55e";
  if (label === "partial") return "#eab308";
  if (label === "covered") return "#94a3b8";
  if (label === "failed entity") return "#f97316";
  return "#64748b";
}

export default function IdeasIndexClient() {
  const [ideas, setIdeas] = useState<Idea[]>([]);
  const [loading, setLoading] = useState(true);
  const [status, setStatus] = useState("all");
  const [query, setQuery] = useState("");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      setLoading(true);
      setError(null);
      try {
        const pagesRes = await fetch("/api/pages?limit=200");
        const pagesData = await pagesRes.json();
        const allPages: WikiPage[] = Array.isArray(pagesData) ? pagesData : pagesData.pages || [];
        const pages = allPages.filter((page) => page.slug === FOCUSED_PAGE_SLUG);

        const batches = await Promise.all(
          pages.map(async (page) => {
            try {
              const res = await fetch(`/api/pages/${page.slug}/ideas?per_page=200`);
              if (!res.ok) return [];
              const data = await res.json();
              return (data.ideas || []).map((idea: Idea) => ({
                ...idea,
                page_slug: page.slug,
                page_title: page.title,
              }));
            } catch {
              return [];
            }
          })
        );

        if (!cancelled) {
          setIdeas(batches.flat().sort((a, b) => (b.novelty || 0) - (a.novelty || 0)));
        }
      } catch {
        if (!cancelled) setError("Research ideas are temporarily unavailable.");
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    load();
    return () => {
      cancelled = true;
    };
  }, []);

  const counts = useMemo(() => {
    const result: Record<string, number> = { all: ideas.length };
    for (const idea of ideas) {
      result[idea.status] = (result[idea.status] || 0) + 1;
    }
    return result;
  }, [ideas]);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return ideas.filter((idea) => {
      if (status !== "all" && idea.status !== status) return false;
      if (!q) return true;
      const blob = [
        idea.question,
        idea.survey_combo,
        idea.page_title,
        idea.why_now,
        idea.status,
        idea.coverage_status,
      ].join(" ").toLowerCase();
      return blob.includes(q);
    });
  }, [ideas, query, status]);

  return (
    <main style={{ padding: "2rem 1.5rem", color: "#f8fafc" }}>
      <div style={{ maxWidth: "1100px", margin: "0 auto" }}>
        <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", gap: "1rem", flexWrap: "wrap", marginBottom: "1.25rem" }}>
          <div>
            <h1 style={{ fontSize: "2rem", lineHeight: 1.15, fontWeight: 700, margin: "0 0 0.35rem" }}>
              {FOCUSED_PAGE_TITLE} Research
            </h1>
            <p style={{ color: "#94a3b8", margin: 0, fontSize: "0.95rem" }}>
              {loading ? "Loading ideas…" : `${filtered.length} of ${ideas.length} ${FOCUSED_PAGE_TITLE} ideas`}
            </p>
          </div>

          <label style={{ position: "relative", minWidth: "260px", flex: "0 1 360px" }}>
            <Search size={16} style={{ position: "absolute", left: "0.8rem", top: "50%", transform: "translateY(-50%)", color: "#64748b" }} />
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search Galaxy Evolution ideas"
              style={{
                width: "100%",
                height: "2.5rem",
                padding: "0 0.8rem 0 2.2rem",
                borderRadius: "6px",
                border: "1px solid #334155",
                background: "#0f172a",
                color: "#f8fafc",
                outline: "none",
              }}
            />
          </label>
        </div>

        <section
          aria-label="Galaxy Evolution manuscript PDFs"
          style={{
            border: "1px solid #334155",
            background: "linear-gradient(135deg, rgba(17,24,39,0.96), rgba(30,41,59,0.82))",
            borderRadius: "10px",
            padding: "1rem",
            marginBottom: "1.25rem",
          }}
        >
          <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap", marginBottom: "0.7rem" }}>
            <div>
              <div style={{ color: "#a5b4fc", fontSize: "0.72rem", fontWeight: 700, letterSpacing: "0.08em", textTransform: "uppercase" }}>
                Manuscript PDFs
              </div>
              <p style={{ color: "#94a3b8", margin: "0.15rem 0 0", fontSize: "0.88rem" }}>
                Draft PDF manuscripts for the current Galaxy Evolution research topics.
              </p>
            </div>
            <Link href="/wiki/galaxy-evolution" style={{ color: "#93c5fd", textDecoration: "none", fontSize: "0.84rem", fontWeight: 600 }}>
              Open Galaxy Evolution wiki
            </Link>
          </div>
          <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap" }}>
            {MANUSCRIPT_PDFS.map((pdf) => (
              <a
                key={pdf.href}
                href={pdf.href}
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  gap: "0.35rem",
                  border: "1px solid #334155",
                  borderRadius: "999px",
                  background: "#0f172a",
                  color: "#bfdbfe",
                  padding: "0.35rem 0.7rem",
                  textDecoration: "none",
                  fontSize: "0.82rem",
                  fontWeight: 600,
                }}
              >
                <span style={{ color: "#94a3b8", fontWeight: 500 }}>{pdf.group}</span>
                {pdf.label}
                <ExternalLink size={13} />
              </a>
            ))}
          </div>
        </section>

        <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap", marginBottom: "1.25rem" }}>
          {STATUS_OPTIONS.map((option) => {
            const active = status === option;
            return (
              <button
                key={option}
                onClick={() => setStatus(option)}
                style={{
                  height: "2.1rem",
                  padding: "0 0.8rem",
                  borderRadius: "6px",
                  border: active ? "1px solid #6366f1" : "1px solid #334155",
                  background: active ? "#312e81" : "#111827",
                  color: active ? "#ffffff" : "#94a3b8",
                  cursor: "pointer",
                  fontSize: "0.85rem",
                  textTransform: "capitalize",
                }}
              >
                {statusLabel(option)} {counts[option] ?? 0}
              </button>
            );
          })}
        </div>

        {error && (
          <div style={{ border: "1px solid #7f1d1d", background: "#1f1215", color: "#fecaca", borderRadius: "8px", padding: "1rem", marginBottom: "1rem" }}>
            {error}
          </div>
        )}

        {loading ? (
          <div style={{ color: "#64748b", padding: "3rem 0", textAlign: "center" }}>Loading ideas…</div>
        ) : (
          <div style={{ display: "grid", gap: "0.75rem" }}>
            {filtered.map((idea) => {
              const claimId = idea.claim_id || idea.anchor_claims?.[0]?.id || null;
              const coverage = coverageLabel(idea);
              const coverageText = coverage.replace(/_/g, " ");
              return (
                <article
                  key={`${idea.page_slug}-${idea.id}`}
                  style={{
                    border: "1px solid #334155",
                    background: "#111827",
                    borderRadius: "8px",
                    padding: "1rem",
                  }}
                >
                  <div style={{ display: "flex", justifyContent: "space-between", gap: "1rem", alignItems: "flex-start", flexWrap: "wrap" }}>
                    <div style={{ minWidth: 0, flex: "1 1 520px" }}>
                      <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap", marginBottom: "0.55rem" }}>
                        <span style={{ color: "#c4b5fd", fontSize: "0.78rem", fontWeight: 600, textTransform: "uppercase" }}>{statusLabel(idea.status)}</span>
                        <span style={{ color: coverageColor(coverageText), fontSize: "0.78rem", fontWeight: 600, textTransform: "uppercase" }}>{coverageText}</span>
                      </div>
                      <h2 style={{ fontSize: "1rem", lineHeight: 1.45, margin: "0 0 0.6rem", color: "#f8fafc", fontWeight: 650 }}>
                        {idea.question}
                      </h2>
                      {idea.why_now && (
                        <p style={{ margin: "0 0 0.75rem", color: "#94a3b8", lineHeight: 1.55, fontSize: "0.9rem" }}>
                          {idea.why_now}
                        </p>
                      )}
                    </div>

                    <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 4.25rem)", gap: "0.4rem", flex: "0 0 auto" }}>
                      <div style={{ border: "1px solid #334155", borderRadius: "6px", padding: "0.45rem", textAlign: "center" }}>
                        <div style={{ color: "#64748b", fontSize: "0.7rem" }}>Novelty</div>
                        <div style={{ color: "#f8fafc", fontWeight: 700 }}>{score(idea.novelty)}</div>
                      </div>
                      <div style={{ border: "1px solid #334155", borderRadius: "6px", padding: "0.45rem", textAlign: "center" }}>
                        <div style={{ color: "#64748b", fontSize: "0.7rem" }}>Feasible</div>
                        <div style={{ color: "#f8fafc", fontWeight: 700 }}>{score(idea.feasibility)}</div>
                      </div>
                    </div>
                  </div>

                  <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap", marginTop: "0.8rem", paddingTop: "0.8rem", borderTop: "1px solid #1f2937" }}>
                    <div style={{ display: "flex", gap: "0.45rem", flexWrap: "wrap", alignItems: "center" }}>
                      <Link href={`/wiki/${idea.page_slug}`} style={{ color: "#93c5fd", textDecoration: "none", fontSize: "0.86rem", fontWeight: 600 }}>
                        {idea.page_title}
                      </Link>
                      {claimId && (
                        <Link href={`/wiki/${idea.page_slug}#claim-${claimId}`} style={{ color: "#a7f3d0", textDecoration: "none", fontSize: "0.86rem", fontWeight: 600 }}>
                          Claim #{claimId}
                        </Link>
                      )}
                      {Object.entries(idea.survey_slugs || {}).map(([name, slug]) => (
                        <Link key={`${idea.id}-${slug}`} href={`/surveys/${slug}`} style={{ color: "#c4b5fd", textDecoration: "none", fontSize: "0.84rem" }}>
                          {name}
                        </Link>
                      ))}
                    </div>
                    <Link href={`/wiki/${idea.page_slug}${claimId ? `#claim-${claimId}` : ""}`} style={{ display: "inline-flex", alignItems: "center", gap: "0.35rem", color: "#94a3b8", textDecoration: "none", fontSize: "0.84rem" }}>
                      Open <ExternalLink size={14} />
                    </Link>
                  </div>
                </article>
              );
            })}
            {filtered.length === 0 && (
              <div style={{ color: "#64748b", padding: "3rem 0", textAlign: "center" }}>
                No matching ideas.
              </div>
            )}
          </div>
        )}
      </div>
    </main>
  );
}
