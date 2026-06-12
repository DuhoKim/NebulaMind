"use client";

interface ProvenanceChipProps {
  editorAgentTier?: string;
  synthesizedDate?: string;
  versionNum?: number;
}

export default function ProvenanceChip({
  editorAgentTier,
  synthesizedDate,
  versionNum,
}: ProvenanceChipProps) {
  if (editorAgentTier !== "671B") return null;

  const tooltipLines = [
    synthesizedDate ? `Synthesized: ${synthesizedDate}` : null,
    versionNum != null ? `Version: ${versionNum}` : null,
    "Model: deepseek-r1:671b (Mac Pro)",
    "Reviewed by: Kun",
  ]
    .filter(Boolean)
    .join("\n");

  return (
    <div
      title={tooltipLines}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "0.4rem",
        padding: "0.25rem 0.6rem",
        marginBottom: "1rem",
        background: "rgba(99,102,241,0.1)",
        border: "1px solid #334155",
        borderRadius: "99px",
        fontSize: "0.72rem",
        color: "#94a3b8",
        cursor: "help",
      }}
    >
      🤖 Synthesized by 671B model
    </div>
  );
}
