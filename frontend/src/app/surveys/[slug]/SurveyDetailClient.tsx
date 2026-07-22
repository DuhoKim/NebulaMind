"use client";

import { useEffect, useId, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import SurveyLogo from "@/components/surveys/SurveyLogo";

interface SurveyDetail {
  slug: string;
  name: string;
  full_name: string;
  description: string;
  emoji: string | null;
  logo_url: string | null;
  logo_bg: "any" | "dark" | "light" | null;
  wavelength_range: string;
  wavelength_band: string;
  sky_coverage_deg2: number | null;
  sky_coverage_note: string | null;
  redshift_range: string | null;
  instruments: string[];
  current_data_release: string | null;
  data_volume: string | null;
  primary_science_goals: string;
  flagship_programs: string[];
  operator: string | null;
  status: string;
  archive_url: string | null;
  mission_url: string | null;
  linked_research_ideas_count: number;
  related_wiki_page_slugs: string[];
  data_releases: SurveyRelease[];
  datasets_count: number;
  facility_profiles: SurveyFacilityProfile[];
  updated_at: string | null;
  // Numeric fields
  num_sources_count: number | null;
  limiting_magnitude: number | null;
  wavelength_center_um: number | null;
  z_max: number | null;
  dr_year: number | null;
  data_volume_tb: number | null;
}

interface SurveyFacilityProfile {
  slug: string;
  short_name: string | null;
  full_name: string;
  relation_type: string;
  is_primary: boolean;
  event_count: number;
  upcoming_count: number;
}

interface SurveyEvent {
  id: number;
  slug: string;
  title: string;
  kind: string;
  track: string;
  summary: string | null;
  occurs_at: string | null;
  occurs_at_confidence: string | null;
  occurrence_status: string | null;
  source_url: string | null;
  data_portal_urls: string | null;
  featured: boolean | null;
  credibility_score: number | null;
  facility_slug: string | null;
  facility_name: string | null;
  facility_url: string | null;
}

interface SurveyRelease {
  label: string;
  release_date: string | null;
  release_year: number | null;
  summary: string;
  n_objects: number | null;
  sky_coverage_deg2: number | null;
  data_volume_tb: number | null;
  doi: string | null;
  bibcode: string | null;
  url: string | null;
  status: "planned" | "released" | "superseded" | "final";
}

interface CatalogField {
  name: string;
  dtype: string | null;
  unit: string | null;
  description: string;
  example: string | null;
  is_key: boolean;
  source_url?: string | null;
}

interface SurveyDataset {
  slug: string;
  name: string;
  full_name: string;
  description: string;
  data_type: string;
  release_label: string | null;
  release_year: number | null;
  sample_size: number | null;
  doi: string | null;
  bibcode: string | null;
  registry: string | null;
  license: string | null;
  primary_url: string;
  archive_url: string | null;
  url_verified_ok: boolean | null;
  catalog_fields: CatalogField[];
}

interface Idea {
  id: number;
  page_slug: string;
  page_title: string;
  survey_combo: string;
  question: string;
  novelty: number;
  feasibility: number;
  saved_by_papa: boolean;
  status: string;
}

const STATUS_COLORS: Record<string, { bg: string; color: string; label: string; icon: string }> = {
  operational:   { bg: "rgba(34,197,94,0.12)",   color: "#22c55e", label: "Operational",   icon: "✅" },
  commissioning: { bg: "rgba(234,179,8,0.12)",   color: "#ca8a04", label: "Commissioning", icon: "🔧" },
  planned:       { bg: "rgba(99,102,241,0.12)",  color: "#818cf8", label: "Planned",        icon: "📋" },
  retired:       { bg: "rgba(100,116,139,0.12)", color: "#64748b", label: "Retired",        icon: "📦" },
};

// ── Formatters ────────────────────────────────────────────────────────────────

function formatSources(n: number): string {
  const withCommas = n.toLocaleString("en-US");
  let readable = "";
  if (n >= 1e12)      readable = `~${(n / 1e12).toFixed(1)} trillion`;
  else if (n >= 1e9)  readable = `~${(n / 1e9).toFixed(1)} billion`;
  else if (n >= 1e6)  readable = `~${(n / 1e6).toFixed(1)} million`;
  else if (n >= 1e3)  readable = `~${(n / 1e3).toFixed(1)} thousand`;
  return readable ? `${withCommas} (${readable})` : withCommas;
}

function formatWavelengthUm(um: number): string {
  if (um >= 1e6)  return `${(um / 1e6).toPrecision(3)} m`;
  if (um >= 1e3)  return `${(um / 1e3).toPrecision(3)} mm`;
  if (um >= 1)    return `${um.toPrecision(4)} μm`;
  if (um >= 1e-3) return `${(um * 1e3).toPrecision(3)} nm`;
  // X-ray / gamma: keV or MeV
  const keV = 1.23984e-3 / um;
  if (keV >= 1e3) return `${(keV / 1e3).toPrecision(3)} MeV`;
  return `${keV.toPrecision(3)} keV`;
}

function formatReleaseDate(release: SurveyRelease): string {
  if (release.release_date) {
    return new Date(`${release.release_date}T00:00:00`).toLocaleDateString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
    });
  }
  return release.release_year ? String(release.release_year) : "Date pending";
}

