"use client";

import { RefObject, useCallback, useEffect, useId, useMemo, useRef, useState } from "react";
import { createPortal } from "react-dom";
import { evidenceStatusMeta } from "./evidenceStatus";
import { buildClaimSourceContradictionAtlas, buildEvidenceCardDensityMeta, buildEvidencePanelCopy, buildEvidenceVoteCockpitVisuals, buildEvidenceVoteSignal, evidenceSide, type ClaimSourceContradictionSource } from "./evidencePanelCopy";
import { buildPaperFootprintForEvidence, type PaperClaimFlightDeck, type PaperClaimFlightDeckItem, type PaperFootprintModalModel } from "./paperClaimFlightDeck";

const DEBATE_PANEL_BREAKPOINT = 768;

export interface DebateEvidenceItem {
  id: number;
  title: string;
  arxiv_id?: string | null;
  url?: string | null;
  authors?: string | null;
  year?: number | null;
  summary?: string | null;
  stance?: string | null;
  status?: string | null;
  votes_agree?: number | null;
  votes_disagree?: number | null;
  comments_count?: number | null;
  element_links?: { element_id: string | number; element_text_snapshot?: string | null }[];
  link_count?: number | null;
  relevance?: number | null;
  entailment?: number | null;
  rigor?: number | null;
  confidence?: number | null;
  quality_v2?: number | null;
}

interface DebateEvidencePanelProps {
  claimId?: number;
  panelId?: string;
  claimText: string;
  trustLevel: string;
  evidence: DebateEvidenceItem[] | null;
  loading?: boolean;
  totalElements?: number;
  onClose: () => void;
  returnFocusRef?: RefObject<HTMLElement>;
  paperFootprintsByEvidenceId?: Record<number, PaperClaimFlightDeckItem | undefined>;
}

function percent(value?: number | null): number {
  if (value == null || Number.isNaN(Number(value))) return 0;
  return Math.min(100, Math.max(0, Math.round(Number(value) * 100)));
}

function AtlasSourceLink({ source, label }: { source: ClaimSourceContradictionSource | null; label: string }) {
  if (!source) {
    return (
      <div style={{ border: "1px dashed #334155", borderRadius: "8px", padding: "0.5rem", color: "#64748b", fontSize: "0.66rem" }}>
        No {label.toLowerCase()} source mapped yet.
      </div>
    );
  }
  return (
    <a
      data-testid="contradiction-atlas-source-link"
      href={source.anchorHref}
      style={{
        display: "block",
        border: "1px solid rgba(148,163,184,0.24)",
        background: "rgba(15,23,42,0.66)",
        borderRadius: "8px",
        padding: "0.5rem 0.55rem",
        color: "#e2e8f0",
        textDecoration: "none",
      }}
    >
      <span style={{ display: "block", color: "#94a3b8", fontSize: "0.58rem", fontWeight: 850, letterSpacing: "0.08em", textTransform: "uppercase" }}>{label}</span>
      <span style={{ display: "block", fontSize: "0.7rem", fontWeight: 750, lineHeight: 1.3, marginTop: "0.18rem" }}>{source.title}</span>
      <span style={{ display: "block", color: "#64748b", fontSize: "0.62rem", marginTop: "0.18rem" }}>{source.voteLabel}{source.qualityLabel ? ` · ${source.qualityLabel}` : ""}</span>
    </a>
  );
}

