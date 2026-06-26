"use client";

import { useEffect, useMemo, useState } from "react";
import SurveysView from "@/components/surveys/SurveysView";
import { BAND_LABELS_LONG, type Survey } from "@/components/surveys/constants";

export default function SurveysPage() {
  const [surveys, setSurveys] = useState<Survey[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/surveys")
      .then(r => r.ok ? r.json() : { surveys: [] })
      .then(d => { setSurveys(d.surveys ?? []); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const stats = useMemo(() => {
    const bandCount = new Set(surveys.map(s => s.wavelength_band).filter(Boolean)).size;
    const activeCount = surveys.filter(s => s.status === "operational" || s.status === "commissioning").length;
    const archivalCount = surveys.filter(s => s.status === "retired").length;
    const releaseCount = surveys.filter(s => Boolean(s.current_data_release)).length;
    return { bandCount, activeCount, archivalCount, releaseCount };
  }, [surveys]);

  return (
    <div style={{ padding: "2rem 1.5rem" }}>
      <style jsx>{`
        .survey-page__header {
          margin-bottom: 1.5rem;
        }
        .survey-page__title {
          font-size: clamp(1.5rem, 4vw, 2.25rem);
          font-weight: 700;
          color: #f8fafc;
          margin: 0 0 0.5rem;
        }
        .survey-page__subtitle {
          color: #94a3b8;
          font-size: 1rem;
          line-height: 1.6;
          max-width: 820px;
          margin: 0;
        }
        .survey-page__stats {
          display: flex;
          flex-wrap: wrap;
          gap: 0.55rem;
          margin-top: 1rem;
        }
        .survey-page__stat {
          display: inline-flex;
          align-items: baseline;
          gap: 0.35rem;
          padding: 0.45rem 0.65rem;
          border: 1px solid #1e293b;
          border-radius: 999px;
          background: rgba(15, 23, 42, 0.72);
          color: #cbd5e1;
          font-size: 0.78rem;
          white-space: nowrap;
        }
        .survey-page__stat strong {
          color: #f8fafc;
          font-size: 0.86rem;
        }
      `}</style>

      <div className="survey-page__header">
        <h1 className="survey-page__title">{"Astronomical Surveys & Facilities"}</h1>
        <p className="survey-page__subtitle">
          {surveys.length > 0
            ? `${surveys.length} observational programs, facilities, and survey data products anchoring research on NebulaMind.`
            : "Observational programs, facilities, and survey data products anchoring research on NebulaMind."}
        </p>
        {surveys.length > 0 && (
          <div className="survey-page__stats" aria-label="Survey atlas summary">
            <span className="survey-page__stat"><strong>{surveys.length}</strong> total</span>
            <span className="survey-page__stat"><strong>{stats.activeCount}</strong> active / commissioning</span>
            <span className="survey-page__stat"><strong>{stats.archivalCount}</strong> completed archival</span>
            <span className="survey-page__stat"><strong>{stats.bandCount}</strong> bands incl. {BAND_LABELS_LONG.optical}, radio, X-ray</span>
            <span className="survey-page__stat"><strong>{stats.releaseCount}</strong> with release notes</span>
          </div>
        )}
      </div>

      {loading ? (
        <div style={{ color: "#64748b", textAlign: "center", padding: "3rem" }}>Loading surveys…</div>
      ) : (
        <SurveysView surveys={surveys} />
      )}
    </div>
  );
}
