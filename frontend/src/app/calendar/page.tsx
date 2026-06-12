import { CalendarContent } from "./CalendarContent";

export default function CalendarPage() {
  return (
    <div style={{ minHeight: "100vh", background: "#0f172a", color: "#f8fafc", fontFamily: "Inter, sans-serif" }}>
      <div style={{ maxWidth: "860px", margin: "0 auto", padding: "2.5rem 1.5rem" }}>
        <CalendarContent />
      </div>
    </div>
  );
}
