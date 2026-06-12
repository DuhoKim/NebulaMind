"use client";
import { useEffect, useState, useCallback } from "react";
import Link from "next/link";

// ─── Types ──────────────────────────────────────────────────────────────────

interface Summary {
  current_q: number | null;
  target_q: number;
  delta_24h: number | null;
  last_commit_at: string | null;
  buddle_fallback_rate: number;
  last_raised_at: string | null;
}

interface TickPoint {
  id: number;
  t: string;
  q0: number | null;
  q1: number | null;
  delta_q: number | null;
  decision: string;
  proposal_type: string | null;
  rationale_snippet: string;
}

interface TargetRaise {
  raised_at: string;
  new_target: number;
}

interface Run {
  id: number;
  started_at: string | null;
  proposal_type: string | null;
  decision: string | null;
  q0: number | null;
  q1: number | null;
  delta_q: number | null;
  h0_struct: number | null;
  h1_struct: number | null;
  u0_median: number | null;
  u1_median: number | null;
  components_before: Record<string, number> | null;
  components_after: Record<string, number> | null;
  u1_runs: Array<Record<string, number>> | null;
  judge_rationale: string | null;
  model_judge: string | null;
  reject_reason: string | null;
}

// ─── Palette ─────────────────────────────────────────────────────────────────

const DECISION_COLOR: Record<string, string> = {
  commit: "#10b981",
  rollback: "#475569",
  gate_reject: "#f59e0b",
  guard_reject: "#f59e0b",
  skip: "#334155",
  error: "#ef4444",
};

const TYPE_COLOR: Record<string, string> = {
  claim_insert_debate: "#a855f7",
  claim_insert_subtopic: "#6366f1",
  evidence_link: "#10b981",
  hero_upgrade: "#f59e0b",
  section_rewrite: "#06b6d4",
};

const COMPONENT_KEYS = ["depth", "freshness", "balance", "hero_richness", "claim_density", "sourcing"];

// ─── Small helpers ───────────────────────────────────────────────────────────

function fmt(n: number | null | undefined, digits = 3) {
  if (n === null || n === undefined) return "—";
  return n.toFixed(digits);
}

function QBadge({ q }: { q: number | null }) {
  if (q === null || q === undefined) return <span style={{ color: "#475569" }}>—</span>;
  const color = q >= 0.78 ? "#10b981" : q >= 0.65 ? "#f59e0b" : "#ef4444";
  return <span style={{ color, fontWeight: 800, fontSize: "1.1em" }}>{q.toFixed(3)}</span>;
}

// ─── Trajectory chart ────────────────────────────────────────────────────────

