"use client"

import { useEffect, useRef } from "react"
import { STATUS_COLORS, BAND_LABELS_LONG, BAND_COLORS, type Survey } from "./constants"
import SurveyLogo from "./SurveyLogo"

interface Props {
  survey: Survey | null
  onClose: () => void
}

export default function SurveyPeek({ survey, onClose }: Props) {
  const contentRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!survey) return
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose()
    }
    window.addEventListener("keydown", handleKeyDown)
    return () => window.removeEventListener("keydown", handleKeyDown)
  }, [survey, onClose])

  if (!survey) return null

  const status = STATUS_COLORS[survey.status]
  const bandColor = BAND_COLORS[survey.wavelength_band] ?? "#818cf8"
  const isContested = survey.linked_research_ideas_count > 0

  return (
    <div
      className="survey-sheet__backdrop"
      style={{
        position: "fixed",
        inset: 0,
        zIndex: 1000,
        background: "rgba(0, 0, 0, 0.7)",
        display: "flex",
        alignItems: "flex-end", // default bottom-sheet for mobile
        justifyContent: "center",
      }}
      onClick={onClose}
    >
      <style jsx global>{`
        .survey-sheet__backdrop {
          backdrop-filter: blur(4px);
          animation: peekFadeIn 180ms ease-out forwards;
        }
        .survey-sheet__content {
          animation: peekSlideUp 240ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        @keyframes peekFadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes peekSlideUp {
          from { transform: translateY(100%); }
          to { transform: translateY(0); }
        }
        @media (min-width: 768px) {
          .survey-sheet__backdrop {
            align-items: center !important;
          }
          .survey-sheet__content {
            animation: peekScaleIn 180ms cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
            border-radius: 12px !important;
            max-width: 540px !important;
            height: auto !important;
            max-height: 85vh !important;
          }
        }
        @keyframes peekScaleIn {
          from { opacity: 0; transform: scale(0.96); }
          to { opacity: 1; transform: scale(1); }
        }
      `}</style>

      <div
        ref={contentRef}
        className="survey-sheet__content"
        role="dialog"
        aria-modal="true"
        aria-label={`${survey.name} survey quick view`}
        style={{
          background: "#0f172a",
          border: "1px solid #334155",
          borderTopLeftRadius: "16px",
          borderTopRightRadius: "16px",
          width: "100%",
          maxHeight: "80vh",
          overflowY: "auto",
          padding: "1.5rem",
          position: "relative",
          boxShadow: "0 -10px 25px -5px rgba(0, 0, 0, 0.5), 0 20px 25px -5px rgba(0, 0, 0, 0.5)",
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Mobile Swipe Handle Drag Indicator */}
        <div
          style={{
            width: "36px",
            height: "4px",
            background: "#334155",
            borderRadius: "2px",
            margin: "-0.5rem auto 1rem auto",
            display: "block",
          }}
          className="md:hidden"
        />

        {/* Close Button */}
        <button
          onClick={onClose}
          style={{
            position: "absolute",
            top: "1rem",
            right: "1rem",
            background: "#1e293b",
            border: "1px solid #334155",
            color: "#64748b",
            fontSize: "1.1rem",
            cursor: "pointer",
            width: "28px",
            height: "28px",
            borderRadius: "50%",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            lineHeight: 1,
            transition: "all 120ms",
          }}
          className="hover:text-slate-100 hover:border-slate-500"
        >
          ×
        </button>

        {/* Header Block */}
        <div style={{ display: "flex", alignItems: "flex-start", gap: "0.75rem", marginBottom: "0.85rem", paddingRight: "1.5rem" }}>
          <SurveyLogo survey={survey} size="peek" />
          <div style={{ minWidth: 0 }}>
            <h3 style={{ fontWeight: 700, fontSize: "1.15rem", color: "#f8fafc", margin: 0, lineHeight: 1.25 }}>{survey.name}</h3>
            <p style={{ color: "#94a3b8", fontSize: "0.82rem", margin: "0.15rem 0 0", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{survey.full_name}</p>
          </div>
        </div>

        {/* Badges Block */}
        <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap", marginBottom: "1rem" }}>
          {status && (
            <span style={{
              fontSize: "0.68rem", fontWeight: 700, padding: "0.1rem 0.5rem",
              borderRadius: 999, background: status.bg, color: status.color,
              textTransform: "uppercase", letterSpacing: "0.04em"
            }}>{status.label}</span>
          )}
          <span style={{
            fontSize: "0.68rem", fontWeight: 700, padding: "0.1rem 0.5rem",
            borderRadius: 999, background: `rgba(${parseInt(bandColor.slice(1,3), 16)}, ${parseInt(bandColor.slice(3,5), 16)}, ${parseInt(bandColor.slice(5,7), 16)}, 0.12)`,
            color: bandColor, textTransform: "uppercase", letterSpacing: "0.04em",
            border: `1px solid rgba(${parseInt(bandColor.slice(1,3), 16)}, ${parseInt(bandColor.slice(3,5), 16)}, ${parseInt(bandColor.slice(5,7), 16)}, 0.25)`
          }}>
            {BAND_LABELS_LONG[survey.wavelength_band] ?? survey.wavelength_band}
          </span>
        </div>

        {/* Description / Science goals fallback */}
        <p style={{ color: "#cbd5e1", fontSize: "0.85rem", lineHeight: 1.6, marginBottom: "1.25rem" }}>
          {survey.description ? survey.description : survey.primary_science_goals}
        </p>

        {/* Facts Grid */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "0.6rem 1rem", marginBottom: "1.25rem", borderTop: "1px solid #1e293b", paddingTop: "0.85rem" }}>
          <FactRow label="Wavelength" value={survey.wavelength_range} />
          {survey.sky_coverage_deg2 != null && (
            <FactRow
              label="Sky Coverage"
              value={`${survey.sky_coverage_deg2.toLocaleString()} deg²${survey.sky_coverage_note ? ` (${survey.sky_coverage_note})` : ""}`}
            />
          )}
          {survey.redshift_range && <FactRow label="Redshift" value={survey.redshift_range} />}
          {survey.current_data_release && <FactRow label="Data Release" value={survey.current_data_release} />}
          {survey.operator && <FactRow label="Operator" value={survey.operator} />}
          {survey.data_volume && <FactRow label="Data Volume" value={survey.data_volume} />}
        </div>

        {/* Linked Research Ideas Badge/Notice */}
        {isContested && (
          <div style={{
            background: "rgba(129, 140, 248, 0.08)",
            border: "1px solid rgba(129, 140, 248, 0.2)",
            borderRadius: "6px",
            padding: "0.6rem 0.85rem",
            marginBottom: "1.25rem",
            fontSize: "0.8rem",
            color: "#a5b4fc",
            display: "flex",
            alignItems: "center",
            gap: "0.4rem"
          }}>
            <span>⚡</span>
            <span><strong>{survey.linked_research_ideas_count} Research Ideas</strong> linked to this survey.</span>
          </div>
        )}

        {/* Action Buttons */}
        <div style={{ display: "flex", gap: "0.6rem", flexWrap: "wrap", borderTop: "1px solid #1e293b", paddingTop: "1rem" }}>
          <a
            href={`/surveys/${survey.slug}`}
            style={{
              flex: "1 0 auto",
              textAlign: "center",
              background: "#3b82f6",
              color: "#ffffff",
              borderRadius: 6,
              padding: "0.45rem 1rem",
              textDecoration: "none",
              fontSize: "0.82rem",
              fontWeight: 600,
              boxShadow: "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
              transition: "background 120ms"
            }}
            className="hover:bg-blue-600"
          >
            Open full page →
          </a>
          {survey.archive_url && (
            <a
              href={survey.archive_url}
              target="_blank"
              rel="noopener noreferrer"
              style={{
                flex: "1 0 auto",
                textAlign: "center",
                background: "#1e293b",
                color: "#cbd5e1",
                border: "1px solid #334155",
                borderRadius: 6,
                padding: "0.45rem 1rem",
                textDecoration: "none",
                fontSize: "0.82rem",
                fontWeight: 600,
                transition: "all 120ms"
              }}
              className="hover:bg-slate-800 hover:text-slate-100"
            >
              Archive ↗
            </a>
          )}
          {survey.mission_url && (
            <a
              href={survey.mission_url}
              target="_blank"
              rel="noopener noreferrer"
              style={{
                flex: "1 0 auto",
                textAlign: "center",
                background: "#1e293b",
                color: "#cbd5e1",
                border: "1px solid #334155",
                borderRadius: 6,
                padding: "0.45rem 1rem",
                textDecoration: "none",
                fontSize: "0.82rem",
                fontWeight: 600,
                transition: "all 120ms"
              }}
              className="hover:bg-slate-800 hover:text-slate-100"
            >
              Mission ↗
            </a>
          )}
        </div>
      </div>
    </div>
  )
}

function FactRow({ label, value }: { label: string; value: string }) {
  return (
    <div style={{ display: "flex", gap: "0.4rem", fontSize: "0.78rem", overflow: "hidden" }}>
      <span style={{ color: "#64748b", flexShrink: 0, minWidth: "90px", fontWeight: 500 }}>{label}:</span>
      <span style={{ color: "#cbd5e1", textOverflow: "ellipsis", overflow: "hidden", whiteSpace: "nowrap" }} title={value}>{value}</span>
    </div>
  )
}