function formatDataType(value: string): string {
  return value.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase());
}

function formatEventDate(value: string | null): string {
  if (!value) return "Date pending";
  return new Date(value).toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

// ── Sub-components ─────────────────────────────────────────────────────────────

function ScoreDots({ value, color }: { value: number; color: string }) {
  const filled = Math.round(value * 5);
  return (
    <span style={{ display: "inline-flex", gap: "2px", verticalAlign: "middle" }}>
      {[1, 2, 3, 4, 5].map(i => (
        <span key={i} style={{
          width: "8px", height: "8px", borderRadius: "50%",
          background: i <= filled ? color : "#334155",
          display: "inline-block",
        }} />
      ))}
    </span>
  );
}

interface ParamRowProps {
  label: string;
  value: React.ReactNode;
  i: number;
}
function ParamRow({ label, value, i }: ParamRowProps) {
  const bg = i % 2 === 0 ? "rgba(255,255,255,0.02)" : "transparent";
  return (
    <>
      <div style={{ padding: "0.6rem 1.25rem", borderBottom: "1px solid #1e293b", background: bg, color: "#64748b", fontSize: "0.85rem", fontWeight: 500 }}>
        {label}
      </div>
      <div style={{ padding: "0.6rem 1.25rem", borderBottom: "1px solid #1e293b", background: bg, color: "#cbd5e1", fontSize: "0.85rem" }}>
        {value}
      </div>
    </>
  );
}

function SectionFrame({ title, id, children }: { title: string; id?: string; children: React.ReactNode }) {
  return (
    <section id={id} style={{ marginBottom: "2rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "8px", overflow: "hidden" }}>
      <div style={{ padding: "0.75rem 1.25rem", borderBottom: "1px solid #334155", background: "#162032" }}>
        <span style={{ fontWeight: 600, color: "#94a3b8", fontSize: "0.85rem", textTransform: "uppercase", letterSpacing: "0.05em" }}>
          {title}
        </span>
      </div>
      {children}
    </section>
  );
}

function ReleaseTimeline({ releases }: { releases: SurveyRelease[] }) {
  const current = releases.find(r => r.status === "released" || r.status === "final");

  return (
    <SectionFrame title="Data Releases" id="data-releases">
      <div style={{ padding: "1rem 1.25rem" }}>
        {releases.length === 0 ? (
          <p style={{ margin: 0, color: "#64748b", fontSize: "0.9rem" }}>No public data releases yet.</p>
        ) : (
          <div style={{ display: "flex", flexDirection: "column", gap: "0.85rem" }}>
            {releases.map(release => {
              const isCurrent = current?.label === release.label;
              const isPlanned = release.status === "planned";
              const isSuperseded = release.status === "superseded";
              return (
                <div
                  key={release.label}
                  style={{
                    position: "relative",
                    border: isCurrent ? "1px solid #6366f1" : "1px solid #334155",
                    borderLeft: isCurrent ? "3px solid #6366f1" : "3px solid #475569",
                    borderRadius: "8px",
                    padding: "0.85rem 1rem",
                    background: isCurrent ? "rgba(99,102,241,0.08)" : "#0f172a",
                    opacity: isPlanned ? 0.62 : 1,
                    fontStyle: isPlanned ? "italic" : "normal",
                  }}
                >
                  <div style={{ display: "flex", gap: "0.5rem", alignItems: "center", flexWrap: "wrap", marginBottom: "0.45rem" }}>
                    <span style={{
                      fontSize: "0.78rem",
                      fontWeight: 800,
                      color: isSuperseded ? "#64748b" : "#f8fafc",
                      textDecoration: isSuperseded ? "line-through" : "none",
                      letterSpacing: "0.02em",
                    }}>
                      {release.label}
                    </span>
                    {!isPlanned && (
                      <span style={{ fontSize: "0.72rem", color: "#94a3b8", background: "#1e293b", border: "1px solid #334155", borderRadius: "999px", padding: "0.08rem 0.5rem" }}>
                        {formatReleaseDate(release)}
                      </span>
                    )}
                    {isPlanned && (
                      <span style={{ fontSize: "0.72rem", color: "#818cf8" }}>{formatReleaseDate(release)}</span>
                    )}
                    <span style={{
                      fontSize: "0.68rem",
                      fontWeight: 700,
                      color: isPlanned ? "#818cf8" : isSuperseded ? "#64748b" : "#22c55e",
                      background: isPlanned ? "rgba(99,102,241,0.12)" : isSuperseded ? "rgba(100,116,139,0.12)" : "rgba(34,197,94,0.12)",
                      borderRadius: "999px",
                      padding: "0.08rem 0.45rem",
                      textTransform: "uppercase",
                    }}>
                      {isCurrent ? "Current" : release.status}
                    </span>
                  </div>
                  <p style={{ margin: "0 0 0.5rem", color: "#cbd5e1", fontSize: "0.88rem", lineHeight: 1.55 }}>
                    {release.summary}
                  </p>
                  <div style={{ display: "flex", gap: "0.75rem", flexWrap: "wrap", color: "#64748b", fontSize: "0.76rem" }}>
                    {release.n_objects != null && <span>{formatSources(release.n_objects)} objects</span>}
                    {release.sky_coverage_deg2 != null && <span>{release.sky_coverage_deg2.toLocaleString("en-US")} deg²</span>}
                    {release.doi && (
                      <a href={`https://doi.org/${release.doi}`} target="_blank" rel="noopener noreferrer" style={{ color: "#818cf8", textDecoration: "none" }}>
                        DOI ↗
                      </a>
                    )}
                    {release.url && (
                      <a href={release.url} target="_blank" rel="noopener noreferrer" style={{ color: "#818cf8", textDecoration: "none" }}>
                        Release notes ↗
                      </a>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </SectionFrame>
  );
}

function DatasetCatalogs({ datasets, loading, expectedCount }: { datasets: SurveyDataset[]; loading: boolean; expectedCount: number }) {
  return (
    <SectionFrame title="Data Products & Catalogs">
      <div style={{ padding: "1rem 1.25rem" }}>
        {loading ? (
          <p style={{ margin: 0, color: "#64748b", fontSize: "0.9rem" }}>Loading catalog metadata…</p>
        ) : datasets.length === 0 ? (
          <p style={{ margin: 0, color: "#64748b", fontSize: "0.9rem" }}>
            {expectedCount > 0 ? "No catalog metadata available yet." : "No public catalog metadata available yet."}
          </p>
        ) : (
          <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
            {datasets.map(dataset => <DatasetCard key={dataset.slug} dataset={dataset} />)}
          </div>
        )}
      </div>
    </SectionFrame>
  );
}

function DatasetCard({ dataset }: { dataset: SurveyDataset }) {
  const [open, setOpen] = useState(false);
  const [showAll, setShowAll] = useState(false);
  const fieldPanelId = useId();
  const keyFields = dataset.catalog_fields.filter(f => f.is_key);
  const otherFields = dataset.catalog_fields.filter(f => !f.is_key);
  const visibleFields = showAll ? [...keyFields, ...otherFields] : (keyFields.length ? keyFields : dataset.catalog_fields);

  return (
    <div style={{ border: "1px solid #334155", borderRadius: "8px", overflow: "hidden", background: "#0f172a" }}>
      <div style={{ display: "flex", alignItems: "stretch" }}>
        <button
          type="button"
          onClick={() => setOpen(v => !v)}
          aria-expanded={open}
          aria-controls={fieldPanelId}
          style={{
            flex: 1,
            minWidth: 0,
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            gap: "1rem",
            padding: "0.85rem 1rem",
            background: "transparent",
            border: "none",
            cursor: "pointer",
            textAlign: "left",
          }}
        >
          <span style={{ minWidth: 0 }}>
            <span style={{ display: "block", color: "#f8fafc", fontWeight: 700, fontSize: "0.92rem" }}>{dataset.name}</span>
            <span style={{ display: "flex", gap: "0.45rem", alignItems: "center", flexWrap: "wrap", marginTop: "0.3rem", color: "#64748b", fontSize: "0.74rem" }}>
              <span style={{ color: "#93c5fd", background: "rgba(59,130,246,0.12)", borderRadius: "999px", padding: "0.05rem 0.45rem" }}>
                {formatDataType(dataset.data_type)}
              </span>
              {dataset.release_label && <span>{dataset.release_label}</span>}
              {dataset.sample_size != null && <span>{formatSources(dataset.sample_size)} rows</span>}
              {dataset.license && <span>{dataset.license}</span>}
            </span>
          </span>
          <span style={{ color: "#64748b", fontSize: "0.85rem" }}>{open ? "▲" : "▼"}</span>
        </button>
        <a
          href={dataset.primary_url}
          target="_blank"
          rel="noopener noreferrer"
          title={dataset.url_verified_ok === false ? "Link unverified" : "Open data product"}
          style={{
            alignSelf: "center",
            flexShrink: 0,
            marginRight: "1rem",
            color: dataset.url_verified_ok === false ? "#64748b" : "#818cf8",
            textDecoration: "none",
            fontSize: "0.78rem",
            border: "1px solid #334155",
            borderRadius: 4,
            padding: "0.2rem 0.5rem",
          }}
        >
          Data ↗
        </a>
      </div>
      <div id={fieldPanelId} hidden={!open} style={{ borderTop: "1px solid #1e293b", padding: "0.9rem 1rem 1rem" }}>
          <p style={{ margin: "0 0 0.85rem", color: "#cbd5e1", fontSize: "0.86rem", lineHeight: 1.55 }}>{dataset.description}</p>
          {(dataset.bibcode || dataset.doi) && (
            <div style={{ display: "flex", gap: "0.75rem", flexWrap: "wrap", marginBottom: "0.85rem", fontSize: "0.78rem" }}>
              {dataset.bibcode && (
                <a href={`https://ui.adsabs.harvard.edu/abs/${encodeURIComponent(dataset.bibcode)}`} target="_blank" rel="noopener noreferrer" style={{ color: "#818cf8", textDecoration: "none" }}>
                  ADS {dataset.bibcode} ↗
                </a>
              )}
              {dataset.doi && (
                <a href={`https://doi.org/${dataset.doi}`} target="_blank" rel="noopener noreferrer" style={{ color: "#818cf8", textDecoration: "none" }}>
                  DOI ↗
                </a>
              )}
            </div>
          )}
          {dataset.catalog_fields.length === 0 ? (
            <p style={{ margin: 0, color: "#64748b", fontSize: "0.84rem" }}>No column-level metadata available yet.</p>
          ) : (
            <>
              <div style={{ display: "grid", gridTemplateColumns: "minmax(110px, 0.8fr) minmax(70px, 0.5fr) minmax(70px, 0.5fr) minmax(220px, 2fr)", border: "1px solid #1e293b", borderRadius: 6, overflowX: "auto" }}>
                {["Column", "Type", "Unit", "Description"].map(label => (
                  <div key={label} style={{ padding: "0.45rem 0.6rem", background: "#162032", color: "#94a3b8", fontSize: "0.72rem", fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.05em" }}>
                    {label}
                  </div>
                ))}
                {visibleFields.map((field, i) => (
                  <CatalogFieldRow key={field.name} field={field} i={i} />
                ))}
              </div>
              {otherFields.length > 0 && (
                <button
                  onClick={() => setShowAll(v => !v)}
                  style={{ marginTop: "0.7rem", background: "transparent", color: "#818cf8", border: "1px solid #334155", borderRadius: 4, padding: "0.3rem 0.65rem", cursor: "pointer", fontSize: "0.78rem" }}
                >
                  {showAll ? "Show key columns" : `Show all ${dataset.catalog_fields.length} columns`}
                </button>
              )}
            </>
          )}
      </div>
    </div>
  );
}

function CatalogFieldRow({ field, i }: { field: CatalogField; i: number }) {
  const bg = field.is_key ? "rgba(99,102,241,0.08)" : i % 2 === 0 ? "rgba(255,255,255,0.02)" : "transparent";
  return (
    <>
      <div style={{ padding: "0.45rem 0.6rem", borderTop: "1px solid #1e293b", background: bg, color: field.is_key ? "#f8fafc" : "#cbd5e1", fontSize: "0.78rem", fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, monospace", fontWeight: field.is_key ? 700 : 500 }}>
        {field.name}
      </div>
      <div style={{ padding: "0.45rem 0.6rem", borderTop: "1px solid #1e293b", background: bg, color: "#94a3b8", fontSize: "0.78rem" }}>{field.dtype || "—"}</div>
      <div style={{ padding: "0.45rem 0.6rem", borderTop: "1px solid #1e293b", background: bg, color: "#94a3b8", fontSize: "0.78rem" }}>{field.unit || "—"}</div>
      <div style={{ padding: "0.45rem 0.6rem", borderTop: "1px solid #1e293b", background: bg, color: "#cbd5e1", fontSize: "0.78rem", lineHeight: 1.45 }}>{field.description}</div>
    </>
  );
}

function SurveyNewsEvents({
  events,
  loading,
  linked,
}: {
  events: SurveyEvent[];
  loading: boolean;
  linked: boolean;
}) {
  if (!linked) return null;

  return (
    <SectionFrame title="News & Events">
      <div style={{ padding: "1rem 1.25rem" }}>
        <p style={{ margin: "0 0 0.9rem", color: "#94a3b8", fontSize: "0.9rem", lineHeight: 1.55 }}>
          Latest data releases, proposal calls, and facility milestones linked to this survey.
        </p>
        {loading ? (
          <p style={{ margin: 0, color: "#64748b", fontSize: "0.9rem" }}>Loading facility events…</p>
        ) : events.length === 0 ? (
          <p style={{ margin: 0, color: "#64748b", fontSize: "0.9rem" }}>No tracked news or calendar events yet.</p>
        ) : (
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(3, minmax(240px, 1fr))",
              gap: "0.75rem",
              overflowX: "auto",
              paddingBottom: "0.2rem",
            }}
          >
            {events.map(event => (
              <article
                key={event.id}
                style={{
                  minWidth: 0,
                  background: "#0f172a",
                  border: "1px solid #334155",
                  borderRadius: "8px",
                  padding: "0.9rem",
                }}
              >
                <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap", marginBottom: "0.55rem" }}>
                  {event.facility_slug && (
                    <span style={{ fontSize: "0.7rem", fontWeight: 700, color: "#c4b5fd", background: "rgba(99,102,241,0.12)", borderRadius: "999px", padding: "0.1rem 0.5rem" }}>
                      {event.facility_name || event.facility_slug}
                    </span>
                  )}
                  <span style={{ fontSize: "0.7rem", fontWeight: 700, color: "#93c5fd", background: "rgba(59,130,246,0.12)", borderRadius: "999px", padding: "0.1rem 0.5rem" }}>
                    {event.kind.replace(/_/g, " ")}
                  </span>
                </div>
                <h3 style={{ margin: "0 0 0.45rem", color: "#f8fafc", fontSize: "0.92rem", lineHeight: 1.35 }}>
                  {event.title}
                </h3>
                {event.summary && (
                  <p
                    style={{
                      margin: "0 0 0.75rem",
                      color: "#94a3b8",
                      fontSize: "0.82rem",
                      lineHeight: 1.45,
                      display: "-webkit-box",
                      WebkitLineClamp: 2,
                      WebkitBoxOrient: "vertical",
                      overflow: "hidden",
                    }}
                  >
                    {event.summary}
                  </p>
                )}
                <div style={{ display: "flex", justifyContent: "space-between", gap: "0.65rem", alignItems: "center", color: "#64748b", fontSize: "0.76rem" }}>
                  <span>
                    {formatEventDate(event.occurs_at)}
                    {event.occurrence_status ? ` · ${event.occurrence_status}` : ""}
                  </span>
                  {event.source_url && (
                    <a href={event.source_url} target="_blank" rel="noopener noreferrer" style={{ color: "#818cf8", textDecoration: "none", flexShrink: 0 }}>
                      Source ↗
                    </a>
                  )}
                </div>
              </article>
            ))}
          </div>
        )}
        <div style={{ marginTop: "0.85rem" }}>
          <Link href="/calendar" style={{ color: "#818cf8", textDecoration: "none", fontSize: "0.84rem" }}>
            View calendar →
          </Link>
        </div>
      </div>
    </SectionFrame>
  );
}

// ── Page ──────────────────────────────────────────────────────────────────────

export default function SurveyDetailClient() {
  const params = useParams();
  const slug = params?.slug as string;
  const [survey, setSurvey] = useState<SurveyDetail | null>(null);
  const [ideas, setIdeas] = useState<Idea[]>([]);
  const [datasets, setDatasets] = useState<SurveyDataset[]>([]);
  const [events, setEvents] = useState<SurveyEvent[]>([]);
  const [datasetsLoading, setDatasetsLoading] = useState(false);
  const [eventsLoading, setEventsLoading] = useState(false);
  const [loading, setLoading] = useState(true);
  const [notFound, setNotFound] = useState(false);

  useEffect(() => {
    if (!slug) return;
    fetch(`/api/surveys/${slug}`)
      .then(r => {
        if (r.status === 404) { setNotFound(true); setLoading(false); return null; }
        return r.json();
      })
      .then(d => {
        if (!d) return;
        setSurvey(d);
        setLoading(false);
        if (d.linked_research_ideas_count > 0) {
          fetch(`/api/surveys/${slug}/ideas?include_stale=0`)
            .then(r => r.ok ? r.json() : { ideas: [] })
            .then(r => setIdeas((r.ideas || []).slice(0, 5)));
        }
      })
      .catch(() => setLoading(false));
  }, [slug]);

  useEffect(() => {
    if (!slug || !survey) return;
    setDatasets([]);
    setDatasetsLoading(true);
    fetch(`/api/surveys/${slug}/datasets`)
      .then(r => r.ok ? r.json() : { datasets: [] })
      .then(d => setDatasets(d.datasets || []))
      .finally(() => setDatasetsLoading(false));
  }, [slug, survey]);

  useEffect(() => {
    if (!slug || !survey) return;
    if (!survey.facility_profiles || survey.facility_profiles.length === 0) {
      setEvents([]);
      return;
    }
    setEvents([]);
    setEventsLoading(true);
    fetch(`/api/surveys/${slug}/events?limit=8`)
      .then(r => r.ok ? r.json() : { events: [] })
      .then(d => setEvents(d.events || []))
      .finally(() => setEventsLoading(false));
  }, [slug, survey]);

  if (loading) {
    return (
      <div style={{ maxWidth: "860px", margin: "0 auto", padding: "2rem 1.5rem", color: "#64748b", textAlign: "center" }}>
        Loading survey…
      </div>
    );
  }

  if (notFound || !survey) {
    return (
      <div style={{ maxWidth: "860px", margin: "0 auto", padding: "2rem 1.5rem", textAlign: "center" }}>
        <h1 style={{ color: "#f8fafc", marginBottom: "1rem" }}>Survey not found</h1>
        <Link href="/surveys" style={{ color: "#6366f1" }}>← Back to Surveys Directory</Link>
      </div>
    );
  }

  const status = STATUS_COLORS[survey.status] || STATUS_COLORS.operational;
  const updatedDate = survey.updated_at
    ? new Date(survey.updated_at).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" })
    : null;

  // Build parameter rows — always shown, null → "—"
  const paramRows: { label: string; value: React.ReactNode }[] = [
    {
      label: "Wavelength",
      value: survey.wavelength_range || "—",
    },
    {
      label: "Center Wavelength",
      value: survey.wavelength_center_um != null
        ? formatWavelengthUm(survey.wavelength_center_um)
        : "—",
    },
    {
      label: "Sky Coverage",
      value: survey.sky_coverage_deg2 != null
        ? `${survey.sky_coverage_deg2.toLocaleString("en-US")} deg²${survey.sky_coverage_note ? ` — ${survey.sky_coverage_note}` : ""}`
        : "—",
    },
    {
      label: "Redshift Range",
      value: survey.redshift_range
        ? survey.z_max != null
          ? `${survey.redshift_range} (z_max ≈ ${survey.z_max})`
          : survey.redshift_range
        : "—",
    },
    {
      label: "Data Volume",
      value: survey.data_volume_tb != null
        ? `${survey.data_volume_tb >= 1000
            ? `${(survey.data_volume_tb / 1000).toPrecision(3)} PB`
            : `${survey.data_volume_tb} TB`}${survey.data_volume ? ` (${survey.data_volume})` : ""}`
        : survey.data_volume || "—",
    },
    {
      label: "Data Release",
      value: (
        <>
          {survey.current_data_release
            ? survey.dr_year && !survey.current_data_release.includes(String(survey.dr_year))
              ? `${survey.current_data_release} (${survey.dr_year})`
              : survey.current_data_release
            : "—"}
          {survey.data_releases.length > 1 && (
            <a href="#data-releases" style={{ color: "#818cf8", textDecoration: "none", marginLeft: "0.45rem", whiteSpace: "nowrap" }}>
              · {survey.data_releases.length} releases ↓
            </a>
          )}
        </>
      ),
    },
    {
      label: "Limiting Magnitude",
      value: survey.limiting_magnitude != null
        ? survey.limiting_magnitude.toFixed(1)
        : "—",
    },
    {
      label: "No. of Sources",
      value: survey.num_sources_count != null
        ? formatSources(survey.num_sources_count)
        : "—",
    },
    {
      label: "Instruments",
      value: survey.instruments.length > 0 ? survey.instruments.join(", ") : "—",
    },
    {
      label: "Operator",
      value: survey.operator || "—",
    },
    {
      label: "Status",
      value: (
        <span style={{
          fontSize: "0.75rem", fontWeight: 600, padding: "0.15rem 0.5rem",
          borderRadius: "999px", background: status.bg, color: status.color,
        }}>
          {status.icon} {status.label}
        </span>
      ),
    },
    {
      label: "Archive",
      value: survey.archive_url
        ? (
          <a href={survey.archive_url} target="_blank" rel="noopener noreferrer"
            style={{ color: "#818cf8", textDecoration: "none" }}>
            {(() => { try { return new URL(survey.archive_url).hostname; } catch { return survey.archive_url; } })()}  ↗
          </a>
        )
        : "—",
    },
  ];

  return (
    <div style={{ maxWidth: "860px", margin: "0 auto", padding: "2rem 1.5rem" }}>

      {/* Breadcrumb */}
      <div style={{ marginBottom: "1.5rem", fontSize: "0.85rem", color: "#64748b" }}>
        <Link href="/surveys" style={{ color: "#6366f1", textDecoration: "none" }}>Surveys</Link>
        <span style={{ margin: "0 0.5rem" }}>›</span>
        <span>{survey.name}</span>
      </div>

      {/* Header */}
      <div style={{ marginBottom: "2rem" }}>
        <div style={{ display: "flex", alignItems: "flex-start", gap: "1rem", flexWrap: "wrap" }}>
          <SurveyLogo survey={survey} />
          <div style={{ flex: 1, minWidth: 0 }}>
            <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", flexWrap: "wrap", marginBottom: "0.25rem" }}>
              <h1 style={{ fontSize: "clamp(1.5rem,4vw,2rem)", fontWeight: 700, color: "#f8fafc", margin: 0 }}>
                {survey.name}
              </h1>
              <span style={{
                fontSize: "0.75rem", fontWeight: 600, padding: "0.2rem 0.6rem",
                borderRadius: "999px", background: status.bg, color: status.color,
              }}>
                {status.icon} {status.label}
              </span>
            </div>
            <p style={{ color: "#94a3b8", fontSize: "1rem", margin: 0 }}>{survey.full_name}</p>
          </div>
        </div>
        <p style={{ marginTop: "1.25rem", color: "#94a3b8", lineHeight: 1.7, fontSize: "0.95rem" }}>
          {survey.description}
        </p>
      </div>

      {/* Survey Parameters table */}
      <section style={{ marginBottom: "2rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "8px", overflow: "hidden" }}>
        <div style={{ padding: "0.75rem 1.25rem", borderBottom: "1px solid #334155", background: "#162032" }}>
          <span style={{ fontWeight: 600, color: "#94a3b8", fontSize: "0.85rem", textTransform: "uppercase", letterSpacing: "0.05em" }}>
            Survey Parameters
          </span>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "minmax(160px,200px) 1fr" }}>
          {paramRows.map((row, i) => (
            <ParamRow key={row.label} label={row.label} value={row.value} i={i} />
          ))}
        </div>
      </section>

      <ReleaseTimeline releases={survey.data_releases} />
      <DatasetCatalogs datasets={datasets} loading={datasetsLoading} expectedCount={survey.datasets_count} />
      <SurveyNewsEvents
        events={events}
        loading={eventsLoading}
        linked={(survey.facility_profiles || []).length > 0}
      />

      {/* Primary Science Goals */}
      {survey.primary_science_goals && (
        <section style={{ marginBottom: "2rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "8px", overflow: "hidden" }}>
          <div style={{ padding: "0.75rem 1.25rem", borderBottom: "1px solid #334155", background: "#162032" }}>
            <span style={{ fontWeight: 600, color: "#94a3b8", fontSize: "0.85rem", textTransform: "uppercase", letterSpacing: "0.05em" }}>
              Primary Science Goals
            </span>
          </div>
          <div style={{ padding: "1rem 1.25rem", color: "#cbd5e1", fontSize: "0.9rem", lineHeight: 1.7 }}>
            {survey.primary_science_goals}
          </div>
          {survey.flagship_programs.length > 0 && (
            <div style={{ padding: "0 1.25rem 1rem", display: "flex", gap: "0.5rem", flexWrap: "wrap" }}>
              {survey.flagship_programs.map(p => (
                <span key={p} style={{
                  fontSize: "0.78rem", background: "rgba(99,102,241,0.1)",
                  color: "#818cf8", border: "1px solid rgba(99,102,241,0.2)",
                  borderRadius: "4px", padding: "0.15rem 0.5rem",
                }}>
                  {p}
                </span>
              ))}
            </div>
          )}
        </section>
      )}

      {/* Archive / Mission Links */}
      <div style={{ display: "flex", gap: "0.75rem", marginBottom: "2rem", flexWrap: "wrap" }}>
        {survey.archive_url && (
          <a href={survey.archive_url} target="_blank" rel="noopener noreferrer"
            style={{ padding: "0.5rem 1rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "6px", color: "#94a3b8", textDecoration: "none", fontSize: "0.875rem", display: "flex", alignItems: "center", gap: "0.4rem" }}>
            🗄 Data Archive ↗
          </a>
        )}
        {survey.mission_url && (
          <a href={survey.mission_url} target="_blank" rel="noopener noreferrer"
            style={{ padding: "0.5rem 1rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "6px", color: "#94a3b8", textDecoration: "none", fontSize: "0.875rem", display: "flex", alignItems: "center", gap: "0.4rem" }}>
            🌐 Mission Page ↗
          </a>
        )}
      </div>

      {/* Research Ideas */}
      {survey.linked_research_ideas_count > 0 && (
        <section style={{ marginBottom: "2rem" }}>
          <h2 style={{ fontSize: "1.1rem", fontWeight: 600, color: "#f8fafc", marginBottom: "1rem" }}>
            Research Ideas using {survey.name} on this site
          </h2>
          <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
            {ideas.map(idea => (
              <div key={idea.id} style={{
                background: "#1e293b", border: "1px solid #334155", borderRadius: "8px",
                padding: "1rem 1.25rem",
              }}>
                <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.4rem", flexWrap: "wrap" }}>
                  <span style={{ fontSize: "0.75rem", fontWeight: 600, color: "#818cf8", background: "rgba(99,102,241,0.1)", padding: "0.1rem 0.5rem", borderRadius: "4px" }}>
                    {idea.survey_combo.replace(/\+/g, " + ")}
                  </span>
                  <Link href={`/wiki/${idea.page_slug}`} style={{ fontSize: "0.75rem", color: "#64748b", textDecoration: "none" }}>
                    {idea.page_title} →
                  </Link>
                  {idea.saved_by_papa && <span style={{ color: "#f59e0b", fontSize: "0.75rem" }}>★</span>}
                </div>
                <p style={{ color: "#cbd5e1", fontSize: "0.875rem", lineHeight: 1.5, margin: "0 0 0.5rem" }}>
                  {idea.question}
                </p>
                <div style={{ display: "flex", gap: "1rem", fontSize: "0.75rem", color: "#475569" }}>
                  <span>Novelty: <ScoreDots value={idea.novelty} color="#818cf8" /></span>
                  <span>Feasibility: <ScoreDots value={idea.feasibility} color="#22c55e" /></span>
                </div>
              </div>
            ))}
          </div>
          {survey.linked_research_ideas_count > 5 && (
            <p style={{ marginTop: "0.75rem", fontSize: "0.85rem", color: "#64748b" }}>
              Showing 5 of {survey.linked_research_ideas_count}. See all on individual wiki pages.
            </p>
          )}
        </section>
      )}

      {/* Related Wiki Pages */}
      {survey.related_wiki_page_slugs.length > 0 && (
        <section style={{ marginBottom: "2rem" }}>
          <h2 style={{ fontSize: "1.1rem", fontWeight: 600, color: "#f8fafc", marginBottom: "0.75rem" }}>
            Related wiki pages
          </h2>
          <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap" }}>
            {survey.related_wiki_page_slugs.map(ps => (
              <Link key={ps} href={`/wiki/${ps}`} style={{
                padding: "0.35rem 0.75rem", background: "#1e293b", border: "1px solid #334155",
                borderRadius: "6px", color: "#94a3b8", textDecoration: "none", fontSize: "0.85rem",
              }}>
                {ps.replace(/-/g, " ").replace(/\b\w/g, c => c.toUpperCase())}
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* Footer */}
      <div style={{ borderTop: "1px solid #1e293b", paddingTop: "1rem", fontSize: "0.78rem", color: "#475569" }}>
        {updatedDate && <span>Last metadata update: {updatedDate} (manual seed by Kun)</span>}
        <span style={{ margin: "0 0.5rem" }}>·</span>
        <Link href="/surveys" style={{ color: "#6366f1", textDecoration: "none" }}>← All surveys</Link>
      </div>
    </div>
  );
}