function TrajectoryChart({
  ticks,
  targetRaises,
  targetQ,
}: {
  ticks: TickPoint[];
  targetRaises: TargetRaise[];
  targetQ: number;
}) {
  const W = 680;
  const H = 120;
  const PAD = { t: 12, r: 16, b: 28, l: 40 };
  const cW = W - PAD.l - PAD.r;
  const cH = H - PAD.t - PAD.b;

  const valid = ticks.filter((t) => t.q1 !== null);
  if (valid.length < 2) {
    return (
      <div style={{ color: "#475569", fontSize: "0.8rem", padding: "1rem" }}>
        Not enough data yet.
      </div>
    );
  }

  const allQ = valid.map((t) => t.q1 as number);
  const minQ = Math.min(...allQ, 0.5);
  const maxQ = Math.max(...allQ, targetQ + 0.05, 1.0);
  const qRange = maxQ - minQ || 0.1;

  const xOf = (i: number) => PAD.l + (i / (valid.length - 1)) * cW;
  const yOf = (q: number) => PAD.t + cH - ((q - minQ) / qRange) * cH;

  const linePts = valid.map((t, i) => `${xOf(i)},${yOf(t.q1 as number)}`).join(" ");
  const targetY = yOf(targetQ);

  return (
    <svg
      width={W}
      height={H}
      style={{ overflow: "visible", display: "block", maxWidth: "100%" }}
    >
      {/* Y axis labels */}
      {[minQ, (minQ + maxQ) / 2, maxQ].map((v, i) => (
        <text
          key={i}
          x={PAD.l - 4}
          y={yOf(v) + 4}
          textAnchor="end"
          fill="#475569"
          fontSize={9}
        >
          {v.toFixed(2)}
        </text>
      ))}

      {/* Target line */}
      <line
        x1={PAD.l}
        y1={targetY}
        x2={W - PAD.r}
        y2={targetY}
        stroke="#6366f1"
        strokeWidth={1}
        strokeDasharray="4 3"
        opacity={0.6}
      />
      <text x={W - PAD.r + 2} y={targetY + 4} fill="#6366f1" fontSize={8}>
        target
      </text>

      {/* Q line */}
      <polyline
        points={linePts}
        fill="none"
        stroke="#94a3b8"
        strokeWidth={1.5}
        strokeLinejoin="round"
      />

      {/* Dots: green=commit, grey=rollback/etc */}
      {valid.map((t, i) => (
        <circle
          key={t.id}
          cx={xOf(i)}
          cy={yOf(t.q1 as number)}
          r={3}
          fill={DECISION_COLOR[t.decision] || "#475569"}
          opacity={t.decision === "commit" ? 1 : 0.4}
        >
          <title>
            {t.decision} | {t.proposal_type} | Q={fmt(t.q1)} | {t.t?.slice(0, 16)} |{" "}
            {t.rationale_snippet}
          </title>
        </circle>
      ))}

      {/* Target-raise markers */}
      {targetRaises.map((e, i) => {
        // Find closest tick index by time
        const raiseMs = new Date(e.raised_at).getTime();
        let closest = 0;
        let minDiff = Infinity;
        valid.forEach((t, j) => {
          const diff = Math.abs(new Date(t.t).getTime() - raiseMs);
          if (diff < minDiff) {
            minDiff = diff;
            closest = j;
          }
        });
        return (
          <line
            key={i}
            x1={xOf(closest)}
            y1={PAD.t}
            x2={xOf(closest)}
            y2={PAD.t + cH}
            stroke="#a855f7"
            strokeWidth={1}
            strokeDasharray="2 2"
            opacity={0.7}
          />
        );
      })}
    </svg>
  );
}

// ─── Per-component sparklines ────────────────────────────────────────────────

function ComponentSparklines({ runs }: { runs: Run[] }) {
  const ordered = [...runs].reverse();
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fill, minmax(160px, 1fr))",
        gap: "0.75rem",
      }}
    >
      {COMPONENT_KEYS.map((key) => {
        const vals = ordered
          .map((r) => r.components_after?.[key] ?? r.components_before?.[key] ?? null)
          .filter((v): v is number => v !== null);
        const min = Math.min(...vals, 0);
        const max = Math.max(...vals, 1);
        const rng = max - min || 0.1;
        const W2 = 140;
        const H2 = 30;
        const pts = vals
          .map((v, i) => {
            const x = (i / Math.max(vals.length - 1, 1)) * W2;
            const y = H2 - ((v - min) / rng) * H2;
            return `${x},${y}`;
          })
          .join(" ");
        const last = vals[vals.length - 1];
        return (
          <div
            key={key}
            style={{
              background: "#1e293b",
              border: "1px solid #334155",
              borderRadius: "0.375rem",
              padding: "0.5rem 0.75rem",
            }}
          >
            <div
              style={{
                fontSize: "0.7rem",
                color: "#64748b",
                marginBottom: "0.25rem",
                textTransform: "uppercase",
                letterSpacing: "0.05em",
              }}
            >
              {key.replace(/_/g, " ")}
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
              <svg width={W2} height={H2}>
                {vals.length > 1 && (
                  <polyline
                    points={pts}
                    fill="none"
                    stroke="#6366f1"
                    strokeWidth={1.5}
                    strokeLinejoin="round"
                  />
                )}
              </svg>
              <span
                style={{
                  fontSize: "0.8rem",
                  fontWeight: 700,
                  color: last !== undefined ? "#f8fafc" : "#475569",
                  minWidth: "30px",
                }}
              >
                {last !== undefined ? last.toFixed(2) : "—"}
              </span>
            </div>
          </div>
        );
      })}
    </div>
  );
}

// ─── Judge panel ─────────────────────────────────────────────────────────────

interface JudgeEntry {
  score: number | null;
  q1: number | null;
  rationale: string | null;
  model: string | null;
  at: string | null;
}

