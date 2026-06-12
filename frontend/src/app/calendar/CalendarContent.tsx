"use client";

import { useEffect, useState, useMemo } from "react";

interface CalendarEvent {
  id: number;
  slug: string;
  title: string;
  kind: string;
  track: string;
  summary: string | null;
  occurs_at: string | null;
  occurs_at_confidence: string;
  occurrence_status: string;
  source_url: string | null;
  data_portal_urls: string | null;
  featured: boolean;
  credibility_score: number | null;
  facility_slug: string | null;
  facility_name: string | null;
  facility_operator: string | null;
  facility_url: string | null;
}

interface CalendarStats {
  total_events: number;
  upcoming_events: number;
  facilities: number;
}

interface FacilityInfo {
  slug: string;
  short_name: string;
  full_name: string;
  event_count: number;
}

const FACILITY_COLORS: Record<string, { bg: string; text: string; border: string }> = {
  desi:         { bg: "rgba(251,146,60,0.15)",  text: "#fb923c", border: "rgba(251,146,60,0.4)" },
  jwst:         { bg: "rgba(96,165,250,0.15)",  text: "#60a5fa", border: "rgba(96,165,250,0.4)" },
  euclid:       { bg: "rgba(74,222,128,0.15)",  text: "#4ade80", border: "rgba(74,222,128,0.4)" },
  "lsst-rubin": { bg: "rgba(167,139,250,0.15)", text: "#a78bfa", border: "rgba(167,139,250,0.4)" },
  rubin:        { bg: "rgba(167,139,250,0.15)", text: "#a78bfa", border: "rgba(167,139,250,0.4)" },
  alma:         { bg: "rgba(248,113,113,0.15)", text: "#f87171", border: "rgba(248,113,113,0.4)" },
  vla:          { bg: "rgba(45,212,191,0.15)",  text: "#2dd4bf", border: "rgba(45,212,191,0.4)" },
};
const DEFAULT_FAC = { bg: "rgba(148,163,184,0.15)", text: "#94a3b8", border: "rgba(148,163,184,0.4)" };

const KIND_CONFIG: Record<string, { label: string; bg: string; text: string }> = {
  release:       { label: "Data Release",  bg: "rgba(96,165,250,0.15)",  text: "#60a5fa" },
  proposal_call: { label: "Proposal Call", bg: "rgba(251,191,36,0.15)",  text: "#fbbf24" },
  milestone:     { label: "Milestone",     bg: "rgba(167,139,250,0.15)", text: "#a78bfa" },
  facility_news: { label: "Facility News", bg: "rgba(74,222,128,0.15)",  text: "#4ade80" },
  news:          { label: "Facility News", bg: "rgba(74,222,128,0.15)",  text: "#4ade80" },
};
const DEFAULT_KIND = { label: "Event", bg: "rgba(148,163,184,0.15)", text: "#94a3b8" };

const TRACK_MAP: Record<string, string[]> = {
  data:    ["release"],
  tools:   ["proposal_call", "milestone"],
  results: ["facility_news", "news"],
};

const TRACK_CONFIG: Record<string, { label: string; desc: string; icon: string; color: string }> = {
  data:    { label: "Data",    desc: "Survey data releases & datasets",        icon: "📦", color: "#60a5fa" },
  tools:   { label: "Tools",   desc: "Proposal calls & instrument milestones", icon: "🔧", color: "#fbbf24" },
  results: { label: "Results", desc: "Science announcements & facility news",  icon: "🔭", color: "#4ade80" },
};

function facilityColor(slug: string | null) {
  if (!slug) return DEFAULT_FAC;
  return FACILITY_COLORS[slug.toLowerCase()] ?? DEFAULT_FAC;
}

function kindConfig(kind: string) {
  return KIND_CONFIG[kind] ?? DEFAULT_KIND;
}

function formatDate(iso: string | null, confidence: string): string {
  if (!iso) return "Date TBD";
  const d = new Date(iso);
  const base = d.toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" });
  return confidence === "soft" ? `~${base}` : base;
}

function monthKey(iso: string | null): string {
  if (!iso) return "Undated";
  const d = new Date(iso);
  return d.toLocaleDateString("en-US", { year: "numeric", month: "long" });
}

