"use client";

import { useEffect, useState } from "react";
import SurveysView from "@/components/surveys/SurveysView";
import { type Survey } from "@/components/surveys/constants";

export default function SurveysPage() {
  const [surveys, setSurveys] = useState<Survey[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/surveys")
      .then(r => r.ok ? r.json() : { surveys: [] })
      .then(d => { setSurveys(d.surveys ?? []); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div style={{ padding: "2rem 1.5rem" }}>
      <div style={{ marginBottom: "1.5rem" }}>
        <h1 style={{ fontSize: "clamp(1.5rem,4vw,2.25rem)", fontWeight: 700, color: "#f8fafc", marginBottom: "0.5rem" }}>
          Astronomical Surveys Directory
        </h1>
        <p style={{ color: "#94a3b8", fontSize: "1rem", lineHeight: 1.6 }}>
          {surveys.length > 0
            ? `${surveys.length} surveys catalogued — the observational facilities anchoring research on NebulaMind.`
            : "The observational facilities anchoring research on NebulaMind."}
        </p>
      </div>

      {loading ? (
        <div style={{ color: "#64748b", textAlign: "center", padding: "3rem" }}>Loading surveys…</div>
      ) : (
        <SurveysView surveys={surveys} />
      )}
    </div>
  );
}