function EvidenceCard({
  ev,
  paperFootprint,
  onOpenPaperFootprint,
}: {
  ev: DebateEvidenceItem;
  paperFootprint?: PaperClaimFlightDeckItem | null;
  onOpenPaperFootprint?: (ev: DebateEvidenceItem, origin: HTMLButtonElement) => void;
}) {
  const [scoreOpen, setScoreOpen] = useState(false);
  const side = evidenceSide(ev.stance);
  const accent = side === "counter" ? "#ef4444" : side === "support" ? "#22c55e" : "#94a3b8";
  const quality = ev.quality_v2;
  const statusMeta = evidenceStatusMeta(ev.status);
  const statusColor = statusMeta.tone === "green" ? "#34d399" : statusMeta.tone === "amber" ? "#fbbf24" : "#94a3b8";
  const statusBg = statusMeta.tone === "green" ? "rgba(52,211,153,0.12)" : statusMeta.tone === "amber" ? "rgba(251,191,36,0.12)" : "rgba(148,163,184,0.12)";
  const cardVoteSignal = buildEvidenceVoteSignal([ev]);
  const density = buildEvidenceCardDensityMeta(ev);

  return (
    <article
      id={`evidence-source-${ev.id}`}
      data-testid="evidence-card-density-shell"
      style={{
        scrollMarginTop: "5rem",
        border: "1px solid #334155",
        borderLeft: `3px solid ${accent}`,
        borderRadius: "9px",
        background: "linear-gradient(180deg, rgba(15,23,42,0.98), rgba(15,23,42,0.9))",
        padding: "0.52rem 0.62rem",
      }}
    >
      <div data-testid="evidence-card-density-rail" style={{ display: "flex", alignItems: "center", gap: "0.34rem", flexWrap: "wrap", marginBottom: "0.32rem" }}>
        <span style={{ color: accent, border: `1px solid ${accent}`, background: "rgba(15,23,42,0.72)", borderRadius: "999px", padding: "0.05rem 0.38rem", fontSize: "0.6rem", fontWeight: 850, textTransform: "uppercase", letterSpacing: "0.04em" }}>
          {density.sideLabel}
        </span>
        <span
          title={`claim support signal ${cardVoteSignal.supportVotes}; claim weakening signal ${cardVoteSignal.weakeningVotes}. ${cardVoteSignal.detail}`}
          style={{ color: "#cbd5e1", border: "1px solid rgba(148,163,184,0.22)", background: "rgba(30,41,59,0.54)", borderRadius: "999px", padding: "0.05rem 0.38rem", fontSize: "0.62rem", fontWeight: 760 }}
        >
          {density.voteLabel}
        </span>
        <span title={statusMeta.detail} style={{ border: `1px solid ${statusColor}`, background: statusBg, color: statusColor, borderRadius: "999px", padding: "0.05rem 0.38rem", fontSize: "0.6rem", fontWeight: 800, textTransform: "uppercase" }}>
          {statusMeta.label}
        </span>
        {density.qualityLabel ? (
          <button
            type="button"
            data-testid="evidence-card-score-toggle"
            aria-expanded={scoreOpen}
            aria-label={scoreOpen ? "Hide evidence quality breakdown" : "Show evidence quality breakdown"}
            onClick={(e) => { e.stopPropagation(); setScoreOpen((v) => !v); }}
            style={{
              marginLeft: "auto",
              border: "1px solid #334155",
              background: "#111827",
              color: quality != null && quality >= 0.8 ? "#34d399" : quality != null && quality >= 0.5 ? "#fbbf24" : "#f87171",
              borderRadius: "999px",
              padding: "0.06rem 0.42rem",
              cursor: "pointer",
              fontSize: "0.62rem",
              fontWeight: 800,
            }}
          >
            {density.qualityLabel} <span aria-hidden="true">{scoreOpen ? "▲" : "▼"}</span>
          </button>
        ) : (
          <span style={{ marginLeft: "auto", color: "#38bdf8", fontSize: "0.62rem", fontWeight: 800 }}>accepted</span>
        )}
      </div>
      <div style={{ display: "flex", alignItems: "flex-start", gap: "0.42rem" }}>
        <span style={{ marginTop: "0.24rem", width: "0.45rem", height: "0.45rem", borderRadius: "50%", background: accent, flexShrink: 0 }} />
        <div style={{ minWidth: 0, flex: 1 }}>
          {ev.url ? (
            <a href={ev.url} target="_blank" rel="noopener noreferrer" style={{ color: "#e2e8f0", textDecoration: "none", fontSize: "0.77rem", fontWeight: 700, lineHeight: 1.28 }}>
              {ev.title}
            </a>
          ) : (
            <div style={{ color: "#e2e8f0", fontSize: "0.77rem", fontWeight: 700, lineHeight: 1.28 }}>{ev.title}</div>
          )}
          <div style={{ color: "#64748b", fontSize: "0.65rem", marginTop: "0.1rem" }}>
            {ev.authors ? `${ev.authors}${ev.year ? " · " : ""}` : ""}{ev.year || ""}
          </div>
          {statusMeta.trustBlocking && (
            <p style={{ color: "#fbbf24", fontSize: "0.64rem", lineHeight: 1.35, margin: "0.24rem 0 0" }}>
              {statusMeta.detail}
            </p>
          )}
          {ev.summary && (
            <p
              data-testid="evidence-card-summary-clamp"
              style={{
                color: "#94a3b8",
                fontSize: "0.68rem",
                lineHeight: 1.38,
                margin: "0.28rem 0 0",
                display: "-webkit-box",
                WebkitLineClamp: 3,
                WebkitBoxOrient: "vertical",
                overflow: "hidden",
              }}
            >
              {ev.summary}
            </p>
          )}
          <div data-testid="evidence-card-activity-rail" style={{ color: density.hasActivity ? "#94a3b8" : "#475569", fontSize: "0.63rem", marginTop: "0.32rem" }}>
            {density.activityLabel}
          </div>
          {paperFootprint && onOpenPaperFootprint && (
            <button
              type="button"
              data-testid="paper-footprint-entry-button"
              aria-haspopup="dialog"
              aria-controls={`paper-footprint-modal-${ev.id}`}
              onClick={(e) => {
                e.preventDefault();
                e.stopPropagation();
                onOpenPaperFootprint(ev, e.currentTarget);
              }}
              style={{
                marginTop: "0.42rem",
                border: "1px solid rgba(56,189,248,0.42)",
                background: "rgba(14,165,233,0.12)",
                color: "#bae6fd",
                borderRadius: "999px",
                padding: "0.18rem 0.52rem",
                cursor: "pointer",
                fontSize: "0.64rem",
                fontWeight: 850,
              }}
            >
              View paper footprint
            </button>
          )}
          {scoreOpen && (
            <div style={{ marginTop: "0.45rem", borderTop: "1px solid #1e293b", paddingTop: "0.4rem" }}>
              {[
                ["Relevance", ev.relevance],
                ["Entailment", ev.entailment],
                ["Rigor", ev.rigor],
                ["Confidence", ev.confidence],
              ].map(([label, raw]) => {
                const p = percent(raw as number | null | undefined);
                return (
                  <div key={label as string} style={{ display: "grid", gridTemplateColumns: "6rem 1fr 2rem", gap: "0.4rem", alignItems: "center", marginBottom: "0.25rem" }}>
                    <span style={{ color: "#94a3b8", fontSize: "0.66rem" }}>{label as string}</span>
                    <span style={{ display: "block", height: "0.28rem", background: "#1e293b", borderRadius: "999px", overflow: "hidden" }}>
                      <span style={{ display: "block", width: `${p}%`, height: "100%", background: "#818cf8" }} />
                    </span>
                    <span style={{ color: "#64748b", fontSize: "0.64rem", textAlign: "right" }}>{p}%</span>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </article>
  );
}

export default function DebateEvidencePanel({
  claimId,
  panelId,
  claimText,
  trustLevel,
  evidence,
  loading = false,
  totalElements = 0,
  onClose,
  returnFocusRef,
  paperFootprintsByEvidenceId,
}: DebateEvidencePanelProps) {
  const [isNarrow, setIsNarrow] = useState(false);
  const [mounted, setMounted] = useState(false);
  const [selectedPaperFootprint, setSelectedPaperFootprint] = useState<PaperFootprintModalModel | null>(null);
  const closeButtonRef = useRef<HTMLButtonElement | null>(null);
  const paperFootprintCloseButtonRef = useRef<HTMLButtonElement | null>(null);
  const paperFootprintReturnFocusRef = useRef<HTMLButtonElement | null>(null);
  const isContested = ["debated", "challenged"].includes(trustLevel);
  const fallbackPanelId = useId();
  const evidencePanelTitle = isContested ? "Debate map" : "Evidence map";
  const evidencePanelNoun = isContested ? "debate map" : "evidence map";
  const evidencePanelBaseId = panelId || (claimId ? `claim-evidence-panel-${claimId}` : `evidence-panel-dialog-${fallbackPanelId}`);
  const evidencePanelHeadingId = `${evidencePanelBaseId}-heading`;
  const evidencePanelHintId = `${evidencePanelBaseId}-keyboard-hint`;
  const paperFootprintHeadingId = selectedPaperFootprint ? `paper-footprint-modal-${selectedPaperFootprint.evidenceId}-heading` : undefined;
  const paperFootprintDescriptionId = selectedPaperFootprint ? `paper-footprint-modal-${selectedPaperFootprint.evidenceId}-description` : undefined;
  const paperFootprintDeck = useMemo(() => ({
    items: Object.values(paperFootprintsByEvidenceId ?? {}).filter((item): item is PaperClaimFlightDeckItem => Boolean(item)),
  } as PaperClaimFlightDeck), [paperFootprintsByEvidenceId]);

  const closePaperFootprint = useCallback(() => {
    const origin = paperFootprintReturnFocusRef.current;
    setSelectedPaperFootprint(null);
    window.setTimeout(() => origin?.focus(), 0);
  }, []);

  const openPaperFootprint = useCallback((ev: DebateEvidenceItem, origin: HTMLButtonElement) => {
    const footprint = buildPaperFootprintForEvidence(paperFootprintDeck, ev.id, {
      claimId,
      stance: ev.stance,
      status: ev.status,
    });
    if (!footprint) return;
    paperFootprintReturnFocusRef.current = origin;
    setSelectedPaperFootprint(footprint);
  }, [claimId, paperFootprintDeck]);

  const closePanel = useCallback(() => {
    setSelectedPaperFootprint(null);
    onClose();
    window.requestAnimationFrame(() => returnFocusRef?.current?.focus());
  }, [onClose, returnFocusRef]);

  useEffect(() => {
    setMounted(true);
    const priorOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    const focusTimer = paperFootprintReturnFocusRef.current ? undefined : window.setTimeout(() => closeButtonRef.current?.focus(), 0);
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        if (selectedPaperFootprint) {
          event.preventDefault();
          event.stopPropagation();
          closePaperFootprint();
          return;
        }
        closePanel();
      }
    };
    document.addEventListener("keydown", closeOnEscape);
    return () => {
      window.clearTimeout(focusTimer);
      document.removeEventListener("keydown", closeOnEscape);
      document.body.style.overflow = priorOverflow;
    };
  }, [closePanel, closePaperFootprint, selectedPaperFootprint]);

  useEffect(() => {
    const check = () => setIsNarrow(window.innerWidth < DEBATE_PANEL_BREAKPOINT);
    check();
    window.addEventListener("resize", check);
    return () => window.removeEventListener("resize", check);
  }, []);

  useEffect(() => {
    if (!selectedPaperFootprint) return;
    const focusTimer = window.setTimeout(() => paperFootprintCloseButtonRef.current?.focus(), 0);
    return () => window.clearTimeout(focusTimer);
  }, [selectedPaperFootprint]);

  const grouped = useMemo(() => {
    const support: DebateEvidenceItem[] = [];
    const counter: DebateEvidenceItem[] = [];
    const neutral: DebateEvidenceItem[] = [];
    for (const ev of evidence || []) {
      const side = evidenceSide(ev.stance);
      if (side === "support") support.push(ev);
      else if (side === "counter") counter.push(ev);
      else neutral.push(ev);
    }
    return { support, counter, neutral };
  }, [evidence]);

  const evidenceCopy = useMemo(
    () => buildEvidencePanelCopy(evidence || [], trustLevel),
    [evidence, trustLevel],
  );
  const voteSignal = useMemo(() => buildEvidenceVoteSignal(evidence || []), [evidence]);
  const voteVisuals = useMemo(() => buildEvidenceVoteCockpitVisuals(voteSignal), [voteSignal]);
  const contradictionAtlas = useMemo(() => buildClaimSourceContradictionAtlas(evidence || []), [evidence]);
  const total = evidenceCopy.total;
  const supportPct = total ? Math.round((grouped.support.length / total) * 100) : 0;
  const counterPct = total ? Math.round((grouped.counter.length / total) * 100) : 0;
  const voteSignalColor = voteSignal.verdict === "net_support"
    ? "#22c55e"
    : voteSignal.verdict === "net_weakening"
      ? "#ef4444"
      : voteSignal.verdict === "split"
        ? "#fbbf24"
        : "#94a3b8";

  if (!mounted) return null;

  return createPortal(
    <>
      <div
        onClick={(e) => { e.stopPropagation(); closePanel(); }}
        style={{
          position: "fixed",
          inset: 0,
          zIndex: 139,
          background: "rgba(2,6,23,0.58)",
        }}
        aria-hidden="true"
      />
      <section
        id={panelId}
        data-testid="evidence-panel-dialog"
        role="dialog"
        aria-modal="true"
        aria-labelledby={evidencePanelHeadingId}
        aria-describedby={evidencePanelHintId}
        onClick={(e) => e.stopPropagation()}
      style={{
        position: "fixed",
        top: isNarrow ? "3rem" : "50%",
        left: isNarrow ? "0.75rem" : "50%",
        right: isNarrow ? "0.75rem" : undefined,
        transform: isNarrow ? undefined : "translate(-50%, -50%)",
        zIndex: 140,
        width: isNarrow ? "auto" : "min(46rem, 94vw)",
        maxHeight: isNarrow ? "calc(100vh - 4.5rem)" : "min(38rem, 82vh)",
        overflowY: "auto",
        background: "#111827",
        border: "1px solid #334155",
        borderLeft: `3px solid ${trustLevel === "challenged" ? "#ef4444" : "#f97316"}`,
        borderRadius: "8px",
        padding: "0.9rem",
        boxShadow: "0 18px 44px rgba(0,0,0,0.55)",
        display: "block",
        whiteSpace: "normal",
        color: "#94a3b8",
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", gap: "0.75rem", alignItems: "flex-start", marginBottom: "0.65rem" }}>
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: "0.45rem", flexWrap: "wrap" }}>
            <span id={evidencePanelHeadingId} style={{ color: "#f8fafc", fontWeight: 750, fontSize: "0.86rem" }}>
              {evidencePanelTitle}
            </span>
            <span style={{ color: "#f97316", border: "1px solid rgba(249,115,22,0.45)", background: "rgba(249,115,22,0.12)", borderRadius: "999px", padding: "0.08rem 0.45rem", fontSize: "0.64rem", fontWeight: 750, textTransform: "uppercase" }}>
              {trustLevel}
            </span>
            {claimId && <span style={{ color: "#64748b", fontSize: "0.68rem" }}>claim #{claimId}</span>}
          </div>
          <p style={{ margin: "0.35rem 0 0", color: "#cbd5e1", fontSize: "0.75rem", lineHeight: 1.45 }}>
            {claimText}
          </p>
          <p id={evidencePanelHintId} style={{ margin: "0.32rem 0 0", color: "#94a3b8", fontSize: "0.68rem", lineHeight: 1.4 }}>
            Press Escape to close this {evidencePanelNoun}.
          </p>
        </div>
        <button
          type="button"
          ref={closeButtonRef}
          onClick={(e) => { e.stopPropagation(); closePanel(); }}
          style={{ border: "1px solid #334155", background: "#0f172a", color: "#cbd5e1", cursor: "pointer", fontSize: "1rem", lineHeight: 1, width: "2.75rem", height: "2.75rem", borderRadius: "999px", flexShrink: 0 }}
          aria-label="Close evidence panel"
        >
          x
        </button>
      </div>

      {total > 0 && evidenceCopy.hasDirectionalStance ? (
        <div style={{ display: "grid", gridTemplateColumns: isNarrow ? "1fr 1fr" : "1fr auto 1fr", gap: "0.65rem", alignItems: "center", marginBottom: "0.8rem" }}>
          <div style={{ textAlign: isNarrow ? "left" : "right", color: "#22c55e", fontSize: "0.7rem", fontWeight: 750 }}>supporting {grouped.support.length}</div>
          <div style={{ width: isNarrow ? "100%" : "9rem", height: "0.55rem", background: "#1e293b", borderRadius: "999px", overflow: "hidden", display: "flex", gridColumn: isNarrow ? "1 / -1" : undefined, gridRow: isNarrow ? 2 : undefined }} title={`${supportPct}% supporting, ${counterPct}% countering`}>
            <span style={{ width: `${supportPct}%`, background: "#22c55e" }} />
            <span style={{ width: `${counterPct}%`, background: "#ef4444" }} />
            <span style={{ flex: 1, background: "#64748b" }} />
          </div>
          <div style={{ color: "#ef4444", fontSize: "0.7rem", fontWeight: 750, textAlign: isNarrow ? "right" : "left" }}>countering {grouped.counter.length}</div>
        </div>
      ) : total > 0 ? (
        <div
          data-testid="evidence-panel-neutral-summary"
          style={{ border: "1px solid #334155", background: "rgba(148,163,184,0.09)", borderRadius: "6px", color: "#cbd5e1", fontSize: "0.72rem", lineHeight: 1.45, padding: "0.6rem 0.7rem", marginBottom: "0.8rem" }}
        >
          {evidenceCopy.neutralOnlySummary}
        </div>
      ) : null}

      {total > 0 && (
        <section
          data-testid="claim-source-contradiction-atlas"
          aria-label="Claim-to-source contradiction atlas"
          style={{
            border: `1px solid ${contradictionAtlas.hasContradiction ? "#f97316" : "#334155"}`,
            borderLeft: `3px solid ${contradictionAtlas.hasContradiction ? "#f97316" : "#64748b"}`,
            background: "linear-gradient(135deg, rgba(15,23,42,0.95), rgba(30,41,59,0.66))",
            borderRadius: "12px",
            padding: "0.76rem 0.82rem",
            marginBottom: "0.9rem",
          }}
        >
          <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap" }}>
            <div>
              <div style={{ color: "#fbbf24", fontSize: "0.62rem", fontWeight: 900, letterSpacing: "0.12em", textTransform: "uppercase" }}>
                Claim-to-source contradiction atlas
              </div>
              <div style={{ color: "#f8fafc", fontSize: "0.88rem", fontWeight: 850, lineHeight: 1.25, marginTop: "0.22rem" }}>
                {contradictionAtlas.headline}
              </div>
              <div style={{ color: "#94a3b8", fontSize: "0.68rem", lineHeight: 1.4, marginTop: "0.22rem", maxWidth: "34rem" }}>
                {contradictionAtlas.summary}
              </div>
            </div>
            <span
              data-testid="contradiction-atlas-tension-badge"
              style={{ color: contradictionAtlas.hasContradiction ? "#f97316" : "#94a3b8", border: `1px solid ${contradictionAtlas.hasContradiction ? "#f97316" : "#64748b"}`, background: "rgba(15,23,42,0.68)", borderRadius: "999px", padding: "0.12rem 0.5rem", fontSize: "0.64rem", fontWeight: 850, whiteSpace: "nowrap" }}
            >
              tension {contradictionAtlas.tensionScore}%
            </span>
          </div>
          <div
            data-testid="contradiction-atlas-lane-grid"
            style={{ display: "grid", gridTemplateColumns: isNarrow ? "1fr" : "repeat(3, minmax(0, 1fr))", gap: "0.45rem", marginTop: "0.62rem" }}
          >
            {contradictionAtlas.lanes.map((lane) => (
              <div key={lane.kind} style={{ border: `1px solid ${lane.color}`, background: lane.background, borderRadius: "9px", padding: "0.48rem 0.55rem" }}>
                <div style={{ color: lane.color, fontSize: "0.92rem", fontWeight: 900, lineHeight: 1 }}>{lane.count.toLocaleString()}</div>
                <div style={{ color: "#cbd5e1", fontSize: "0.62rem", fontWeight: 800, letterSpacing: "0.07em", textTransform: "uppercase", marginTop: "0.18rem" }}>{lane.label}</div>
                <div style={{ color: "#94a3b8", fontSize: "0.62rem", marginTop: "0.1rem" }}>{lane.percent}% of mapped sources</div>
              </div>
            ))}
          </div>
          <div style={{ display: "grid", gridTemplateColumns: isNarrow ? "1fr" : "1fr 1fr", gap: "0.5rem", marginTop: "0.62rem" }}>
            <AtlasSourceLink source={contradictionAtlas.primarySupport} label="Representative support" />
            <AtlasSourceLink source={contradictionAtlas.primaryCounter} label="Representative counter" />
          </div>
        </section>
      )}

      {total > 0 && (
        <div
          data-testid="evidence-vote-signal"
          aria-label="At-a-glance vote balance"
          style={{
            border: `1px solid ${voteSignalColor}`,
            borderLeft: `3px solid ${voteSignalColor}`,
            background: "linear-gradient(135deg, rgba(15,23,42,0.92), rgba(30,41,59,0.74))",
            borderRadius: "12px",
            padding: "0.78rem 0.82rem",
            marginBottom: "0.9rem",
            boxShadow: "0 12px 30px rgba(2,6,23,0.24)",
          }}
        >
          <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: "0.75rem", flexWrap: "wrap" }}>
            <div>
              <div style={{ color: "#a5b4fc", fontSize: "0.62rem", fontWeight: 900, letterSpacing: "0.12em", textTransform: "uppercase" }}>
                {voteVisuals.eyebrow}
              </div>
              <div style={{ color: "#f8fafc", fontSize: "0.9rem", fontWeight: 850, marginTop: "0.2rem", lineHeight: 1.25 }}>
                Evidence vote cockpit
              </div>
              <div style={{ color: "#94a3b8", fontSize: "0.68rem", lineHeight: 1.4, marginTop: "0.22rem" }}>
                {voteVisuals.dominantLabel}
              </div>
            </div>
            <span style={{ color: voteSignalColor, border: `1px solid ${voteSignalColor}`, background: "rgba(15,23,42,0.68)", borderRadius: "999px", padding: "0.12rem 0.5rem", fontSize: "0.64rem", fontWeight: 850, whiteSpace: "nowrap" }}>
              {voteSignal.verdictLabel}
            </span>
          </div>
          <div style={{ color: "#e2e8f0", fontSize: "0.74rem", fontWeight: 750, marginTop: "0.58rem" }}>
            {voteVisuals.summary}
          </div>
          <div
            data-testid="evidence-vote-balance-bar"
            aria-label={voteVisuals.summary}
            style={{ display: "flex", height: "0.62rem", overflow: "hidden", borderRadius: "999px", background: "rgba(100,116,139,0.22)", border: "1px solid rgba(148,163,184,0.16)", marginTop: "0.58rem" }}
          >
            {voteVisuals.segments.map((segment) => (
              <span
                key={segment.kind}
                title={`${segment.label}: ${segment.count.toLocaleString()} (${segment.percent}%)`}
                style={{
                  width: `${segment.percent}%`,
                  minWidth: segment.count > 0 ? "0.45rem" : 0,
                  background: segment.color,
                }}
              />
            ))}
          </div>
          <div data-testid="evidence-vote-metric-grid" style={{ display: "grid", gridTemplateColumns: isNarrow ? "1fr" : "repeat(3, minmax(0, 1fr))", gap: "0.45rem", marginTop: "0.62rem" }}>
            {voteVisuals.segments.map((segment) => (
              <div key={segment.kind} style={{ border: `1px solid ${segment.color}`, background: segment.background, borderRadius: "9px", padding: "0.48rem 0.55rem" }}>
                <div style={{ color: segment.color, fontSize: "0.9rem", fontWeight: 900, lineHeight: 1 }}>{segment.count.toLocaleString()}</div>
                <div style={{ color: "#cbd5e1", fontSize: "0.62rem", fontWeight: 800, letterSpacing: "0.07em", textTransform: "uppercase", marginTop: "0.18rem" }}>{segment.label}</div>
                <div style={{ color: "#94a3b8", fontSize: "0.62rem", marginTop: "0.1rem" }}>{segment.percent}% of counted votes</div>
              </div>
            ))}
          </div>
          <details style={{ marginTop: "0.55rem", color: "#94a3b8", fontSize: "0.66rem", lineHeight: 1.45 }}>
            <summary style={{ cursor: "pointer", color: "#cbd5e1", fontWeight: 750 }}>How counted votes map to the claim signal</summary>
            <div style={{ marginTop: "0.32rem" }}>{voteSignal.detail}</div>
          </details>
        </div>
      )}

      {totalElements > 0 && (
        <div style={{ color: "#64748b", fontSize: "0.66rem", marginBottom: "0.7rem" }}>
          linked across {totalElements} claim element{totalElements !== 1 ? "s" : ""}
        </div>
      )}

      {loading && <div style={{ color: "#64748b", fontSize: "0.75rem" }}>Loading evidence...</div>}
      {!loading && total === 0 && <div style={{ color: "#64748b", fontSize: "0.75rem" }}>No detailed papers linked yet.</div>}

      {!loading && total > 0 && (
        evidenceCopy.hasDirectionalStance ? (
          <div style={{ display: "grid", gridTemplateColumns: isNarrow ? "1fr" : "minmax(0, 1fr) minmax(0, 1fr)", gap: "0.75rem" }}>
            <div>
              <div style={{ color: "#22c55e", fontSize: "0.68rem", fontWeight: 750, textTransform: "uppercase", letterSpacing: "0.05em", marginBottom: "0.45rem" }}>Supporting evidence</div>
              <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
                {grouped.support.length > 0 ? grouped.support.map((ev) => <EvidenceCard key={ev.id} ev={ev} paperFootprint={paperFootprintsByEvidenceId?.[ev.id]} onOpenPaperFootprint={openPaperFootprint} />) : (
                  <div style={{ border: "1px dashed #334155", borderRadius: "6px", padding: "0.7rem", color: "#64748b", fontSize: "0.7rem" }}>No supporting evidence recorded.</div>
                )}
              </div>
            </div>
            <div>
              <div style={{ color: "#ef4444", fontSize: "0.68rem", fontWeight: 750, textTransform: "uppercase", letterSpacing: "0.05em", marginBottom: "0.45rem" }}>Countering evidence</div>
              <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
                {grouped.counter.length > 0 ? grouped.counter.map((ev) => <EvidenceCard key={ev.id} ev={ev} paperFootprint={paperFootprintsByEvidenceId?.[ev.id]} onOpenPaperFootprint={openPaperFootprint} />) : (
                  <div style={{ border: "1px dashed #334155", borderRadius: "6px", padding: "0.7rem", color: "#64748b", fontSize: "0.7rem" }}>No countering evidence recorded.</div>
                )}
                {grouped.neutral.length > 0 && (
                  <div style={{ marginTop: "0.35rem" }}>
                    <div style={{ color: "#94a3b8", fontSize: "0.66rem", fontWeight: 750, marginBottom: "0.35rem" }}>Neutral or unresolved</div>
                    <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
                      {grouped.neutral.map((ev) => <EvidenceCard key={ev.id} ev={ev} paperFootprint={paperFootprintsByEvidenceId?.[ev.id]} onOpenPaperFootprint={openPaperFootprint} />)}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        ) : (
          <div>
            <div style={{ color: "#94a3b8", fontSize: "0.68rem", fontWeight: 750, textTransform: "uppercase", letterSpacing: "0.05em", marginBottom: "0.45rem" }}>Linked paper sources</div>
            <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
              {grouped.neutral.map((ev) => <EvidenceCard key={ev.id} ev={ev} paperFootprint={paperFootprintsByEvidenceId?.[ev.id]} onOpenPaperFootprint={openPaperFootprint} />)}
            </div>
          </div>
        )
      )}
      </section>
      {selectedPaperFootprint && (
        <>
          <div
            onClick={(e) => { e.stopPropagation(); closePaperFootprint(); }}
            style={{
              position: "fixed",
              inset: 0,
              zIndex: 149,
              background: "rgba(2,6,23,0.42)",
            }}
            aria-hidden="true"
          />
          <section
            id={`paper-footprint-modal-${selectedPaperFootprint.evidenceId}`}
            data-testid="paper-footprint-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby={paperFootprintHeadingId}
            aria-describedby={paperFootprintDescriptionId}
            onClick={(e) => e.stopPropagation()}
            style={{
              position: "fixed",
              top: isNarrow ? "3.6rem" : "50%",
              left: isNarrow ? "0.8rem" : "50%",
              right: isNarrow ? "0.8rem" : undefined,
              transform: isNarrow ? undefined : "translate(-50%, -50%)",
              zIndex: 150,
              width: isNarrow ? "auto" : "min(42rem, 92vw)",
              maxHeight: isNarrow ? "calc(100vh - 5rem)" : "min(34rem, 78vh)",
              overflowY: "auto",
              background: "linear-gradient(135deg, #0f172a, #111827)",
              border: "1px solid rgba(56,189,248,0.42)",
              borderLeft: "3px solid #38bdf8",
              borderRadius: "12px",
              padding: "0.95rem",
              boxShadow: "0 24px 54px rgba(0,0,0,0.58)",
              color: "#cbd5e1",
            }}
          >
            <div style={{ display: "flex", justifyContent: "space-between", gap: "0.85rem", alignItems: "flex-start" }}>
              <div>
                <div style={{ color: "#67e8f9", fontSize: "0.62rem", fontWeight: 900, letterSpacing: "0.12em", textTransform: "uppercase" }}>
                  Paper footprint on this page
                </div>
                <h2 id={paperFootprintHeadingId} style={{ margin: "0.18rem 0 0", color: "#f8fafc", fontSize: "0.98rem", lineHeight: 1.28 }}>
                  {selectedPaperFootprint.title}
                </h2>
                <p id={paperFootprintDescriptionId} style={{ margin: "0.35rem 0 0", color: "#bae6fd", fontSize: "0.72rem", lineHeight: 1.45 }}>
                  {selectedPaperFootprint.headline}. {selectedPaperFootprint.currentStanceLabel}. Paper footprint is shown on this page only and is not a final verdict.
                </p>
              </div>
              <button
                ref={paperFootprintCloseButtonRef}
                type="button"
                data-testid="paper-footprint-close"
                aria-label="Close paper footprint"
                onClick={(e) => { e.stopPropagation(); closePaperFootprint(); }}
                style={{ border: "1px solid #334155", background: "#0f172a", color: "#cbd5e1", cursor: "pointer", fontSize: "1rem", lineHeight: 1, width: "2.5rem", height: "2.5rem", borderRadius: "999px", flexShrink: 0 }}
              >
                x
              </button>
            </div>
            <div style={{ display: "flex", flexWrap: "wrap", gap: "0.38rem", marginTop: "0.68rem" }}>
              <span style={{ color: "#67e8f9", border: "1px solid rgba(103,232,249,0.34)", background: "rgba(14,165,233,0.12)", borderRadius: "999px", padding: "0.08rem 0.44rem", fontSize: "0.62rem", fontWeight: 850 }}>
                {selectedPaperFootprint.paperLabel}
              </span>
              <span style={{ color: "#94a3b8", border: "1px solid rgba(148,163,184,0.24)", background: "rgba(15,23,42,0.66)", borderRadius: "999px", padding: "0.08rem 0.44rem", fontSize: "0.62rem", fontWeight: 850 }}>
                {selectedPaperFootprint.rankLabel}
              </span>
              <span style={{ color: "#fbbf24", border: "1px solid rgba(251,191,36,0.34)", background: "rgba(251,191,36,0.12)", borderRadius: "999px", padding: "0.08rem 0.44rem", fontSize: "0.62rem", fontWeight: 850, textTransform: "uppercase" }}>
                {selectedPaperFootprint.currentStatusLabel}
              </span>
            </div>
            <p style={{ margin: "0.58rem 0 0", color: "#94a3b8", fontSize: "0.7rem", lineHeight: 1.45 }}>
              {selectedPaperFootprint.byline} · {selectedPaperFootprint.locator}
            </p>
            <p style={{ margin: "0.52rem 0 0", color: "#cbd5e1", fontSize: "0.72rem", lineHeight: 1.48 }}>
              {selectedPaperFootprint.summary}
            </p>
            <div style={{ display: "flex", flexWrap: "wrap", gap: "0.45rem", marginTop: "0.72rem" }}>
              {selectedPaperFootprint.externalHref && (
                <a data-testid="paper-footprint-open-paper" href={selectedPaperFootprint.externalHref} target="_blank" rel="noopener noreferrer" style={{ color: "#e0f2fe", border: "1px solid rgba(56,189,248,0.42)", background: "rgba(14,165,233,0.12)", borderRadius: "999px", padding: "0.2rem 0.58rem", fontSize: "0.64rem", fontWeight: 850, textDecoration: "none" }}>
                  Open paper
                </a>
              )}
              {selectedPaperFootprint.sourceIndexHref && (
                <a data-testid="paper-footprint-source-index-link" href={selectedPaperFootprint.sourceIndexHref} style={{ color: "#bfdbfe", border: "1px solid rgba(59,130,246,0.3)", background: "rgba(59,130,246,0.1)", borderRadius: "999px", padding: "0.2rem 0.58rem", fontSize: "0.64rem", fontWeight: 850, textDecoration: "none" }}>
                  Open source index
                </a>
              )}
            </div>
            <div style={{ display: "grid", gap: "0.45rem", marginTop: "0.78rem" }}>
              {selectedPaperFootprint.claimRows.map((row) => {
                const toneColor = row.tone === "counter" || row.tone === "counter-pressure" ? "#fb923c" : row.tone === "support" ? "#34d399" : "#93c5fd";
                return (
                  <a
                    key={row.claimId}
                    data-testid="paper-footprint-claim-row"
                    href={row.href}
                    onClick={(e) => { e.stopPropagation(); closePaperFootprint(); }}
                    style={{ display: "block", color: "#e2e8f0", textDecoration: "none", border: `1px solid ${row.isCurrentClaim ? toneColor : "rgba(148,163,184,0.22)"}`, background: row.isCurrentClaim ? "rgba(14,165,233,0.14)" : "rgba(15,23,42,0.62)", borderRadius: "10px", padding: "0.58rem 0.64rem" }}
                  >
                    <span style={{ display: "flex", flexWrap: "wrap", gap: "0.32rem", alignItems: "center", marginBottom: "0.28rem" }}>
                      <span style={{ color: toneColor, border: `1px solid ${toneColor}`, background: "rgba(15,23,42,0.62)", borderRadius: "999px", padding: "0.04rem 0.38rem", fontSize: "0.6rem", fontWeight: 850 }}>
                        {row.relationLabel}
                      </span>
                      <span style={{ color: "#94a3b8", fontSize: "0.62rem", fontWeight: 760 }}>
                        claim #{row.claimId} · {row.trustLevel} · {row.sectionLabel}
                      </span>
                    </span>
                    <span style={{ display: "block", color: "#cbd5e1", fontSize: "0.72rem", lineHeight: 1.42 }}>
                      {row.claimText}
                    </span>
                  </a>
                );
              })}
            </div>
            <p style={{ margin: "0.76rem 0 0", color: "#64748b", fontSize: "0.66rem", lineHeight: 1.42 }}>
              {selectedPaperFootprint.scopeCaveat}
            </p>
          </section>
        </>
      )}
    </>,
    document.body,
  );
}