function sortMonthKeys(keys: string[]): string[] {
  return keys.sort((a, b) => {
    if (a === "Undated") return 1;
    if (b === "Undated") return -1;
    return new Date(a).getTime() - new Date(b).getTime();
  });
}

function isUpcomingIn30Days(e: CalendarEvent): boolean {
  if (!e.occurs_at) return false;
  const now = Date.now();
  const t = new Date(e.occurs_at).getTime();
  return t >= now && t <= now + 30 * 24 * 60 * 60 * 1000;
}

function FilterChip({
  active, onClick, children,
}: {
  active: boolean;
  onClick: () => void;
  children: React.ReactNode;
}) {
  return (
    <button
      onClick={onClick}
      style={{
        padding: "5px 12px",
        borderRadius: "999px",
        border: "1px solid",
        borderColor: active ? "#6366f1" : "#334155",
        background: active ? "rgba(99,102,241,0.15)" : "transparent",
        color: active ? "#a5b4fc" : "#64748b",
        fontSize: "0.78rem",
        fontWeight: 500,
        cursor: "pointer",
        transition: "all 0.15s",
        whiteSpace: "nowrap" as const,
      }}
    >
      {children}
    </button>
  );
}

function EventCard({ event }: { event: CalendarEvent }) {
  const fc = facilityColor(event.facility_slug);
  const kc = kindConfig(event.kind);
  let portalUrls: Array<{ url: string; label?: string } | string> = [];
  try {
    if (event.data_portal_urls) {
      const parsed = JSON.parse(event.data_portal_urls);
      portalUrls = Array.isArray(parsed) ? parsed : [];
    }
  } catch {}

  const isCompleted = event.occurrence_status === "completed";
  const isDelayed = event.occurrence_status === "delayed";

  return (
    <div
      style={{
        background: "#1e293b",
        border: `1px solid ${isCompleted ? "#1e293b" : "#334155"}`,
        borderLeft: `3px solid ${fc.text}`,
        borderRadius: "8px",
        padding: "1rem 1.25rem",
        opacity: isCompleted ? 0.65 : 1,
        transition: "border-color 0.15s",
      }}
      onMouseEnter={e => { if (!isCompleted) (e.currentTarget as HTMLElement).style.borderColor = "#475569"; }}
      onMouseLeave={e => { if (!isCompleted) (e.currentTarget as HTMLElement).style.borderColor = "#334155"; }}
    >
      <div style={{ display: "flex", flexWrap: "wrap", gap: "0.4rem", marginBottom: "0.5rem", alignItems: "center" }}>
        {event.facility_name && (
          <span style={{
            fontSize: "0.68rem", fontWeight: 700, letterSpacing: "0.04em",
            padding: "2px 7px", borderRadius: "999px",
            background: fc.bg, color: fc.text, border: `1px solid ${fc.border}`,
          }}>
            {event.facility_name.toUpperCase()}
          </span>
        )}
        <span style={{
          fontSize: "0.68rem", fontWeight: 600,
          padding: "2px 7px", borderRadius: "4px",
          background: kc.bg, color: kc.text,
        }}>
          {kc.label}
        </span>
        {isCompleted && (
          <span style={{ fontSize: "0.68rem", color: "#64748b", background: "rgba(100,116,139,0.12)", border: "1px solid #334155", borderRadius: "4px", padding: "2px 7px" }}>
            ✓ Completed
          </span>
        )}
        {isDelayed && (
          <span style={{ fontSize: "0.68rem", color: "#f87171", background: "rgba(248,113,113,0.1)", border: "1px solid rgba(248,113,113,0.3)", borderRadius: "4px", padding: "2px 7px" }}>
            ⚠ Delayed
          </span>
        )}
        {event.featured && !isCompleted && (
          <span style={{ fontSize: "0.68rem", color: "#fbbf24", marginLeft: "auto" }}>★ Featured</span>
        )}
      </div>

      <div style={{ fontWeight: 600, fontSize: "0.95rem", color: "#f1f5f9", marginBottom: "0.3rem", lineHeight: 1.4 }}>
        {event.source_url ? (
          <a href={event.source_url} target="_blank" rel="noopener noreferrer"
            style={{ color: "inherit", textDecoration: "none" }}
            onMouseEnter={e => (e.currentTarget.style.color = "#a5b4fc")}
            onMouseLeave={e => (e.currentTarget.style.color = "#f1f5f9")}>
            {event.title}
          </a>
        ) : event.title}
      </div>

      {event.summary && (
        <p style={{ fontSize: "0.82rem", color: "#94a3b8", margin: "0.25rem 0 0.5rem", lineHeight: 1.55,
          display: "-webkit-box", WebkitLineClamp: 2, WebkitBoxOrient: "vertical", overflow: "hidden" } as React.CSSProperties}>
          {event.summary}
        </p>
      )}

      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginTop: "0.5rem", marginBottom: "0.5rem" }}>
        <span style={{ fontSize: "0.8rem", color: "#cbd5e1" }}>
          📅 {formatDate(event.occurs_at, event.occurs_at_confidence)}
        </span>
        {event.occurs_at_confidence === "soft" && (
          <span style={{ fontSize: "0.65rem", color: "#64748b", border: "1px solid #334155", borderRadius: "3px", padding: "1px 5px" }}>
            approx.
          </span>
        )}
      </div>

      <div style={{ display: "flex", flexWrap: "wrap", gap: "0.5rem" }}>
        {event.source_url && (
          <a href={event.source_url} target="_blank" rel="noopener noreferrer"
            style={{ fontSize: "0.73rem", color: "#6366f1", textDecoration: "none",
              background: "rgba(99,102,241,0.08)", border: "1px solid rgba(99,102,241,0.2)",
              borderRadius: "4px", padding: "3px 8px" }}>
            Source ↗
          </a>
        )}
        {portalUrls.map((entry, i) => {
          const url = typeof entry === "string" ? entry : entry.url;
          const label = typeof entry === "object" && entry.label ? entry.label : "Data Portal";
          return (
            <a key={i} href={url} target="_blank" rel="noopener noreferrer"
              style={{ fontSize: "0.73rem", color: "#4ade80", textDecoration: "none",
                background: "rgba(74,222,128,0.08)", border: "1px solid rgba(74,222,128,0.2)",
                borderRadius: "4px", padding: "3px 8px" }}>
              {label} ↗
            </a>
          );
        })}
      </div>
    </div>
  );
}