interface JudgePanelData {
  rakon: JudgeEntry | null;
  sonnet: JudgeEntry | null;
  opus: JudgeEntry | null;
  max_divergence: number | null;
  divergence_flagged: boolean;
}

function JudgePanelWidget({ pageId }: { pageId: number }) {
  const [panel, setPanel] = useState<JudgePanelData | null>(null);

  useEffect(() => {
    fetch(`/api/autowiki/judge-panel?page_id=${pageId}`)
      .then((r) => r.json())
      .then((d) => setPanel(d))
      .catch(() => {});
  }, [pageId]);

  const judges: { key: keyof Pick<JudgePanelData, "rakon" | "sonnet" | "opus">; label: string; color: string }[] = [
    { key: "rakon", label: "Rakon (deepseek-r1)", color: "#6366f1" },
    { key: "sonnet", label: "HwaO (Sonnet)", color: "#10b981" },
    { key: "opus", label: "Kun (Opus)", color: "#f59e0b" },
  ];

  return (
    <div>
      <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap", alignItems: "flex-start" }}>
        {judges.map(({ key, label, color }) => {
          const entry = panel ? panel[key] : null;
          return (
            <div
              key={key}
              style={{
                background: "#1e293b",
                border: `1px solid ${entry ? color + "66" : "#334155"}`,
                borderRadius: "0.5rem",
                padding: "0.75rem 1.25rem",
                minWidth: "160px",
                flex: "1 1 160px",
              }}
            >
              <div style={{ fontSize: "0.68rem", color: "#64748b", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: "0.25rem" }}>
                {label}
              </div>
              {entry ? (
                <>
                  <div style={{ fontSize: "1.8rem", fontWeight: 800, color, lineHeight: 1 }}>
                    {entry.score !== null ? entry.score.toFixed(2) : "—"}
                  </div>
                  <div style={{ fontSize: "0.7rem", color: "#475569", marginTop: "0.2rem" }}>
                    Q={entry.q1 !== null ? entry.q1.toFixed(3) : "—"}
                    {entry.at && ` · ${entry.at.slice(0, 16).replace("T", " ")}`}
                  </div>
                  {entry.rationale && (
                    <div
                      style={{
                        fontSize: "0.68rem",
                        color: "#64748b",
                        marginTop: "0.4rem",
                        overflow: "hidden",
                        display: "-webkit-box",
                        WebkitLineClamp: 2,
                        WebkitBoxOrient: "vertical",
                      }}
                      title={entry.rationale}
                    >
                      {entry.rationale}
                    </div>
                  )}
                </>
              ) : (
                <div style={{ fontSize: "0.8rem", color: "#475569", marginTop: "0.25rem" }}>
                  {panel ? "No data yet" : "…"}
                </div>
              )}
            </div>
          );
        })}
      </div>
      {panel?.divergence_flagged && panel.max_divergence !== null && (
        <div
          style={{
            marginTop: "0.75rem",
            padding: "0.4rem 0.75rem",
            background: "rgba(239,68,68,0.08)",
            border: "1px solid rgba(239,68,68,0.4)",
            borderRadius: "0.375rem",
            fontSize: "0.78rem",
            color: "#ef4444",
          }}
        >
          ⚠ Judge divergence: {panel.max_divergence.toFixed(2)} pts — review scores above
        </div>
      )}
    </div>
  );
}

// ─── Kill switch ─────────────────────────────────────────────────────────────

