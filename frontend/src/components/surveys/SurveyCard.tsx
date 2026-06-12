"use client"

import { STATUS_COLORS, BAND_LABELS_LONG, BAND_COLORS, type Survey } from "./constants"
import SurveyLogo from "./SurveyLogo"

interface Props {
  survey: Survey
  onOpen: (slug: string) => void
}

export default function SurveyCard({ survey, onOpen }: Props) {
  const status = STATUS_COLORS[survey.status]
  const bandColor = BAND_COLORS[survey.wavelength_band] ?? "#818cf8"

  return (
    <div
      className="survey-card"
      onClick={() => onOpen(survey.slug)}
      style={{
        background: "#1e293b",
        border: "1px solid #334155",
        borderRadius: "8px",
        padding: "1.25rem 1.5rem",
        cursor: "pointer",
        width: "100%",
        display: "flex",
        flexDirection: "column",
        gap: "0.5rem",
        transition: "border-color 150ms ease, transform 150ms ease",
        userSelect: "none",
      }}
    >
      <style jsx>{`
        .survey-card:hover {
          border-color: #3b82f6 !important;
        }
        .survey-card__row1 {
          display: flex;
          align-items: center;
          gap: "0.5rem";
          flex-wrap: wrap;
        }
        .survey-card__title {
          font-weight: 700;
          font-size: 1.05rem;
          color: #f8fafc;
        }
        .survey-card__fullname {
          color: #94a3b8;
          font-size: 0.85rem;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
          flex: 1 1 auto;
          min-width: 0;
        }
        .survey-card__badge-status {
          font-size: 0.68rem;
          font-weight: 700;
          padding: 0.1rem 0.5rem;
          border-radius: 99px;
          text-transform: uppercase;
          letter-spacing: "0.02em";
        }
        .survey-card__dot-band {
          width: 8px;
          height: 8px;
          border-radius: 50%;
          flex-shrink: 0;
        }
        .survey-card__row2-meta {
          color: #64748b;
          font-size: 0.8rem;
          display: flex;
          gap: 0.4rem;
          align-items: center;
          flex-wrap: wrap;
        }
        .survey-card__row3-goals {
          margin: 0.25rem 0;
          color: #cbd5e1;
          font-size: 0.85rem;
          line-height: 1.5;
        }
        .survey-card__row4-footer {
          display: flex;
          gap: 1rem;
          flex-wrap: wrap;
          font-size: 0.75rem;
          color: #475569;
          font-weight: 500;
          margin-top: 0.25rem;
        }
        .survey-card__ideas-count {
          color: #818cf8;
          font-weight: 600;
        }
      `}</style>

      {/* Row 1: Logo, name, status, band dot */}
      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", flexWrap: "wrap", justifyContent: "space-between" }}>
        <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", minWidth: 0, flex: "1 1 auto" }}>
          <SurveyLogo survey={survey} />
          <span className="survey-card__title">{survey.name}</span>
          <span style={{ color: "#334155" }} className="hidden sm:inline">|</span>
          <span className="survey-card__fullname">{survey.full_name}</span>
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: "0.4rem", flexShrink: 0 }}>
          {status && (
            <span
              className="survey-card__badge-status"
              style={{ background: status.bg, color: status.color }}
            >
              {status.label}
            </span>
          )}
          <span
            className="survey-card__dot-band"
            style={{ backgroundColor: bandColor }}
            title={BAND_LABELS_LONG[survey.wavelength_band] ?? survey.wavelength_band}
          />
        </div>
      </div>

      {/* Row 2: Band label, range, sky coverage, data release year */}
      <div className="survey-card__row2-meta">
        <span>{BAND_LABELS_LONG[survey.wavelength_band] ?? survey.wavelength_band}</span>
        <span>·</span>
        <span>{survey.wavelength_range}</span>
        {survey.sky_coverage_deg2 != null && (
          <>
            <span>·</span>
            <span>{survey.sky_coverage_deg2.toLocaleString()} deg²</span>
          </>
        )}
        {survey.current_data_release && (
          <>
            <span>·</span>
            <span>DR: {survey.current_data_release}</span>
          </>
        )}
      </div>

      {/* Row 3: Science goals truncated */}
      <p className="survey-card__row3-goals">
        {survey.primary_science_goals.length > 140
          ? `${survey.primary_science_goals.slice(0, 140)}…`
          : survey.primary_science_goals}
      </p>

      {/* Row 4: Archive hostname, DR year, linked ideas */}
      <div className="survey-card__row4-footer">
        {survey.dr_year && <span>Active: {survey.dr_year}</span>}
        {survey.archive_url && (() => {
          try {
            return <span>Archive: {new URL(survey.archive_url).hostname}</span>
          } catch {
            return null
          }
        })()}
        {survey.linked_research_ideas_count > 0 && (
          <span className="survey-card__ideas-count">
            ⚡ {survey.linked_research_ideas_count} Research Idea{survey.linked_research_ideas_count !== 1 ? "s" : ""}
          </span>
        )}
      </div>
    </div>
  )
}