function StatPill({ icon, value, label }: { icon: string; value: number | string; label: string }) {
  return (
    <div style={{
      background: "#1e293b", border: "1px solid #334155", borderRadius: "8px",
      padding: "0.75rem 1rem", minWidth: "100px", textAlign: "center",
    }}>
      <div style={{ fontSize: "1.25rem", marginBottom: "2px" }}>{icon}</div>
      <div style={{ fontSize: "1.25rem", fontWeight: 700, color: "#f8fafc" }}>{value}</div>
      <div style={{ fontSize: "0.72rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.05em" }}>{label}</div>
    </div>
  );
}

export function CalendarContent() {
  const [events, setEvents] = useState<CalendarEvent[]>([]);
  const [stats, setStats] = useState<CalendarStats | null>(null);
  const [facilities, setFacilities] = useState<FacilityInfo[]>([]);
  const [loading, setLoading] = useState(true);

  const [activeKind, setActiveKind] = useState("");
  const [activeTrack, setActiveTrack] = useState("");
  const [activeStatus, setActiveStatus] = useState("upcoming");
  const [activeFacility, setActiveFacility] = useState("");

  const API = process.env.NEXT_PUBLIC_API_URL || "";

  useEffect(() => {
    Promise.all([
      fetch(`${API}/api/calendar/?limit=200&past_days=180&upcoming_days=730`).then(r => r.json()),
      fetch(`${API}/api/calendar/stats`).then(r => r.json()).catch(() => null),
      fetch(`${API}/api/calendar/facilities`).then(r => r.json()).catch(() => []),
    ]).then(([evData, statsData, facData]) => {
      setEvents(Array.isArray(evData) ? evData : []);
      if (statsData) setStats(statsData);
      setFacilities(Array.isArray(facData) ? facData : []);
    }).catch(() => {}).finally(() => setLoading(false));
  }, [API]);

  const filtered = useMemo(() => {
    let list = events;
    if (activeStatus === "upcoming") list = list.filter(e => e.occurrence_status === "upcoming");
    else if (activeStatus === "completed") list = list.filter(e => e.occurrence_status === "completed");
    else if (activeStatus === "delayed") list = list.filter(e => e.occurrence_status === "delayed");
    if (activeKind) list = list.filter(e => e.kind === activeKind);
    if (activeTrack) list = list.filter(e => TRACK_MAP[activeTrack]?.includes(e.kind));
    if (activeFacility) list = list.filter(e => e.facility_slug === activeFacility);
    return [...list].sort((a, b) => {
      const ta = a.occurs_at ? new Date(a.occurs_at).getTime() : Infinity;
      const tb = b.occurs_at ? new Date(b.occurs_at).getTime() : Infinity;
      return ta - tb;
    });
  }, [events, activeKind, activeTrack, activeStatus, activeFacility]);

  const upcoming30 = useMemo(() => filtered.filter(isUpcomingIn30Days), [filtered]);

  const byMonth = useMemo(() => {
    const map = new Map<string, CalendarEvent[]>();
    for (const e of filtered) {
      const key = monthKey(e.occurs_at);
      if (!map.has(key)) map.set(key, []);
      map.get(key)!.push(e);
    }
    return map;
  }, [filtered]);

  const sortedMonths = useMemo(() => sortMonthKeys(Array.from(byMonth.keys())), [byMonth]);

  const clearFilters = () => {
    setActiveKind(""); setActiveTrack(""); setActiveStatus("upcoming"); setActiveFacility("");
  };

  const hasFilters = activeKind || activeTrack || activeStatus !== "upcoming" || activeFacility;

  return (
    <div>
      <div style={{ marginBottom: "2rem" }}>
        <h2 style={{ fontSize: "1.5rem", fontWeight: 700, color: "#f8fafc", margin: 0 }}>
          📅 Astronomy Calendar
        </h2>
        <p style={{ color: "#64748b", marginTop: "0.4rem", fontSize: "0.9rem", margin: "0.4rem 0 0" }}>
          Survey data releases, proposal deadlines, and major milestones across leading observatories.
        </p>
      </div>

      {stats && (
        <div style={{ display: "flex", gap: "0.75rem", flexWrap: "wrap", marginBottom: "2rem" }}>
          <StatPill icon="📅" value={stats.total_events} label="Total Events" />
          <StatPill icon="⏳" value={stats.upcoming_events} label="Upcoming" />
          <StatPill icon="🔭" value={stats.facilities} label="Facilities" />
        </div>
      )}

      <div style={{ marginBottom: "1rem" }}>
        <div style={{ fontSize: "0.7rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: "0.5rem", fontWeight: 600 }}>Track</div>
        <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap" }}>
          <FilterChip active={!activeTrack} onClick={() => setActiveTrack("")}>All Tracks</FilterChip>
          {Object.entries(TRACK_CONFIG).map(([id, cfg]) => (
            <FilterChip key={id} active={activeTrack === id} onClick={() => { setActiveTrack(id); setActiveKind(""); }}>
              {cfg.icon} {cfg.label}
            </FilterChip>
          ))}
        </div>
      </div>

      <div style={{ marginBottom: "1rem" }}>
        <div style={{ fontSize: "0.7rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: "0.5rem", fontWeight: 600 }}>Status</div>
        <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap" }}>
          {[
            { id: "", label: "All" },
            { id: "upcoming", label: "Upcoming" },
            { id: "completed", label: "Completed" },
            { id: "delayed", label: "Delayed" },
          ].map(s => (
            <FilterChip key={s.id} active={activeStatus === s.id} onClick={() => setActiveStatus(s.id)}>
              {s.label}
            </FilterChip>
          ))}
        </div>
      </div>

      {!activeTrack && (
        <div style={{ marginBottom: "1rem" }}>
          <div style={{ fontSize: "0.7rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: "0.5rem", fontWeight: 600 }}>Event Type</div>
          <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap" }}>
            <FilterChip active={!activeKind} onClick={() => setActiveKind("")}>All Types</FilterChip>
            {Object.entries(KIND_CONFIG).filter(([k]) => k !== "news").map(([id, cfg]) => (
              <FilterChip key={id} active={activeKind === id} onClick={() => setActiveKind(id)}>
                {cfg.label}
              </FilterChip>
            ))}
          </div>
        </div>
      )}

      {facilities.length > 0 && (
        <div style={{ marginBottom: "1.5rem" }}>
          <div style={{ fontSize: "0.7rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: "0.5rem", fontWeight: 600 }}>Facility</div>
          <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap" }}>
            <FilterChip active={!activeFacility} onClick={() => setActiveFacility("")}>All Facilities</FilterChip>
            {facilities.filter(f => f.event_count > 0).map(f => {
              const fc = facilityColor(f.slug);
              return (
                <button
                  key={f.slug}
                  onClick={() => setActiveFacility(activeFacility === f.slug ? "" : f.slug)}
                  style={{
                    padding: "5px 12px", borderRadius: "999px",
                    border: `1px solid ${activeFacility === f.slug ? fc.text : fc.border}`,
                    background: activeFacility === f.slug ? fc.bg : "transparent",
                    color: fc.text, fontSize: "0.78rem", fontWeight: 600,
                    cursor: "pointer", transition: "all 0.15s", whiteSpace: "nowrap" as const,
                  }}
                >
                  {f.short_name || f.slug.toUpperCase()}
                  {f.event_count > 0 && (
                    <span style={{ marginLeft: "4px", opacity: 0.7, fontWeight: 400 }}>({f.event_count})</span>
                  )}
                </button>
              );
            })}
          </div>
        </div>
      )}

      {hasFilters && (
        <div style={{ marginBottom: "1.5rem" }}>
          <button onClick={clearFilters} style={{
            fontSize: "0.75rem", color: "#64748b", background: "transparent",
            border: "1px solid #334155", borderRadius: "4px", padding: "4px 10px", cursor: "pointer",
          }}>
            ✕ Clear filters
          </button>
          <span style={{ fontSize: "0.75rem", color: "#64748b", marginLeft: "0.75rem" }}>
            {filtered.length} event{filtered.length !== 1 ? "s" : ""} shown
          </span>
        </div>
      )}

      {loading && (
        <div style={{ textAlign: "center", padding: "4rem", color: "#475569" }}>Loading calendar…</div>
      )}

      {!loading && filtered.length === 0 && (
        <div style={{ textAlign: "center", padding: "4rem", color: "#475569" }}>
          No events match the current filters.
        </div>
      )}

      {!loading && upcoming30.length > 0 && (
        <div style={{ marginBottom: "2.5rem" }}>
          <div style={{
            background: "rgba(251,191,36,0.06)", border: "1px solid rgba(251,191,36,0.2)",
            borderRadius: "8px", padding: "0.75rem 1rem", marginBottom: "1rem",
            display: "flex", alignItems: "center", gap: "0.75rem",
          }}>
            <span style={{ fontSize: "1rem" }}>⚡</span>
            <div>
              <div style={{ fontSize: "0.875rem", fontWeight: 700, color: "#fbbf24" }}>Upcoming in 30 Days</div>
              <div style={{ fontSize: "0.75rem", color: "#94a3b8" }}>
                {upcoming30.length} event{upcoming30.length !== 1 ? "s" : ""} soon
              </div>
            </div>
          </div>
          <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
            {upcoming30.map(e => <EventCard key={e.id} event={e} />)}
          </div>
          <hr style={{ border: "none", borderTop: "1px solid #1e293b", margin: "2rem 0" }} />
        </div>
      )}

      {!loading && sortedMonths.map(month => {
        const monthEvents = byMonth.get(month)!;
        const alreadyShownIds = new Set(upcoming30.map(e => e.id));
        const rest = monthEvents.filter(e => !alreadyShownIds.has(e.id));
        if (rest.length === 0) return null;
        return (
          <div key={month} style={{ marginBottom: "2.5rem" }}>
            <h2 style={{
              fontSize: "0.85rem", fontWeight: 700, color: "#94a3b8",
              textTransform: "uppercase", letterSpacing: "0.08em",
              borderBottom: "1px solid #1e293b", paddingBottom: "0.6rem", marginBottom: "1rem",
            }}>
              {month}
            </h2>
            <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
              {rest.map(e => <EventCard key={e.id} event={e} />)}
            </div>
          </div>
        );
      })}
    </div>
  );
}