function KillSwitch() {
  const [enabled, setEnabled] = useState<boolean | null>(null);
  const [confirming, setConfirming] = useState(false);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    fetch("/api/autowiki/kill-switch")
      .then((r) => r.json())
      .then((d) => setEnabled(d.autowiki_enabled ?? false))
      .catch(() => setEnabled(false));
  }, []);

  const toggle = useCallback(() => {
    if (!confirming) {
      setConfirming(true);
      return;
    }
    setBusy(true);
    const next = !enabled;
    fetch(`/api/autowiki/kill-switch?enabled=${next}`, { method: "POST" })
      .then((r) => r.json())
      .then((d) => {
        setEnabled(d.autowiki_enabled);
        setConfirming(false);
      })
      .catch(() => {})
      .finally(() => setBusy(false));
  }, [enabled, confirming]);

  return (
    <div
      style={{
        background: "#1e293b",
        border: `1px solid ${enabled ? "#10b981" : "#334155"}`,
        borderRadius: "0.5rem",
        padding: "1rem 1.25rem",
        display: "flex",
        alignItems: "center",
        gap: "1.5rem",
      }}
    >
      <div>
        <div style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: "0.2rem" }}>
          autowiki:enabled
        </div>
        <div
          style={{
            fontSize: "1.25rem",
            fontWeight: 800,
            color: enabled ? "#10b981" : "#ef4444",
          }}
        >
          {enabled === null ? "…" : enabled ? "ON" : "OFF"}
        </div>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "0.4rem" }}>
        <button
          onClick={toggle}
          disabled={busy || enabled === null}
          style={{
            background: confirming
              ? "#ef4444"
              : enabled
              ? "#1e293b"
              : "#10b981",
            border: `1px solid ${confirming ? "#ef4444" : enabled ? "#ef4444" : "#10b981"}`,
            color: "#f8fafc",
            borderRadius: "0.375rem",
            padding: "0.35rem 0.9rem",
            cursor: "pointer",
            fontSize: "0.8rem",
            fontWeight: 600,
          }}
        >
          {busy
            ? "Updating…"
            : confirming
            ? `Confirm: turn ${enabled ? "OFF" : "ON"}?`
            : enabled
            ? "Turn OFF"
            : "Turn ON"}
        </button>
        {confirming && (
          <button
            onClick={() => setConfirming(false)}
            style={{
              background: "transparent",
              border: "none",
              color: "#64748b",
              cursor: "pointer",
              fontSize: "0.75rem",
            }}
          >
            Cancel
          </button>
        )}
      </div>

      <div style={{ fontSize: "0.72rem", color: "#475569", maxWidth: "200px" }}>
        Flips Redis <code>autowiki:enabled</code>. Loop stops within 5 min.
      </div>
    </div>
  );
}

// ─── Run row with expandable rationale ───────────────────────────────────────

function RunRow({ run }: { run: Run }) {
  const [expanded, setExpanded] = useState(false);
  const dc = DECISION_COLOR[run.decision || ""] || "#475569";
  const tc = TYPE_COLOR[run.proposal_type || ""] || "#64748b";

  return (
    <>
      <tr
        style={{
          borderBottom: "1px solid #1e293b",
          background:
            run.decision === "commit"
              ? "rgba(16,185,129,0.04)"
              : undefined,
          cursor: run.judge_rationale ? "pointer" : "default",
        }}
        onClick={() => run.judge_rationale && setExpanded((e) => !e)}
      >
        <td style={{ padding: "0.45rem 0.6rem", color: "#475569", whiteSpace: "nowrap", fontSize: "0.75rem" }}>
          {run.started_at ? new Date(run.started_at).toLocaleString() : "—"}
        </td>
        <td style={{ padding: "0.45rem 0.6rem" }}>
          {run.proposal_type ? (
            <span
              style={{
                background: tc + "22",
                color: tc,
                borderRadius: "0.2rem",
                padding: "0.1rem 0.35rem",
                fontSize: "0.72rem",
              }}
            >
              {run.proposal_type.replace(/_/g, " ")}
            </span>
          ) : (
            <span style={{ color: "#334155" }}>—</span>
          )}
        </td>
        <td style={{ padding: "0.45rem 0.6rem" }}>
          <span style={{ color: dc, fontWeight: 700, fontSize: "0.75rem" }}>
            {run.decision || "—"}
          </span>
        </td>
        <td style={{ padding: "0.45rem 0.6rem", fontSize: "0.8rem" }}>
          <span style={{ color: "#64748b" }}>{fmt(run.q0)}</span>
          {" → "}
          <QBadge q={run.q1} />
        </td>
        <td style={{ padding: "0.45rem 0.6rem", fontSize: "0.8rem", color: "#64748b" }}>
          {fmt(run.h0_struct, 1)} → {fmt(run.h1_struct, 1)}
        </td>
        <td style={{ padding: "0.45rem 0.6rem", fontSize: "0.8rem", color: "#64748b" }}>
          {fmt(run.u0_median, 2)} → {fmt(run.u1_median, 2)}
        </td>
        <td
          style={{
            padding: "0.45rem 0.6rem",
            fontSize: "0.75rem",
            color: "#64748b",
            maxWidth: "200px",
            overflow: "hidden",
            textOverflow: "ellipsis",
            whiteSpace: "nowrap",
          }}
        >
          {run.reject_reason || (run.judge_rationale ? run.judge_rationale.slice(0, 80) + "…" : "—")}
        </td>
        <td style={{ padding: "0.45rem 0.6rem", fontSize: "0.72rem", color: "#334155" }}>
          {run.model_judge === "buddle" ? (
            <span style={{ color: "#f59e0b" }}>buddle</span>
          ) : (
            run.model_judge || "—"
          )}
        </td>
      </tr>
      {expanded && run.judge_rationale && (
        <tr style={{ background: "#0f172a" }}>
          <td
            colSpan={8}
            style={{
              padding: "0.6rem 1rem",
              fontSize: "0.8rem",
              color: "#94a3b8",
              fontStyle: "italic",
              borderBottom: "1px solid #1e293b",
            }}
          >
            <strong style={{ color: "#64748b" }}>Rationale:</strong>{" "}
            {run.judge_rationale}
          </td>
        </tr>
      )}
    </>
  );
}

