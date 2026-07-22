type PaperVideoProps = {
  videoId?: string;
  title: string;
};

export function PaperVideo({ videoId, title }: PaperVideoProps) {
  if (!videoId) return null;

  return (
    <div
      style={{
        position: "relative",
        width: "100%",
        aspectRatio: "16 / 9",
        marginTop: "0.9rem",
        overflow: "hidden",
        border: "1px solid rgba(142, 166, 199, 0.25)",
        borderRadius: "0.55rem",
        background: "#080c18",
      }}
    >
      <iframe
        src={`https://www.youtube-nocookie.com/embed/${videoId}`}
        title={`${title} explainer video`}
        loading="lazy"
        allow="clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowFullScreen
        referrerPolicy="strict-origin-when-cross-origin"
        style={{ position: "absolute", inset: 0, width: "100%", height: "100%", border: 0 }}
      />
    </div>
  );
}