// ─── Main page ────────────────────────────────────────────────────────────────

export default function AutowikiAdminPage() {
  const [summary, setSummary] = useState<Summary | null>(null);
  const [runs, setRuns] = useState<Run[]>([]);
  const [trajectory, setTrajectory] = useState<{ ticks: TickPoint[]; target_raises: TargetRaise[] }>({
    ticks: [],
    target_raises: [],
  });
  const [loading, setLoading] = useState(true);
  const PAGE_ID = 57;

  useEffect(() => {
    Promise.all([
      fetch(`/api/autowiki/summary?page_id=${PAGE_ID}`).then((r) => r.json()).catch(() => null),
      fetch(`/api/autowiki/runs?page_id=${PAGE_ID}&limit=50`).then((r) => r.json()).catch(() => []),
      fetch(`/api/autowiki/trajectory?page_id=${PAGE_ID}&limit=200`).then((r) => r.json()).catch(() => ({ ticks: [], target_raises: [] })),
    ]).then(([s, r, t]) => {
      setSummary(s);
      setRuns(Array.isArray(r) ? r : []);
      setTrajectory(t || { ticks: [], target_raises: [] });
      setLoading(false);
    });
  }, []);

  if (loading) {
    return (
      <div style={{ padding: "2rem", color: "#475569", fontFamily: "sans-serif" }}>
        Loading autowiki dashboard…
      </div>
    );
  }

  return (
    <div style={{ maxWidth: "76rem", margin: "0 auto", padding: "2rem 1rem", fontFamily: "sans-serif" }}>
      {/* Header */}
      <div style={{ marginBottom: "1.75rem" }}>
        <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: "0.4rem" }}>
          <Link href="/admin/llm" style={{ color: "#6366f1", textDecoration: "none" }}>
            ← Admin
          </Link>
        </div>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "#f8fafc", margin: 0 }}>
          ⚡ Autowiki Loop
        </h1>
        <p style={{ color: "#475569", fontSize: "0.875rem", marginTop: "0.3rem" }}>
          galaxy-evolution (page 57) · AstroSage drafts · Atom-7B gates · Rakon judges
        </p>
      </div>

      {/* ── Summary row ── */}
      <div style={{ display: "flex", gap: "1rem", marginBottom: "1.5rem", flexWrap: "wrap" }}>
        {/* Utility score — headline number per Papa's directive */}
        <div
          style={{
            background: "#1e293b",
            border: "1px solid #6366f1",
            borderRadius: "0.5rem",
            padding: "1rem 1.5rem",
            minWidth: "140px",
            textAlign: "center",
          }}
        >
          <div style={{ fontSize: "0.7rem", color: "#6366f1", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: "0.3rem" }}>
            Composite Q
          </div>
          <div style={{ fontSize: "2.5rem", fontWeight: 900, lineHeight: 1 }}>
            <QBadge q={summary?.current_q ?? null} />
          </div>
          <div style={{ fontSize: "0.7rem", color: "#475569", marginTop: "0.3rem" }}>
            target {summary?.target_q?.toFixed(2) ?? "—"}
          </div>
        </div>

        {[
          { label: "24h Δ", value: summary?.delta_24h != null ? (summary.delta_24h >= 0 ? "+" : "") + summary.delta_24h.toFixed(3) : "—", color: summary?.delta_24h != null && summary.delta_24h >= 0 ? "#10b981" : "#ef4444" },
          { label: "Last commit", value: summary?.last_commit_at ? new Date(summary.last_commit_at).toLocaleString() : "none" },
          { label: "Buddle fallback rate", value: summary?.buddle_fallback_rate != null ? (summary.buddle_fallback_rate * 100).toFixed(1) + "%" : "—", color: (summary?.buddle_fallback_rate ?? 0) > 0.1 ? "#f59e0b" : "#10b981" },
        ].map((s) => (
          <div
            key={s.label}
            style={{
              background: "#1e293b",
              border: "1px solid #334155",
              borderRadius: "0.5rem",
              padding: "0.75rem 1.25rem",
              minWidth: "130px",
            }}
          >
            <div style={{ fontSize: "0.7rem", color: "#64748b", marginBottom: "0.2rem", textTransform: "uppercase", letterSpacing: "0.06em" }}>
              {s.label}
            </div>
            <div style={{ fontSize: "1.1rem", fontWeight: 700, color: s.color || "#f8fafc" }}>
              {s.value}
            </div>
          </div>
        ))}

        <div style={{ marginLeft: "auto" }}>
          <KillSwitch />
        </div>
      </div>

      {/* ── Trajectory chart ── */}
      <div
        style={{
          background: "#1e293b",
          border: "1px solid #334155",
          borderRadius: "0.5rem",
          padding: "1rem 1.25rem",
          marginBottom: "1.5rem",
          overflowX: "auto",
        }}
      >
        <div style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: "0.5rem", textTransform: "uppercase", letterSpacing: "0.06em" }}>
          Q trajectory · green=commit · grey=rollback · purple line=target raise
        </div>
        <TrajectoryChart
          ticks={trajectory.ticks}
          targetRaises={trajectory.target_raises}
          targetQ={summary?.target_q ?? 0.78}
        />
      </div>

      {/* ── Judge panel ── */}
      <div
        style={{
          background: "#1e293b",
          border: "1px solid #334155",
          borderRadius: "0.5rem",
          padding: "1rem 1.25rem",
          marginBottom: "1.5rem",
        }}
      >
        <div style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: "0.75rem", textTransform: "uppercase", letterSpacing: "0.06em" }}>
          Judge panel · utility scores (0–10) · divergence &gt;1.5 flagged
        </div>
        <JudgePanelWidget pageId={PAGE_ID} />
      </div>

      {/* ── Per-component sparklines ── */}
      <div style={{ marginBottom: "1.5rem" }}>
        <div style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: "0.75rem", textTransform: "uppercase", letterSpacing: "0.06em" }}>
          Structural components
        </div>
        <ComponentSparklines runs={runs} />
      </div>

      {/* ── Recent ticks table ── */}
      <div>
        <div style={{ fontSize: "0.75rem", color: "#64748b", marginBottom: "0.75rem", textTransform: "uppercase", letterSpacing: "0.06em" }}>
          Recent ticks (last 50) · click row to expand rationale
        </div>
        {runs.length === 0 ? (
          <div style={{ color: "#475569", padding: "1.5rem 0" }}>No runs yet.</div>
        ) : (
          <div style={{ overflowX: "auto" }}>
            <table style={{ width: "100%", borderCollapse: "collapse", fontSize: "0.8rem" }}>
              <thead>
                <tr style={{ color: "#475569", borderBottom: "1px solid #334155" }}>
                  {["Time", "Type", "Decision", "Q0 → Q1", "Struct", "Util", "Reason / Rationale", "Judge"].map(
                    (h) => (
                      <th key={h} style={{ textAlign: "left", padding: "0.45rem 0.6rem", fontWeight: 600, fontSize: "0.72rem", textTransform: "uppercase", letterSpacing: "0.05em" }}>
                        {h}
                      </th>
                    )
                  )}
                </tr>
              </thead>
              <tbody>
                {runs.map((r) => (
                  <RunRow key={r.id} run={r} />
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
